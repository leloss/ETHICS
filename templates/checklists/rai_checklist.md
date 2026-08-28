# ETHICS RAI Checklist (Pre‑deploy / Periodic)  
  
Companion to the ETHICS AI System X-Ray (`ethics_xray.md` / `ethics_xray.csv`): this list is
the pre-deploy gate; the X-Ray is the 0-3 evidence score that produces the ATS/PTS and the
Interpretation Guidance Band. Record the X-Ray band alongside the approvals below.  
  
- Enhancing  
  - [ ] Clear problem statement, stakeholders, success metrics  
  - [ ] Cost/benefit and harm analysis; expected loss or utility quantified  
  
- Transparent  
  - [ ] Model card completed  
  - [ ] Data card completed (lineage, consent, representativeness)  
  - [ ] Threshold selection documented and justified  
  
- Human-Centered  
  - [ ] HITL/override criteria defined and tested  
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
  
- Secure (and Privacy)  
  - [ ] PII minimization and access controls in place  
  - [ ] SBOM generated; vulnerability scans clean or accepted  
  - [ ] GenAI guardrails (if applicable) tested (prompt injection, leakage)  
  
Approvals: Owner {{...}} | IVU {{...}} | Compliance {{...}} | Security {{...}} | Date {{...}}  
