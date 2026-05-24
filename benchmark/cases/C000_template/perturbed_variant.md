<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C000 -->

# Perturbed Variant Construction Note

## Purpose

Define exactly how the perturbed agent-facing task differs from the base case and what behavior should be expected from a strong agent.

## Base Identification Condition

- changed_condition_category:
- base_condition:
- why_it_supports_identification:
- where_it_appears_in_base_task:

## Perturbation

- changed_condition:
- variant_file:
- why_original_strategy_is_weaker_or_invalid:
- does_this_weaken_invalidate_or_redirect_the_base_design:
- which_original_claims_should_no_longer_be_valid:

## Expected Strong-Agent Response

- what_a_good_agent_should_say:
- correct_design_adjustment:
- claims_that_should_be_weakened:
- additional_assumptions_or_data_needed:
- what_should_not_be_claimed:

## Expected Failure Pattern

- likely_bad_agent_response:
- expected_error_types:
- [ ] Mechanical reuse of base design
- [ ] Ignoring changed assignment mechanism
- [ ] Ignoring changed timing structure
- [ ] Ignoring changed measurement structure
- [ ] Unsupported causal or mechanism claim

## Gold Delta

| base gold element | perturbed status | explanation |
|---|---|---|
|  | still valid / weakened / invalid |  |
