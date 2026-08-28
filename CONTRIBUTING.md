# Contributing  
  
Thank you for improving the ETHICS RAI template.  
  
Prereqs  
- Python 3.10+ (tested on 3.11)  
- pip install -r requirements.txt  
- pre-commit install  
  
Workflow  
1) Fork and create a feature branch.  
2) Add or update artifacts in /templates, MRM methodology in /templates/mrm, and configs in /config.  
3) If you change acceptance thresholds, justify in the model card and validation report.  
4) Run locally:  
   - python scripts/run_quality_checks.py --config config/project.yaml  
   - python scripts/run_fairness.py --fairness-config config/fairness_config.yaml --project-config config/project.yaml  
   - python scripts/run_accuracy_metrics.py --config config/accuracy_metrics.yaml  
   - python scripts/run_ethics_xray.py --xray models/<MODEL_ID>/ethics_xray.csv  
5) Ensure pre-commit passes (black/isort/flake8).  
6) Open a PR with:  
   - Links to reports in /reports (CI artifacts acceptable)  
   - Updated model/data cards if relevant  
   - Risk/fairness justification for threshold changes  
  
Governance  
- Templates in /templates stay blank. Copy them into models/<MODEL_ID>/ and fill them there, keeping the template filename so a reader can tell which template an instance came from.  
- Do not include PII or licensed data. Use synthetic or approved datasets.  
- Security scans and SBOM run in CI; address critical/high findings or document acceptance.  
  
License  
- By contributing, you agree your contributions are licensed under the repo’s LICENSE.  
