# ETHICS Entry Case — Chronic Disease Risk Stratification for Population Health

## Background
A primary-care network deployed an AI risk stratification score to identify patients at high risk of 12-month hospital admission (diabetes complications, CHF exacerbation) for enrollment into proactive care management programs.

## Problem (before ETHICS)
- The model prioritized patients with frequent visit histories (which correlated with access), inadvertently **under-prioritizing underserved patients** who had fewer past visits despite high unmet needs.
- Care managers received only a numeric risk score with no patient-level rationale or suggested interventions.
- No mechanism to capture clinician feedback or social determinants of health (SDOH) that were not in EHR.
- Risk lists were exported to shared drives with weak access control, raising privacy and compliance concerns.

## ETHICS (applied simply)
- **Enhancing**: Replace blind risk ranking with a resource-aware targeting objective — maximize prevented admissions per care manager hour. Incorporate proxy SDOH signals (neighborhood indices, insurance type) to reduce bias.
- **Transparent**: Provide structured rationale for each flagged patient (key drivers: HbA1c trend, recent ED visit, home health usage) and suggested next steps (medication review, home visit).
- **Human-Centered**: Make risk lists actionable: per-patient quick actions, scheduling suggestions, and ability for care managers to adjust priority with a reason (captured).
- **Imputable**: Log algorithm inputs (hashed), version, clinician actions, outreach attempts, and eventual outcomes to enable retrospective validation of intervention impact.
- **Credible**: Monitor equity metrics (TPR and intervention uptake across socioeconomic strata) and require the model to meet minimum equity thresholds before scale-up.
- **Secure**: Enforce strict role-based access, audit trails for exported risk lists, and retention limits for intermediate analytics datasets.

## Example Results (illustrative)
- Intervention yield (prevented admissions per 100 patients contacted) rose by ~30% after resource-aware targeting.
- Disparity in outreach (previously 2.1x higher for insured vs uninsured) narrowed to 1.1x after augmenting with SDOH proxies.
- Care manager acceptance of AI suggestions increased from 33% → 70% following the addition of short rationales and actionable next steps.

## What the team continues to monitor

- Area-level SDOH proxies are reviewed for their own bias each cycle, since neighborhood is an approximation of individual need.
- A randomized rollout with matched controls is underway to convert modeled prevented-admission estimates into measured outcomes.
- Care-manager capacity is the binding constraint on the program, so targeting gains are planned as better use of existing hours.
- Patients with a thin EHR footprint are picked up through a parallel referral route rather than the model.

---

## Next Steps
- Conduct a randomized rollout with matched control groups to measure causal impact on admissions and costs.
- Expand SDOH data inputs in a privacy-preserving manner (e.g., area-level indices) and continue equity monitoring.
- Set up a governance cadence — monthly review with clinicians, data scientists, and compliance to approve model tweaks.
