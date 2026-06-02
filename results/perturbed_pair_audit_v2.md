# Perturbed Pair Audit (research_agent_v2_search)

- Mechanical reuse headline: `0/10` perturbed cases show mechanical reuse under broken identification.
- Counting rule: `yes` means the key identifying condition is explicitly broken in the perturbed packet, but the agent still retains the base estimand, base identification logic, or only surface-level threat wording.

| Case | Broken Condition | Mechanical Reuse | Rationale |
|---|---|---|---|
| `C001` | pre-contact state is no longer researcher-assigned; households self-select into pre-contact availability | `no` | The final memo no longer preserves a point-identified pressure-versus-altruism estimand and explicitly treats the perturbation as fatal to the base causal design. |
| `C002` | borrowers are no longer cleanly blind to later terms at take-up | `no` | The final memo explicitly states that the Karlan-Zinman style decomposition is not identified once later terms are anticipated, so the base selection-versus-incentive logic is not retained. |
| `C004` | ad-availability variation is manager-chosen rather than exogenous | `no` | The memo fully abandons the exogenous-assignment logic rather than trying to salvage causal ad-availability effects with a weakened observational design. |
| `C005` | untreated opportunity-side logs are removed | `no` | Unlike v1, the final memo no longer preserves a secondary causal actual-exposure estimand; the base exposed-user logic is explicitly treated as not identified under the perturbation. |
| `C008` | untreated comparison stores/products are no longer available in the original clean form | `no` | Unlike v1, the memo does not retain a secondary within-store DiD or salience-gradient causal story after the untreated comparison structure is removed. |
| `C010` | later offer is known in advance, weakening timing-based procrastination separation | `no` | The memo no longer treats the timing contrast as identifying procrastination once the later offer is anticipated. |
| `C014` | independent outcome measurement is removed; only official reports remain | `no` | The memo fully absorbs the measurement breakdown and no longer interprets official records as clean corruption outcomes. |
| `C016` | objective downstream outcome is removed, leaving selected self-reports | `no` | The final memo treats self-reports as a distinct reporting outcome rather than reusing the base interpretation of actual behavioral change. |
| `C019` | clean pre-trip basket capture is removed | `no` | The memo preserves the same broad downgrade discipline as v1 and does not attempt to keep the base incremental-spending identification logic. |
| `C020` | price ending is bundled with markdown/sale framing | `no` | The final memo does not preserve the base mechanism-separation claim after price endings and promotion framing become perfectly bundled. |
