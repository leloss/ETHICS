# ETHICS RAI Checklist (Pre‑deploy / Periodic)  
  
Model ID: {{MODEL_ID}} | Version: {{MODEL_VERSION}} | Tier: {{TIER}} | Date: {{DATE}}  
  
Companion to the ETHICS System X-Ray (`ethics_xray.md` / `ethics_xray.csv`): this list is
the pre-deploy gate; the X-Ray is the 0-3 evidence score that produces the ATS/PTS and the
Interpretation Guidance Band. Record the X-Ray band alongside the approvals below.  
  
Both run at lifecycle stage 3 of the [MRM methodology](../mrm/README.md), before independent
validation. Findings raised here are logged in [model_findings_log.csv](../mrm/model_findings_log.csv)
so that self-assessment and validation feed one remediation queue rather than two.  
  
- Enhancing  
  - [ ] Clear problem statement, stakeholders, success metrics  
  - [ ] Failure thresholds defined BEFORE launch (what would count as not working)  
  - [ ] Human/incumbent baseline measured; uplift stated with the population used  
  - [ ] Counter-metrics tracked alongside the headline gain (rework, overrides, complaints)  
  - [ ] Burden created for other teams identified and quantified  
  - [ ] Simpler non-AI alternatives considered and compared  
  - [ ] Cost/benefit and harm analysis; expected loss or utility quantified  
  
- Transparent  
  - [ ] Model card completed  
  - [ ] Data card completed (lineage, consent, representativeness)  
  - [ ] GenAI system card completed (if LLM/RAG/agentic)  
  - [ ] Threshold selection documented and justified  
  - [ ] Workflow placement documented (what action, what converts score to consequence)  
  - [ ] Explanation pathway defined per audience, not one generic layer  
  - [ ] Decision pathway reconstructable after the fact (version, inputs, output, action)  
  
- Human-Centered  
  - [ ] HITL/override criteria defined and tested  
  - [ ] Authority: reviewers can reject/defer/escalate without penalty for disagreeing  
  - [ ] Time: workload allows the review to actually happen (cases/shift vs. review time)  
  - [ ] Evidence: reviewers get what they need to disagree, in their own domain terms  
  - [ ] Clarity: reviewers know what the system is for, and what it is not for  
  - [ ] Accepting the model output requires as much thought as rejecting it, where stakes justify it  
  - [ ] Interface sequences evidence before recommendation (H4: reduce anchoring and deference)  
  - [ ] Confidence values and generated rationale signal uncertainty honestly, not false authority  
  - [ ] Override rate, override-upheld rate, and review time monitored post-deployment  
  - [ ] Override patterns segmented by team, shift, and experience level, and connected to change control  
  - [ ] Appeal route exists for affected people; volume and upheld rate monitored  
  - [ ] Affected people can challenge the underlying record, not only the final label  
  - [ ] Points of choice before the decision lands (human review on request, opt-out of an AI channel, decline non-essential data use)  
  - [ ] Frontline staff can raise concerns safely and reach governance without routing through the model owner  
  - [ ] Deskilling and silent-deference risk assessed (H7)  
  - [ ] **When the system is wrong, can the reviewer reasonably catch it?** If no, the review step shifts liability rather than controlling risk  
  - [ ] Adverse action reason card completed; compliance reviewed  
  
- Imputable (Accountability/Auditability)  
  - [ ] Versioning: code, data, model, environment hashes recorded  
  - [ ] Decision and explanation logging enabled with retention  
  - [ ] Independent validation report completed  
  
- Credible (Quality/Robustness)  
  - [ ] OOT/OOS performance acceptable  
  - [ ] Calibration within policy (Brier/ECE)  
  - [ ] Stress/sensitivity scenarios pass acceptance  
  - [ ] Group definitions validated  
  - [ ] Parity metrics within thresholds or waivers approved  
  - [ ] Fairness monitoring plan and cadence set  
  - [ ] Error-cost distribution reviewed (who bears the harm, not only who is selected)  
  
- Secure (and Privacy)  
  - [ ] PII minimization and access controls in place  
  - [ ] SBOM generated; vulnerability scans clean or accepted  
  - [ ] GenAI guardrails (if applicable) tested (prompt injection, leakage)  
  
Approvals: Model owner {{...}} | Validator {{...}} | Compliance {{...}} | Security {{...}} | Date {{...}}  
Deployment approval is recorded separately in [model_approval_record.md](../mrm/model_approval_record.md).  
