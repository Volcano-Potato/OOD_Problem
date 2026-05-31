<!-- visibility: agent-facing -->
<!-- case_id: C004 -->
<!-- variant: perturbed -->

# Anonymous Research Design Task: Perturbed Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A consumer-facing firm wants to know whether paid placements in query-driven digital traffic generate incremental purchases or mainly intercept users who would have reached the firm anyway. Managers still care about whether effects differ across less active and already active users.

## Research Setting

The firm records repeated downstream sales outcomes across multiple market areas during a campaign. Campaign managers can choose to reduce or suspend paid-search availability in some markets while keeping it active elsewhere. Users differ in prior familiarity and can still reach the firm through unpaid or direct channels.

## Research Objective

Assess whether changes in paid-search availability affect downstream purchases and whether any measured effect can be interpreted causally.

## Specific Questions To Answer

1. Can the researcher still estimate a credible causal effect of paid-search availability on downstream sales?
2. How should the researcher separate genuine ad effects from underlying market demand differences?
3. What happens to the interpretation of user-segment heterogeneity if treatment assignment is no longer clearly exogenous?
4. Which claims, if any, remain defensible under the available variation?

## Data Structure Overview

- Stage 1: The researcher observes historical sales patterns and baseline market characteristics for multiple market areas.
- Stage 2: During the campaign, some markets have paid-search availability reduced or suspended while others remain active.
- Stage 3: The researcher records downstream sales or purchase outcomes over time for all markets.
- Stage 4: Outcomes can also be summarized for user-history segments defined by prior familiarity, recency, or frequency of activity.

## Data Card

| field | description |
|---|---|
| unit of observation | Market-by-time sales observation, optionally split by prior user-history segment. |
| time span | Pre-period and intervention-period repeated observations. |
| sample construction | Markets are observed continuously for downstream sales, and campaign managers can change paid-search availability during the intervention period. |
| treatment or exposure variable | Indicator for paid-search availability in a market during the intervention window. |
| outcome variable | Downstream purchases, orders, sales, or revenue. |
| secondary outcomes | Segment-specific purchases or related downstream sales summaries if observed. |
| assignment or variation source | Campaign managers choose where to reduce or suspend paid-search availability based on operational or demand considerations rather than using a pre-committed experimental rule. |
| assignment level | Market or market-time cell. |
| outcome measurement level | Market-by-time or market-by-time-by-segment sales outcome. |
| panel or repeated structure | Yes; repeated market-by-time observations before and during the campaign. |
| compliance or take-up | Market-level ad availability does not map one-to-one into individual exposure, clicks, or purchases. |
| spillover or interference | Users may substitute across unpaid search, direct navigation, neighboring markets, or other acquisition channels. |

## Variable Groups

### Treatment Or Exposure Variables

- Market-level paid-search availability during the intervention window.
- Intensity or duration of paid-search availability if observed.

### Selection Or Sample-Flow Variables

- Market membership of demand observations.
- User-history segment assignment based on pre-period familiarity or activity.

### Main Outcome Variables

- Downstream purchases or sales.
- Revenue or order counts.

### Secondary Outcome Variables

- Segment-specific sales outcomes.
- New-to-firm or less-active-user purchase outcomes if available.

### Baseline Controls And Design Variables

- Historical market-level sales.
- Market fixed characteristics, seasonality controls, and time indicators.
- Prior familiarity, recency, or frequency segment summaries.

## Perturbed Condition

Paid-search availability is no longer varied according to a clearly exogenous or pre-committed experimental rule. Instead, campaign managers choose which markets to reduce or suspend based on operational judgments, expected demand, or budget considerations.

## Known Constraints

- The business setting and most of the data structure are intentionally similar to the base task.
- One key identification condition has changed.
- The answer must explain whether the original design logic still works, becomes weaker, or fails.
- If strong causal identification is no longer justified, the answer must explicitly downgrade the claim or propose additional design changes.

## Required Output

1. Executive summary
2. Research question
3. Target estimand or strongest defensible estimand
4. Treatment or exposure and main outcomes
5. Data structure summary
6. Relevant causal mechanisms
7. Main identification challenge
8. Whether credible causal identification is possible
9. Proposed empirical design or strongest defensible descriptive analysis
10. Why the design is valid or why causal identification is not credible
11. Required assumptions
12. Statistical model or analysis equation
13. Robustness, placebo, falsification checks, or diagnostic tests
14. Heterogeneity analysis if supportable
15. Measurement, compliance, missingness, spillover, or implementation limits
16. Failure modes and alternative explanations
17. What cannot be claimed
18. Additional data needed
19. Threat-response table if explicitly requested by the task packet
20. Claim-evidence table

## Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
