import argparse  
import json  
from pathlib import Path  
from typing import Dict, List, Optional, Tuple, Union  
  
import numpy as np  
import pandas as pd  
import yaml  
from sklearn import metrics as skm  
    
def _as_numpy(a):  
    if isinstance(a, pd.Series):  
        return a.values  
    return np.asarray(a)  
    
def _to_binary(y, pos_label):  
    y = _as_numpy(y)  
    return (y == pos_label).astype(int)  
    
def _safe(func, default=float("nan")):  
    try:  
        return func()  
    except Exception:  
        return default  
    
def _confusion_to_df(cm: np.ndarray, labels: List) -> pd.DataFrame:  
    return pd.DataFrame(  
        cm,  
        index=[f"true_{l}" for l in labels],  
        columns=[f"pred_{l}" for l in labels],  
    )  
    
def _compute_threshold_sweep(y_true_bin: np.ndarray, y_score: np.ndarray, beta: float = 1.0) -> pd.DataFrame:  
    # Evaluate precision, recall, f1 across thresholds in [0,1]  
    thresholds = np.linspace(0.0, 1.0, 101)  
    rows = []  
    for thr in thresholds:  
        y_pred = (y_score >= thr).astype(int)  
        p = skm.precision_score(y_true_bin, y_pred, zero_division=0)  
        r = skm.recall_score(y_true_bin, y_pred, zero_division=0)  
        f = skm.fbeta_score(y_true_bin, y_pred, beta=beta, zero_division=0)  
        rows.append((thr, p, r, f))  
    return pd.DataFrame(rows, columns=["threshold", "precision", "recall", "f_beta"])  
    
def compute_binary_metrics(  
    y_true: Union[pd.Series, np.ndarray],  
    y_score: Optional[Union[pd.Series, np.ndarray]],  
    y_pred_labels: Optional[Union[pd.Series, np.ndarray]],  
    pos_label: Union[int, str] = 1,  
    thr: float = 0.5,  
    beta: float = 1.0,  
    save_curves: bool = True,  
    out_dir: Optional[Path] = None,  
) -> Tuple[Dict, Dict]:  
    # Map y_true and y_pred to 0/1 space using pos_label  
    y_true_bin = _to_binary(y_true, pos_label)  
  
    # Establish y_pred_bin  
    if y_pred_labels is not None:  
        y_pred_bin = _to_binary(y_pred_labels, pos_label)  
        mask_pred = np.ones_like(y_pred_bin, dtype=bool)  
    elif y_score is not None:  
        y_score = _as_numpy(y_score)  
        mask_pred = ~np.isnan(y_score)  
        y_pred_bin = (y_score >= thr).astype(int)  
    else:  
        raise ValueError("Either y_pred (labels) or y_score must be provided for binary metrics.")  
  
    # Valid rows for classification metrics (need y_true and y_pred)  
    mask_true = ~np.isnan(y_true_bin)  
    mask = mask_true & mask_pred  
    y_true_b = y_true_bin[mask]  
    y_pred_b = y_pred_bin[mask]  
    n_used = int(mask.sum())  
  
    # Confusion matrix  
    cm = skm.confusion_matrix(y_true_b, y_pred_b, labels=[0, 1])  
    tn, fp, fn, tp = cm.ravel()  
  
    # Core metrics  
    accuracy = skm.accuracy_score(y_true_b, y_pred_b)  
    precision = skm.precision_score(y_true_b, y_pred_b, zero_division=0)  
    recall = skm.recall_score(y_true_b, y_pred_b, zero_division=0)  # TPR  
    f1 = skm.f1_score(y_true_b, y_pred_b, zero_division=0)  
    f_beta = skm.fbeta_score(y_true_b, y_pred_b, beta=beta, zero_division=0)  
    bal_acc = skm.balanced_accuracy_score(y_true_b, y_pred_b)  
    mcc = _safe(lambda: skm.matthews_corrcoef(y_true_b, y_pred_b))  
    kappa = _safe(lambda: skm.cohen_kappa_score(y_true_b, y_pred_b))  
  
    # Derived rates  
    tpr = recall  
    fpr = fp / (fp + tn) if (fp + tn) > 0 else float("nan")  
    fnr = fn / (fn + tp) if (fn + tp) > 0 else float("nan")  
    tnr = tn / (tn + fp) if (tn + fp) > 0 else float("nan")  # specificity  
    npv = tn / (tn + fn) if (tn + fn) > 0 else float("nan")  
    ppv = precision  
    prevalence = (tp + fn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) > 0 else float("nan")  
    positive_rate = (tp + fp) / (tp + tn + fp + fn) if (tp + tn + fp + fn) > 0 else float("nan")  
  
    # Scores requiring y_score  
    roc_auc = float("nan")  
    pr_auc = float("nan")  
    brier = float("nan")  
    log_loss = float("nan")  
  
    curves = {}  
    thr_sweep_df = None  
    if y_score is not None:  
        y_score_b = _as_numpy(y_score)[mask]  
        if y_score_b.size > 0:  
            roc_auc = _safe(lambda: skm.roc_auc_score(y_true_b, y_score_b))  
            pr_auc = _safe(lambda: skm.average_precision_score(y_true_b, y_score_b))  
            brier = _safe(lambda: skm.brier_score_loss(y_true_b, y_score_b, pos_label=1))  
            # For binary, compute log_loss from probabilities of positive class  
            log_loss = _safe(lambda: skm.log_loss(y_true_b, np.vstack([1 - y_score_b, y_score_b]).T, labels=[0, 1]))  
  
            if save_curves and out_dir is not None:  
                fpr_arr, tpr_arr, roc_th = skm.roc_curve(y_true_b, y_score_b)  
                prec_arr, rec_arr, pr_th = skm.precision_recall_curve(y_true_b, y_score_b)  
                curves["roc"] = pd.DataFrame({"fpr": fpr_arr, "tpr": tpr_arr, "threshold": roc_th})  
                # precision_recall_curve returns thresholds of length n-1  
                pr_df = pd.DataFrame(  
                    {  
                        "precision": prec_arr[:-1],  
                        "recall": rec_arr[:-1],  
                        "threshold": pr_th,  
                    }  
                )  
                curves["pr"] = pr_df  
  
                thr_sweep_df = _compute_threshold_sweep(y_true_b, y_score_b, beta=beta)  
  
    # Classification report  
    cls_report = skm.classification_report(y_true_b, y_pred_b, target_names=["neg", "pos"], output_dict=True, zero_division=0)  
  
    metrics = {  
        "task": "binary",  
        "n_samples_used": n_used,  
        "threshold_used": thr,  
        "positive_class": pos_label,  
        "accuracy": accuracy,  
        "balanced_accuracy": bal_acc,  
        "precision": precision,  
        "recall": recall,  
        "specificity": tnr,  
        "fpr": fpr,  
        "fnr": fnr,  
        "ppv": ppv,  
        "npv": npv,  
        "prevalence": prevalence,  
        "positive_rate": positive_rate,  
        "f1": f1,  
        "f_beta": f_beta,  
        "roc_auc": roc_auc,  
        "pr_auc": pr_auc,  
        "brier": brier,  
        "log_loss": log_loss,  
        "mcc": mcc,  
        "kappa": kappa,  
        "tp": int(tp),  
        "tn": int(tn),  
        "fp": int(fp),  
        "fn": int(fn),  
    }  
  
    extras = {  
        "confusion_matrix": cm.tolist(),  
        "confusion_labels": [0, 1],  
        "classification_report": cls_report,  
    }  
  
    # Save curves and threshold sweep if requested  
    if save_curves and out_dir is not None:  
        if "roc" in curves:  
            curves["roc"].to_csv(out_dir / "roc_curve.csv", index=False)  
        if "pr" in curves:  
            curves["pr"].to_csv(out_dir / "pr_curve.csv", index=False)  
        if thr_sweep_df is not None:  
            thr_sweep_df.to_csv(out_dir / "threshold_metrics.csv", index=False)  
            # Best threshold by F_beta  
            best_idx = int(thr_sweep_df["f_beta"].idxmax())  
            metrics["f_beta_max"] = float(thr_sweep_df.loc[best_idx, "f_beta"])  
            metrics["threshold_at_f_beta_max"] = float(thr_sweep_df.loc[best_idx, "threshold"])  
  
    return metrics, extras  
    
def compute_multiclass_metrics(  
    y_true: Union[pd.Series, np.ndarray],  
    y_pred: Union[pd.Series, np.ndarray],  
    labels: Optional[List] = None,  
    y_proba: Optional[np.ndarray] = None,  
    average: str = "macro",  
) -> Tuple[Dict, Dict]:  
    y_true = _as_numpy(y_true)  
    y_pred = _as_numpy(y_pred)  
  
    if labels is None:  
        # Preserve order of appearance  
        labels = list(pd.unique(y_true))  
  
    # Confusion matrix  
    cm = skm.confusion_matrix(y_true, y_pred, labels=labels)  
  
    # Core metrics  
    accuracy = skm.accuracy_score(y_true, y_pred)  
    bal_acc = skm.balanced_accuracy_score(y_true, y_pred)  
    prec_macro = skm.precision_score(y_true, y_pred, average="macro", zero_division=0)  
    rec_macro = skm.recall_score(y_true, y_pred, average="macro", zero_division=0)  
    f1_macro = skm.f1_score(y_true, y_pred, average="macro", zero_division=0)  
    prec_weighted = skm.precision_score(y_true, y_pred, average="weighted", zero_division=0)  
    rec_weighted = skm.recall_score(y_true, y_pred, average="weighted", zero_division=0)  
    f1_weighted = skm.f1_score(y_true, y_pred, average="weighted", zero_division=0)  
    mcc = _safe(lambda: skm.matthews_corrcoef(y_true, y_pred))  
    kappa = _safe(lambda: skm.cohen_kappa_score(y_true, y_pred))  
  
    # Scores requiring probabilities  
    roc_auc_macro = float("nan")  
    roc_auc_weighted = float("nan")  
    log_loss = float("nan")  
  
    if y_proba is not None:  
        # Ensure shape (n_samples, n_classes)  
        y_proba = _as_numpy(y_proba)  
        if y_proba.ndim != 2 or y_proba.shape[1] != len(labels):  
            raise ValueError("y_proba must be of shape (n_samples, n_classes) matching labels length.")  
        roc_auc_macro = _safe(lambda: skm.roc_auc_score(y_true, y_proba, multi_class="ovr", average="macro", labels=labels))  
        roc_auc_weighted = _safe(lambda: skm.roc_auc_score(y_true, y_proba, multi_class="ovr", average="weighted", labels=labels))  
        log_loss = _safe(lambda: skm.log_loss(y_true, y_proba, labels=labels))  
  
    cls_report = skm.classification_report(y_true, y_pred, labels=labels, output_dict=True, zero_division=0)  
  
    metrics = {  
        "task": "multiclass",  
        "n_samples_used": int(len(y_true)),  
        "labels": [str(l) for l in labels],  
        "accuracy": accuracy,  
        "balanced_accuracy": bal_acc,  
        "precision_macro": prec_macro,  
        "recall_macro": rec_macro,  
        "f1_macro": f1_macro,  
        "precision_weighted": prec_weighted,  
        "recall_weighted": rec_weighted,  
        "f1_weighted": f1_weighted,  
        "roc_auc_macro_ovr": roc_auc_macro,  
        "roc_auc_weighted_ovr": roc_auc_weighted,  
        "log_loss": log_loss,  
        "mcc": mcc,  
        "kappa": kappa,  
    }  
  
    extras = {  
        "confusion_matrix": cm.tolist(),  
        "confusion_labels": [str(l) for l in labels],  
        "classification_report": cls_report,  
    }  
    return metrics, extras  
    
def check_acceptance_gates(summary: Dict, gates: Dict) -> List[str]:  
    """  
    gates is a dict with keys under 'metrics', e.g.:  
      acceptance_gates:  
        metrics:  
          accuracy_min: 0.8  
          f1_min: 0.7  
          log_loss_max: 0.6  
          roc_auc_min: 0.75  
    This function interprets suffix _min/_max to compare against summary[metric].  
    """  
    failures = []  
    metrics_gates = gates.get("metrics", {}) if gates else {}  
    for name, threshold in metrics_gates.items():  
        if name.endswith("_min"):  
            metric_name = name[:-4]  
            if metric_name not in summary or np.isnan(summary[metric_name]):  
                failures.append(f"Metric '{metric_name}' missing for gate '{name}'.")  
                continue  
            if summary[metric_name] < threshold:  
                failures.append(f"{metric_name} {summary[metric_name]:.3f} < {threshold} (min)")  
        elif name.endswith("_max"):  
            metric_name = name[:-4]  
            if metric_name not in summary or np.isnan(summary[metric_name]):  
                failures.append(f"Metric '{metric_name}' missing for gate '{name}'.")  
                continue  
            if summary[metric_name] > threshold:  
                failures.append(f"{metric_name} {summary[metric_name]:.3f} > {threshold} (max)")  
        else:  
            # Unknown pattern; skip  
            failures.append(f"Unsupported gate key '{name}'. Use *_min or *_max.")  
    return failures  
    
def main(cfg_path: str):  
    with open(cfg_path, "r") as f:  
        cfg = yaml.safe_load(f)  
  
    # Config settings  
    data_cfg = cfg.get("data", {})  
    model_cfg = cfg.get("model", {})  
    out_cfg = cfg.get("output", {})  
    gates = cfg.get("acceptance_gates", {})  
  
    data_path = data_cfg.get("path")  
    if not data_path:  
        raise ValueError("Config must specify data.path to a CSV file.")  
  
    label_col = data_cfg.get("label_col", "y_true")  
    score_col = data_cfg.get("score_col", "y_score")  
    pred_col = data_cfg.get("pred_col", "y_pred")  
    prob_cols = data_cfg.get("prob_cols")  # For multiclass probabilities  
  
    task = model_cfg.get("task")  # "binary" or "multiclass"; if None, infer  
    thr = float(model_cfg.get("threshold", 0.5))  
    pos_label = model_cfg.get("positive_class", 1)  
    beta = float(model_cfg.get("beta", 1.0))  
    labels_cfg = model_cfg.get("labels")  # For multiclass label order  
  
    out_dir = Path(out_cfg.get("dir", "artifacts/accuracy"))  
    save_curves = bool(out_cfg.get("save_curves", True))  
    out_dir.mkdir(parents=True, exist_ok=True)  
  
    # Load data  
    df = pd.read_csv(data_path)  
  
    if label_col not in df.columns:  
        raise ValueError(f"Label column '{label_col}' not found in data.")  
  
    y_true = df[label_col]  
  
    # Infer task if not provided  
    if task is None:  
        unique_vals = pd.unique(y_true.dropna())  
        task = "binary" if len(unique_vals) <= 2 else "multiclass"  
  
    summary = {}  
    extras = {}  
    confusion_df = None  
    cls_report = None  
  
    if task == "binary":  
        y_score = df[score_col] if score_col in df.columns else None  
        y_pred = df[pred_col] if pred_col in df.columns else None  
  
        metrics, xtra = compute_binary_metrics(  
            y_true=y_true,  
            y_score=y_score,  
            y_pred_labels=y_pred,  
            pos_label=pos_label,  
            thr=thr,  
            beta=beta,  
            save_curves=save_curves,  
            out_dir=out_dir,  
        )  
        summary.update(metrics)  
        extras.update(xtra)  
  
        # Save confusion matrix CSV  
        confusion_df = _confusion_to_df(np.array(extras["confusion_matrix"]), extras["confusion_labels"])  
        confusion_df.to_csv(out_dir / "confusion_matrix.csv")  
        # Save classification report  
        cls_report = extras.get("classification_report") or {}  
        with open(out_dir / "classification_report.json", "w") as f:  
            json.dump(cls_report, f, indent=2)  
  
    elif task == "multiclass":  
        # y_pred labels or derive from prob columns  
        if pred_col in df.columns:  
            y_pred = df[pred_col]  
        elif prob_cols and all(c in df.columns for c in prob_cols):  
            # Argmax over probability columns  
            y_proba = df[prob_cols].values  
            # Labels ordering: from config or from column names  
            if labels_cfg is not None:  
                labels = labels_cfg  
            else:  
                labels = list(range(y_proba.shape[1]))  
            y_pred = pd.Series([labels[i] for i in np.argmax(y_proba, axis=1)], index=df.index)  
        else:  
            raise ValueError("For multiclass, provide data.pred_col or data.prob_cols to derive predictions.")  
  
        # Determine labels order  
        if labels_cfg is not None:  
            labels = labels_cfg  
        else:  
            labels = list(pd.unique(y_true.dropna()))  
  
        # Optional probability matrix  
        y_proba = None  
        if prob_cols and all(c in df.columns for c in prob_cols):  
            y_proba = df[prob_cols].values  
  
        metrics, xtra = compute_multiclass_metrics(y_true=y_true, y_pred=y_pred, labels=labels, y_proba=y_proba)  
        summary.update(metrics)  
        extras.update(xtra)  
  
        # Save confusion matrix CSV  
        confusion_df = _confusion_to_df(np.array(extras["confusion_matrix"]), extras["confusion_labels"])  
        confusion_df.to_csv(out_dir / "confusion_matrix.csv")  
        # Save classification report  
        cls_report = extras.get("classification_report") or {}  
        with open(out_dir / "classification_report.json", "w") as f:  
            json.dump(cls_report, f, indent=2)  
    else:  
        raise ValueError(f"Unknown task '{task}'. Use 'binary' or 'multiclass'.")  
  
    # Save JSON summary  
    with open(out_dir / "accuracy_summary.json", "w") as f:  
        json.dump(summary, f, indent=2)  
  
    # Acceptance gates  
    failures = check_acceptance_gates(summary, gates)  
    status = "PASS" if not failures else "FAIL"  
    with open(out_dir / "accuracy_gates.txt", "w") as f:  
        f.write(status + "\n")  
        for msg in failures:  
            f.write(f"- {msg}\n")  
  
    # Print combined output  
    print(json.dumps({"status": status, "failures": failures, **summary}, indent=2))  
  
    if failures:  
        raise SystemExit(1)  
  
  
if __name__ == "__main__":  
    ap = argparse.ArgumentParser()  
    ap.add_argument("--config", default="config/accuracy_metrics.yaml", help="Path to YAML config for accuracy metrics.")  
    args = ap.parse_args()  
    main(args.config)  


"""
Example minimal config (binary):

data:
  path: data/eval.csv
  label_col: y_true
  score_col: y_score
  pred_col: y_pred
model:
  task: binary
  positive_class: 1
  threshold: 0.5
  beta: 1.0
output:
  dir: artifacts/accuracy
  save_curves: true
  acceptance_gates:
metrics:
  accuracy_min: 0.80
  f1_min: 0.70
  roc_auc_min: 0.75
  log_loss_max: 0.60

Example minimal config (multiclass):
data:
  path: data/eval.csv
  label_col: y_true
  pred_col: y_pred

Optionally, if you have per-class probabilities aligned with model.labels order:
prob_cols: [p_class0, p_class1, p_class2]

model:
  task: multiclass
  labels: [class0, class1, class2]
output:
  dir: artifacts/accuracy
acceptance_gates:
  metrics:
    accuracy_min: 0.75
    f1_macro_min: 0.65
Outputs saved:
  artifacts/accuracy/accuracy_summary.json
  artifacts/accuracy/confusion_matrix.csv
  artifacts/accuracy/classification_report.json
  artifacts/accuracy/roc_curve.csv (binary, if scores present)
  artifacts/accuracy/pr_curve.csv (binary, if scores present)
  artifacts/accuracy/threshold_metrics.csv (binary, if scores present)
  artifacts/accuracy/accuracy_gates.txt
"""
