# ETHICS RAI Checklist (Pre‑deploy / Periodic)  
  
- Enhancing value  
  - [ ] Clear problem statement, stakeholders, success metrics  
  - [ ] Cost/benefit and harm analysis; expected loss or utility quantified  
  
- Transparency  
  - [ ] Model card completed  
  - [ ] Data card completed (lineage, consent, representativeness)  
  - [ ] Threshold selection documented and justified  
  
- Humans  
  - [ ] HITL/override criteria defined and tested  
  - [ ] Adverse action reason card completed; compliance reviewed  
  
- Imputability (Accountability/Auditability)  
  - [ ] Versioning: code, data, model, environment hashes recorded  
  - [ ] Decision and explanation logging enabled with retention  
  - [ ] Independent validation report completed  
  
- Credibility (Quality/Robustness)  
  - [ ] OOT/OOS performance acceptable  
  - [ ] Calibration within policy (Brier/ECE)  
  - [ ] Stress/sensitivity scenarios pass acceptance  
  
- Security (and Privacy)  
  - [ ] PII minimization and access controls in place  
  - [ ] SBOM generated; vulnerability scans clean or accepted  
  - [ ] GenAI guardrails (if applicable) tested (prompt injection, leakage)  
  
- Fairness  
  - [ ] Group definitions validated  
  - [ ] Parity metrics within thresholds or waivers approved  
  - [ ] Fairness monitoring plan and cadence set  
  
Approvals: Owner {{...}} | IVU {{...}} | Compliance {{...}} | Security {{...}} | Date {{...}}  
