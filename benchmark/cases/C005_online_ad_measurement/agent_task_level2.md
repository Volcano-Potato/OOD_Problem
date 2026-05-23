<!-- visibility: agent-facing -->
<!-- case_id: C005 -->
<!-- variant: level2 -->

# Anonymous Research Design Task: Level 2

## Task Rule

You must not search the web, infer the original paper, or use external literature. Use only the information provided below. Your goal is to design a rigorous empirical strategy, not to write a literature review.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A firm wants to measure whether a digital advertising campaign causes users to visit, sign up, or purchase. The central difficulty is that actual ad exposure is not simply random. Online platforms often decide which users receive impressions through auctions, targeting rules, and optimization systems.

A useful design must define the relevant counterfactual for users who receive the campaign while accounting for platform delivery and selection.

## Research Objective

Design a study to estimate the causal effect of actual digital ad exposure on downstream user outcomes in a setting where platform delivery may be optimized and selected.

## Data Card

| field | description |
|---|---|
| unit of observation | User-ad opportunity or user-impression record linked to downstream user outcomes. Aggregation to user level is possible only if exposure opportunities are summarized consistently. |
| time span | Short campaign window plus a post-exposure outcome window; exact dates and duration are withheld. |
| geographic or market scope | Online platform campaign for a single advertiser or product category; platform and advertiser names are withheld. |
| sample construction | Eligible users enter platform auctions or delivery opportunities during the campaign. Logs may include campaign assignment, realized impressions, non-delivery, and downstream outcomes. |
| treatment or exposure variable | Actual exposure to the focal ad, campaign eligibility or assignment, and indicators describing whether a user had a comparable opportunity for the focal ad to be delivered. |
| outcome variable | Downstream conversion outcomes such as website visit, registration, lead, purchase, or revenue within a defined attribution window. |
| covariates | Pre-campaign user activity, device or channel, broad geography or market segment, campaign eligibility rules, time of opportunity, platform-predicted relevance if available. |
| panel or repeated structure | Users can have multiple ad opportunities and multiple impressions over time. Opportunity-level records should be linked to user-level outcomes. |
| assignment or variation source | Campaign-level randomization or holdout assignment exists, but realized exposure is also shaped by auctions, targeting, pacing, and optimization. |
| assignment level | User or ad-opportunity level, depending on the platform implementation. The answer must state which level it assumes. |
| outcome measurement level | User-level downstream conversion, optionally linked back to opportunity or impression records. |
| recommended clustering or inference level | User level when multiple opportunities exist; campaign cell, time cell, or market level if randomization is grouped. |
| repeated exposure | Likely; users may receive zero, one, or multiple focal-ad impressions. |
| compliance or take-up | Assignment or eligibility does not guarantee actual exposure because the ad may not be served. |
| missingness or attrition | Outcomes may be missing because of tracking loss, cross-device behavior, cookie or identifier churn, or incomplete conversion matching. |
| possible spillover or interference | Users may see ads on other channels, share information, or be affected by market-level campaign saturation. |

## Known Constraints

- The design should match the data structure above.
- The answer must distinguish causal claims from descriptive claims.
- The answer should state what cannot be learned from the available information.
- Do not assume that observed exposure is as-if random.
- Do not rely on external facts about any named platform, advertiser, campaign, or previous study.

## Required Output

1. Research question
2. Estimand
3. Treatment or exposure
4. Outcome
5. Main identification challenge
6. Proposed empirical design
7. Why the design is valid
8. Required assumptions
9. Statistical model
10. Robustness or placebo checks
11. Heterogeneity analysis
12. Failure modes
13. What cannot be claimed
14. Additional data needed
15. Claim-evidence table

## Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
