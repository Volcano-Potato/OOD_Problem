<!-- visibility: agent-facing -->
<!-- case_id: C004 -->
<!-- variant: level3 -->

# Anonymous Research Design Task: Level 3

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A consumer-facing firm wants to measure whether paid placements in query-driven digital traffic create incremental purchases or mainly capture users who were already likely to reach the firm through other channels. Observational campaign metrics can greatly overstate value when paid clicks reflect user intent rather than causal persuasion.

Managers also care about whether search advertising is broadly ineffective or whether average near-zero effects hide gains for less active or less familiar users.

## Research Setting

The firm runs a campaign across multiple market areas. The campaign can be active in some markets and inactive in other comparable markets during the same period, while downstream sales are recorded continuously. Users differ in prior familiarity and activity, and they may reach the firm through paid search, unpaid search, direct navigation, or other channels.

## Research Objective

Design a study to estimate the causal effect of paid search availability on downstream purchases and to assess whether effects differ across user-history segments.

## Specific Questions To Answer

1. What causal effect can be learned from market-level paid-search availability?
2. How should the researcher distinguish incremental demand creation from channel substitution or interception of existing intent?
3. How should heterogeneous treatment effects across less active versus already active users be studied?
4. Which claims are credible about mechanism, average effect size, and segment-specific impact?

## Causal Mechanisms To Distinguish

- Informational or discovery effect for users with low prior familiarity or long absence.
- Route-substitution effect for already informed users who would have arrived through other channels anyway.
- Intent-selection problem in clicked and attributed traffic.
- Composition effect where aggregate averages hide segment-level differences.

## Data Structure Overview

- Stage 1: The researcher observes pre-period sales histories and baseline market characteristics for multiple comparable market areas.
- Stage 2: During a campaign window, paid search availability differs across some markets while remaining active in comparable markets.
- Stage 3: The researcher records downstream sales or purchase outcomes over time for treated and untreated markets.
- Stage 4: Outcomes can also be summarized for user-history segments defined by prior familiarity, recency, or frequency of activity.

## Data Card

| field | description |
|---|---|
| unit of observation | Market-by-time sales observation, optionally split by prior user-history segment. |
| time span | Pre-period and intervention-period repeated observations; exact dates are withheld. |
| geographic or market scope | Multiple comparable market areas under a common campaign and common sales-recording system. |
| sample construction | Markets are observed continuously for downstream sales, and a focal paid-search traffic class is active in some markets and unavailable in others during the intervention period. |
| treatment or exposure variable | Indicator for paid-search availability in a market during the intervention window. |
| outcome variable | Downstream purchases, orders, sales, or revenue recorded after search-driven user acquisition. |
| secondary outcomes | Segment-specific purchases, customer acquisition outcomes, or related downstream sales summaries if observed. |
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

### Treatment Or Exposure Variables

- Market-level paid-search availability during the intervention window.
- Intensity or duration of paid-search availability if observed.

### Selection Or Sample-Flow Variables

- Market membership of demand observations.
- User-history segment assignment based on pre-period familiarity or activity.
- Indicators for whether observed purchases come from users plausibly affected during the campaign window.

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

## Institutional Details Relevant For Identification

Paid-search availability is controlled by the firm or the platform's campaign controls at the market level rather than by individual users. Users discover the firm after initiating search-like behavior and can still choose whether to click, browse, or purchase. This means individual clicks remain behavior-driven even if market-level ad availability varies exogenously.

The packet supports repeated pre-period market outcomes, so baseline trends and comparability can be checked. Outcomes are measured using downstream administrative sales rather than clicks alone. However, users can substitute to unpaid channels or direct navigation, and cross-market or cross-channel spillovers are not ruled out automatically.

## Potential Threats

- Potential selection or endogenous exposure issue: clicked traffic and attributed conversions may overstate causal value because search intent is not randomly assigned at the individual level.
- Potential timing, anticipation, or trend issue: treated and untreated markets may differ in demand trends or seasonality during the campaign window.
- Potential mechanism-confounding issue: an observed effect could reflect channel substitution rather than new demand creation.
- Potential measurement issue: aggregate sales may hide whether effects differ across more active and less active users.
- Potential spillover or interference issue: users may reach the firm through unpaid search, direct traffic, or neighboring markets.
- Potential compliance, take-up, attrition, or missingness issue: market-level ad availability does not guarantee comparable individual exposure intensity, and segment classification may be incomplete.
- Potential inference or clustering issue: treatment variation occurs at the market level, so user-level inference would overstate precision.

## Required Threat-Response Table

In addition to the standard output, include this table. If a threat cannot be addressed with the available data, say so.

| Threat | Why It Matters | Proposed Diagnostic Or Design Response | Remaining Limitation |
|---|---|---|---|

## Known Constraints

- The design should match the data, institutional details, and threats above.
- The answer must distinguish descriptive associations, randomized or quasi-random causal claims, and mechanism claims.
- The answer should state what cannot be learned from the available information.
- Do not turn the threat list into a generic robustness checklist. Connect each threat to the proposed design.
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
