# Stage 3: Candidate Identification Strategies

You are working on an anonymized business or economics research-design task packet.

Your job in this stage is not to write the final report. Your job is to enumerate candidate designs before any final commitment.

## Instructions

1. Read the packet carefully.
2. List at least 3 distinct candidate strategies.
3. Do not collapse multiple ideas into one bundled candidate.
4. If no credible causal design is defensible from the packet, at least one candidate must be a descriptive fallback and set `is_fallback` to `true`.
5. Stay inside the packet. Do not reconstruct hidden paper details.
6. Output JSON only. No prose before or after the JSON.

## Required JSON Schema

```json
{
  "candidates": [
    {
      "name": "short candidate name",
      "estimand": "target estimand or strongest defensible target",
      "identifying_variation": "what variation would identify it",
      "critical_assumption": "most important identifying assumption",
      "packet_support": "which packet-local evidence motivates this candidate",
      "fragility": "why this candidate may fail in this packet",
      "is_fallback": false
    }
  ],
  "recommended_primary": "candidate name or null",
  "notes": "optional short note"
}
```

## Packet

<!-- visibility: agent-facing -->
<!-- case_id: C019 -->
<!-- variant: perturbed -->

# Anonymous Research Design Task: Perturbed Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A retailer wants to know whether longer in-store travel increases unplanned spending and whether path-inducing promotions are useful. The challenge is still that route length is a choice-driven exposure rather than a naturally randomized treatment.

## Research Setting

The researcher can observe a shopper's actual route through the store and the final basket at checkout. The retailer also observes which category-level prompts were available near different store areas. However, unlike the base case, there is no reliable pre-trip record of the shopper's planned basket or intended mission.

## Research Objective

Design a study to estimate whether longer in-store travel causes higher unplanned spending when no reliable pre-trip basket information is available.

## Specific Questions To Answer

1. Can the original route-based identification logic still work?
2. What kinds of causal claims remain plausible with only observed routes, prompts, and checkout outcomes?
3. What additional data or redesign would be needed to recover a stronger route-based causal design?
4. What descriptive or predictive analyses are still defensible?

## Data Structure Overview

- Stage 1: Shoppers enter the store and begin shopping, but there is no validated pre-trip basket or mission capture.
- Stage 2: The shopper's route through the store is measured during the trip, and category-level prompts or stimuli may be observed.
- Stage 3: Checkout records reveal the final basket and total spending, allowing some definition of unplanned or additional spending.
- Stage 4: The retailer may know which prompts were displayed, but does not know the shopper's original intended basket before wandering begins.

## Data Card

| field | description |
|---|---|
| unit of observation | Individual shopping trip. |
| time span | Single-trip setting with in-trip measurement and post-checkout outcomes. |
| sample construction | Trips are observed when route measures and checkout transactions are available, but there is no reliable pre-trip planning record. |
| treatment or exposure variable | Actual route length or observed route-inducing prompts. |
| outcome variable | Trip-level unplanned or additional spending. |
| secondary outcomes | Number of unplanned categories or prompt redemption if observed. |
| assignment or variation source | Observed route and prompt exposure; no validated pre-trip route benchmark is available. |
| assignment level | Shopper-trip level. |
| outcome measurement level | Shopper-trip level. |
| panel or repeated structure | Primarily cross-sectional at the trip level. |
| compliance or take-up | Shoppers may ignore or partially respond to prompts. |
| spillover or interference | Minimal cross-shopper interference; the main issue is endogenous within-trip exposure. |

## Variable Groups

### Treatment Or Exposure Variables

- Actual route length.
- Observed prompts or in-store stimuli.

### Selection Or Sample-Flow Variables

- Availability of usable route measures.
- Availability of linked checkout records.

### Main Outcome Variables

- Unplanned or additional spending amount.

### Secondary Outcome Variables

- Number of unplanned categories.
- Prompt-response indicators if available.

### Baseline Controls And Design Variables

- Shopper demographics and store familiarity measures if available.

## Perturbed Condition

The reliable pre-trip planned basket and mission capture used in the base setting is unavailable here. The researcher sees where the shopper walked and what the shopper bought, but not a validated statement of what the shopper intended to buy before the trip unfolded.

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

