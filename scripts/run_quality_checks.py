import argparse  
import json  
import os  
from pathlib import Path  
  
import numpy as np  
import pandas as pd  
import yaml  
from sklearn import metrics  
  
def ece_score(y_true, y_prob, n_bins=10):  
    y_true = np.asarray(y_true)  
    y_prob = np.asarray(y_prob)  
    bins = np.linspace(0.0, 1.0, n_bins + 1)  
    idx = np.digitize(y_prob, bins) - 1  
    ece = 0.0  
    for b in range(n_bins):  
        mask = idx == b  
        if not np.any(mask):  
            continue  
        conf = y_prob[mask].mean()  
        acc = y_true[mask].mean()  
        ece += (mask.sum() / len(y_prob)) * abs(acc - conf)  
    return float(ece)  
  
def psi(ref, cur, n_bins=10):  
    ref = np.asarray(ref)  
    cur = np.asarray(cur)  
    bins = np.linspace(0.0, 1.0, n_bins + 1)  
    r_hist, _ = np.histogram(ref, bins=bins)  
    c_hist, _ = np.histogram(cur, bins=bins)  
    r = np.clip(r_hist / max(r_hist.sum(), 1), 1e-6, 1.0)  
    c = np.clip(c_hist / max(c_hist.sum(), 1), 1e-6, 1.0)  
    return float(np.sum((r - c) * np.log(r / c)))  
  
def main(cfg_path):  
    with open(cfg_path, "r") as f:  
        cfg = yaml.safe_load(f)  
  
    eval_path = cfg["data"]["eval_path"]  
    baseline_path = cfg["data"].get("baseline_path")  
    thr = cfg["model"]["threshold"]  
    pos = cfg["model"].get("positive_class", 1)  
    gates = cfg["acceptance_gates"]  
    out_dir = Path(cfg["artifacts"]["reports_dir"])  
    out_dir.mkdir(parents=True, exist_ok=True)  
  
    df = pd.read_csv(eval_path)  
    y_true = df["y_true"].values  
    y_score = df["y_score"].values  
    y_pred = (y_score >= thr).astype(int)  
  
    # Performance  
    roc_auc = metrics.roc_auc_score(y_true, y_score)  
    try:  
        pr_auc = metrics.average_precision_score(y_true, y_score)  
    except Exception:  
        pr_auc = float("nan")  
    f1 = metrics.f1_score(y_true, y_pred, pos_label=pos)  
    coverage = 1.0 - np.mean(np.isnan(y_score))  
    brier = metrics.brier_score_loss(y_true, y_score, pos_label=pos)  
    ece = ece_score(y_true, y_score, n_bins=10)  
  
    summary = {  
        "roc_auc": roc_auc,  
        "pr_auc": pr_auc,  
        "f1": f1,  
        "coverage": coverage,  
        "brier": brier,  
        "ece": ece,  
    }  
  
    # Optional drift vs baseline  
    psi_val = None  
    if baseline_path and os.path.exists(baseline_path):  
        base = pd.read_csv(baseline_path)  
        if "y_score" in base.columns:  
            psi_val = psi(base["y_score"].values, y_score, n_bins=10)  
            summary["psi_y_score"] = psi_val  
  
    # Save JSON summary  
    with open(out_dir / "quality_summary.json", "w") as f:  
        json.dump(summary, f, indent=2)  
  
    # Acceptance gates  
    failures = []  
    perf = gates.get("performance", {})  
    cali = gates.get("calibration", {})  
    drift = gates.get("drift", {})  
  
    if "roc_auc_min" in perf and roc_auc < perf["roc_auc_min"]:  
        failures.append(f"ROC-AUC {roc_auc:.3f} < {perf['roc_auc_min']}")  
    if "pr_auc_min" in perf and not np.isnan(pr_auc) and pr_auc < perf["pr_auc_min"]:  
        failures.append(f"PR-AUC {pr_auc:.3f} < {perf['pr_auc_min']}")  
    if "f1_min" in perf and f1 < perf["f1_min"]:  
        failures.append(f"F1 {f1:.3f} < {perf['f1_min']}")  
    if "coverage_min" in perf and coverage < perf["coverage_min"]:  
        failures.append(f"Coverage {coverage:.3f} < {perf['coverage_min']}")  
  
    if "brier_max" in cali and brier > cali["brier_max"]:  
        failures.append(f"Brier {brier:.3f} > {cali['brier_max']}")  
    if "ece_max" in cali and ece > cali["ece_max"]:  
        failures.append(f"ECE {ece:.3f} > {cali['ece_max']}")  
  
    if psi_val is not None and "psi_max" in drift and psi_val > drift["psi_max"]:  
        failures.append(f"PSI {psi_val:.3f} > {drift['psi_max']}")  
  
    status = "PASS" if not failures else "FAIL"  
    with open(out_dir / "quality_gates.txt", "w") as f:  
        f.write(status + "\n")  
        for msg in failures:  
            f.write(f"- {msg}\n")  
  
    print(json.dumps({"status": status, "failures": failures, **summary}, indent=2))  
    if failures:  
        raise SystemExit(1)  
  
if __name__ == "__main__":  
    ap = argparse.ArgumentParser()  
    ap.add_argument("--config", default="config/project.yaml")  
    args = ap.parse_args()  
    main(args.config)  
