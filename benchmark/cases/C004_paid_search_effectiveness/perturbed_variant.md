<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C004 -->

# Perturbed Variant Construction Note

## Purpose

Keep the same paid-search measurement environment while removing the exogenous market-level assignment that supports the base causal design.

## Base Identification Condition

- changed_condition_category: assignment mechanism
- base_condition: Paid-search availability differs across markets according to a planned exogenous or experimentally controlled rule.
- why_it_supports_identification: It makes market-level ad availability independent of short-run local demand shocks, allowing treated and untreated markets to serve as credible counterfactuals after appropriate trend controls.
- where_it_appears_in_base_task: `agent_task_level2.md` and `agent_task_level3.md` in the assignment or variation source and market-comparison structure.

## Perturbation

- changed_condition: Campaign managers choose where to reduce or suspend paid-search availability based on expected demand, budget pressure, or other operational judgments.
- variant_file: `agent_task_perturbed.md`
- why_original_strategy_is_weaker_or_invalid: The treatment timing and location are now endogenous to expected sales conditions, so the original market-comparison logic no longer has clean causal interpretation.
- does_this_weaken_invalidate_or_redirect_the_base_design: weakens and partially redirects the task toward observational panel analysis, sensitivity analysis, or a request for restored randomization.
- which_original_claims_should_no_longer_be_valid: Clean causal claims about the effect of ad availability on downstream sales from the observed market differences alone.

## Expected Strong-Agent Response

- what_a_good_agent_should_say: The original experimental logic no longer holds because assignment is chosen in response to expected demand. Stronger causal claims are not justified without a new source of exogenous variation.
- correct_design_adjustment: Downgrade to descriptive or weakly quasi-experimental analysis, emphasize pre-trend diagnostics and sensitivity limits, or ask for restored randomization or an external shock.
- claims_that_should_be_weakened: Claims of causal ad lift and strong segment-level causal heterogeneity.
- additional_assumptions_or_data_needed: Pre-committed randomization, an externally imposed policy change, or another clearly exogenous source of ad-availability variation.
- what_should_not_be_claimed: That treated-versus-untreated market comparisons remain causal just because repeated market-time data are available.

## Expected Failure Pattern

- likely_bad_agent_response: Reuse the base market-level experiment logic and treat manager-chosen suspension as if it were random or as-if random.
- expected_error_types: mechanical reuse of base design; timing endogeneity; endogenous assignment overclaim
- [x] Mechanical reuse of base design
- [x] Ignoring changed assignment mechanism
- [ ] Ignoring changed timing structure
- [ ] Ignoring changed measurement structure
- [x] Unsupported causal or mechanism claim

## Gold Delta

| base gold element | perturbed status | explanation |
|---|---|---|
| Exogenous market-level ad-availability variation | invalid | The central experimental condition is removed. |
| Market-time comparison structure | still valid | Repeated panel structure remains useful descriptively. |
| Strong causal estimate of incremental sales | weakened | It now requires a new source of exogenous variation. |
| Segment-level heterogeneity interpretation | weakened | Segment differences are harder to interpret causally when assignment is endogenous. |
