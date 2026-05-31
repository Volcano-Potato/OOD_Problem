# Raw Agent Run Log

- `run_id`: RUN_20260527_225055_12_openclaw_deepseekv4pro_isolated
- `case_id`: C005
- `variant_id`: level3
- `level`: level3
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
- `timestamp`: 2026-05-27T22:50:55+0800
- `input_file`: benchmark/cases/C005_online_ad_measurement/agent_task_level3.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: Measuring the Causal Effect of Digital Ad Exposure Under Platform-Controlled Delivery

---

## 1. Executive Summary

This design addresses the measurement of advertising effectiveness when actual ad exposure is jointly determined by a campaign-level assignment mechanism and a platform-level delivery optimization system. The core problem is that users who actually receive impressions differ systematically from those who do not, because platform auctions and pacing algorithms allocate impressions toward users with higher predicted engagement or conversion propensity. The proposed strategy uses campaign-level assignment or eligibility (e.g., from a randomized holdout or phased rollout) as an instrument for actual exposure within an instrumental variables framework. Because assignment operates above the individual impression decision, it can generate plausibly exogenous variation in exposure probability without being contaminated by the platform's within-eligibility optimization. The design must carefully distinguish four sequential concepts: assignment, eligibility, exposure opportunity, and actual exposure. The strongest defensible causal estimand is the local average treatment effect (LATE) of actual exposure among compliers—users whose exposure status is shifted by assignment. Where compliance is weak, the estimand may be further limited to the intention-to-treat (ITT) effect of assignment itself. Critical threats include differential platform sorting within eligibility, weak instruments when assignment only modestly shifts exposure probability, tracking-driven measurement error in outcomes, and interference from other advertising channels.

---

## 2. Research Question

What is the causal effect of actual digital ad exposure on downstream conversion outcomes (visits, registrations, purchases), when the platform—not the researcher—controls which eligible users receive focal-ad impressions through auctions, targeting, pacing, and optimization rules?

---

## 3. Target Estimand (or Strongest Defensible Estimand)

### 3.1 Four Distinct Quantities

The design must disentangle four concepts that are observationally distinct but often conflated:

| Quantity | Definition | Supports Claim About |
|---|---|---|
| **ITT (Intent-to-Treat)** | Effect of campaign assignment/eligibility on outcomes, ignoring whether exposure actually occurred | Whether the *campaign eligibility policy* changes outcomes |
| **ATT (Average Treatment Effect on the Treated)** | Effect of actual exposure among those exposed | Whether *exposed users* differ from what they would have been without exposure (requires unconfoundedness of exposure, which is not credible here) |
| **LATE (Local Average Treatment Effect)** | Effect of actual exposure among compliers—users whose exposure status is shifted by the assignment instrument | Whether exposure *causes* behavior change for the marginal user whose exposure decision depends on assignment |
| **ATE (Average Treatment Effect)** | Effect of exposure if all eligible users were exposed | Unidentified without extrapolation from LATE |

### 3.2 Primary Target Estimand

The **strongest defensible causal estimand** is the **Local Average Treatment Effect (LATE)** of actual focal-ad exposure on downstream conversions for the subpopulation of users whose exposure status is shifted by campaign assignment or eligibility (the complier subpopulation).

Formally, for user \(i\) with potential outcomes \(Y_i(1)\) under exposure and \(Y_i(0)\) under no exposure, and instrument \(Z_i\) (assignment/eligibility) shifting actual exposure \(D_i\):

\[
\tau_{\text{LATE}} = \mathbb{E}[Y_i(1) - Y_i(0) \mid D_i(1) > D_i(0)]
\]

Where \(D_i(z)\) is potential exposure status under assignment status \(z\).

### 3.3 Fallback Estimand

If the instrument is too weak (assignment barely shifts exposure probability), the primary defensible estimand becomes the **ITT effect** of campaign assignment on downstream outcomes:

\[
\tau_{\text{ITT}} = \mathbb{E}[Y_i \mid Z_i = 1] - \mathbb{E}[Y_i \mid Z_i = 0]
\]

This identifies the causal effect of *making users eligible for the campaign*, not the effect of *receiving ads*. It remains policy-relevant (answering "should we run this campaign?") but cannot isolate the ad mechanics.

### 3.4 What Cannot Be Estimated

- **ATE** of exposure on all eligible users is not identified without strong and untestable homogeneity or extrapolation assumptions.
- **ATT** (effect on exposed users relative to an unexposed counterfactual) is not identified without assuming that, conditional on observables, exposure is as-good-as-random. This assumption is not credible given platform optimization.

---

## 4. Treatment/Exposure and Main Outcomes

### Treatment and Exposure Variables

| Variable | Type | Description |
|---|---|---|
| \(Z_i\) | Binary instrument | Campaign assignment or eligibility (e.g., randomized holdout indicator, treatment-cell membership) |
| \(O_{it}\) | Binary intermediate | Exposure opportunity at time \(t\) for user \(i\) (user had a realistic chance for the focal ad to be served) |
| \(D_i\) | Binary endogenous treatment | Actual focal-ad exposure (received at least one impression during the campaign window) |
| \(F_i\) | Count (secondary) | Exposure frequency (number of focal-ad impressions received) |

### Outcome Variables

| Variable | Type | Description |
|---|---|---|
| \(Y_i\) | Binary or continuous | Primary: downstream conversion (visit, registration, purchase, revenue) within attribution window |
| \(E_i\) | Binary (secondary) | Intermediate engagement event (click, landing-page visit within shorter window) |
| \(R_i\) | Continuous (secondary) | Revenue or transaction value if available |

---

## 5. Data Structure Summary

The data has a hierarchical opportunity-within-user structure:

- **Level 1 (opportunity-level):** Each record is a user-ad-opportunity during the campaign window. Fields include: opportunity timestamp, whether the focal ad was served, auction or relevance signals, eligibility flags.
- **Level 2 (user-level):** Aggregated from opportunity records. Fields include: assignment indicator \(Z_i\), any-exposure indicator \(D_i\), exposure count \(F_i\), pre-campaign covariates \(X_i\), post-exposure outcome \(Y_i\).

The design operates primarily at the user level for estimation (assignment and outcomes are user-level concepts), but exploits opportunity-level records for:
1. Verifying that assignment shifts exposure probability (instrument relevance)
2. Constructing exposure-opportunity indicators
3. Diagnosing platform sorting patterns

Clustering is at the user level (or campaign-cell level if assignment is grouped).

---

## 6. Relevant Causal Mechanisms

### M1: Endogenous Platform Sorting
The platform's auction, targeting, and pacing systems allocate impressions toward users with higher predicted relevance, engagement propensity, or purchase intent. This generates positive selection: exposed users have systematically higher baseline outcome potential than unexposed users, even absent any causal ad effect. A naive comparison of \(Y\) by \(D\) confounds selection with treatment.

**Direction of bias:** Likely upward—exposed users would have converted at higher rates anyway.

### M2: Assignment-Exposure Gap (Non-Compliance)
Campaign assignment or eligibility changes the set of users who *could* receive impressions, but some assigned/eligible users receive zero impressions (never-takers in the opportunity sense), while some non-assigned users may still receive impressions through other channels or spillover (potential always-takers or defiers). This creates a compliance gap between assignment and exposure.

### M3: Sequential Opportunity Structure
Users face multiple ad opportunities over time. Later opportunities may be affected by earlier exposures (dynamic treatment effects) and by platform learning from earlier user responses. Simple binary exposure measures may miss dose-response relationships.

### M4: Measurement-Driven Outcome Variation
Conversion outcomes are observed through tracking systems that depend on identifiers, attribution windows, cross-device matching, and cookie/ID persistence. Measurement error in outcomes may correlate with exposure (e.g., users who click on ads leave stronger tracking traces), creating differential measurement error by treatment status.

### M5: Cross-Channel and Market-Level Interference
Users may be exposed to the advertiser's campaigns on other platforms, competitor advertising, or organic brand activity during the same period. These spillovers violate SUTVA (Stable Unit Treatment Value Assumption) at the user level.

---

## 7. Main Identification Challenge

The central challenge is that **actual ad exposure \(D_i\) is endogenous** because the platform delivery system selects users for impression delivery based on characteristics—observed or unobserved—that also predict conversion outcomes. Even within a randomized assignment cell, the platform's within-cell optimization creates differential selection into actual exposure.

This generates a classic simultaneity: \(D_i\) is correlated with the error term in any regression of \(Y_i\) on \(D_i\), because unobserved user quality \(u_i\) drives both platform delivery decisions and conversion outcomes:

\[
Y_i = \alpha + \tau D_i + \beta X_i + u_i
\]
\[
\text{Cov}(D_i, u_i) \neq 0
\]

The researcher's task is to find variation in \(D_i\) that is uncorrelated with \(u_i\). Campaign assignment \(Z_i\) provides such variation if it is randomized (or conditionally random), but assignment operates on eligibility, not on the platform's impression-by-impression delivery decision. The instrument shifts the *probability* of exposure but does not determine it deterministically.

---

## 8. Whether Credible Causal Identification Is Possible

**Yes, credible causal identification is possible for LATE**, provided:

1. Campaign assignment or eligibility \(Z_i\) is randomized (or conditionally random given observable strata).
2. Assignment generates a meaningful first stage (it substantively shifts the probability of actual exposure).
3. The exclusion restriction holds: assignment affects outcomes only through its effect on exposure probability (no direct effect of eligibility per se, other than through changing exposure).
4. Monotonicity holds: assignment does not reduce any user's probability of receiving the focal ad (no defiers).

**Causal identification is not credible without an assignment instrument.** A purely observational comparison of exposed vs. unexposed users—even with rich covariate controls—cannot credibly recover the causal effect of exposure because the platform optimizes on unobservable user characteristics that are unavailable to the researcher.

---

## 9. Proposed Empirical Design

### 9.1 Core Design: Instrumental Variables with Campaign Assignment as Instrument

**Stage 0: Assignment mechanism.** The researcher exploits campaign-level randomization or holdout assignment \(Z_i \in \{0, 1\}\). Examples of assignment mechanisms (illustrative, not assumed):
- Randomized user-level holdout (advertiser-side experiment)
- Geographic or temporal phased rollout generating as-if-random variation
- Platform-provided ghost bidding or PSA control conditions

The crucial requirement is that \(Z_i\) is independent of potential outcomes and potential exposure status: \(\{Y_i(0), Y_i(1), D_i(0), D_i(1)\} \perp\!\!\!\perp Z_i\).

**Stage 1: First stage.** Estimate the effect of assignment on exposure probability:

\[
D_i = \gamma_0 + \gamma_1 Z_i + \gamma_2 X_i + \varepsilon_i
\]

The F-statistic on \(\gamma_1 = 0\) must exceed conventional thresholds (F > 10) for reliable inference. If \(Z_i\) only weakly shifts \(D_i\), LATE estimation is unreliable, and the design should fall back to ITT.

**Stage 2: Reduced form.** Estimate the effect of assignment on outcomes:

\[
Y_i = \pi_0 + \pi_1 Z_i + \pi_2 X_i + \nu_i
\]

This is the ITT estimate. It is a valid causal estimate under randomization of \(Z_i\) alone, regardless of compliance.

**Stage 3: Second stage (2SLS).** Instrument \(D_i\) with \(Z_i\):

\[
Y_i = \beta_0 + \beta_1 \hat{D}_i + \beta_2 X_i + \eta_i
\]

Where \(\hat{D}_i\) is the predicted exposure from the first stage. \(\beta_1\) estimates the LATE.

### 9.2 Design Variant: Dose-Response IV

If exposure frequency \(F_i\) (count of impressions) is the treatment of interest rather than binary exposure, extend the IV framework:

\[
F_i = \gamma_0 + \gamma_1 Z_i + \gamma_2 X_i + \varepsilon_i \quad \text{(first stage)}
\]
\[
Y_i = \beta_0 + \beta_1 \hat{F}_i + \beta_2 X_i + \eta_i \quad \text{(second stage)}
\]

This requires the stronger assumption that assignment shifts exposure frequency monotonically and that the exclusion restriction holds in expectation across frequency levels. The LATE interpretation becomes "the effect of one additional impression for compliers whose impression count is shifted by assignment."

### 9.3 Opportunity-Level Diagnostics (Not the Primary Design)

To validate the instrument and understand the compliance mechanism, opportunity-level data should be used diagnostically:

1. **Exposure probability by assignment:** Verify that \(P(D_i = 1 \mid Z_i = 1) > P(D_i = 1 \mid Z_i = 0)\) and that the difference is substantively meaningful.
2. **Platform sorting by assignment:** Check whether observable covariates \(X_i\) predict exposure *within* assignment cells similarly. If \(X_i\) predicts exposure equally in both \(Z_i = 0\) and \(Z_i = 1\) groups, this supports the instrument's validity (the platform is not differentially sorting by assignment status).
3. **Opportunity counts by assignment:** Verify that assignment shifts the number of opportunities users face, not just the per-opportunity probability of winning the auction.
4. **First-stage decomposition:** Estimate how much of the first-stage relationship operates through increasing opportunity count vs. increasing win probability per opportunity.

### 9.4 Fallback: ITT Analysis

If the first-stage F-statistic is below 10, or if monotonicity is suspect:

Report the ITT as the primary result. This answers the question: "Did making users eligible for the campaign change their behavior?" It is a well-defined causal effect of the *policy* of campaign eligibility, even though it cannot isolate the *mechanism* of ad exposure.

---

## 10. Why the Design Is Valid

### 10.1 Instrument Relevance

If campaign assignment genuinely changes whether users are eligible to receive impressions, it should generate a non-trivial shift in the probability that the focal ad is actually served. The first stage formalizes and tests this condition. The key concern—and the condition that must be empirically verified—is whether the platform's delivery system is sufficiently constrained by assignment status for \(Z_i\) to act as a meaningful shifter of \(D_i\).

The design is valid because:
- Assignment operates *above* the platform's delivery optimization: it changes the eligible pool rather than competing within the auction.
- Randomization (or conditional randomization) of \(Z_i\) ensures that users in the treatment and control assignment cells are balanced on both observed and unobserved pre-campaign characteristics.
- The IV estimator recovers the causal effect for compliers without requiring the implausible assumption that exposure is random conditional on observables.

### 10.2 Exclusion Restriction Reasoning

The exclusion restriction requires that assignment \(Z_i\) affects outcomes \(Y_i\) only through its effect on actual exposure \(D_i\). The main threat is that assignment itself—being marked as eligible—could change user behavior through mechanisms other than ad exposure (e.g., changes in platform ranking, organic visibility, or other platform features correlated with campaign inclusion).

**Defense:** If the campaign operates purely through ad delivery (i.e., assignment changes nothing for the user except the probability of seeing the focal ad), the exclusion restriction is plausible. If the platform treats eligible users differently in non-ad dimensions (e.g., organic search ranking, recommendation feed placement), the restriction is violated. The design should test for differences in non-ad platform interactions by assignment status among never-exposed users as a falsification check.

### 10.3 Monotonicity Reasoning

Monotonicity requires that assignment to the campaign does not *reduce* any user's probability of receiving the focal ad: \(P(D_i = 1 \mid Z_i = 1) \geq P(D_i = 1 \mid Z_i = 0)\) for all \(i\). This is plausible if the campaign purely expands the eligible pool—adding users to the auction rather than removing them. It could be violated if assignment involves platform-level re-optimization (e.g., the platform responds to campaign assignment by re-allocating delivery budgets in ways that reduce exposure for some assigned users). The design cannot test monotonicity directly, but it can assess plausibility by checking whether the first stage is positive and whether there is any evidence of negative individual-level treatment effects (which would indicate defiers if the exclusion restriction holds).

---

## 11. Required Assumptions

| Assumption | Formal Statement | Plausibility | Testable? |
|---|---|---|---|
| **A1: Random Assignment** | \(Z_i \perp\!\!\!\perp \{Y_i(0), Y_i(1), D_i(0), D_i(1)\}\) | Depends on assignment mechanism quality | Partially: covariate balance tests |
| **A2: Instrument Relevance** | \(\text{Cov}(Z_i, D_i) \neq 0\) | Requires empirical verification | Yes: first-stage F-test |
| **A3: Exclusion Restriction** | \(Y_i(z, d) = Y_i(d)\) for all \(z, d\) | Plausible if assignment only affects exposure, not other platform features | Partially: falsification tests on never-exposed |
| **A4: Monotonicity** | \(D_i(1) \geq D_i(0)\) for all \(i\) | Plausible if campaign expands eligible pool | No direct test; sign checks |
| **A5: SUTVA / No Interference** | \(Y_i(\mathbf{D}) = Y_i(D_i)\) | Questionable if other ad channels operate simultaneously | Partially: market-level saturation checks |
| **A6: Outcome Measurement Independence** | Measurement error in \(Y_i\) is independent of \(Z_i\) | Questionable if tracking differs by assignment | Partially: tracking-coverage by assignment checks |

---

## 12. Statistical Model or Analysis Equation

### Primary Specification: Two-Stage Least Squares

**First stage:**
\[
D_i = \gamma_0 + \gamma_1 Z_i + \mathbf{X}_i'\boldsymbol{\gamma}_2 + \varepsilon_i
\]

**Reduced form:**
\[
Y_i = \pi_0 + \pi_1 Z_i + \mathbf{X}_i'\boldsymbol{\pi}_2 + \nu_i
\]

**Second stage:**
\[
Y_i = \beta_0 + \beta_1 \hat{D}_i + \mathbf{X}_i'\boldsymbol{\beta}_2 + \eta_i
\]

Where:
- \(Z_i\): campaign assignment/eligibility indicator
- \(D_i\): actual exposure indicator (or exposure count \(F_i\))
- \(\hat{D}_i\): predicted exposure from first stage
- \(\mathbf{X}_i\): pre-campaign covariates (user activity, device, channel, market segment, time indicators)
- \(\beta_1\): LATE of actual exposure (or per-impression LATE for count specification)

### Standard Errors

Cluster standard errors at the user level if multiple observations per user are retained. If assignment is grouped (e.g., by geography or time cell), cluster at the assignment-unit level.

### IV Estimator Expression

For binary \(Z_i\) and binary \(D_i\), the Wald estimator gives:

\[
\beta_1^{\text{Wald}} = \frac{\mathbb{E}[Y_i \mid Z_i = 1] - \mathbb{E}[Y_i \mid Z_i = 0]}{\mathbb{E}[D_i \mid Z_i = 1] - \mathbb{E}[D_i \mid Z_i = 0]}
\]

This is the ITT scaled by the compliance rate, and it directly recovers LATE under the stated assumptions.

---

## 13. Robustness, Placebo, Falsification Checks, and Diagnostic Tests

### 13.1 Covariate Balance

Test balance of pre-campaign covariates \(X_i\) across assignment arms \(Z_i = 0\) and \(Z_i = 1\). Standardized mean differences should be near zero. Imbalance indicates failure of randomization or conditional randomization.

### 13.2 First-Stage Strength

Report F-statistic on excluded instrument. F < 10 indicates weak instruments; use limited-information maximum likelihood (LIML) or Anderson-Rubin confidence sets instead of 2SLS. F < 5 suggests fall back to ITT.

### 13.3 Platform Sorting Diagnostics

Within each assignment arm, regress exposure \(D_i\) on observable covariates \(X_i\):
\[
D_i = \delta_0 + \mathbf{X}_i'\boldsymbol{\delta} + \zeta_i \quad \text{(within } Z_i = 1 \text{ and } Z_i = 0 \text{ separately)}
\]

If the coefficients \(\boldsymbol{\delta}\) are similar across arms, this suggests that platform sorting operates similarly regardless of assignment—supporting instrument validity. If sorting patterns differ by arm, the platform may be responding to assignment in ways that violate the exclusion restriction.

### 13.4 Pre-Period Outcome Placebo

If pre-campaign outcome data exist (e.g., conversions before the campaign window), test:
\[
Y_i^{\text{pre}} = \alpha_0 + \alpha_1 Z_i + u_i
\]

\(\alpha_1\) should not be statistically or economically significant. This tests whether assignment is independent of baseline outcome levels.

### 13.5 Never-Exposed Outcome Test (Exclusion Diagnostic)

Among users who never receive a focal-ad impression (\(D_i = 0\)), test whether assignment \(Z_i\) predicts outcomes:
\[
Y_i \mid (D_i = 0) = \kappa_0 + \kappa_1 Z_i + \omega_i
\]

If \(\kappa_1 \neq 0\), this suggests assignment has a direct effect on outcomes through channels other than ad exposure (violation of exclusion). This is an imperfect test because never-exposed users may be selected differently across arms, but a null result is reassuring.

### 13.6 Alternative Instrument Specifications

- Use a **split-sample IV**: estimate the first stage on one random half, the second stage on the other, to reduce finite-sample bias from weak instruments.
- Use **multiple instruments** if assignment varies by sub-period or sub-geography (e.g., different rollout timing as separate instruments) and test overidentifying restrictions via Hansen's J-test.

### 13.7 Bounds Analysis

If the instrument is weak or exclusion is questionable, compute **nonparametric bounds** (e.g., Manski bounds or Nevo-Rosen imperfect IV bounds) that characterize the range of possible treatment effects consistent with weaker assumptions.

---

## 14. Heterogeneity Analysis (If Supportable)

### 14.1 By Pre-Campaign Activity Level

Split users by pre-campaign activity terciles. Estimate LATE separately within each tercile to assess whether ad effects differ by baseline engagement. This is substantively important because platform delivery systems often prioritize high-activity users, and the complier subpopulation may differ across activity levels.

### 14.2 By Device or Channel

If device (mobile vs. desktop) or channel is observable, estimate separate first stages and LATEs. Platform auction dynamics may differ across device types, and treatment effects may differ as well.

### 14.3 By Exposure Frequency

Among compliers, estimate whether the effect of a first impression differs from the effect of additional impressions (requires dose-response IV with multiple instruments or stronger assumptions).

### 14.4 By Timing Within Campaign

If campaign-level randomization is time-invariant but delivery timing varies, estimate whether effects differ by how early in the campaign the first exposure occurs.

### 14.5 Caveat

Heterogeneity analysis requires sufficient statistical power within subgroups. With weak instruments, subgroup LATE estimates will be imprecise. In such cases, report subgroup ITT effects instead.

---

## 15. Measurement, Compliance, Missingness, Spillover, and Implementation Limits

### 15.1 Measurement Error in Outcomes

Tracking loss (identifier churn, cross-device behavior, cookie deletion) creates measurement error in \(Y_i\). If tracking loss is independent of assignment \(Z_i\), this attenuates the reduced form but does not bias the IV estimator (classical measurement error in the dependent variable). However, if users who receive ads are more likely to be trackable (e.g., because the ad impression itself creates or refreshes a tracking identifier), measurement error is differential and biases even IV estimates.

**Response:** If possible, compare tracking-coverage rates by assignment arm among users with similar pre-campaign characteristics. If tracking rates differ, acknowledge this as a remaining limitation.

### 15.2 Non-Compliance (Never-Takers)

Users assigned to the campaign who receive zero impressions are never-takers. LATE explicitly excludes them from the estimand. The design must report:
- Compliance rate: \(\hat{\gamma}_1 = \mathbb{E}[D_i \mid Z_i = 1] - \mathbb{E}[D_i \mid Z_i = 0]\)
- The characteristics of compliers (estimated via the Abadie weighting approach: weight observations by \(1 - D_i(1 - Z_i)/P(Z_i = 1) - (1 - D_i)Z_i/P(Z_i = 0)\))
- Whether compliers differ meaningfully from the full eligible population

### 15.3 Missing Outcome Data

If outcomes are missing for some users (neither observed as converting nor non-converting), assess whether missingness is differential by assignment arm. If missingness is non-differential, complete-case analysis is unbiased for ITT (under MCAR). If differential, bounds or sensitivity analysis (e.g., Lee bounds) should be applied.

### 15.4 Spillover and Interference

Users in the control arm may be exposed to the focal campaign through other channels (other platforms, shared devices, organic brand activity). This attenuates the ITT and inflates the LATE (since the compliance differential narrows while the reduced form narrows proportionally).

**Response:** If the campaign operates on a single platform and assignment is user-level within that platform, the main spillover concern is cross-platform exposure and market-level effects. Both are difficult to rule out with single-platform data. Acknowledge that estimates represent the *incremental* effect of platform-level ad delivery beyond what control users might receive through other channels.

### 15.5 Implementation Limit: Platform Opacity

The researcher cannot observe the platform's full delivery algorithm, relevance scores, or auction mechanics. This limits the ability to:
- Precisely model the compliance mechanism
- Test why some assigned users remain unexposed
- Verify that assignment does not trigger other platform behavioral changes

---

## 16. Failure Modes and Alternative Explanations

| Failure Mode | Likelihood | Consequence | Diagnostic |
|---|---|---|---|
| **Weak instrument** (F < 10) | Moderate—depends on platform delivery constraints | 2SLS estimates severely biased toward OLS; confidence intervals invalid | First-stage F-statistic |
| **Exclusion violation** (assignment affects outcomes through non-ad channels) | Low-to-moderate—if platform ties eligibility to other features | IV estimates confounded by non-exposure channels | Never-exposed outcome test; non-ad platform interaction checks |
| **Monotonicity violation** (some users less likely to receive ads when assigned) | Low—but depends on platform re-optimization | LATE estimand no longer well-defined; Wald ratio does not recover a meaningful causal parameter | Cannot be directly tested; assess via plausibility arguments |
| **Differential measurement error** (tracking quality differs by assignment) | Moderate—if ad impressions improve tracking | Bias in both ITT and LATE of unknown sign | Compare tracking rates by assignment |
| **Cross-platform spillover** (control users receive ads on other platforms) | Moderate-to-high for multi-channel advertisers | Attenuated ITT, inflated LATE | Cannot be assessed with single-platform data |
| **Dynamic treatment effects** (later impressions depend on responses to earlier ones) | High—given repeated exposure structure | Static IV does not capture dynamic treatment response | Compare ITT for single- vs. multi-impression users |
| **Selection into repeated exposure** | High—platform optimizes delivery toward responsive users | LATE interpretable only for marginal impression, not for additional impressions among already-exposed compliers | Stratify by exposure count, acknowledge limitations |

---

## 17. What Cannot Be Claimed

1. **The ATE of ad exposure for all eligible users.** LATE recovers the effect only for compliers—users whose exposure is shifted by assignment. This subpopulation may not be representative of all eligible users, especially if compliance is low.

2. **The ATT of ad exposure (effect on the exposed).** Without the assumption that exposure is unconfounded conditional on observables—which is not credible given platform optimization—this parameter is not identified.

3. **That ad exposure causes conversions through any specific mechanism** (e.g., awareness, persuasion, reminder). The design estimates a causal effect but does not decompose it into pathways.

4. **The incremental effect beyond what other channels or market-level activity would generate.** If control users are affected by spillovers, the estimated LATE is relative to the control group's partially-treated state, not relative to a true zero-exposure counterfactual.

5. **Long-run effects beyond the attribution window.** The design is limited to outcomes observed within the defined window.

6. **That the same effect would hold under different platform delivery rules or campaign budget levels.** LATE is specific to the institutional setting in which assignment generates variation.

7. **General equilibrium or market-level effects.** The user-level design cannot capture price effects, competitive responses, or aggregate demand shifts.

8. **That exposure is the sole driver of ITT effects if exclusion is violated.** If assignment changes non-ad platform features, the ITT should not be interpreted as purely an ad effect.

---

## 18. Additional Data Needed

To strengthen identification beyond the current design:

| Data Need | Why It Would Help |
|---|---|
| **Multiple assignment arms with different eligibility intensity** (e.g., budget levels, targeting breadth) | Would generate multiple instruments, allowing tests of overidentifying restrictions and potentially identifying average causal response functions across exposure levels |
| **Pre-campaign outcome data** (same metric as primary outcome in a pre-period) | Enables difference-in-differences IV to control for baseline differences and assess parallel trends |
| **Platform-side auction data** (bids, relevance scores, competitor ads served) | Allows modeling the selection mechanism and constructing more precise compliance models |
| **Cross-platform ad exposure data** (impressions on other platforms) | Enables assessment and bounding of spillover, and isolation of the focal platform's incremental effect |
| **Longer post-campaign windows** | Enables assessment of effect persistence and decay beyond the immediate attribution window |
| **User-level tracking-coverage indicators** | Enables assessment and correction for differential measurement error |
| **Ghost-ad or PSA control data** (if the platform provides counterfactual auction outcomes) | Would strengthen the control group by ensuring the platform's delivery logic is applied identically to control users |

---

## 19. Threat-Response Table

| Threat | Why It Matters | Proposed Diagnostic or Design Response | Remaining Limitation |
|---|---|---|---|
| **Endogenous exposure:** Users receiving impressions have higher baseline conversion propensity because the platform optimizes delivery toward predicted relevance or intent | A naive OLS regression of \(Y\) on \(D\) estimates a confounded mixture of the causal effect and selection bias. Direction of bias is likely upward. | Use campaign assignment \(Z_i\) as an instrument for \(D_i\) in an IV framework. Assignment generates variation in exposure that is (by design) uncorrelated with user-level unobservables. First stage formalizes this. | (1) LATE only identifies effect for compliers, not all eligible users. (2) If the instrument is weak, IV estimates are unreliable. (3) If the platform's sorting mechanism interacts with assignment, exclusion may be violated. |
| **Estimand confusion:** ITT, ATT, LATE, and ATE are distinct quantities supporting different claims | Conflating assignment effects with exposure effects leads to incorrect inference about ad mechanics. Reporting ITT as "ad effect" overstates what the design can attribute to the ad. | Explicitly distinguish four quantities (ITT, ATT, LATE, ATE). Primary estimand is LATE. ITT is the fallback. Report both the reduced form and the IV result. Clearly label which claim each estimate supports. | Even with clear labeling, consumers of the research may conflate the estimates. The complier subpopulation may differ from policy-relevant populations. |
| **Timing/outcome window:** Conversions may occur before, during, or after exposure; post-treatment information may contaminate covariates | Using post-exposure variables as controls or defining the outcome window incorrectly creates post-treatment bias or reverses causality | Define outcome window to start only after the opportunity for first exposure. Use strictly pre-campaign covariates only. Avoid any covariate measured after campaign start. | The timing of the outcome window relative to exposure may still misattribute conversions that would have occurred anyway if users have pre-existing conversion trajectories. Without a pre-period outcome series, this cannot be tested. |
| **Measurement of outcomes:** Conversion tracking may miss outcomes due to ID churn, cross-device, offline purchases, or incomplete attribution | Measurement error in \(Y\) reduces precision. If tracking quality differs by exposure status (e.g., clicked users have stronger identifiers), error is differential and biases even IV estimates. | Compare tracking-coverage proxies by assignment arm. If differential tracking is suspected, apply bounds (e.g., Lee bounds for differential attrition). Acknowledge direction of potential bias. | Single-platform data may not allow verification of cross-device or offline conversions. Bounds may be wide and uninformative. |
| **Compliance/take-up:** Many assigned/eligible users receive zero focal impressions; some may receive repeated impressions | Low compliance weakens the first stage (weak instrument problem). Repeated exposure creates a dose-response dimension that binary exposure measures miss. | Report compliance rate and first-stage F-statistic. If compliance is too low, fall back to ITT. For repeated exposure, estimate dose-response IV with impression count as the endogenous variable, acknowledging stronger assumptions. | Dose-response IV requires stronger monotonicity and linearity assumptions. LATE for the first impression may differ from LATE for additional impressions, but single-instrument designs cannot separately identify both. |
| **Spillover/interference:** Control users may see ads on other platforms; market saturation may affect all users | Control group is not a pure zero-exposure counterfactual. ITT is attenuated; LATE is inflated (denominator shrinks more than numerator). | Acknowledge this as a fundamental limitation of single-platform designs. If geographic variation exists, compare markets with different campaign saturation levels for a diagnostic. | Cannot isolate the focal platform's incremental effect from cross-platform or market-level effects. Estimated LATE should be interpreted as "incremental to whatever exposure the control group receives through other channels." |

---

## 20. Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
| **C1:** Making users eligible for the campaign changes their conversion behavior (ITT) | Reduced-form regression of \(Y_i\) on \(Z_i\) with covariate adjustment. Randomized or conditionally randomized assignment ensures internal validity. | Causal (under randomization of \(Z_i\)) | High (if assignment is well-randomized) | Falsification: Pre-period outcome imbalance across \(Z_i\) arms; covariate imbalance despite randomization; null reduced-form with tight confidence intervals |
| **C2:** Actual ad exposure causes increased conversions among compliers (LATE) | 2SLS estimate of \(Y_i\) on \(\hat{D}_i\) using \(Z_i\) as instrument. First stage confirms \(Z_i\) shifts \(D_i\). | Causal (under IV assumptions) | Moderate—depends on instrument strength, exclusion, and monotonicity | Falsification: F < 10 (weak instrument); never-exposed outcome test shows \(Z_i\) affects \(Y_i\) when \(D_i = 0\); alternative overidentifying restrictions rejected; sign of first stage is negative |
| **C3:** Ad exposure is more effective for high-activity users than low-activity users | Subgroup LATE estimates by pre-campaign activity tercile | Correlational heterogeneity of a causal estimate | Low-to-moderate (reduced power in subgroups; complier composition may differ across subgroups) | Falsification: Subgroup LATEs are statistically indistinguishable; complier characteristics differ systematically across subgroups such that comparisons conflate selection with heterogeneity |
| **C4:** Additional impressions (beyond the first) have diminishing returns | Dose-response IV with \(F_i\) as endogenous variable | Causal under stronger assumptions (linearity, monotonicity across frequency levels) | Low—single instrument cannot separately identify first-impression and additional-impression effects | Falsification: Non-linearity in reduced form of \(Y_i\) on \(Z_i\) (i.e., ITT does not scale linearly with exposure frequency); different instruments produce different dose-response estimates |
| **C5:** Platform delivery optimization creates positive selection into exposure | Within-assignment-arm regressions of \(D_i\) on pre-campaign covariates \(X_i\); comparison of observable characteristics of exposed vs. unexposed users within \(Z_i = 1\) | Descriptive (but highly informative) | High—this pattern is expected from platform optimization and should be observable | Falsification: No observable covariate differences between exposed and unexposed within the assignment arm (would suggest platform is not optimizing on observables, though unobservable optimization could still exist) |
| **C6:** The campaign's effect persists beyond the immediate attribution window | ITT or LATE estimated over progressively longer outcome windows | Descriptive (causal within each window, but comparison across windows is descriptive) | Moderate—longer windows increase risk of contamination from other campaigns and events | Falsification: Effect converges to zero at longer windows; pattern is inconsistent with a dose-response relationship |
| **C7:** The measured ad effect is not driven by differential tracking quality | Comparison of tracking-coverage indicators by assignment arm; sensitivity of results to exclusion of users with known tracking issues | Diagnostic | Moderate—can detect gross differential tracking but not subtle differences | Falsification: Tracking rates differ significantly by arm; results change materially when restricting to well-tracked users |
| **C8:** The effect of campaign assignment is not driven by non-ad platform changes (exclusion restriction holds) | Never-exposed outcome test; comparison of non-ad platform interactions by assignment arm | Diagnostic | Moderate—can detect some violations but not all | Falsification: \(Z_i\) predicts \(Y_i\) among never-exposed users; non-ad platform engagement metrics differ by \(Z_i\) |

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260527_225055_98725_12
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_225055_98725_12.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_225055_98725_12.trajectory.jsonl

## Operator Notes

- duration_ms: 223197
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
