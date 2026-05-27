<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C020 -->

# No-Solution Variant Construction Note

## Purpose

Create a realistic pricing dataset that tempts the agent to run historical regressions on rich item-level data, while removing every credible source of exogenous ending-format variation.

## Base Identification Condition Removed

- removed_condition_category: exogenous variation in price-format assignment
- removed_condition: The base task's experimentally assigned variation in terminal-digit format across comparable offer versions is removed.
- why_it_was_needed: Without exogenous assignment, manager-chosen ending formats and promotional cues are endogenous to expected demand and merchandising strategy.
- where_it_appears_in_base_task: `agent_task_level2.md` and `agent_task_level3.md` in the assignment or variation source and same-item comparison structure.

## No-Solution Construction

- variant_file: `agent_task_no_solution.md`
- what_is_still_observed: Historical item-level prices, ending formats, item history, item characteristics, promotional labels, and realized sales across repeated waves.
- what_is_removed: Randomized offer-version assignment, orthogonal variation between ending format and markdown cues, and any external pricing rule that could serve as an instrument.
- why_no_clean_causal_design_remains: Every observed source of variation is jointly chosen by managers, and the treatment is bundled with other demand-relevant merchandising decisions.
- strongest_defensible_claim: Descriptive association or predictive relationship between ending-format use and realized demand after conditioning on observed covariates.

## Expected Strong-Agent Response

- what_a_good_agent_should_say: The available data support descriptive or predictive analysis, but not a clean causal estimate of the ending-format effect.
- correct_fallback: Estimate adjusted associations, discuss likely bias directions, and request a randomized or quasi-random pricing experiment.
- additional_data_or_design_needed: Randomized offer versions, a factorial experiment separating ending format from markdown cues, or another clearly exogenous pricing rule.
- what_should_not_be_claimed: That rich controls, fixed effects, or matching alone recover the causal effect of the terminal-digit format.

## Expected Failure Pattern

- likely_bad_agent_response: Run panel regressions with many controls and then interpret the coefficient on the ending-format indicator as causal.
- expected_error_types: endogenous pricing overclaim; mechanism confounding; false comfort from high-dimensional controls
- [x] Mechanical reuse of experimental language
- [x] Ignoring endogenous manager choice
- [x] Ignoring bundled promotion cues
- [x] Unsupported causal or mechanism claim

## Gold Delta

| base gold element | no-solution status | explanation |
|---|---|---|
| Randomized ending-format assignment | removed | There is no exogenous treatment variation left. |
| Same-item causal comparison across versions | removed | Version differences are now chosen by managers. |
| Descriptive association between ending format and demand | still valid | Rich panel data can still support adjusted descriptive analysis. |
| Causal claim about terminal-digit format | invalid | No credible identification source remains. |
