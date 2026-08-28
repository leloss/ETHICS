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
  
## Workflow Placement  
- Action taken by the system: {{rank / suppress / recommend / route / interrupt / draft / decide}}  
- Where it sits in the process: {{step, upstream input, downstream consumer}}  
- Score-to-action rule: {{threshold or rule that converts output into consequence}}  
- Business rules and policy overlays applied after the model: {{...}}  
- What is suppressed or never surfaced to a human: {{...}}  
- Steps that remain genuinely discretionary vs. effectively mandatory under time/volume  
  pressure: {{...}}  
- Reliance expectation: {{assistive only / decision support / automated with review / automated}}  
  
## Performance (primary)  
- Metrics: ROC-AUC={{...}}, PR-AUC={{...}}, F1={{...}}, Expected loss={{...}}  
- Counter-metrics (E2): rework={{...}}, override rate={{...}}, complaints={{...}}, FN rate={{...}}  
- Human baseline (E3): current process={{...}}, its metrics={{...}}, measured how={{...}}  
- Uplift vs. that baseline: {{delta, with the population it was measured on}}  
- Net benefit (E6): gain={{...}}, cost={{...}}, burden created elsewhere={{...}},  
  prevalence of the targeted problem in the full population={{...}}  
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
  
### Explanation Pathways by Audience  
One generic explanation layer serves no audience well. State what each group receives and  
whether it lets them act.  
  
| Audience | What they receive | Sufficient to act/review/challenge? |  
|---|---|---|  
| Operator (analyst, officer, clinician) | {{reasons in domain terms, evidence, uncertainty}} | {{...}} |  
| Manager / control function | {{intended use, thresholds, blind spots, escalation triggers}} | {{...}} |  
| Executive | {{what it influences, evidence of benefit, failure modes, residual reliance}} | {{...}} |  
| Validator / audit / regulator | {{lineage, versions, change control, reconstructable pathway}} | {{...}} |  
| Affected person (customer, patient) | {{faithful reasons, route to challenge}} | {{...}} |  
  
- Where disclosure is deliberately limited (gaming or security risk): {{what, and why}}  
  
## Impact on Affected People (H5, H7)  
- Who is affected by an output being wrong, and how: {{...}}  
- Consequence of a false negative for that person: {{...}}  
- Consequence of a false positive for that person: {{...}}  
- Is that consequence borne evenly across groups? {{...}} — note that selection-rate parity  
  (SPD, TPR/FPR gaps) measures who is selected, not who absorbs the harm.  
- Appeal / correction route: {{what it is, who runs it, target turnaround}}  
- Is the affected person told an AI system was involved? {{Yes/No, how}}  
- Social impact assessment: {{link, date, author}}  
  
## Limitations and Risks  
- Known failure modes: {{...}}  
- Domain guardrails and approved uses: {{...}}  
  
## Approvals  
- Model owner sign-off: {{NAME/DATE}}  
- Independent validation: {{NAME/DATE}}  
- Business/Compliance: {{NAME/DATE}}  
