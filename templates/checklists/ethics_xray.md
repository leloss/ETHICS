# ETHICS System X-Ray
### ETHICS-Based Responsible AI Self-Assessment

## Model / System Metadata

| Field | Value |
|---|---|
| Business Unit | {{BUSINESS_UNIT}} |
| Model ID | {{MODEL_ID}} — matches [model_inventory.csv](../mrm/model_inventory.csv) |
| Model / System Name | {{SYSTEM_NAME}} |
| Version | {{VERSION}} |
| Intended Use / Scope | {{INTENDED_USE}} |
| Date of Assessment | {{DATE}} |
| Assessors (business owner, technical lead, risk/compliance, users) | {{ASSESSORS}} |

> This checklist works best when completed jointly. A product owner acting alone tends to
> overstate readiness; a control function acting alone tends to miss workflow realities.

## Scoring scale

Score the **evidence** of a control, not its presence in policy.

| Score | Meaning |
|---|---|
| 0 | Absent, unsupported, or not evidenced |
| 1 | Ad hoc, partial, or inconsistently applied |
| 2 | Operational, but incomplete or unevenly evidenced |
| 3 | Strong, evidenced, and able to withstand review |

Optionally record a maturity note alongside the score: `Ad hoc`, `Defined`, `Operational`,
or `Proven under review`. This distinguishes controls that exist on paper from controls
that have actually held up in practice.

## ETHICS Pillars Scoring Sheet

### Enhancing

| ID | Aspect / Checkpoint | Score (0–3) | Maturity | Evidence |
|---|---|---|---|---|
| E1 | AI quantitatively improves outcomes | | | |
| E2 | Complementary/contrasting evaluation metrics used | | | |
| E3 | Improvement vs. human baseline reported | | | |
| E4 | Tested under realistic/production conditions | | | |
| E5 | Edge conditions and limitations reported | | | |
| E6 | Cost/benefit clearly and numerically demonstrated | | | |
| E7 | Periodic re-evaluation planned and scheduled | | | |

### Transparent

| ID | Aspect / Checkpoint | Score (0–3) | Maturity | Evidence |
|---|---|---|---|---|
| T1 | Full model/system documentation available | | | |
| T2 | Decisions explainable in domain experts language | | | |
| T3 | Simplified rationale for non-experts used | | | |
| T4 | Data lineage clearly tracked and reported | | | |
| T5 | Features and variables influencing outputs disclosed | | | |
| T6 | Assumptions, limitations, and hardcoded terms explicitly reported | | | |
| T7 | Justification reproducible and traceable at decision time | | | |

### Human-Centered

| ID | Aspect / Checkpoint | Score (0–3) | Maturity | Evidence |
|---|---|---|---|---|
| H1 | Human-in-the-loop oversight enabled | | | |
| H2 | Easy and safe override mechanisms exist | | | |
| H3 | Alerts are actionable with enough context and instructions | | | |
| H4 | Interfaces support usability defined by known design patterns | | | |
| H5 | Appeals process for customers formally put in place | | | |
| H6 | User feedback loop integrated to training/enhancement process | | | |
| H7 | Social impact assessed and disclosed | | | |

### Imputable

| ID | Aspect / Checkpoint | Score (0–3) | Maturity | Evidence |
|---|---|---|---|---|
| I1 | Full audit trail of model activity available | | | |
| I2 | Traceability enabled from input to decision | | | |
| I3 | Logs include metadata, data, parameters, outputs | | | |
| I4 | Native top-down monitoring enabled | | | |
| I5 | Governance roles assigned and embodied | | | |
| I6 | Evidence retention aligned with policy and needs | | | |
| I7 | Automated alerts for anomalous or non-compliant behavior | | | |

### Credible

| ID | Aspect / Checkpoint | Score (0–3) | Maturity | Evidence |
|---|---|---|---|---|
| C1 | Independent validation possible | | | |
| C2 | Stress-tested under edge cases | | | |
| C3 | Bias tested across subgroups | | | |
| C4 | Fairness metrics regularly reported | | | |
| C5 | Explanations faithful and consistent | | | |
| C6 | Claims are supported by evidence and reproducible | | | |
| C7 | Private and public benchmarks used | | | |

### Secure

| ID | Aspect / Checkpoint | Score (0–3) | Maturity | Evidence |
|---|---|---|---|---|
| S1 | Data encrypted at rest and in transit | | | |
| S2 | Access controlled and logged | | | |
| S3 | Model hardened against adversarial inputs | | | |
| S4 | Regular penetration testing performed | | | |
| S5 | Incident response plan defined | | | |
| S6 | Security monitoring continuous | | | |
| S7 | Third-party dependencies vetted | | | |

## Result

| Measure | Value |
|---|---|
| Absolute Total Score (ATS → 0–126) | {{ATS}} |
| Percentage Total Score (PTS → 0–100%) | {{PTS}} |
| Interpretation Guidance Band (IGB) | {{IGB}} |
| Recommended Actions (RA) and other specific actions | {{RA}} |

## Interpretation Guidance Bands

| Band | IGB | RA |
|---|---|---|
| **Strong (85–100%)** | ETHICS principles are well-integrated. Risks are low and primarily residual; the system demonstrates robust governance, reliability, and trustworthiness. | Maintain good practices with quarterly reviews, continuous red-teaming, and upkeep of model inventory and SBOM. |
| **Acceptable (65–84%)** | System satisfies most ETHICS requirements. Remaining issues are limited in scope and manageable, but ongoing monitoring and planned remediation are necessary. | Close minor gaps, increase cadence of monitoring and fairness checks, and conduct targeted adversarial and stress testing. |
| **Deficient (40–64%)** | Significant gaps in controls. Some ETHICS principles are in place, but coverage is inconsistent, creating material risks if deployed at scale. | Add missing documentation, enable native auditability, deploy essential monitoring, and schedule a re-assessment. |
| **Weak (0–39%)** | Major deficiencies. ETHICS principles are largely unmet, creating high operational, compliance, and reputational risk. System is not fit for regulated or high-stakes use without major remediation. | Apply stop-gap controls, restrict or pause outputs, require independent validation and security review, and assign dedicated remediation resources. |

## Scoring it automatically

Fill the `score` column of `templates/checklists/ethics_xray.csv` (copy it per system/version), then:

```
python scripts/run_ethics_xray.py --xray templates/checklists/ethics_xray.csv
```

This writes `reports/ethics_xray_summary.json` and `reports/ethics_xray.md` with the ATS,
PTS, per-pillar breakdown, IGB band, and recommended action.

To gate a release the way the performance and fairness checks do, use the three-part gate:

```
python scripts/run_ethics_xray.py --xray models/MDL-0001/ethics_xray.csv   --min-pts 65 --min-pillar-pts 50 --require-nonzero T7,I1,I5,C1,S1,S2,H2,H5
```

- `--min-pts` — overall band floor
- `--min-pillar-pts` — per-pillar floor, so strength in five pillars cannot carry a
  collapse in the sixth
- `--require-nonzero` — checkpoints where a zero is not compensable at any aggregate score

Thresholds by tier, and the reasoning behind them, are in
[`../mrm/model_risk_tiering.md`](../mrm/model_risk_tiering.md). Note that several
checkpoints score on operating history (C4, S4, S6, H6) and cannot reach 3 before a system
has run; the deployment floor is set accordingly, with the higher band due at first
recertification.

Adapt the checkpoint list to your environment and domain; if you add or remove
checkpoints, the ATS maximum changes accordingly and the scorer adjusts the percentage
automatically.
