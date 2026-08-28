# Model Development Document — {{MODEL_ID}} / {{MODEL_NAME}} (v{{MODEL_VERSION}})
- Developer: {{NAME}} | Model owner: {{NAME}} | Date: {{DATE}}
- Tier: {{TIER}} | Related: [tiering](model_risk_tiering.md) · [model card](../model_card.md) · [data card](../data_card.md) · [validation plan](validation_plan.md)

The development record supporting conceptual soundness under SR 11-7. The standard it must
meet: a competent third party who did not build the model can read this document and
reconstruct what was built, why those choices were made, what was rejected, and what the
model should not be used for. The model card summarises the result; this document carries
the reasoning.

## 1. Business problem and intended use
- Decision the model informs: {{...}}
- Intended use, stated operationally: {{...}}
- Prohibited uses and out-of-scope populations: {{...}}
- Consequence of the decision for the affected person: {{...}}
- Regulatory obligations engaged: {{...}}

## 2. Alternatives considered
The case for a model is not made by the model's performance alone. Record what else was
considered and why it was rejected.

| Alternative | Why rejected | Evidence |
|---|---|---|
| Do nothing / current process | {{...}} | {{...}} |
| Workflow or policy change | {{...}} | {{...}} |
| Rules or scorecard | {{...}} | {{...}} |
| Simpler model class | {{...}} | {{...}} |

- Why the chosen complexity is justified by the gain: {{...}}

## 3. Conceptual soundness
- Theory, mechanism, or empirical basis for believing the inputs relate to the target: {{...}}
- Target variable definition, and how faithfully it proxies the real objective: {{...}}
- Label provenance: how labels were generated, by whom, and what institutional history they
  may encode rather than ground truth: {{...}}
- Key assumptions, and what breaks if each fails:

| Assumption | Rationale | Consequence if violated | How monitored |
|---|---|---|---|
| {{...}} | {{...}} | {{...}} | {{...}} |

## 4. Data
- Sources, timeframe, and extraction logic: {{...}}
- Population definition and exclusions, with the reason for each exclusion: {{...}}
- Train / validation / test split design; temporal separation: {{...}}
- Leakage assessment: what was checked and how: {{...}}
- Representativeness against the deployment population: {{...}}
- Known quality issues and their treatment: {{...}}
- Protected attributes and proxies: excluded={{...}}, proxy testing performed={{...}}
- Full detail in [`../data_card.md`](../data_card.md).

## 5. Feature engineering
- Feature set and the rationale for each material feature: {{...}}
- Transformations, imputation, encoding, scaling: {{...}}
- Features rejected on grounds other than performance (proxy risk, instability,
  unavailability at decision time, unjustifiable to an affected person): {{...}}
- Point-in-time correctness: are all features available at decision time in production
  exactly as constructed in training? {{Yes/No, evidence}}

## 6. Methodology and estimation
- Model class and why it suits the problem: {{...}}
- Hyperparameter search: method={{...}}, space={{...}}, selection criterion={{...}}
- Cross-validation design: {{...}}
- Random seeds and determinism: {{...}}
- Class imbalance treatment: {{...}}
- Calibration method and rationale: {{...}}

## 7. Testing performed by development
Testing is the developer's own challenge to the model, not a demonstration that it works.

- Performance on held-out and out-of-time samples: {{...}}
- Calibration: {{Brier, ECE}}
- Subgroup performance: {{...}}
- Sensitivity to input perturbation: {{...}}
- Stress and edge-case testing: {{scenarios and results}}
- Benchmark against the alternatives in section 2, including the human baseline: {{...}}
- Failure analysis: where does it break, and what characterises the cases it gets wrong? {{...}}
- Tests that were run and did **not** support the model: {{...}}

## 8. Threshold and decision rule
- Threshold selection procedure: {{...}}
- Error costs used: FP={{...}}, FN={{...}}, and their source: {{...}}
- Threshold sensitivity: how much does the outcome move for a small threshold change? {{...}}
- Business rules and policy overlays applied after the model output: {{...}}
- Who may change the threshold, and under what control: {{...}}

## 9. Implementation
- Production architecture and where the model executes: {{...}}
- Training / serving consistency: how verified? {{...}}
- Pre-production parity test results: {{...}}
- Fallback behaviour if the model is unavailable or returns an invalid output: {{...}}
- Versioning: code commit={{...}}, data hash={{...}}, environment={{...}}, artifact registry={{...}}

## 10. Limitations
- Conditions under which output should not be relied on: {{...}}
- Populations where evidence is thin: {{...}}
- Known weaknesses accepted at release, and why: {{...}}
- Expected degradation profile and what would signal it: {{...}}

## 11. Developer's statement
- Residual concerns the developer wishes to record for the validator: {{...}}
- Confirmation that testing and limitations above are complete and not selectively reported:
  {{NAME/DATE}}
