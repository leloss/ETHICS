# Model Card — {{MODEL_NAME}} (v{{MODEL_VERSION}})  
- Owners: {{TEAM}} | Email: {{CONTACT}} | Date: {{DATE}}  
- Use case: {{INTENDED_USE}} | Out of scope: {{OUT_OF_SCOPE}}  
- Decision criticality/risk tier: {{TIER}} | Regulatory scope: {{REGULATIONS}}  
  
## Data  
- Sources/timeframe: {{SOURCES}}, {{DATES}}  
- Consent/legal basis: {{CONSENT_BASIS}}  
- Not used/prohibited: {protected attributes, proxies}: {{PROHIBITED}}  
- Representativeness/coverage: {{REPRESENTATIVENESS_SUMMARY}}  
  
## Features  
- Feature list and rationale: {{FEATURES}}  
- Preprocessing: imputation={{...}}, encoding={{...}}, scaling={{...}}  
  
## Model  
- Class/architecture: {{MODEL_TYPE}}  
- Training: CV={{...}}, seed={{...}}, hyperparams={{...}}  
- Versioning: code commit={{GIT_COMMIT}}, data hash={{DATA_HASH}}, env={{ENV_HASH}}  
  
## Performance (primary)  
- Metrics: ROC-AUC={{...}}, PR-AUC={{...}}, F1={{...}}, Expected loss={{...}}  
- Calibration: Brier={{...}}, ECE={{...}}; method (e.g., isotonic/Platt)={{...}}  
- Threshold selection: procedure={{...}}, acceptance criteria={{...}}  
  
## Fairness  
- Groups: {{GROUPS_DEF}}  
- Metrics by group: TPR parity={{...}}, FPR parity={{...}}, SPD={{...}}  
- Mitigations applied: {{MITIGATIONS}}  
- Residual trade-offs/justification: {{TRADEOFFS}}  
  
## Monitoring  
- Data drift: tests={{PSI/KL}}, triggers={{...}}  
- Performance/cali drift: {{...}}  
- Fairness drift cadence: {{...}}  
- Incident playbooks and rollback: {{LINKS}}  
  
## Explainability and Adverse Action  
- Method(s): {{SHAP/monotone/ablation}}; faithfulness tests={{...}}  
- Adverse action reason generation: {{PROCESS}}, QA and suppression rules: {{...}}  
  
## Limitations and Risks  
- Known failure modes: {{...}}  
- Domain guardrails and approved uses: {{...}}  
  
## Approvals  
- Model owner sign-off: {{NAME/DATE}}  
- Independent validation: {{NAME/DATE}}  
- Business/Compliance: {{NAME/DATE}}  
