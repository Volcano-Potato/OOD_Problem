<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C001 -->

# Perturbed Variant Construction Note

## Purpose

Break the exogenous assignment of the pre-contact avoidance channel while keeping the fundraising setting and outcomes comparable.

## Base Identification Condition

- changed_condition_category: assignment mechanism
- base_condition: The solicitation-process condition is researcher-assigned at the contact-opportunity level.
- why_it_supports_identification: Exogenous assignment lets the design interpret differences in contact and giving as responses to the solicitation condition rather than to self-selection into the condition.
- where_it_appears_in_base_task: `agent_task_level2.md` and `agent_task_level3.md` under `assignment or variation source`.

## Perturbation

- changed_condition: Households choose whether to receive pre-contact notice or indicate a preference not to be approached after hearing about the campaign beforehand.
- variant_file: `agent_task_perturbed.md`
- why_original_strategy_is_weaker_or_invalid: The original mechanism logic relies on exogenous variation in the avoidance channel. Once households self-select into the pre-contact condition, differences in contact and giving can reflect underlying discomfort, altruism, or availability rather than the causal effect of the condition itself.
- does_this_weaken_invalidate_or_redirect_the_base_design: invalidates the clean mechanism test unless the agent proposes new randomization, encouragement, or strong additional assumptions.
- which_original_claims_should_no_longer_be_valid: Any claim that observed differences across pre-contact conditions cleanly identify social-pressure effects.

## Expected Strong-Agent Response

- what_a_good_agent_should_say: The self-selected pre-contact condition makes the original mechanism comparison endogenous. The agent should either downgrade the design to descriptive/selection analysis or propose a new source of exogenous variation.
- correct_design_adjustment: Re-randomize the pre-contact condition, use a valid encouragement or instrument, or explicitly analyze selection into avoidance as an outcome rather than a treatment effect.
- claims_that_should_be_weakened: Claims about causal separation of altruism and pressure.
- additional_assumptions_or_data_needed: New randomization, pre-treatment covariates strong enough for selection adjustment, or a plausible instrument for pre-contact choice.
- what_should_not_be_claimed: That differences across chosen pre-contact conditions reveal social pressure causally.

## Expected Failure Pattern

- likely_bad_agent_response: Reuse the base design as if the pre-contact condition were still randomized and interpret lower contact or giving as causal evidence of pressure.
- expected_error_types: endogenous-treatment blindness; mechanical reuse of base mechanism design; unsupported causal mechanism claim
- [x] Mechanical reuse of base design
- [x] Ignoring changed assignment mechanism
- [ ] Ignoring changed timing structure
- [ ] Ignoring changed measurement structure
- [x] Unsupported causal or mechanism claim

## Gold Delta

| base gold element | perturbed status | explanation |
|---|---|---|
| Exogenous comparison across solicitation conditions | invalid | The key condition is now self-selected rather than assigned. |
| Contact and giving as joint mechanism outcomes | still valid | These outcomes still matter, but no longer identify the mechanism causally on their own. |
| Mechanism separation between altruism and pressure | weakened | It now requires new exogenous variation or much weaker interpretation. |
