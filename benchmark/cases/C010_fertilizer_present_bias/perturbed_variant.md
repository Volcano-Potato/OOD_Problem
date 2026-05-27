<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C010 -->

# Perturbed Variant Construction Note

## Purpose

Keep the same seasonal-input environment while changing the information structure so that later offers are anticipated in advance.

## Base Identification Condition

- changed_condition_category: timing and information structure
- base_condition: Producers do not know in advance whether a later offer window will be available, so the early intervention changes the timing of the decision itself.
- why_it_supports_identification: It helps isolate procrastination or follow-through because producers must decide early rather than planning around a later announced option.
- where_it_appears_in_base_task: `agent_task_level2.md` and `agent_task_level3.md` in the early-versus-late offer structure.

## Perturbation

- changed_condition: Every producer learns at the start of the season whether and when a later offer will occur.
- variant_file: `agent_task_perturbed.md`
- why_original_strategy_is_weaker_or_invalid: If later offers are anticipated from the beginning, producers can plan around them, so differences between early and later arms no longer isolate the same procrastination or follow-through mechanism.
- does_this_weaken_invalidate_or_redirect_the_base_design: weakens and partly redirects the design toward expectations and anticipation rather than pure timing-based commitment.
- which_original_claims_should_no_longer_be_valid: Strong claims that the early effect reveals procrastination or present-bias through unanticipated timing alone.

## Expected Strong-Agent Response

- what_a_good_agent_should_say: The early-versus-late comparison is now harder to interpret because later offers are known in advance. The mechanism test is weaker and may capture planning responses rather than failure to follow through.
- correct_design_adjustment: Reframe the estimand, add an arm that withholds advance information about later offers, or downgrade the strength of mechanism claims.
- claims_that_should_be_weakened: Clean procrastination or commitment interpretation from early-versus-late differences.
- additional_assumptions_or_data_needed: Evidence that advance information does not change savings or planning behavior, or a new experimental arm that restores the original information structure.
- what_should_not_be_claimed: That the original timing-based mechanism test still works unchanged.

## Expected Failure Pattern

- likely_bad_agent_response: Reuse the base mechanism story and ignore that anticipation of later offers changes the decision environment.
- expected_error_types: mechanical reuse of base design; ignoring changed timing structure; unsupported mechanism claim
- [x] Mechanical reuse of base design
- [ ] Ignoring changed assignment mechanism
- [x] Ignoring changed timing structure
- [ ] Ignoring changed measurement structure
- [x] Unsupported causal or mechanism claim

## Gold Delta

| base gold element | perturbed status | explanation |
|---|---|---|
| Early-versus-late timing contrast | weakened | Later offers are now anticipated in advance. |
| Randomized offer assignment | still valid | Experimental variation remains. |
| Strong procrastination interpretation | weakened | Planning and anticipation now contaminate the mechanism test. |
