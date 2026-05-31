# Perturbed Pair Audit

- Mechanical reuse headline: `9/10` perturbed cases show mechanical reuse under broken identification.
- Counting rule: `yes` means the key identifying condition is explicitly broken in the perturbed packet, but the agent still retains the base estimand, base identification logic, or only surface-level threat wording.

| Case | Broken Condition | Mechanical Reuse | Rationale |
|---|---|---|---|
| `C001` | pre-contact state is no longer researcher-assigned; households self-select into pre-contact availability | `yes` | The perturbed packet breaks clean assignment of pre-contact state, but the output continues to reason as if the base decomposition remains available. |
| `C002` | borrowers are no longer cleanly blind to later terms at take-up | `yes` | The output does not fully re-scope the estimand after the key timing condition is weakened. |
| `C004` | ad-availability variation is manager-chosen rather than exogenous | `yes` | The output downgrades somewhat, but not enough to stop using the broken assignment as if it still carried causal identification. |
| `C005` | untreated opportunity-side logs are removed | `yes` | This is the clearest mechanical reuse case in the benchmark. |
| `C008` | untreated comparison stores/products are no longer available in the original clean form | `yes` | The output preserves more of the base comparison logic than the perturbed packet supports. |
| `C010` | later offer is known in advance, weakening timing-based procrastination separation | `yes` | The output softens the claim but still reuses the base mechanism story too directly. |
| `C014` | independent outcome measurement is removed; only official reports remain | `yes` | The output does not fully absorb the measurement breakdown. |
| `C016` | objective downstream outcome is removed, leaving selected self-reports | `yes` | The output weakens some claims but still reuses the base behavioral interpretation too aggressively. |
| `C019` | clean pre-trip basket capture is removed | `no` | The output still stretches some assumptions, but it does recognize the main design downgrade and proposes a weaker approach. |
| `C020` | price ending is bundled with markdown/sale framing | `yes` | The output does not fully abandon the base mechanism separation after bundling is introduced. |
