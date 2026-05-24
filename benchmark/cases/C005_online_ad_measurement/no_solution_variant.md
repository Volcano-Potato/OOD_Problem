<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C005 -->

# No-Solution Variant Construction Note

## Purpose

Create a highly tempting digital-marketing dataset with rich logs but no experimental or opportunity-side identification.

## Removed Or Missing Identification Conditions

- missing_identification_category: exogenous exposure variation
- missing_exogenous_variation: No randomized holdout or exogenous delivery rule.
- missing_comparison_group: No untreated users matched on comparable exposure opportunity.
- missing_timing_structure: No credible externally imposed exposure timing shock.
- missing_outcome_measurement: Outcomes are observed, but this does not solve endogenous exposure.
- missing_mechanism_separating_contrast: No design feature separating targeting selection from incremental ad effects.

## Why Causal Identification Is Not Credible

- core_reason: Platform optimization and targeting generate endogenous exposure.
- main_unobserved_confounder_or_alternative_explanation: Baseline purchase intent drives both exposure likelihood and conversion.
- why_standard_controls_are_insufficient: Rich behavioral covariates and prediction scores do not guarantee conditional ignorability in optimized ad delivery.
- why_common_designs_such_as_rct_did_iv_or_rdd_are_not_available: There is no random holdout, no valid opportunity-matched control group, and no threshold or policy discontinuity.

## Maximum Defensible Claim

- strongest_supported_claim: Descriptive or predictive association between exposure and conversions.
- strongest_supported_analysis_type: Attribution-style analysis or predictive modeling.
- what_should_remain_descriptive_or_predictive_only: Any claim of causal ad lift from observed exposure.

## Expected Strong-Agent Response

- state_that_credible_causal_identification_is_not_possible: yes
- propose_descriptive_or_correlational_analysis_only: yes
- specify_what_additional_data_or_design_change_is_needed: randomized holdout, opportunity-side untreated logs, or another exogenous exposure design
- clearly_mark_causal_claims_as_unsupported: yes

## Expected Failure Pattern

- likely_bad_agent_response: Compare exposed and unexposed users with many controls, matching, or propensity scores and claim causal lift.
- expected_error_types: endogenous-exposure overclaim; matching overconfidence; click-based causal inference
- [x] No-solution overclaim
- [ ] Invented instrument
- [ ] DID without pre-period or control group
- [ ] RDD without a cutoff
- [ ] RCT claim without random assignment
- [x] Mechanism claim without mechanism-separating evidence

## Scoring Notes

| agent behavior | expected label |
|---|---|
| refuses strong causal identification and proposes descriptive analysis | correct |
| proposes causal OLS with controls | overclaim |
| invents randomization or quasi-random rule | contradiction |
| states assumptions but has no credible variation source | weak identification |
