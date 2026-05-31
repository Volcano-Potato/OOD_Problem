# Stage 4: Independent Critique

You are acting as an independent design critic.

You are given:

- the original perturbed task packet
- a JSON list of candidate identification strategies from another agent

Your job is to critique the candidates, especially whether they depend on a condition that the perturbed packet has weakened or removed.

## Instructions

1. For each candidate, identify at least 2 packet-grounded threats.
2. Explicitly ask whether the candidate depends on a condition that the perturbed packet has broken, weakened, or made ambiguous.
3. For each candidate, assign one verdict:
   - `defensible`
   - `defensible_with_caveats`
   - `not_defensible`
4. If no candidate is defensible, recommend a descriptive fallback.
5. Keep the critique grounded in the provided packet and candidate JSON.
6. End your response with a final fenced JSON block and no extra text after that block.

## Required Final JSON Block

```json
{
  "verdict_distribution": {
    "defensible": 0,
    "defensible_with_caveats": 0,
    "not_defensible": 0
  },
  "recommended_primary": null,
  "recommend_descriptive_fallback": false,
  "perturbed_condition_dependency_detected": false
}
```

## Original Packet

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


## Stage 3 Candidate JSON

```json
{
  "candidates": [
    {
      "name": "Intent-to-Treat (ITT)",
      "estimand": "Average causal effect of campaign assignment or eligibility on downstream conversion outcomes, regardless of whether the focal ad was actually served.",
      "identifying_variation": "Higher-level randomization or holdout assignment that determines which users become eligible for campaign delivery, generating as-good-as-random variation in assignment status independent of potential outcomes.",
      "critical_assumption": "Assignment is as-good-as-random (no differential selection into assignment groups) and the Stable Unit Treatment Value Assumption holds (no interference or spillover across users).",
      "packet_support": "Packet explicitly states that 'Campaign-level randomization or holdout assignment exists' (Stage 2 of the data structure). Assignment status, actual impressions, and downstream outcomes are all observed in the logs. The randomization design is pre-specified and does not depend on opportunity-side logs for untreated users.",
      "fragility": "ITT does not estimate the effect of actual ad exposure—it estimates the effect of being eligible to be served the ad, which includes users who were assigned but never received an impression. This may not satisfy the research objective to measure 'the causal effect of actual digital ad exposure.' ITT estimates are diluted by non-compliance (one-sided, since the unassigned group cannot receive the ad). If the take-up rate is low, power is severely reduced. Interference from market-level saturation or cross-channel exposure could also bias the estimate.",
      "is_fallback": false
    },
    {
      "name": "Instrumental Variables LATE via Random Assignment",
      "estimand": "Local Average Treatment Effect of actual focal-ad exposure on downstream conversions among compliers—users who would receive an impression if and only if assigned to campaign eligibility.",
      "identifying_variation": "Random or holdout-based assignment serves as an instrument Z for actual exposure D. Exogenous variation in Z induces variation in D (through the first stage) that is orthogonal to unobserved confounders, permitting identification of the causal effect of D on Y for the complier subpopulation.",
      "critical_assumption": "Exclusion restriction: assignment affects downstream outcomes only through its effect on actual ad exposure. No direct effect of assignment on outcomes through alternative channels (e.g., assignment status does not change platform behavior, other targeting, or user experience beyond the focal ad). Also requires monotonicity (no defiers who would receive the ad only when unassigned).",
      "packet_support": "The data structure describes staged eligibility: Stage 2 randomization exists; Stage 3 platform delivery is observed; Stage 4 outcomes are observed. The first-stage relationship between assignment and actual exposure is estimable because both assignment and realized impressions appear in logs for both assigned and unassigned groups. The reduced form (ITT) is also estimable. The IV ratio is computable without opportunity-side logs for untreated users.",
      "fragility": "Missing opportunity-side logs make it impossible to characterize the complier population or verify that compliers are comparable to the full eligible population. Exclusion restriction is not testable without opportunity-level data (cannot check whether assignment alters platform behavior toward users in ways unrelated to the focal ad, e.g., different auction dynamics or ad load). Monotonicity may be violated if assignment status changes platform bidding or optimization in ways that reduce exposure for some assigned users. If the first stage is weak (low take-up), LATE estimates have wide confidence intervals and are sensitive to small violations. SUTVA violations from market-level saturation or cross-channel spillover threaten both first-stage and reduced-form validity. The IV strategy identifies a complier-specific effect that may not generalize to always-takers or never-takers.",
      "is_fallback": false
    },
    {
      "name": "Selection-on-Observables Descriptive Regression",
      "estimand": "Conditional association between actual focal-ad exposure and downstream conversion outcomes, adjusted for observable pre-campaign user activity, device, channel, segment, and time-of-opportunity indicators.",
      "identifying_variation": "Residual variation in actual ad exposure after controlling for observed baseline characteristics and delivery covariates. Users with similar observable profiles but different realized exposure provide the comparison.",
      "critical_assumption": "Unconfoundedness given observables: after conditioning on pre-campaign activity, device, channel, segment, and timing controls, any remaining variation in actual ad exposure is as-good-as-random with respect to potential outcomes.",
      "packet_support": "Packet provides baseline controls including pre-campaign user activity, device, channel, segment, and time-of-opportunity indicators. Actual impressions and downstream outcomes are observed. The panel structure permits rich user-level fixed effects or pre-treatment covariate histories. No opportunity-side logs are needed for this approach.",
      "fragility": "The unconfoundedness assumption is not credible in this setting. Platform delivery systems use auctions, targeting rules, pacing, and optimization—all of which select users for ad exposure based on characteristics that are likely correlated with conversion propensity (e.g., predicted click-through rate, bidding strategy adjustments based on user value). These platform-internal selection variables are absent from the researcher's observable covariate set. Even with rich pre-campaign controls, the selection mechanism is endogenous by design (the platform optimizes for outcomes correlated with the researcher's outcome). No causal interpretation is defensible.",
      "is_fallback": true
    },
    {
      "name": "Within-User Pre-Post Exposure Trajectory Comparison",
      "estimand": "Change in the user-level outcome trajectory after the first focal-ad impression, relative to the same user's pre-exposure baseline trajectory, among users who received at least one impression.",
      "identifying_variation": "Within-user temporal variation: the same user transitions from an unexposed state to an exposed state at the time of first impression. The user serves as their own counterfactual via their pre-exposure outcome path.",
      "critical_assumption": "Parallel trends at the user level: absent ad exposure, each user's outcome trajectory would have continued along its pre-exposure path. No time-varying confounders (e.g., seasonal shopping, concurrent promotions, life events) coincide with the timing of first exposure.",
      "packet_support": "Packet describes a panel or repeated structure where 'Users can have multiple ad opportunities and multiple impressions over time' and 'pre-campaign user activity' is available. The short campaign window plus post-exposure outcome window supports a before-after comparison. The design uses only data that are observed (impressions, outcomes, pre-campaign activity).",
      "fragility": "Only exposed users are included—no untreated comparison group. Cannot separate the ad effect from common time trends, seasonality, or contemporaneous shocks affecting all users during the campaign window. The platform's delivery optimization means the timing of first exposure is endogenous (users may be served the ad when they are already on an upward conversion trajectory). Regression to the mean is a serious concern: users with extreme pre-campaign activity may naturally revert. Without an unexposed control group experiencing the same calendar time, no causal claim about ad exposure is credible.",
      "is_fallback": false
    }
  ],
  "recommended_primary": "Intent-to-Treat (ITT)",
  "notes": "The ITT is the only design that rests on clean, defensible identification from the packet's randomization structure without requiring unverifiable assumptions. The IV/LATE design is computationally feasible even without opportunity-side logs but is substantially weakened: missing opportunity-side data prevent complier characterization, exclusion-restriction diagnostics, and assessment of whether the platform's delivery behavior toward assigned users differs from delivery toward unassigned users in ways unrelated to the focal ad. The naive exposure-outcome regression and pre-post designs are included for completeness but should not be interpreted as causal. If the research question genuinely requires the effect of actual exposure (not assignment), the IV/LATE should be reported with heavy caveats and accompanied by the ITT as the primary credible causal benchmark."
}
```
