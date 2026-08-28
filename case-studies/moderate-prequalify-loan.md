# Case Study: Applying ETHICS to an AI Loan Pre-Qualification Assistant

## Background
A mid-sized financial services firm launched an **AI-driven loan pre-qualification assistant**.  
The solution aimed to automate early screening of applicants, estimate eligibility, and reduce time spent by analysts on manual checks.  

However, the project soon ran into **serious performance, trust, and compliance issues** that undermined adoption.

---

## Initial Issues & Shortcomings

### **Enhancing (Performance)**
- Training AUC was reported at **0.85**, but in real-world deployment, the assistant only achieved an **approval accuracy of 72%**, with **false negatives (missed good applicants) at 18%**.  
- Performance gains were inconsistent: in some segments, the AI performed **worse than baseline logistic regression**.

### **Transparent (Black-box nature)**
- Stakeholders had no visibility into **why applicants were rejected or accepted**.  
- Explanations were generic ("insufficient eligibility"), offering **no actionable insights**.  

### **Human-Centered**
- Applicants received **rigid, robotic responses**, often mismatched to tone of voice expected in financial advisory.  
- The assistant failed to recognize sensitive contexts (e.g., applicants mentioning financial hardship), creating **negative user experiences**.  

### **Imputable**
- Analysts had **no audit trail** to trace why the system rejected borderline cases.  
- Root cause analysis was impossible since there were **no logs of model inputs, retrievals, or decision thresholds**.

### **Credible**
- Internal reviewers did not trust the system:
  - **Analyst override rate**: 46% of AI decisions were manually corrected.  
  - Business stakeholders halted full rollout because **nobody could reliably measure AI contribution** to approvals or risk.  

### **Secure**
- During an external audit, it was discovered that applicant **PII (names, addresses, SSNs)** was being **sent to third-party cloud APIs for feature enrichment** without proper anonymization.  
- This created a **data leakage risk** and regulatory exposure under **GDPR/CCPA**.  

---

## ETHICS Implementation

### **Enhancing**
- Introduced **calibrated ROC and precision–recall monitoring** across demographic and income groups.  
- Deployed **ensemble gradient boosting + calibration layers**, improving predictive balance.  
- False-negative rate reduced from **18% → 9%**, and overall approval accuracy rose to **83%**.  

### **Transparent**
- Implemented **model explainability dashboards** (SHAP + feature contributions).  
- Every applicant now receives a **reason code report** ("Rejected due to debt-to-income ratio > 60%") rather than a vague message.  

### **Human-Centered**
- Responses were rewritten into **clear, empathetic language**, aligned with company tone:  
  - Before: *"Your eligibility is insufficient."*  
  - After: *"Based on current income and debt levels, this loan may not be a good fit right now. Here are some next steps you can take…"*.  
- Sensitive cases now trigger **human escalation**.  
- Customer satisfaction scores on AI interactions rose from **62% → 81%**.

### **Imputable**
- Introduced **decision logging** at each step: input features, retrieved data, applied thresholds, and model outputs.  
- Analysts can now **trace any decision in under 3 minutes**, compared to “impossible” before.  

### **Credible**
- Continuous monitoring was introduced:  
  - Analyst override rate dropped from **46% → 12%**.  
  - Model drift checks with quarterly retraining improved trust among risk teams.  
- Business stakeholders approved **scaled deployment** after repeatable evidence of value.  

### **Secure**
- Stopped sending raw PII to external APIs.  
- Replaced with **hashed or anonymized tokens** for enrichment.  
- Added **access controls + encryption at rest and in transit**.  
- Post-remediation audits confirmed **no applicant PII reaching third-party services**, with enrichment limited to hashed tokens.  

---

## Results (Pre- vs Post-ETHICS)

| Dimension       | Before ETHICS                  | After ETHICS                     |
|-----------------|--------------------------------|----------------------------------|
| Accuracy        | 72%                            | 83%                              |
| False Negatives | 18%                            | 9%                               |
| Analyst Overrides | 46%                         | 12%                              |
| Decision Traceability | None                     | <3 min per case                  |
| Customer Satisfaction | 62%                     | 81%                              |
| Data Leakage    | SSNs, addresses to APIs        | Full anonymization + encryption  |

---

## What the team continues to monitor

- The assistant pre-qualifies rather than decides, and accuracy is monitored at 83% with declines always reaching a human.
- Overrides are sampled for correctness so the drop from 46% to 12% reflects decision quality rather than deference.
- Reason codes are re-tested against policy overlays whenever those overlays change, keeping the stated reason aligned with the operative basis.
- Enrichment runs on hashed tokens, with the provider's data handling reviewed annually.

---

## Lessons Learned
- **Performance metrics must go beyond training AUC/loss**; real-world calibration and subgroup fairness are essential.  
- **Transparency and imputability** turn AI from a black box into a tool analysts can trust and debug.  
- **Human-Centered design** not only improves adoption but directly impacts customer trust.  
- **Security** must be baked into AI pipelines; unchecked third-party integrations can create hidden liabilities.  
- ETHICS helped transform a risky, opaque assistant into a **performant, auditable, empathetic, and secure system**.  

