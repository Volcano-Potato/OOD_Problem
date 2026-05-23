<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C008 -->

# Case Audit: C008

## Gold Reference Audit

- audit_date: 2026-05-23
- audit_scope: `gold_reference.md` checked against `source_facts.md` and `source_packet.md`
- reviewer: Codex separate audit pass
- independent_model_session: not used in this pass
- audit_decision: approve

## Evidence Support Check

| gold section | audit finding | status |
|---|---|---|
| Core Research Problem | Research question, estimand, treatment, outcome, and unit are supported by F002-F016. | pass |
| Data Structure | Product/store/time structure and comparison requirements are supported by F005-F013 and U001-U002. | pass |
| Original Identification Logic | DID and DDD logic are supported by F017-F020. | pass |
| Linchpin Detail | Product-category plus store/time controls are supported by L001-L003. | pass |
| Must-Have Conditions | Conditions require valid comparison structure without demanding exact original categories/specification. | pass |
| Acceptable Alternative Designs | Alternatives specify assumptions and claim limits. | pass |
| Common Invalid Designs | Invalid designs cover before-after, weak controls, price confounding, and unsupported mechanism claims. | pass |

## Issue Table

| issue_id | section | severity | problem | required_fix | status |
|---|---|---|---|---|---|
| C008-AUD-001 | Scoring Notes | medium | Gold reference allows DID as partial credit and DDD as full credit, but exact threshold needs rubric calibration. | In Task 20 rubric, distinguish minimal valid DID from stronger DDD with control-store validation. | accepted limitation |
| C008-AUD-002 | Data Structure | low | Exact regression formula, weights, and standard errors remain unextracted. | Do not require exact formula in agent task scoring. | accepted limitation |
| C008-AUD-003 | Leakage | low | Exact product categories and original tax context can be recognizable. | Generalize product categories and add-on charge framing in agent-facing tasks. | accepted limitation |

## High Severity Issues

- None.

## Linchpin Audit

- Decision: valid linchpin.
- Reason: The design needs product-category and store/time comparisons to avoid confounding salience with category shocks or time shocks.
- Evidence: L001-L003, F017-F020, N001-N003.

## Over-Narrowness Audit

- Decision: not over-narrow.
- Reason: The gold reference accepts DID, DDD, and randomized rollout designs. It does not require the exact original product categories, tax rate, dates, or regression specification.

## Acceptable Alternatives Audit

- DID is acceptable under credible parallel trends and no spillover.
- DDD is stronger because it uses stores and categories.
- Randomized rollout is acceptable if it isolates visibility from actual price changes.

## Common Invalid Designs Audit

- The invalid designs cover before-after comparisons, category-only controls, price/promotion confounding, cross-sectional comparisons, and unsupported attention claims.
- Error labels are actionable for later annotation.

## Required Revisions Before Task Packet Generation

- None.

## Follow-Up For Task 09-13

- Preserve treated products, control products, treatment store/market, control stores/markets, and pre/post timing.
- Do not leak exact product categories, exact tax rate, exhibit, title, or authors.
