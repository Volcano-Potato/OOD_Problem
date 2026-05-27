<!-- visibility: agent-facing -->
<!-- case_id: C004 -->
<!-- variant: no_solution -->

# Anonymous Research Design Task: No-Solution Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A consumer-facing firm wants to know whether paid placements in query-driven digital traffic cause additional purchases. The firm has rich records on ad spend, clicks, attributed conversions, market-level sales, and prior user activity, so the dataset looks highly informative.

The business question is important, but rich digital-marketing data do not by themselves solve the causal problem if campaign intensity follows expected demand and observed clicks mainly reflect user intent.

## Research Setting

The firm runs paid-search campaigns continuously across markets. Campaign managers and delivery systems decide how aggressively to bid, where to show the ads, and which traffic classes to emphasize based on performance signals and business priorities. The researcher observes market-time sales outcomes, marketing logs, and historical user activity summaries, but there is no experimental holdout or externally imposed policy variation in the available data.

## Research Objective

Assess whether greater paid-search activity is associated with higher downstream purchases and whether those differences can be interpreted as causal ad lift.

## Specific Questions To Answer

1. Are markets with more paid-search activity associated with higher downstream sales?
2. Can rich historical controls and segment information make that relationship causal?
3. What can the data still support descriptively or predictively?
4. What additional design or data would be needed to estimate incremental paid-search effects credibly?

## Data Structure Overview

- Stage 1: The researcher observes historical market-level sales and prior user-activity summaries.
- Stage 2: During the campaign, paid-search spend, clicks, and traffic volumes vary across markets and over time according to business and platform decisions.
- Stage 3: The researcher records downstream sales, orders, and attributed conversions for each market over time.
- Stage 4: Outcomes can also be summarized for user-history segments defined by prior familiarity, recency, or frequency of activity.

## Available Data

| field | description |
|---|---|
| unit of observation | Market-by-time sales observation, campaign log, or segment-level summary linked to downstream outcomes. |
| time span | Historical pre-period plus campaign-period repeated observations. |
| sample construction | Markets observed continuously under a live campaign with no experimental holdout in the available data. |
| treatment or exposure variable | Paid-search spend, clicks, attributed conversions, impression volume, or campaign intensity measures. |
| outcome variable | Downstream purchases, orders, sales, or revenue. |
| secondary outcomes | Attributed conversions, visits, user-segment sales, and other marketing-performance summaries. |
| covariates | Historical sales, seasonality controls, market size, prior activity summaries, and campaign-management indicators if available. |
| panel or repeated structure | Yes; repeated market-by-time observations. |
| assignment or variation source | Campaign intensity is determined by managers, delivery rules, and expected demand rather than experimental assignment. |
| assignment level | Market, market-time, or campaign-management cell. |
| outcome measurement level | Market-by-time or market-by-time-by-segment sales outcome. |
| missingness or attrition | Aggregate sales are generally observed, but attribution and segment classification may be incomplete. |
| possible spillover or interference | Users may substitute across unpaid search, direct navigation, other channels, and neighboring markets. |

## Variable Groups

### Treatment Or Exposure Variables

- Paid-search spend or campaign intensity.
- Click volume or attributed conversions.
- Impression or traffic acquisition summaries.

### Selection Or Sample-Flow Variables

- Market participation in the campaign.
- User-history segment assignment based on pre-period familiarity or activity.
- Inclusion in attribution or conversion measurement systems.

### Main Outcome Variables

- Downstream purchases or sales.
- Revenue or order counts.

### Secondary Outcome Variables

- Attributed conversions.
- Visits or engagement summaries.
- Segment-specific sales outcomes.

### Baseline Controls And Design Variables

- Historical market-level sales.
- Market fixed characteristics, seasonality controls, and time indicators.
- Prior familiarity, recency, or frequency segment summaries.

## Identification Limitations

- No randomized assignment or quasi-random variation is provided.
- No credible instrument, threshold, boundary, or externally imposed timing shock is provided.
- Treated and untreated markets may differ in unobserved demand conditions related to both campaign intensity and outcomes.
- Observed clicks, spend, and attributed conversions do not separate incremental demand creation from existing intent or channel substitution.

## Known Constraints

- The task should still look empirically tempting: many covariates, clear outcomes, and real business or policy relevance.
- The answer must explicitly distinguish what is causally identifiable from what is only descriptive or correlational.
- If causal identification is not credible, the answer must say so plainly rather than inventing a design.

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
