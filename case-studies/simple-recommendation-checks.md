# ETHICS Entry Case — Advisor Recommendation Checks for Retail Investments

## Background
A robo-advice overlay suggests model portfolios to retail investors. Wealth managers sometimes adopt those suggestions for clients. The firm wants simple guardrails to ensure suitability and explainability.

## Problem (before ETHICS)
- The recommendation engine optimized for long-term returns only; it ignored short-term liquidity needs.
- Clients received portfolios with higher-than-intended volatility for their stated risk profile.
- Advisors could not see why a portfolio was recommended and hesitated to present it to clients.
- No process to capture advisor feedback that could improve models.

## ETHICS (applied simply)
- **Enhancing**: Add a suitability filter that enforces max volatility and minimum liquid allocation per client risk bucket before recommendations are published.
- **Transparent**: Provide a one-paragraph plain-language rationale for each recommended portfolio (primary driver, main risk, and suggested holding period).
- **Human-Centered**: Require advisor sign-off for “non-standard” recommendations; allow advisors to flag recommendations and record why a client-level tweak was made.
- **Imputable**: Record client inputs, portfolio version, risk constraints applied, advisor decision, and communications sent to the client.
- **Credible**: Monitor realized vs. projected volatility and measure advisor acceptance rates; introduce a small A/B challenger test to validate new portfolio logic.
- **Secure**: Ensure client preference data (risk profile, liquidity needs) is stored with fine-grained access control and not embedded in logs exposed outside the advisory team.

## Example Results (simple, illustrative)
- Advisor acceptance of recommended portfolios rose from **38% → 72%** after adding a one-paragraph rationale and suitability filter.
- Client complaints about unexpected volatility dropped **from 9% → 2%** in the first quarter post-implementation.
- Advisor feedback loop produced three small model improvements in six months, increasing average suitability score.

## What the team continues to monitor

- The suitability filter covers platform assets; advisors capture held-away accounts during the annual review so the full picture reaches the client file.
- Advisor acceptance and portfolio suitability are tracked as separate measures, since adoption alone does not evidence suitability.
- Realized-versus-projected volatility is reviewed each quarter and will take a full market cycle to be conclusive.
- Model changes arising from advisor feedback go through the challenger test before release.

---

## Next Steps
- Publish a short model card for advisor training.
- Add quarterly review of realized outcomes vs. client objectives.
- Expand the advisor feedback mechanism into an explicit human-in-the-loop retraining trigger.
