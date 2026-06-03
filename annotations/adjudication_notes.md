# Adjudication Notes

- total first-pass claims in file: `647`
- preserved existing adjudication for variants with unchanged claim sets:
  - `research_agent_v1`: `77` claims
  - `research_agent_v2_search`: `77` claims
  - `research_agent_v3_planner_debate`: `79` claims
- newly generated adjudication sections follow below.

## Agent Variant: `benchmark_isolated`

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

- sampled claims: `87`
- sample by case:
  - `C001`: `16`
  - `C002`: `10`
  - `C004`: `7`
  - `C005`: `13`
  - `C008`: `11`
  - `C010`: `6`
  - `C014`: `6`
  - `C016`: `6`
  - `C019`: `6`
  - `C020`: `6`
- sample by variant:
  - `level1`: `25`
  - `level2`: `21`
  - `level3`: `16`
  - `no_solution`: `9`
  - `perturbed`: `16`

### Agreement

- simple agreement on `human_judgment`: `94.3%`
- simple agreement on `error_type`: `94.3%`
- disagreement rows requiring adjudication: `5`

### Disagreement Table

| Claim ID | Case | Variant | Labeler1 | Labeler2 | Final | Reason |
|---|---|---|---|---|---|---|
| `RUN_20260527_215707_05_openclaw_deepseekv4pro_isolated_CL004` | `C002` | `level2` | `unsupported` | `partially_supported` | `partially_supported` | Adopt the weaker label because the design motivates an interaction test but does not justify asserting additivity from the packet alone. |
| `RUN_20260527_224724_11_openclaw_deepseekv4pro_isolated_CL010` | `C005` | `level2` | `partially_supported` | `unsupported` | `unsupported` | Adopt the stricter second-pass label: this is not merely too strong, it positively asserts a condition the packet does not establish. |
| `RUN_20260527_230906_16_openclaw_deepseekv4pro_isolated_CL004` | `C008` | `level3` | `partially_supported` | `supported` | `partially_supported` | Keep the first-pass conservative judgment because the claim reads as stronger than a pure diagnostic proposal. |
| `RUN_20260527_232448_20_openclaw_deepseekv4pro_isolated_CL002` | `C010` | `perturbed` | `supported` | `partially_supported` | `partially_supported` | Adopt the second-pass weaker label: the heterogeneity claim is plausible but better treated as exploratory under the perturbed information structure. |
| `RUN_20260528_001055_31_openclaw_deepseekv4pro_isolated_CL007` | `C020` | `level2` | `supported` | `unsupported` | `unsupported` | The second-pass label is adopted because the gold explicitly warns against a pure digit-processing interpretation at this strength. |
