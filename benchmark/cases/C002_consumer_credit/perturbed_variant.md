<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C002 -->

# Perturbed Variant Construction Note

## Purpose

Break the blindness-to-later-terms assumption while preserving the staged credit setting.

## Base Identification Condition

- changed_condition_category: information structure
- base_condition: Borrowers do not know the later contract-term realization when deciding whether to apply or accept.
- why_it_supports_identification: This preserves a distinction between selection at take-up and post-borrowing incentives or burdens.
- where_it_appears_in_base_task: `agent_task_level2.md` and `agent_task_level3.md` in the staged timing and institutional-detail descriptions.

## Perturbation

- changed_condition: Borrowers are informed before application that final contract terms may differ from the initial offer and are shown how those later terms can be determined.
- variant_file: `agent_task_perturbed.md`
- why_original_strategy_is_weaker_or_invalid: Once borrowers know the later contract structure at take-up, selection can occur on expected final terms, so the original post-selection comparison no longer isolates adverse selection from repayment burden in the same way.
- does_this_weaken_invalidate_or_redirect_the_base_design: invalidates the clean surprise-contract logic and redirects the task toward a different design or a weaker interpretation.
- which_original_claims_should_no_longer_be_valid: Claims that common final terms across borrowers with different initial offers isolate adverse selection.

## Expected Strong-Agent Response

- what_a_good_agent_should_say: The key separation between take-up selection and later contract terms is broken because borrowers can select with knowledge of later terms.
- correct_design_adjustment: Propose a new design in which later terms are unknown at take-up, or downgrade the analysis to reduced-form price and selection effects with explicit caveats.
- claims_that_should_be_weakened: Clean adverse-selection identification from the offer-versus-contract comparison.
- additional_assumptions_or_data_needed: Evidence that borrowers ignored later-term information, a new surprise-based randomization, or a different incentive margin that is truly post-borrowing.
- what_should_not_be_claimed: That the same staged comparison still separates adverse selection from post-borrowing incentives causally.

## Expected Failure Pattern

- likely_bad_agent_response: Reuse the base staged design as if later contract terms were still hidden at application time.
- expected_error_types: ignored information timing; mechanism confounding; unsupported adverse-selection claim
- [x] Mechanical reuse of base design
- [ ] Ignoring changed assignment mechanism
- [x] Ignoring changed timing structure
- [ ] Ignoring changed measurement structure
- [x] Unsupported causal or mechanism claim

## Gold Delta

| base gold element | perturbed status | explanation |
|---|---|---|
| Surprise-based separation of offer and final terms | invalid | Borrowers can now select with knowledge of later terms. |
| Repayment outcomes as post-origination outcomes | still valid | Repayment is still observed, but its interpretation changes. |
| Adverse selection versus incentive separation | weakened | The original identifying comparison is no longer clean. |
