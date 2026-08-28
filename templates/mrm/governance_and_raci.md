# Model Risk Governance, Roles, and Appetite
- Institution / business unit: {{...}} | Policy owner: {{NAME}} | Version: {{...}} | Date: {{DATE}}
- Related: [MRM methodology](README.md) · [tiering](model_risk_tiering.md) · [change control](change_control.md)

## Three lines of defence

| Line | Who | Owns | Does not |
|---|---|---|---|
| First | Business owner, model developer, operations | Model risk itself: design, documentation, use, monitoring, remediation | Validate its own models |
| Second | Model risk management, compliance, and other control functions | Independent validation, effective challenge, policy, aggregate risk view, appetite monitoring | Build or approve its own challenge |
| Third | Internal audit | Assurance over whether the framework operates as designed | Perform validation on the framework's behalf |

Where the institution is too small for full separation, record the compensating
arrangement — an external validator, a rotating reviewer from another team, or committee
challenge — rather than leaving the gap unstated.

## Roles

| Role | Named | Accountable for |
|---|---|---|
| Model owner (business) | {{...}} | Fitness for purpose, correct use, monitoring, remediation, appetite compliance |
| Model developer | {{...}} | Sound construction, complete and non-selective documentation, disclosed limitations |
| Model validator | {{...}} | Effective challenge, validation opinion, findings, conditions |
| Model risk head (2LOD) | {{...}} | Policy, tier confirmation, aggregate reporting, escalation |
| Data owner | {{...}} | Data quality, lineage, permitted use, upstream change notification |
| Technology owner | {{...}} | Implementation, parity, availability, rollback |
| Security owner | {{...}} | Access, encryption, adversarial resilience, vendor security |
| Compliance | {{...}} | Regulatory interpretation, adverse action, disclosure obligations |
| Operations lead | {{...}} | Oversight conditions in practice: authority, time, evidence, clarity for reviewers |
| Model risk committee | {{...}} | Approval of Tier 1, appetite, exceptions, suspension |

Every model in the inventory carries a named person in each applicable role. A role held by
"the team" is an unowned role.

## RACI by lifecycle stage

R = responsible · A = accountable · C = consulted · I = informed

| Stage | Owner | Developer | Validator | 2LOD | Tech | Security | Compliance | Committee |
|---|---|---|---|---|---|---|---|---|
| Intake and tiering | A | C | C | R | I | I | C | I |
| Development | A | R | I | I | C | C | C | — |
| X-Ray self-assessment | A | R | I | C | C | C | C | — |
| Validation | C | C | R | A | I | C | C | I |
| Approval (Tier 1) | C | I | C | C | I | I | C | A/R |
| Approval (Tier 2–4) | C | I | C | A/R | I | I | C | I |
| Deployment | A | C | I | I | R | C | I | I |
| Monitoring | A/R | C | C | C | C | I | I | I |
| Change assessment | A/R | C | C | C | C | C | C | I |
| Recertification | C | C | R | A | I | I | C | I |
| Incident response | A | C | C | C | R | R | C | I |
| Suspension | R | I | C | A | R | I | C | I |
| Decommissioning | A/R | I | C | C | R | R | C | I |

## Model risk committee

- Members: {{...}} | Chair: {{...}} | Quorum: {{...}} | Frequency: {{...}}
- Standing agenda: new Tier 1 approvals · open Critical and High findings past due ·
  appetite breaches · emergency changes since last cycle · suspensions and restrictions ·
  models overdue for recertification · inventory completeness · aggregate risk view
- Decision rights: approve Tier 1 · set and revise appetite · grant exceptions with expiry ·
  suspend any model · require re-validation
- Minutes and decisions retained: {{where, how long}}

## Model risk appetite

Appetite is stated so that a breach is observable rather than debatable.

| Statement | Limit | Measure | Breach action |
|---|---|---|---|
| Models operating without current validation | {{0 for Tier 1–2}} | Inventory | {{...}} |
| Tier 1–2 models with open Critical findings | {{0}} | Findings log | Suspend or restrict |
| Findings past remediation date | {{≤ N}} | Findings log | Committee escalation |
| Models past recertification date | {{≤ N}} | Inventory | {{...}} |
| Unregistered models discovered | {{0}} | Discovery review | Register and tier within {{N}} days |
| Fully automated decisions on Tier 1 populations | {{...}} | Inventory | {{...}} |
| Aggregate exposure to a single vendor model | {{...}} | Inventory | {{...}} |
| Models deployed below their minimum X-Ray band | {{0}} | X-Ray reports | {{...}} |

- Appetite set by: {{...}} | Reviewed: {{frequency}}
- Exceptions: granted by {{...}}, time-bound to {{max duration}}, recorded with rationale,
  compensating controls, and expiry. Exceptions that are renewed twice are escalated as a
  standing appetite question rather than renewed a third time.

## Policy requirements

- Every model in scope is registered in [model_inventory.csv](model_inventory.csv) before
  it influences a decision.
- No Tier 1–2 model is deployed without independent validation and a recorded approval.
- No model operates outside its documented intended use; extension of use is a material
  change.
- Every model has a named business owner and a named technical owner at all times; role
  changes are recorded within {{N}} days.
- Monitoring evidence is retained for {{period}}; decision and explanation logs for
  {{period}}, aligned to the longest applicable regulatory requirement.
- Any person may raise a model risk concern to the second line without routing through the
  model owner. Route: {{...}}

## Framework assurance

- Internal audit review of the framework: frequency={{...}}, last performed={{DATE}}
- Model discovery exercise to find unregistered models: frequency={{...}}, method={{...}}
- Validation quality review (are validations finding what they should?): {{...}}
- Policy review and approval: {{owner, frequency, approver}}
