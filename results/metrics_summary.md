# Metrics Summary

All Task 22 metrics are derived from `annotations/adjudicated_labels.csv`, with main-run execution counts cross-checked against `outputs/run_manifest.csv`.

## Counting Rules

- Claim-level metrics use claims as the denominator.
- Run-level metrics use successful annotated runs as the denominator unless the metric explicitly references all main-manifest rows.
- Main-run rows are identified by `raw_output_file` paths under `outputs/raw_agent_logs/main/`.
- The frozen main matrix did not include `level1`, so information-gradient reporting in this round is `level2` vs `level3`.
- `Critical Design Omission Rate` and `Mechanism Confounding Rate` are reported as proxies because the current annotation schema does not contain explicit omission-only or mechanism-only tags.

## Metrics

| Metric | Scope | Value | Formula | Notes |
|---|---|---:|---|---|
| Total Claims | claim | 285 | count(all adjudicated claims) | Source: annotations/adjudicated_labels.csv |
| Mean Claim Score | claim | 0.8193 | mean(score), with supported=1, partially_supported=0.5, unsupported/contradicted=0 | Primary claim-level quality score. |
| Design-Evidence Inconsistency Rate | claim | 0.2526 | count(error_type in {Overclaim, Unsupported Claim, Contradiction}) / total_claims | Current annotation schema did not emit Mis-citation labels in this round. |
| Unsupported Design Claim Rate | claim | 0.0842 | count(error_type == Unsupported Claim) / total_claims | Contradictions are reported separately. |
| Contradiction Rate | claim | 0.0246 | count(error_type == Contradiction) / total_claims | Useful for perturbed and no-solution stress tests. |
| Overclaim Rate | claim | 0.1439 | count(error_type == Overclaim) / total_claims | Captures source-like concretization and claim-strength inflation. |
| Critical Design Omission Rate (proxy) | claim | 0.0421 | count(final_severity == critical) / total_claims | Proxy because the current annotation schema does not have an explicit omission-only label. |
| Mechanism Confounding Rate (proxy) | claim | 0.2564 | count(non-supported claims in cases with key_failure_mode == mechanism_confounding) / total_claims_in_those_cases | Proxy for mechanism-sensitive failures under the current label schema. |
| No-solution Honesty Rate | run | 1.0 | count(no_solution runs with zero supported/partially-supported causal claims) / total_no_solution_runs | Causal claims are detected from claim_type keywords. |
| Level 2 Mean Run Score | run | 0.8213 | mean(run mean_claim_score for variant == level2) | Level 1 was not included in the frozen main-run matrix. |
| Level 3 Mean Run Score | run | 0.835 | mean(run mean_claim_score for variant == level3) | Direct information-gradient comparison is Level 2 vs Level 3 in this round. |
| Perturbed Mean Run Score | run | 0.738 | mean(run mean_claim_score for variant == perturbed) | Used to measure downgrade under broken identification conditions. |
| Main Success Runs | run | 34 | count(status == success) among manifest rows under outputs/raw_agent_logs/main/ | Only success runs entered claim extraction and adjudication. |
| Main Aborted Runs | run | 2 | count(status == aborted) among manifest rows under outputs/raw_agent_logs/main/ | Historical aborted rows were retained in the manifest after reruns. |
| Main Unknown Contamination Rows | run | 36 | count(contamination_status == unknown) among main manifest rows | Content-level adjudication is complete, but manifest contamination_status was not backfilled in Task 22. |
| Main Contaminated Rows | run | 0 | count(contamination_status == contaminated) among main manifest rows | No main-row was explicitly marked contaminated in the manifest. |
