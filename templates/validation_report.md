# Independent Validation Report — {{MODEL_ID}} / {{MODEL_NAME}} (v{{MODEL_VERSION}})  
Decision: {{Approve / Approve with conditions / Approve for restricted use / Reject / Defer}} | Date: {{DATE}} | Validator: {{NAME}}, independent of development.  
- Tier: {{TIER}} | Agreed scope: [validation plan](mrm/validation_plan.md) | Findings recorded in: [findings log](mrm/model_findings_log.csv)  
- Evidence reviewed: [development document](mrm/model_development_document.md) · [model card](model_card.md) · [data card](data_card.md) · [GenAI system card](genai_system_card.md) · [X-Ray](checklists/ethics_xray.md)  
  
## Scope and Conceptual Soundness  
- Use-case fit, risk tier, regulatory scope: {{...}}  
- Feature review (proxies/justification): {{...}}  
  
## Testing Evidence  
- Out-of-sample/out-of-time: {{metrics}}  
- Calibration: {{Brier, ECE}}, recalibration need={{Yes/No}}  
- Fairness: groups={{...}}, metrics={{...}}, thresholds vs. policy={{...}}  
- Stress/sensitivity: {{scenarios}}  
  
## Monitoring & Governance  
- Quality gates and triggers: {{link to config/project.yaml; e.g., ROC-AUC >= X, ECE <= Y, SPD <= Z}}  
- Drift monitoring: {{PSI/KL thresholds, dashboards, cadence}}  
- Fairness monitoring: {{metrics, review cadence, escalation paths}}  
- Change management: {{versioning (code/data/models), approvers, release checklist}}  
- Logging and audit: {{decision logs, adverse action logs, lineage, retention}}  
- Human-in-the-loop: {{criteria for manual review/override; sampling for QA}}  
- Third-party/SBOM: {{libraries, models, licenses; security scan status/links}}  
  
## Residual Risks and Conditions  
- Residual risks: {{list}}  
- Conditions to approval: {{gates to meet, mitigations, time-bound actions}}  
- Sunset/rollback criteria: {{what triggers rollback, who approves}}  
  
## Final Determination  
- Decision: {{Approve / Approve with conditions / Approve for restricted use / Reject / Defer}}  
- Where restricted: the populations, workflow steps, or reliance levels permitted: {{...}}  
- Validator signature: {{NAME/DATE}}  
- Reviewed by 2LOD: {{NAME/DATE}}  
  
This report is the validation opinion, not the approval. The decision to accept the
residual risk and deploy is recorded separately in
[model_approval_record.md](mrm/model_approval_record.md), signed by the approval authority
for the tier. A validator who also approves is not independent.  
