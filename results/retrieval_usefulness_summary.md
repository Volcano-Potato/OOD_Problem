# Retrieval Usefulness Audit (research_agent_v2_search)

## Scope

- Arm: `research_agent_v2_search`
- Subset: `10` `perturbed` cases
- Source files:
  - [run_manifest.csv](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/run_manifest.csv)
  - [retrieval_usefulness_audit.csv](/Users/jiangcanxiang/Documents/OOD_Problem/results/retrieval_usefulness_audit.csv)
  - [research_agent_v2](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/raw_agent_logs/research_agent_v2)
  - [main](/Users/jiangcanxiang/Documents/OOD_Problem/outputs/raw_agent_logs/main)

## Labeling Rule

- `helpful`: retrieval materially sharpened the downgrade, rejection, or reframing of a candidate design.
- `neutral`: retrieval occurred, but the final design choice appears broadly the same as a strong packet-grounded critic run.
- `noisy`: retrieval ran and the final memo remained usable, but rate limits, irrelevant hits, or extra search churn added friction without clear benefit.
- `failed`: retrieval did not succeed well enough to support the final stage.

## Headline

- retrieval attempt rate: `10/10 = 100%`
- retrieval success rate: `10/10 = 100%`
- cases with zero actual tool use: `0/10`
- mean recorded retrieval tool calls: `16.7`
- min / max retrieval tool calls: `10 / 24`
- runs with non-empty retrieval failure notes: `2/10`

## Usefulness Distribution

- `helpful`: `6/10`
- `neutral`: `3/10`
- `noisy`: `1/10`
- `failed`: `0/10`

## Interpretation

- Retrieval is not merely nominal in `v2`; all `10` runs made real tool calls and all `10` completed Stage 2 successfully.
- The clearest retrieval wins are concentrated in:
  - `C005`, where retrieval helps eliminate the residual `actual exposure` / `LATE` salvage that survived in `v1`
  - `C008`, where retrieval on interference bias and contaminated untreated comparisons helps eliminate the residual within-store comparison salvage that survived in `v1`
- Additional clearly helpful cases are:
  - `C002`
  - `C004`
  - `C014`
  - `C016`
- Retrieval is not uniformly transformative:
  - `C001`, `C010`, and `C019` look more like `neutral` support than decisive upgrades
- Retrieval also introduces some cost:
  - `C020` logged rate-limit / off-target search noise even though the final memo still landed on the correct downgraded estimand

## Tool Mix

- `deepxiv__search_papers`: `10/10`
- `deepxiv__get_paper_brief`: `8/10`
- `web_search`: `5/10`
- `semantic-scholar__search_papers`: `5/10`
- other tools appear only occasionally and do not define the arm-level pattern

## Bottom Line

`research_agent_v2_search` shows real, stable retrieval behavior rather than merely exposing tools in the schema. The retrieval layer is helpful in a majority of cases, but its most important causal-design value is concentrated in the last residual reuse case left over from `v1` (`C005`) and in measurement-heavy perturbations (`C014`, `C016`).
