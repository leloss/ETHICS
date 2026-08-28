# Ongoing Monitoring Plan — {{MODEL_ID}} / {{MODEL_NAME}} (v{{MODEL_VERSION}})
- Model owner: {{NAME}} | Monitoring operated by: {{TEAM}} | Tier: {{TIER}} | Date: {{DATE}}
- Related: [tiering](model_risk_tiering.md) · [change control](change_control.md) · [`config/project.yaml`](../../config/project.yaml)

Monitoring is the control that detects the difference between the model that was approved
and the model that is running. It covers three questions, and most institutions instrument
only the first: is the model still accurate, is it still being used as approved, and are
the people around it still exercising judgment.

Thresholds marked *(automated)* are enforced by
[`config/project.yaml`](../../config/project.yaml) and fail the pipeline when breached.
The rest are reviewed on cadence by a named person.

## 1. Model performance

| Metric | Threshold | Frequency | Owner | Breach action |
|---|---|---|---|---|
| ROC-AUC / PR-AUC *(automated)* | {{...}} | {{...}} | {{...}} | {{...}} |
| Precision / recall at operating threshold *(automated)* | {{...}} | {{...}} | {{...}} | {{...}} |
| Calibration: Brier, ECE *(automated)* | {{...}} | {{...}} | {{...}} | {{...}} |
| Score distribution drift: PSI *(automated)* | {{...}} | {{...}} | {{...}} | {{...}} |
| Input feature drift | {{...}} | {{...}} | {{...}} | {{...}} |
| Prediction volume and mix | {{...}} | {{...}} | {{...}} | {{...}} |
| Missing / invalid input rate | {{...}} | {{...}} | {{...}} | {{...}} |

- Label availability lag: {{...}} — where outcomes arrive late, state the leading
  indicators used in the interim: {{...}}

## 2. Fairness and error distribution

| Metric | Threshold | Frequency | Owner | Breach action |
|---|---|---|---|---|
| Selection rate parity (SPD) *(automated)* | {{...}} | {{...}} | {{...}} | {{...}} |
| TPR / FPR gaps *(automated)* | {{...}} | {{...}} | {{...}} | {{...}} |
| Subgroup performance | {{...}} | {{...}} | {{...}} | {{...}} |
| Error-cost distribution by group | {{...}} | {{...}} | {{...}} | {{...}} |

Parity metrics answer who is selected. Error-cost distribution answers who absorbs the harm
when the model is wrong. Both are required where the consequence is material.

## 3. Use in practice

The approved model and the operating model diverge through use, not through code. These
metrics detect that divergence.

| Signal | Expected range | Frequency | Owner | Escalation |
|---|---|---|---|---|
| Override rate | {{...}} | {{...}} | {{...}} | {{Investigate above AND below range}} |
| Override-upheld rate | {{...}} | {{...}} | {{...}} | {{...}} |
| Median review time per case | {{...}} | {{...}} | {{...}} | {{...}} |
| Cases per reviewer per shift | {{...}} | {{...}} | {{...}} | {{...}} |
| Appeals volume and upheld rate | {{...}} | {{...}} | {{...}} | {{...}} |
| Complaint volume referencing the decision | {{...}} | {{...}} | {{...}} | {{...}} |
| Rework and downstream exception volume | {{...}} | {{...}} | {{...}} | {{...}} |
| Use outside approved population or workflow step | Zero | {{...}} | {{...}} | {{...}} |

An override rate falling toward zero is not agreement between human and model. It is the
signal that review has become nominal, and it is investigated on the same footing as a
performance breach.

## 4. Generative components (if applicable)

| Signal | Threshold | Frequency | Owner |
|---|---|---|---|
| Groundedness / citation accuracy | {{...}} | {{...}} | {{...}} |
| Hallucination rate on sampled outputs | {{...}} | {{...}} | {{...}} |
| Over-refusal rate | {{...}} | {{...}} | {{...}} |
| Retrieval corpus staleness | {{...}} | {{...}} | {{...}} |
| Provider model version changes | Any change notified | Continuous | {{...}} |
| Prompt injection attempts detected | {{...}} | {{...}} | {{...}} |

A provider-side model version change is a change to the system whether or not the
institution initiated it, and is assessed under [change control](change_control.md).

## 5. Thresholds, actions, and escalation

| Level | Trigger | Action | Decision rights |
|---|---|---|---|
| Green | Within all thresholds | Routine reporting | Model owner |
| Amber | Any threshold breached once, or sustained trend | Investigate, report to 2LOD, remediation plan within {{N}} days | Model owner + 2LOD |
| Red | Sustained breach, or any Critical signal | Restrict, revert, or suspend; notify committee within {{N}} days | 2LOD / committee |

- Who can suspend the model: {{NAME/ROLE}}
- Rollback procedure and last known good version: {{...}}
- Suspension does not require committee pre-approval; the committee is informed after.

## 6. Retraining

- Retraining trigger: {{scheduled cadence / drift threshold / performance breach}}
- Retraining is a change and is assessed under [change control](change_control.md) before
  release, including on scheduled cadence.
- Automatic retraining permitted? {{Yes/No}} — if yes, the guardrails that bound it and the
  approval required before the retrained model reaches production: {{...}}
- Champion/challenger arrangements: {{...}}

## 7. Reporting

| Report | Audience | Frequency | Contents |
|---|---|---|---|
| Monitoring pack | Model owner, 2LOD | {{...}} | Sections 1–4, breaches, actions |
| Exception report | 2LOD | On breach | Trigger, impact, action, owner, date |
| Aggregate model risk report | Committee | {{...}} | Portfolio view, open findings, appetite status |

- Retention period for monitoring evidence: {{...}}
- Where reports are stored: {{...}}
- Plan reviewed and agreed: Owner {{NAME/DATE}} | Validator {{NAME/DATE}} | 2LOD {{NAME/DATE}}
