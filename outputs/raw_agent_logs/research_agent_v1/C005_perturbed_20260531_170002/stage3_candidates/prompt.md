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
<!-- case_id: C005 -->
<!-- variant: perturbed -->

# Anonymous Research Design Task: Perturbed Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

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
2. What comparison group would make exposed users comparable to an untreated counterfactual if opportunity-side control logs are unavailable?
3. How should the design distinguish a campaign-level assignment effect from the effect of actual exposure?
4. Which claims about ad lift remain credible under the available logging structure?

## Data Structure Overview

- Stage 1: Users become eligible for the campaign during a live delivery window with platform-level auctions or allocation rules.
- Stage 2: Some higher-level randomization or holdout assignment can affect whether users are eligible to receive the campaign.
- Stage 3: Conditional on eligibility, the platform determines whether the focal ad is actually served at each opportunity.
- Stage 4: The researcher observes actual impressions and downstream conversions, but does not retain logs identifying which untreated users had the same opportunity to receive the focal ad.

## Data Card

| field | description |
|---|---|
| unit of observation | User-ad opportunity or user-impression record linked to downstream user outcomes where available. |
| time span | Short campaign window plus a post-exposure outcome window. |
| sample construction | Eligible users enter platform auctions or delivery opportunities during the campaign. Logs include campaign assignment, realized impressions, and downstream outcomes. |
| treatment or exposure variable | Campaign assignment or eligibility, actual focal-ad exposure, and repeated exposure counts if available. |
| outcome variable | Downstream conversion outcomes such as website visit, registration, lead, purchase, or revenue. |
| secondary outcomes | Intermediate engagement outcomes and any auxiliary delivery outcomes if observed. |
| assignment or variation source | Campaign-level randomization or holdout assignment exists, but the platform does not retain opportunity-side logs for untreated users. |
| assignment level | User or ad-opportunity level, depending on the platform implementation. |
| outcome measurement level | User-level downstream conversion, optionally linked to actual impression records. |
| panel or repeated structure | Users can have multiple ad opportunities and multiple impressions over time. |
| compliance or take-up | Assignment or eligibility does not guarantee actual exposure because the focal ad may not be served. |
| spillover or interference | Users may see ads on other channels, share information, or be affected by market-level campaign saturation. |

## Variable Groups

### Treatment Or Exposure Variables

- Campaign assignment or eligibility.
- Actual focal-ad exposure.

### Selection Or Sample-Flow Variables

- Eligibility for campaign delivery.
- Realized impression or non-delivery.

### Main Outcome Variables

- Downstream conversions.
- Revenue or purchase indicators if observed.

### Secondary Outcome Variables

- Intermediate engagement events.
- Exposure frequency.

### Baseline Controls And Design Variables

- Pre-campaign user activity.
- Device, channel, segment, and time-of-opportunity indicators.

## Perturbed Condition

The platform retains campaign assignment and actual impression logs, but it does not retain logs that identify which untreated users had the same opportunity to receive the focal ad.

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

