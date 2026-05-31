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

## Stage 4 Critique

## Independent Design Critique

### Candidate 1: Intent-to-Treat (ITT)

**Summary**: Estimates the average causal effect of campaign assignment/eligibility on downstream outcomes, using the Stage-2 randomization as the identifying variation. Does not require opportunity-side logs for untreated users.

**Packet-Grounded Threats**

1. **Estimand–Objective Mismatch (T1.1)**. The packet's stated research objective is to "estimate the causal effect of actual digital ad exposure on downstream user outcomes," and Specific Question 1 explicitly asks how to distinguish assignment effects from exposure effects. The ITT estimand answers a different question — the effect of *being eligible for* the campaign — which may not satisfy the research sponsor's decision-making needs. This is not a validity threat per se but a relevance threat grounded in the packet's own framing.

2. **SUTVA / Interference (T1.2)**. The packet's Data Card explicitly flags: "Users may see ads on other channels, share information, or be affected by market-level campaign saturation." If the campaign is large enough to produce market-level saturation, the control group's outcomes are contaminated, biasing the ITT estimate toward zero even under perfect randomization. The perturbation (no opportunity-side logs for untreated users) removes any ability to measure the degree of cross-group ad exposure or diagnose interference magnitude.

3. **One-Sided Non-Compliance Opacity (T1.3)**. The packet's Data Card states: "Assignment or eligibility does not guarantee actual exposure because the focal ad may not be served." Without opportunity-side logs for untreated users, the researcher cannot characterize the non-compliance mechanism — specifically, cannot observe what fraction of unassigned users would have been eligible for ad opportunities. This limits the external validity discussion: the ITT's generalizability to settings with different take-up rates cannot be assessed.

**Does this candidate depend on a condition the perturbed packet has broken, weakened, or made ambiguous?**

No. The ITT design does not use opportunity-side logs for untreated users in any step of its identification. The randomization structure (Stage 2) is intact, assignment status is observed, and outcomes are observed. The perturbation leaves ITT identification essentially unchanged. The perturbation does, however, remove auxiliary diagnostics (e.g., characterizing non-compliance, measuring interference) that would strengthen the ITT's interpretability — but these are supplementary, not essential to internal validity.

**Verdict**: `defensible`

---

### Candidate 2: Instrumental Variables LATE via Random Assignment

**Summary**: Uses random/holdout assignment as an instrument Z for actual ad exposure D, identifying the LATE for compliers. The first-stage (assignment → exposure) and reduced-form (assignment → outcomes) are both estimable from observed logs. The IV ratio (reduced-form / first-stage) is computable without opportunity-side logs.

**Packet-Grounded Threats**

1. **Exclusion Restriction is Fundamentally Untestable (T2.1)**. The perturbation removes "logs that identify which untreated users had the same opportunity to receive the focal ad." This eliminates the only data that could provide diagnostic evidence for the exclusion restriction. Without opportunity-side logs, the researcher cannot test whether assignment status alters platform behavior toward users through channels *other than* the focal ad — for instance, the platform might change bid shading, ad load, or auction participation rules for assigned vs. unassigned users in ways that affect downstream outcomes independently of focal-ad exposure. The exclusion restriction becomes a pure article of faith rather than a defended assumption. The packet itself warns: "Stage 3: Conditional on eligibility, the platform determines whether the focal ad is actually served at each opportunity" — the platform's optimization could respond differently to assigned vs. unassigned users' auction eligibility in ways that violate the exclusion restriction, and the perturbation makes this response unobservable.

2. **Complier Population is Uncharacterizable (T2.2)**. The LATE applies only to compliers — users who would receive an impression if and only if assigned. Without opportunity-side logs, the researcher cannot observe which unassigned users *would have* been eligible for ad opportunities, making it impossible to estimate the complier share, describe complier characteristics, or assess whether compliers differ systematically from always-takers and never-takers. The packet's Specific Question 2 asks: "What comparison group would make exposed users comparable to an untreated counterfactual if opportunity-side control logs are unavailable?" — this question itself signals that the lack of opportunity-side logs makes standard complier characterization impossible.

3. **Monotonicity Cannot Be Verified (T2.3)**. The packet describes a platform using "auctions, targeting rules, pacing, and optimization." If assignment status changes how the platform's delivery system treats a user (e.g., assigned users face different auction competition or pacing rules), some users might receive *fewer* impressions when assigned than when unassigned — a defier pattern. Without opportunity-side data for both groups, monotonicity violations are undetectable. This is a direct consequence of the perturbation: detecting defiers requires observing ad-opportunity eligibility for both assigned and unassigned users.

4. **Weak Instrument Risk (T2.4)**. The packet's Data Card states that "Assignment or eligibility does not guarantee actual exposure because the focal ad may not be served." Combined with the platform's endogenous delivery optimization, the first-stage F-statistic could be low, producing wide confidence intervals and hypersensitivity to small violations of the exclusion restriction. Without opportunity-side logs, the researcher cannot diagnose *why* the first stage is weak (e.g., whether the platform systematically under-delivers to certain user segments among the assigned), limiting the ability to improve the instrument.

**Does this candidate depend on a condition the perturbed packet has broken, weakened, or made ambiguous?**

Yes, critically. The IV/LATE design does not *require* opportunity-side logs for point estimation (the IV ratio is algebraically computable), but it *does* require them for defending the exclusion restriction, characterizing compliers, verifying monotonicity, and diagnosing weak-instrument mechanisms. The perturbation removes all four of these supporting pillars. The design transitions from a defensible IV to an IV that is computationally feasible but epistemically hollow — the estimator produces a number whose interpretation and credibility are severely compromised.

**Verdict**: `defensible_with_caveats`

*Rationale for caveat rather than "not_defensible":* The first stage and reduced form are both identified from observed data alone. The IV ratio is computable. In some research traditions, a LATE estimate with acknowledged but untestable exclusion restriction is still considered informative, provided the caveats are prominently disclosed. The IV can be reported alongside the ITT as a supplementary estimate with strong qualification. However, if the standard for "defensible" is that the key identifying assumption must be *supportable* rather than merely *assertable*, this candidate is `not_defensible`.

---

### Candidate 3: Selection-on-Observables Descriptive Regression

**Summary**: Conditions actual ad exposure on pre-campaign user activity, device, channel, segment, and time-of-opportunity indicators, then estimates the residual association between exposure and outcomes. The candidate itself is labeled as a fallback.

**Packet-Grounded Threats**

1. **Selection on Unobservables by Construction (T3.1)**. The packet's Research Background explicitly states: "platform delivery systems use auctions, targeting rules, pacing, and optimization." These platform-internal mechanisms select users for ad exposure based on variables — predicted click-through rate, user value scores, bid landscapes, pacing states — that are deliberately correlated with the researcher's outcome (conversions, purchases). These selection variables are not in the researcher's covariate set ("pre-campaign user activity, device, channel, segment, and time-of-opportunity indicators"). The unconfoundedness assumption fails not because of an empirical accident but because of the institutional design of the ad-delivery system: the platform *optimizes for outcomes correlated with the researcher's outcome*.

2. **Perturbation Amplifies the Problem (T3.2)**. Without opportunity-side logs for untreated users, even partial modeling of the selection process is impossible. A Heckman-style selection correction requires observing the selection equation's outcome (at-risk status) for both treated and untreated units. The perturbation removes this possibility entirely. The researcher cannot estimate a propensity score for ad-exposure opportunity, cannot implement inverse-probability weighting that accounts for opportunity-level selection, and cannot bound selection effects using the untreated population's opportunity distribution — because that distribution is unobserved.

3. **Omitted Variable: Platform Optimization State (T3.3)**. The packet's Stage 3 notes: "Conditional on eligibility, the platform determines whether the focal ad is actually served at each opportunity." The platform's decision is a function of real-time auction conditions, budget pacing, and competitive dynamics — all of which are absent from the researcher's covariate set and likely correlated with time-varying conversion propensity. No amount of pre-campaign user-level controls can capture within-campaign, opportunity-level optimization.

**Does this candidate depend on a condition the perturbed packet has broken, weakened, or made ambiguous?**

The perturbation compounds an already-fatal problem. Even *with* opportunity-side logs, unconfoundedness would be implausible given the platform's endogenous optimization. The perturbation removes any residual possibility of selection modeling or bounding. The candidate was already `not_defensible`; the perturbation makes it doubly so.

**Verdict**: `not_defensible`

---

### Candidate 4: Within-User Pre-Post Exposure Trajectory Comparison

**Summary**: Compares each user's outcome trajectory after first focal-ad impression to their own pre-exposure baseline. Uses only exposed users; each user serves as their own counterfactual.

**Packet-Grounded Threats**

1. **No Untreated Comparison Group Experiencing the Same Calendar Time (T4.1)**. The perturbation is directly fatal here. A credible pre-post design requires either (a) an untreated control group observed over the same calendar period to net out common time trends, or (b) a design-based argument that no time-varying confounders exist. The perturbation removes (a) because we cannot identify untreated users who had ad opportunities during the campaign window. And the packet's setting makes (b) implausible: a "short campaign window plus a post-exposure outcome window" does not rule out concurrent promotions, seasonal effects, or other platform-level changes coinciding with the campaign period.

2. **Endogenous Timing of First Exposure (T4.2)**. The packet states the platform "controls which users actually receive impressions" through "auctions, targeting rules, pacing, and optimization." Users receive their first impression when the platform's optimization determines they are high-value targets — which is precisely when their conversion propensity is rising. The pre-exposure trajectory cannot serve as a valid counterfactual because the timing of the "treatment" (first impression) is itself a function of the outcome process. This is a classic Ashenfelter's dip / regression-to-the-mean problem.

3. **Regression to the Mean (T4.3)**. Users selected for ad delivery by the platform's optimization are likely those with elevated pre-campaign activity or favorable recent trajectories. Their outcomes would naturally revert toward the mean in the post period regardless of ad exposure. The pre-post difference conflates the ad effect with mean reversion, and the perturbation removes any ability to estimate the degree of mean reversion from an untreated comparison group.

4. **Single-Group Design Cannot Separate Causal Mechanisms (T4.4)**. Even if an outcome change is observed, it is impossible to attribute the change to ad exposure vs. contemporaneous platform changes, market conditions, or user lifecycle effects. The packet's Specific Question 2 asks about constructing comparison groups precisely because single-group designs lack a credible counterfactual, and the perturbation removes the data needed to construct any comparison.

**Does this candidate depend on a condition the perturbed packet has broken, weakened, or made ambiguous?**

Yes, fatally. A pre-post comparison can be upgraded to a difference-in-differences design only if untreated users with ad-opportunity eligibility can be observed over the same calendar period. The perturbation explicitly removes those logs. Without them, this design collapses to a single-group before-after comparison — which is not a causal identification strategy. The perturbation transforms an already-weak design (endogenous timing) into one with no credible counterfactual at all.

**Verdict**: `not_defensible`

---

## Overall Assessment

The perturbation — no opportunity-side logs for untreated users — selectively damages the candidates:

- **ITT**: Unaffected. Randomization + assignment + outcomes are all observed. The perturbation removes auxiliary diagnostics but leaves core identification intact.
- **IV/LATE**: Severely weakened. Point estimation remains possible, but the exclusion restriction, monotonicity, and complier characterization become untestable. The design is computationally feasible but its credibility is substantially degraded.
- **Selection-on-Observables**: Already indefensible (endogenous platform optimization); the perturbation removes residual selection-modeling possibilities.
- **Pre-Post**: Fatal. The perturbation removes the data needed to construct any untreated comparison group, collapsing a potential DiD into a single-group time-series.

**Recommendation**: The ITT is the only cleanly defensible design. The IV/LATE should be reported as a supplementary estimate with prominent disclosure that the exclusion restriction and monotonicity cannot be tested due to missing opportunity-side logs. The Stage 3 recommendation of ITT as primary is correct.

