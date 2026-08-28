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
| Minimum X-Ray band to deploy | Strong | Acceptable | Acceptable | Deficient with plan |
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

Where a Tier 1 model cannot reach the Strong band before a deadline that cannot move, the
route is a time-bound exception with compensating controls under
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
