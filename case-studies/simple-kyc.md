# Case Study: Applying ETHICS to a KYC AI System

## Background
A financial institution deployed an AI-based solution to support its **Know Your Customer (KYC)** process.  
During development, the expert team reported **89% accuracy** on historical data.  

However, once deployed:
- Analysts and stakeholders used the system as a **black box**.  
- No clarity existed on **which features or components drove errors**.  
- In practice, the system was **poorly tuned** to catch real suspicious cases.  

This created frustration among analysts, reduced trust in the tool, and limited its organizational value.

---

## Challenge
Despite a strong-looking performance metric (accuracy), the system failed to provide:
- **Transparency** for oversight and error diagnosis.  
- **Trustworthy detection** of suspicious cases in production.  
- **Alignment with analysts’ needs**, since explanations and actionable insights were missing.  

Management decided to adopt the **ETHICS Framework** to address these shortcomings.

---

## ETHICS Implementation

### **Enhancing**
- Introduced **FP/FN analysis** and calibrated thresholds using ROC curves.  
- Improved actual detection rates while reducing unnecessary false positives.  
- Measurably improved analysts’ ability to identify high-risk cases.

### **Transparent**
- Added **model interpretability tools** and explanation reports.  
- Analysts could now see which features contributed to risk scoring.  
- Leadership received periodic model performance documentation.

### **Human-Centered**
- Implemented **analyst-in-the-loop (HITL)** review for borderline cases.  
- Standardized explanations helped analysts understand and contest decisions.  
- Analysts reported increased confidence in combining their expertise with the model’s output.

### **Imputable**
- Established **audit trails** for data inputs, system decisions, and analyst overrides.  
- Defined clear ownership and monitoring responsibilities.  
- Enabled regular validation cycles and concept-drift checks.

### **Credible**
- Shifted focus from headline “accuracy” to **robust metrics**:  
  - ROC-AUC improved by 7 percentage points.  
  - False-negative rate reduced significantly at operational thresholds.  
- Continuous monitoring of fairness metrics across customer subgroups.

### **Secure**
- Reinforced **access controls** for model outputs and explanations.  
- Applied **data minimization** for sensitive features.  
- Incorporated security checks into the AI lifecycle.

---

## Results
- **Performance**: ROC-AUC ↑ 0.72 → 0.79; FN rate ↓ 18%.  
- **Trust**: Analysts reported **greater confidence** and adoption of the system.  
- **Governance**: Compliance teams received clear reports, satisfying oversight needs.  
- **Value**: KYC investigations became **faster, more accurate, and auditable**.  

---

## What the team continues to monitor

- Suspicion labels come from prior analyst decisions, so the typology library is refreshed periodically to extend coverage beyond known patterns.
- Detection is measured against known cases, with a periodic look-back on closed files to test for missed activity.
- Subgroup fairness monitoring is in place, with nationality and residency proxies reviewed with legal before use.
- Gains are measured at the current operating threshold; any change in risk appetite triggers revalidation.

---

## Lessons Learned
- Raw accuracy metrics can be **misleading** without calibration and transparency.  
- Embedding **ETHICS principles** (Enhancing, Transparent, Human-Centered, Imputable, Credible, Secure) provides a **structured pathway** to build Responsible AI in financial compliance.  
- By aligning AI design with governance and human needs, organizations can turn black-box models into **trustworthy decision-support systems**.
