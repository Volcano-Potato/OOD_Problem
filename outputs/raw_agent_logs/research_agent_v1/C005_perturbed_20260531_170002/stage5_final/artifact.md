# Stage 5: Final Design Memo

**Case ID**: C005 (Perturbed Variant)
**Perturbation**: No opportunity-side logs for untreated users.
**Stage 4 Critic Verdict**: ITT `defensible` | IV/LATE `defensible_with_caveats` | Selection-on-Observables `not_defensible` | Pre-Post `not_defensible`

---

## 1. Executive Summary

The packet asks whether a measurement strategy can credibly estimate the causal effect of actual digital ad exposure on downstream user outcomes when the platform controls delivery through auctions, targeting, and optimization — and when opportunity-side logs for untreated users are unavailable. The perturbation (no opportunity-side control logs) selectively damages the candidate designs.

The **Intent-to-Treat (ITT)** design, which estimates the causal effect of campaign *assignment* on outcomes using the Stage-2 randomization, is the only cleanly defensible identification strategy. Its core internal validity is unaffected by the perturbation because it uses only assignment status, realized impressions, and outcomes — all of which are observed. The ITT does not answer the question about *actual exposure*, but it answers the question that can be answered credibly.

The **IV/LATE** design, which instruments actual exposure with random assignment, is computationally feasible but its credibility is substantially degraded. The perturbation removes all ability to test the exclusion restriction, characterize the complier population, or verify monotonicity. It should be reported as a supplementary estimate with prominent disclosure of these untestable assumptions.

The **Selection-on-Observables** regression and the **Pre-Post** trajectory comparison are not defensible as causal designs. The former founders on endogenous platform optimization; the latter collapses into a single-group time series without any untreated comparison.

The primary recommendation is to center the analysis on the ITT, report the IV/LATE as a heavily caveated supplementary estimate, and explicitly downgrade any claim about the causal effect of *actual ad exposure* to a descriptive or correlational interpretation.

---

## 2. Research Question

What is the causal effect of a digital advertising campaign on downstream user conversion outcomes (website visits, registrations, leads, purchases, revenue) in a setting where the online platform controls ad delivery through auctions, targeting, pacing, and optimization, and where the researcher cannot observe which untreated users were eligible for ad opportunities?

---

## 3. Target Estimand or Strongest Defensible Estimand

**Primary (defensible)**: The Intent-to-Treat (ITT) effect — the average causal effect of campaign assignment (eligibility) on downstream conversion outcomes, regardless of whether the focal ad was actually served.

Formally:
\[
\tau_{\text{ITT}} = \mathbb{E}[Y_i(1) - Y_i(0) \mid \text{eligible}]
\]

where \(Y_i(1)\) is the potential outcome under assignment to campaign eligibility and \(Y_i(0)\) the potential outcome under holdout.

**Supplementary (heavily caveated)**: The Local Average Treatment Effect (LATE) of actual focal-ad exposure on downstream outcomes among compliers — users who receive an impression if and only if assigned. This estimand is computationally estimable but its identifying assumptions are untestable given the perturbation.

**What is not a defensible estimand**: The average treatment effect on the treated (ATT) of actual exposure among all exposed users, the population average treatment effect (ATE) of actual exposure, or any causal effect estimated solely from selection-on-observables or single-group pre-post comparisons.

---

## 4. Treatment or Exposure and Main Outcomes

**Treatment/Exposure**:
- Campaign assignment or eligibility (binary: assigned to campaign vs. holdout/control).
- Actual focal-ad exposure (binary: received at least one impression; count: number of impressions).
- The distinction between these two is central: assignment does not guarantee exposure, and the perturbation removes logs that would characterize this gap for untreated users.

**Main Outcomes**:
- Downstream conversion: website visit, registration, lead, purchase, revenue (binary or continuous).
- Measured at the user level over a short post-exposure outcome window.

**Secondary Outcomes**:
- Intermediate engagement events (clicks, landing-page visits, add-to-cart).
- Exposure frequency (number of impressions received).

---

## 5. Data Structure Summary

The data follow a four-stage structure:

| Stage | Description | Observed? |
|-------|-------------|-----------|
| **Stage 1** | Users become eligible for the campaign during a live delivery window with platform-level auctions or allocation rules. | Partially (eligibility rules inferred, not logged per opportunity). |
| **Stage 2** | Higher-level randomization or holdout assignment determines which users are eligible to receive the campaign. | **Yes** — assignment status is observed. |
| **Stage 3** | Conditional on eligibility, the platform determines whether the focal ad is actually served at each opportunity (via auctions, targeting, pacing, optimization). | **Partially** — realized impressions are observed for exposed users. Opportunity eligibility for *untreated* users is **not observed** (the perturbation). |
| **Stage 4** | The researcher observes actual impressions and downstream conversion outcomes. | **Yes** — impressions and outcomes are observed. |

**Key features**:
- **Unit of observation**: User-ad opportunity or user-impression record, linked to downstream outcomes.
- **Time span**: Short campaign window + post-exposure outcome window.
- **Panel structure**: Users can have multiple ad opportunities and multiple impressions over time.
- **Pre-campaign covariates**: User activity, device, channel, segment, time-of-opportunity indicators.

---

## 6. Relevant Causal Mechanisms

**Assignment → Eligibility → Exposure → Outcomes** is the core causal chain:

1. **Randomization channel**: The holdout assignment independently determines whether a user enters the campaign-eligible pool. This generates as-good-as-random variation in eligibility status.

2. **Platform delivery channel**: Conditional on eligibility, the platform's auction, targeting, pacing, and optimization algorithms determine whether the focal ad is actually served. This channel is endogenous: the platform optimizes for outcomes (clicks, conversions) that are correlated with the researcher's outcome of interest.

3. **Exposure → Outcome channel**: Actual ad exposure may change user behavior through attention, persuasion, reminder effects, or information transmission, leading to downstream conversions.

4. **Alternative pathways (threats to identification)**:
   - Market-level saturation: campaign scale may affect control-group outcomes.
   - Cross-channel exposure: users may see related ads on other channels.
   - Social spillover: exposed users may share information with unexposed users.
   - Platform behavioral response: assignment status may alter how the platform treats users beyond serving the focal ad (e.g., different ad load, different auction dynamics).

---

## 7. Main Identification Challenge

The central challenge is a **selection problem by institutional design**. The platform's delivery system — which uses auctions, targeting rules, pacing, and optimization — selects users for ad exposure based on variables (predicted click-through rate, user value scores, real-time auction conditions) that are correlated with the researcher's outcome. This makes naive comparisons of exposed vs. unexposed users hopelessly confounded.

The perturbation intensifies this challenge by removing the data that would allow the researcher to:
- Model the selection process into ad opportunities.
- Characterize which untreated users *would have* been eligible.
- Construct comparison groups matched on opportunity-level eligibility.
- Test platform behavioral responses to assignment status.
- Diagnose interference magnitude.

The identification challenge is not merely that selection exists — it is that the perturbation removes the data needed to observe, model, or bound it.

---

## 8. Whether Credible Causal Identification Is Possible

**For the effect of campaign assignment (ITT)**: **Yes.** Credible causal identification is possible using the Stage-2 randomization. The ITT design does not require opportunity-side logs for untreated users. Its internal validity rests on randomization integrity and SUTVA — assumptions that are defensible within the packet constraints.

**For the effect of actual ad exposure**: **No, not at full credibility.** The IV/LATE design produces a point estimate but cannot defend its core identifying assumptions (exclusion restriction, monotonicity) given the perturbation. The estimate is computationally feasible but its causal interpretation is epistemically hollow — it rests on untestable assertions rather than supportable assumptions. Any claim about the causal effect of actual exposure must be downgraded to a descriptive association with acknowledged, unquantifiable selection bias.

**For selection-on-observables or pre-post designs**: **No.** These designs produce associational estimates only. No causal interpretation is defensible.

---

## 9. Proposed Empirical Design or Strongest Defensible Descriptive Analysis

### Primary Design: Intent-to-Treat (ITT)

**Estimand**: \(\tau_{\text{ITT}} = \mathbb{E}[Y_i \mid Z_i = 1] - \mathbb{E}[Y_i \mid Z_i = 0]\), where \(Z_i = 1\) for users assigned to campaign eligibility and \(Z_i = 0\) for holdout.

**Identification**: Randomization of \(Z_i\) (Stage 2) ensures \(Z_i \perp\!\!\!\perp (Y_i(0), Y_i(1))\). The ITT is identified by the difference in mean outcomes between assigned and unassigned groups.

**Estimation**: Simple difference-in-means, or regression-adjusted:
\[
Y_i = \alpha + \tau_{\text{ITT}} Z_i + \mathbf{X}_i'\boldsymbol{\beta} + \varepsilon_i
\]
where \(\mathbf{X}_i\) includes pre-campaign user activity, device, channel, and segment controls to improve precision.

**Inference**: Heteroskedasticity-robust standard errors. If assignment is clustered (e.g., by geography or time block), cluster-robust standard errors at the assignment level.

**Interpretation**: \(\tau_{\text{ITT}}\) measures the causal effect of making the campaign *available* to users — the combined effect of eligibility, platform delivery, and any platform behavioral response. It is a policy-relevant parameter: it answers "what happens to outcomes when we turn the campaign on for this group?"

### Supplementary (Heavily Caveated): IV/LATE

**Estimand**: \(\tau_{\text{LATE}} = \frac{\mathbb{E}[Y_i \mid Z_i = 1] - \mathbb{E}[Y_i \mid Z_i = 0]}{\mathbb{E}[D_i \mid Z_i = 1] - \mathbb{E}[D_i \mid Z_i = 0]}\), where \(D_i\) is actual ad exposure.

**Reporting requirements**: The IV estimate must be accompanied by:
1. A prominent statement that the exclusion restriction and monotonicity are **untestable** given missing opportunity-side logs.
2. The first-stage F-statistic and complier share estimate.
3. A bounds analysis on plausible exclusion-restriction violations (e.g., Conley et al. 2012-style sensitivity).
4. An explicit warning that the LATE applies to an uncharacterizable complier subpopulation.

### Descriptive Analysis: Exposure-Outcome Association

**Purpose**: Document the raw association between actual exposure and outcomes, fully adjusted for observable covariates. Explicitly labeled as **descriptive, not causal**.

---

## 10. Why the Design Is Valid or Why Causal Identification Is Not Credible

### Why the ITT is valid

The ITT's internal validity rests on the Stage-2 randomization, which is explicitly stated in the packet: "Campaign-level randomization or holdout assignment exists." Randomization ensures that, in expectation, assigned and unassigned groups are balanced on all observed and unobserved baseline characteristics. The perturbation does not touch randomization, assignment-status observation, or outcome observation. The ITT is therefore identified from observed data alone with minimal assumptions.

Validity does not require:
- Opportunity-side logs for untreated users (assignment and outcomes suffice).
- The exclusion restriction (the ITT is the reduced form, not the structural parameter).
- Complier characterization (the ITT estimates the effect for all assigned).

### Why causal identification of actual ad exposure is not fully credible

The IV/LATE design requires the exclusion restriction: assignment affects outcomes *only* through actual ad exposure. The packet describes a platform that "controls which users actually receive impressions" through "auctions, targeting rules, pacing, and optimization." The perturbation removes the data that would allow testing whether assignment status alters platform behavior through channels other than focal-ad exposure. Without opportunity-side logs, the researcher cannot:
- Compare the distribution of ad opportunities across assigned and unassigned users.
- Test whether the platform serves different non-focal ads to assigned users.
- Detect differential auction dynamics, ad load, or pacing by assignment status.

The exclusion restriction is not merely untested — it is **untestable by construction** under this perturbation. The IV/LATE point estimate is computable, but its causal interpretation is not defensible at the standard of evidence the packet implies.

---

## 11. Required Assumptions

### For the ITT (primary)

| Assumption | Description | Defensibility Given Packet |
|------------|-------------|---------------------------|
| **Random assignment integrity** | Assignment to campaign eligibility is as-good-as-random. | **Defensible**: Packet states "Campaign-level randomization or holdout assignment exists." |
| **SUTVA / No interference** | One user's assignment does not affect another user's outcomes. | **Partially defensible**: Packet flags spillover risks. Can be partially assessed via dose-response or geographic clustering analysis, but market-level saturation is untestable given the perturbation. |
| **No differential attrition** | Outcome measurement is not differentially missing by assignment status. | **Defensible**: Outcomes are passively logged; no self-report attrition. |
| **Excludability of assignment** (not required) | Not required for ITT. Assignment is the treatment, not an instrument. | N/A |

### For the IV/LATE (supplementary)

| Assumption | Description | Defensibility Given Packet |
|------------|-------------|---------------------------|
| **Relevance** | Assignment affects actual exposure (first stage ≠ 0). | **Testable**: First stage estimable from observed data. |
| **Exclusion restriction** | Assignment affects outcomes only through actual ad exposure. | **Untestable**: The perturbation removes all diagnostic data. The platform's endogenous optimization makes this assumption suspect. |
| **Monotonicity** | No defiers: no users who would receive the ad only when unassigned. | **Untestable**: The perturbation removes the data needed to detect defiers. |
| **SUTVA** | As above. | As above. |
| **Complier comparability** | The LATE for compliers is informative for the population of interest. | **Unassessable**: Complier characteristics cannot be estimated without opportunity-side logs. |

---

## 12. Statistical Model or Analysis Equation

### Primary: ITT with Covariate Adjustment

\[
Y_i = \alpha + \tau_{\text{ITT}} Z_i + \mathbf{X}_i^{\text{pre}}\boldsymbol{\beta} + \boldsymbol{\gamma}_{s(i)} + \boldsymbol{\delta}_{t(i)} + \varepsilon_i
\]

where:
- \(Y_i\): downstream conversion outcome (binary or continuous) for user \(i\).
- \(Z_i\): binary indicator for campaign assignment/eligibility.
- \(\mathbf{X}_i^{\text{pre}}\): vector of pre-campaign user activity covariates.
- \(\boldsymbol{\gamma}_{s(i)}\): segment fixed effects.
- \(\boldsymbol{\delta}_{t(i)}\): time-of-eligibility fixed effects.
- \(\tau_{\text{ITT}}\): parameter of interest — the ITT effect.
- \(\varepsilon_i\): idiosyncratic error, clustered at the assignment unit level if applicable.

**Estimation**: OLS with heteroskedasticity-robust standard errors. For binary outcomes, linear probability model is preferred for interpretability of \(\tau_{\text{ITT}}\); logistic regression with average marginal effects as robustness.

### Supplementary: IV/LATE (caveated)

**First stage**:
\[
D_i = \pi_0 + \pi_1 Z_i + \mathbf{X}_i^{\text{pre}}\boldsymbol{\phi} + \nu_i
\]

**Reduced form**:
\[
Y_i = \alpha_{\text{RF}} + \tau_{\text{RF}} Z_i + \mathbf{X}_i^{\text{pre}}\boldsymbol{\psi} + \eta_i
\]

**LATE (Wald estimator)**:
\[
\tau_{\text{LATE}} = \frac{\tau_{\text{RF}}}{\pi_1}
\]

**Inference**: Two-stage least squares (2SLS) with robust standard errors. Weak-instrument robust inference (Anderson-Rubin confidence sets, or Kleibergen-Paap Wald F-statistic with Stock-Yogo critical values).

### Descriptive: Exposure-Outcome Association

\[
Y_i = \alpha_{\text{desc}} + \beta_{\text{desc}} D_i + \mathbf{X}_i^{\text{pre}}\boldsymbol{\theta} + \varepsilon_i
\]

Explicitly reported as **descriptive only**. \(\beta_{\text{desc}}\) is not a causal parameter.

---

## 13. Robustness, Placebo, Falsification Checks, or Diagnostic Tests

### For the ITT

| Check | Description | Data Required |
|-------|-------------|---------------|
| **Balance tests** | Compare pre-campaign covariates (activity, device, channel, segment) across assignment groups. Formalized via joint F-test of \(Z_i\) on all pre-campaign covariates. | Assignment status + pre-campaign covariates (observed). |
| **Pre-trends test** | If pre-campaign outcomes are available over time, test whether assigned and unassigned groups follow parallel trends before the campaign. Estimate: \(Y_{it}^{\text{pre}} = \alpha_t + \beta_t Z_i + \varepsilon_{it}\) and test \(\beta_t = 0\) for all pre-campaign periods. | Pre-campaign outcome panel (should be available per "pre-campaign user activity"). |
| **Placebo outcome** | Replace the conversion outcome with a pre-determined variable that should be unaffected by campaign assignment (e.g., pre-campaign activity metric). | Pre-campaign user activity (observed). |
| **Placebo treatment** | If multiple campaigns or holdout waves exist, test whether assignment to a *future* campaign predicts current outcomes (should be zero). | Multi-wave assignment data (packet-ambiguous; if unavailable, note as limitation). |
| **Randomization inference** | Fisher-style exact p-values via permutation of assignment labels to avoid asymptotic approximations. | Assignment + outcomes (observed). |

### For the IV/LATE (supplementary)

| Check | Description | Feasibility Given Perturbation |
|-------|-------------|-------------------------------|
| **First-stage strength** | Report Kleibergen-Paap F-statistic. If F < 10, use weak-instrument robust methods. | **Feasible**: Assignment and exposure both observed. |
| **Sensitivity to exclusion violation** | Conley et al. (2012) bounds: estimate LATE under assumed plausible ranges of direct effect of \(Z\) on \(Y\). | **Feasible**: Requires only observed data + researcher-specified bounds. |
| **Overidentification** (if multiple instruments) | If assignment has multiple dimensions (timing, intensity, creative variant), test overidentifying restrictions. | **Potentially feasible**: Depends on whether multiple assignment dimensions exist in the packet. |
| **Exclusion restriction diagnostics** | **Not feasible**: Requires opportunity-side logs for untreated users. | N/A — the perturbation removes this. |
| **Complier characterization** | **Not feasible**: Requires opportunity-side logs for untreated users. | N/A — the perturbation removes this. |

---

## 14. Heterogeneity Analysis If Supportable

**Within the ITT framework**, heterogeneity analysis is supportable for dimensions observed in both assignment groups:

1. **By pre-campaign activity tercile**: Are high-activity users more responsive to campaign eligibility? Estimate stratum-specific ITTs and test for interaction.

2. **By device or channel**: Does the campaign assignment effect differ by mobile vs. desktop, or by platform channel? Report channel-specific ITTs with interaction tests.

3. **By segment**: If the packet's segment variable captures demographic or behavioral clusters, estimate segment-specific ITTs.

4. **By exposure frequency (descriptive only)**: Among assigned users who were actually exposed, describe how outcomes vary with impression count. This is **descriptive**, not causal — exposure intensity is endogenous to the platform's delivery optimization.

**Limitation**: Heterogeneity analysis by actual exposure level (e.g., exposed vs. unexposed among the assigned) requires controlling for selection into exposure, which the perturbation makes impossible. Do not present such subgroup comparisons as causal.

---

## 15. Measurement, Compliance, Missingness, Spillover, or Implementation Limits

### Compliance

The packet explicitly states: "Assignment or eligibility does not guarantee actual exposure because the focal ad may not be served." This is one-sided non-compliance: unassigned users cannot receive the ad (no defiers in the standard sense, though the platform's behavioral response could create complex patterns). The first-stage take-up rate is estimable among assigned users from observed impression logs. What is **not** estimable: the counterfactual exposure rate among unassigned users if they had been assigned — i.e., the complier share — because the perturbation removes opportunity-side logs.

### Measurement

Outcomes (conversions, revenue) are passively logged platform events. Measurement error is likely low for binary outcomes (purchase, registration) but may be higher for revenue if attribution windows are incomplete. If the outcome window is short and fixed, right-censoring is minimal.

### Missingness

Differential missingness is unlikely given passive logging, but if the platform's outcome tracking relies on user identifiers that may be lost (cookie deletion, cross-device), the match rate between impression records and outcome records should be reported by assignment group.

### Spillover / Interference

The packet's Data Card flags: "Users may see ads on other channels, share information, or be affected by market-level campaign saturation." Without opportunity-side logs for untreated users, the researcher **cannot**:
- Measure how many control-group users were eligible for but did not receive ad opportunities.
- Diagnose market-level saturation by comparing opportunity-eligible control users to non-eligible users.
- Detect within-platform cross-user interference.

The perturbation removes the most natural diagnostic for SUTVA violations. The ITT estimate should be interpreted as the net effect *in the presence of whatever spillover exists*, which may be a lower bound on the direct effect.

### Implementation Limits

The ITT requires that assignment status is accurately recorded and not contaminated. If holdout leakage occurs (assigned users who are treated as unassigned by the platform, or vice versa), the ITT is biased toward zero.

---

## 16. Failure Modes and Alternative Explanations

### Failure modes for the ITT

| Failure Mode | Mechanism | Consequence | Detectability |
|-------------|-----------|-------------|---------------|
| **Randomization failure** | Assignment not truly random (e.g., platform engineers manually overrode holdout for high-value users). | Biased ITT estimate. | **Partially detectable**: Balance tests on observables. Not testable for unobservables. |
| **SUTVA violation (market saturation)** | Campaign is large enough that control-group outcomes are suppressed or elevated by market-level effects. | ITT biased toward zero (if saturation depresses relative lift) or away from zero (if saturation elevates outcomes for all). | **Not detectable** given the perturbation — requires opportunity-level data showing control users' ad-opportunity eligibility. |
| **SUTVA violation (social spillover)** | Exposed users share information with unexposed users, affecting control-group outcomes. | ITT biased toward zero. | **Not detectable** with packet data. Requires social-graph or geographic proximity data. |
| **Differential attrition** | Outcome tracking fails more often for one assignment group (e.g., assigned users clear cookies more). | Biased ITT. | **Partially detectable**: Compare match rates and missingness by assignment group. |
| **Holdout leakage** | Platform misclassifies some assigned users as unassigned, or vice versa. | ITT biased toward zero (both groups become more similar). | **Not detectable** without platform-internal assignment logs. |

### Failure modes for the IV/LATE (if reported as supplementary)

| Failure Mode | Mechanism | Consequence | Detectability |
|-------------|-----------|-------------|---------------|
| **Exclusion restriction violation** | Assignment changes platform behavior (ad load, auction dynamics) in ways that affect outcomes beyond focal-ad exposure. | LATE overstates or understates the effect of actual exposure. | **Not detectable** — the perturbation removes diagnostic data. |
| **Monotonicity violation** | Some users receive fewer impressions when assigned due to platform reprioritization. | LATE is not interpretable as a causal effect for any well-defined subpopulation. | **Not detectable** — requires opportunity-side logs for both groups. |
| **Weak instrument** | Low take-up rate produces imprecise estimates and hypersensitivity to exclusion violations. | Wide confidence intervals; small exclusion violations produce large LATE bias. | **Detectable**: First-stage F-statistic. |

### Alternative explanations for any observed ITT effect

1. **Concurrent marketing**: Other campaigns (email, search, TV) coinciding with the campaign window drive outcomes in the assigned group.
2. **Seasonal effects**: If assignment is correlated with calendar time (e.g., holdout wave timing), seasonal conversion patterns confound the ITT.
3. **Platform algorithmic change**: If the platform changed its delivery algorithm during the campaign window, the ITT conflates the campaign effect with the algorithm change effect.
4. **User lifecycle effects**: If eligible users were at a different point in their user lifecycle than ineligible users (despite randomization, small samples could produce imbalance).

---

## 17. What Cannot Be Claimed

In light of the Stage 4 critique and the perturbation, the following claims are **not** supported:

1. **"The campaign's ads caused a X% lift in conversions."** The ITT estimates the effect of campaign *eligibility/assignment*, not the effect of ad exposure. The supplementary IV/LATE produces a number for actual exposure but its identifying assumptions are untestable. Neither design supports an unqualified causal claim about actual ad exposure.

2. **"The causal effect of ad exposure is \(\tau_{\text{LATE}}\)."** The IV/LATE estimate rests on an untestable exclusion restriction and unverifiable monotonicity. The estimate is computationally feasible but its causal interpretation is not defensible. It should be reported, if at all, as: "Under the strong and untestable assumptions that assignment affects outcomes only through focal-ad exposure and that no defiers exist, the LATE for compliers is approximately \(\hat{\tau}_{\text{LATE}}\). We cannot verify these assumptions with available data."

3. **"Exposed users are comparable to unexposed users after controlling for observables."** The platform optimizes delivery using variables correlated with the outcome. No amount of observable covariate control removes this selection. This is a descriptive association, not a causal effect.

4. **"The ad increased conversions relative to users' pre-campaign trajectories."** Without an untreated comparison group experiencing the same calendar period, pre-post changes conflate ad effects with common time trends, seasonality, and regression to the mean.

5. **"The effect generalizes to users who were not served the ad."** The complier population is uncharacterizable without opportunity-side logs. The LATE's external validity is unknown and unknowable from available data.

6. **"The campaign had no spillover effects."** SUTVA violations are flagged in the packet but untestable given the perturbation. The ITT estimate is the net effect inclusive of whatever interference exists; it cannot be decomposed into direct and indirect effects.

**What can be claimed:**

- "Campaign assignment/eligibility caused a \(\hat{\tau}_{\text{ITT}}\) change in downstream conversions (95% CI: [...]), relative to the holdout group, under the maintained assumption of no interference."
- "The first-stage take-up rate was \(\hat{\pi}_1\): among assigned users, \(\hat{\pi}_1 \times 100\%\) received at least one impression."
- "The raw association between actual ad exposure and conversions, adjusted for observable covariates, was \(\hat{\beta}_{\text{desc}}\) (descriptive only; does not support causal interpretation)."

---

## 18. Additional Data Needed

To upgrade the analysis from ITT-only to credible identification of actual ad exposure effects, the following data would be needed:

| Data Need | Purpose | Priority |
|-----------|---------|----------|
| **Opportunity-side logs for untreated users** | Enables complier characterization, exclusion-restriction diagnostics, monotonicity checks, and selection modeling. Would transform IV/LATE from untestable to defensible. | **Highest** |
| **Pre-campaign outcome panel** | Enables formal pre-trends tests and difference-in-differences extensions. | High |
| **Multi-wave campaign data** | Enables placebo treatment tests and staggered adoption designs. | High |
| **Geographic or network proximity data** | Enables spillover diagnostics and partial interference bounds. | Medium |
| **Platform-internal bidding/optimization features** (predicted CTR, user value scores, pacing state) | Would allow partial modeling of the selection mechanism into exposure, even without opportunity-side logs for untreated users. | Medium |
| **Cross-channel ad exposure data** | Enables assessment of cross-channel contamination of the control group. | Medium |
| **Longer outcome window** | Enables assessment of treatment-effect dynamics and whether effects persist or decay. | Low |

---

## 19. Threat-Response Table

*Not explicitly requested by the task packet. Omitted per contract.*

---

## 20. Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|-------|---------------|------------|------------|-------------------------------|
| Campaign assignment/eligibility causally affects downstream conversion outcomes. | Stage-2 randomization (packet: "Campaign-level randomization or holdout assignment exists"); observed assignment status; observed outcomes; balance on pre-campaign covariates. | Causal (ITT) | **High** (internal validity from randomization; external validity limited by setting) | Failure of balance tests on pre-campaign observables; evidence of holdout leakage; detectable SUTVA violation from auxiliary data. |
| The effect of campaign assignment operates partly through actual ad exposure. | First-stage regression of actual exposure on assignment (both observed in logs); positive and statistically significant \(\pi_1\). | Causal (first-stage) | **High** conditional on no measurement error in exposure logging. | \(\pi_1 = 0\) or indistinguishable from zero; evidence that assignment suppresses exposure (negative first stage). |
| The causal effect of actual ad exposure on outcomes among compliers is approximately \(\hat{\tau}_{\text{LATE}}\). | IV ratio of reduced-form ITT to first-stage; random assignment as instrument. | Causal (LATE) with **heavy caveats** | **Low** — exclusion restriction and monotonicity are untestable given the perturbation. | Any evidence of exclusion-restriction violation (requires unobserved data); evidence of defiers (requires unobserved data); first-stage F < 10. |
| Actual ad exposure is positively associated with conversions after controlling for observables. | Regression of outcomes on actual exposure with pre-campaign activity, device, channel, segment, and time controls. | Descriptive association | **High** (as an association); **zero** (as a causal claim) | Not falsifiable as an association claim; as a causal claim, any evidence of unobserved confounders (which the packet itself provides: platform optimization). |
| Users' outcomes changed after first ad exposure relative to their pre-exposure baseline. | Within-user pre-post comparison among exposed users. | Descriptive trend | **High** (as a measured trend); **zero** (as a causal claim) | The existence of the trend is not falsifiable; its causal interpretation is falsified by any common time shock, seasonal effect, or evidence of regression to the mean. |
| The assignment mechanism was as-good-as-random. | Balance tests on pre-campaign covariates; no significant predictors of assignment among observables beyond the randomization design. | Supporting / diagnostic | **Moderate** — observables may balance even if unobservables do not. | Significant imbalance on any pre-campaign covariate; evidence of manual overrides in assignment logs. |
| No interference between assignment groups (SUTVA). | Auxiliary: geographic dispersion of assigned vs. unassigned users; dose-response analysis (if larger assigned share in a market → smaller ITT, that's evidence of saturation). | Supporting / diagnostic | **Low** — the perturbation removes the most direct diagnostic (opportunity-side logs). Packet itself flags interference risks. | Evidence that ITT varies with campaign intensity at the market level; evidence of cross-user information sharing (requires social-graph data not in packet). |

---

**Final recommendation**: Center the research report on the ITT as the only cleanly defensible causal estimand. Report the IV/LATE as a supplementary sensitivity analysis with prominent disclosure of untestable assumptions. Explicitly label all exposure-outcome associations and pre-post comparisons as descriptive. State clearly that the perturbation (no opportunity-side logs for untreated users) makes credible causal identification of the effect of *actual ad exposure* impossible with available data — but that the ITT still provides a policy-relevant causal answer about the effect of campaign eligibility.