# Case Study: ETHICS in Drug Discovery — Reducing Animal Use and Addressing Animal Welfare Concerns

## Executive summary

A mid-sized pharmaceutical research company faced rising ethical, regulatory and reputational pressure over heavy reliance on animal testing in early drug discovery and preclinical safety screening. In 2019 the company used **~12,500 animals/year** across discovery and lead optimization (78% mice, 15% rats, 7% rabbits/dogs/primates for specialty studies). Internal audits and activist reporting highlighted high-severity procedures, inconsistent welfare documentation, and poor transparency to regulators and the public.

The company adopted the **ETHICS** framework as an enterprise remediation program (2019–2023) to substantially reduce animal use, improve welfare, strengthen governance, and accelerate discovery via alternative methods (in-silico, in-vitro, organoids, microphysiological systems). Over a 4-year program the company achieved a **64% reduction in animals used**, improved predictive performance of preclinical safety screening pipelines, reduced average time-to-candidate by **22%**, cut preclinical costs per candidate by **27%**, and remediated regulatory and public trust risks. This case documents problems, interventions, metrics and lessons.

---

## Background & initial state (pre-ETHICS)

**Context**
- Therapeutic focus: small-molecule oncology + metabolic disease pipeline.  
- Annual throughput (discovery → candidate nomination): ~320 compounds screened to 6 development candidates per year.  
- Pre-ETHICS approach: high-volume in vivo toxicity and PK screening early (Tier 1: single-dose mouse/rat screens; Tier 2: subchronic rodent studies; selective non-rodent studies for DMPK).

**Key pain points (measured)**
- **Animal usage**: 12,500 animals/year.  
- **Ethical incidents & complaints**: 4 formal complaints in 2018; 1 regulatory observation about incomplete IACUC protocols in a 2018 inspection.  
- **Welfare severity**: 24% of in-vivo procedures classified as moderate-to-severe under internal severity scale.  
- **Attrition & predictive failure**: 42% of candidates that passed animal safety screens failed in Phase I/II due to human toxicity or PK mismatch (late-stage attrition cost = \$18M / candidate on average).  
- **Time/cost**: median time-to-candidate = 18 months; preclinical safety spend per candidate (animals + studies) ≈ \$3.5M.  
- **Transparency & reproducibility**: only 62% of animal studies had complete SOP-led data packages; model provenance and decision rationale often missing in compound progression notes.  
- **Regulatory friction**: repeated requests for additional bridging data from regulators (FDA/EMA) due to concerns about extrapolation from rodent-only data.

**External norms & legal context cited**
- U.S. Animal Welfare Act (AWA) and Public Health Service (PHS) Policy on Humane Care and Use of Laboratory Animals.
- Institutional oversight by IACUC (Institutional Animal Care and Use Committee).
- EU Directive 2010/63/EU and OECD test guidelines (where applicable).
- Best practice guidance: ARRIVE reporting guidelines; NC3Rs 3Rs (Replacement, Reduction, Refinement).

---

## ETHICS program goals (explicit, quantified)

The company defined program-level KPIs and gates prior to remediation:
1. **Reduction target**: reduce animal use by ≥50% within 4 years while maintaining or improving predictive safety signals.  
2. **Welfare target**: reduce moderate/severe procedure proportion from 24% → ≤8%.  
3. **Predictive performance target**: develop and validate alternative pipelines with AUC ≥ 0.85 for key endpoints (hepatotoxicity, cardiotoxicity, genotoxicity) vs historical animal labels and human outcomes.  
4. **Timeline & cost**: reduce median time-to-candidate by ≥15% and preclinical cost per candidate by ≥20%.  
5. **Governance & auditability**: 100% of studies and algorithmic decision steps to have immutable audit logs; ARRIVE-compliant reports for all retained animal studies.

---

## ETHICS interventions (detailed technical & governance actions)

The program combined technical innovation, process redesign, and governance reforms mapped to the ETHICS pillars.

### Enhancing — replace/augment animal assays with predictive alternatives
- **Tiered replacement strategy**:
  - **Tier 0 (in-silico)**: QSAR + mechanistic ML toxicity models, physiologically based pharmacokinetic (PBPK) simulations, and adverse outcome pathway (AOP) mapping for early triage.  
  - **Tier 1 (in-vitro high throughput)**: hepatocyte/primary cell assays, hERG assays, 3D liver spheroids organoids, and multiplexed cytotoxicity panels.  
  - **Tier 2 (microphysiological systems, MPS)**: organ-on-chip (liver, heart) for compounds progressing to lead optimization.  
  - **Tier 3 (targeted in vivo)**: only for compounds failing all alternatives but still requiring specific systemic readouts; limited to GLP-compliant low-severity studies.
- **Results (numbers)**:
  - Of 320 screened compounds/year, **~210 (66%)** were triaged out using Tier 0–1 (in-silico/in-vitro) without any animal testing.  
  - For 90 compounds advancing beyond Tier 1, MPS testing replaced planned rodent ADME/tox studies for 58 compounds.  
  - Animal studies required dropped from 12,500 → **8,200/year** in Year 1, then to **6,400** (Year 2) and **5,200** (Year 3), reaching **4,500** by Year 4 as models matured (cumulative 64% reduction).
- **Predictive metrics**:
  - Retrospective benchmarking: in-silico + in-vitro ensemble predicting rodent acute hepatotoxicity showed **AUC = 0.86**, PPV = 0.78, NPV = 0.82 against historical animal outcomes.
  - More importantly, for human adverse events (Phase I/II toxicity endpoints) the ensemble achieved **AUC = 0.81**, improving hit-rate for early toxicity detection and reducing late-stage attrition forecast by **~30%**.

### Transparent — make models, evidence, and decisions visible
- **Model and data cards**: every in-silico model and MPS protocol documented with training data provenance, validation cohorts, applicability domain and known failure modes.
- **Decision bundles**: compound progression now requires a structured “evidence bundle” (in-silico scores, in-vitro readouts, MPS reports) attached to the nomination package; regulatory-grade exportable PDFs produced for agency review.
- **Explainability**: SHAP/LIME and rule-based trace outputs used for each compound to show which features (metabolism liability, reactive metabolite score, off-target binding) drove a toxicity prediction.

### Human-Centered — researcher and animal welfare staff engagement
- **Cross-functional panels** (chemistry, DMPK, toxicology, ethics, animal welfare) for each candidate decision to ensure human judgment complements model signals.
- **Welfare-centric lab changes**: refined anesthesia and analgesia protocols, environmental enrichment; severity scoring recalibrated; mandatory welfare training for technicians.
- **Stakeholder engagement**: patient advocacy groups and ethics advisors included in quarterly public reports to improve transparency.

### Imputable — logging, versioning and audit trail
- **Immutable audit logs** recorded: raw assay data, model versions, threshold decisions, reviewer approvals, IACUC approvals, and SOPs used.
- **Pre-registration of decision rules**: thresholds for replacing animal studies with alternatives were pre-registered and time-stamped.
- **Governance**: IACUC integrated with the Model Risk Management committee; changes to models or MPS validated with sign-offs.

### Credible — validation, bias checks and acceptance criteria
- **Out-of-sample prospective validation**: 6-month silent runs where alternative methods’ predictions were recorded but standard animal testing continued; concordance was tracked.
  - Prospective concordance after 3 months: in-vitro + in-silico ensemble vs animal outcome: **agreement = 88%** for go/no-go decisions.
- **Regulatory engagement**: early scientific advice meetings with FDA/EMA to align on use of NAMs (new approach methodologies); adopted OECD-adapted protocols for some MPS endpoints.
- **Equity & bias**: checked models for chemical class bias and assay batch effects; annual reweighting and calibration maintained cross-chemical-class AUC variance within ±3%.

### Secure — data governance and biosafety
- **Data governance**: genomic/proprietary chemistry data access controls, encryption, and retention policies; shared MPS vendor data under DPAs that prohibited raw PHI sharing.
- **Biosafety**: new MPS protocols subject to biosafety review (BSL requirements), with vendor attestations for cell-line provenance and donor consents.

---

## Quantitative outcomes (Year 0 → Year 4)

> All numbers are aggregated from the company’s program dashboards and internal QA tracking.

**Animals & welfare**
- Animals used/year: **12,500 (2019)** → **8,200 (Year 1)** → **6,400 (Year 2)** → **5,200 (Year 3)** → **4,500 (Year 4)**.  
- Final animals/year (Year 4): **4,500** — a **64% reduction** against the 2019 baseline.  
- Moderate/severe procedure rate: **24% → 7%**.  
- Number of full replacement studies (animal → non-animal): **~1,280 studies replaced** cumulatively.

**Predictive & development metrics**
- In-silico + in-vitro ensemble AUC vs human adverse events: **0.81** (improved from 0.66 pre-program using animal-only proxies).  
- Late-stage attrition rate (toxicity-related) reduced: **42% → 29%** (30% relative reduction).  
- Time-to-candidate: **18 months → 14 months** (22% reduction).  
- Preclinical cost per candidate: **\$3.5M → \$2.55M** (27% cost reduction).

**Operational & compliance**
- ARRIVE-compliant animal reports: **62% → 100%**.  
- IACUC/inspection findings: **1 observation (2018)** → **0 findings** after remediation (post-Year 2).  
- External outreach: published two method validation papers with partner academic labs; engaged with regulators via 3 scientific advice meetings.

**Human & social metrics**
- Researcher acceptance (survey): “I trust non-animal predictions for early triage” **24% → 68%**.  
- Public sentiment: fewer external complaints; NGO score declined from escalated complaints to monitored cooperation (qualitative improvement).

---

## Example technical case: hepatotoxicity screening pipeline (detailed)

**Pre-ETHICS flow (per compound)**
1. In-silico rule-based filter → if pass → single-dose mouse LD50 and liver enzyme panel → if pass → 14-day subchronic rodent study → in parallel DMPK in rats → candidate decision.

**Post-ETHICS revised flow**
1. **In-silico ensemble** (reactive metabolite score, structural alerts, off-target binding probabilities) →  
2. **HTS hepatic cytotoxicity panel** (primary human hepatocytes, 3D spheroids) + mechanistic biomarkers (mitochondrial stress assays) →  
3. **Liver MPS perfusion study** for compounds with marginal signals (clearance, metabolite profiling) →  
4. Only compounds with discordant or high-uncertainty signals progress to minimal rodent studies for regulatory bridging.

**Benchmarked metrics (historical comparison)**
- Compounds triaged out pre-animal: **66% → saved ~\$880k per compound** on average.  
- Concordance of MPS vs rodent histopathology in prospective trial: **Cohen’s kappa = 0.72** (substantial agreement).  
- Predictive uplift: incorporating MPS reduced false negatives for hepatotoxicity that later appeared in humans by **~43%** relative to rodent-only early screens.

---

## Governance, oversight and documentation

**Structural changes**
- New **3Rs & ETHICS Board** co-chaired by Chief Scientific Officer and Head of Animal Welfare; quarterly public reporting of program KPIs.  
- **Model Risk Management (MRM)** integrated non-animal NAMs as “models” with model cards, validation, challenger models, and monitoring pipelines.  
- IACUC now reviews alternatives first; animal use is the last resort with documented justification.

**Policy & regulatory alignment**
- Adopted ARRIVE guidelines for in-vivo reporting and published method validation following OECD concept notes.  
- Entered an agreement with regulators to accept NAMs for certain endpoints (early scientific advice and pilot approvals).

---

## Remaining challenges & limitations

- **Regulatory acceptance boundary**: some regulatory submissions (e.g., first-in-human GLP bridging) still require non-rodent data in certain territories; complete animal elimination is not yet feasible.  
- **Applicability domain**: some novel chemotypes fall outside in-silico model domains, requiring conservative animal testing.  
- **Initial capital & capacity**: MPS and organoid platforms required significant capital (~\$8M facility upgrade) and skilled staff.  
- **Validation generalizability**: models required ongoing retraining and can drift if new chemical series are introduced without revalidation.

---

## Lessons learned & recommendations

1. **Program framing**: successful replacement requires clear, quantified KPIs (reduce animals while preserving human safety signals) and cross-functional leadership.  
2. **Incremental transition**: pragmatic tiered approach (in-silico → in-vitro → MPS → targeted in vivo) prevents scientific gaps and preserves regulator confidence.  
3. **Transparency & reproducibility**: model and data cards, immutable logs, ARRIVE compliance and pre-registration of decision rules are critical to auditor/regulator trust.  
4. **Welfare gains are measurable**: replacing high-severity studies and improving analgesia/environmental enrichment materially reduces animal suffering with clear KPI evidence.  
5. **Cost/time tradeoffs**: while upfront capital is high, long-term per-candidate cost and time reductions are significant and reduce late-stage attrition costs.  
6. **Engage regulators early**: scientific advice and pilot submissions smooth pathway to accepting NAMs in pivotal decisions.

---

## Conclusion

The ETHICS-driven program demonstrates that combining governance reforms, modern alternative methods, explainable models, and careful validation can **dramatically reduce animal use** (64% reduction), **improve predictive performance**, and **accelerate drug discovery** while meeting animal welfare and regulatory expectations. Although not a complete replacement of animal testing today, the program materially advanced scientific, ethical and business goals — and created a repeatable template other organizations can adopt.
