# Raw Agent Run Log

- `run_id`: RUN_20260527_210840_01_openclaw_deepseekv4pro_isolated
- `case_id`: C001
- `variant_id`: level2
- `level`: level2
- `agent_name`: openclaw
- `agent_id`: benchmark_isolated
- `model`: deepseek-v4-pro
- `model_provider`: deepseek
- `openclaw_build_or_version`: 2026.5.5
- `channel`: cli
- `temperature`: not_supported
- `top_p`: not_supported
- `max_tokens`: not_supported
- `seed`: not_supported
- `tools_enabled`: locally_isolated_remote_tool_enabled
- `closed_book`: false
- `timestamp`: 2026-05-27T21:08:40+0800
- `input_file`: benchmark/cases/C001_charitable_giving/agent_task_level2.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: Separating Social Pressure from Genuine Willingness in In-Person Fundraising

---

## 1. Executive Summary

This design proposes a multi-arm field experiment that varies two dimensions of the solicitation process prior to an in-person fundraising visit: (1) whether potential donors receive advance notice of the upcoming visit, and (2) whether they are given a low-cost opportunity to opt out of the face-to-face interaction. By crossing these features, the design creates conditions that differ in the degree of social pressure at the moment of contact while holding constant the information available to potential donors. Comparing contact rates, giving rates conditional on contact, and contribution-size distributions across arms allows separation of avoidance-driven selection from pressure-driven conditional giving. The design can credibly identify causal effects of solicitation-process features on contact and giving outcomes. However, distinguishing *why* pressure-sensitive giving occurs — whether from pure discomfort, reciprocity norms, or information revelation — requires additional interpretive structure that goes beyond the experimental contrast alone. I provide a suite of ancillary predictions and heterogeneity tests that can narrow the set of plausible mechanisms, and I explicitly flag what cannot be claimed from the available evidence.

---

## 2. Research Question

Do voluntary contributions in an in-person fundraising request reflect genuine willingness to support the cause, social pressure arising from the face-to-face interaction, or both — and under what conditions can these mechanisms be empirically separated?

---

## 3. Target Estimand (or Strongest Defensible Estimand)

The primary target estimands are:

**a. Average causal effect of advance notice on contact probability.**
The difference in the probability that a potential donor is reached and engages with the fundraiser between those who receive advance notice (and any associated interaction-cost manipulation) and those who do not. This captures avoidance-based selection.

**b. Average causal effect of solicitation-process features on giving conditional on contact.**
Among those who are contacted, the difference in the probability and amount of giving across process conditions. This captures differential sorting into the contacted pool *and* any direct effect of the process on giving behavior.

**c. Composition-adjusted giving effect.**
The contribution rate and amount among those who would be contacted regardless of condition (the "always-contacted" stratum), identified under assumptions detailed below. This isolates the pressure component of conditional giving from the selection component.

If the data cannot support principal-stratum identification (due to weak instruments or monotonicity violations), the strongest defensible estimands are the intention-to-treat (ITT) effects on contact and giving, supplemented by bounding exercises on the conditional giving effect among always-contacted units.

---

## 4. Treatment or Exposure and Main Outcomes

### Treatment/Exposure Variables

The design crosses two binary features, yielding up to four solicitation-process conditions:

| Arm | Advance Notice | Opt-Out Channel | Interpretation |
|-----|---------------|-----------------|----------------|
| A (Control) | No | No | Standard unannounced visit; maximum surprise element; contact depends only on being home |
| B | Yes | No | Notice given but no easy opt-out; potential donors know about the visit but cannot cheaply avoid it |
| C | Yes | Yes | Notice given with a low-cost way to decline the in-person interaction (e.g., check a box, return a note, send a text) |
| D | No | Yes | Logically degenerate: an opt-out channel without advance notice is operationally almost indistinguishable from Arm A, because potential donors would not know to use it. If implemented, it serves primarily as a procedural check |

**The minimal design** that addresses the research question requires at least three arms: A (control), B (notice only), and C (notice + opt-out). The opt-out channel must impose minimal time or cognitive cost — its purpose is to reveal avoidance preference, not to screen based on transaction costs.

The researcher controls assignment at the household or contact-opportunity level. Assignment can be blocked by route, neighborhood, or timing window to improve balance.

### Main Outcomes

| Outcome | Definition | Level |
|---------|-----------|-------|
| Contact occurred | Binary: fundraiser reached and engaged the potential donor (door answered, conversation initiated) | Household/opportunity |
| Contribution made | Binary: any positive donation | Household/opportunity |
| Contribution amount | Continuous (or discrete positive) amount given | Household/opportunity, conditional on contact |
| Contribution size category | Ordinal bins (e.g., zero, small, medium, large) | Household/opportunity |

### Secondary Outcomes

- **Avoidance behavior**: Any observable proxy for active avoidance (e.g., opt-out rate in Arm C, not-at-home rate patterns across arms, door-not-opened rate)
- **Engagement duration**: If measurable, time spent interacting with the fundraiser
- **Small vs. large contributions**: Partitioning the contribution distribution to test whether marginal giving is differentially sensitive to condition

---

## 5. Data Structure Summary

The data have a two-stage decision structure with partial observability, matching the process described in the packet:

**Stage 1 (Assignment):** Each planned contact opportunity *i* is assigned to a solicitation-process condition *Tᵢ* ∈ {A, B, C, D}. Assignment is randomized within blocks (route × timing window). Pre-treatment covariates *Xᵢ* (neighborhood indicators, timing, housing characteristics if available) are recorded.

**Stage 2 (Contact):** The fundraiser attempts the visit. Contact occurs (*Cᵢ* = 1) if the potential donor is present, available, and does not actively avoid the interaction. Contact is zero (*Cᵢ* = 0) if the donor is absent, avoids, or otherwise cannot be reached. In Arm C, *Cᵢ* = 0 may also reflect active opt-out before the visit.

**Stage 3 (Giving, conditional on contact):** If *Cᵢ* = 1, the potential donor decides whether to give (*Gᵢ* ∈ {0, 1}) and how much (*Yᵢ* ≥ 0). Both *Gᵢ* and *Yᵢ* are unobserved when *Cᵢ* = 0.

**Stage 4 (Supplementary):** Route, timing, solicitor identifiers; possibly post-interaction surveys or neighborhood-level characteristics.

The unit of observation is the planned contact opportunity. The data have the following structure:

```
Row i: (i, block, T_i, X_i, C_i, G_i, Y_i)
```

with *Gᵢ* and *Yᵢ* missing when *Cᵢ* = 0.

---

## 6. Relevant Causal Mechanisms

The packet specifies four mechanisms that the design must distinguish:

### Mechanism 1: Genuine willingness
Potential donors actively want to engage and contribute. Their giving reflects true altruism, warm glow, or support for the cause. These donors would give even if the interaction were costless to avoid, and they might even seek out the fundraiser. Predicted pattern: high contact rates across all arms; giving persists even when avoidance is easy.

### Mechanism 2: Social pressure / avoidance cost
Some potential donors prefer to avoid the interaction and give only when avoidance is difficult or costly. Their giving is not a revealed preference for supporting the cause but rather a response to the discomfort of saying no in person. Predicted pattern: contact rates fall when opt-out is offered (Arm C), and among those who remain contacted, giving rates may differ from those in pressure-only conditions (Arm B) because the contacted pool is now selected on lower pressure sensitivity.

### Mechanism 3: Scheduling or awareness effects
Advance notice may change who is home, when they are home, or whether they are mentally prepared to engage — even if it does not change the social pressure of the interaction itself. Predicted pattern: contact rates differ between Arms A and B (notice changes availability), but giving conditional on contact is similar between A and B *if* the selection into contact is similar. If notice changes *who* is contacted, the composition of the contacted pool shifts, producing apparent differences in conditional giving that are selection effects rather than behavioral responses to pressure.

### Mechanism 4: Marginal-giving sensitivity
Small contributions may be especially responsive to pressure because they are the cheapest way to relieve discomfort without committing substantial resources. This interpretation requires evidence that the share of small gifts (or the lower tail of the contribution distribution) shifts differentially with pressure conditions, compared to large gifts. However, without a design that independently varies the cost of giving, this interpretation is associational rather than causal.

---

## 7. Main Identification Challenge

The central identification challenge is **partial observability with endogenous selection**. Giving outcomes *Gᵢ* and *Yᵢ* are observed only when contact occurs (*Cᵢ* = 1). The treatment *Tᵢ* can affect both the probability of contact and the composition of the contacted pool. As a result:

- Differences in unconditional giving rates (E[*G* | *T* = t]) confound treatment effects on contact (extensive margin) with treatment effects on giving conditional on contact (intensive margin).
- Differences in conditional giving (E[*G* | *C* = 1, *T* = t]) confound compositional changes in who is contacted with behavioral responses to the treatment among contacted units.

Without further structure, one cannot distinguish whether Arm B produces higher conditional giving than Arm C because (a) pressure induces more giving among comparable people, or (b) people who are pressure-sensitive avoid Arm C, leaving only intrinsically motivated givers in the Arm-C contacted pool — a selection effect that yields the same observed pattern.

A secondary challenge is that the opt-out mechanism in Arm C may itself signal something about the fundraiser or the cause (e.g., "this organization respects your time"), which could change giving behavior among those who choose not to opt out. This confounds the pure pressure interpretation of Arm C and must be addressed through design or supplementary measurement.

---

## 8. Whether Credible Causal Identification Is Possible

**Yes, for ITT effects on contact and unconditional giving.** Because the researcher controls assignment to solicitation-process conditions and randomization is feasible at the household level (within blocks), causal identification of the reduced-form effects of each process condition on contact probability and on unconditional giving probability/amount is credible under standard experimental assumptions (random assignment, SUTVA, no differential attrition from the sample frame).

**Partially, for the decomposition into selection and pressure.** The decomposition into avoidance-based selection and pressure-driven conditional giving requires additional assumptions beyond randomization. Under a monotonicity assumption (advance notice with opt-out does not *increase* contact probability for any unit relative to advance notice without opt-out), one can bound the average giving effect among always-contacted units using principal-stratum methods (Lee bounds, or Imbens-Angrist-style LATE logic if the opt-out is treated as an instrument for contact). However, the credibly identified parameter is the effect for a specific subpopulation (compliers/always-contacted), not the ATE on conditional giving for the full population.

**No, for cleanly separating all four mechanisms simultaneously.** The design can generate evidence consistent or inconsistent with each mechanism, but it cannot produce a single contrast that isolates, say, pure social pressure independently of awareness effects, or pure genuine willingness independently of selection. Multiple mechanisms can produce observationally equivalent patterns. The design provides necessary conditions for each mechanism, not sufficient ones.

---

## 9. Proposed Empirical Design

### Design Architecture

Randomly assign each planned contact opportunity *i* to one of three conditions:

- **Arm A (Baseline/No Notice):** Fundraiser visits without prior communication. This is the standard unannounced door-to-door solicitation.
- **Arm B (Notice Only):** One to three days before the planned visit, the household receives advance notice (e.g., a flyer, postcard, or door hanger) indicating that a fundraiser will visit during a specified time window. No explicit opt-out mechanism is provided.
- **Arm C (Notice + Opt-Out):** Same advance notice as Arm B, but the notice includes a low-cost way to decline the in-person visit. The opt-out could be: check a box and leave the notice on the door, send a brief text message to a designated number, or check a box on a simple web form. Critically, the opt-out does not preclude donating through an alternative channel (e.g., the notice could include a link or QR code for online giving), but the design's primary comparison focuses on the in-person interaction.

### Assignment Procedure

1. **Blocking:** Block on route and visit-timing window (e.g., weekday evening vs. weekend afternoon) to ensure that solicitor quality, neighborhood characteristics, and time-of-day effects are balanced across arms.
2. **Randomization:** Within each block, randomly assign households to arms. If spillover concerns are severe (neighbors communicating), consider cluster-randomizing at the street segment or building level.
3. **Solicitor blinding (if feasible):** The fundraiser should ideally not know the assigned condition before the interaction, to prevent changes in solicitor effort or demeanor. If advance notice makes blinding impossible (the notice is visible at the door), record solicitor awareness and test for solicitor-level effects.

### Key Comparisons

| Comparison | What It Estimates | Mechanism Tested |
|------------|-------------------|------------------|
| *C* in Arm A vs. Arm B | Effect of advance notice on contact probability, holding pressure roughly constant | Scheduling/awareness (M3) |
| *C* in Arm B vs. Arm C | Effect of adding a low-cost opt-out on contact probability, holding information constant | Avoidance/pressure (M2) |
| E[*G* \| *C*=1] in Arm A vs. Arm B | Change in conditional giving from notice, net of any selection change | Joint test of M1, M2, M3 |
| E[*G* \| *C*=1] in Arm B vs. Arm C | Change in conditional giving from opt-out availability, net of selection | Joint test of M1, M2, M4 |
| Contribution-size distribution in Arm B vs. Arm C | Whether small gifts respond differentially | Marginal-giving sensitivity (M4) |
| Unconditional E[*G*] across all arms | Total effect of process on giving (contact × conditional giving) | Overall welfare/policy effect |

### Analytical Strategy

**Step 1: Estimate ITT effects on contact and unconditional giving.**

Run reduced-form regressions of *Cᵢ* and *Gᵢ* on treatment indicators, with block fixed effects. This establishes the causal effect of each process condition on the two observable margins separately.

**Step 2: Decompose the unconditional giving effect.**

The unconditional giving probability can be written as:

P(*Gᵢ* = 1 | *Tᵢ* = t) = P(*Cᵢ* = 1 | *Tᵢ* = t) × P(*Gᵢ* = 1 | *Cᵢ* = 1, *Tᵢ* = t)

Differences across arms in the unconditional rate are the sum of a contact-margin effect (first term) and a conditional-giving effect (second term). By estimating both components, one can attribute how much of any total effect runs through each channel.

**Step 3: Bound the conditional giving effect net of selection.**

Apply Lee (2009) bounds to the difference in conditional giving between Arm B and Arm C. The trimming procedure uses the differential contact rate to bound how much of any difference in E[*G* | *C* = 1] can be attributed to selection (the unobserved givers in the non-contacted pool) rather than to a behavioral effect of pressure.

Specifically, if Arm B has contact rate *pB* and Arm C has contact rate *pC* < *pB*, then the difference in conditional giving between the two arms for the always-contacted subpopulation is bounded between:

- Lower bound: E[*G* | *C* = 1, T = B] among the *pC*/*pB* fraction with the *lowest* giving in Arm B, minus E[*G* | *C* = 1, T = C]
- Upper bound: E[*G* | *C* = 1, T = B] among the *pC*/*pB* fraction with the *highest* giving in Arm B, minus E[*G* | *C* = 1, T = C]

If the bounds exclude zero, there is evidence of a pressure effect on giving net of selection. If they include zero, the observed difference in conditional giving could be entirely compositional.

**Step 4: Test ancillary predictions for mechanism discrimination.**

These are not dispositive individually but collectively narrow the set of plausible mechanisms:

- If M1 (genuine willingness) dominates: contact rates should be similar across Arms B and C (few people opt out), and conditional giving rates should be similar to Arm A.
- If M2 (social pressure) dominates: contact rates should be substantially lower in Arm C than Arm B, and conditional giving in Arm C should be *lower* (because pressure-sensitive givers are gone) or *higher* (because the remaining pool is more intrinsically motivated) — the sign is ambiguous, but a *difference* in conditional giving between B and C is evidence of selection on giving propensity.
- If M3 (scheduling) dominates: contact rates differ between A and B, but conditional giving rates are similar between A and B once the composition of the contacted pool is accounted for.
- If M4 (marginal-giving sensitivity) holds: the share of contributions in the smallest positive category should fall more sharply from Arm B to Arm C than the share in larger categories, because pressure-motivated marginal gifts disappear when avoidance is possible.

---

## 10. Why the Design Is Valid (or Why Causal Identification Is Not Credible)

### What Is Causal

Random assignment of solicitation-process conditions supports **causal interpretation of the ITT contrasts**:

- Arm B vs. Arm A → causal effect of advance notice on contact and unconditional giving.
- Arm C vs. Arm B → causal effect of adding a low-cost opt-out (given notice) on contact and unconditional giving.
- Arm C vs. Arm A → causal effect of the combined intervention (notice + opt-out) relative to the standard approach.

These are identified under:
1. **Random assignment**: Treatment is independent of potential outcomes.
2. **SUTVA** (Stable Unit Treatment Value Assumption): One household's treatment does not affect another's outcomes.
3. **No differential sample attrition**: Missing outcomes (e.g., unrecorded visits) are unrelated to treatment assignment.

### What Is Interpretive, Not Causal

The decomposition of ITT effects into selection and behavioral components requires untestable assumptions:

- **Monotonicity** for Lee bounds: The opt-out does not increase contact probability for any unit. This is plausible (offering an opt-out should not make people *more* likely to answer the door), but it is not testable at the individual level.
- **The opt-out reveals avoidance preference, not something else**: If potential donors interpret the opt-out offer as a signal of fundraiser quality, organization trustworthiness, or social norms, then Arm C differs from Arm B on more dimensions than just the cost of avoidance. The causal contrast is then the effect of "notice + opt-out as a bundle" rather than "reduced interaction cost."
- **Contact is a single decision**: In reality, the "contact" outcome combines (a) being home, (b) answering the door, and (c) engaging with the fundraiser. The opt-out affects (b) and (c) directly, but (a) may be affected by notice through scheduling changes. These cannot be separately identified without additional data on home presence.

---

## 11. Required Assumptions

### Design Assumptions

| # | Assumption | Justification/Testability |
|---|-----------|--------------------------|
| A1 | Random assignment is successfully implemented and balanced | Testable via balance checks on pre-treatment covariates (neighborhood indicators, housing characteristics if available, timing) |
| A2 | SUTVA: no interference between units | Partially testable by examining spatial correlation in outcomes; can be relaxed by cluster-randomizing at street/building level |
| A3 | No Hawthorne effects: the act of receiving notice does not itself change behavior beyond the mechanisms of interest | Untestable; mitigated by making notice as naturalistic as possible |
| A4 | The opt-out mechanism imposes negligible transaction costs | Can be assessed by examining the opt-out rate; if very low, the mechanism may not be functioning as intended (or avoidance preference is genuinely low) |
| A5 | Solicitor behavior does not vary systematically with treatment assignment | Testable by including solicitor fixed effects and testing for solicitor × treatment interactions |

### Identification Assumptions for Bounding

| # | Assumption | Justification/Testability |
|---|-----------|--------------------------|
| A6 | Monotonicity: Arm C contact probability ≤ Arm B contact probability for all units | Plausible given that adding an opt-out cannot force someone to answer the door; untestable at individual level |
| A7 | The opt-out does not directly affect giving outcomes except through contact | This is the exclusion restriction for an IV interpretation; partially testable if some units in Arm C opt out but are still contacted (e.g., the opt-out was not processed in time) |
| A8 | The distribution of potential giving outcomes among always-contacted units is the same shape as the trimmed distribution in the higher-contact arm (for Lee bounds) | Untestable; this is why bounds are computed under worst-case selection |

---

## 12. Statistical Model or Analysis Equation

### Primary Specification: ITT on Contact

Let *Tᵢᴮ* and *Tᵢᶜ* be indicators for assignment to Arm B and Arm C, respectively (Arm A is the omitted category). Let *W_b* be block fixed effects.

**Contact equation (linear probability model):**

*Cᵢ* = α + β₁*Tᵢᴮ* + β₂*Tᵢᶜ* + *W_b*′γ + εᵢ

- β₁: causal effect of notice (without opt-out) on contact probability, relative to no notice
- β₂: causal effect of notice + opt-out on contact probability, relative to no notice
- β₂ − β₁: causal effect of adding the opt-out (given notice) on contact probability

### Primary Specification: ITT on Unconditional Giving

*Gᵢ* = α + δ₁*Tᵢᴮ* + δ₂*Tᵢᶜ* + *W_b*′γ + νᵢ

- δ₁, δ₂: total causal effects on giving (combining contact and conditional giving channels)

For contribution amount *Yᵢ*, use the same specification with *Yᵢ* (set to zero when *Gᵢ* = 0):

*Yᵢ* = α + θ₁*Tᵢᴮ* + θ₂*Tᵢᶜ* + *W_b*′γ + ηᵢ

Standard errors clustered at the route or building level (the level at which treatment may be operationally grouped or at which spatial correlation is plausible).

### Secondary Specification: Conditional Giving

Among contacted units (*Cᵢ* = 1):

*Gᵢ* = α + λ₁*Tᵢᴮ* + λ₂*Tᵢᶜ* + *W_b*′γ + ξᵢ

- λ₁, λ₂ are **not** causal effects because the contacted sample is endogenously selected. They are descriptive associations that, combined with the contact regression and Lee bounds, support the decomposition.

### Decomposition

The total giving effect δ₁ can be decomposed as:

δ₁ = (P(*C* = 1 | B) − P(*C* = 1 | A)) × E[*G* | *C* = 1, A]  
&nbsp;&nbsp;&nbsp;&nbsp;+ P(*C* = 1 | B) × (E[*G* | *C* = 1, B] − E[*G* | *C* = 1, A])  
&nbsp;&nbsp;&nbsp;&nbsp;+ interaction term

where the first term captures the contact-margin effect (how many more/ fewer people are reached), and the second term captures the composition-plus-behavior change in conditional giving. This is an accounting identity, not a causal decomposition, but it reveals which margin dominates.

### Lee Bounds for Pressure Effect Net of Selection

For the comparison between Arms B and C, with contact rates *pB* and *pC* (*pB* > *pC* under monotonicity):

Let *q* = *pC* / *pB* be the fraction of Arm B contactors who would also be contacted in Arm C (the always-contacted).

Trim the lower *q* quantile of the Arm B giving distribution and compute mean giving. This gives the lower bound for E[*G*(C) | always-contacted, T = B], where *G*(C) is the potential giving outcome under Arm C.

Similarly, trim the upper (1 − *q*) quantile for the upper bound.

The trimmed mean in Arm B minus the mean in Arm C is bounded:

*LB* ≤ E[*G*(C) − *G*(B) | always-contacted] ≤ *UB*

If 0 ∉ [*LB*, *UB*], there is evidence of a treatment effect on giving net of selection.

### Contribution-Size Specification

Define *Sᵢ* ∈ {0, small, large} as the contribution category. Estimate a multinomial logit or ordered logit of *Sᵢ* on treatment indicators (for unconditional comparison) and test whether the treatment effect is concentrated in the small-contribution category:

P(*Sᵢ* = small | *Tᵢ*) / P(*Sᵢ* = 0 | *Tᵢ*) modeling with treatment × category interactions.

---

## 13. Robustness, Placebo, Falsification Checks, and Diagnostic Tests

### Balance and Randomization Checks

| Check | Procedure |
|-------|-----------|
| Covariate balance | Regress each pre-treatment covariate on treatment indicators; F-test for joint significance; report normalized differences |
| Timing balance | Verify that visit timing (hour of day, day of week) is balanced across arms |
| Route/neighborhood balance | Check that the spatial distribution of assignments is not clustered in ways that correlate with neighborhood characteristics |

### Placebo and Falsification Tests

| Test | Rationale |
|------|-----------|
| Pre-treatment donor history (if available) | If prior giving records exist, test whether prior giving predicts treatment assignment (it should not). If it does, re-randomization inference may be needed |
| Non-contact outcomes as placebo | If any outcomes are available for units not contacted (e.g., whether the notice was visible at the door, whether opt-out forms were left), test whether these show treatment effects consistent with the mechanism |
| Arm D as procedural check | If implemented, Arm D (opt-out without notice) should produce outcomes indistinguishable from Arm A. Any difference indicates that the opt-out mechanism itself — rather than the interaction of notice + opt-out — is driving results |

### Robustness Checks

| Check | Procedure |
|-------|-----------|
| Alternative clustering | Re-estimate standard errors clustering at route, building, solicitor, and household levels; report the most conservative |
| Solicitor fixed effects | Include solicitor indicators to absorb any solicitor-level heterogeneity in effort or effectiveness |
| Remove outlier contribution amounts | Winsorize the top 1% of contribution amounts and re-estimate |
| Alternative bounding methods | In addition to Lee bounds, compute Horowitz-Manski bounds (which require no monotonicity assumption but are wider) as a robustness check |
| Differential timing within windows | If visits occur across multiple days, include day fixed effects to absorb any temporal trends |
| Balance of opt-out timing | In Arm C, check whether opt-out timing (early vs. late) predicts contribution behavior among those who do not opt out |

### Diagnostic Tests for Mechanism Interpretation

| Test | What It Diagnoses |
|------|-------------------|
| Opt-out rate in Arm C | If near zero, the mechanism may not bind (avoidance cost is trivially low or avoidance preference is absent). If very high, the pressure interpretation gains credibility |
| Contact-rate gradient: A vs. B vs. C | If A ≈ B but B > C, pressure/avoidance (M2) is the primary channel. If A < B and B ≈ C, scheduling/awareness (M3) dominates |
| Contribution-size shift test | Test whether the small-gift share changes differentially between B and C compared to the large-gift share. A differential decline in small gifts supports M4 |
| Solicitor heterogeneity | If the treatment effect varies by solicitor (e.g., more persuasive solicitors show larger pressure effects), this suggests the interaction dynamic matters, consistent with M2 |
| Neighborhood heterogeneity | If the opt-out rate varies by neighborhood characteristics (e.g., socioeconomic status), this may reveal heterogeneity in pressure sensitivity |

---

## 14. Heterogeneity Analysis (If Supportable)

Heterogeneity analysis is supportable to the extent that pre-treatment covariates are available and the sample size is sufficient. Key dimensions:

### Covariate-Based Heterogeneity

| Dimension | Rationale | Specification |
|-----------|-----------|---------------|
| Neighborhood/route indicators | Different areas may have different baseline giving propensities or social norms around door-to-door solicitation | Interact treatment indicators with neighborhood dummies |
| Timing window (weekday evening vs. weekend) | Being home at different times may correlate with employment, family structure, and availability to engage | Interact treatment with timing-window indicators |
| Housing characteristics (if available) | Single-family homes vs. apartments may differ in both contact probability and social pressure dynamics | Interact treatment with housing-type indicators |
| Baseline donor status (if prior records exist) | Prior donors may respond differently than new prospects | Include prior-donor indicator × treatment interactions |

### Design-Relevant Heterogeneity

| Analysis | What It Reveals |
|----------|-----------------|
| Quantile treatment effects on contribution amount | Whether the treatment shifts the entire distribution or only specific parts (e.g., the lower tail → M4) |
| Heterogeneity by solicitor | Whether some solicitors generate more pressure-driven giving than others |
| Spatial spillover tests | Whether households in Arm A that are adjacent to Arm C households show different behavior (suggesting information sharing) |

### Caution

All heterogeneity analyses are secondary and should be treated as exploratory. The design is powered for main effects, not for interactions. Multiple-hypothesis-testing corrections (e.g., Romano-Wolf stepdown, Benjamini-Hochberg) should be applied to any family of heterogeneity tests.

---

## 15. Measurement, Compliance, Missingness, Spillover, and Implementation Limits

### Measurement Issues

| Issue | Concern | Mitigation |
|-------|---------|------------|
| Contact definition | "Contact" may include brief door-openings without meaningful engagement | Pre-specify what counts as contact (e.g., fundraiser delivers at least the opening script; or door opens and conversation begins). If possible, record engagement duration |
| Contribution measurement | Solicitors self-report contributions; recording errors or fraud are possible | Use pre-numbered receipt books, electronic recording if feasible, or independent verification for a subsample |
| Opt-out measurement | Opt-outs may be ambiguous (e.g., note falls off door, text received but not recorded) | Standardize the opt-out channel; log all opt-outs with timestamp |
| Avoidance measurement | "Not at home" vs. "home but not answering" vs. "answered but refused to engage" are observationally difficult to distinguish | Train solicitors to record observation codes; acknowledge measurement error in interpretation |

### Compliance

| Issue | Concern | Mitigation |
|-------|---------|------------|
| Notice delivery failure | Flyers may blow away, be removed by others, or not be seen | Use door hangers that are harder to miss; if budget allows, verify notice presence before visit |
| Opt-out non-processing | An opt-out may be submitted but not registered before the visit | Record opt-out processing time and flag cases where visit occurred before opt-out was processed; treat these as a separate "partial compliance" category in sensitivity analyses |
| Solicitor non-compliance | Fundraiser may deviate from protocol (e.g., reveal condition, adjust effort) | Random spot checks or ride-along monitoring; include protocol-deviation flag |

### Missingness

| Pattern | Concern | Mitigation |
|---------|---------|------------|
| Outcome not recorded | Solicitor fails to record outcome for some visits | Track visit completion rate by solicitor; test whether missingness is associated with treatment or covariates |
| Unit not attempted | Some assigned units are never visited (solicitor runs out of time, skips units) | Distinguish "assigned but not attempted" from "attempted but no contact." The former is a protocol deviation; the latter is an outcome. Analyze "not attempted" as a separate category |
| Differential missingness by arm | If Arm C units who opted out are disproportionately not recorded | Compare the total number of units in each arm against the assigned count; test for differential attrition |

### Spillover and Interference

| Concern | Mitigation |
|---------|------------|
| Neighbors in different arms discuss the fundraiser | If feasible, cluster-randomize at street segment or building level. If not, measure spatial proximity and test for spillover: regress outcomes on own-treatment and neighbor-treatment indicators |
| Solicitor learning across arms | If the same solicitor works multiple arms, they may adjust behavior. Randomize the order of visits within solicitor shifts, or assign solicitors to only one arm per shift |
| Repeated contact | If the same household appears multiple times (e.g., follow-up visits), flag these and cluster standard errors at the household level |

### Implementation Limits

| Limit | Implication |
|-------|-------------|
| Single fundraising organization | External validity is limited to this type of organization and cause. Pressure dynamics may differ for political, religious, or commercial solicitations |
| Short field window | Cannot capture long-term effects (donor retention, repeat giving, reputational effects) |
| Geographic scope | Results may not generalize to areas with different norms around door-to-door interaction |
| No auxiliary measurement of preferences | Without a separate elicitation of true willingness-to-pay or altruistic preferences, mechanism interpretation relies on behavioral patterns alone |

---

## 16. Failure Modes and Alternative Explanations

### Failure Mode 1: No Difference in Contact Rates

If contact rates are identical across Arms A, B, and C, this could mean:
- (a) Avoidance preference is negligible in this population (M2 is absent).
- (b) The opt-out mechanism did not work (notice not delivered, opt-out too costly, opt-out not salient).
- (c) Notice does not change scheduling behavior (M3 is absent).

Without a manipulation check on whether the notice and opt-out were received and understood, (b) cannot be distinguished from (a). **Mitigation**: Include a brief post-interaction check (e.g., "Did you receive our notice?") for a subsample of contacted units, or an unobtrusive measure of whether the notice was removed.

### Failure Mode 2: Contact Rates Differ but Conditional Giving Does Not

If Arm B has higher contact than Arm C but conditional giving is identical:
- (a) The marginal contactors in Arm B (those who would have opted out in Arm C) have the same giving propensity as always-contactees — inconsistent with M2 but consistent with a pure scheduling/awareness story plus homogeneous giving preferences.
- (b) Social pressure exists but operates equally on marginal and inframarginal units, producing no detectable difference in conditional means. The design has limited power to distinguish (a) from (b) without additional data on giving *amounts* (the distribution may shift even if the mean does not).

### Failure Mode 3: Arm C Has Higher Conditional Giving Than Arm B

If conditional giving in Arm C exceeds that in Arm B:
- This could mean that the opt-out selects out low-givers (consistent with M2: pressure-sensitive donors are also low-givers).
- Alternatively, receiving the opt-out offer generates positive affect toward the organization (a "respect" or "autonomy" effect), increasing giving among those contacted.
- These explanations have opposite welfare implications. **Mitigation**: Include a survey item for Arm C contactees measuring attitudes toward the organization; compare attitudinal measures across arms.

### Failure Mode 4: Opt-Out Signals Organization Type

If the opt-out offer itself signals something about the organization (e.g., professionalism, respect for autonomy, low-pressure culture), then the Arm B vs. Arm C contrast confounds pressure with signaling. This is a fundamental limitation of a design where the treatment itself alters perceptions. **Mitigation**: If feasible, vary the framing of the opt-out (e.g., neutral vs. warm language) to test whether framing matters, or include a post-interaction survey measure of perceived organization quality.

### Alternative Explanations for Any Observed Pattern

| Pattern | Standard Interpretation | Alternative Explanation |
|---------|------------------------|------------------------|
| Lower giving in Arm C | Pressure drives giving in B; pressure-sensitive types avoid C | Arm C notice signals low-quality organization; people give less because they value the cause less |
| Higher contact in B than A | Notice increases awareness and scheduling | Notice signals legitimacy, making people more willing to open the door (information effect, not pressure) |
| Small gifts fall in C relative to B | Pressure-driven marginal giving disappears | People who would give small amounts opt out entirely; the remaining pool happens to give larger amounts for unrelated reasons |
| No difference in large gifts across arms | Large gifts reflect genuine willingness (insensitive to pressure) | Large givers are always-contacted and their behavior is inelastic to process features for reasons unrelated to pressure |

---

## 17. What Cannot Be Claimed

Based on the available information, the following claims are not supported:

1. **"Social pressure causes X% of all giving."** The design can estimate the share of giving that disappears when avoidance is made easy, but this is the combined effect of selection (who avoids) and behavioral response (pressure on those who remain). Bounds can be placed on the behavioral component, but point identification requires untestable assumptions.

2. **"Genuine willingness is the only motive for giving."** Even if conditional giving is identical across all arms, this does not rule out pressure. Pressure may operate uniformly across all contacted units, or it may be offset by other differences between arms.

3. **"The opt-out mechanism reveals true preferences."** Opting out reveals a preference to avoid the interaction. It does not reveal the counterfactual giving decision if the interaction had occurred, nor does it reveal the underlying valuation of the cause.

4. **"The results generalize to other fundraising contexts."** The design is specific to in-person, door-to-door solicitation by a single organization in a particular geographic area.

5. **"Welfare effects are unambiguously positive or negative."** Even if pressure drives giving, the welfare implications depend on (a) the utility cost of pressure to donors, (b) the social value of the funds raised, and (c) any long-term effects on donor behavior or attitudes toward the organization. The design does not measure (a) or (c).

6. **"The design identifies the causal effect of social pressure on giving."** The design identifies the causal effect of solicitation-process features (notice, opt-out) on contact and giving. Social pressure is one interpretation of the mechanism behind these effects, but it is not directly manipulated or measured.

7. **"Contact and giving are independent decisions."** The design reveals that they are interdependent, but it cannot fully disentangle the joint decision process without stronger modeling assumptions.

---

## 18. Additional Data Needed

To strengthen the design from suggestive to dispositive, the following data would be valuable (listed in order of priority):

### High Priority

| Data Need | Why It Helps |
|-----------|-------------|
| **Post-interaction survey** (for contacted units) | Measures attitudes toward the organization, perceived pressure, and motivation for giving/not giving. Provides direct evidence on mechanisms rather than behavioral inference alone |
| **Notice delivery verification** | Confirms that the manipulation was received. Without this, null results are uninterpretable |
| **Prior giving history** (if any records exist) | Enables within-household comparisons and reduces noise in estimating treatment effects |
| **Detailed contact coding** (not home vs. home but no answer vs. brief answer vs. full engagement) | Disaggregates the "contact" outcome into components that have different mechanism interpretations |

### Medium Priority

| Data Need | Why It Helps |
|-----------|-------------|
| **Neighborhood demographic characteristics** | Enables heterogeneity analysis and improves precision of estimates |
| **Solicitor characteristics** (experience, gender, age) | Tests for solicitor-level heterogeneity in treatment effects |
| **Weather data for visit windows** | Weather may affect both contact rates (people home) and mood/generosity |
| **Alternative giving channel data** (online giving, mail-in) | If the notice includes an alternative giving option, comparing in-person vs. alternative giving across arms reveals substitution patterns |

### Lower Priority

| Data Need | Why It Helps |
|-----------|-------------|
| **Long-term follow-up** (repeat giving, donor retention) | Reveals whether pressure-driven giving crowds out future genuine giving or has lasting effects on the donor relationship |
| **Community-level social capital measures** | Contextualizes pressure dynamics in the local social environment |
| **Exact geographic coordinates** | Enables precise spatial spillover analysis |

---

## 19. Threat-Response Table

*(Not explicitly requested by the task packet, but provided for completeness.)*

| Threat | Response |
|--------|----------|
| Selection into contact is endogenous | Decompose unconditional giving into contact margin × conditional margin; apply Lee bounds under monotonicity |
| Opt-out signals organization quality | Acknowledge as a confound; test via attitudinal survey items or framing variations |
| Null contact-rate differences (manipulation failure) | Pre-register manipulation checks; if manipulation fails, the design collapses to a single-arm descriptive study |
| SUTVA violation (neighbor spillover) | Cluster-randomize if feasible; test for spatial correlation in outcomes; report spatial-robust standard errors |
| Solicitor heterogeneity | Block on solicitor; include solicitor FE; test for solicitor × treatment interactions |
| Differential attrition | Compare unit counts across arms; test whether missingness predicts treatment; conduct worst-case bounds on attrition |
| Small sample / low power | Pre-register minimum detectable effect sizes; use block randomization and covariate adjustment to improve precision |
| Multiple hypothesis testing | Pre-specify primary outcomes; apply correction for secondary tests |
| External validity | Be explicit about scope conditions; do not generalize beyond the study context without replication |

---

## 20. Claim-Evidence Table

| # | Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|-------|--------------|------------|------------|-------------------------------|
| 1 | Advance notice affects contact probability | Reduced-form regression of *Cᵢ* on Arm B indicator (vs. Arm A), with block FE | Causal (ITT) | High, under randomization | No statistically significant difference between Arm A and Arm B in contact rates, with a precisely estimated zero |
| 2 | Adding a low-cost opt-out reduces contact probability | Reduced-form regression of *Cᵢ* on Arm C vs. Arm B contrast | Causal (ITT) | High, under randomization and if manipulation is successful | Contact rates in Arm C are not lower than in Arm B (with sufficient power to detect a meaningful difference) |
| 3 | Unconditional giving differs across solicitation-process conditions | Reduced-form regression of *Gᵢ* on treatment indicators | Causal (ITT) | High, under randomization | No difference in unconditional giving rates across arms |
| 4 | The total giving effect can be decomposed into contact-margin and conditional-giving components | Accounting identity decomposition applied to ITT estimates | Descriptive decomposition | High (it is an identity given the estimates) | Not falsifiable — it is an accounting relationship. However, if the contact margin explains all of the total effect, the conditional-giving component is zero |
| 5 | Pressure-driven giving exists net of selection | Lee bounds on E[*G*(C) − *G*(B) \| always-contacted] exclude zero | Causal, under monotonicity + exclusion | Moderate (depends on untestable monotonicity) | Lee bounds include zero; or contact rates are equal across Arms B and C (bounds collapse) |
| 6 | Small gifts are differentially sensitive to pressure | Interaction between treatment and contribution-size category in a multinomial/ordered model | Descriptive association; suggestive of mechanism | Low (confounded by selection and alternative explanations) | Small-gift share does not differ differentially across arms; or the pattern is consistent with alternative explanations (e.g., differential selection by income) |
| 7 | Genuine willingness accounts for giving that persists when avoidance is easy | Giving rate in Arm C among contacted units, relative to Arm B | Descriptive; consistent with mechanism but not a causal test | Moderate for existence, low for magnitude | Giving in Arm C among contacted units is near zero (inconsistent with any genuine willingness) or identical to Arm B (the opt-out selects out no one, so willingness cannot be separated from other motives) |
| 8 | The opt-out mechanism reveals avoidance preference | Opt-out take-up rate in Arm C; differential contact rates between B and C | Descriptive behavioral measure | Moderate (if opt-out rate > 0, avoidance preference exists in at least some units) | Opt-out rate is zero; or opt-out rate is positive but driven by factors unrelated to avoidance (e.g., language barriers, misunderstanding) |
| 9 | The results are not driven by solicitor-level confounds | Solicitor FE regressions; solicitor × treatment interaction tests | Robustness check | High for ruling out large confounds, moderate for small ones | Treatment effects change substantially when solicitor FE are included; or solicitor × treatment interactions are large and significant |
| 10 | The findings are not artifacts of spatial spillover | Cluster-robust SE at route/building level; spatial correlation tests | Robustness check | Moderate (spillover is difficult to rule out conclusively) | Standard errors inflate substantially under spatial clustering; or neighbor-treatment indicators are significant predictors of own outcomes |

---

## Summary of Design Logic

The core logic of this design is:

1. **Vary the cost of avoiding the in-person interaction** (via the opt-out channel in Arm C) while holding information about the fundraiser constant (both Arms B and C receive advance notice).

2. **Observe who avoids.** The difference in contact rates between Arm B and Arm C reveals the share of potential donors who would prefer not to engage when avoidance is cheap. This is a behavioral measure of avoidance preference.

3. **Observe who gives, among those who do not avoid.** The difference in conditional giving between Arm B and Arm C, after accounting for the compositional change in who is contacted (via Lee bounds), reveals whether the interaction itself — above and beyond selection — changes giving behavior.

4. **Triangulate mechanisms through pattern-matching.** No single contrast cleanly isolates one mechanism, but the configuration of results across all comparisons narrows the set of plausible stories. The table below summarizes the predicted pattern for each pure mechanism:

| Pattern | Pure Genuine Willingness (M1) | Pure Social Pressure (M2) | Pure Scheduling (M3) | Marginal-Giving Sensitivity (M4) |
|---------|------------------------------|--------------------------|---------------------|----------------------------------|
| Contact: B vs. A | ≈ 0 | ≈ 0 | > 0 | ≈ 0 |
| Contact: C vs. B | ≈ 0 | < 0 | ≈ 0 | < 0 |
| Conditional giving: B vs. A | ≈ 0 | ≈ 0 or ambiguous | ≈ 0 (after Lee bounds) | ≈ 0 |
| Conditional giving: C vs. B | ≈ 0 (or >0 if C selects more motivated) | Ambiguous; Lee bounds needed | ≈ 0 (after Lee bounds) | Depends on composition |
| Small-gift share: C vs. B | ≈ 0 | < 0 | ≈ 0 | < 0 |
| Large-gift share: C vs. B | ≈ 0 | ≈ 0 | ≈ 0 | ≈ 0 |

In practice, mechanisms will coexist. The design estimates their relative importance by quantifying the magnitude of each margin rather than testing for the exclusive presence of any single mechanism.

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260527_210840_98725_1
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_210840_98725_1.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_210840_98725_1.trajectory.jsonl

## Operator Notes

- duration_ms: 375890
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
