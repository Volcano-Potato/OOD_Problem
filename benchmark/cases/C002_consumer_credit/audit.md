<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C002 -->

# Case Audit: C002

## Gold Reference Audit

- audit_date: 2026-05-23
- audit_scope: `gold_reference.md` checked against `source_facts.md` and `source_packet.md`
- reviewer: Codex separate audit pass
- independent_model_session: not used in this pass
- audit_decision: approve

## Evidence Support Check

| gold section | audit finding | status |
|---|---|---|
| Core Research Problem | Research question, mechanism target, treatments, outcomes, and unit are supported by F002-F015. | pass |
| Data Structure | Time sequence and information structure are supported by F005-F008, F013, F016, U001-U002. | pass |
| Original Identification Logic | Selection and moral-hazard logic are supported by F017-F020. | pass |
| Linchpin Detail | Offer/contract separation, dynamic incentive, and borrower blindness are supported by L001-L003. | pass |
| Must-Have Conditions | Conditions require mechanism separation, not exact source replication. | pass |
| Acceptable Alternative Designs | Alternatives are broader than the original design and specify claim boundaries. | pass |
| Common Invalid Designs | Invalid designs map to N001-N003 and common weak-agent claims. | pass |

## Issue Table

| issue_id | section | severity | problem | required_fix | status |
|---|---|---|---|---|---|
| C002-AUD-001 | Data Structure | medium | Exact dynamic-incentive randomization level and standard-error level remain unextracted. | Gold scoring should not require exact clustering or wave details until a later verification pass. | accepted limitation |
| C002-AUD-002 | Must-Have Conditions | low | "At least two randomized margins" is a general condition but full mechanism separation may require three margins. | Keep partial-credit distinction: two margins can identify selection but not full moral hazard. | resolved in gold |
| C002-AUD-003 | Leakage | low | The offer-rate/contract-rate/dynamic-incentive sequence is distinctive. | In agent-facing tasks, describe stages generically without source title, country, or lender details. | accepted limitation |

## High Severity Issues

- None.

## Linchpin Audit

- Decision: valid linchpins.
- Reason: A single randomized loan price confounds adverse selection and moral hazard; staged timing and borrower information are necessary for mechanism separation.
- Evidence: L001-L003, F018-F020, N001-N003.

## Over-Narrowness Audit

- Decision: not over-narrow.
- Reason: The gold reference allows two-stage, factorial, and encouragement-style alternatives. It does not demand the exact original lender, country, sample, terminology, or contract labels.

## Acceptable Alternatives Audit

- The alternatives correctly specify which mechanism each design can identify.
- The two-stage design is properly limited because it may not identify pure moral hazard without a post-borrowing incentive.
- The future-incentive design is properly limited because it cannot estimate adverse selection without take-up variation.

## Common Invalid Designs Audit

- The invalid designs cover single-rate randomization, unequal final terms, contaminated future incentives, unsupported adverse-selection claims, and borrower-information failures.
- Error labels are actionable for later annotation.

## Required Revisions Before Task Packet Generation

- None.

## Follow-Up For Task 09-13

- Preserve the timing sequence: offer, application/take-up, final contract term revelation, repayment/future incentive.
- Avoid exact country, lender identity, and source-specific terminology in agent-facing tasks.
