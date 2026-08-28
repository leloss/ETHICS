# ML Model Risk Management (MRM) Methodology

A model risk management methodology for machine learning and AI systems, structured on the
three elements of SR 11-7 / OCC 2011-12 and extended for the failure modes that classical
model risk frameworks were not written to address: drift, retraining, learned bias,
non-deterministic generative output, and workflows where a human is nominally in control.

**Model risk** is the potential for adverse consequences from decisions based on incorrect
or misused model output. It arises two ways: the model may be wrong, or the model may be
right and used wrongly. Both are in scope here.

> **Small team, or a low-tier model?** Start with [`mrm_lite.md`](mrm_lite.md) — one page
> covering the governance that prevents most harm, with explicit triggers for when to move
> up to the full set. The depth below is proportionate to Tier 1 and 2 models; applying it
> everywhere is how frameworks get abandoned.

## Scope: what counts as a model

A model is any quantitative method that applies statistical, economic, financial, or
mathematical theory, techniques, or assumptions to process input data into output that
informs a decision. Under this methodology that explicitly includes:

- Supervised, unsupervised, and reinforcement learning systems
- Rules engines and deterministic scorecards where thresholds drive consequential action
- Large language models, retrieval-augmented systems, and agentic pipelines
- Vendor and third-party models, including those embedded in purchased platforms
- Material spreadsheets and analytical tools that shape regulated decisions

If output influences a decision the institution must be able to justify, it is in scope.
Systems are classified in the inventory as **model** or **non-model tool**; the
classification decision itself is recorded and owned, because scope exclusion is the most
common way institutions lose sight of model risk.

## The three elements

### 1. Development, implementation, and use
Sound design, defensible data, documented assumptions, testing appropriate to the
consequence, and controlled deployment. Covered by
[`model_development_document.md`](model_development_document.md), plus
[`../model_card.md`](../model_card.md), [`../data_card.md`](../data_card.md), and
[`../genai_system_card.md`](../genai_system_card.md).

### 2. Validation
Effective challenge by parties independent of development, with authority and standing to
influence the outcome. Covered by [`validation_plan.md`](validation_plan.md),
[`../validation_report.md`](../validation_report.md), and
[`model_findings_log.csv`](model_findings_log.csv).

### 3. Governance, policies, and controls
Ownership, approval rights, inventory completeness, risk appetite, change control,
monitoring, and escalation. Covered by
[`governance_and_raci.md`](governance_and_raci.md),
[`model_inventory.csv`](model_inventory.csv),
[`model_risk_tiering.md`](model_risk_tiering.md),
[`ongoing_monitoring_plan.md`](ongoing_monitoring_plan.md),
[`model_approval_record.md`](model_approval_record.md),
[`model_incident_management.md`](model_incident_management.md), and
[`change_control.md`](change_control.md).

## Lifecycle

Each stage names the artifact that must exist before the stage can close. Stages 1–6 run
in order; stages 7, 8, and 10 are event-driven; stage 9 is periodic.

| Stage | Gate question | Artifact | Owner |
|---|---|---|---|
| 1. Intake | Is this a model, and how material? | Inventory entry + [tiering](model_risk_tiering.md) | Business owner |
| 2. Development | Is it conceptually sound and defensibly built? | [Development document](model_development_document.md), model/data/GenAI cards | Model developer |
| 3. Pre-validation self-assessment | Would this survive challenge? | [ETHICS System X-Ray](../checklists/ethics_xray.md) + [RAI checklist](../checklists/rai_checklist.md) | Joint |
| 4. Validation | Does it withstand effective challenge? | [Validation plan](validation_plan.md) → [validation report](../validation_report.md) → [findings log](model_findings_log.csv) | Independent validator |
| 5. Approval | Is residual risk within appetite? | [Approval record](model_approval_record.md) | Approver per [RACI](governance_and_raci.md) |
| 6. Production use | Is it still performing and still used as approved? | [Monitoring plan](ongoing_monitoring_plan.md), monitoring reports | Model owner |
| 7. Change | Is this change material, and does it require re-validation? | [Change control record](change_control.md) | Model owner + validator |
| 8. Incident | Did something go wrong, and who is put right? | [Incident record](model_incident_management.md) | Model owner + 2LOD |
| 9. Periodic review | Does approval still hold? | Re-tiering + recertification | Validator |
| 10. Decommissioning | Is retirement clean and evidenced? | [Decommissioning record](change_control.md) | Model owner |

Third-party models enter at stage 1 and run
[`third_party_model_due_diligence.md`](third_party_model_due_diligence.md) alongside
stages 2–4, since the institution cannot delegate its own accountability to a vendor.

## Proportionality

Controls scale with tier. A Tier 1 model carries full independent validation, annual
recertification, and model risk committee approval. A Tier 3 model carries targeted
validation, second-line challenge, approval by the second-line head, and two-yearly
recertification, and may use [`mrm_lite.md`](mrm_lite.md) as its core record. A Tier 4
model carries peer review and Lite alone. [`model_risk_tiering.md`](model_risk_tiering.md)
is the authority on tier assignment and on the control set each tier triggers; where any
other document appears to disagree with it, that table wins. Proportionality is what
keeps the methodology usable — a framework that demands Tier 1 rigour everywhere is
abandoned everywhere.

## ETHICS ↔ SR 11-7 crosswalk

The two frameworks answer different questions and are strongest used together. MRM asks
whether the institution controls its model risk. ETHICS asks whether the system deserves to
be relied on and whether the people around it retain authority. MRM has little to say about
appeal routes, dignity, or oversight decay; ETHICS has little to say about inventory
completeness or aggregate model risk reporting.

| ETHICS pillar | SR 11-7 element | Where the frameworks meet |
|---|---|---|
| **Enhancing** | Development and use; conceptual soundness | MRM asks whether the model is fit for purpose; ETHICS asks whether it improves the outcome against a human baseline and net of burden created elsewhere |
| **Transparent** | Documentation; validation of conceptual soundness | MRM requires documentation sufficient for a third party to reconstruct; ETHICS requires explanation that lands differently for each audience |
| **Human-Centered** | Use and implementation controls | MRM addresses model misuse; ETHICS specifies the operating conditions — authority, time, evidence, clarity — under which oversight is real rather than nominal |
| **Imputable** | Governance, policies, and controls | Direct overlap: named ownership, approval rights, audit trail, change control |
| **Credible** | Validation; ongoing monitoring | Direct overlap, extended by ETHICS to subgroup performance and error-cost distribution |
| **Secure** | Implementation controls; vendor management | MRM treats security as an operational control; ETHICS treats it as a fitness condition — an insecure system is not deployable regardless of performance |

The [ETHICS System X-Ray](../checklists/ethics_xray.md) sits at lifecycle stage 3 as a
pre-validation self-assessment. It is not a substitute for independent validation: it is
completed by the people closest to the system, which makes it useful for surfacing gaps
early and unsuitable as effective challenge. A validator may use the X-Ray as an input and
should score the same checkpoints independently where they bear on the validation opinion.

## Regulatory reference points

| Reference | Relevance |
|---|---|
| SR 11-7 / OCC 2011-12 | Supervisory guidance on model risk management (US banking) |
| SS1/23 (PRA) | UK model risk management principles, explicitly covering AI/ML |
| ECB TRIM guide | Internal models, targeted review expectations |
| EU AI Act | Risk classification, high-risk system obligations, human oversight |
| NIST AI RMF | Govern / Map / Measure / Manage functions |
| ISO/IEC 23894 | AI risk management |
| ECOA / Reg B, FCRA | Adverse action reasons, credit decisioning |
| SR 15-18, SR 15-19 | Governance and controls at large financial institutions |

Mapped per control in [`../checklists/controls_map.csv`](../checklists/controls_map.csv).

## ML-specific extensions

Classical MRM assumes a model is estimated once, validated, and re-estimated on a schedule.
Machine learning breaks several of those assumptions, and this methodology adds explicit
treatment for each:

| Assumption that breaks | Extension |
|---|---|
| The model is static between releases | Drift monitoring and retraining triggers as governed controls, not maintenance activity ([monitoring plan](ongoing_monitoring_plan.md)) |
| Inputs are a stable, documented set of variables | Data lineage, feature provenance, and upstream-change notification ([`../data_card.md`](../data_card.md)) |
| Output is deterministic and reproducible | Reconstruction from stored records rather than replay; prompt, retrieval, and decoding settings as versioned components ([`../genai_system_card.md`](../genai_system_card.md)) |
| Performance is a single population statistic | Subgroup performance and error-cost distribution as first-class validation evidence |
| Errors are symmetric and priced | Per-error cost, and who bears it, recorded before approval |
| Human review is a control | Override rate, override-upheld rate, and review time monitored, because nominal oversight decays silently |
| Retraining is a technical operation | Retraining treated as a change requiring assessment against materiality criteria ([change control](change_control.md)) |

## Using this alongside the automated gates

The thresholds in [`../../config/project.yaml`](../../config/project.yaml) and
[`../../config/accuracy_metrics.yaml`](../../config/accuracy_metrics.yaml) are the
machine-enforced subset of this methodology: performance, calibration, fairness, and drift
limits that fail a build when breached. The templates here carry the judgment that cannot
be automated — materiality, conceptual soundness, effective challenge, appetite, and
approval. Gate thresholds should be set by the validator and recorded as approval
conditions, so that a config change is visible as a change to an approved control.
