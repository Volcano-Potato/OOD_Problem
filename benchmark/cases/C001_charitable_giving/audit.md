<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C001 -->

# Case Audit: C001

## Gold Reference Audit

- audit_date: 2026-05-23
- audit_scope: `gold_reference.md` checked against `source_facts.md` and `source_packet.md`
- reviewer: Codex separate audit pass
- independent_model_session: not used in this pass
- audit_decision: approve

## Evidence Support Check

| gold section | audit finding | status |
|---|---|---|
| Core Research Problem | Research question, treatment, outcome, unit, and target mechanism are supported by F002-F016. | pass |
| Data Structure | Observation unit, assignment level, outcome level, timing, and uncertainty notes are supported by F005-F008 and U001. | pass |
| Original Identification Logic | The mechanism-experiment logic is supported by F017-F020. | pass |
| Linchpin Detail | Low-cost avoidance/opt-out is supported by L001-L002 and N001-N003. | pass |
| Must-Have Conditions | Conditions generalize the source design into necessary mechanism-identification requirements rather than exact paper replication. | pass |
| Acceptable Alternative Designs | Alternatives specify what they can and cannot claim; none require exact original method. | pass |
| Common Invalid Designs | Invalid designs match naive failure modes N001-N003 and likely agent errors. | pass |

## Issue Table

| issue_id | section | severity | problem | required_fix | status |
|---|---|---|---|---|---|
| C001-AUD-001 | Data Structure | low | Exact randomization unit and inference details are not yet extracted. | Do not require exact clustering or standard-error formulas in task generation or scoring until later verification. | accepted limitation |
| C001-AUD-002 | Must-Have Conditions | low | The opt-out condition could become too source-specific if copied literally into agent-facing tasks. | Phrase as a generic low-cost private avoidance channel during Task 09-13. | accepted limitation |
| C001-AUD-003 | Acceptable Alternative Designs | low | Alternative appointment/decline design may introduce public refusal pressure if not private. | Keep privacy/low-cost condition in the alternative design. | resolved in gold |

## High Severity Issues

- None.

## Linchpin Audit

- Decision: valid linchpin.
- Reason: Without an avoidance/sorting channel, the design can estimate solicitation effects but cannot separate altruism/warm glow from social pressure.
- Evidence: L001-L002, F019-F020, N001-N003.

## Over-Narrowness Audit

- Decision: not over-narrow.
- Reason: The gold reference does not require exact flyers, exact charities, exact wording, exact dates, or exact original implementation. It requires the more general identification condition: a pre-contact low-cost avoidance or sorting channel plus separate contact and donation outcomes.

## Acceptable Alternatives Audit

- The listed alternatives are reasonable because they preserve the needed mechanism contrast.
- Each alternative states what claim it supports and what claim it cannot support.
- No alternative is accepted without separate contact/avoidance and giving outcomes.

## Common Invalid Designs Audit

- The invalid designs cover donation-only designs, simple RCT overclaiming, mechanism confounding, and observational selection.
- Error labels are usable for later annotation.

## Required Revisions Before Task Packet Generation

- None.

## Follow-Up For Task 09-13

- Do not include original title, authors, exact city, named charities, exact sample size, or source-specific opt-out phrase in agent-facing tasks.
- Preserve generic mechanism requirements: advance information, avoidance/sorting option, contact outcome, donation outcome.
