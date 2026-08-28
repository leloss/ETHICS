# Adverse Action Reason Card — {{MODEL_ID}} / {{MODEL_NAME}} (v{{MODEL_VERSION}})  
Purpose: Document how adverse action reasons are generated and governed (ECOA/Reg B, FCRA).  
- Related: [model card](model_card.md) — see its Explanation Pathways by Audience table, of which this card is the affected-person row · [GenAI system card](genai_system_card.md) if reasons are rendered by an LLM · [validation report](validation_report.md)  
- Where reasons are rendered in natural language by a generative component, the reason must originate in the decision system; the generator may render it but not produce it.  
  
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
