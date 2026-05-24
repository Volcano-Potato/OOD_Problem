<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C008 -->

# Perturbed Variant Construction Note

## Purpose

Remove untreated comparison stores while keeping the treated-store retail setting intact.

## Base Identification Condition

- changed_condition_category: comparison structure
- base_condition: The design includes untreated comparison stores in addition to treated and untreated product groups.
- why_it_supports_identification: Comparison stores help separate the intervention from store-wide time shocks and support stronger trend validation.
- where_it_appears_in_base_task: `agent_task_level2.md` and `agent_task_level3.md` in the data structure and institutional detail sections.

## Perturbation

- changed_condition: The data no longer include untreated comparison stores; only treated and untreated product groups within the focal store are observed over time.
- variant_file: `agent_task_perturbed.md`
- why_original_strategy_is_weaker_or_invalid: The stronger cross-store comparison is unavailable, so the original multi-market logic becomes weaker. The agent may still use within-store category comparisons, but store-wide time shocks become harder to rule out.
- does_this_weaken_invalidate_or_redirect_the_base_design: weakens rather than fully invalidates the original design.
- which_original_claims_should_no_longer_be_valid: Strong claims that category-level changes are cleanly separated from store-wide time shocks using untreated markets.

## Expected Strong-Agent Response

- what_a_good_agent_should_say: The loss of untreated stores weakens identification. A within-store treated-versus-control category design may still be possible, but it requires stronger assumptions and weaker claims.
- correct_design_adjustment: Use within-store category-by-time comparisons, test pre-trends carefully, control for prices and promotions, and explicitly acknowledge the missing untreated-market comparison.
- claims_that_should_be_weakened: Strong causal salience claims insulated from store-level shocks.
- additional_assumptions_or_data_needed: Comparison-store data, randomized rollout, or additional untreated markets to recover the stronger design.
- what_should_not_be_claimed: That the original richer comparison structure is still available.

## Expected Failure Pattern

- likely_bad_agent_response: Reuse the base multi-market design language or claim that store-wide shocks are already controlled even though untreated stores are absent.
- expected_error_types: overclaim from missing control markets; mechanical reuse of base design; ignored timing-shock risk
- [x] Mechanical reuse of base design
- [ ] Ignoring changed assignment mechanism
- [x] Ignoring changed timing structure
- [ ] Ignoring changed measurement structure
- [x] Unsupported causal or mechanism claim

## Gold Delta

| base gold element | perturbed status | explanation |
|---|---|---|
| Untreated comparison stores | invalid | The cross-store comparison is unavailable. |
| Within-store treated-versus-control categories | still valid | This comparison remains usable but is weaker. |
| Strong protection against store-wide shocks | weakened | Additional assumptions are now needed. |
