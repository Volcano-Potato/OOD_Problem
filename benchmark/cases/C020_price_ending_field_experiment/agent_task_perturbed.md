<!-- visibility: agent-facing -->
<!-- case_id: C020 -->
<!-- variant: perturbed -->

# Anonymous Research Design Task: Perturbed Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A retailer wants to know whether a salient terminal-digit pricing format raises demand for a focal item, and whether the effect reflects the format itself or broader bargain signaling.

## Research Setting

The retailer can still present otherwise comparable versions of the same offer to separate customer groups, and the focal price format can vary across versions. Demand outcomes are observed for the focal products after exposure.

## Research Objective

Assess whether the measured demand difference under the available variation can still be interpreted as the effect of the terminal-digit format itself.

## Specific Questions To Answer

1. Can the researcher still estimate a credible causal effect of the terminal-digit format itself?
2. What happens if the format variation is no longer separated from markdown or sale labeling?
3. Which claims remain defensible about item-familiarity heterogeneity?
4. What additional design changes would be needed to recover a cleaner interpretation?

## Data Structure Overview

- Stage 1: The researcher selects focal products that can appear in multiple otherwise comparable offer versions.
- Stage 2: Different customer groups receive different versions of the same focal offer.
- Stage 3: The researcher records item-level demand outcomes after exposure.
- Stage 4: Item-history indicators remain available for heterogeneity analysis.

## Data Card

| field | description |
|---|---|
| unit of observation | Item-offer exposure or offer-version demand outcome for a focal product. |
| time span | Repeated merchandising or campaign waves. |
| sample construction | Comparable customer groups receive different versions of the same focal offer. |
| treatment or exposure variable | Whether the focal item is shown with the salient terminal-digit format. |
| outcome variable | Demand for the focal product. |
| secondary outcomes | Differential effects by item familiarity or prior appearance. |
| assignment or variation source | The visible ending format varies across versions, but it is always bundled with explicit markdown or sale presentation rather than being varied independently. |
| assignment level | Product-offer version or customer-group-by-offer version. |
| outcome measurement level | Product demand or transaction outcome linked to the assigned version. |
| panel or repeated structure | Yes; items may recur across versions or waves. |
| compliance or take-up | Assignment determines the displayed version, but realized purchases remain customer choices. |
| spillover or interference | Other cues in the same version may alter interpretation of the focal price. |

## Variable Groups

### Treatment Or Exposure Variables

- Indicator for the salient terminal-digit ending.
- Indicator for explicit markdown or sale presentation, which now moves together with the ending format.

### Selection Or Sample-Flow Variables

- Assignment of customer groups to offer versions.
- Inclusion of the focal item in the manipulated sample.

### Main Outcome Variables

- Item purchases or units sold.

### Secondary Outcome Variables

- Differential response by item familiarity or prior appearance.

### Baseline Controls And Design Variables

- Item history and prior appearance.
- Product or category controls.
- Offer-context indicators.

## Perturbed Condition

The visible ending format is no longer varied independently of bargain presentation. Whenever the focal item uses the salient terminal-digit ending, the surrounding offer also makes the product look explicitly discounted or on promotion. Alternative ending formats appear only in versions without that promotional framing.

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
