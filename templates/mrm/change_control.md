# Change Control, Recertification, and Decommissioning — {{MODEL_ID}} / {{MODEL_NAME}}
- Model owner: {{NAME}} | Tier: {{TIER}} | Date: {{DATE}}
- Related: [tiering](model_risk_tiering.md) · [validation plan](validation_plan.md) · [monitoring plan](ongoing_monitoring_plan.md) · [findings log](model_findings_log.csv)

Models drift out of their approval through accumulated small changes, each defensible on
its own. This document defines what counts as material, what each class of change triggers,
and who decides.

## Part A — Change control

### Materiality criteria

A change is **material** if it meets any of the following. Judgment sits with the model
owner and is confirmed by the validator; where they disagree, the change is treated as
material.

- Alters the model's output distribution beyond {{...}} on a benchmark sample
- Changes the decision threshold, decision rule, or any post-model policy overlay
- Adds, removes, or redefines a feature or input source
- Changes the training population, label definition, or exclusion logic
- Changes the model class, architecture, or hyperparameters beyond retuning
- Extends use to a new population, jurisdiction, product, or workflow step
- Changes the reliance level (Advisory → Decision support → Automated with review → Automated)
- Changes prompts, prompt templates, retrieval corpus, retrieval parameters, tools, or
  decoding settings in a generative system
- Changes the base model version, including a provider-initiated update
- Changes human oversight design: who reviews, with what time, authority, or information
- Changes data retention, access scope, or the security posture of the system

### Change classes

| Class | Examples | Requires | Approval |
|---|---|---|---|
| **Major** | New model class, new population, reliance level increase, threshold change on Tier 1–2 | Full re-validation, re-tiering, X-Ray re-score | Committee |
| **Minor material** | Feature change, retraining on new data, prompt or retrieval change, provider version update | Targeted validation of affected areas, X-Ray re-score of affected pillars | 2LOD |
| **Non-material** | Infrastructure move, latency optimization, logging addition, cosmetic UI change | Regression test, parity evidence, record only | Model owner |
| **Emergency** | Fix for live harm or breach | Deploy first, full assessment within {{N}} business days | Model owner, notify 2LOD immediately |

Emergency changes are the route most often abused. Each one is reported to the committee at
the next cycle with its retrospective assessment, and a pattern of emergency changes is a
governance finding in its own right.

### Change record

| Field | Value |
|---|---|
| Change ID | {{CHG-####}} |
| Date raised / requested by | {{...}} |
| Description | {{...}} |
| Reason | {{...}} |
| Materiality assessment and class | {{...}} |
| Version before → after | {{...}} |
| Testing performed | {{...}} |
| Impact on performance, fairness, oversight | {{...}} |
| X-Ray checkpoints affected and re-scored | {{...}} |
| Validator opinion | {{...}} |
| Approved by / date | {{...}} |
| Deployed by / date | {{...}} |
| Rollback plan and last known good version | {{...}} |
| Inventory updated | {{Y/N}} |

## Part B — Periodic recertification

Recertification asks whether the original approval still holds, not whether the model still
runs. Frequency by tier is set in [model_risk_tiering.md](model_risk_tiering.md).

- Recertification date: {{DATE}} | Performed by: {{NAME}} | Period covered: {{...}}

| Question | Finding |
|---|---|
| Is intended use unchanged in practice? | {{...}} |
| Has the tier changed? | {{...}} |
| Has performance held within thresholds across the period? | {{...}} |
| Has fairness held, and has error-cost distribution shifted? | {{...}} |
| Are override rate, review time, and appeals within expected range? | {{...}} |
| Have the assumptions in the development document held? | {{...}} |
| Are documentation and cards current? | {{...}} |
| Are prior findings closed, and closed with evidence? | {{...}} |
| Have accumulated non-material changes become material in aggregate? | {{...}} |
| Does the model still beat the human baseline and the alternatives? | {{...}} |
| Is residual risk still within appetite? | {{...}} |

- Determination: {{Recertify / Recertify with conditions / Restrict / Re-validate / Retire}}
- Conditions: {{...}}
- Next recertification due: {{DATE}}
- Signed: Owner {{NAME/DATE}} | Validator {{NAME/DATE}} | 2LOD {{NAME/DATE}}

## Part C — Decommissioning

Retired models remain a risk while their outputs persist in downstream decisions, records,
and other models.

| Field | Value |
|---|---|
| Reason for retirement | {{superseded / no longer needed / failed recertification / unacceptable risk}} |
| Retirement date | {{...}} |
| Replacement model or process | {{...}} |
| Downstream consumers identified and notified | {{...}} |
| Decisions made by this model that remain in force | {{...}} |
| Treatment of those decisions | {{re-decided / left standing with rationale / flagged}} |
| Appeals in flight at retirement, and how handled | {{...}} |
| Model artifacts and code archived at | {{...}} |
| Evidence retained until | {{DATE, per retention policy}} |
| Access revoked | {{Y/N, date}} |
| Serving infrastructure decommissioned | {{Y/N, date}} |
| Inventory status updated to Retired | {{Y/N, date}} |
| Approved by | {{NAME/DATE}} |

Retention outlives retirement: a decision made by a retired model may still be challenged,
so its evidence is kept for the full retention period rather than removed with the system.
