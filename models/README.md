# Model Records

Filled artifacts live here, one directory per model, named by `MODEL_ID`. Templates stay
blank in [`../templates/`](../templates/) so they can be copied cleanly for the next model.

```
models/
├─ README.md
├─ MDL-0001/
│  ├─ mrm_lite.md              # Lite path: often the only file needed
│  └─ ethics_xray.csv          # scored
└─ MDL-0002/                   # full path, Tier 1-2
   ├─ tiering.md
   ├─ development_document.md
   ├─ model_card.md
   ├─ data_card.md
   ├─ genai_system_card.md
   ├─ ethics_xray.csv
   ├─ rai_checklist.md
   ├─ validation_plan.md
   ├─ validation_report.md
   ├─ approval_record.md
   ├─ monitoring_plan.md
   └─ changes/
      ├─ CHG-0001.md
      └─ INC-0001.md
```

Registers are institution-wide rather than per-model, so they live at this level once you
have more than one model:

```
models/
├─ model_inventory.csv         # copied from templates/mrm/
└─ model_findings_log.csv      # copied from templates/mrm/
```

## Conventions

- **`MODEL_ID` is permanent.** It survives renames, retraining, version bumps, and
  ownership changes. A new ID means a genuinely different model, not a new version.
- **Version the records with the model.** These files belong in git next to the code, so
  that the record of what was approved moves with the thing that was approved.
- **A filled artifact is dated and signed.** An undated governance document cannot be
  placed in time when someone asks what was known and when.
- **Nothing here contains raw PII, credentials, or licensed data.** These are governance
  records, and they are read by more people than the data is.
- **Retired models stay.** Move the directory to `models/retired/` rather than deleting it;
  a decision made by a retired model can still be challenged. Retention is set in
  [`../templates/mrm/change_control.md`](../templates/mrm/change_control.md).

## Starting a model record

1. Assign the next `MODEL_ID` and add a row to `model_inventory.csv`.
2. Score materiality in [`../templates/mrm/model_risk_tiering.md`](../templates/mrm/model_risk_tiering.md) to get the tier.
3. Tier 3–4: copy [`mrm_lite.md`](../templates/mrm/mrm_lite.md) and fill it.
   Tier 1–2: follow [`../templates/mrm/README.md`](../templates/mrm/README.md).
4. Score the X-Ray and run it: `python scripts/run_ethics_xray.py --xray models/MDL-0001/ethics_xray.csv`
