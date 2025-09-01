# Independent Validation Report — {{MODEL_NAME}} (v{{MODEL_VERSION}})  
Decision: {{Approve/Approve with conditions/Reject}} | Date: {{DATE}} | Validator: {{NAME}}, Independent of dev.  
  
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
- Decision: {{Approve/Approve with conditions/Reject}}  
- Validator signature: {{NAME/DATE}}  
- Business/Compliance sign-off: {{NAMES/DATES}}  
