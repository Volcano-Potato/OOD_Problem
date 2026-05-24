<!-- visibility: agent-facing -->
<!-- case_id: C005 -->
<!-- variant: level2 -->

# Anonymous Research Design Task: Level 2

## Task Rule

You must not search the web, infer the original paper, or use external literature. Use only the information provided below. Your goal is to design a rigorous empirical strategy, not to write a literature review.

Do not assume that a known paper has already solved the task. Treat this as an anonymous applied business/economics research problem.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A firm wants to measure whether a digital advertising campaign actually changes user behavior. The central problem is that observed ad exposure is not purely random because platform delivery systems use auctions, targeting rules, pacing, and optimization.

The research problem is to design a measurement strategy that identifies a credible counterfactual for users who were realistically in a position to see the campaign.

## Research Setting

An advertiser runs a campaign on an online platform, and the researcher can observe some combination of campaign assignment, delivery logs, and downstream user outcomes. The platform controls which users actually receive impressions, even when some higher-level experimentation is possible.

## Research Objective

Design a study to estimate the causal effect of actual digital ad exposure on downstream user outcomes in a setting where platform delivery may be optimized and selected.

## Specific Questions To Answer

1. How should the researcher define the causal estimand when campaign assignment and actual ad exposure are not the same thing?
2. What comparison group would make exposed users comparable to an untreated counterfactual?
3. How should the design distinguish a campaign-level assignment effect from the effect of actual exposure?
4. Which claims about ad lift remain credible if exposure opportunity is measured imperfectly?

## Causal Mechanisms To Distinguish

- Users who receive impressions may already have higher baseline demand or purchase intent.
- Platform-delivery rules may sort different user types into exposure even under an experiment.
- Campaign assignment can affect eligibility or opportunity without guaranteeing actual exposure.
- Measured conversions may depend on tracking systems as well as on real behavior.

## Data Structure Overview

- Stage 1: Users become eligible for the campaign during a live delivery window with platform-level auctions or allocation rules.
- Stage 2: Some higher-level randomization or holdout assignment can affect whether users are eligible to receive the campaign.
- Stage 3: Conditional on eligibility, the platform determines whether the focal ad is actually served at each opportunity.
- Stage 4: The researcher observes downstream conversions such as visits, registrations, or purchases within a defined outcome window.

## Data Card

| field | description |
|---|---|
| unit of observation | User-ad opportunity or user-impression record linked to downstream user outcomes. Aggregation to user level is possible only if exposure opportunities are summarized consistently. |
| time span | Short campaign window plus a post-exposure outcome window; exact dates and duration are withheld. |
| geographic or market scope | Online platform campaign for a single advertiser or product category; platform and advertiser names are withheld. |
| sample construction | Eligible users enter platform auctions or delivery opportunities during the campaign. Logs may include campaign assignment, realized impressions, non-delivery, and downstream outcomes. |
| treatment or exposure variable | Actual exposure to the focal ad, campaign eligibility or assignment, and indicators describing whether a user had a comparable opportunity for the focal ad to be delivered. |
| outcome variable | Downstream conversion outcomes such as website visit, registration, lead, purchase, or revenue within a defined attribution window. |
| secondary outcomes | Intermediate engagement outcomes, repeated exposure counts, or any auxiliary delivery outcomes if observed. |
| covariates | Pre-campaign user activity, device or channel, broad geography or market segment, campaign eligibility rules, time of opportunity, and platform relevance scores if available. |
| baseline or pre-treatment variables | User or segment characteristics known before the campaign and any prior activity used by the platform or advertiser. |
| panel or repeated structure | Users can have multiple ad opportunities and multiple impressions over time. Opportunity-level records should be linked to user-level outcomes. |
| assignment or variation source | Campaign-level randomization or holdout assignment exists, but realized exposure is also shaped by auctions, targeting, pacing, and optimization. |
| assignment level | User or ad-opportunity level, depending on the platform implementation. The answer must state which level it assumes. |
| outcome measurement level | User-level downstream conversion, optionally linked back to opportunity or impression records. |
| recommended clustering or inference level | User level when multiple opportunities exist; campaign cell, time cell, or market level if randomization is grouped. |
| repeated exposure | Likely; users may receive zero, one, or multiple focal-ad impressions. |
| compliance or take-up | Assignment or eligibility does not guarantee actual exposure because the focal ad may not be served. |
| missingness or attrition | Outcomes may be missing because of tracking loss, cross-device behavior, identifier churn, or incomplete conversion matching. |
| possible spillover or interference | Users may see ads on other channels, share information, or be affected by market-level campaign saturation. |

## Variable Groups

### Treatment Or Exposure Variables

- Campaign assignment or eligibility.
- Actual focal-ad exposure.
- Exposure-opportunity indicators or equivalent opportunity-side signals.

### Selection Or Sample-Flow Variables

- User eligibility for campaign delivery.
- Realized impression or non-delivery.
- Inclusion in outcome tracking.

### Main Outcome Variables

- Downstream conversions.
- Revenue or purchase indicators if observed.

### Secondary Outcome Variables

- Intermediate engagement events.
- Exposure frequency.
- Delivery or auction outcomes if observed.

### Baseline Controls And Design Variables

- Pre-campaign user activity.
- Device, channel, broad market segment, and time-of-opportunity indicators.

## Known Constraints

- The design should match the data structure above.
- The answer must distinguish descriptive associations, causal claims, and mechanism claims.
- The answer should state what cannot be learned from the available information.
- Do not label the final identification strategy by name unless you justify why the data support it.
- Do not rely on external facts about the original paper, platform, or advertiser.

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
