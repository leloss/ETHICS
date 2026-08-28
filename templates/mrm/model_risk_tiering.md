# Model Risk Tiering — {{MODEL_ID}} / {{MODEL_NAME}} (v{{MODEL_VERSION}})
- Assessed by: {{NAME}} | Date: {{DATE}} | Reviewed by 2LOD: {{NAME/DATE}}
- Related: [inventory](model_inventory.csv) · [development document](model_development_document.md) · [validation plan](validation_plan.md)

Tiering runs at intake and is revisited at every periodic review and every material change.
It determines how much control the model receives, so an understated tier is itself a model
risk finding. The tier is assigned by the business owner and confirmed by the second line;
where they disagree, the higher tier applies until the disagreement is resolved on record.

## Materiality scoring

Score each dimension 1–4. The tier is driven by the **highest** dimension, not the average:
a model with modest financial exposure that makes irreversible decisions about people is
not a low-risk model, and averaging would hide that.

| # | Dimension | 1 — Low | 2 — Moderate | 3 — High | 4 — Critical | Score |
|---|---|---|---|---|---|---|
| M1 | Financial exposure | Immaterial | Contained | Material to a business line | Material to the institution | |
| M2 | Consequence for affected people | No direct effect | Inconvenience, easily corrected | Access to credit, services, or care affected | Irreversible harm: safety, liberty, health, livelihood | |
| M3 | Regulatory exposure | No specific obligation | Internal policy | Named regulatory obligation | Direct supervisory or statutory scrutiny | |
| M4 | Autonomy of decision | Advisory, routinely overridden | Decision support with real review | Automated with review that is rarely exercised | Fully automated, no human in the path | |
| M5 | Reversibility | Trivially reversible | Reversible with effort | Reversible only via appeal | Effectively irreversible | |
| M6 | Population reach | Handful of cases | Single team or segment | Business line | Whole customer or patient population | |
| M7 | Complexity and opacity | Transparent, few inputs | Interpretable model | Complex, post hoc explanation required | Opaque, generative, or non-deterministic | |
| M8 | Dependency and reuse | Standalone | One downstream consumer | Feeds other models or decisions | Systemic: failure cascades | |

**Highest dimension score:** {{...}} → **Assigned tier:** {{...}}

| Highest score | Tier |
|---|---|
| 4 | Tier 1 — Critical |
| 3 | Tier 2 — High |
| 2 | Tier 3 — Moderate |
| 1 | Tier 4 — Low |

### Overrides
A tier may be raised at any time by the second line or the model risk committee. It may be
lowered only with documented rationale and committee approval. Record either here:
- Override direction and rationale: {{...}}
- Approved by: {{NAME/DATE}}

## Control requirements by tier

| Control | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Governance artifact set | Full | Full | [Lite](mrm_lite.md) acceptable | [Lite](mrm_lite.md) |
| Development document | Full | Full | Standard | Short form |
| Model card | Required | Required | Required | Required |
| Data card | Required | Required | Required | Simplified |
| GenAI system card (if applicable) | Required | Required | Required | Required |
| ETHICS System X-Ray | Full 42, joint review | Full 42, joint review | Full 42, owner + 1 | Owner self-score |
| X-Ray gate to deploy | See below | See below | See below | See below |
| Independent validation | Full, pre-deployment | Full, pre-deployment | Targeted review | Peer review |
| Effective challenge by 2LOD | Required | Required | Required | Not required |
| Approval authority | Model risk committee | Committee delegate | 2LOD head | Business owner + 1 |
| Ongoing monitoring frequency | Monthly | Monthly | Quarterly | Annually |
| Recertification | Annual | Annual | Every 2 years | Every 3 years |
| Change control | Full re-validation on material change | Full on material change | Assessment on material change | Notification |
| Adverse action / appeal artifact | Required if decisions affect people | Required if applicable | Required if applicable | If applicable |
| Approval record | Required | Required | Required | Lite sign-off |
| Incident plan | Required | Required | Required | Named suspender + rollback |
| Aggregate risk reporting | Every cycle | Every cycle | Exceptions only | Exceptions only |

Tiers 1 and 2 may not deploy with open High or Critical validation findings. Tier 3 may
deploy with open Medium findings under a dated remediation plan.

## The X-Ray gate

A single aggregate band is the wrong gate on its own, for two reasons. Several checkpoints
score on operating history — C4 *regularly reported*, S6 *continuous*, S4 *regular
penetration testing*, H6 *feedback loop integrated* — and cannot honestly reach 3 before a
system has run. And an aggregate permits compensation: 41 strong checkpoints can carry a
zero on encryption or on the appeal route, which is exactly the trade the band should
forbid.

The gate is therefore three conditions, all of which must hold.

| | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| **1. Overall PTS at deployment** | ≥ 65% (Acceptable) | ≥ 65% (Acceptable) | ≥ 55% | ≥ 40% (Deficient) with plan |
| **2. No pillar below** | 50% | 50% | 40% | — |
| **3. Non-negotiable checkpoints at 0** | None permitted | None permitted | None permitted | Documented and accepted |
| **Band required by first recertification** | 85% (Strong) | 75% | 65% (Acceptable) | 55% |

The deployment bar is set where an honest pre-deployment score can reach it, and the Strong
band becomes an approval condition with a date rather than a launch blocker that is waived
in practice. A control whose exception is routine is not a control.

### Non-negotiable checkpoints

Zero on any of these blocks deployment at Tier 1–3 regardless of the aggregate, because a
zero here cannot be compensated by strength elsewhere.

| Checkpoint | Why it cannot be traded away |
|---|---|
| T7 — Justification reproducible and traceable at decision time | A decision that cannot be reconstructed cannot be governed, defended, or corrected |
| I1 — Full audit trail of model activity | Without it, every later control is unevidenced |
| I5 — Governance roles assigned and embodied | An unowned model has no one to act when it fails |
| C1 — Independent validation possible | If challenge is impossible, the validation opinion is decoration |
| S1 — Data encrypted at rest and in transit | Confidentiality failure alone makes a regulated system unfit |
| S2 — Access controlled and logged | Unbounded access defeats every other security control |
| H2 — Easy and safe override mechanisms *(where a human is in the decision path)* | Oversight without a usable override is nominal |
| H5 — Appeals process for customers *(where decisions affect people)* | An affected person with no route to challenge has no remedy |

Enforce the full gate with:

```
python scripts/run_ethics_xray.py --xray models/MDL-0001/ethics_xray.csv   --min-pts 65 --min-pillar-pts 50 --require-nonzero T7,I1,I5,C1,S1,S2,H2,H5
```

Where a deployment date cannot move and the gate is not met, the route is a time-bound
exception with compensating controls under
[governance_and_raci.md](governance_and_raci.md), recorded in the
[approval record](model_approval_record.md) — not a quiet re-reading of the band.

## Inherent, control, and residual risk

| | Rating | Basis |
|---|---|---|
| Inherent risk | {{Tier from above}} | Materiality scoring |
| Control effectiveness | {{Strong / Acceptable / Deficient / Weak}} | X-Ray band, validation findings, monitoring history |
| **Residual risk** | {{...}} | Inherent adjusted for demonstrated control effectiveness |
| Within appetite? | {{Yes / No / With conditions}} | See [governance_and_raci.md](governance_and_raci.md) |

Control effectiveness is evidenced, not asserted: it draws on the X-Ray band, open findings,
and the last monitoring cycle. A model with strong stated controls and no monitoring
evidence is rated on the evidence.

## Determination

- Tier: {{...}} | Residual risk: {{...}} | Within appetite: {{Yes/No/Conditions}}
- Conditions attached: {{...}}
- Next tiering review due: {{DATE}}
- Business owner: {{NAME/DATE}} | 2LOD: {{NAME/DATE}}
