# Adjudication Notes

## Sampling Rule

- fixed seed: `20260528`
- include all `critical` first-pass claims
- include all `calibration_set` claims
- top up to 60 total claims with stratified case coverage (minimum 6 per case)

## Sample Summary

- sampled claims: `60`
- share of all claims: `60/285 = 21.1%`
- sample by case:
  - `C001`: `6`
  - `C002`: `6`
  - `C004`: `6`
  - `C005`: `6`
  - `C008`: `6`
  - `C010`: `6`
  - `C014`: `6`
  - `C016`: `6`
  - `C019`: `6`
  - `C020`: `6`
- sample by variant:
  - `level2`: `19`
  - `level3`: `15`
  - `no_solution`: `4`
  - `perturbed`: `22`

## Agreement

- simple agreement on `human_judgment`: `83.3%`
- simple agreement on `error_type`: `83.3%`
- disagreement rows requiring adjudication: `10`

## Disagreement Table

| Claim ID | Case | Variant | Labeler1 | Labeler2 | Final | Reason |
|---|---|---|---|---|---|---|
| `RUN_20260527_215707_05_openclaw_deepseekv4pro_isolated_CL004` | `C002` | `level2` | `unsupported` | `partially_supported` | `partially_supported` | Adopt the weaker label because the design motivates an interaction test but does not justify asserting additivity from the packet alone. |
| `RUN_20260527_224724_11_openclaw_deepseekv4pro_isolated_CL010` | `C005` | `level2` | `partially_supported` | `unsupported` | `unsupported` | Adopt the stricter second-pass label: this is not merely too strong, it positively asserts a condition the packet does not establish. |
| `RUN_20260527_230906_16_openclaw_deepseekv4pro_isolated_CL004` | `C008` | `level3` | `partially_supported` | `supported` | `partially_supported` | Keep the first-pass conservative judgment because the claim reads as stronger than a pure diagnostic proposal. |
| `RUN_20260527_232448_20_openclaw_deepseekv4pro_isolated_CL002` | `C010` | `perturbed` | `supported` | `partially_supported` | `partially_supported` | Adopt the second-pass weaker label: the heterogeneity claim is plausible but better treated as exploratory under the perturbed information structure. |
| `RUN_20260527_232816_21_openclaw_deepseekv4pro_isolated_CL007` | `C014` | `level2` | `supported` | `partially_supported` | `partially_supported` | The design supports alternative definitions, but not an ex ante robustness conclusion. |
| `RUN_20260527_234026_24_openclaw_deepseekv4pro_isolated_CL010` | `C016` | `level2` | `supported` | `partially_supported` | `partially_supported` | Replace the strong attrition claim with the weaker statement that attrition should be diagnosed rather than assumed harmless. |
| `RUN_20260528_000312_29_openclaw_deepseekv4pro_isolated_CL007` | `C019` | `level3` | `supported` | `partially_supported` | `partially_supported` | The claim reaches beyond the most directly identified route-induced spending effect, so the weaker label is more defensible. |
| `RUN_20260528_000656_30_openclaw_deepseekv4pro_isolated_CL006` | `C019` | `perturbed` | `partially_supported` | `unsupported` | `unsupported` | The second-pass stricter label is more faithful to the gold reference: the proxy is useful but not validated enough to support the claim as stated. |
| `RUN_20260528_001055_31_openclaw_deepseekv4pro_isolated_CL007` | `C020` | `level2` | `supported` | `unsupported` | `unsupported` | The second-pass label is adopted because the gold explicitly warns against a pure digit-processing interpretation at this strength. |
| `RUN_20260528_001721_33_openclaw_deepseekv4pro_isolated_CL005` | `C020` | `perturbed` | `supported` | `unsupported` | `unsupported` | Under the bundled perturbed treatment, attributing heterogeneity to standalone format sensitivity is too strong. |
