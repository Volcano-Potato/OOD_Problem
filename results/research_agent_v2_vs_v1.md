# research_agent_v2_search vs research_agent_v1

## Scope

- Comparator arms:
  - `research_agent_v1`
  - `research_agent_v2_search`
- Evaluation subset: `10` `perturbed` cases (`C001`, `C002`, `C004`, `C005`, `C008`, `C010`, `C014`, `C016`, `C019`, `C020`)
- Primary result source:
  - [perturbed_mechanical_reuse_v1.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/perturbed_mechanical_reuse_v1.csv)
  - [perturbed_mechanical_reuse_v2.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/perturbed_mechanical_reuse_v2.csv)
- Retrieval-behavior source:
  - [retrieval_usefulness_audit.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/retrieval_usefulness_audit.csv)
  - [run_manifest.csv](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/run_manifest.csv)

## Headline

- `research_agent_v1` `perturbed mechanical reuse`: `2/10`
- `research_agent_v2_search` `perturbed mechanical reuse`: `0/10`
- Absolute reduction from `v1` to `v2`: `-2/10 = -0.20`
- Relative reduction from `v1` to `v2`: `-100%`

Interpretation:
Within the perturbed subset, adding an explicit retrieval stage on top of the critic-and-reconcile loop removes the last two residual reuse cases left in `v1`.

## Where v2 Improves Over v1

The incremental gain is concentrated in two cases:

- `C005`
  - `v1`: still retained a supplementary causal `actual exposure` / `LATE` story
  - `v2`: explicitly rejects exposure-level identification and keeps only assignment-level `ITT` plus predictive `PIE`
- `C008`
  - `v1`: still retained a secondary within-store comparison / salience-gradient salvage
  - `v2`: fully downgrades to descriptive demand reallocation with no causal within-store rescue

All other cases show the same broad downgrade direction as `v1`, but `v2` often adds stronger methodological backing for why the downgrade is required.

## Retrieval Behavior

- retrieval attempted: `10/10`
- retrieval successful: `10/10`
- cases with zero actual tool use: `0/10`
- mean recorded retrieval tool calls: `16.7`
- retrieval usefulness labels:
  - `helpful`: `6/10`
  - `neutral`: `3/10`
  - `noisy`: `1/10`
  - `failed`: `0/10`

This means `v2` is not just a prompt rename or schema exposure change. It is a genuinely retrieval-using arm.

## Case-by-case Transition

| Case | `v1` | `v2` | Retrieval Effect |
|---|---:|---:|---|
| `C001` | `no` | `no` | neutral support |
| `C002` | `no` | `no` | helpful methodological backing |
| `C004` | `no` | `no` | helpful rejection of observational salvage |
| `C005` | `yes` | `no` | decisive improvement |
| `C008` | `yes` | `no` | decisive improvement |
| `C010` | `no` | `no` | neutral support |
| `C014` | `no` | `no` | helpful measurement clarification |
| `C016` | `no` | `no` | helpful measurement clarification |
| `C019` | `no` | `no` | neutral support |
| `C020` | `no` | `no` | noisy but still lands correctly |

## Cost-Benefit Reading

- Benefit:
  - removes the last `2/10` residual reuse failures left in `v1`
  - produces real, stable tool use
  - is especially helpful in packet settings where the perturbation creates a measurement or interference argument that external methodological literature can sharpen
- Cost:
  - more tool calls and more infrastructure dependency
  - occasional retrieval noise (`C020`)
  - claim-level summary metrics remain too optimistic under the current annotation-overrides regime

## Metrics Caveat

- [metrics_summary_research_agent_v2_search.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/metrics_summary_research_agent_v2_search.csv) is useful for execution counts and now carries the correct `Perturbed Mechanical Reuse Rate`.
- The broader claim-level headline values in that file remain provisional for the same reason as `v1`:
  - the annotation pipeline is still calibrated around frozen baseline run IDs rather than arm-specific override coverage
- For `task35`, the manual paired audit plus the retrieval-usefulness audit are the primary result sources.

## Go / No-Go Recommendation

**Recommendation: `go to v3`, but as a clean optional ablation rather than a mandatory rescue step.**

Why:

- `v2` already fixes the perturbed mechanical-reuse problem on this subset (`0/10`)
- the retrieval layer is real and usually useful, not fake
- the remaining rationale for `v3` is not "v2 is still broken"
- the rationale for `v3` is instead:
  - to test whether planner / debate structure adds anything beyond `critic + retrieval`
  - to see whether more agentic decomposition improves cases where retrieval is only neutral

If resources are tight, the project can stop at `v2` and still claim a clean result:
critic-only `v1` helps a lot, and retrieval-augmented `v2` removes the remaining residual reuse on the perturbed subset.
