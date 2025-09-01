import argparse  
import json  
from pathlib import Path  
  
import numpy as np  
import pandas as pd  
import yaml  
from fairlearn.metrics import MetricFrame, selection_rate, true_positive_rate, false_positive_rate  
  
  
def compute_metrics(df, label_col, score_col, pred_col, group_col, threshold):  
    if pred_col is None or pred_col not in df.columns:  
        df["y_pred"] = (df[score_col] >= threshold).astype(int)  
        pred_col = "y_pred"  
  
    y_true = df[label_col]  
    y_pred = df[pred_col]  
    groups = df[group_col]  
  
    mf_sel = MetricFrame(metrics=selection_rate, y_true=y_true, y_pred=y_pred, sensitive_features=groups)  
    mf_tpr = MetricFrame(metrics=true_positive_rate, y_true=y_true, y_pred=y_pred, sensitive_features=groups)  
    mf_fpr = MetricFrame(metrics=false_positive_rate, y_true=y_true, y_pred=y_pred, sensitive_features=groups)  
  
    selection_by_group = mf_sel.by_group.to_dict()  
    tpr_by_group = mf_tpr.by_group.to_dict()  
    fpr_by_group = mf_fpr.by_group.to_dict()  
  
    # Parity gaps (max absolute difference)  
    def gap(d):  
        vals = list(d.values())  
        return float(np.max(vals) - np.min(vals)) if vals else float("nan")  
  
    spd = gap(selection_by_group)  # absolute statistical parity difference  
    tpr_gap = gap(tpr_by_group)  
    fpr_gap = gap(fpr_by_group)  
  
    return {  
        "selection_rate_by_group": selection_by_group,  
        "tpr_by_group": tpr_by_group,  
        "fpr_by_group": fpr_by_group,  
        "spd_abs": spd,  
        "tpr_gap": tpr_gap,  
        "fpr_gap": fpr_gap,  
    }  
  
  
def main(fair_cfg_path, proj_cfg_path):  
    with open(fair_cfg_path, "r") as f:  
        fcfg = yaml.safe_load(f)  
    with open(proj_cfg_path, "r") as f:  
        pcfg = yaml.safe_load(f)  
  
    df = pd.read_csv(fcfg["data"]["path"])  
    label_col = fcfg["data"]["label_col"]  
    score_col = fcfg["data"]["score_col"]  
    pred_col = fcfg["data"].get("pred_col")  
    group_col = fcfg["data"]["group_col"]  
    thr = fcfg["model"]["threshold"]  
  
    out_dir = Path(fcfg["output"]["dir"])  
    out_dir.mkdir(parents=True, exist_ok=True)  
  
    res = compute_metrics(df, label_col, score_col, pred_col, group_col, thr)  
  
    with open(out_dir / "fairness_summary.json", "w") as f:  
        json.dump(res, f, indent=2)  
  
    gates = pcfg["acceptance_gates"]["fairness"]  
    failures = []  
    if "spd_abs_max" in gates and res["spd_abs"] > gates["spd_abs_max"]:  
        failures.append(f"SPD_abs {res['spd_abs']:.3f} > {gates['spd_abs_max']}")  
    if "tpr_gap_max" in gates and res["tpr_gap"] > gates["tpr_gap_max"]:  
        failures.append(f"TPR gap {res['tpr_gap']:.3f} > {gates['tpr_gap_max']}")  
    if "fpr_gap_max" in gates and res["fpr_gap"] > gates["fpr_gap_max"]:  
        failures.append(f"FPR gap {res['fpr_gap']:.3f} > {gates['fpr_gap_max']}")  
  
    # Optional: ensure coverage of expected groups  
    expected = (fcfg.get("groups") or {}).get("expected") or []  
    if expected:  
        present = set(map(str, df[group_col].unique()))  
        missing = [g for g in expected if str(g) not in present]  
        if missing:  
            failures.append(f"Missing expected groups in eval data: {missing}")  
  
    status = "PASS" if not failures else "FAIL"  
    with open(out_dir / "fairness_gates.txt", "w") as f:  
        f.write(status + "\n")  
        for msg in failures:  
            f.write(f"- {msg}\n")  
  
    print(json.dumps({"status": status, "failures": failures, **res}, indent=2))  
    if failures:  
        raise SystemExit(1)  
  
  
if __name__ == "__main__":  
    ap = argparse.ArgumentParser()  
    ap.add_argument("--fairness-config", default="config/fairness_config.yaml")  
    ap.add_argument("--project-config", default="config/project.yaml")  
    args = ap.parse_args()  
    main(args.fairness_config, args.project_config)  
