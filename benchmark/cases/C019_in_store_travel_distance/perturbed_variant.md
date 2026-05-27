<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C019 -->

# Perturbed Variant Construction Note

## Purpose

Keep the same retail-navigation environment while removing the validated pre-trip shopping-plan information that underpins the base observational design.

## Base Identification Condition

- changed_condition_category: pre-treatment information structure
- base_condition: The base task includes a reliable pre-trip basket or mission capture that can be used to build a route benchmark and control for shopping mission.
- why_it_supports_identification: It allows route-based variation to be determined before in-trip spending and route deviations occur.
- where_it_appears_in_base_task: `agent_task_level2.md` and `agent_task_level3.md` in the staged data description and pre-trip variable set.

## Perturbation

- changed_condition: No validated pre-trip basket or mission information is available.
- variant_file: `agent_task_perturbed.md`
- why_original_strategy_is_weaker_or_invalid: Without pre-trip planning information, the original reference-route logic becomes much weaker because the analyst cannot separate planned route demands from realized endogenous wandering.
- does_this_weaken_invalidate_or_redirect_the_base_design: weakens and largely invalidates the original observational IV-style route benchmark.
- which_original_claims_should_no_longer_be_valid: Strong claims that the analyst can identify the causal effect of route length from observational route data alone.

## Expected Strong-Agent Response

- what_a_good_agent_should_say: The original route-benchmark logic no longer works cleanly because the design lacks a pre-trip measure of intended purchases or mission. Causal claims should be downgraded unless a new randomized route-inducing intervention is added.
- correct_design_adjustment: Propose a new experimental manipulation, add validated pre-trip intention capture, or downgrade to descriptive analysis.
- claims_that_should_be_weakened: Clean causal interpretation of observed route length.
- additional_assumptions_or_data_needed: Reliable pre-trip basket capture, randomized path-inducing prompts, or another exogenous source of route variation.
- what_should_not_be_claimed: That observed route logs plus checkout data alone preserve the base design's identification strength.

## Expected Failure Pattern

- likely_bad_agent_response: Reuse the base IV or pre-trip route-benchmark logic even though the necessary pre-trip planning information is gone.
- expected_error_types: mechanical reuse of base design; ignoring changed information structure; unsupported causal claim
- [x] Mechanical reuse of base design
- [ ] Ignoring changed assignment mechanism
- [x] Ignoring changed timing structure
- [ ] Ignoring changed measurement structure
- [x] Unsupported causal or mechanism claim

## Gold Delta

| base gold element | perturbed status | explanation |
|---|---|---|
| Pre-trip route benchmark from planned basket | invalid | The necessary pre-trip basket information is no longer observed. |
| Route endogeneity concern | still valid | The core problem remains. |
| Randomized path-inducing intervention as alternative | still valid | A new experimental route shifter could still identify a causal effect. |
