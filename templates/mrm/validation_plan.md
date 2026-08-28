# Model Validation Plan — {{MODEL_ID}} / {{MODEL_NAME}} (v{{MODEL_VERSION}})
- Validator: {{NAME}}, independent of development | Date: {{DATE}} | Tier: {{TIER}}
- Related: [development document](model_development_document.md) · [validation report](../validation_report.md) · [findings log](model_findings_log.csv)

Agreed before validation begins, so that scope is set by risk rather than negotiated
against findings once they appear.

## Independence

| Question | Answer |
|---|---|
| Validator's reporting line | {{...}} |
| Any role in development, selection, or approval of this model? | {{None / describe}} |
| Compensation or objectives tied to this model's deployment? | {{No / describe}} |
| Authority to require remediation before deployment | {{Yes / escalation route}} |
| Authority to recommend rejection | {{Yes / escalation route}} |

Effective challenge requires competence, incentives to challenge, and standing to be heard.
Where any is limited, record it here and escalate rather than proceeding quietly.

## Scope

Set by tier per [model_risk_tiering.md](model_risk_tiering.md).

| Area | In scope | Depth | Rationale |
|---|---|---|---|
| Conceptual soundness | {{Y/N}} | {{...}} | {{...}} |
| Data quality and lineage | {{Y/N}} | {{...}} | {{...}} |
| Feature construction and proxy risk | {{Y/N}} | {{...}} | {{...}} |
| Independent replication of results | {{Y/N}} | {{...}} | {{...}} |
| Outcome analysis / benchmarking | {{Y/N}} | {{...}} | {{...}} |
| Calibration | {{Y/N}} | {{...}} | {{...}} |
| Subgroup performance and fairness | {{Y/N}} | {{...}} | {{...}} |
| Stress and sensitivity testing | {{Y/N}} | {{...}} | {{...}} |
| Threshold and decision rule | {{Y/N}} | {{...}} | {{...}} |
| Implementation and training/serving parity | {{Y/N}} | {{...}} | {{...}} |
| Explainability and adverse action | {{Y/N}} | {{...}} | {{...}} |
| Workflow placement and use in practice | {{Y/N}} | {{...}} | {{...}} |
| Human oversight conditions | {{Y/N}} | {{...}} | {{...}} |
| Monitoring design | {{Y/N}} | {{...}} | {{...}} |
| Security and third-party controls | {{Y/N}} | {{...}} | {{...}} |
| Generative components (prompts, retrieval, grounding) | {{Y/N}} | {{...}} | {{...}} |

- Explicitly out of scope, and why: {{...}}
- Reliance placed on other functions' work (audit, security, privacy): {{...}}

## Validation beyond replication

Reproducing the developer's numbers confirms arithmetic, not soundness. The plan must also
test the model where the developer had least incentive to look.

- **Independent test data**: source={{...}}, why it is genuinely independent={{...}}
- **Independent benchmark**: challenger model or alternative approach={{...}}
- **Use as practiced**: how output is actually used in the workflow, versus how the
  development document says it is used. Method={{shadowing, case sampling, interviews}}
- **Oversight reality**: override rate, review time per case, and whether reviewers can
  articulate grounds for disagreement. Method={{...}}
- **Error catchability**: seed known-wrong outputs into review and measure whether reviewers
  catch them. If they cannot, the review step is shifting liability rather than controlling
  risk, and that is a finding regardless of how the model scores. Method={{...}}
- **Deference test**: does the interface present evidence before recommendation, and does
  acceptance require comparable effort to rejection? Method={{...}}
- **Population the developer did not test**: {{...}}
- **Adversarial and edge conditions**: {{...}}

## Acceptance criteria

Set before testing, so that a marginal result is judged against a standard rather than
explained against one.

| Criterion | Threshold | Source |
|---|---|---|
| Discrimination | {{...}} | {{config/project.yaml or policy}} |
| Calibration | {{...}} | {{...}} |
| Subgroup performance | {{...}} | {{...}} |
| Stability / drift | {{...}} | {{...}} |
| Uplift vs. human baseline | {{...}} | {{project.yaml human_baseline}} |
| Explanation faithfulness | {{...}} | {{...}} |

## Findings and severity

Findings are recorded in [model_findings_log.csv](model_findings_log.csv) with this scale:

| Severity | Meaning | Effect on approval |
|---|---|---|
| Critical | Model is not fit for its intended use | Deployment blocked |
| High | Material weakness affecting reliance | See the tier table below |
| Medium | Weakness requiring remediation | Deploy with dated remediation plan |
| Low | Improvement opportunity | Track, no deployment effect |
| Observation | No action required | Record only |

The interaction of severity and tier is set in one place — the *Open findings at
deployment* table in [model_risk_tiering.md](model_risk_tiering.md). These definitions say
what a severity means; that table says what it blocks.

## Outcome

- Possible determinations: Approve · Approve with conditions · Approve for restricted use ·
  Reject · Defer pending evidence
- Restricted use means named populations, workflow steps, or reliance levels only, recorded
  as approval conditions and enforced in the workflow, not by guidance alone.

## Logistics
- Evidence and access required from development: {{...}}
- Timeline: {{...}} | Validator effort: {{...}}
- Escalation route if scope, access, or independence is constrained: {{...}}
- Plan agreed: Validator {{NAME/DATE}} | Model owner {{NAME/DATE}} | 2LOD {{NAME/DATE}}
