# Adjudication Notes

## Sampling Rule

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

## Sample Summary

- sampled claims: `78`
- share of all claims: `78/370 = 21.1%`
- sample by case:
  - `C001`: `16`
  - `C002`: `10`
  - `C004`: `8`
  - `C005`: `8`
  - `C008`: `6`
  - `C010`: `6`
  - `C014`: `6`
  - `C016`: `6`
  - `C019`: `6`
  - `C020`: `6`
- sample by variant:
  - `level1`: `24`
  - `level2`: `19`
  - `level3`: `16`
  - `no_solution`: `4`
  - `perturbed`: `15`

## Agreement

- simple agreement on `human_judgment`: `97.4%`
- simple agreement on `error_type`: `97.4%`
- disagreement rows requiring adjudication: `2`

## Disagreement Table

| Claim ID | Case | Variant | Labeler1 | Labeler2 | Final | Reason |
|---|---|---|---|---|---|---|
| `RUN_20260527_215707_05_openclaw_deepseekv4pro_isolated_CL004` | `C002` | `level2` | `unsupported` | `partially_supported` | `partially_supported` | Adopt the weaker label because the design motivates an interaction test but does not justify asserting additivity from the packet alone. |
| `RUN_20260528_001055_31_openclaw_deepseekv4pro_isolated_CL007` | `C020` | `level2` | `supported` | `unsupported` | `unsupported` | The second-pass label is adopted because the gold explicitly warns against a pure digit-processing interpretation at this strength. |
