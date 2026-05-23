<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C000 -->

# No-Solution Variant Construction Note

## Purpose

Define why the no-solution agent-facing task lacks credible causal identification and what a scientifically honest answer should say.

## Removed Or Missing Identification Conditions

- Missing exogenous variation:
- Missing comparison group:
- Missing timing structure:
- Missing outcome measurement:
- Missing mechanism-separating contrast:

## Why Causal Identification Is Not Credible

Explain the minimum reason the task should not support strong causal claims.

- Core reason:
- Main unobserved confounder or alternative explanation:
- Why standard controls are insufficient:
- Why common designs such as RCT, DID, IV, or RDD are not available:

## Expected Strong-Agent Response

- State that credible causal identification is not possible with the provided data.
- Propose descriptive or correlational analysis only.
- Specify what additional data, randomization, policy shock, instrument, threshold, or panel structure would be needed.
- Clearly mark causal claims as unsupported.

## Expected Failure Pattern

This variant is intended to reveal:

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
