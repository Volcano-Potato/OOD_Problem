# Stage 5: Final Design Memo

You are writing the final memo after reviewing:

- the original perturbed task packet
- the Stage 3 candidate list
- the Stage 4 independent critique

Your output must follow the existing evidence-aware benchmark report structure.

## Required Reconciliation Rule

You must reconcile the Stage 4 critic verdict.

- If the critic marks a candidate `not_defensible`, do not present it as a credibly identified causal design unless you explicitly point to packet-local evidence that the critic missed.
- If the critic recommends a descriptive fallback, you must either adopt that downgrade or explain, with packet-local evidence, why a stronger design is still defensible.
- In section 17, explicitly state what cannot be claimed in light of the critique.

## Required Output Contract

Follow this structure exactly:

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

Use the canonical claim-evidence table header:

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|

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

## Stage 4 Critique

# Independent Design Critique: C001 Perturbed Variant

## Candidate 1: Partial Identification via Contact-Behavior Bounds

### Threat 1 — Monotonicity is Untestable and Plausibly Violated Under Self-Selection

The packet's perturbed condition removes researcher assignment of pre-contact status. When households *choose* whether to receive advance notice or signal avoidance, the monotonicity assumption (no households that would avoid contact under advance-notice but seek contact under no-notice) becomes substantially harder to defend. Consider: a household that learns about the campaign through advance notice may be *mobilized* to be present and give, whereas without notice they would be absent. These "defiers" — households activated by notice rather than deterred by it — directly violate monotonicity. The packet acknowledges this fragility ("monotonicity may fail if advance notice mobilizes some households") but the perturbation makes this failure mode *more likely*, not less, because self-selection into notice-receipt is correlated with engagement motivation. With only one solicitation event per unit (the packet says "Primarily one planned solicitation event per unit"), there is no within-unit variation to test or relax this assumption.

### Threat 2 — Bounds Confound Avoidance-Choice Mechanism with Giving Mechanism

The bounds approach uses observed avoidance choices to bound the pressure vs. willingness decomposition. But under the perturbation, avoidance is an endogenous choice. A household that signals avoidance may do so because (a) they feel acute social pressure and want to escape it, or (b) they have zero genuine willingness to give and see no reason to engage. These two types have opposite implications for the pressure/willingness decomposition, yet the bounding logic cannot distinguish them without auxiliary data. The packet provides no survey measures of altruism, pressure sensitivity, or motivation — the candidate itself notes "packet provides no auxiliary data (e.g., survey measures of altruism) to tighten bounds." Without such data, the bounds will span both interpretations, making them uninformative for the core research question.

### Perturbed-Condition Dependency

**Yes.** The bounding logic implicitly relies on avoidance behavior being informative about latent type (pressure-sensitive vs. genuinely willing). Under random assignment of pre-contact conditions, avoidance behavior is a response to an exogenous nudge and can be interpreted as revealing type. Under self-selection (the perturbation), the choice to opt into notice or signal avoidance is itself an equilibrium outcome of unobserved characteristics. The same unobserved characteristic (e.g., low altruism) could drive both avoidance and low giving, making the bounds confound type with selection. The perturbation doesn't merely widen the bounds — it changes what the bounds *mean*.

### Verdict: `defensible_with_caveats`

This is the most intellectually honest candidate. It acknowledges the fundamental identification problem, makes its assumptions transparent, and works within (rather than against) the perturbation. However, the caveats are severe: monotonicity is less credible under self-selection, bounds may be too wide to distinguish pressure from willingness, and the interpretation of bounds is muddied by endogenous avoidance choices.

---

## Candidate 2: Route-and-Solicitor Stratified Observational Comparison

### Threat 1 — Selection-on-Observables Is Directly Contradicted by the Packet

The candidate's critical assumption is that "conditional on route, neighborhood, timing window, and solicitor identifiers, a household's pre-contact choice is as-good-as-random with respect to unobserved determinants of giving." The packet explicitly states: "Potential donors may differ in how much they want to engage with the fundraiser, and pre-contact choices may affect who is ultimately exposed to the interaction." This is a direct acknowledgment that unobserved willingness-to-engage drives pre-contact choices. The packet's research background frames the entire problem around separating mechanisms that are *observationally confounded* — if conditioning on observables solved the problem, there would be no research design challenge to solve. The candidate's assumption substitutes for the identification problem rather than solving it.

### Threat 2 — The Available Covariates Cannot Plausibly Absorb Selection Bias

The packet lists the following baseline controls: route, building, neighborhood, area indicators, contact timing, visit window, and solicitor/team identifiers. These are all *supply-side* or *administrative* variables. Conspicuously absent are any *household-level* characteristics: income, wealth, past giving history, relationship with the cause, altruism measures, social pressure sensitivity, household composition, or any demographic variables. The selection process the packet describes — "households can choose whether to receive advance notice or indicate that they prefer not to be approached after learning about the fundraising campaign beforehand" — is fundamentally an individual-level decision driven by individual-level characteristics. Controlling for route and solicitor fixed effects addresses sorting across geographic areas but cannot absorb within-route, within-solicitor selection on individual unobservables. The candidate's assumption effectively requires that no individual-level unobservable affects both pre-contact choice and giving — a claim the packet's own framing refutes.

### Perturbed-Condition Dependency

**Yes, fatally.** This candidate's identification logic would only be credible under random assignment of pre-contact conditions — which is *exactly* what the perturbation removes. The perturbation states: "The pre-contact interaction condition is no longer assigned by the researcher." The candidate attempts to recover identification through conditioning, but the available covariates are insufficient, and the selection mechanism described in the packet makes the conditional independence assumption implausible. The perturbation doesn't merely weaken this design — it makes the critical assumption untenable given the data provided.

### Verdict: `not_defensible`

The critical assumption is both untestable and contradicted by the packet's description of the data-generating process. The candidate substitutes an implausible statistical assumption for a genuine identification strategy.

---

## Candidate 3: Solicitor-Induced Contact Instrumental Variables

### Threat 1 — Exclusion Restriction Violation Flagged by the Packet Itself

The packet warns: "solicitor behavior may change across routes or conditions." This is a direct acknowledgment that solicitor characteristics affect outcomes through channels beyond the contact margin. A persuasive, persistent, or skilled solicitor simultaneously (a) achieves higher contact rates (the first stage) and (b) extracts larger contributions conditional on contact (a direct effect violating exclusion). The candidate acknowledges this ("solicitor skill, persistence, or personal characteristics may directly affect contribution amounts conditional on contact") but offers no resolution. The exclusion restriction is not a minor technical concern — it is the foundational requirement for IV validity, and the packet provides affirmative reasons to doubt it.

### Threat 2 — Non-Random Solicitor Assignment and the Research Question Mismatch

The packet states that "The organization constructs a list or route of planned in-person solicitation opportunities" — this is organizational planning, not random assignment. Organizations routinely assign better solicitors to higher-potential routes. The packet provides zero evidence of random or as-if-random solicitor assignment. Furthermore, even if the IV were miraculously valid, it estimates the LATE of *contact on giving*, not the decomposition of giving into *pressure vs. willingness*. The packet's research objective is specifically to "estimate whether voluntary contributions reflect genuine willingness to support the cause, social pressure from the interaction, or both." The IV tells us whether being contacted causes giving (among compliers) but cannot separate the mechanism — a contacted complier who gives may do so from genuine willingness, social pressure, or any combination. The candidate addresses a different question than the one posed.

### Perturbed-Condition Dependency

**Partially.** The solicitor IV logic doesn't directly depend on random assignment of pre-contact conditions — it operates on a different margin (solicitor → contact → giving). However, the perturbation makes the *overall* research design problem harder: now there are two endogenous margins (pre-contact choice AND contact-giving) instead of one. The IV addresses only the second margin, leaving the perturbation's core challenge (endogenous pre-contact selection) completely unaddressed. Moreover, the exclusion restriction and non-random solicitor assignment were fatal problems *before* the perturbation — the perturbation doesn't create these problems but also doesn't resolve them.

### Verdict: `not_defensible`

Fails the exclusion restriction (flagged by the packet), lacks evidence of random solicitor assignment, and — critically — does not answer the research question of separating pressure from willingness even if it were valid.

---

## Candidate 4: Descriptive Decomposition of Solicitation Patterns

### Threat 1 — Does Not Answer the Research Question

The packet's explicit research objective is to "estimate whether voluntary contributions in an in-person request setting reflect genuine willingness to support the cause, social pressure from the interaction, or both." This candidate explicitly "refrains from causal interpretation of pre-contact-choice-to-giving pathways" and can only "document that the two mechanisms are observationally entangled." The candidate itself acknowledges: "This design cannot answer the core research question of separating social pressure from genuine willingness." As an *identification strategy candidate*, this is not a strategy — it is a concession that identification is impossible.

### Threat 2 — Descriptive Decomposition Conflates Selection and Treatment in Ways That Can Mislead

Decomposing giving rates by pre-contact choice group produces patterns that are uninterpretable for the research question. Suppose the "advance notice" group has higher giving rates. This could reflect: (a) advance notice mobilized genuinely willing donors (willingness mechanism), (b) advance notice increased social pressure salience (pressure mechanism), or (c) households with higher baseline giving propensity selected into receiving advance notice (selection). All three interpretations are consistent with the same observed pattern. The descriptive decomposition cannot distinguish among them, and presenting these patterns without causal interpretation may create an illusion of evidence where none exists.

### Perturbed-Condition Dependency

**No.** This candidate makes no causal claims, so the perturbation doesn't break it. It is equally (un)informative about the pressure/willingness decomposition regardless of whether pre-contact conditions are assigned or self-selected. This is simultaneously its strength (robust) and its fatal limitation (uninformative for the research question).

### Verdict: `not_defensible` (as an identification strategy)

Explicitly labeled as a fallback (`is_fallback: true`) and acknowledged by the candidate as unable to answer the research question. It is the *appropriate fallback* when causal identification is impossible, and the packet's instructions require it — but it is not an identification strategy and should not be evaluated as one.

---

## Overall Assessment

### Perturbed-Condition Dependency

**Detected: Yes.** The perturbation — removing researcher assignment of pre-contact conditions — fundamentally alters the identification landscape:

- **Candidate 2** depends on a condition (as-if-random pre-contact choice conditional on observables) that the perturbation directly contradicts.
- **Candidate 1** is weakened because self-selection into avoidance muddies the interpretation of bounds (avoidance-as-type-revelation vs. avoidance-as-selection).
- **Candidate 3** doesn't directly depend on pre-contact assignment but is independently invalid and doesn't address the perturbation's core challenge.
- **Candidate 4** is unaffected by the perturbation because it makes no causal claims — and is therefore uninformative.

### Recommendation

Candidate 1 (Partial Identification via Contact-Behavior Bounds) is the recommended primary, consistent with the Stage 3 recommendation. It is the only candidate that is intellectually honest about what can be learned under the perturbation, makes its assumptions transparent, and provides a framework (bounds) that can narrow what is knowable even if it cannot point-identify the decomposition. The descriptive fallback (Candidate 4) should be presented alongside it as the honest baseline and as required by the packet when causal identification fails.

