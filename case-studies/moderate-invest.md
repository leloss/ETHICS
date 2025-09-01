# Case Study: Applying ETHICS to an AI-Driven Investment Advisory System

## Background
A global asset management firm deployed an **AI-based investment assistant** to recommend portfolio allocations, assess risks, and monitor client accounts in real time.  

The system was expected to:  
- Optimize asset allocations for **over 150,000 retail and institutional clients**  
- Detect early signs of **portfolio risk exposure**  
- Provide **personalized, real-time investment recommendations**  
- Reduce compliance team burden  

Initial enthusiasm was high, but after launch the firm discovered **critical issues undermining trust, usability, and compliance**.

---

## Initial Issues & Shortcomings

### **Enhancing (Performance)**
1. **Unstable performance across market regimes**:  
   - In backtests, the system achieved a **Sharpe ratio of 1.4**.  
   - In live trading during volatile periods (e.g., energy price shock), Sharpe fell to **0.6**.  
   - Risk-adjusted returns underperformed a simple S&P 500 index tracker by **12% annually**.  

2. **Failure to incorporate transaction costs and slippage**:  
   - Portfolios looked profitable in simulation but incurred **hidden costs** of ~0.8% per trade.  
   - Small investors saw net returns drop below **bank deposit rates**.  

---

### **Transparent (Black-box nature)**
1. **Opaque recommendation engine**:  
   - The system would suggest: *“Reallocate 18% of bonds into emerging markets equities”* without explaining **macro drivers or risk assumptions**.  
   - Clients had no way of understanding if recommendations were based on sentiment, historical correlation, or macro forecasts.  

2. **Risk score opacity**:  
   - Portfolios were assigned labels such as *“High-Moderate Risk”* with no breakdown of factors (volatility, sector concentration, liquidity risk).  
   - Compliance teams could not justify to regulators why clients received certain scores.  

---

### **Human-centered**
1. **Misalignment with client needs**:  
   - For retirees, the system still proposed **high-equity allocations (70%)** because “historically equities outperform,” ignoring income and liquidity needs.  
   - Younger clients received overly conservative advice because of **short data horizons**.  

2. **Communication mismatch**:  
   - Language in the app was highly technical: *“Portfolio beta exceeds 1.2 relative to MSCI World Index.”*  
   - Retail clients found this alienating; **surveyed satisfaction dropped to 36%**.  

---

### **Imputable**
1. **Lack of traceability in portfolio construction**:  
   - When regulators questioned why a specific client was allocated to illiquid private equity funds, no logs could show which rules or models triggered the suggestion.  

2. **No failure analysis framework**:  
   - When returns underperformed, risk officers couldn’t determine if it was due to:  
     - Poor feature engineering  
     - Outdated macro signals  
     - Weakness in sentiment models  

---

### **Credible**
1. **Loss of trust with advisors**:  
   - Human wealth managers stopped using AI recommendations in 61% of cases, saying: *“It makes me look incompetent to my clients.”*  
   - 40% of advisors reverted to Excel-based portfolio templates.  

2. **Client attrition**:  
   - 12% of high-net-worth clients closed accounts, citing “lack of clarity and inappropriate allocations.”  

---

### **Secure**
1. **Data leakage to third-party analytics APIs**:  
   - Client portfolios and demographic details were sent unencrypted to external risk scoring services.  
   - This violated **MiFID II** data residency requirements.  

2. **PII embedded in logs**:  
   - Transaction logs contained raw client IDs, income levels, and asset balances without anonymization.  
   - Internal penetration tests showed potential **identity theft vectors**.  

---

## ETHICS Implementation

### **Enhancing**
- Introduced **regime-aware modeling**: system now dynamically adjusts to volatility regimes, preventing performance collapse in crises.  
- Factored in **transaction costs, liquidity spreads, and slippage** in all portfolio optimizations.  
- Result: live trading Sharpe ratio improved from **0.6 → 1.2**, annualized return improved by **+9% vs benchmark**.  

---

### **Transparent**
- Added **explainability layers**:
  - Portfolio recommendations show **macro drivers**: e.g., *“Increasing energy allocation due to correlation with inflation expectations (0.72 correlation last 12 months).”*  
  - Risk scores now decompose into **volatility (42%), sector concentration (33%), liquidity risk (25%)**.  
- Compliance dashboards provide **full reasoning chains** for regulators.  

---

### **Human-centered**
- Redesigned allocation rules to reflect **life-stage and income goals**:  
  - Retirees capped at **30% equity allocation**.  
  - Younger investors allowed higher growth exposure with clear justification.  
- Natural language generation redesigned for clarity:  
  - *“Your portfolio is more concentrated in tech stocks than average. If tech declines, your losses may be higher.”*  
- Satisfaction score rose from **36% → 81%** in post-ETHICS survey.  

---

### **Imputable**
- Implemented **decision logging framework**:  
  - Every portfolio suggestion now records data sources, features, model weights, and confidence intervals.  
  - Example: *“Allocation to EM equities driven by macro factor X, risk-adjusted expected return = 7.2%, confidence = 0.68.”*  
- Root cause analysis dashboards now allow auditors to trace underperformance to specific model weaknesses (e.g., outdated sentiment model).  

---

### **Credible**
- Advisor override rate dropped from **61% → 18%**.  
- Client attrition rate improved from **12% → 3%**.  
- Internal trust survey:  
  - Pre-ETHICS: only 22% of advisors “trusted” AI recommendations.  
  - Post-ETHICS: 76% expressed trust.  

---

### **Secure**
- Replaced third-party APIs with **in-house risk scoring tools**.  
- Logs now use **anonymized client IDs and encrypted balances**.  
- Data flows audited for compliance with **MiFID II and GDPR**.  
- Security incidents dropped to **zero** after ETHICS remediation.  

---

## Results (Pre- vs Post-ETHICS)

| Dimension         | Before ETHICS                                      | After ETHICS                                    |
|-------------------|---------------------------------------------------|------------------------------------------------|
| Sharpe Ratio      | 0.6 (live)                                        | 1.2                                            |
| Annual Returns    | -12% vs benchmark                                 | +9% vs benchmark                               |
| Transaction Costs | Ignored                                           | Fully modeled                                  |
| Client Satisfaction | 36%                                             | 81%                                            |
| Advisor Override  | 61%                                               | 18%                                            |
| Client Attrition  | 12%                                               | 3%                                             |
| Decision Traceability | None                                          | Full logging (<10 min trace per allocation)    |
| Risk Explanation  | “High/Moderate/Low” labels                        | Decomposed, factor-based explanations          |
| Data Security     | PII leakage to APIs, raw IDs in logs              | Fully anonymized & compliant with MiFID/GDPR   |

---

## Lessons Learned
- **Market regime sensitivity matters**: models must adapt to volatility, not just historical averages.  
- **Transparency is a compliance requirement, not a feature**: regulators demand reasoning chains.  
- **Investment advice is inherently human-centered**: ignoring client goals undermines adoption.  
- **Imputability protects against regulatory fines**: traceable logs are essential for audit trails.  
- **Credibility requires both accuracy and clarity**: when trust is broken, even accurate AI is discarded.  
- **Security lapses destroy trust instantly**: fixing PII leaks was as important as fixing portfolio logic.  

---

## Conclusion
By applying ETHICS, the firm turned a **risky, opaque, underperforming system** into a **transparent, human-aligned, trustworthy, and compliant advisory tool**. ETHICS not only improved **returns and client satisfaction**, but also protected the firm from **regulatory and reputational risk**, enabling safe scaling across **20 countries and $150B AUM**.
