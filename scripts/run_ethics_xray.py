"""Score a completed ETHICS AI System X-Ray.

Reads a filled-in checkpoint CSV (see templates/checklists/ethics_xray.csv), computes the
Absolute Total Score (ATS), Percentage Total Score (PTS), per-pillar breakdown, and the
Interpretation Guidance Band (IGB) with its Recommended Action (RA), then writes a JSON
summary and a Markdown report to the reports directory.
"""

import argparse
import json
from pathlib import Path

import pandas as pd

MAX_SCORE = 3
PILLAR_ORDER = [
    "Enhancing",
    "Transparent",
    "Human-Centered",
    "Imputable",
    "Credible",
    "Secure",
]

# (band, lower bound inclusive, upper bound inclusive, recommended action)
BANDS = [
    (
        "Strong",
        85.0,
        100.0,
        "Maintain good practices with quarterly reviews, continuous red-teaming, and "
        "upkeep of model inventory and SBOM.",
    ),
    (
        "Acceptable",
        65.0,
        84.0,
        "Close minor gaps, increase cadence of monitoring and fairness checks, and "
        "conduct targeted adversarial and stress testing.",
    ),
    (
        "Deficient",
        40.0,
        64.0,
        "Add missing documentation, enable native auditability, deploy essential "
        "monitoring, and schedule a re-assessment.",
    ),
    (
        "Weak",
        0.0,
        39.0,
        "Apply stop-gap controls, restrict or pause outputs, require independent "
        "validation and security review, and assign dedicated remediation resources.",
    ),
]


def band_for(pts):
    """Return (band, recommended_action) for a percentage total score."""
    for name, low, high, action in BANDS:
        if low <= pts <= high:
            return name, action
    # Bands are contiguous on 0-100 except for the sub-percent gaps between them
    # (e.g. 84.5); fall back to the nearest lower band.
    for name, low, _high, action in BANDS:
        if pts >= low:
            return name, action
    return BANDS[-1][0], BANDS[-1][3]


def load_xray(path):
    df = pd.read_csv(path)
    required = {"checkpoint_id", "pillar", "aspect", "score"}
    missing = required - set(df.columns)
    if missing:
        raise SystemExit(f"X-Ray CSV missing required columns: {sorted(missing)}")

    df["score"] = pd.to_numeric(df["score"], errors="coerce")

    unscored = df[df["score"].isna()]["checkpoint_id"].tolist()
    if unscored:
        raise SystemExit(
            "Unscored checkpoints (each must be 0-3 to produce a defensible ATS): "
            + ", ".join(map(str, unscored))
        )

    out_of_range = df[(df["score"] < 0) | (df["score"] > MAX_SCORE)]["checkpoint_id"].tolist()
    if out_of_range:
        raise SystemExit(f"Scores outside 0-{MAX_SCORE}: {', '.join(map(str, out_of_range))}")

    return df


def summarize(df):
    ats = int(df["score"].sum())
    ats_max = int(len(df) * MAX_SCORE)
    pts = round(100.0 * ats / ats_max, 1) if ats_max else 0.0
    igb, ra = band_for(pts)

    pillars = {}
    for pillar, grp in df.groupby("pillar", sort=False):
        p_ats = int(grp["score"].sum())
        p_max = int(len(grp) * MAX_SCORE)
        p_pts = round(100.0 * p_ats / p_max, 1) if p_max else 0.0
        p_igb, _ = band_for(p_pts)
        pillars[pillar] = {
            "ats": p_ats,
            "ats_max": p_max,
            "pts": p_pts,
            "igb": p_igb,
            "checkpoints": len(grp),
        }

    # Present pillars in canonical ETHICS order, then any custom pillars added locally.
    ordered = {p: pillars[p] for p in PILLAR_ORDER if p in pillars}
    ordered.update({p: v for p, v in pillars.items() if p not in ordered})

    gaps = [
        {
            "checkpoint_id": r["checkpoint_id"],
            "pillar": r["pillar"],
            "aspect": r["aspect"],
            "score": int(r["score"]),
        }
        for _, r in df[df["score"] <= 1].sort_values("score").iterrows()
    ]

    return {
        "ats": ats,
        "ats_max": ats_max,
        "pts": pts,
        "igb": igb,
        "recommended_action": ra,
        "pillars": ordered,
        "priority_gaps": gaps,
    }


def write_markdown(summary, path):
    lines = [
        "# ETHICS AI System X-Ray — Result",
        "",
        f"- **Absolute Total Score (ATS):** {summary['ats']} / {summary['ats_max']}",
        f"- **Percentage Total Score (PTS):** {summary['pts']}%",
        f"- **Interpretation Guidance Band (IGB):** {summary['igb']}",
        f"- **Recommended Action (RA):** {summary['recommended_action']}",
        "",
        "## Per-pillar breakdown",
        "",
        "| Pillar | ATS | PTS | Band |",
        "|---|---|---|---|",
    ]
    for pillar, v in summary["pillars"].items():
        lines.append(f"| {pillar} | {v['ats']}/{v['ats_max']} | {v['pts']}% | {v['igb']} |")

    lines += ["", "## Priority gaps (scored 0 or 1)", ""]
    if summary["priority_gaps"]:
        lines += ["| ID | Pillar | Checkpoint | Score |", "|---|---|---|---|"]
        for g in summary["priority_gaps"]:
            lines.append(
                f"| {g['checkpoint_id']} | {g['pillar']} | {g['aspect']} | {g['score']} |"
            )
    else:
        lines.append("None — no checkpoint scored below 2.")

    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main(xray_path, out_dir, min_pts, min_pillar_pts):
    df = load_xray(xray_path)
    summary = summarize(df)

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "ethics_xray_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    write_markdown(summary, out_dir / "ethics_xray.md")

    failures = []
    if min_pts is not None and summary["pts"] < min_pts:
        failures.append(f"PTS {summary['pts']}% < required {min_pts}%")
    if min_pillar_pts is not None:
        for pillar, v in summary["pillars"].items():
            if v["pts"] < min_pillar_pts:
                failures.append(f"{pillar} PTS {v['pts']}% < required {min_pillar_pts}%")

    status = "PASS" if not failures else "FAIL"
    print(json.dumps({"status": status, "failures": failures, **summary}, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--xray", default="templates/checklists/ethics_xray.csv")
    ap.add_argument("--out-dir", default="reports")
    ap.add_argument(
        "--min-pts",
        type=float,
        default=None,
        help="Fail if the overall Percentage Total Score is below this value.",
    )
    ap.add_argument(
        "--min-pillar-pts",
        type=float,
        default=None,
        help="Fail if any single pillar's Percentage Total Score is below this value.",
    )
    args = ap.parse_args()
    main(args.xray, args.out_dir, args.min_pts, args.min_pillar_pts)
