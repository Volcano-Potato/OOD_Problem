<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C005 -->

# Case Audit: C005

## Gold Reference Audit

- audit_date: 2026-05-23
- audit_scope: `gold_reference.md` checked against `source_facts.md` and `source_packet.md`
- reviewer: Codex separate audit pass
- independent_model_session: not used in this pass
- audit_decision: approve

## Evidence Support Check

| gold section | audit finding | status |
|---|---|---|
| Core Research Problem | Research question, estimand, exposure, outcome, and unit are supported by F002-F015. | pass |
| Data Structure | Assignment, platform structure, outcome level, exposure opportunity, and uncertainty notes are supported by F005-F012 and U001-U002. | pass |
| Original Identification Logic | Exposure-opportunity comparison is supported by F017-F020. | pass |
| Linchpin Detail | Comparable exposure opportunity, platform optimization, and prediction validation are supported by L001-L003. | pass |
| Must-Have Conditions | Conditions require correction for endogenous exposure without requiring the named source method. | pass |
| Acceptable Alternative Designs | Alternatives specify extra data/assumptions and claim limits. | pass |
| Common Invalid Designs | Invalid designs map to N001-N003 and likely ad-measurement agent failures. | pass |

## Issue Table

| issue_id | section | severity | problem | required_fix | status |
|---|---|---|---|---|---|
| C005-AUD-001 | Scoring Notes | medium | ITT treatment is a possible partial-credit design, but the exact partial-credit boundary is judgment-sensitive. | Keep explicit distinction between assignment/eligibility effect and exposed-user lift during rubric construction. | resolved in gold |
| C005-AUD-002 | Acceptable Alternative Designs | low | Geo/time campaign shutdown is plausible but not directly extracted from the source facts. | Treat it as evaluator-approved alternative requiring extra comparability, spillover, and seasonality assumptions. | accepted limitation |
| C005-AUD-003 | Leakage | low | The source method name is highly identifying. | Do not use the named method in agent-facing task packets. | accepted limitation |

## High Severity Issues

- None.

## Linchpin Audit

- Decision: valid linchpin.
- Reason: Actual exposure is selected by platform optimization and user intent. The answer must construct a counterfactual group based on comparable exposure opportunity.
- Evidence: L001-L003, F017-F020, N001-N003.

## Over-Narrowness Audit

- Decision: not over-narrow.
- Reason: The gold reference does not require the named source method. It accepts any design that solves the same exposure-opportunity counterfactual problem and states limits.

## Acceptable Alternatives Audit

- Logged exposure-opportunity holdout is directly aligned with the source facts.
- Auction replay/simulation is acceptable only with validation.
- Geo/time shutdown is acceptable only for campaign-level lift and is explicitly limited.

## Common Invalid Designs Audit

- The invalid designs cover exposed-vs-unexposed comparisons, naive PSA controls, ITT overclaiming, click regressions, and prediction-error neglect.
- Error labels are usable for later annotation.

## Required Revisions Before Task Packet Generation

- None.

## Follow-Up For Task 09-13

- Use generic terms like "would-have-been ad opportunity" rather than source-specific method names.
- Make clear that random assignment and realized exposure are different variables.
