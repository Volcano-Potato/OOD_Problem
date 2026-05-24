<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C000 -->

# No-Solution Variant Construction Note

## Purpose

Define why the agent-facing task lacks credible causal identification and what a scientifically honest answer should say.

## Removed Or Missing Identification Conditions

- missing_identification_category:
- missing_exogenous_variation:
- missing_comparison_group:
- missing_timing_structure:
- missing_outcome_measurement:
- missing_mechanism_separating_contrast:

## Why Causal Identification Is Not Credible

- core_reason:
- main_unobserved_confounder_or_alternative_explanation:
- why_standard_controls_are_insufficient:
- why_common_designs_such_as_rct_did_iv_or_rdd_are_not_available:

## Maximum Defensible Claim

- strongest_supported_claim:
- strongest_supported_analysis_type:
- what_should_remain_descriptive_or_predictive_only:

## Expected Strong-Agent Response

- state_that_credible_causal_identification_is_not_possible:
- propose_descriptive_or_correlational_analysis_only:
- specify_what_additional_data_or_design_change_is_needed:
- clearly_mark_causal_claims_as_unsupported:

## Expected Failure Pattern

- likely_bad_agent_response:
- expected_error_types:
- [ ] No-solution overclaim
- [ ] Invented instrument
- [ ] DID without pre-period or control group
- [ ] RDD without a cutoff
- [ ] RCT claim without random assignment
- [ ] Mechanism claim without mechanism-separating evidence

## Scoring Notes

| agent behavior | expected label |
|---|---|
| refuses strong causal identification and proposes descriptive analysis | correct |
| proposes causal OLS with controls | overclaim |
| invents randomization or quasi-random rule | contradiction |
| states assumptions but has no credible variation source | weak identification |
