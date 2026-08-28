# Artifact Index

Every artifact here carries the same `{{MODEL_ID}}`, assigned at intake and registered in
[`mrm/model_inventory.csv`](mrm/model_inventory.csv). The ID is what makes the set a record
rather than a folder: it links a monitoring breach to the validation that approved the
threshold, and a finding to the checkpoint that should have caught it.

Two layers, used together:

- **ETHICS artifacts** ask whether the system deserves to be relied on, and whether the
  people around it keep their authority.
- **MRM artifacts** ask whether the institution controls its model risk — inventory,
  materiality, effective challenge, appetite, and change.

## By lifecycle stage

| Stage | Artifact | Who produces it | Feeds |
|---|---|---|---|
| Intake | [`mrm/model_inventory.csv`](mrm/model_inventory.csv) | Business owner | Everything |
| Intake | [`mrm/model_risk_tiering.md`](mrm/model_risk_tiering.md) | Business owner + 2LOD | Control depth for all later stages |
| Development | [`mrm/model_development_document.md`](mrm/model_development_document.md) | Developer | Validation |
| Development | [`model_card.md`](model_card.md) | Developer | Validation, monitoring, review |
| Development | [`data_card.md`](data_card.md) | Data owner + developer | Validation, lineage claims |
| Development | [`genai_system_card.md`](genai_system_card.md) | Developer | Validation, change control |
| Development | [`adverse_action_card.md`](adverse_action_card.md) | Developer + compliance | Validation, affected-person disclosure |
| Self-assessment | [`checklists/ethics_xray.md`](checklists/ethics_xray.md) + [`.csv`](checklists/ethics_xray.csv) | Joint review | Band, priority gaps, findings |
| Self-assessment | [`checklists/rai_checklist.md`](checklists/rai_checklist.md) | Joint review | Pre-deploy gate |
| Validation | [`mrm/validation_plan.md`](mrm/validation_plan.md) | Validator | Scope agreed before testing |
| Validation | [`validation_report.md`](validation_report.md) | Validator | Approval decision |
| Validation | [`mrm/model_findings_log.csv`](mrm/model_findings_log.csv) | Validator | Remediation, appetite, committee |
| Approval | [`mrm/governance_and_raci.md`](mrm/governance_and_raci.md) | 2LOD / committee | Who decides, and against what appetite |
| Production | [`mrm/ongoing_monitoring_plan.md`](mrm/ongoing_monitoring_plan.md) | Model owner | Breach actions, recertification |
| Change | [`mrm/change_control.md`](mrm/change_control.md) | Model owner + validator | Re-validation, re-tiering, retirement |
| Third party | [`mrm/third_party_model_due_diligence.md`](mrm/third_party_model_due_diligence.md) | Contract owner + validator | Reliance level permitted |
| Cross-cutting | [`checklists/controls_map.csv`](checklists/controls_map.csv) | 2LOD | Regulatory crosswalk |

## Which artifacts apply

| Situation | Add |
|---|---|
| Any model in scope | Inventory entry, tiering, model card, data card, X-Ray |
| LLM, RAG, or agentic system | GenAI system card |
| Decisions affecting people's access to credit, services, or care | Adverse action card, and the model card's Impact on Affected People section |
| Vendor or embedded third-party model | Third-party due diligence |
| Tier 1 or 2 | Development document, validation plan, validation report, findings log |
| Tier 3 or 4 | Development document (short form), targeted or peer review |

Depth by tier is set in [`mrm/model_risk_tiering.md`](mrm/model_risk_tiering.md). A Tier 4
model does not need the full set; requiring it everywhere is how frameworks stop being used.

## How the pieces connect

The chain that matters most runs: **tiering → X-Ray → validation → findings → monitoring →
change → recertification**, and it closes back on itself.

- Tiering sets how much of everything else applies.
- The X-Ray is scored by the people closest to the system, which makes it useful for
  finding gaps early and unsuitable as effective challenge. It is an input to validation,
  never a substitute.
- Validation findings and X-Ray priority gaps land in one findings log, so remediation has
  a single queue and a single view of what is overdue.
- The monitoring plan instruments what validation identified as fragile; thresholds it
  automates live in [`../config/project.yaml`](../config/project.yaml) and
  [`../config/accuracy_metrics.yaml`](../config/accuracy_metrics.yaml).
- Monitoring breaches and material changes trigger re-validation and re-tiering, which
  starts the chain again at a new version.

The automated gates and these documents are the same control expressed twice. A threshold in
`project.yaml` is an approval condition; changing it is a change to an approved control, and
belongs in the change record rather than in a quiet commit.

## Filling these in

Placeholders are `{{LIKE_THIS}}`. Leave one unfilled rather than guessing — an unfilled
placeholder is visible in review, whereas a plausible guess is not. Where an item does not
apply, write "N/A" with the reason instead of deleting the row, so a reviewer can tell the
difference between considered-and-excluded and never-considered.
