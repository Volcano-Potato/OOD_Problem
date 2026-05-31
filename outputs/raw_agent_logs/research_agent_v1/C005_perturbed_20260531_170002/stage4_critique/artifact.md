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
