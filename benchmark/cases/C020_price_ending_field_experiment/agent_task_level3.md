<!-- visibility: agent-facing -->
<!-- case_id: C020 -->
<!-- variant: level3 -->

# Anonymous Research Design Task: Level 3

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A retailer wants to know whether a salient terminal-digit pricing format raises demand for a focal item. Managers care not only about whether the tactic works on average, but also about why it works and when it should not be expected to work.

The central challenge is mechanism interpretation. Even if the pricing format is experimentally assigned, a measured effect may reflect a generic bargain signal, an interaction with explicit markdown labeling, or a stronger response when customers have limited prior information about the item.

## Research Setting

Otherwise comparable versions of the same offer can be sent to separate customer groups. The focal item is the same across versions, but the visible price format differs. Some items are relatively new, while others have appeared before and are likely to be more familiar. In some offer environments, explicit promotional or markdown cues may also be present.

## Research Objective

Design a study to estimate the causal effect of terminal-digit pricing format on demand and to determine whether the measured effect reflects the format itself, broader bargain signaling, or interactions with customer information and item familiarity.

## Specific Questions To Answer

1. What is the cleanest estimand for the demand effect of the terminal-digit format?
2. How should the design separate the format effect from low-price or markdown signaling?
3. How should the researcher evaluate whether effects are stronger for newer or less familiar items?
4. Which conclusions about consumer psychology are supportable and which remain too strong?

## Causal Mechanisms To Distinguish

- Terminal-digit or threshold-processing effect tied to the displayed format itself.
- Low-price or markdown signal effect where the format is interpreted as evidence of a bargain.
- Information-limitation effect where the format matters more when customers know less about the item.
- Offer-environment effect where other cues in the same version alter interpretation of the focal price.

## Data Structure Overview

- Stage 1: The researcher selects focal products that can appear in multiple otherwise comparable offer versions.
- Stage 2: Separate customer groups receive different offer versions in which the same focal item is displayed under different price formats.
- Stage 3: The researcher records item-level demand outcomes after exposure to each version.
- Stage 4: Item-history indicators and promotional-context indicators are available to support heterogeneity and mechanism analysis.

## Data Card

| field | description |
|---|---|
| unit of observation | Item-offer exposure or offer-version demand outcome for a focal product. |
| time span | Multiple merchandising or campaign waves; exact dates are withheld. |
| geographic or market scope | Common retail demand environment with separate customer samples; exact channel and retailer are withheld. |
| sample construction | Comparable customer groups receive different versions of the same offer. |
| treatment or exposure variable | Whether the focal item is shown with a salient terminal-digit ending rather than an alternative ending. |
| outcome variable | Demand for the focal product, such as purchases or units sold. |
| secondary outcomes | Differential effects by item familiarity, prior appearance, or promotional context. |
| covariates | Item-history indicators, offer-context indicators, customer-group controls if observed, and product characteristics. |
| baseline or pre-treatment variables | Prior item appearance, product familiarity proxies, and pre-existing promotional classification. |
| panel or repeated structure | Yes; items and customer groups may recur across versions or waves. |
| assignment or variation source | Researcher-controlled variation in price format across otherwise comparable versions. |
| assignment level | Product-offer version or customer-group-by-offer version. |
| outcome measurement level | Product demand or transaction outcome linked to the assigned version. |
| recommended clustering or inference level | Offer-version, product, or customer-group level, depending on the final dataset. |
| repeated exposure | Possible across waves or repeated item appearances. |
| compliance or take-up | Assignment determines displayed price format, but realized purchases remain customer choices. |
| missingness or attrition | Not every product may be manipulable in every wave because of operational restrictions. |
| possible spillover or interference | Other items or promotional cues in the same version may alter how the focal price is interpreted. |

## Variable Groups

### Treatment Or Exposure Variables

- Indicator for salient terminal-digit ending versus alternative ending.
- Indicator for explicit markdown or sale cue.
- Interaction terms between ending format and item familiarity.

### Selection Or Sample-Flow Variables

- Assignment of customer groups to offer versions.
- Inclusion of the focal item in the manipulated sample.
- Availability of item-level demand outcomes.

### Main Outcome Variables

- Item purchases or units sold.
- Demand rate for the focal offer.

### Secondary Outcome Variables

- Differential response by new versus familiar item status.
- Differential response by presence or absence of markdown cues.

### Baseline Controls And Design Variables

- Item history and prior appearance.
- Product or category controls.
- Offer-environment or promotional-context indicators.
- Customer-group controls if available.

## Institutional Details Relevant For Identification

The packet supports a design in which the visible price format can be varied across otherwise comparable offer versions for the same focal product. This means the core assignment problem is more tractable than in historical pricing data where managers choose endings endogenously.

However, the packet does not guarantee that all other cues around the focal item are automatically neutral. Some products are more familiar than others, and some offer versions may make bargain or markdown status more salient. The design therefore has to distinguish assignment validity from interpretation validity.

## Potential Threats

- Potential product-comparability issue: the focal comparison may fail if different products, not the same product, are compared across price endings.
- Potential mechanism-confounding issue: an observed effect may reflect explicit markdown or sale signaling rather than the terminal-digit format itself.
- Potential heterogeneity issue: new and familiar items may respond differently, so a pooled estimate can hide the relevant mechanism.
- Potential offer-environment issue: the surrounding offer context may change customer interpretation of the focal item price.
- Potential compliance or take-up issue: assignment determines the displayed version, but realized purchases remain selective.
- Potential inference or clustering issue: treatment is assigned at the offer-version level, so transaction-level precision can be overstated.
- Potential implementation issue: operational constraints may restrict which items or waves can be manipulated.

## Required Threat-Response Table

In addition to the standard output, include this table. If a threat cannot be addressed with the available data, say so.

| Threat | Why It Matters | Proposed Diagnostic Or Design Response | Remaining Limitation |
|---|---|---|---|

## Known Constraints

- The design should match the data, institutional details, and threats above.
- The answer must distinguish descriptive associations, randomized or quasi-random causal claims, and mechanism claims.
- The answer should state what cannot be learned from the available information.
- Do not turn the threat list into a generic robustness checklist. Connect each threat to the proposed design.
- Do not rely on unsupported source-specific facts about the original paper, retailer, channel, exact customer-sampling rule, or exact price values.

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
