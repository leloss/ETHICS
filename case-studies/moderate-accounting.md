# Case Study: Applying ETHICS to an AI-Driven Financial Accounting Assistant

## Background
A multinational corporation implemented an **AI-driven financial accounting assistant** to automate quarterly reporting, detect anomalies, and reduce auditor workloads.  

The system leveraged:
- **Automated journal entry classification**  
- **Anomaly detection in expense and revenue accounts**  
- **Narrative generation for reports**  

The initiative was intended to **improve efficiency and reduce compliance costs**, but instead uncovered **systemic issues that undermined trust, adoption, and compliance risk posture**.

---

## Initial Issues & Shortcomings

### **Enhancing (Performance)**
- The AI was benchmarked internally with **F1 = 0.88 on historical journal data**.  
- However, in production:
  - **Misclassification rate for journal entries** was **22%** on newly emerging categories.  
  - Anomaly detection produced **high false positives (30%)**, overwhelming accounting teams.  
- Correlation analysis revealed: performance degraded **with seasonality shifts (Q4 reporting spikes)**, as training data did not represent peak-period transactions.  

### **Transparent (Black-box nature)**
- The anomaly detection module flagged entries as “suspicious” without explanations.  
- Accountants could not see whether anomalies were due to:
  - Currency conversion errors  
  - Revenue recognition mismatches  
  - Duplicate invoices  
- Stakeholders described the system as a “black hole,” where **false alarms buried real issues**.

### **Human-centered**
- The system **generated robotic, jargon-heavy narratives** in reports.  
- Example: *"Detected deviation in accrual-basis revenue adjustments at threshold 1.43 sigma."*  
- End-users (finance teams, executives) found this **useless and alienating**, preferring manual summaries.  
- It also ignored cultural context: in APAC regions, dates and currencies were displayed in **U.S.-centric format**, causing confusion.  

### **Imputable**
- During audits, **no logs existed** to trace why journal entries were auto-classified into specific GL accounts.  
- Example: an R&D expense was incorrectly classified under “Marketing,” but no trail showed which rules, embeddings, or thresholds led to the decision.  
- Auditors flagged this as a **material weakness in financial controls**.  

### **Credible**
- Trust collapsed rapidly:
  - **Auditor override rate** was 55% in Q1 reporting.  
  - Finance teams reverted to **manual review of 78% of system output**, nullifying time savings.  
- A PwC compliance review found that the **lack of auditability and false positives** meant the system could not be relied upon for **SOX reporting**.  

### **Secure**
- Sensitive data, including **employee reimbursement receipts and vendor contracts**, was sent through third-party APIs for OCR and classification **without redaction**.  
- An internal red-team test proved that **confidential contract terms** were accessible by API vendors.  
- This was a **serious PII and trade-secret leakage risk**, exposing the company to **GDPR fines** and **contractual breaches**.  

---

## ETHICS Implementation

### **Enhancing**
- Introduced **dynamic model retraining with seasonality-aware data augmentation**.  
- Ensemble anomaly detection (statistical + machine learning) reduced **false positives from 30% → 11%**.  
- Journal classification accuracy increased from **78% → 91%** on real-time transaction streams.  

### **Transparent**
- Added **explainability layers**:
  - Each anomaly flag now specifies: *"Currency mismatch between ledger entry (USD) and source invoice (EUR)"*.  
  - Journal reclassification provides top 3 features and probabilities.  
- Dashboards show **how performance varies by geography, account type, and quarter**, allowing stakeholders to challenge outputs.

### **Human-centered**
- Narrative generation was redesigned using **finance-team co-creation workshops**.  
- Reports now:  
  - Use **plain language** ("Revenue increased 12% YoY, but one-time costs caused lower margins")  
  - Support **local currency/date formats** per region.  
- User satisfaction (internal survey of 400 accountants) improved from **41% → 84%**.  

### **Imputable**
- Implemented **comprehensive decision logging**: every journal entry now includes:
  - Input data source  
  - Preprocessing steps  
  - Classification confidence scores  
  - Threshold applied  
- Auditors can **trace any decision within 5 minutes**, enabling compliance alignment with **SOX and IFRS audit trails**.  

### **Credible**
- After ETHICS:
  - Auditor override rate dropped from **55% → 14%**.  
  - Manual review load decreased from **78% → 27%**, recovering **1200+ staff hours per quarter**.  
  - Finance leadership approved scaling to 14 subsidiaries.  
- Confidence was restored as **external auditors signed off on ETHICS controls** for the first time.  

### **Secure**
- Replaced third-party OCR APIs with **on-prem secure document processing**.  
- Applied **PII masking and contract redaction** before any model ingestion.  
- Encryption (AES-256 at rest, TLS 1.3 in transit) was enforced across pipelines.  
- Security audits showed **zero leakage vectors**, closing previous compliance gaps.  

---

## Results (Pre- vs Post-ETHICS)

| Dimension         | Before ETHICS                               | After ETHICS                          |
|-------------------|---------------------------------------------|---------------------------------------|
| Journal Accuracy  | 78%                                         | 91%                                   |
| Anomaly False Positives | 30%                                  | 11%                                   |
| Auditor Overrides | 55%                                         | 14%                                   |
| Manual Review Load | 78% of outputs                            | 27%                                   |
| User Satisfaction | 41%                                        | 84%                                   |
| Traceability      | None                                        | <5 min per entry                      |
| Data Security     | PII & contracts leaked via APIs             | Fully anonymized, on-prem secured      |

---

## Lessons Learned
- **Performance without context is misleading**: AI worked on benchmarks but collapsed under seasonality and distribution drift.  
- **Black-box anomaly detection is useless to auditors**; transparent reason codes turned the tool into a credible partner.  
- **Human-centered design is essential**: shifting from robotic, technical narratives to localized, empathetic reports drove adoption.  
- **Traceability and imputability are non-negotiable** in regulated accounting environments.  
- **Security lapses can negate all gains**: leaking PII and contracts exposed the company to existential risk.  
- ETHICS transformed a **risky, distrusted system** into a **performant, auditable, human-friendly, and compliant solution**, enabling safe global deployment.  

---

