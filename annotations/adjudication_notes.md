# Adjudication Notes

- total first-pass claims in file: `603`
- preserved existing adjudication for variants with unchanged claim sets:
  - `benchmark_isolated`: `370` claims
  - `research_agent_v1`: `77` claims
  - `research_agent_v2_search`: `77` claims
- newly generated adjudication sections follow below.

## Agent Variant: `research_agent_v3_planner_debate`

### Sampling Rule

- fixed seed: `20260528`
- include all `critical` first-pass claims
- include all `calibration_set` claims
- target sample size: `max(60, ceil(total_claims * 0.21))`
- enforce minimum case coverage: `6` claims per case when available
- enforce minimum variant coverage:
  - `level1`: up to `10` claims when available
  - `level2`: up to `10` claims when available
  - `level3`: up to `10` claims when available
  - `perturbed`: up to `10` claims when available
  - `no_solution`: up to `4` claims when available

### Sample Summary

- sampled claims: `60`
- sample by case:
  - `C001`: `7`
  - `C002`: `6`
  - `C004`: `6`
  - `C005`: `5`
  - `C008`: `6`
  - `C010`: `6`
  - `C014`: `6`
  - `C016`: `6`
  - `C019`: `6`
  - `C020`: `6`
- sample by variant:
  - `perturbed`: `60`

### Agreement

- simple agreement on `human_judgment`: `100.0%`
- simple agreement on `error_type`: `100.0%`
- disagreement rows requiring adjudication: `0`

### Disagreement Table

| Claim ID | Case | Variant | Labeler1 | Labeler2 | Final | Reason |
|---|---|---|---|---|---|---|
