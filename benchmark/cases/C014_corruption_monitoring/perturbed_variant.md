<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C014 -->

# Perturbed Variant Construction Note

## Purpose

Remove the independent outcome measurement while preserving the randomized monitoring environment.

## Base Identification Condition

- changed_condition_category: outcome measurement
- base_condition: Corruption or leakage is measured using outcome data not controlled solely by the implementing officials.
- why_it_supports_identification: Independent measurement prevents official records from serving as both the treatment environment and the sole outcome source.
- where_it_appears_in_base_task: `agent_task_level2.md` and `agent_task_level3.md` in the outcome variable, data structure, and institutional-detail sections.

## Perturbation

- changed_condition: Independent post-completion measurement is unavailable, so the researcher observes only official project reports and related administrative records as outcomes.
- variant_file: `agent_task_perturbed.md`
- why_original_strategy_is_weaker_or_invalid: The base corruption outcome is no longer available. Official records may respond to monitoring through reporting behavior, concealment, or bookkeeping rather than through true reductions in leakage.
- does_this_weaken_invalidate_or_redirect_the_base_design: invalidates corruption-outcome identification and redirects the task toward reported-spending outcomes unless new independent measurement is added.
- which_original_claims_should_no_longer_be_valid: Claims that the design identifies true corruption reduction or missing expenditures.

## Expected Strong-Agent Response

- what_a_good_agent_should_say: Official records alone are not a clean corruption outcome. The agent should either collect independent measurement or downgrade the estimand to effects on reported expenditures, reporting compliance, or administrative behavior.
- correct_design_adjustment: Propose third-party audits, engineering or quality inspections, supplier verification, or other independent hard outcomes; otherwise redefine the question around official reporting rather than corruption itself.
- claims_that_should_be_weakened: Any claim about true leakage reduction.
- additional_assumptions_or_data_needed: Independent technical measurement, supplier or wage verification, quality audits, or other objective post-completion evidence.
- what_should_not_be_claimed: That changes in official reports alone measure corruption reduction.

## Expected Failure Pattern

- likely_bad_agent_response: Reuse the base audit design and treat official spending records as a clean corruption outcome.
- expected_error_types: measurement credulity; mechanical reuse of base design; unsupported corruption claim
- [x] Mechanical reuse of base design
- [ ] Ignoring changed assignment mechanism
- [ ] Ignoring changed timing structure
- [x] Ignoring changed measurement structure
- [x] Unsupported causal or mechanism claim

## Gold Delta

| base gold element | perturbed status | explanation |
|---|---|---|
| Independent cost or quality measurement | invalid | The key outcome source is gone. |
| Randomized monitoring assignment | still valid | Monitoring variation may still be exogenous. |
| Corruption or missing-expenditure estimand | weakened | The remaining data support only reported-record outcomes unless new measurement is added. |
