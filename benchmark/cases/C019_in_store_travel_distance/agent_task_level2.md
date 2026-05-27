<!-- visibility: agent-facing -->
<!-- case_id: C019 -->
<!-- variant: level2 -->

# Anonymous Research Design Task: Level 2

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A retailer wants to know whether getting shoppers to cover more of the store will increase unplanned spending. This question matters for both physical layout design and targeted promotional tactics intended to redirect shoppers toward additional categories.

The main difficulty is that route length is not a natural treatment. Shoppers with larger planned baskets, more complicated missions, or more in-store temptations may both walk farther and spend more on unplanned items.

## Research Setting

For each shopping trip, the researcher can collect pre-trip or early-trip information on intended purchases, measure how far the shopper travels through the store, and observe the final basket at checkout. The retailer is also interested in promotion strategies that could redirect shoppers toward categories that are off their most direct route.

## Research Objective

Design a study to estimate whether longer in-store travel causes higher unplanned spending and whether path-inducing promotions can increase unplanned purchases.

## Specific Questions To Answer

1. What is the right causal estimand: observed route length, exogenously induced additional travel, or route-based exposure to product stimuli?
2. How should the design separate pre-trip shopping mission from the causal effect of route length itself?
3. What kind of variation could make route length as-good-as-random or at least plausibly exogenous?
4. What can be learned about promotion strategies that intentionally redirect shoppers to categories off their planned route?

## Causal Mechanisms To Distinguish

- Longer travel may expose shoppers to more products, reminders, and category cues that trigger additional purchases.
- Larger planned missions may mechanically require longer routes and also leave less or more room for unplanned spending, depending on budget slack.
- Unplanned purchases may themselves lengthen the route by sending shoppers to additional locations.
- Congestion, displays, route-tracking noise, or store familiarity may affect both route length and spending.

## Data Structure Overview

- Stage 1: At store entry, the researcher observes or elicits the shopper's planned basket, shopping mission, or expected expenditure.
- Stage 2: During the trip, shopper movement through the store is measured as route length or route path.
- Stage 3: At checkout, the final basket and total spending are observed, allowing the researcher to construct unplanned spending relative to the planned basket.
- Stage 4: In some settings, the retailer can also assign targeted offers intended to draw the shopper toward an unplanned category that is nearer to or farther from the planned route.

## Data Card

| field | description |
|---|---|
| unit of observation | Individual shopping trip. |
| time span | Single-trip setting with pre-trip, in-trip, and post-checkout measurement. |
| geographic or market scope | One or more physical retail locations under a common store format; exact retailer and map are withheld. |
| sample construction | Trips are observed for shoppers who can be linked across entry information, route measurement, and checkout transactions. |
| treatment or exposure variable | Actual route length or exogenously induced additional travel distance during the trip. |
| outcome variable | Trip-level unplanned spending. |
| secondary outcomes | Number of unplanned categories, coupon redemption, or other trip-level spending decomposition outcomes. |
| covariates | Planned basket composition, expected expenditure, budget slack, impulsivity or shopping-style measures, store familiarity, demographics, and trip mission indicators. |
| baseline or pre-treatment variables | Planned categories, shopping mission, and any pre-trip budget or list information observed before route realization. |
| panel or repeated structure | Mainly cross-sectional at the trip level, though multiple trips per shopper could exist in an extension. |
| assignment or variation source | Observed route variation is endogenous; credible designs require either a pre-trip route benchmark or randomized route-inducing intervention. |
| assignment level | Shopper-trip level. |
| outcome measurement level | Shopper-trip level. |
| recommended clustering or inference level | Shopper-trip level; shopper level if repeated trips exist. |
| repeated exposure | Possible if the same shopper appears across multiple trips, but not required. |
| compliance or take-up | Not all shoppers exposed to a route-inducing promotion will redeem or follow it. |
| missingness or attrition | Route measures can be noisy or incomplete; some trips may lack linked entry, path, or checkout information. |
| possible spillover or interference | Minimal direct cross-shopper interference; the main problem is endogenous within-trip exposure. |

## Variable Groups

Define the variable groups needed for the research design. Use generic names rather than source-specific labels.

### Treatment Or Exposure Variables

- Actual in-store route length or route-based exposure.
- Indicator for whether a path-inducing offer or prompt was assigned.
- Distance of the promoted or induced category from the shopper's planned route, if available.

### Selection Or Sample-Flow Variables

- Shopper inclusion in the entry survey or planned-basket collection.
- Availability of usable route measurement.
- Availability of linked checkout transaction data.

### Main Outcome Variables

- Unplanned spending amount.
- Incremental unplanned basket value relative to planned purchases.

### Secondary Outcome Variables

- Number of unplanned categories.
- Promotion redemption or induced detour behavior.

### Baseline Controls And Design Variables

- Planned basket size and composition.
- Expected expenditure or mental budget.
- Budget slack.
- Store familiarity, trip mission, and shopper-level controls.

## Known Constraints

- The design should match the data structure above.
- The answer must distinguish descriptive associations, randomized or quasi-random causal claims, and mechanism claims.
- The answer should state what cannot be learned from the available information.
- Do not label the final identification strategy by name unless you have justified why the data support it.
- Do not rely on unsupported source-specific facts about the original paper, retailer, technology provider, or exact store geometry.

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
