<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C005 -->

# Perturbed Variant Construction Note

## Purpose

Remove the clean opportunity-side control construction while preserving the same campaign and outcome environment.

## Base Identification Condition

- changed_condition_category: exposure measurement
- base_condition: The researcher can identify untreated users who had the same opportunity to receive the focal ad.
- why_it_supports_identification: This is what makes exposed users comparable to a relevant untreated counterfactual rather than to all unexposed users.
- where_it_appears_in_base_task: `agent_task_level2.md` and `agent_task_level3.md` in the treatment/exposure description and exposure-opportunity logic.

## Perturbation

- changed_condition: The platform retains campaign assignment and actual impression logs but not opportunity-side logs for untreated users.
- variant_file: `agent_task_perturbed.md`
- why_original_strategy_is_weaker_or_invalid: Without opportunity-side logs, the base exposed-user counterfactual cannot be constructed directly. The researcher may still estimate an assignment-level effect, but not the same exposed-user lift estimand.
- does_this_weaken_invalidate_or_redirect_the_base_design: redirects the task from clean exposed-user lift toward assignment or eligibility effects unless new logging is added.
- which_original_claims_should_no_longer_be_valid: Claims about causal lift for users who actually had the relevant opportunity to see the focal ad.

## Expected Strong-Agent Response

- what_a_good_agent_should_say: The original exposed-user comparison is no longer directly available. The agent should either downgrade to an assignment-level estimand or request additional opportunity-side logging.
- correct_design_adjustment: Estimate intent-to-treat or assignment effects, or redesign the logging architecture so untreated opportunity-side counterparts can be observed.
- claims_that_should_be_weakened: Claims about exposed-user causal lift.
- additional_assumptions_or_data_needed: New opportunity-side logs, validated simulation of untreated opportunities, or a clearly redefined estimand.
- what_should_not_be_claimed: That actual exposed users can still be compared causally to untreated users as if the missing opportunity-side records did not matter.

## Expected Failure Pattern

- likely_bad_agent_response: Reuse the base exposed-user design or compare exposed users to all unexposed users without acknowledging that the key counterfactual is no longer observed.
- expected_error_types: estimand confusion; endogenous-exposure error; mechanical reuse of base design
- [x] Mechanical reuse of base design
- [ ] Ignoring changed assignment mechanism
- [ ] Ignoring changed timing structure
- [x] Ignoring changed measurement structure
- [x] Unsupported causal or mechanism claim

## Gold Delta

| base gold element | perturbed status | explanation |
|---|---|---|
| Opportunity-matched untreated controls | invalid | The required control-group logs are unavailable. |
| Assignment-level experimentation | still valid | Random assignment may still support a campaign-level effect. |
| Exposed-user lift estimand | weakened | It now requires additional data or a different design. |
