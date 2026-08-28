# Model Card — {{MODEL_ID}} / {{MODEL_NAME}} (v{{MODEL_VERSION}})  
- Owners: {{TEAM}} | Email: {{CONTACT}} | Date: {{DATE}}  
- Related: [data card](data_card.md) · [GenAI system card](genai_system_card.md) (if applicable) · [adverse action card](adverse_action_card.md) · [development document](mrm/model_development_document.md) · [validation report](validation_report.md) · [X-Ray](checklists/ethics_xray.md)  
- Purpose: the summary record of what the model is and how it behaves. The reasoning behind the choices lives in the development document; this card is what a reviewer reads first.  
- Use case: {{INTENDED_USE}} | Out of scope: {{OUT_OF_SCOPE}}  
- Decision criticality/risk tier: {{TIER}} | Regulatory scope: {{REGULATIONS}}  
  
## Data  
- Sources/timeframe: {{SOURCES}}, {{DATES}}  
- Consent/legal basis: {{CONSENT_BASIS}}  
- Not used/prohibited (protected attributes, proxies): {{PROHIBITED}}  
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
- Reliance expectation: {{Advisory / Decision support / Automated with review / Automated}}  
  
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
- Incident playbooks and rollback: {{LINKS}} — see [incident management](mrm/model_incident_management.md)  
- Full monitoring design: [ongoing monitoring plan](mrm/ongoing_monitoring_plan.md)  
  
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
- Can the affected person challenge the underlying record, not only the final label, and does  
  that challenge reach someone able to reopen the factual basis? {{...}}  
- Points of choice before the decision lands: human review on request, opt-out of an  
  AI-driven channel, declining data use beyond what the service requires: {{...}}  
- Is the affected person told an AI system was involved? {{Yes/No, how}}  
- Deskilling and silent-deference risk for the staff operating it: {{...}}  
- Behavior near or outside the validated envelope, and the safety consequence for affected  
  people and staff: {{...}}  
- Social and safety impact assessment: {{link, date, author}}  
  
## Limitations and Risks  
- Known failure modes: {{...}}  
- Domain guardrails and approved uses: {{...}}  
  
## Approvals  
- Model owner sign-off (card is complete and accurate): {{NAME/DATE}}  
- Independent validation: [validation report](validation_report.md), {{NAME/DATE}}  
- Deployment approval: [approval record](mrm/model_approval_record.md), {{NAME/DATE}}  
  
Signing this card attests that the record is accurate. It is not the approval to deploy —
that decision, its conditions, and its scope live in the approval record.  
