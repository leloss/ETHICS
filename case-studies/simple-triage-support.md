# ETHICS Entry Case: Emergency Department (ED) Triage Support Tool

## Background
A regional hospital deployed a machine-learning triage support tool in its Emergency Department to help prioritize incoming patients and allocate nursing resources. The model used vitals, triage notes, and simple labs to predict short-term deterioration risk (6–24 hours).

## Problem (before ETHICS)
- Developers reported high validation accuracy (AUC ~0.88) but clinicians observed missed deteriorations and 'alarm fatigue' from many low-value alerts.
- The system produced terse risk scores with **no explanation**, so nurses didn't understand what to act on.
- No clear escalation workflow: overrides were not logged and inconsistent between shifts.
- Data access and logs included unredacted patient identifiers stored in a shared analyst workspace — a privacy concern.
- Clinicians distrusted the tool; adoption remained low despite investment.

## ETHICS (applied simply)
- **Enhancing**: Move from single-metric accuracy to clinically meaningful outcomes — sensitivity for deterioration, time-to-intervention, and clinician workload. Rebalanced thresholding to prioritize early detection (sensitivity) for high-risk patients while controlling alert volume.
- **Transparent**: Surface concise, local explanations (e.g., “Score driven by rising respiratory rate, SpO₂ drop, and increasing lactate”) using model-agnostic explainers limited to clinically relevant features.
- **Human-centered**: Integrate the tool into existing triage workflows as decision-support only; require nurse confirmation for any automated escalation and provide quick-action buttons (acknowledge, escalate, defer).
- **Imputable**: Log all model scores, inputs (hashed), clinician decisions and timestamps. Add a simple RACI map: triage nurse (decision), ED physician (override), clinical data science (model owner), compliance (auditor).
- **Credible**: Implement prospective monitoring (daily) of sensitivity/specificity and periodic clinical validation with a multidisciplinary panel. Add a small challenger model to detect drift.
- **Secure**: Apply data minimization (only necessary vitals & coded notes), encrypt logs, and remove raw identifiers from analyst environments. Implement role-based access for clinicians vs. analysts.

## Example Results (illustrative)
- Alert volume reduced 45% through threshold tuning and filtering non-actionable triggers.
- Sensitivity for 6-hour deterioration rose from 0.62 → 0.81 at operational thresholds.
- Nurse override rate decreased from 36% → 14% after adding explanations and simple workflows.
- Time from alert to bedside evaluation decreased by 22%.

## Next Steps
- Run a controlled pilot comparing outcomes (length of stay, ICU transfers) with matched controls.
- Add patient-facing communications policy for any automated messages.
- Quarterly ethical review with clinicians, data scientists, and privacy officers.
