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
      "name": "Descriptive Stratification by Pre-Contact Choice × Contact Status",
      "estimand": "Conditional mean differences in contribution probability and amount across four exposure groups defined by pre-contact choice (opted for notice vs. did not) and realized contact (contacted vs. not contacted).",
      "identifying_variation": "Observed associations between self-selected pre-contact choices, realized contact status, and giving outcomes within strata of route, neighborhood, and timing.",
      "critical_assumption": "No causal assumption is required for the descriptive estimand itself; the design explicitly refrains from claiming identification. Any causal interpretation would require unconfoundedness, which the perturbation precludes.",
      "packet_support": "All necessary variables are directly observed in the data structure: pre-contact notice receipt, avoidance signals, realized contact, contribution occurrence, and contribution amount. Route, neighborhood, and timing controls are available for stratification.",
      "fragility": "Cannot support any causal claim. The perturbation removes random assignment of the pre-contact condition, making self-selection the central feature of the data. Group comparisons conflate treatment effects with selection effects by construction.",
      "is_fallback": true
    },
    {
      "name": "Instrumental Variables Using Solicitor Identity and Visit Timing",
      "estimand": "Local average treatment effect (LATE) of in-person contact on contribution probability, for the subpopulation of households whose contact status is shifted by variation in solicitor assignment or visit timing.",
      "identifying_variation": "Different solicitors or teams have different baseline contact rates; visit timing windows (early vs. late in the route) create plausibly exogenous variation in the probability that a household is reached, independent of the household's own giving propensity.",
      "critical_assumption": "Solicitor identity and visit timing affect contribution outcomes only through the probability of contact (exclusion restriction), and solicitor/route assignments are as good as randomly assigned conditional on observable area characteristics.",
      "packet_support": "The data card explicitly lists solicitor or team identifiers and contact timing or visit window as baseline controls and design variables. The organization constructs the initial route list, providing a potential source of quasi-experimental variation in who conducts each visit and when.",
      "fragility": "Solicitor assignment is unlikely to be random in practice: more experienced solicitors may be assigned to higher-income or denser routes. The exclusion restriction is fundamentally untestable. The packet provides no evidence that solicitor assignment or timing is orthogonal to area characteristics, and no explicit randomization protocol is described. The instrument may be weak if solicitor effects on contact are small relative to household self-selection.",
      "is_fallback": false
    },
    {
      "name": "Revealed-Preference Bounding with Avoidance Signals",
      "estimand": "Bounds on the social-pressure component of giving, derived from comparing contribution behavior of households that signaled an avoidance preference but were contacted anyway to households that welcomed contact.",
      "identifying_variation": "The gap between stated avoidance preference and realized contact status: households that explicitly signaled a desire to avoid the visit but were nonetheless contacted reveal a lower bound on pressure-induced giving, while households that sought advance notice and were contacted provide an upper bound on unpressured willingness.",
      "critical_assumption": "The avoidance signal is a truthful revelation of the household's preference not to be solicited, and any contribution from contacted avoiders is attributable primarily to social pressure from the in-person interaction rather than to latent willingness.",
      "packet_support": "The data structure records both whether the household signals a preference to avoid the visit (Stage 2) and whether contact actually occurs (Stage 3), along with contribution outcomes. The four-way classification of avoidance-signal × contact-status × contribution is directly constructable from observed variables.",
      "fragility": "Avoidance signals may be noisy or strategic rather than truthful (e.g., households may signal avoidance to reduce fundraising hassle while still intending to give if contacted). The subpopulation of contacted avoiders may be too small to yield informative bounds. The bounding approach produces intervals rather than point estimates, and those intervals may be wide enough to be substantively uninformative. No auxiliary assumptions about monotonicity or treatment response are verifiable from the packet.",
      "is_fallback": false
    },
    {
      "name": "Selection-on-Observables with Route-Neighborhood Fixed Effects",
      "estimand": "Average treatment effect of receiving advance notice (relative to no notice) on contribution probability, estimated from within-route and within-neighborhood comparisons of households that made different pre-contact choices.",
      "identifying_variation": "Within narrowly defined geographic areas (same route segment, same neighborhood), some households opt for advance notice while others do not; comparing their giving outcomes conditional on a rich set of area-level and timing controls.",
      "critical_assumption": "Conditional on route, neighborhood, building, visit timing, and solicitor fixed effects, the household's pre-contact choice (advance notice vs. not) is independent of potential giving outcomes. All determinants of both selection and giving are captured by the observables.",
      "packet_support": "The packet provides route, building, neighborhood, and area indicators; contact timing or visit window; and solicitor or team identifiers as baseline controls. These permit a high-dimensional fixed-effects specification.",
      "fragility": "The unconfoundedness assumption is implausible in this setting. Household-level characteristics such as altruism, income, social pressure sensitivity, and baseline engagement with the cause likely drive both pre-contact choices and giving outcomes. These are unobserved in the data structure. Even rich geographic and timing controls cannot absorb individual-level selection. The design would produce conditional correlations, not credible causal estimates.",
      "is_fallback": false
    }
  ],
  "recommended_primary": "Descriptive Stratification by Pre-Contact Choice × Contact Status",
  "notes": "The perturbation removes researcher control over the pre-contact condition, which is the core source of identifying variation in the base design. No candidate achieves credible point identification of a causal effect. The IV strategy is the strongest causal candidate but requires an exclusion restriction and quasi-random solicitor assignment that the packet does not support. The bounding approach offers partial identification but depends on the truthfulness of avoidance signals. The recommended primary is the descriptive fallback because it aligns with the packet's instruction to downgrade claims when strong identification is no longer justified."
}
```
