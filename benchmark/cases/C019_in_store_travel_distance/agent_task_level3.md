<!-- visibility: agent-facing -->
<!-- case_id: C019 -->
<!-- variant: level3 -->

# Anonymous Research Design Task: Level 3

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

Retailers often assume that increasing how much of the store a shopper covers will increase unplanned spending by exposing the shopper to more product cues. This logic motivates both layout decisions and targeted promotional tactics.

But observed route length is not automatically a treatment. The same trip can feature planned destinations, unplanned detours, in-store triggers, and budget constraints that jointly determine both where the shopper walks and what the shopper buys.

## Research Setting

Researchers can observe a shopper's intended purchases near the beginning of the trip, measure actual route length during the trip, and compare the final basket with the initial plan. In some cases, the retailer can also assign a targeted offer designed to pull the shopper toward an additional category that lies nearer to or farther from the most direct planned route.

## Research Objective

Design a study to estimate the causal effect of longer in-store travel on unplanned spending and to evaluate whether route-inducing promotions increase unplanned purchases.

## Specific Questions To Answer

1. What design can separate endogenous wandering from the causal effect of route length?
2. How should the study use pre-trip information about planned purchases or shopping mission?
3. What assumptions are needed if the design uses a route benchmark or route-inducing intervention?
4. What can and cannot be claimed about broader revenue or welfare implications?

## Causal Mechanisms To Distinguish

- Longer travel may increase exposure to products and reminders that trigger unplanned purchases.
- Larger or more flexible shopping missions may generate both longer routes and higher unplanned spending even without a causal route effect.
- Additional unplanned purchases may themselves cause further travel.
- In-store displays, congestion, or route-tracking noise may contaminate the relationship between observed path length and spending.

## Data Structure Overview

- Stage 1: A shopper enters with a planned basket, mission, or expected spending target that can be observed or elicited.
- Stage 2: The shopper's route through the store is measured while the trip unfolds.
- Stage 3: Checkout records reveal the final basket and total spending, allowing unplanned spending to be constructed.
- Stage 4: Some trips may additionally include a route-inducing offer or prompt for a category not on the initial plan.

## Data Card

| field | description |
|---|---|
| unit of observation | Individual shopping trip. |
| time span | Single-trip setting with pre-trip, in-trip, and post-checkout measurement. |
| geographic or market scope | One or more physical retail locations under a common layout and measurement system; exact retailer and map are withheld. |
| sample construction | Trips are included only when entry information, route measures, and checkout transactions can be linked. |
| treatment or exposure variable | Actual route length or exogenously induced additional travel distance. |
| outcome variable | Trip-level unplanned spending. |
| secondary outcomes | Number of unplanned categories, redemption behavior, or other trip-level spending components. |
| covariates | Planned basket composition, expected expenditure, budget slack, shopping style, store familiarity, and demographics. |
| baseline or pre-treatment variables | Pre-trip plan, mission, and expected spend observed before the route unfolds. |
| panel or repeated structure | Primarily cross-sectional at the trip level. |
| assignment or variation source | Observed route variation is endogenous; credible variation must come from a pre-trip route benchmark or randomized route-inducing prompt. |
| assignment level | Shopper-trip level. |
| outcome measurement level | Shopper-trip level. |
| recommended clustering or inference level | Shopper-trip level; shopper level if multiple trips per shopper are observed. |
| repeated exposure | Possible but not required. |
| compliance or take-up | Route-inducing prompts may not be followed or redeemed. |
| missingness or attrition | Route measures may be noisy, and some trips may lack complete linkage. |
| possible spillover or interference | Cross-shopper spillovers are limited; the major issue is within-trip endogeneity. |

## Variable Groups

### Treatment Or Exposure Variables

- Actual route length.
- Route-benchmark or route-inducing variation if observed.
- Indicator for farther-versus-nearer promotional prompts, if assigned.

### Selection Or Sample-Flow Variables

- Inclusion in pre-trip basket capture.
- Availability of usable route measures.
- Availability of linked checkout records.

### Main Outcome Variables

- Unplanned spending amount.
- Incremental unplanned basket value relative to planned purchases.

### Secondary Outcome Variables

- Number of unplanned categories.
- Redemption behavior for route-inducing prompts.

### Baseline Controls And Design Variables

- Planned basket size and composition.
- Expected expenditure or mental budget.
- Budget slack.
- Store familiarity, trip mission, and shopper-level controls.

## Institutional Details Relevant For Identification

- Actual route length is realized during the trip and is partly under the shopper's control.
- The researcher can observe planned purchases or a pre-trip mission before in-store wandering occurs.
- Checkout outcomes are observed after all route and purchase decisions have been made.
- Some interventions can be assigned before the shopper reaches the relevant decision point, creating exogenous incentives to travel farther or not.
- Route measurement may be noisy and may not perfectly capture every detour or micro-movement.
- The retailer may care about both immediate unplanned spending and broader shopping convenience, but the available data focus mainly on the current trip.

## Potential Threats

- Potential endogenous-exposure issue: shoppers with larger or more flexible missions may both walk farther and spend more unplanned dollars.
- Potential simultaneity issue: unplanned purchases may create additional travel rather than the other way around.
- Potential omitted-variable issue: displays, congestion, product salience, or shopper impulsivity may affect both route length and spending.
- Potential measurement issue: route-tracking measures may be noisy or incomplete.
- Potential selection issue: only shoppers with complete entry, path, and checkout linkage enter the analysis.
- Potential compliance issue: assigned route-inducing promotions may not be redeemed or followed.
- Potential interpretation issue: more unplanned spending on the current trip need not imply higher long-run incremental revenue or shopper welfare.

## Required Threat-Response Table

In addition to the standard output, include this table. If a threat cannot be addressed with the available data, say so.

| Threat | Why It Matters | Proposed Diagnostic Or Design Response | Remaining Limitation |
|---|---|---|---|

## Known Constraints

- The design should match the data, institutional details, and threats above.
- The answer must distinguish descriptive associations, randomized or quasi-random causal claims, and mechanism claims.
- The answer should state what cannot be learned from the available information.
- Do not turn the threat list into a generic robustness checklist. Connect each threat to the proposed design.
- Do not rely on unsupported source-specific facts about the original paper, exact tracking technology, or exact store map.

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
