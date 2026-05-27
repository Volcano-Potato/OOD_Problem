<!-- visibility: agent-facing -->
<!-- case_id: C004 -->
<!-- variant: level2 -->

# Anonymous Research Design Task: Level 2

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A consumer-facing firm wants to measure whether paid placements in query-driven digital traffic create incremental purchases or mainly capture users who were already likely to reach the firm through other channels. The central empirical challenge is that paid-search spending, clicks, and attributed conversions are closely tied to underlying user intent.

The practical goal is to decide whether campaign spending is genuinely productive and whether any gains are concentrated among less familiar or less active users rather than among already active users.

## Research Setting

The firm runs search-style paid acquisition campaigns across multiple market areas. During part of the campaign, ad availability can differ across comparable markets while downstream sales are recorded continuously. Users in those markets vary in prior familiarity and activity, and some users would have reached the firm even without the paid placement.

## Research Objective

Design a study to estimate the causal effect of paid search availability on downstream purchases and to assess whether the effect differs across user-history segments.

## Specific Questions To Answer

1. What is the relevant causal estimand: ad availability, campaign exposure, or downstream incremental sales?
2. How should the researcher compare treated and untreated markets so that underlying demand trends are not mistaken for ad effects?
3. How should the design separate true demand creation from channel substitution or interception of existing intent?
4. What can be learned about heterogeneity across less active versus already active users?

## Causal Mechanisms To Distinguish

- Paid placements may inform or attract less familiar users who otherwise would not have purchased.
- Already informed users may use the paid link as a substitute route rather than because the ad changed behavior.
- Observed click and attribution outcomes may mechanically overstate causal value because they reflect search intent.
- Average campaign effects may mask meaningful heterogeneity across prior-activity segments.

## Data Structure Overview

- Stage 1: The researcher observes pre-period sales histories and baseline market characteristics for multiple comparable market areas.
- Stage 2: During a campaign window, paid search availability differs across some markets while remaining active in comparable markets.
- Stage 3: The researcher records downstream sales or purchase outcomes over time for treated and untreated markets.
- Stage 4: Outcomes can also be summarized for user-history segments defined by prior familiarity, recency, or frequency of activity.

## Data Card

| field | description |
|---|---|
| unit of observation | Market-by-time sales observation, optionally split by prior user-history segment. |
| time span | Pre-period and intervention-period repeated observations; exact dates and campaign length are withheld. |
| geographic or market scope | Multiple comparable market areas under a common campaign and common sales-recording system. |
| sample construction | Market areas are observed continuously for downstream sales, and a focal paid-search traffic class is active in some markets and unavailable in others during the intervention period. |
| treatment or exposure variable | Indicator for paid-search availability in a market during the intervention window. |
| outcome variable | Downstream purchases, orders, sales, or revenue recorded after search-driven user acquisition. |
| secondary outcomes | Segment-specific purchases, customer acquisition outcomes, or other downstream sales summaries if observed. |
| covariates | Baseline market size, historical sales levels, seasonality controls, and segment composition measures. |
| baseline or pre-treatment variables | Pre-period sales histories and prior user-activity or familiarity summaries. |
| panel or repeated structure | Yes; repeated market-by-time observations before and during the campaign. |
| assignment or variation source | Planned market-level variation in whether paid search is available for the focal traffic class. |
| assignment level | Market or market-time cell. |
| outcome measurement level | Market-by-time or market-by-time-by-segment sales outcome. |
| recommended clustering or inference level | Market level or matched-market-pair level if markets are paired. |
| repeated exposure | Yes; users in treated markets can face repeated search opportunities during the campaign. |
| compliance or take-up | Market-level ad availability does not map one-to-one into individual exposure, clicks, or purchases. |
| missingness or attrition | Aggregate sales are typically well measured, but segment classification and cross-channel tracking may be incomplete. |
| possible spillover or interference | Users may substitute across unpaid search, direct navigation, neighboring markets, or other acquisition channels. |

## Variable Groups

Define the variable groups needed for the research design. Use generic names rather than source-specific labels.

### Treatment Or Exposure Variables

- Market-level paid-search availability during the intervention window.
- Intensity or duration of paid-search availability if observed.

### Selection Or Sample-Flow Variables

- Market membership of demand observations.
- User-history segment assignment based on pre-period familiarity or activity.
- Indicators for whether observed purchases come from users plausibly exposed during the campaign window.

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

## Known Constraints

- The design should match the data structure above.
- The answer must distinguish descriptive associations, randomized or quasi-random causal claims, and mechanism claims.
- The answer should state what cannot be learned from the available information.
- Do not label the final identification strategy by name unless you have justified why the data support it.
- Do not rely on unsupported source-specific facts about the original paper, place, firm, platform, or policy.

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
