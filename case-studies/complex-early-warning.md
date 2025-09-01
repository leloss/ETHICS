# ETHICS Case Study — Sepsis Early Warning System (EWS) at a 12-Hospital Health System

## Overview

A regional health system operating **12 hospitals (total 4,200 beds)** deployed a vendor-supplied machine-learning **Sepsis Early Warning System (EWS)** into electronic health records (EHR) to accelerate recognition and treatment of sepsis. The vendor’s datasheet reported strong performance (AUC 0.89) and low alarm rates; the solution was rolled out in “assistive” mode across EDs and wards to reduce time-to-antibiotics and improve outcomes.

After 9 months of operation, clinicians and quality teams reported systemic problems. The hospital adopted the **ETHICS** framework to diagnose, govern, and remediate the deployment.

---

## Problems observed (pre-ETHICS)

### Operational & clinical performance
- Realized model performance on local data: **AUC = 0.72** (vendor claim 0.89).  
- At the operational threshold selected by the vendor:  
  - **Sensitivity = 0.60**, **Specificity = 0.85**.  
  - **Alert rate = 25 alerts per 100 admissions** (target ≤ 8/100 to avoid fatigue).  
- Median **time-to-first-antibiotic** after sepsis onset: **3.8 hours** (goal <1 hour).  
- In-hospital **sepsis mortality** among flagged patients: **18.2%**.  
- Alert fatigue: clinicians reported ignoring **~40% of alerts**.  
- High false-alarm burden consumed **~1.6 FTE nurses** worth of review time weekly.

### Fairness & bias
- Subgroup performance disparities: sensitivity for Black patients = **0.52**, White patients = **0.63** (Δ = 11 pp).  
- Older patients (>75) had higher false-negative rates compared with middle-aged cohort (sensitivity 0.49 vs 0.62).

### Explainability & traceability
- Alerts displayed only a score and a short text “Sepsis risk elevated”; no feature-level explanation or provenance.  
- No immutable audit trail linking which EHR fields triggered an alert, which prevented post-hoc RCA and regulatory auditability.

### Governance & clinical workflow
- No local validation / acceptance criteria; deployment used vendor thresholds without hospital risk-committee review.  
- No designated RACI (who owns model performance monitoring, threshold adjustments, escalation rules).

### Security & privacy
- Vendor ingested PHI into US-hosted cloud service. Internal review found **unredacted timestamps and patient identifiers** stored in vendor logs accessible by vendor analysts — potential HIPAA exposure.  
- No business assurance that data residency policies met patient consent terms for certain jurisdictions within the health system.

---

## ETHICS remediations (what the team did)

The multi-disciplinary remediation program (Clinical Ops, Data Science, IT, Legal, Privacy, and Quality) applied ETHICS pillars with an intensive 6-month program:

### Enhancing (Improve clinical utility)
- **Local re-validation**: retrained a local LightGBM ensemble on multi-hospital EHR data (2016–2019) and validated on holdout 2020 data and a silent prospective pilot (Q1).  
- **Operational objective**: maximize early detection (sensitivity) subject to EL (clinical burden) and clinician workload constraints. Target set by cross-functional committee: **sensitivity ≥ 0.80** at an alert rate ≤ **9/100 admissions**.
- **Thresholding policy**: dynamic thresholds by unit (ED vs ward) and by acuity band to optimize resource use.

### Transparent (explainable & documented)
- **Per-alert explanations**: integrated SHAP summaries (top 3 contributing features with direction and magnitude) into the alert card (e.g., rising lactate +1.2, systolic BP drop −0.8, HR trend +0.6).  
- **Model cards & data cards**: published to the clinical governance portal, documenting training data timeframe, population shifts, performance per subpopulation, and known limitations.

### Human-centered (fit into clinician workflow)
- **HITL escalation**: top **5% most uncertain alerts** (closest to threshold) routed to a rapid-response nurse reviewer for confirmation prior to activating sepsis bundles.  
- **Actionable alert design**: alerts now contained next steps (e.g., “Order lactate and blood cultures; consider 1st dose IV antibiotic within 1 hour”) and links to relevant order sets.

### Imputable (auditability & ownership)
- **Immutable logging**: stored event logs (input features hash, model version, threshold, SHAP contributions, action taken, timestamp) in the hospital’s secure log store with 7-year retention for audits.  
- **RACI map**: clarified ownership — Clinical Ops (owner of thresholds), Data Science (model maintenance), IT (deployment), Compliance (audit), optionally escalating to Board-level if EL gates breached.

### Credible (robustness, fairness & monitoring)
- **Bias mitigation**: identified causes of subgroup gaps (missing vitals documented less frequently in certain wards and demographic groups). Implemented feature-augmentation and reweighting so sensitivity differences ≤ **3 pp** across race/age cohorts.  
- **Monitoring**: real-time dashboards for AUC, sensitivity, specificity, ECE (expected calibration error), per-subgroup metrics, and alert volumes. Alarms trigger when drop >5 pp or subgroup gaps exceed thresholds.

### Secure (privacy & data controls)
- **On-prem inference for PHI**: moved inference pipelines and logs into the health system’s private cloud; vendor only receives hashed identifiers and aggregated metrics.  
- **Data-use agreements** revised** with the vendor to enforce EU/State data residency, limited access, and mandatory incident notification clauses.

---

## Results (post-ETHICS, measured at 6 months)

> Note: all numbers are from the health system’s QA dashboards and prospective pilot.

### Core performance
- **AUC (local retrained model)**: **0.88** (pre-ETHICS realized 0.72).  
- **Operational threshold results (ward/ED combined)**:  
  - **Sensitivity = 0.82** (target ≥ 0.80).  
  - **Specificity = 0.78**.  
- **Alert rate**: **9 alerts per 100 admissions** (down from 25/100).  
- **False alarm reduction**: clinician-verified false-alarm fraction fell from **~72% → 28%** per reviewed alerts.

### Clinical outcomes & workflow
- **Median time-to-first-antibiotic** for true sepsis cases: **3.8 h → 1.2 h** (median reduction 2.6 h).  
- **In-hospital sepsis mortality** among cases detected: **18.2% → 13.0%** (absolute reduction 5.2 pp; relative reduction ~28.6%).  
- **Number of nurse-FTEs freed** from manual alert triage: estimated **1.5 FTE** reallocated to bedside care.

### Fairness & calibration
- Race subgroup sensitivity gap: **Black vs White** reduced from **Δ = 11 pp → Δ = 2 pp**.  
- ECE (10 bins): **6.5% → 1.9%** (better calibration so probabilities are more reliable).

### Governance & trust
- Clinician acceptance (survey): “I find alerts useful” increased from **34% → 79%**.  
- Time to root-cause an alert (audit trace): **>3 days** (pre) → **<30 minutes** (post with immutable logs).

### Security & compliance
- PHI exposure incidents: **1 confirmed** pre-ETHICS (minor breach) → **0 incidents** post-ETHICS.  
- HIPAA/State audits: no findings after migration to on-prem inference and revised DUAs.

---

## Lessons & Considerations

- **Local validation is essential**: vendor metrics rarely translate directly—local data distribution, documentation practices, and workflows matter.  
- **Tradeoffs are inevitable**: raising sensitivity required accepting a moderate specificity drop; ETHICS centered the tradeoff around clinical goals and operational capacity.  
- **Explainability and audit logs** are non-negotiable for clinical deployments: they enabled clinicians to trust and act on alerts.  
- **Equity monitoring** must be baked into performance gates; missing documentation biases were a root cause of subgroup gaps.  
- **Data residency and privacy** require explicit architectural controls when vendors are involved.

---

## Appendix — Monitoring thresholds & gates used in the program

- **Gate A (safety/clinical EL)**: trigger committee review if sensitivity < 0.78 or alert rate > 12/100 admissions.  
- **Gate B (fairness)**: trigger mitigation workflow if subgroup sensitivity gap > 5 pp.  
- **Gate C (calibration)**: ECE > 3% triggers recalibration and retraining.  
- **HITL policy**: top 5% most uncertain alerts routed to nurse reviewer; >2 consecutive divergent reviewer decisions triggers model audit.
