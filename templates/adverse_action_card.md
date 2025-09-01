# Adverse Action Reason Card — {{MODEL_NAME}} (v{{MODEL_VERSION}})  
Purpose: Document how adverse action reasons are generated and governed (ECOA/Reg B, FCRA).  
  
## Scope and Context  
- Decision type: {{e.g., credit approval/limit adjustment}}  
- Explanation basis: {{e.g., monotone scorecard + ablation tests; SHAP used for QA, not sole basis}}  
  
## Reason Code Mapping  
| Feature/Factor | Human-readable reason | Code/Category | Directionality | Notes/Suppression |  
|---|---|---|---|---|  
| {{DTI}} | {{High debt-to-income ratio}} | {{Debt obligations}} | {{Higher is riskier}} | {{suppress if proxy risk}} |  
| {{UTIL}} | {{High credit utilization}} | {{Credit utilization}} | {{Higher is riskier}} | {{...}} |  
  
- Stability tests: reason rank stability across bootstraps = {{%}}  
- Coverage: percent of decisions with ≥1 valid reason = {{%}}  
- Guardrails: block ambiguous/proxy reasons; manual override protocol link: {{LINK}}  
  
## QA, Monitoring, and Audit  
- Spot-check cadence and samples per segment: {{...}}  
- Dispute/appeals workflow: {{...}}  
- Change control and version history: {{...}}  
  
Approvals: Owner {{...}}, Compliance {{...}}, Date {{...}}  
