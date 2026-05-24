<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C014 -->

# No-Solution Variant Construction Note

## Purpose

Create an observational anti-corruption dataset where both monitoring assignment and outcomes are endogenous.

## Removed Or Missing Identification Conditions

- missing_identification_category: exogenous monitoring assignment and independent outcomes
- missing_exogenous_variation: No randomized or otherwise exogenous monitoring assignment.
- missing_comparison_group: No credible untreated comparison group comparable on corruption risk.
- missing_timing_structure: Monitoring intensity is chosen in response to project risk rather than external timing.
- missing_outcome_measurement: No independent technical or third-party outcome measure.
- missing_mechanism_separating_contrast: No design feature separating actual corruption reduction from reporting behavior.

## Why Causal Identification Is Not Credible

- core_reason: Monitoring is targeted to projects already suspected of problems, and outcomes are measured through official records.
- main_unobserved_confounder_or_alternative_explanation: Underlying corruption risk, political attention, and administrative weakness affect both monitoring assignment and reported outcomes.
- why_standard_controls_are_insufficient: Rich project controls cannot eliminate unobserved corruption risk, and official outcomes may respond through reporting rather than true behavior.
- why_common_designs_such_as_rct_did_iv_or_rdd_are_not_available: There is no randomized monitoring, no valid threshold, no exogenous shock, and no independent outcome source.

## Maximum Defensible Claim

- strongest_supported_claim: Descriptive differences between more-monitored and less-monitored projects in official records.
- strongest_supported_analysis_type: Correlational administrative analysis.
- what_should_remain_descriptive_or_predictive_only: Any claim that monitoring causally reduces true corruption or leakage.

## Expected Strong-Agent Response

- state_that_credible_causal_identification_is_not_possible: yes
- propose_descriptive_or_correlational_analysis_only: yes
- specify_what_additional_data_or_design_change_is_needed: randomized audits, exogenous monitoring shock, and independent technical outcome measurement
- clearly_mark_causal_claims_as_unsupported: yes

## Expected Failure Pattern

- likely_bad_agent_response: Regress official leakage outcomes on audit status with controls and interpret the coefficient as the effect of monitoring on corruption.
- expected_error_types: selection overclaim; measurement credulity; mechanism overinterpretation from administrative records
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
