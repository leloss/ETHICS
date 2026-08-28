# Case Study: Applying ETHICS to a Third-Party Adverse Media Monitoring (AMM) Solution  
  
## Background  
  
In 2019, the Financial Crime Risk & Compliance (FCRC) team of a multinational commercial bank purchased a third-party Adverse Media Monitoring (AMM) solution to automate risk flagging during KYC onboarding and periodic customer reviews.  
  
**The vendor claimed:**  
- **Coverage:** 95% of relevant media outlets  
- **Accuracy:** 92% precision in entity resolution  
- **Recall:** >85% for adverse/risk mentions  
- **End-to-End integration:** seamless API into case management systems  
  
By 2024, the AMM solution was deeply embedded into onboarding workflows, periodic reviews, and regulatory reporting, with 5+ years of operational history. The annual vendor license cost exceeded $3.5M.  
  
---  
  
## Pain Points Observed by Analysts  
  
Despite strong vendor-reported KPIs, the analyst team’s internal benchmarks told another story:  
  
- **False Positives (FPs):**    
  Internal QA showed 85% of flagged entities were false alarms, usually due to poor disambiguation (e.g., “John Smith” in a fraud article mislinked to unrelated customers).  
  
- **Blind Spots:**    
  30% of benchmarked adverse articles (e.g., from regional dailies, paywalled industry newsletters) were missing from AMM feeds.  
  
- **Inconsistency:**    
  - Same entity flagged “high-risk” one week, “no risk” the next, with no changes in profile.  
  - Results varied depending on ingestion lag, synonym handling, and ambiguous name resolution.  
  
- **Black Box Vendor:**    
  - Analysts had no visibility into crawling pipelines, NLP filters, or confidence thresholds.  
  - Vendor only provided aggregate precision/recall, no breakdown by geography, sector, or source type.  
  
- **Escalation Fatigue:**    
  - Analysts wasted time reviewing 80+ irrelevant articles per flagged entity.  
  - This stretched onboarding timelines by +27% (from 5.5 days to 7.0 days average).  
  
- **Compliance Red Flags:**    
  - Regulators (under EU AMLD5 and FATF Rec. 10, 12, 15) demanded auditability of AMM systems.  
  - The black-box nature was flagged as a compliance risk in two separate internal audits (2020, 2021).  
  
---  
  
## ETHICS Application  
  
The FCRC team deployed ETHICS not to replace, but to layer governance, visibility, and augmentations on top of the AMM vendor solution.  
  
---  
  
### 1. Enhancing (Effectiveness)  
  
**Baseline:**  
- Vendor-reported precision: 92%  
- Internal precision: 15% (85% FPs)  
- Recall (internal test set): 61% (far below vendor’s >85% claim)  
  
**ETHICS Action:**  
- Built an overlay evaluation framework with precision-recall curves, ROC curves, FPs/FNs tracking using annotated QA datasets (5k manually tagged articles).  
- Applied adaptive thresholds per customer segment (e.g., higher tolerance for FPs in retail, lower tolerance in corporate/PEPs).  
  
**Improvement:**  
- Precision rose from 15% → 49% (+34 pp).  
- Recall improved from 61% → 77% (+16 pp).  
- Average onboarding SLA reduced by 1.2 days (-17%).  
  
---  
  
### 2. Transparent (Black-Box to Glass-Box)  
  
**Baseline Issues:**  
- No insight into which sources/articles triggered alerts.  
- Analysts had to “trust vendor’s black box”.  
  
**ETHICS Action:**  
- Implemented LIME (Local Interpretable Model-Agnostic Explanations) on top of NLP entity-matching outputs.  
- Created a decision log pipeline: each alert now stored the matched entity string, similarity score, threshold applied, and source ID.  
  
**Improvement:**  
- Analysts could now pinpoint why an article was matched (e.g., “string match: 0.72 similarity, alias expansion used”).  
- Transparency allowed constructive vendor feedback loops, resulting in 2 algorithmic patches (NER tuning, alias pruning).  
  
---  
  
### 3. Human-Centered  
  
**Baseline Issues:**  
- AMM alerts written in robotic, jargon-heavy summaries.  
- Analysts had difficulty communicating findings to relationship managers (RMs).  
  
**ETHICS Action:**  
- Standardized natural-language summaries with audience-tuned phrasing.  
- HITL escalation pipeline: top 5% borderline cases escalated to senior analysts with contextual explanations + source snapshot.  
  
**Improvement:**  
- Analyst satisfaction survey: “usefulness of AMM alerts” rating jumped from 2.1 → 4.0 / 5.  
- RM escalations dropped by 42% (fewer complaints about incomprehensible reports).  
  
---  
  
### 4. Imputable (Accountability & Traceability)  
  
**Baseline Issues:**  
- Hard to attribute errors (false alarms vs. missed coverage).  
- Vendor offered no root-cause visibility.  
  
**ETHICS Action:**  
- Created root-cause dashboards:  
    - FP sources = homonyms, incomplete disambiguation, OCR errors.  
    - FN sources = unindexed regional newspapers, inaccessible paywalled journals.  
- Logged every AMM pipeline decision: crawl → parse → NER → match → flag.  
  
**Improvement:**  
- Analysts could now classify 92% of issues into “coverage gap” vs. “matching error”.  
- Weekly RCA reports provided the evidence base for SLA renegotiation with vendor.  
  
---  
  
### 5. Credible (Confidence & Trust)  
  
**Baseline:**  
- Despite high vendor KPIs, internally the AMM was not trusted.  
- Analysts resorted to manual Google searches for onboarding validation.  
  
**ETHICS Action:**  
- Introduced calibrated confidence scores (Platt scaling on similarity outputs).  
- Established quarterly fairness & performance audits (monitoring shifts in FP/FN rates).  
- Incorporated FAQ-driven validation to detect content drift (“Is the AMM still catching sanctions, fraud, terrorism financing coverage at same levels?”).  
  
**Improvement:**  
- Manual Google searches declined by 63%.  
- Trust survey (“I trust AMM output in onboarding”) rose from 29% → 74%.  
  
---  
  
### 6. Secure (Security & Privacy)  
  
**Baseline Issues:**  
- Sensitive customer PII (names, IDs) sent to third-party APIs for enrichment.  
- Logs revealed occasional leakage of non-anonymized data to external servers (GDPR red flag).  
  
**ETHICS Action:**  
- Introduced data minimization: only hashed identifiers sent for AMM queries.  
- Enforced role-based access control (RBAC) and PII masking in audit logs.  
- Vendor required to migrate from US-hosted storage to EU-only cloud zones to comply with GDPR Art. 44.  
  
**Improvement:**  
- **No confirmed PII exposure** in the two post-remediation audit cycles.  
- Compliance rating by internal Data Protection Office improved from amber → green.  
  
---  
  
## Quantitative Results (Post-ETHICS vs. Baseline)  
  
| Metric                    | Baseline (Vendor Reported) | Baseline (Internal Reality) | Post-ETHICS |  
|---------------------------|----------------------------|-----------------------------|-------------|  
| Precision                 | 92% (claimed)              | 15% (85% FPs)               | 49%         |  
| Recall                    | >85% (claimed)             | 61%                         | 77%         |  
| Avg. Onboarding SLA       | 5.5 days (reported)        | 7.0 days (measured)         | 5.8 days    |  
| Analyst “usefulness” rating| N/A                       | 2.1 / 5                     | 4.0 / 5     |  
| RM escalations (alerts clarity) | N/A                  | High (avg. 19/week)         | -42%        |  
| Analyst time wasted on FPs| ~12h/week                  | ~18h/week                    | 7h/week     |  
| PII compliance            | Claimed GDPR-ready         | Audit flagged “amber”        | Green       |  
  
---  
  
## What the team continues to monitor

- Precision at 49% is planned into analyst capacity, with the disambiguation backlog worked through the vendor roadmap.
- The internal benchmark set is expanded each quarter to cover regional and paywalled sources the vendor indexes thinly.
- Hashed identifiers constrain vendor matching by design, and the recall tradeoff is reviewed against privacy requirements annually.
- Vendor cooperation is secured through contractual SLAs, with renewal used as the point of leverage.

---

## Lessons Learned  
  
- **Vendor KPIs ≠ Reality:** Without ETHICS, the vendor’s impressive stats masked deep performance and compliance issues.  
- **Overlay Governance is Powerful:** ETHICS provided glass-box visibility even without access to vendor internals.  
- **Analyst-Centric Fixes Matter:** Language, context, and HITL workflows boosted adoption as much as raw accuracy gains.  
- **Compliance is Not Optional:** PII leakage risk could have led to GDPR fines (up to €20M or 4% of turnover); ETHICS mitigated this proactively.  
  
---  
  
## Conclusion  
  
Even with expensive, long-established third-party solutions, ETHICS can surface blind spots, enforce accountability, and convert a black-box liability into a trusted, auditable, human-aligned system.  
