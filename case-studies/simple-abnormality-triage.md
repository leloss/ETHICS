# ETHICS Entry Case: Radiology AI (Chest X-Ray Abnormality Triage)

## Background
A hospital network introduced an AI system to triage chest X-rays (CXR) for urgent findings (pneumothorax, large effusion, consolidation) so radiologists could prioritize critical studies.

## Problem (before ETHICS)
- The vendor model flagged many studies as “urgent” that radiologists judged normal — creating backlog and fatigue.
- The model produced heatmaps but no structured explanation of which findings it relied on; heatmaps varied in ways that confused clinicians.
- Different hospitals in the network showed inconsistent performance (small, rural facility vs tertiary center).
- No versioning or frozen model policy — updates rolled without clinical sign-off.
- DICOM metadata with patient identifiers was mirrored into a cloud analytics environment without strict controls.

## ETHICS (applied simply)
- **Enhancing**: Shift evaluation to clinically relevant triage metrics: precision@topK radiologist review priority, time-to-read for true positives, and downstream impact (time to treatment). Re-calibrate thresholds separately per site to account for case-mix differences.
- **Transparent**: Standardize interpretability outputs: not just heatmaps but short structured reasons (“High likelihood consolidation in right lower zone; model confidence 0.87”), and link to example prior cases.
- **Human-Centered**: Keep radiologist in the loop — AI marks priority but radiologist issues final urgency. Provide an “explain & teach” feedback button so radiologists can flag spurious heatmaps or correct labels.
- **Imputable**: Enforce immutable logging: model version, input DICOM hash, heatmap artifact, radiologist label, and timestamps. Freeze model during active clinical audits.
- **Credible**: Site-specific validation and continuous performance dashboards; schedule monthly spot-checks and require vendor evidence for any upstream data shifts.
- **Secure**: Ensure DICOM metadata masking for analytics and that any cloud storage is HIPAA-compliant with BAAs, encryption, and strict access controls.

## Example Results (illustrative)
- Radiologist triage precision@Top10 improved from 0.42 → 0.78 after per-site recalibration.
- Average time to report for true-positive urgent CXRs decreased by 28 minutes.
- Clinician trust (survey) improved from 48% → 85% with the ‘explain & teach’ feedback loop incorporated.

## What the team continues to monitor

- Per-site recalibration runs whenever scanner hardware, acquisition protocols, or case mix change, with drift treated as expected.
- Benefit scales with queue depth, so the tool is deployed where worklists are long and reviewed where they are not.
- The rural site gap to the tertiary center is on the monthly performance dashboard until it closes.
- Explain-and-teach feedback is adjudicated against ground truth before it enters any retraining set.

---

## Next Steps
- Formalize a model update approval protocol requiring clinical sign-off and post-deployment shadow monitoring.
- Share de-identified failure cases with vendor for targeted retraining.
- Expand to CT triage only after rigorous prospective validation.
