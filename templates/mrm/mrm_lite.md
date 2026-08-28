# MRM Lite — One-Page Model Governance

For small teams, startups, and low-tier models. One file, filled in an afternoon, that
covers the governance that actually prevents harm. It replaces the full artifact set for
Tier 3 and Tier 4 models, and for any organisation not yet carrying a second line of
defence.

This is the same methodology at a proportionate depth, not a different standard. The
questions below are the ones the full templates ask; they are asked once, briefly, in the
order a small team encounters them. Start here. Move to the
[full set](README.md) when a graduation trigger below fires.

**How to use:** copy to `models/{{MODEL_ID}}/mrm_lite.md`, fill it, keep it in version
control next to the code, and revisit on the review date. If a section does not apply,
write "N/A" and why — that is an answer, and a reviewer can tell it apart from a blank.

---

## 1. What this is

| Field | Value |
|---|---|
| Model ID / name / version | {{MDL-0001}} / {{...}} / {{...}} |
| What it does, in one sentence | {{...}} |
| Decision it influences | {{...}} |
| Who is affected by that decision | {{...}} |
| Business owner (accountable) | {{NAME}} |
| Technical owner | {{NAME}} |
| Date / next review date | {{DATE}} / {{DATE}} |

## 2. How much could this hurt

Answer honestly; everything downstream scales from here.

- Worst realistic outcome if the model is wrong: {{...}}
- Who bears that outcome: {{...}}
- Is it reversible? {{...}}
- How many decisions per month: {{...}}
- Regulatory obligations engaged: {{... / none identified}}
- Can a person get the decision reviewed by a human? {{...}}

**Tier:** {{1 Critical / 2 High / 3 Moderate / 4 Low}} — using the highest applicable
dimension from [model_risk_tiering.md](model_risk_tiering.md).

> **If you land on Tier 1 or Tier 2, stop and use the [full set](README.md).** Lite is not
> sufficient for models that make irreversible decisions about people, run without a human
> in the path, or carry direct supervisory scrutiny. That is the one boundary this document
> will not bend.

## 3. Is it actually better than what we did before

The question that stops teams from shipping models that only look useful.

- What we did before this model: {{...}}
- How that performed, measured: {{...}}
- How the model performs, on the same population: {{...}}
- The gain, stated plainly: {{...}}
- What got worse or moved elsewhere: {{...}}
- Simpler option we rejected, and why: {{...}}

## 4. What we built and tested

- Data: sources, period, and how the population was defined: {{...}}
- What the label actually represents, and whether it encodes past practice: {{...}}
- Model type and why: {{...}}
- Held-out and out-of-time results: {{...}}
- Performance by subgroup, where the decision affects people: {{...}}
- Where it fails: {{...}}
- Threshold and how it was chosen: {{...}}
- Someone other than the builder reviewed this: {{NAME/DATE}}

> Peer review is the Lite substitute for independent validation. It is weaker, and it is
> real: a second person with the standing to say no, who did not build the model. Where no
> such person exists internally, name the external reviewer or record that this control is
> absent.

## 5. Explaining it

- Can we tell an affected person why they got this outcome, in terms they can act on? {{...}}
- Can we reconstruct a decision from six months ago — version, inputs, output, and what a
  human did with it? {{Y/N — if no, fix this before deploying}}
- For LLM/RAG systems: are prompts, retrieval sources, and model version logged per
  output? {{Y/N}} — see [genai_system_card.md](../genai_system_card.md)

## 6. Humans

- Who reviews the output, and can they realistically disagree? {{...}}
- How much time do they have per case: {{...}}
- What happens when they override: {{...}}
- How does an affected person challenge the outcome: {{...}}

## 7. Security and data

- Sensitive data in / out: {{...}}
- Where it goes, including any third party: {{...}}
- Access control and encryption: {{...}}
- If a vendor model: what we tested ourselves rather than took on trust: {{...}}

## 8. What we watch

Three signals minimum. More is better; zero is how models fail silently for a year.

| Signal | Threshold | Who checks | How often | What we do on breach |
|---|---|---|---|---|
| Performance: {{metric}} | {{...}} | {{NAME}} | {{...}} | {{...}} |
| Input or score drift | {{...}} | {{NAME}} | {{...}} | {{...}} |
| Override rate, or complaints | {{...}} | {{NAME}} | {{...}} | {{...}} |

- Who can switch it off, today, without a meeting: {{NAME}}
- How we roll back: {{...}}

## 9. Known problems we are accepting

| Problem | Why we accept it for now | Revisit by |
|---|---|---|
| {{...}} | {{...}} | {{DATE}} |

Writing these down is the point. An accepted risk is governed; an unwritten one is not.

## 10. If something goes wrong

- Who is told, and how fast: {{...}}
- Who can suspend the model: {{NAME}}
- How we identify decisions already affected: {{...}}
- How we put those right: {{...}}

Fuller structure in [model_incident_management.md](model_incident_management.md) when needed.

## 11. Sign-off

| Role | Name | Date |
|---|---|---|
| Business owner | {{...}} | {{...}} |
| Technical owner | {{...}} | {{...}} |
| Peer reviewer (not the builder) | {{...}} | {{...}} |

---

## Graduate to the full set when any of these is true

Growth, not calendar time, is what should move a team off Lite. Check at each review:

- [ ] The model reaches Tier 1 or Tier 2 on re-assessment
- [ ] Decisions become automated, or human review becomes nominal in practice
- [ ] Use extends to a new population, jurisdiction, product, or workflow step
- [ ] A regulator, auditor, enterprise customer, or investor asks how the model is governed
- [ ] The organisation acquires a second line of defence, or is required to have one
- [ ] More than {{5}} models are in production, or more than one team is building them
- [ ] A SEV1 or SEV2 incident occurs, or the same problem recurs
- [ ] The model feeds another model, or its output is reused downstream
- [ ] Anyone cannot answer, from memory, who owns the model and what it is approved to do

**Migration path.** Nothing filled in here is wasted. Section 1 becomes the
[inventory](model_inventory.csv) row. Section 2 becomes the
[tiering](model_risk_tiering.md). Sections 3–5 become the
[development document](model_development_document.md) and
[model card](../model_card.md). Section 8 becomes the
[monitoring plan](ongoing_monitoring_plan.md). Section 9 becomes the
[findings log](model_findings_log.csv). Section 11 becomes the
[approval record](model_approval_record.md).

## What Lite deliberately leaves out

Named so the gap is a decision rather than an oversight:

| Not covered here | Full-set artifact | Why it can wait at low tier |
|---|---|---|
| Independent validation and effective challenge | [validation_plan.md](validation_plan.md), [validation report](../validation_report.md) | Peer review substitutes at Tier 3–4; nothing substitutes at Tier 1–2 |
| Portfolio inventory and aggregate risk view | [model_inventory.csv](model_inventory.csv) | One or two models fit in one file; five do not |
| Formal risk appetite and committee | [governance_and_raci.md](governance_and_raci.md) | Needs an organisation large enough to have a second line |
| Structured change control and recertification | [change_control.md](change_control.md) | Section 9 plus a review date carries this until change becomes frequent |
| Full 42-checkpoint ETHICS System X-Ray | [ethics_xray.md](../checklists/ethics_xray.md) | Worth doing anyway — it is a checklist, not a project |
| Third-party due diligence depth | [third_party_model_due_diligence.md](third_party_model_due_diligence.md) | Section 7 covers the essentials for a single vendor |
