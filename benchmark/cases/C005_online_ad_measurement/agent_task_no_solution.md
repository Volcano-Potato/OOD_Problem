<!-- visibility: agent-facing -->
<!-- case_id: C005 -->
<!-- variant: no_solution -->

# Anonymous Research Design Task: No-Solution Variant

## Task Rule

You must not search the web, infer the original paper, or use external literature. Use only the information provided below. Your goal is to design a rigorous empirical strategy, not to write a literature review.

Do not assume that a known paper has already solved the task. Treat this as an anonymous applied business/economics research problem.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A firm wants to know whether seeing a digital advertising campaign causes users to visit, sign up, or purchase. The platform provides detailed behavioral logs, and exposure appears measurable at the user level.

The business question is highly consequential, but detailed exposure data do not by themselves solve the causal measurement problem if delivery is driven by targeting and optimization.

## Research Setting

An advertiser runs a campaign on an online platform that uses targeting, auctions, and optimization to decide who sees ads. The advertiser and researcher can observe user-level impression logs, clicks, site visits, conversions, and many user covariates, but there is no experimental holdout in the available dataset.

## Research Objective

Assess whether users who see the focal campaign are more likely to convert and whether those differences can be interpreted as causal ad lift.

## Specific Questions To Answer

1. Are exposed users more likely to convert than unexposed users?
2. Can rich user-level controls make that comparison causal?
3. What can be learned descriptively or predictively from exposure and conversion logs?
4. What additional design or data would be needed to estimate causal lift credibly?

## Data Structure Overview

- Stage 1: Users browse or search on the platform and become eligible for targeted campaign delivery.
- Stage 2: The platform decides whom to expose based on targeting, bidding, and optimization rules.
- Stage 3: The researcher observes actual impression, click, and conversion logs for exposed and unexposed users.
- Stage 4: The advertiser also has rich pre-campaign user behavior and segment-level covariates.

## Available Data

| field | description |
|---|---|
| unit of observation | User-level or user-impression-level campaign log linked to downstream outcomes. |
| time span | Campaign-period exposure data plus downstream conversion window. |
| sample construction | Users eligible for targeting under the platform's operational rules during the campaign. |
| treatment or exposure variable | Actual exposure to the focal campaign, impression counts, clicks, and recency or frequency measures. |
| outcome variable | Conversions such as visits, sign-ups, purchases, or revenue. |
| secondary outcomes | Clicks, intermediate engagement, and repeat visits. |
| covariates | Rich user history, browsing behavior, past purchases, device, geography, segment, and platform prediction scores if available. |
| panel or repeated structure | Users can appear many times across impressions and over time. |
| assignment or variation source | Exposure is determined by targeting, bidding, and platform optimization rather than experimental assignment. |
| assignment level | User or impression level. |
| outcome measurement level | User-level downstream conversion. |
| missingness or attrition | Tracking can be incomplete because of identifier loss, cross-device behavior, or attribution windows. |
| possible spillover or interference | Users may see ads on other channels or be affected by broader campaign saturation. |

## Variable Groups

### Treatment Or Exposure Variables

- Impression exposure.
- Exposure frequency and recency.
- Click behavior.

### Selection Or Sample-Flow Variables

- Eligibility for targeting.
- Observed exposure versus non-exposure.
- Inclusion in tracked conversion logs.

### Main Outcome Variables

- Conversion indicator.
- Revenue or purchase outcome.

### Secondary Outcome Variables

- Clicks.
- Repeat visits.
- Other intermediate engagement events.

### Baseline Controls And Design Variables

- Pre-campaign browsing and purchase history.
- Device, segment, and platform prediction scores.
- Time and market indicators.

## Identification Limitations

- No randomized assignment or quasi-random variation is provided.
- No credible instrument, threshold, boundary, or externally imposed timing shock is provided.
- Exposed and unexposed users may differ in unobserved purchase intent even after rich controls.
- Observed exposure and click behavior cannot separate incremental ad effects from targeting selection.

## Known Constraints

- The task should still look empirically tempting: many covariates, clear outcomes, and real business relevance.
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
