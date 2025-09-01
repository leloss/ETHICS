# ETHICS Entry Case — Fraud Alert Triage for a Retail Bank

## Background
A retail bank receives thousands of transaction alerts daily from a rule-based fraud system. Analysts must triage and investigate; capacity is limited. The team pilots a lightweight machine-learned triage score to prioritize alerts.

## Problem (before ETHICS)
- High alert volume with low signal: analysts reported ~82% of alerts as false positives.
- No transparency on why some alerts are prioritized.
- No clear SLA for reviewer response time; escalation was ad hoc.
- Security concern: enrichment calls to a third-party API exposed masked PAN fragments.

## ETHICS (applied simply)
- **Enhancing**: Re-rank alerts by estimated precision at top-K (prioritize alerts with highest probability of true fraud). Define a target: top 10% prioritized alerts should contain ≥60% of true frauds.
- **Transparent**: Surface the top 3 features driving the triage score for each alert (e.g., velocity, merchant risk, geo mismatch).
- **Human-centered**: Design compact analyst queues (max 50 items) and add quick actions for common outcomes (escalate, close, hold).
- **Imputable**: Keep immutable logs of alert data, inputs to enrichment, triage score, analyst action, and resolution code.
- **Credible**: Track precision@K, recall@K, and reviewer agreement (simple κ) weekly.
- **Secure**: Ensure enrichment calls use tokenized identifiers and require an allowlist of approved vendors.

## Example Results (simple, illustrative)
- Analyst time on low-value alerts reduced **by 55%**, enabling focus on high-value investigations.
- Precision@Top10% improved from **22% → 61%** after model tuning and thresholding.
- Security posture: third-party tokenization rolled out, reducing PII exposure on enrichment calls.

## Next Steps
- Automate weekly precision@K reporting to fraud ops dashboard.
- Run monthly spot-checks (golden alerts) to detect drift.
- Formalize vendor data sharing agreements and technical controls.
