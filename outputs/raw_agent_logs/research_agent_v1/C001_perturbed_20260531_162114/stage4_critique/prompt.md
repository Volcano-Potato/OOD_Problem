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
<!-- case_id: C001 -->
<!-- variant: perturbed -->

# Anonymous Research Design Task: Perturbed Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

Organizations that rely on voluntary contributions often use direct personal requests to raise funds. Those requests may increase giving because people genuinely want to support the cause, because they feel pressure when confronted in person, or because communication changes who is available and willing to engage.

The research problem is to design a field study that separates these explanations rather than estimating only an undifferentiated average effect of solicitation.

## Research Setting

A fundraising organization approaches residential units in person and can observe whether contact occurs and whether a contribution is made. Potential donors may differ in how much they want to engage with the fundraiser, and pre-contact choices may affect who is ultimately exposed to the interaction.

## Research Objective

Design a study to estimate whether voluntary contributions in an in-person request setting reflect genuine willingness to support the cause, social pressure from the interaction, or both.

## Specific Questions To Answer

1. Which design can estimate the effect of solicitation conditions on contact and giving?
2. How can the study distinguish pressure-related giving from genuine willingness to contribute?
3. How should the researcher handle the fact that pre-contact interaction conditions are no longer assigned by the researcher?
4. Which parts of the proposed design still support causal claims, and which become only suggestive?

## Data Structure Overview

- Stage 1: The organization constructs a list or route of planned in-person solicitation opportunities.
- Stage 2: Before the visit, households may choose whether to receive advance notice or signal that they prefer not to be approached.
- Stage 3: During the visit window, the researcher observes whether contact occurs and whether a contribution is made.
- Stage 4: Supplementary information may be available on route, timing, solicitor, and contribution size patterns.

## Data Card

| field | description |
|---|---|
| unit of observation | Household or individual solicitation opportunity. |
| time span | Short field window around scheduled in-person solicitation attempts; exact dates are not provided. |
| sample construction | Potential donors are selected from a feasible contact list or route plan before solicitation. |
| treatment or exposure variable | Solicitation-process condition before the in-person request, including whether the household receives advance notice or a lower-friction way to avoid contact. |
| outcome variable | Whether contact occurs, whether the person contributes, contribution amount, and contribution size bins. |
| secondary outcomes | Conditional giving among contacted units, engagement or avoidance behavior, and contribution-size patterns. |
| assignment or variation source | Households can choose whether to receive pre-contact notice or indicate a preference not to be approached after hearing about the campaign in advance; the researcher observes these choices rather than assigning them. |
| assignment level | Household or individual contact opportunity. |
| outcome measurement level | Contact opportunity and resulting interaction. |
| panel or repeated structure | Primarily one planned solicitation event per unit. |
| compliance or take-up | Some households may be absent, unreachable, or inconsistent between stated preferences and realized contact. |
| spillover or interference | Neighbors may communicate about the fundraiser; solicitor behavior may change across routes or conditions. |

## Variable Groups

### Treatment Or Exposure Variables

- Whether the household receives pre-contact notice.
- Whether the household signals a preference to avoid the visit.

### Selection Or Sample-Flow Variables

- Planned contact opportunity.
- Household choice over pre-contact interaction status.
- Whether contact actually occurs.

### Main Outcome Variables

- Whether a contribution is made.
- Contribution amount.

### Secondary Outcome Variables

- Whether contact occurs.
- Small versus large contribution categories.

### Baseline Controls And Design Variables

- Route, building, neighborhood, or area indicators.
- Contact timing or visit window.
- Solicitor or team identifiers.

## Perturbed Condition

The pre-contact interaction condition is no longer assigned by the researcher. Households can choose whether to receive advance notice or indicate that they prefer not to be approached after learning about the fundraising campaign beforehand.

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
      "name": "Partial Identification via Contact-Behavior Bounds",
      "estimand": "Bounds on the fraction of giving attributable to social pressure versus genuine willingness, leveraging the necessary condition that contact must occur before giving.",
      "identifying_variation": "Observed variation in household pre-contact avoidance choices combined with variation in contact and contribution outcomes across households that do and do not receive advance notice.",
      "critical_assumption": "Monotonicity of selection into contact: households that would avoid contact under advance-notice conditions would also avoid contact under no-notice conditions (no 'defiers' who seek contact only when they have a chance to opt out).",
      "packet_support": "The packet describes a three-stage structure (pre-contact choice → contact → contribution) where contact is a necessary intermediate step; households can signal a preference to avoid the visit; contact occurrence is observed alongside contribution outcomes. This structure supports bounding exercises using the relationship between avoidance and giving.",
      "fragility": "Monotonicity may fail if advance notice mobilizes some households to give who would otherwise be absent (generating defiers); bounds may be too wide to distinguish pressure from willingness in practice given the single-observation-per-unit structure; packet provides no auxiliary data (e.g., survey measures of altruism) to tighten bounds.",
      "is_fallback": false
    },
    {
      "name": "Route-and-Solicitor Stratified Observational Comparison",
      "estimand": "Conditional association between pre-contact choice status and giving outcomes, controlling for route, neighborhood, timing, and solicitor fixed effects.",
      "identifying_variation": "Within-route, within-solicitor variation in household pre-contact choices (opt-in to advance notice, signal avoidance, or neither) and subsequent contact and contribution outcomes.",
      "critical_assumption": "Conditional on route, neighborhood, timing window, and solicitor identifiers, a household's pre-contact choice is as-good-as-random with respect to unobserved determinants of giving (selection on observables).",
      "packet_support": "Baseline controls and design variables listed in the packet include route, building, neighborhood, area indicators, contact timing, visit window, and solicitor/team identifiers. The multi-stage data structure (planned route → pre-contact choice → contact → contribution) is observed for each unit.",
      "fragility": "Selection on observables is almost certainly violated: unobserved household characteristics (altruism, income, social-desirability bias, prior relationship with the cause) simultaneously drive pre-contact choices and giving propensity. The packet explicitly states pre-contact conditions are chosen by households rather than assigned, making this design correlational at best for the pre-contact-choice-to-giving pathway.",
      "is_fallback": false
    },
    {
      "name": "Solicitor-Induced Contact Instrumental Variables",
      "estimand": "Local average treatment effect (LATE) of in-person contact on contribution, among households whose contact status is influenced by which solicitor visits them.",
      "identifying_variation": "Cross-solicitor variation in contact rates within the same route or neighborhood, used as an instrument for whether contact occurs.",
      "critical_assumption": "Solicitor assignment is as-good-as-random within routes and affects giving only through the contact channel (exclusion restriction). Solicitor characteristics affect the probability of contact but not contribution amounts directly.",
      "packet_support": "The packet lists solicitor or team identifiers as baseline control/design variables. Contact occurrence and contribution outcomes are observed. The staged structure (route plan → pre-contact choice → visit/contact → contribution) makes contact a measurable intermediate step.",
      "fragility": "The exclusion restriction is likely violated: solicitor skill, persistence, or personal characteristics may directly affect contribution amounts conditional on contact (e.g., more persuasive solicitors generate both more contact and larger gifts). The packet explicitly warns that 'solicitor behavior may change across routes or conditions,' suggesting solicitor effects are not cleanly separable. Solicitor assignment is not described as random; the organization may assign better solicitors to higher-potential routes. This design cannot separate pressure from willingness within the contact effect.",
      "is_fallback": false
    },
    {
      "name": "Descriptive Decomposition of Solicitation Patterns",
      "estimand": "Unadjusted associations among pre-contact choice, contact occurrence, contribution probability, and contribution size, with decomposition of overall giving rates by pre-contact choice group.",
      "identifying_variation": "All observed variation in the data — cross-household, cross-route, cross-solicitor — used purely to describe patterns without asserting causal identification.",
      "critical_assumption": "No causal identifying assumption is required. The analysis treats all observed associations as descriptive and explicitly refrains from causal interpretation of pre-contact-choice-to-giving pathways.",
      "packet_support": "The full data structure (contact occurrence, contribution yes/no, contribution amount, contribution size bins, pre-contact choices, route identifiers, solicitor identifiers, timing) supports rich descriptive tabulation and visualization. The packet provides explicit outcome variables and baseline controls for stratification.",
      "fragility": "This design cannot answer the core research question of separating social pressure from genuine willingness; it can only document that the two mechanisms are observationally entangled. The packet's research objective — 'estimate whether voluntary contributions reflect genuine willingness, social pressure, or both' — remains unaddressed. This is a fallback when causal designs are not defensible.",
      "is_fallback": true
    }
  ],
  "recommended_primary": "Partial Identification via Contact-Behavior Bounds",
  "notes": "The perturbed condition — households self-select into pre-contact status — fundamentally breaks random-assignment-based identification. No candidate can credibly point-identify the separation of social pressure from genuine willingness without strong, untestable assumptions. The partial identification candidate is recommended as primary because it is the most honest about what can and cannot be learned: it explicitly acknowledges that only bounds are attainable and makes its monotonicity assumption transparent. The solicitor-IV candidate provides limited leverage for the contact→giving margin but cannot separate pressure from willingness. The descriptive fallback is included because the packet's instructions require a fallback when credible causal identification is not defensible, which is the case here."
}
```
