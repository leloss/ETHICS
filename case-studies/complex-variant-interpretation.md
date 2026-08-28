# ETHICS Case Study — Genomic Variant Interpretation Pipeline for Oncology (Clinical Molecular Diagnostics)

## Overview

A tertiary cancer center operating a **Clinical Genomics Laboratory (CGL)** implemented an AI-assisted variant interpretation pipeline to accelerate germline and somatic variant classification and clinical reporting for oncology patients. The pipeline automated annotation, pathogenicity scoring, and report generation to support tumor boards and therapy selection.

The solution was intended to shorten turnaround time, increase throughput, and standardize variant interpretation. After deployment, the lab discovered multiple clinical, regulatory, and ethical failures. The center used ETHICS to remediate and re-qualify the tool for clinical use (CLIA/CAP context) and downstream decision support.

---

## Problems observed (pre-ETHICS)

### Diagnostic performance & clinical safety
- Vendor/academic model claimed **sensitivity = 0.92**, **specificity = 0.87** for detecting pathogenic variants from panel data.  
- Local validation revealed **PPV (positive predictive value) for ‘pathogenic’ calls = 0.55**, meaning **45% of variants labeled “pathogenic” were later downgraded** by molecular pathologists after manual review.  
- Turnaround time (sample to report): **14 calendar days** median, causing delays in treatment planning.  
- There were **7 near-misses** within a year where automated classification suggested a targeted therapy later judged inappropriate after tumor board review.

### Explainability & provenance
- Automated reports included a binary call (Pathogenic/Likely Pathogenic/VUS/Likely Benign/Benign) with a short confidence score but **no transparent evidence trail** linking to dbSNP, ClinVar entries, supporting literature, or population frequency provenance in a structured way.  
- No immutable versioning of annotation databases (e.g., ClinVar snapshot not recorded), impeding reproducibility.

### Governance & compliance
- The pipeline was used to support therapeutic decisions prior to formal **software-as-medical-device (SaMD)** assessment and without complete validation for the lab’s CLIA/CAP accreditation workflows.  
- The lab lacked a formal RACI for model updates, and model changes occurred without clinical sign-off.

### Bias & data quality
- Variant calling and annotation performance varied by genomic ancestry and sequencing center (batch effects): PPV for samples of non-European ancestry **0.41** vs European ancestry **0.60**.  
- Somatic variant detection sensitivity dropped for low tumor purity samples (<20% tumor fraction), causing missed actionable mutations.

### Trust & operational impact
- Molecular tumor boards increasingly overrode AI calls: override rate **37%**, leading to clinician distrust and extra workload.  
- Cost per case (labor + wet lab + informatics) inflated due to rework and manual curation; estimated additional cost **$1,200 per case** attributable to AI false positives.

### Privacy & data sharing
- Raw genomic BAM files and variant call data were temporarily staged in a vendor cloud for annotation; consent language for data sharing was inconsistent across consent forms — potential HIPAA and GDPR issues for international patients.

---

## ETHICS remediations (what the team did)

A comprehensive remediation program was established involving Laboratory Medicine, Molecular Pathology, Bioinformatics, Legal/Compliance, and Patient Advocacy.

### Enhancing (accuracy, throughput)
- **Evidence-weighted ensemble**: replaced single black-box classifier with an ensemble that combined rule-based ACMG-AMP criteria engine, evidence scoring (population frequency, in-silico predictors), and a calibrated machine learning classifier for borderline cases.  
- **Tumor purity & ancestry-aware models**: incorporated sample QC (tumor fraction) and ancestry inference into model confidence scoring, and applied posterior calibration accordingly.  
- **Workflow automation**: parallelized curation tasks and automated lookups (ClinVar snapshots, gnomAD frequencies), cutting median turnaround time from **14 → 7 days**.

### Transparent (provenance & explanations)
- **Structured evidence bundles**: each variant report includes: snapshot of databases used (with accession and date), population frequency table, links to supporting literature (PMIDs), and a per-criterion breakdown of ACMG rules applied.  
- **Explainable pathogenicity score**: output decomposed into components (population rarity, functional prediction aggregate, segregation evidence, prior clinical assertions) with weights and citation links.

### Human-centered (MTB integration & clinician workflows)
- **Tiered reporting**: critical actionable variants surfaced in an executive summary for oncologists; full evidence bundle available for molecular pathologists.  
- **HITL for uncertain/high-impact variants**: variants with intermediate confidence or those triggering treatment recommendations were routed to a rapid molecular review panel (median review time goal 48 hours).  
- **Patient-facing language**: developed lay summaries for germline incidental findings to support genetic counseling.

### Imputable (auditability & versioning)
- **Immutable provenance logs**: for every variant, logged the raw VCF, variant caller version, annotation databases (with hash), model version, and final decision with signer identity and timestamp. These logs persisted to a WORM (write-once) store for CLIA/CAP auditability.  
- **Model freeze and release pipeline**: no model/annotation database update moves to production without formal validation and clinical sign-off.

### Credible (robustness & equity)
- **Ancestry stratification & rebalancing**: augmented training/annotation datasets with curated non-European variants and reweighted evidence to improve PPV across ancestries.  
- **Prospective shadow phase**: 3 months of shadow operation comparing model calls to routine pathology decisions; metrics had to meet pre-defined thresholds (PPV ≥ 0.88 for pathogenic calls, sensitivity ≥ 0.88) before model-supported reporting resumed.

### Secure (consent & data controls)
- **Consent harmonization**: standardized consent language; re-consented where appropriate for cloud processing.  
- **On-prem annotation gateway**: instead of staging BAMs in vendor cloud, only encrypted variant metadata and hashed identifiers were sent; vendor APIs returned annotations and evidence but never received raw reads.  
- **Data access governance**: role-based access to full evidence bundles; genome data quarantined per retention policy.

---

## Results (measured outcomes at 12 months)

> All metrics from laboratory QA dashboards, tumor board logs, and compliance audits.

### Diagnostic performance & safety
- **PPV for pathogenic calls**: **0.55 → 0.92** (post-ETHICS ensemble + curations).  
- **Sensitivity**: **0.91 → 0.88** (small, controlled tradeoff to raise PPV while maintaining sensitivity for actionable variants).  
- **Override rate at tumor boards**: **37% → 9%**.  
- **Number of inappropriate treatment recommendations averted**: estimated **7 → 0** clinically significant near-misses in the first 12 months post-fix.  
- **Turnaround time (median)**: **14 days → 7 days**.

### Equity & calibration
- PPV for non-European ancestry samples: **0.41 → 0.86** (major improvement after augmentation and ancestry-aware calibration).  
- Calibration (ECE on pathogenicity probability): **8.3% → 1.8%**.

### Operational & economic
- Lab rework cost per case reduced **$1,200 → $210** (savings ~$990 per case).  
- Throughput increased ~**28%** (same staffing), enabling quicker access to molecular results for tumor boards.  
- Patient safety: no downstream inappropriate targeted therapy starts attributable to automated miscalls in the post-ETHICS period.

### Governance & compliance
- CLIA/CAP inspections: **4 major deficiencies** pre-ETHICS (related to traceability and validation) → **0 major deficiencies** post-ETHICS.  
- FDA SaMD posture: initiated a formal documentation package aligning with FDA guidance for AI/ML-based SaMD (evidence of validation, monitoring, change control), lowering regulatory risk for future commercialization.

### Privacy & security
- Incidents of unauthorized vendor access: **1** pre-ETHICS → **0** post-ETHICS (after on-prem gateway).  
- GDPR/HIPAA compliance audit: no outstanding findings after consent harmonization and access controls.

---

## Lessons & reflections

1. **Pathogenicity decisions have high clinical consequences** — ETHICS prioritized high PPV and robust provenance over raw classifier sensitivity to avoid harm from false positives.  
2. **Provenance & immutable logs are essential** for CLIA/CAP audits and for enabling reproducibility of clinical decisions.  
3. **Ancestry bias is real and remediable** by augmenting evidence sets and applying ancestry-aware calibration.  
4. **Human oversight (HITL) for uncertain, high-impact cases** is non-negotiable — it preserved safety while allowing automation to scale.  
5. **Operational workflows matter**: halving turnaround time required both algorithmic improvements and process automation (parallel evidence retrieval and streamlined tumor board prep).

---

## Appendix — Key gates used before model-supported clinical reporting

- **Gate 1 (PPV)**: pathogenic call PPV on local validation ≥ 0.88 required to publish an automated pathogenic label.  
- **Gate 2 (Equity)**: PPV difference across major ancestry buckets ≤ 5 pp.  
- **Gate 3 (Provenance)**: all evidence sources must be recorded with snapshot hash and accessible in report bundle.  
- **Gate 4 (HITL)**: If treatment recommendation confidence < 0.90 or the variant is novel (no prior clinical assertion), route to molecular tumor board review.
