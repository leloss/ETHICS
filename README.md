# ETHICS: Responsible AI for Highly Regulated Industries

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

![ETHICS: A six-pillar framework for responsible AI in highly-regulated industries.](ethics-pillars3.png)

**E**nhancing · **T**ransparent · **H**uman-Centered · **I**mputable · **C**redible · **S**ecure

In highly regulated industries, an AI system is not judged only by whether it improves a
metric. It is judged by whether the institution can explain its role, defend its use,
document its outputs, and show that the people around it remain in control. This repository
turns that standard into artifacts you can fill in, thresholds a build can enforce, and a
model risk methodology you can run.

## What is here

| | |
|---|---|
| **Governance artifacts** | Model card, data card, GenAI system card, adverse action reason card, validation report |
| **ETHICS System X-Ray** | 42-checkpoint self-assessment scored on evidence, producing ATS → PTS → interpretation band |
| **ML model risk management** | Inventory, risk tiering, development documentation, validation, approval, findings, monitoring, incidents, change control, third-party due diligence — structured on SR 11-7 / SS1/23 |
| **MRM Lite** | One-page governance for small teams and low-tier models, with explicit triggers for when to move up |
| **Automated gates** | Performance, calibration, fairness, and drift thresholds that fail a build when breached |
| **20 case studies** | Banking, AML, insurance, healthcare, genomics, drug discovery, and trading, graded simple → moderate → complex |

Two layers, designed to be used together. The **ETHICS artifacts** ask whether a system
deserves to be relied on and whether the people around it keep their authority. The **MRM
artifacts** ask whether the institution controls its model risk. A crosswalk between the
six pillars and the three SR 11-7 elements is in
[templates/mrm/README.md](templates/mrm/README.md).

## Start here

| You are | Start with |
|---|---|
| A small team or startup, or governing a low-risk model | [templates/mrm/mrm_lite.md](templates/mrm/mrm_lite.md) — one page, one afternoon |
| A regulated institution, or governing a high-risk model | [templates/mrm/README.md](templates/mrm/README.md) — the full methodology |
| Assessing a system that already exists | [templates/checklists/ethics_xray.md](templates/checklists/ethics_xray.md) — score it, then act on the band |
| Looking for worked examples | [case-studies/](case-studies/) |

[templates/README.md](templates/README.md) is the artifact index: which artifact applies at
which lifecycle stage, who produces it, and what it feeds.

## Quick start

Requires Python 3.11.

1. Copy this repository as a template. Choose a license (default: Apache-2.0).
2. Assign a `MODEL_ID` at intake and register it in
   [templates/mrm/model_inventory.csv](templates/mrm/model_inventory.csv). Carry that ID
   across every artifact — it is what turns a folder of documents into a record.
3. Score materiality in
   [templates/mrm/model_risk_tiering.md](templates/mrm/model_risk_tiering.md). The tier
   determines how much of everything else applies.
4. Fill the artifacts your tier calls for, keeping filled copies in
   [models/](models/) so the blank templates stay reusable.
5. Score the ETHICS System X-Ray: copy `templates/checklists/ethics_xray.csv` to
   `models/<MODEL_ID>/ethics_xray.csv` and fill the `score` column (0–3, on evidence).
   Complete it jointly — business owner, technical lead, risk or compliance, and the people
   who actually use or supervise the system. A product owner scoring alone tends to
   overstate readiness; a control function alone tends to miss workflow realities.
6. Put your evaluation data at `data/processed/eval.csv` with columns `y_true`, `y_score`,
   `group` (and optional `y_pred`).
7. Set thresholds in `config/project.yaml`, `config/accuracy_metrics.yaml`, and
   `config/fairness_config.yaml`. In `project.yaml`, fill `human_baseline` and
   `cost_benefit` before claiming improvement — a gain measured against nothing is not a gain.
8. Run locally:
   ```
   pip install -r requirements.txt
   python scripts/run_quality_checks.py
   python scripts/run_fairness.py
   python scripts/run_accuracy_metrics.py --config config/accuracy_metrics.yaml
   python scripts/run_ethics_xray.py --xray models/<MODEL_ID>/ethics_xray.csv
   ```
9. Push to GitHub; CI publishes reports as Actions artifacts, and link those artifacts in
   pull requests to support review and audit.

CI is red until you supply `data/processed/eval.csv`. That is intentional. The X-Ray step
scores every `models/<MODEL_ID>/ethics_xray.csv` it finds and skips when there are none, so
a partially scored sheet fails rather than passing as zero-risk.

### Gating a release on governance evidence

The X-Ray can gate a build the way the performance checks do, using three conditions
together — an aggregate floor, a per-pillar floor so strength in five pillars cannot carry a
collapse in the sixth, and checkpoints where a zero is not compensable at any score:

```
python scripts/run_ethics_xray.py --xray models/MDL-0001/ethics_xray.csv \
  --min-pts 65 --min-pillar-pts 50 --require-nonzero T7,I1,I5,C1,S1,S2,H2,H5
```

Thresholds by tier are in
[templates/mrm/model_risk_tiering.md](templates/mrm/model_risk_tiering.md).

## Project structure

```
ETHICS/
├─ README.md
├─ LICENSE
├─ templates/
│  ├─ README.md                    # artifact index: which artifact, which stage, what it feeds
│  ├─ model_card.md
│  ├─ data_card.md
│  ├─ genai_system_card.md         # LLM/RAG/agentic: prompts, retrieval, reconstruction
│  ├─ adverse_action_card.md
│  ├─ validation_report.md
│  ├─ ethics-self-assessment.png
│  ├─ ethics-bands.png
│  ├─ checklists/
│  │  ├─ ethics_xray.md            # 42 checkpoints, scoring scale, interpretation bands
│  │  ├─ ethics_xray.csv           # machine-readable scoring sheet
│  │  ├─ rai_checklist.md          # pre-deploy / periodic gate
│  │  └─ controls_map.csv          # controls mapped to NIST AI RMF, SR 11-7, ISO 23894, GDPR/GLBA
│  └─ mrm/                         # ML model risk management (SR 11-7 / SS1/23 shaped)
│     ├─ README.md                 # methodology, lifecycle, ETHICS <-> SR 11-7 crosswalk
│     ├─ mrm_lite.md               # one-page version for small teams and low-tier models
│     ├─ model_inventory.csv
│     ├─ model_risk_tiering.md
│     ├─ model_development_document.md
│     ├─ validation_plan.md
│     ├─ model_findings_log.csv
│     ├─ model_approval_record.md
│     ├─ ongoing_monitoring_plan.md
│     ├─ model_incident_management.md
│     ├─ change_control.md
│     ├─ governance_and_raci.md
│     └─ third_party_model_due_diligence.md
├─ models/                         # filled artifacts, one directory per MODEL_ID
│  └─ README.md
├─ config/
│  ├─ project.yaml                 # gates, human baseline, cost/benefit, oversight monitoring
│  ├─ accuracy_metrics.yaml        # detailed accuracy report and its gates
│  └─ fairness_config.yaml
├─ scripts/
│  ├─ run_quality_checks.py
│  ├─ run_fairness.py
│  ├─ run_accuracy_metrics.py
│  └─ run_ethics_xray.py
├─ case-studies/                   # 20 worked examples across regulated sectors
├─ data/
│  ├─ raw/.gitkeep
│  └─ processed/.gitkeep           # place eval.csv here (y_true, y_score, group)
├─ reports/.gitkeep                # CI writes HTML/JSON here
├─ .github/workflows/
│  ├─ quality-gates.yml
│  └─ security.yml
├─ requirements.txt
├─ .pre-commit-config.yaml
├─ SECURITY.md
├─ CODE_OF_CONDUCT.md
└─ CONTRIBUTING.md
```

## The article series

1. *ETHICS: A Six-Pillar Framework for Responsible AI in Highly Regulated Industries* — June 2026
2. *The Case for Enhancement: Building AI Systems That Objectively Improve Processes and Outcomes* — June 2026
3. *The Case for Transparency: Making AI Systems and Their Decisions Understandable and Verifiable* — July 2026
4. *The Case for Human-Centered AI: Upholding Human Agency, Dignity, and Safety* — August 2026

Articles on Imputable, Credible, and Secure are in preparation.

## References

[1] Leandro A. Loss, *ETHICS: A Six-Pillar Framework for Responsible AI in Highly Regulated Industries*, 2026.

[2] Leandro A. Loss, *ETHICS: A Six-Pillar Framework for Responsible AI in Finance*, The 2nd Workshop on LLMs and Generative AI for Finance (ACM ICAIF'25), 2025.

## Open-source tools referenced

- [Fairlearn](https://fairlearn.org) — fairness assessment
- [AIF360](https://github.com/Trusted-AI/AIF360) — bias metrics and mitigation
- [Great Expectations](https://greatexpectations.io) — data quality
- [Evidently](https://github.com/evidentlyai/evidently) — drift and monitoring
- [Trivy](https://github.com/aquasecurity/trivy) — vulnerability scanning and SBOM
- [Syft](https://github.com/anchore/syft) — SBOM generation
- [Grype](https://github.com/anchore/grype) — software composition analysis

## Contributing and security

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) and
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). To report a vulnerability, follow
[SECURITY.md](SECURITY.md) rather than opening a public issue.

## Notes

- Not legal advice. Align adverse action content and regulatory interpretation with counsel
  and internal policy.
- Do not commit raw PII or licensed data. Use secrets and approved data paths.
- Never commit private keys or credentials. Pre-commit runs `detect-private-key`; keep SSH
  keys in `~/.ssh`, outside the repository.

Licensed under [Apache-2.0](LICENSE).
