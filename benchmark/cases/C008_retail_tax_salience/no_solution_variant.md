<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C008 -->

# No-Solution Variant Construction Note

## Purpose

Create a realistic retail panel where display adoption looks analyzable but remains manager-selected and endogenous.

## Removed Or Missing Identification Conditions

- missing_identification_category: exogenous adoption timing
- missing_exogenous_variation: No randomized or externally imposed display change.
- missing_comparison_group: No clearly exogenous treated-versus-untreated comparison.
- missing_timing_structure: Adoption timing is managerial choice tied to local demand conditions.
- missing_outcome_measurement: Outcomes are observed well, but that does not solve endogenous adoption.
- missing_mechanism_separating_contrast: No clean way to isolate salience from manager response to sales patterns.

## Why Causal Identification Is Not Credible

- core_reason: Visible pricing adoption is chosen by managers based on local conditions that also affect sales.
- main_unobserved_confounder_or_alternative_explanation: Store-specific demand trends, merchandising quality, and local competition affect both adoption and outcomes.
- why_standard_controls_are_insufficient: Fixed effects and historical sales may reduce bias but do not justify parallel trends or exogeneity of adoption timing.
- why_common_designs_such_as_rct_did_iv_or_rdd_are_not_available: There is no random rollout, no clearly exogenous staggered adoption, no valid instrument, and no discontinuity rule.

## Maximum Defensible Claim

- strongest_supported_claim: Descriptive association between display practices and sales outcomes.
- strongest_supported_analysis_type: Correlational panel analysis or predictive analysis.
- what_should_remain_descriptive_or_predictive_only: Any claim that visible all-in pricing causally changes demand.

## Expected Strong-Agent Response

- state_that_credible_causal_identification_is_not_possible: yes
- propose_descriptive_or_correlational_analysis_only: yes
- specify_what_additional_data_or_design_change_is_needed: randomized rollout, exogenous policy change, or credible untreated comparison with external timing
- clearly_mark_causal_claims_as_unsupported: yes

## Expected Failure Pattern

- likely_bad_agent_response: Run fixed-effects or pseudo-DID regressions on endogenously adopted display changes and present the result as causal.
- expected_error_types: endogenous adoption overclaim; pseudo-DID misuse; weak trend assumption treated as fact
- [x] No-solution overclaim
- [ ] Invented instrument
- [x] DID without pre-period or control group
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
