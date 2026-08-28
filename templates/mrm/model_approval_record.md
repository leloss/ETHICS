# Model Approval Record — {{MODEL_ID}} / {{MODEL_NAME}} (v{{MODEL_VERSION}})
- Approval date: {{DATE}} | Tier: {{TIER}} | Approval authority: {{per governance_and_raci.md}}
- Related: [validation report](../validation_report.md) · [tiering](model_risk_tiering.md) · [findings log](model_findings_log.csv) · [governance and appetite](governance_and_raci.md) · [monitoring plan](ongoing_monitoring_plan.md)

Validation gives an opinion on whether the model is sound. Approval is the separate,
business decision to accept the residual risk and put it into use. Keeping them apart
matters: a validator who both challenges and approves is not independent, and an approval
that merely restates the validation opinion records no decision at all.

## What is being approved

| Field | Value |
|---|---|
| Model version approved | {{...}} |
| Approved intended use, stated operationally | {{...}} |
| Approved population and jurisdictions | {{...}} |
| Approved workflow step(s) | {{...}} |
| Approved reliance level | {{Advisory / Decision support / Automated with review / Automated}} |
| Prohibited uses | {{...}} |
| Approved decision threshold and any policy overlays | {{...}} |
| Effective from / until | {{DATE}} / {{DATE or next recertification}} |

Anything not listed above is outside the approval. Extension of use is a material change
under [change_control.md](change_control.md), not a matter of local discretion.

## Basis for the decision

| Input | Reference | Summary |
|---|---|---|
| Validation opinion | [validation report](../validation_report.md) | {{Approve / with conditions / restricted / reject}} |
| Tier and residual risk | [tiering](model_risk_tiering.md) | {{tier, residual rating}} |
| ETHICS System X-Ray | [X-Ray](../checklists/ethics_xray.md) | PTS {{...}}%, band {{...}}, lowest pillar {{...}}% |
| X-Ray gate for this tier | [tiering](model_risk_tiering.md) | Overall {{Y/N}} · pillar floor {{Y/N}} · non-negotiable checkpoints {{Y/N}} |
| Band due at first recertification | [tiering](model_risk_tiering.md) | {{...}}% by {{DATE}} — tracked as a condition below |
| Open findings | [findings log](model_findings_log.csv) | Critical {{n}}, High {{n}}, Medium {{n}} |
| Benefit evidence | [`config/project.yaml`](../../config/project.yaml) | Uplift vs. human baseline: {{...}} |
| Net cost/benefit | [`config/project.yaml`](../../config/project.yaml) | {{...}} |
| Security review | {{LINK}} | {{outcome}} |
| Appetite position | [governance](governance_and_raci.md) | Within appetite? {{Y/N}} |

## Conditions of approval

Conditions are binding and tracked to closure in the findings log. An approval with
conditions that nobody tracks is an unconditional approval.

| # | Condition | Owner | Due | Findings ID | Consequence if missed |
|---|---|---|---|---|---|
| 1 | {{...}} | {{...}} | {{DATE}} | {{FND-####}} | {{restrict / suspend / escalate}} |

- Restrictions enforced in the workflow rather than by guidance alone: {{how}}
- Monitoring thresholds set as approval conditions: {{reference to project.yaml values}}
- Any change to those thresholds is a change to an approved control and requires
  {{approval level}}.

## Exceptions

Complete only if approving outside policy or appetite.

| Field | Value |
|---|---|
| What policy or appetite limit is being excepted | {{...}} |
| Why the exception is justified | {{...}} |
| Compensating controls | {{...}} |
| Expiry date (mandatory) | {{DATE}} |
| Renewal count to date | {{n}} — a second renewal is escalated as a standing appetite question |
| Granted by | {{NAME/ROLE/DATE}} |

## Dissent

Recorded so that disagreement survives the meeting. A decision taken over a documented
objection is legitimate; one that erases the objection is not.

- Objections raised, by whom, and how resolved: {{... / None recorded}}

## Decision

- **Determination:** {{Approve / Approve with conditions / Approve for restricted use / Reject / Defer}}
- Rationale, in the approver's own terms: {{...}}
- Next recertification due: {{DATE}}
- Inventory updated: {{Y/N, date}}

| Role | Name | Date | Signature/record |
|---|---|---|---|
| Approval authority | {{...}} | {{...}} | {{...}} |
| Business owner (accepts operational responsibility) | {{...}} | {{...}} | {{...}} |
| 2LOD / model risk | {{...}} | {{...}} | {{...}} |
| Compliance | {{...}} | {{...}} | {{...}} |
