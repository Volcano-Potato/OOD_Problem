# Perturbed Pair Audit (research_agent_v1)

- Mechanical reuse headline: `2/10` perturbed cases show mechanical reuse under broken identification.
- Counting rule: `yes` means the key identifying condition is explicitly broken in the perturbed packet, but the agent still retains the base estimand, base identification logic, or only surface-level threat wording.

| Case | Broken Condition | Mechanical Reuse | Rationale |
|---|---|---|---|
| `C001` | pre-contact state is no longer researcher-assigned; households self-select into pre-contact availability | `no` | The final memo explicitly says the perturbation is fatal to the base causal design and downgrades claims to descriptive or bound-based statements rather than preserving the original decomposition. |
| `C002` | borrowers are no longer cleanly blind to later terms at take-up | `no` | The output no longer claims that selection and incentive effects remain separately identified; the surviving fixed-effects design targets a different, weaker incentive-margin estimand. |
| `C004` | ad-availability variation is manager-chosen rather than exogenous | `no` | The memo fully abandons the broken exogeneity logic instead of trying to salvage causal ad-availability effects with surface-level threat language. |
| `C005` | untreated opportunity-side logs are removed | `yes` | The final memo does downgrade the headline estimand, but it still preserves a causal actual-exposure LATE despite the packet removing the clean opportunity-side support that made the base exposed-user logic credible. |
| `C008` | untreated comparison stores/products are no longer available in the original clean form | `yes` | The clean untreated comparison is gone, yet the memo still leans on treated-versus-untreated within-store comparisons and salience-pattern interpretation rather than fully dropping the base comparison design. |
| `C010` | later offer is known in advance, weakening timing-based procrastination separation | `no` | The output stops short of reusing the base procrastination story and clearly states that timing and anticipation are now fused. |
| `C014` | independent outcome measurement is removed; only official reports remain | `no` | The memo treats administrative reports as the only credible outcome target left and does not keep the base corruption-reduction interpretation. |
| `C016` | objective downstream outcome is removed, leaving selected self-reports | `no` | The final memo absorbs the measurement breakdown and no longer treats self-reports as if they identified actual behavioral change. |
| `C019` | clean pre-trip basket capture is removed | `no` | The memo fully downgrades to non-causal route-spending associations and does not preserve the base incremental-spending identification logic. |
| `C020` | price ending is bundled with markdown/sale framing | `no` | The output no longer claims that ending-format effects can be separated from promotion effects; the remaining bundle discussion changes the estimand rather than reusing the base mechanism separation. |
