# ETHICS Entry Case — Simple Loan Pre-Screening for a Community Bank

## Background
A community bank wants to speed up small personal loan pre-screening to reduce customer wait times. A lightweight ML model (logistic regression) flags likely-approvable applicants so officers can fast-track cases.

## Problem (before ETHICS)
- Model reported 86% accuracy in development but produced unclear errors in production.
- Officers lacked explanations and often disagreed with automated fast-tracks.
- Fairness concerns emerged: lower-income applicants saw 8 percentage points higher false-decline rates.
- No audit trail for overrides; compliance worried about explainability for adverse-action notices.

## ETHICS (applied simply)
- **Enhancing**: Replace single accuracy target with operational metrics — approval yield, false-decline rate, and average processing time. Set a conservative threshold to limit portfolio EL impact.
- **Transparent**: Provide a one-line reason for each automated decision (top contributing features) and a short model card for officers.
- **Human-centered**: Keep officers in control — automated fast-track only recommends, officer must confirm; capture officer rationale when overriding.
- **Imputable**: Log inputs, model score, recommended action, officer decision, and timestamp for every case.
- **Credible**: Monitor AUC and calibration monthly; run simple fairness checks (compare TPR across income quartiles).
- **Secure**: Limit model access to authorized staff and avoid sending raw PII to external services.

## Example Results (simple, illustrative)
- Processing time for fast-tracked cases: **48 → 24 hours** (−50%).
- False-decline rate (lower-income group): **+8 pp → +2 pp** after thresholding and small bias mitigation.
- Officer override rate reduced from **27% → 12%** after adding short explanations.

## Next Steps
- Publish the model card to internal policy owners.
- Add quarterly fairness and EL reporting to the risk dashboard.
- Keep a simple “challenge” process so any officer can request a model review.
