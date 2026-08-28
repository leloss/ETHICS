# Third-Party Model Due Diligence — {{MODEL_ID}} / {{VENDOR}} / {{PRODUCT}} (v{{VERSION}})
- Assessed by: {{NAME}} | Date: {{DATE}} | Tier: {{TIER}} | Contract owner: {{NAME}}
- Related: [MRM methodology](README.md) · [tiering](model_risk_tiering.md) · [validation plan](validation_plan.md)

Third-party capability does not transfer institutional accountability. A purchased model is
validated, monitored, tiered, and owned exactly as an internal one; what changes is the
evidence available and how it must be obtained. Where the vendor will not supply evidence,
the institution generates its own or accepts a documented limitation on reliance.

## Vendor and product
- Vendor, legal entity, jurisdiction: {{...}}
- Product and version in use: {{...}}
- Contract term, renewal, and termination rights: {{...}}
- Annual cost and switching cost estimate: {{...}}
- Concentration: other institution processes dependent on this vendor: {{...}}
- Vendor's own sub-processors and model providers: {{...}}

## Evidence obtained

| Evidence | Obtained | Adequate | Gap and treatment |
|---|---|---|---|
| Model documentation / methodology | {{Y/N}} | {{Y/N}} | {{...}} |
| Training data description and provenance | {{Y/N}} | {{Y/N}} | {{...}} |
| Performance claims with test conditions | {{Y/N}} | {{Y/N}} | {{...}} |
| Subgroup / fairness testing | {{Y/N}} | {{Y/N}} | {{...}} |
| Known limitations and failure modes | {{Y/N}} | {{Y/N}} | {{...}} |
| Independent audit or certification | {{Y/N}} | {{Y/N}} | {{...}} |
| Security attestation (SOC 2, ISO 27001, pen test) | {{Y/N}} | {{Y/N}} | {{...}} |
| SBOM / dependency disclosure | {{Y/N}} | {{Y/N}} | {{...}} |
| Change and version notification policy | {{Y/N}} | {{Y/N}} | {{...}} |
| Right to audit | {{Y/N}} | {{Y/N}} | {{...}} |

## Independent testing

Vendor-reported performance is a claim about the vendor's population, not evidence about
the institution's. Reliance rests on testing against the institution's own data.

- Institution's benchmark set: size={{...}}, construction={{...}}, labeling method={{...}}
- Vendor-claimed performance: {{...}}
- Measured performance on institution data: {{...}}
- Gap between claimed and measured, and explanation: {{...}}
- Subgroup performance measured internally: {{...}}
- Performance by segment the vendor does not report on (geography, sector, language,
  source type): {{...}}
- Stability across the period tested: {{...}}

## Transparency and reliance limits
- What the institution can and cannot see of the vendor's processing: {{...}}
- Can an individual output be explained to an affected person? {{...}}
- Can a past decision be reconstructed from records the institution holds? {{Y/N, how}}
- Where the vendor is a black box, the compensating controls applied: {{overlay evaluation,
  decision logging on the institution's side, confidence calibration, sampling QA}}
- Reliance level permitted given the evidence available: {{Advisory | Decision support |
  Automated with review | Automated}}

## Data and security
- Data sent to the vendor: {{fields, and whether minimized or hashed}}
- Legal basis for the transfer: {{...}}
- Processing and storage locations: {{...}}
- Retention at the vendor and deletion rights: {{...}}
- Is institution data used to train vendor models? {{Y/N, contractual position}}
- Encryption in transit and at rest: {{...}}
- Access controls on the vendor side: {{...}}
- Incident notification obligation and timeframe: {{...}}
- Prompt injection / adversarial input handling, for generative products: {{...}}

## Change and continuity
- How the institution learns of model or version changes: {{...}}
- Notice period before a change takes effect: {{...}}
- Ability to pin, defer, or reject a version: {{Y/N}}
- Re-validation triggered by vendor change: {{per change_control.md}}
- Exit plan: data retrieval, transition, and continuity if the vendor fails or is
  terminated: {{...}}
- Time to switch, and what happens to in-flight decisions during transition: {{...}}

## Determination
- Reliance approved at level: {{...}}
- Conditions and compensating controls: {{...}}
- Limitations recorded and accepted by: {{NAME/ROLE/DATE}}
- Reassessment due: {{DATE}}
- Approved: Contract owner {{NAME/DATE}} | Validator {{NAME/DATE}} | Security {{NAME/DATE}} | 2LOD {{NAME/DATE}}
