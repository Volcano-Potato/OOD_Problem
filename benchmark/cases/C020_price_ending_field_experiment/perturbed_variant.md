<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C020 -->

# Perturbed Variant Construction Note

## Purpose

Keep the same product-offer field-experiment environment while removing the independent variation that lets the researcher separate terminal-digit format from markdown or sale signaling.

## Base Identification Condition

- changed_condition_category: mechanism separation
- base_condition: The price-ending format can be varied across comparable offer versions without forcing the same movement in explicit markdown or sale cues.
- why_it_supports_identification: It allows the design to attribute demand differences to the terminal-digit format itself, or at least to test whether the effect survives after separating format from promotion signaling.
- where_it_appears_in_base_task: `agent_task_level2.md` and `agent_task_level3.md` in the treatment definition, causal mechanisms, and threat structure.

## Perturbation

- changed_condition: Every version using the salient terminal-digit format is also explicitly presented as a markdown or sale offer, while alternative endings appear only without that framing.
- variant_file: `agent_task_perturbed.md`
- why_original_strategy_is_weaker_or_invalid: Assignment may still be randomized, but the treatment no longer isolates the price-ending format itself. The design now identifies a bundled effect of ending format plus promotional framing.
- does_this_weaken_invalidate_or_redirect_the_base_design: weakens and redirects the task toward a bundled-treatment interpretation or a request for orthogonal variation.
- which_original_claims_should_no_longer_be_valid: Clean causal claims about the terminal-digit format itself, and any claim that a measured effect proves a pure threshold-pricing mechanism.

## Expected Strong-Agent Response

- what_a_good_agent_should_say: The assignment may still identify the causal effect of the bundled presentation, but it no longer isolates the terminal-digit format from sale signaling.
- correct_design_adjustment: Recast the estimand as a combined treatment effect, request orthogonal variation in sale cues, or propose a factorial experiment.
- claims_that_should_be_weakened: Claims about the standalone ending-format effect and its pure mechanism.
- additional_assumptions_or_data_needed: Independent variation in markdown or sale presentation, or a design that holds all non-ending cues fixed.
- what_should_not_be_claimed: That the original base-task mechanism can still be identified from the perturbed data alone.

## Expected Failure Pattern

- likely_bad_agent_response: Reuse the base experiment logic and continue to interpret the estimate as the pure effect of the terminal-digit ending.
- expected_error_types: mechanical reuse of base design; mechanism confounding; unsupported psychological-mechanism claim
- [x] Mechanical reuse of base design
- [x] Ignoring changed assignment mechanism
- [ ] Ignoring changed timing structure
- [x] Ignoring changed measurement structure
- [x] Unsupported causal or mechanism claim

## Gold Delta

| base gold element | perturbed status | explanation |
|---|---|---|
| Randomized ending-format variation | still valid | Assignment can remain randomized. |
| Standalone ending-format estimand | invalid | Ending format is now bundled with promotion framing. |
| Demand effect of bundled offer presentation | still valid | The combined treatment can still be studied causally. |
| Pure threshold-psychology interpretation | weakened | It now requires additional independent variation. |
