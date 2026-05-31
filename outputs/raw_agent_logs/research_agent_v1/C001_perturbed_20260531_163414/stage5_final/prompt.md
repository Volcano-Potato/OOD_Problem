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

## Stage 4 Critique

## Independent Critique

### Candidate 1: Descriptive Stratification by Pre-Contact Choice × Contact Status

**Threat 1 — Double selection confound.** The four-way stratification (opted-for-notice × contacted status) embeds two layers of endogenous selection. The packet states that "Potential donors may differ in how much they want to engage with the fundraiser, and pre-contact choices may affect who is ultimately exposed to the interaction." Households that seek advance notice are likely more engaged with the cause; among those who did not seek notice, who is contacted depends on availability and absence patterns. Neither dimension is random, so group mean differences conflate engagement propensity, availability, and any causal effects.

**Threat 2 — No basis for decomposition.** The packet's core objective is to "separate these explanations" (genuine willingness vs. social pressure). Descriptive stratification across self-selected groups cannot separate these mechanisms. A contacted household that opted for notice and gives could be acting from willingness, pressure, or both; the design provides no leverage to decompose these components, and the stratification offers no test that would falsify one mechanism over another.

**Condition dependency?** No. This candidate explicitly disclaims causal identification and operates entirely within the perturbation's constraints. It does not depend on researcher assignment of the pre-contact condition because it makes no causal claims requiring such assignment.

**Verdict:** `defensible` — as a descriptive fallback. The packet instructs that if "strong causal identification is no longer justified, the answer must explicitly downgrade the claim," and this candidate does exactly that.

---

### Candidate 2: Instrumental Variables Using Solicitor Identity and Visit Timing

**Threat 1 — Exclusion restriction is implausible and untestable.** The IV requires that solicitor identity and visit timing affect contribution outcomes *only* through contact probability. But the packet warns that "solicitor behavior may change across routes or conditions." Solicitors differ in persuasiveness, persistence, ask amounts, and interpersonal skills — all of which plausibly affect giving *conditional on contact*, violating the exclusion restriction. The packet provides no evidence, protocol, or institutional detail suggesting solicitors follow standardized scripts that would support the restriction.

**Threat 2 — No assignment mechanism for the instrument.** The packet describes Stage 1 as: "The organization constructs a list or route of planned in-person solicitation opportunities." It says nothing about random or quasi-random assignment of solicitors to routes. Organizations facing fundraising goals have strong incentives to assign experienced solicitors to higher-potential areas. The packet provides route/neighborhood/timing controls but no evidence that solicitor assignment is orthogonal to area characteristics — and the burden of establishing quasi-random assignment falls on the researcher, not on the absence of contradictory evidence.

**Additional fragility:** Even if the instrument were valid for contact, it does not address the perturbation's core challenge. The IV estimates the effect of *contact* on giving (among compliers), not the effect of *pre-contact conditions* (advance notice vs. avoidance signal) on giving. The packet asks the design to distinguish pressure from willingness in the context of pre-contact choices; an IV for contact does not decompose these mechanisms under self-selected pre-contact conditions.

**Condition dependency?** Yes, indirectly. The IV strategy depends on the existence of quasi-random variation in solicitor assignment or timing — a condition the packet never establishes but that becomes more fragile precisely because the perturbation removes researcher control over the primary treatment. When the researcher cannot assign the key treatment, relying on an unverified secondary source of variation that the packet does not describe as randomized is not defensible.

**Verdict:** `not_defensible`

---

### Candidate 3: Revealed-Preference Bounding with Avoidance Signals

**Threat 1 — Avoidance signal truthfulness is a strong, untestable behavioral assumption.** The packet states that households "can choose whether to receive advance notice or indicate that they prefer not to be approached after hearing about the fundraising campaign beforehand." The perturbation makes this choice unconstrained and unobserved in its motivation. A household might signal avoidance because it is busy at the scheduled time, because it prefers to donate online through a different channel, or because it has a policy of never answering the door — not because it is susceptible to social pressure. Attributing contributions from contacted avoiders to "pressure" requires that the avoidance signal cleanly reflects pressure sensitivity, which the packet provides no basis to assert.

**Threat 2 — The contacted-avoider subpopulation may be trivially small or non-representative.** The packet notes that "pre-contact choices may affect who is ultimately exposed to the interaction" and that "Some households may be absent, unreachable, or inconsistent between stated preferences and realized contact." If avoidance signals translate into effective avoidance (e.g., households that signal avoidance are not home or refuse to answer), the "contacted avoiders" group shrinks toward zero. Even if some avoiders are contacted, they may be a selected subset (e.g., those who were less determined to avoid, or those the solicitor pursued more aggressively), introducing additional selection bias into the lower bound.

**Threat 3 — Bounds may be uninformatively wide.** The packet provides no information about expected subgroup sizes, variance in contribution behavior, or the strength of the avoidance signal's correlation with giving. Without such information, the bounds could span nearly the entire range of possible contribution probabilities, making them substantively vacuous even if formally valid.

**Condition dependency?** Partially. The bounding strategy does not depend on random assignment, which is a strength given the perturbation. However, it does depend on avoidance signals carrying reliable information about social-pressure sensitivity — a condition the perturbation weakens because the researcher no longer controls how, when, or with what framing the avoidance option is presented. In a researcher-assigned design, the signal could be embedded in a structured instrument; under the perturbation, it is an organic household choice of unknown meaning.

**Verdict:** `defensible_with_caveats` — The logic is coherent and does not require random assignment, but the truthfulness assumption is heroic, the sample-size concern is acute, and the bounds may be uninformative.

---

### Candidate 4: Selection-on-Observables with Route-Neighborhood Fixed Effects

**Threat 1 — Unconfoundedness is explicitly violated by the perturbation.** The perturbation states: "Households can choose whether to receive advance notice or indicate that they prefer not to be approached after learning about the fundraising campaign beforehand." This choice is endogenous to precisely the unobserved characteristics that drive giving outcomes. The packet explicitly flags that "Potential donors may differ in how much they want to engage with the fundraiser." Household-level altruism, income, civic engagement, and social-pressure sensitivity are all unobserved in the data card and all plausibly determine both pre-contact choice and contribution behavior. The selection-on-observables assumption requires these to be irrelevant conditional on geographic and timing controls, which is not credible.

**Threat 2 — Within-neighborhood variation is endogenously determined, not as-good-as-random.** Two adjacent households on the same route segment that make different pre-contact choices are not exchangeable. The household that opts for advance notice has revealed higher baseline engagement with the cause. Even conditional on neighborhood × timing × solicitor fixed effects, the remaining variation in pre-contact choice is driven by individual-level factors that also predict giving. The fixed effects absorb area-level confounds but not the individual-level selection that the perturbation introduces.

**Threat 3 — No household-level balancing covariates exist.** The packet's baseline controls consist entirely of geographic, timing, and solicitor identifiers. It contains no household-level demographics, no prior giving history, no income or wealth proxies, and no measures of cause affinity. Selection-on-observables designs in applied microeconomics typically require rich pre-treatment covariates (e.g., lagged outcomes, detailed demographics) to make unconfoundedness plausible. The packet provides none of these.

**Condition dependency?** Yes, critically. This design depends on the condition that selection into pre-contact status is determined by observables (or that unobservables are orthogonal to pre-contact choice conditional on observables). The perturbation explicitly breaks this condition by making pre-contact choice a household-level behavioral decision driven by unobserved engagement with the cause. The candidate treats the perturbation as a nuisance to be controlled with fixed effects when it is, in fact, the central identification failure.

**Verdict:** `not_defensible`

---

### Summary

The perturbation — removal of researcher assignment of the pre-contact condition — is fatal to causal identification strategies that require exogeneity of treatment assignment (Candidates 2, 4). Candidate 3 partially survives by using the choice itself as information, but depends on untestable behavioral assumptions. Candidate 1 is the only fully defensible design because it honestly aligns with the packet's requirement to "downgrade the claim" when "strong causal identification is no longer justified."

