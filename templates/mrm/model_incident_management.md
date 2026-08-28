# Model Incident Management — {{MODEL_ID}} / {{MODEL_NAME}}
- Model owner: {{NAME}} | Tier: {{TIER}} | Plan version: {{...}} | Date: {{DATE}}
- Related: [monitoring plan](ongoing_monitoring_plan.md) · [change control](change_control.md) · [findings log](model_findings_log.csv) · [governance and RACI](governance_and_raci.md)

A model incident is any event where the model caused, or could have caused, an outcome the
institution would struggle to defend. Incidents are distinct from findings: a finding is a
weakness identified before it bites, an incident is one that already has.

## What counts as an incident

- Materially wrong output that reached a decision
- Sustained performance or calibration breach past the Red threshold
- Output outside the approved population, workflow step, or reliance level
- Discovery that a model has been running unregistered, unvalidated, or past its approval
- Fairness breach, or harm concentrated on a group
- Data leakage, unauthorised access, prompt injection, or adversarial manipulation
- Upstream data failure that silently changed model inputs
- Provider-side model change deployed without assessment
- Human oversight failure: review that did not occur, or occurred without the information
  or authority to be meaningful
- Affected-person harm surfaced through complaint, appeal, regulator, or media
- Near miss: any of the above caught before consequence

Near misses are logged and reviewed on the same footing as incidents. They carry the same
information at a fraction of the cost, and an institution that only records incidents that
caused harm learns exclusively from harm.

## Severity

| Severity | Definition | Notify | Initial response |
|---|---|---|---|
| **SEV1** | Harm to people, regulatory breach, or systemic wrong decisions at scale | Committee + 2LOD + Legal/Compliance immediately | Suspend or revert now, assess after |
| **SEV2** | Material wrong decisions, contained; or a control demonstrably failed | 2LOD within {{N}} hours | Restrict use pending assessment |
| **SEV3** | Localised error, correctable, no external consequence | Model owner + 2LOD next cycle | Correct and monitor |
| **Near miss** | Would have been SEV1–3 but was caught | 2LOD next cycle | Record, review the control that caught it |

Severity is set on **potential** consequence, not on what happened to occur. A SEV1 that
caused no harm through luck is still a SEV1.

## Response

1. **Contain.** Suspend, revert to last known good version, or fall back to the manual
   process. Suspension does not need committee pre-approval — see
   [governance_and_raci.md](governance_and_raci.md). Who can suspend: {{NAME/ROLE}}.
2. **Preserve evidence.** Freeze logs, model version, inputs, outputs, and configuration
   before remediating. Remediation frequently destroys the record needed to explain what
   happened. Evidence hold owner: {{NAME}}.
3. **Assess scope.** How many decisions, over what period, affecting whom.
4. **Notify.** Per the severity table, plus any regulatory notification clock.
5. **Remediate affected people.** Below — the step most often skipped.
6. **Fix.** Under [change_control.md](change_control.md); emergency changes are permitted
   and are assessed retrospectively within {{N}} business days.
7. **Review.** Post-incident review, findings raised, controls updated.

## Incident record

| Field | Value |
|---|---|
| Incident ID | {{INC-####}} |
| Model ID / version in force | {{...}} |
| Detected on / by | {{DATE}} / {{monitoring, user, complaint, audit, vendor, regulator}} |
| Detection lag: how long was it happening before detection? | {{...}} |
| Severity | {{SEV1/2/3/Near miss}} |
| Description | {{...}} |
| Decisions affected: number and period | {{...}} |
| People affected, and how | {{...}} |
| Groups disproportionately affected | {{...}} |
| Immediate containment taken / by whom / when | {{...}} |
| Evidence preserved at | {{...}} |
| Regulatory notification required | {{Y/N, which, by when, done}} |
| Root cause | {{...}} |
| Was this a known risk? Which finding or limitation covered it? | {{FND-#### / not identified}} |
| Which control should have caught it, and why it did not | {{...}} |
| Which X-Ray checkpoint does this map to | {{e.g. C2, H2, S3}} |
| Fix applied / change ID | {{CHG-####}} |
| Findings raised | {{FND-####}} |
| Closed on / by | {{...}} |

## Remediation for affected people

Fixing the model does not undo the decision it produced. Where output reached a
consequential decision:

- Affected decisions identified: {{how, and completeness}}
- Are those decisions re-decided, reversed, or left standing? {{...}}
- Rationale where decisions are left standing: {{...}}
- Are affected people informed? {{Y/N, how, when}}
- Is the appeal route open and resourced for the expected volume? {{...}}
- Redress provided: {{...}}
- Who signed off that remediation is complete: {{NAME/DATE}}

## Post-incident review

Held for every SEV1 and SEV2, and for near misses at the model owner's discretion.

- Date, attendees, chair: {{...}}
- Timeline: what happened, when, and what was known at each point: {{...}}
- Detection: could it have been detected sooner, and what would have done it? {{...}}
- Was the tier correct? Does this incident change the materiality assessment? {{...}}
- Was the approval basis still valid at the time of the incident? {{...}}
- Control changes: {{...}}
- Monitoring changes: {{new signal, new threshold, new cadence}}
- Methodology changes: does any template or policy need to change so this class of incident
  is caught earlier? {{...}}
- Findings raised with owners and dates: {{FND-####}}

The review names causes, not people. An incident process that produces blame produces
under-reporting, and under-reported incidents are the ones that recur.

## Aggregate reporting

Reported to the committee each cycle: incident count by severity and by model, repeat
causes, detection lag trend, near-miss ratio, and remediation still open. A falling
incident count with a falling near-miss ratio is usually reduced detection rather than
reduced risk.
