# Raw Agent Run Log

- `run_id`: RUN_20260527_225838_14_openclaw_deepseekv4pro_isolated
- `case_id`: C005
- `variant_id`: no_solution
- `level`: no_solution
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
- `timestamp`: 2026-05-27T22:58:38+0800
- `input_file`: benchmark/cases/C005_online_ad_measurement/agent_task_no_solution.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: Digital Advertising Effectiveness Without Experimental Variation

---

## 1. Executive Summary

This research design evaluates whether exposure to a digital advertising campaign causes users to convert (visit, sign up, or purchase). The advertiser possesses rich user-level behavioral logs, impression data, and conversion outcomes — but no experimental holdout exists. Exposure is entirely determined by the platform's targeting, bidding, and optimization algorithms, which allocate ads to users precisely because they are predicted to convert. This creates a fundamental selection problem: exposed and unexposed users differ systematically in unobserved purchase intent, and no amount of covariate adjustment can credibly eliminate this confounding when selection is driven by the same latent factors that determine outcomes.

After examining the available data structure, identification constraints, and potential design approaches, I conclude that **credible causal identification of the effect of ad exposure on conversion is not possible with the data described in this packet**. No randomized or quasi-random variation source, credible instrument, regression discontinuity threshold, difference-in-differences shock, or natural experiment is available. Rich covariates reduce observable imbalance but cannot address selection on unobservables that is inherent in algorithmic ad delivery.

The strongest defensible analysis is therefore **descriptive and predictive**: documenting conversion-rate differences between exposed and unexposed users, decomposing these differences into observable and residual components using rich covariate adjustment, and quantifying the sensitivity of estimated associations to unobserved confounding. I recommend bounding exercises, heterogeneity descriptions, and predictive modeling as the legitimate empirical contribution, coupled with a clear statement of what would be required to estimate causal ad lift in future work (a randomized controlled trial or a credible quasi-experimental design).

---

## 2. Research Question

Does exposure to the focal digital advertising campaign cause an increase in user conversions (visits, sign-ups, purchases, or revenue), and can this effect be credibly separated from the targeting-driven selection that determines who sees ads?

The question has both a primary causal component — "does seeing the ad *cause* conversion?" — and an auxiliary descriptive component — "how large are the raw and covariate-adjusted associations between exposure and conversion, and what do they reveal about targeting, user behavior, and campaign reach?"

---

## 3. Target Estimand (or Strongest Defensible Estimand)

### Ideal Causal Estimand (Not Credibly Identifiable)

The ideal causal estimand is the **average treatment effect on the treated (ATT)**:

> *ATT = E[Y(1) − Y(0) | D = 1]*

where *Y(1)* is the potential conversion outcome if a user is exposed to the campaign, *Y(0)* is the potential outcome if the same user is not exposed, and *D = 1* indicates actual exposure. The ATT captures the average causal lift among users who actually saw the ad, which is the quantity of direct business interest.

### Strongest Defensible Estimand

Because *Y(0)* is never observed for exposed users and no credible identification strategy exists to recover it, the ATT is not credibly identifiable. The strongest defensible estimand is instead the **covariate-adjusted associational difference**:

> *Δ_adj = E[Y | D = 1, X] − E[Y | D = 0, X]*

aggregated over the exposed-user covariate distribution. This is a descriptive estimand, not a causal one. It answers: "After accounting for observable differences between exposed and unexposed users, what is the residual difference in conversion rates?" It does not and cannot answer: "What would have happened to exposed users had they not been exposed?"

A supplementary estimand is the **bounds on the ATT** under explicit assumptions about the maximum degree of selection on unobservables, following partial-identification or sensitivity-analysis frameworks (see Section 12).

---

## 4. Treatment or Exposure and Main Outcomes

### Primary Exposure Variable

- **Binary exposure indicator** (*D_i*): whether user *i* received at least one impression from the focal campaign during the campaign window. This is the simplest and most policy-relevant definition, corresponding to the "intent-to-treat" concept in an experimental analogue.

### Supplementary Exposure Measures (for Descriptive Analysis)

- **Exposure frequency**: count of impressions delivered to user *i*.
- **Exposure recency**: time since most recent impression relative to conversion window end.
- **Click indicator**: whether user *i* clicked on any campaign creative.

These are not independent treatments but endogenous outcomes of the targeting process. They are useful for describing dose-response patterns and engagement depth but cannot support causal claims about incremental effects of additional impressions or clicks.

### Main Outcome Variable

- **Binary conversion indicator** (*Y_i*): whether user *i* completed a conversion event (visit, sign-up, or purchase) within the downstream attribution window.

### Secondary Outcomes

- Revenue or purchase amount (continuous or zero-inflated).
- Repeat visit indicator.
- Intermediate engagement events (e.g., product page views, add-to-cart).

---

## 5. Data Structure Summary

The data have a **user-level cross-sectional structure with repeated impression-event histories**. The researcher observes, for each user in the eligible population during the campaign period:

| Dimension | Description |
|---|---|
| Unit of observation | User (with impression-event sub-records) |
| Cross-section size | All users eligible for targeting under platform rules |
| Treatment group | Users receiving ≥1 impression |
| Comparison group | Eligible users receiving zero impressions |
| Time structure | Single campaign period with defined pre-period and post-period conversion window |
| Pre-campaign data | Historical browsing, purchase, segment, and device covariates |
| Panel element | Users may have multiple impression timestamps; outcomes are measured once per user |

**Critical data limitation**: The comparison group (unexposed eligible users) is not a control group. These users were *not* randomly withheld from exposure. They were systematically not shown ads because the platform's algorithms, bidding, and targeting rules determined they were less valuable to show ads to — a decision that correlates with their latent conversion propensity.

---

## 6. Relevant Causal Mechanisms

Several mechanisms could link ad exposure to observed conversion differences. Distinguishing among them is the core identification challenge.

### Mechanism 1: Genuine Causal Ad Effect (The Mechanism of Interest)

Seeing the ad causes an increase in conversion probability through awareness, persuasion, reminder effects, or reduced search costs. This is the mechanism the advertiser hopes to measure.

### Mechanism 2: Algorithmic Targeting Selection (Confounding)

The platform's delivery algorithm assigns ads to users based on features that also predict conversion — past purchase behavior, browsing recency, predicted purchase intent scores, segment membership, and real-time auction dynamics. Users selected for exposure have higher *baseline* conversion probability even without the ad. Observed conversion differences between exposed and unexposed users therefore reflect a mixture of Mechanism 1 (causal effect) and Mechanism 2 (selection bias), with no way to decompose them using observational data alone.

### Mechanism 3: User-Driven Selection (Endogenous Exposure)

Users who are more likely to convert may also be more likely to be in environments, times, or behavioral states where ads are served (e.g., frequent platform users see more ads simply because they are on the platform more). This induces a positive correlation between exposure and conversion that is not causal.

### Mechanism 4: Click-Mediated Effects (Mediation and Post-Treatment Bias)

If exposure causes clicks and clicks cause conversion, the total effect of exposure decomposes into a direct effect and an indirect effect through clicks. But clicks are themselves endogenous: users click because they are interested, and controlling for clicks introduces post-treatment bias. Causal mediation analysis is not feasible without additional identification.

### Mechanism 5: Spillover and Cross-Channel Contamination

Users not exposed on this platform may see the advertiser's ads on other platforms, through other channels, or be affected by general campaign awareness (e.g., word-of-mouth, earned media, offline promotion). This violates the Stable Unit Treatment Value Assumption (SUTVA) and biases the comparison between "exposed" and "unexposed" toward zero (if unexposed users are partially treated elsewhere) or in unknown directions.

### Mechanism 6: Attribution and Measurement Error

Conversion tracking may be incomplete due to cross-device behavior (user sees ad on mobile, converts on desktop), cookie or identifier loss, ad-blocking, or mismatched attribution windows. This introduces measurement error in both the exposure and outcome variables, likely attenuating estimated associations.

---

## 7. Main Identification Challenge

The central identification challenge is **selection on unobservables driven by algorithmic ad delivery**. The assignment mechanism — platform targeting, bidding, and optimization — is:

1. **Non-random**: exposure probability is a deterministic or stochastic function of user features, many of which are also predictors of conversion.
2. **Non-ignorable**: the features driving exposure assignment overlap substantially with the features driving conversion outcomes.
3. **Partially unobserved by the researcher**: even with rich user covariates, the platform's internal prediction scores, real-time bidding dynamics, and algorithmic logic are typically proprietary and unavailable. The features the platform uses to target may be more granular, more timely, or differently constructed than what the researcher observes.

The standard condition for covariate-based identification is **conditional unconfoundedness (selection on observables)**:

> *(Y(0), Y(1)) ⟂ D | X*

This requires that, conditional on observed covariates *X*, exposure assignment is as good as random. In a platform advertising setting with algorithmic targeting, this assumption is **highly implausible**. The platform's algorithm exists precisely to select users with high *Y(1)* and/or high *Y(0)*, using proprietary information beyond the researcher's covariate set. The rich covariates available to the researcher reduce but do not eliminate this problem: the same latent purchase intent that drives conversion also drives the platform's decision to serve an ad.

No quasi-experimental variation source (instrument, discontinuity, timing shock, staggered rollout, or natural experiment) is provided in the data. Therefore, **no credible identification strategy is available** to isolate variation in *D* that is independent of *Y(0)*.

---

## 8. Whether Credible Causal Identification Is Possible

**No.** Credible causal identification is not possible with the data and variation sources described in this packet.

This conclusion follows from:

1. **No random or quasi-random assignment**: Exposure is entirely determined by platform optimization, which targets users based on conversion-relevant features.
2. **No instrument**: No variable exists that shifts exposure probability without affecting conversion through any channel other than exposure. The packet explicitly states no credible instrument is available.
3. **No discontinuity**: No threshold, cutoff, or boundary exists in the assignment process that would enable a regression discontinuity design.
4. **No timing shock**: No externally imposed change in ad delivery, campaign launch, or eligibility rules creates a natural experiment or difference-in-differences opportunity.
5. **Impossible-to-satisfy unconfoundedness**: The condition required for covariate adjustment to yield causal estimates — that all confounders are observed and correctly modeled — is not credible when assignment is algorithmic and targeted.

The strongest defensible position is to **refuse to claim causal identification** and instead conduct and clearly label a descriptive and predictive analysis with sensitivity bounds.

---

## 9. Proposed Empirical Design: Strongest Defensible Descriptive Analysis

Since causal identification is not credible, I propose a multi-component descriptive and diagnostic analysis that transparently documents what the data can and cannot reveal.

### Component A: Raw Comparison and Balance Diagnostics

**Step A1**: Compute the unadjusted difference in mean conversion rates between exposed and unexposed users:

> *Δ_raw = Ȳ|D=1 − Ȳ|D=0*

**Step A2**: Construct standardized mean differences (SMDs) for all available covariates between exposed and unexposed users. Report the full balance table. This documents the degree of selection — large SMDs on conversion-relevant covariates (past purchases, browsing intensity, prediction scores) directly reveal algorithmic targeting at work.

### Component B: Covariate-Adjusted Associational Estimates

**Step B1**: Estimate the covariate-adjusted associational difference using a range of flexible estimators:

- Logistic or linear probability model with rich controls.
- Propensity score weighting (inverse probability weighting, IPW) to reweight the unexposed group to match the exposed group on observables.
- Doubly robust methods (augmented inverse probability weighting, AIPW) that combine outcome regression and propensity score modeling.
- Machine learning-based methods (e.g., causal forests, BART, or double/debiased machine learning approaches adapted for associational estimation) to capture nonlinear relationships without assuming correct parametric specification.

**Step B2**: Report how the adjusted associational difference changes as increasingly rich covariate sets are added, following a "coefficient stability" approach. If adding more controls meaningfully reduces the estimated gap, this is evidence that observable selection accounts for part of the raw difference. However, stability after adding strong predictors of conversion does **not** imply the remaining difference is causal — it may simply reflect that the remaining selection is on dimensions orthogonal to the observed covariates.

### Component C: Sensitivity Analysis for Unobserved Confounding

**Step C1**: Apply formal sensitivity analysis to quantify how strong unobserved confounding would need to be to eliminate the adjusted associational difference. Suitable frameworks include:

- **Rosenbaum bounds** (for binary outcomes with matched designs): how large must the odds ratio of differential assignment to exposure be, due to an unobserved confounder, to render the estimated effect statistically insignificant?
- **Imbens-style sensitivity** (or extensions by Cinelli and Hazlett, or Oster): how strongly must an unobserved confounder correlate with both exposure and outcome, relative to the observed covariates, to explain away the residual association?
- **Partial identification bounds** (Manski-style or horizon-specific): under explicit assumptions about the maximum possible treatment effect or the support of the outcome, what is the identified set for the ATT?

**Step C2**: Present results as a sensitivity contour or parameter space: for each assumed degree of selection on unobservables (relative to selection on observables), what is the implied range of possible ATT values?

### Component D: Heterogeneity Description

Describe how the associational difference varies across pre-specified subgroups defined by pre-campaign covariates: past purchase frequency, device type, geographic market, segment, and pre-campaign browsing intensity. These descriptions are associational only but may inform future targeting or experimental design by identifying where the largest raw gaps appear.

### Component E: Predictive Modeling of Conversion

Train predictive models of conversion using pre-campaign covariates and (for exposed users) exposure features. Decompose model performance to understand how much incremental predictive power exposure variables add beyond pre-campaign covariates alone. This is a purely predictive exercise that does not require causal identification and can inform ad-placement and budget-allocation decisions under a prediction-policy framework.

### Component F: Falsification and Placebo Exercises

Conduct diagnostic analyses that would be expected to produce null results if selection on observables alone explained the data:

- **Pre-period "effect" test**: Using pre-campaign conversion data, test whether "would-be exposed" users (defined by characteristics that the algorithm later uses for targeting) had higher conversion rates *before* the campaign began. A large pre-period difference is direct evidence of selection.
- **Future-campaign placebo**: If future campaign data become available, test whether current-campaign "exposure" predicts future-campaign conversion before the future campaign launches. A positive association is evidence of persistent selection.

---

## 10. Why the Design Is Valid (or Why Causal Identification Is Not Credible)

### Why Causal Identification Is Not Credible

The proposed descriptive analysis is valid as a description. It is **not** a causal analysis, and this distinction is the core of the research design.

Causal identification is not credible for three layered reasons:

**First, the assignment mechanism violates ignorability by construction.** The platform's algorithm optimizes ad delivery to maximize some combination of clicks, conversions, and revenue. It uses user-level features — some observed by the researcher, many not — to predict conversion propensity and allocate ads accordingly. The algorithm's objective function aligns with the outcome of interest: it wants to show ads to users who will convert. The resulting selection is not a nuisance to be controlled away; it is the entire purpose of the targeting system.

**Second, the unobserved confounders are systematic, not random.** It is not a matter of missing a few noisy covariates. The platform's internal prediction scores, real-time behavioral signals, auction dynamics, and modeling infrastructure constitute a high-dimensional, optimized representation of conversion propensity that is structurally unavailable to the researcher. Even if the researcher's covariate set is "rich," it is definitionally poorer than the platform's own targeting apparatus.

**Third, no design-based solution is available.** Without randomization, an instrument, a discontinuity, or a timing shock, there is no source of variation in exposure that is independent of potential outcomes. Every empirical approach that might be applied — matching, weighting, regression adjustment, difference-in-differences, synthetic control — reduces to the unconfoundedness assumption in this setting. That assumption is not plausible.

### Why the Descriptive Analysis Is Valid

The descriptive analysis is valid because it makes no causal claims. It reports:
- Raw differences in outcomes between groups.
- How much of those differences observable covariates can account for.
- How sensitive the residual differences are to hypothetical unobserved confounding.
- How exposure and outcome variables covary across subgroups and over time.

These are statistical descriptions of the joint distribution of (*D, Y, X*). They are reliably computed from the data and require no causal assumptions beyond measurement validity.

---

## 11. Required Assumptions

### For the Descriptive Analysis (Defensible)

| # | Assumption | Plausibility |
|---|---|---|
| A1 | Exposure and outcome are measured without systematic error that differs by group. | Moderately plausible. Cross-device tracking, cookie loss, and attribution window mismatches may introduce measurement error. Sensitivity to attribution rules should be checked. |
| A2 | The eligible population is correctly defined and consistently observed. | Plausible if platform eligibility rules are documented. |
| A3 | Covariates are measured before or independently of the campaign exposure decision (temporal ordering preserved). | Plausible for pre-campaign covariates; potentially violated for contemporaneous behavioral covariates. |
| A4 | The functional form of covariate-adjustment models is sufficiently flexible to capture observable confounding. | Addressable through nonparametric or machine learning methods with honest performance evaluation (cross-validation). |

### For Causal Interpretation (Not Defensible)

| # | Assumption | Plausibility |
|---|---|---|
| C1 | Unconfoundedness: (Y(0), Y(1)) ⟂ D \| X. | **Not plausible.** Algorithmic targeting uses unobserved features. |
| C2 | Overlap (common support): 0 < P(D=1 \| X) < 1 for all X. | **May be violated.** The platform may deterministically exclude some user types from exposure. |
| C3 | SUTVA: No interference between users. | **Likely violated.** Cross-channel advertising and general campaign effects mean unexposed users are partially treated. |
| C4 | Correct model specification for the relationship between X and Y(0). | **Cannot be verified** and unlikely to hold exactly. |

---

## 12. Statistical Model or Analysis Equation

### Primary Associational Model

For binary conversion outcome *Y_i*, estimate via logistic regression:

> *logit(P(Y_i = 1)) = α + β · D_i + X_i' · γ + ε_i*

where *D_i* is the binary exposure indicator, *X_i* is the vector of pre-campaign covariates (browsing history, past purchases, device, geography, segment, platform scores), and *β* is the **associational log-odds ratio** — not a causal parameter.

### Doubly Robust Estimation

For a more flexible associational estimate:

> *Δ̂_DR = (1/N) Σ_i [ (D_i · (Y_i − μ̂₀(X_i))) / π̂(X_i) − ((1−D_i) · (Y_i − μ̂₀(X_i))) / (1−π̂(X_i)) + μ̂₁(X_i) − μ̂₀(X_i) ]*

where *π̂(X_i)* is the estimated propensity score, *μ̂_d(X_i)* is the estimated outcome regression for treatment status *d*, and both are estimated using flexible methods (gradient-boosted trees, neural nets with cross-fitting). Δ̂_DR has the property of being consistent for the associational parameter if *either* the propensity model *or* the outcome model is correctly specified, but it remains associational — not causal — because neither model addresses unobserved confounding.

### Sensitivity Model

Following the partial R² parameterization (in the spirit of Cinelli-Hazlett or Oster):

Define *R²_{Y∼D|X}* as the partial R² from regressing *Y* on *D* after controlling for *X*, and *R²_{D∼Z|X}* as the partial R² from regressing *D* on an unobserved confounder *Z* after controlling for *X*. For an unobserved confounder to reduce the estimated associational difference to zero, the product of these partial R² values must equal approximately the current residual variation. The sensitivity analysis reports, for a grid of possible (*R²_{Y∼Z|X,D}*, *R²_{D∼Z|X}*) values, the implied bias-adjusted treatment effect:

> *β_adj(δ, R²_{D∼Z|X}) = β̂ − δ · (bias multiplier)*

where *δ* parameterizes the strength of confounding and the bias multiplier is derived from the observed covariate relationships.

### Bounding Model (Manski-style Partial Identification)

Under the weakest assumptions (bounded outcome: Y ∈ [0, 1]):

> *E[Y(1) − Y(0) | D = 1] ∈ [E[Y|D=1] − 1, E[Y|D=1] − 0]*

which is vacuous. Under the monotone treatment response assumption (Y(1) ≥ Y(0)):

> *E[Y(1) − Y(0) | D = 1] ∈ [0, E[Y|D=1]]*

which provides an upper bound (the observed mean among exposed) but no useful lower bound beyond zero. Tighter bounds require stronger assumptions that may themselves be controversial.

---

## 13. Robustness, Placebo, Falsification Checks, and Diagnostic Tests

### Falsification Test 1: Pre-Campaign Outcome Comparison

Using pre-campaign conversion data (from a period before the campaign launched), define a pseudo-treatment indicator *D̃_i* that classifies users as "would be exposed" based on the characteristics that predict actual campaign exposure. Test whether:

> *H₀: E[Y_pre | D̃ = 1] = E[Y_pre | D̃ = 0]*

A significant difference in pre-period outcomes between would-be-exposed and would-be-unexposed users is **direct evidence of selection**. If the raw difference in the campaign period is similar in magnitude to the pre-period difference, this suggests little to no incremental campaign effect beyond baseline differences.

### Falsification Test 2: Stable Coefficient Comparison

Following coefficient stability approaches (Altonji-Elder-Taber, Oster), compare *β̂* (the coefficient on *D*) from a sparse model (few controls) to *β̂* from a rich model (many controls). Compute:

> *δ̂ = β̂_rich / (β̂_sparse − β̂_rich)*

where δ̂ approximates the degree of selection on unobservables relative to selection on observables that would be required to drive *β̂_rich* to zero. If δ̂ is small (e.g., δ̂ < 1), the associational difference is highly sensitive to modest unobserved confounding and would not survive even weak selection on unobservables.

### Robustness Check 1: Alternative Exposure Definitions

Re-estimate all analyses using:
- Exposure as continuous impression count (linear and binned).
- Exposure as recency-weighted cumulative measure.
- Exposure thresholded at different minimum impression counts (1+, 3+, 5+ impressions).
- Click-based definitions: clickers vs. non-clickers, impression-only vs. click-through.

Consistency in the pattern of associational differences across definitions supports descriptive robustness; large variations reveal the importance of how exposure is operationalized.

### Robustness Check 2: Alternative Attribution Windows

Vary the conversion attribution window (e.g., 1-day, 7-day, 14-day, 30-day post-impression). Longer windows capture more conversions but introduce more contamination from other marketing activities.

### Robustness Check 3: Alternative Estimators

Compare associational estimates across:
- Logistic regression with linear controls.
- Propensity score matching (1:1 nearest-neighbor, caliper matching).
- IPW with stabilized weights and trimming.
- Doubly robust AIPW.
- Machine learning (gradient boosting, causal forest).

Wide variation across estimators with similar covariates suggests model dependence; report the range.

### Robustness Check 4: Sub-Sample Stability

Exclude users with extreme propensity scores (e.g., trim top and bottom 1%, 5%, 10% of the estimated propensity score distribution) to assess sensitivity to lack of common support.

### Diagnostic Test: Negative Control Outcomes

Identify outcomes that should not be affected by the campaign (e.g., conversions in a product category unrelated to the advertised product, or platform actions that the ad content should not influence). A significant "effect" on negative control outcomes is evidence of unobserved confounding rather than a genuine campaign effect.

---

## 14. Heterogeneity Analysis (If Supportable)

Heterogeneity analysis is supportable as a descriptive exercise. All findings are associational, not causal, but may still be informative for campaign design and future experimentation.

### Pre-Specified Subgroup Dimensions

| Dimension | Rationale | Causal Interpretability |
|---|---|---|
| Pre-campaign purchase frequency (terciles) | Heavy buyers may have less room for incremental lift | None; selection on purchase frequency is confounded with ad delivery |
| Device type (mobile, desktop, tablet) | Different browsing contexts, different conversion funnels | None; device is a targeting dimension |
| Geographic market | Market-level variation in brand awareness and competition | None; markets differ in platform penetration and baseline conversion rates |
| Customer segment (new vs. returning) | Returning users may have different baseline conversion propensity | None; segment is a targeting dimension |
| Time of campaign (early vs. late) | Campaign wear-out or saturation effects | Descriptively informative but confounded by who enters the eligible pool over time |
| Pre-campaign browsing intensity | Proxy for baseline platform engagement | None; engagement drives both exposure probability and conversion |

### Analytical Approach

For each subgroup *g*, estimate:

> *Δ̂_g = E[Y | D=1, G=g, X] − E[Y | D=0, G=g, X]*

using the doubly robust estimator described above, applied to the subgroup data. Report subgroup-specific Δ̂_g as descriptive statistics only, with appropriate multiple-comparison adjustments if formal testing is conducted. Do not interpret differences in Δ̂_g across subgroups as differences in causal effects — they reflect differences in both selection patterns and (possibly) treatment effects, with no way to separate the two.

---

## 15. Measurement, Compliance, Missingness, Spillover, and Implementation Limits

### Measurement

- **Cross-device tracking failure**: A user exposed on a mobile device who converts on a desktop may appear unexposed (if identifiers are not linked) or may have the conversion attributed incorrectly. This attenuates the associational difference between exposed and unexposed users.
- **Attribution window arbitrariness**: The choice of post-exposure conversion window is a business convention, not a statistical principle. Short windows miss delayed conversions; long windows capture organic conversions unrelated to the ad.
- **Impression viewability**: An "impression" may be logged even if the ad was below the fold, rendered off-screen, or served to a bot. This inflates the exposed group with effectively-unexposed users and biases associational differences toward zero.
- **Identifier loss**: Cookie deletion, app reinstallation, or logged-out browsing breaks the link between exposure and conversion events, creating false negatives in both directions.

### Compliance

The concept of compliance is not directly applicable in this setting because assignment is not experimental. There is no "assigned-to-exposure" status distinct from "actual-exposure" status. However, the analogue is: users targeted and bid on by the platform may not actually see the ad (ad was below the fold, page loaded but user scrolled past, ad-blocker active). This creates a distinction between "won the auction" and "actually viewed" that is analogous to non-compliance but not separately observed.

### Missingness

- **Outcome missingness**: Users who convert through channels not tracked by the platform (phone orders, in-store purchases, competitor platform purchases) appear as non-converters. If exposed and unexposed users differ in their propensity to convert through untracked channels, this biases associational estimates.
- **Covariate missingness**: Pre-campaign covariates may be missing for new users or users with limited platform history. If new users are differentially targeted (e.g., prospecting campaigns), excluding them or imputing their covariates introduces selection bias or measurement error.
- **Attrition from the eligible pool**: Users may leave the platform, switch devices, or become inactive during the campaign period. If attrition is differential by exposure status, the observed comparison is on a selected sample.

### Spillover and Interference

- **Cross-platform spillover**: The advertiser likely runs campaigns on multiple platforms simultaneously. An "unexposed" user on this platform may have seen the same campaign elsewhere, making them effectively treated. This biases the associational difference toward zero.
- **Within-platform network effects**: Social features, recommendation systems, or shared-device usage may cause one user's exposure to affect another user's behavior. This violates SUTVA and is not measurable with the available data.
- **Market saturation**: In small geographic markets or narrow segments, the campaign may reach a high enough fraction of the target audience that the "unexposed" group is too small or too unusual to serve as a comparison.

### Implementation Limits

- **Propensity score estimation**: With high-dimensional covariates and nonlinear selection into exposure, propensity score models may be poorly calibrated, especially in tails. Poor overlap (some user types nearly always or never exposed) limits the population over which associational comparisons can be made.
- **Multiple testing**: With many outcomes, subgroup cuts, and exposure definitions, naive significance testing will overstate the precision of associational estimates. Corrections for multiple comparisons should be applied if formal hypothesis tests are reported.
- **Computational scale**: User-level datasets from large platforms may contain millions of observations. Flexible ML-based estimators require careful implementation for computational feasibility, honest inference (sample splitting, cross-fitting), and avoidance of overfitting.

---

## 16. Failure Modes and Alternative Explanations

### Failure Mode 1: The Adjusted Difference Reflects Residual Selection, Not Causal Effect

The most likely failure mode is that any statistically significant adjusted associational difference reflects *selection on unobservables* rather than a genuine ad effect. The platform's targeting algorithm uses richer, more timely, and more directly conversion-predictive features than the researcher observes. Covariate adjustment can reduce but not eliminate the gap. The "adjusted lift" is an upper bound on what residual selection could explain.

**Alternative explanation**: The entire adjusted difference is attributable to unobserved differences in purchase intent between users the algorithm chooses to show ads to and users it does not.

### Failure Mode 2: The Adjusted Difference Is Attenuated by Measurement Error

Poor impression tracking (non-viewable impressions, bot traffic, ad-blockers) dilutes the treatment group with effectively-unexposed users. Poor conversion tracking (cross-device, untracked channels) dilutes the outcome. The combination can attenuate the adjusted difference downward, potentially masking a genuine effect.

**Alternative explanation**: A null or small adjusted difference may reflect measurement error rather than absence of a causal effect.

### Failure Mode 3: Click-Based Conditioning Introduces Collider Bias

If the analysis conditions on clicking (e.g., comparing clickers to non-clickers, or including clicks as a control), this introduces collider stratification bias: clicking is a post-exposure variable affected by both exposure and unobserved user interest. Conditioning on it opens a non-causal path between exposure and conversion.

### Failure Mode 4: Time-Varying Confounding

Users' browsing and purchase behavior during the campaign period is affected by ad exposure. Including contemporaneous covariates as "controls" introduces post-treatment bias. Excluding them leaves time-varying confounders unaddressed.

### Failure Mode 5: Reverse Causation

High conversion intent causes ad exposure (through real-time bidding on high-intent signals), not the reverse. The associational difference could be entirely driven by the platform's success at identifying high-intent users and serving them ads, with zero incremental effect of the ads themselves.

### Failure Mode 6: Simpson's Paradox Through Aggregation

Aggregating across markets, devices, or segments with different baseline conversion rates and different exposure probabilities can produce an aggregate associational difference that differs in sign or magnitude from within-group associational differences.

---

## 17. What Cannot Be Claimed

Based on the data, variation sources, and identification constraints described in this packet, the following claims **cannot** be made:

1. **"The campaign caused a X% lift in conversions."** No causal claim about the effect of ad exposure on conversion is supportable.

2. **"The incremental ROAS (return on ad spend) is Y."** ROAS requires a causal estimate of incremental conversions attributable to ad spend. Without a causal effect estimate, ROAS is not computable.

3. **"Exposed users converted at a higher rate because of the ads."** The observed difference is a mixture of causal effect and selection, with no way to decompose them.

4. **"Adding more controls eliminates selection bias."** Rich controls reduce observable imbalance but cannot address selection on unobservables that is inherent in algorithmic targeting.

5. **"The propensity-score-weighted estimate is the causal effect."** Propensity score methods estimate the associational parameter under the unconfoundedness assumption, which is not credible here. They are useful descriptive tools, not causal identification strategies.

6. **"Frequency of exposure has a causal dose-response relationship with conversion."** Exposure frequency is endogenous — users who see more impressions are systematically different from those who see fewer — and no instrument or exogenous shifter of frequency is available.

7. **"Clicks on the ad cause conversion."** Clicks are themselves endogenous outcomes of user interest and ad creative quality, not randomly assigned.

---

## 18. Additional Data Needed

To move from descriptive associational analysis to credible causal estimation, the following data or design elements would be needed, listed in order of increasing feasibility and decreasing idealness:

### Tier 1: Gold Standard — Randomized Controlled Trial

- **Randomized holdout**: A randomly assigned subset of the eligible audience is withheld from seeing the campaign. The difference in conversion rates between the exposed group and the holdout group identifies the intent-to-treat effect.
- **Ghost ads**: The platform serves "ghost" impressions to the control group — logging that an ad *would have been served* without actually rendering it — to measure the counterfactual conversion rate among users the algorithm wanted to target.
- **Platform cooperation**: The experiment must be implemented at the ad-delivery infrastructure level, not by the researcher after the fact.

### Tier 2: Quasi-Experimental Variation

- **An instrument**: A variable that shifts exposure probability without directly affecting conversion. Candidates could include: randomized ad creative (A/B test that affects engagement but not baseline interest), budget exhaustion that creates arbitrary timing variation in who sees ads, or platform-level algorithm A/B tests that change delivery rules without changing user composition.
- **A discontinuity**: A sharp threshold in the targeting or bidding process — e.g., a minimum predicted conversion probability to qualify for bidding, or a geographic boundary for campaign delivery — that creates a local randomized comparison at the threshold.
- **A timing shock**: A staggered campaign rollout by geography or segment (with randomness in rollout timing), an unexpected platform policy change that affects ad delivery, or an event that exogenously interrupts campaign delivery for some users.

### Tier 3: Improved Observational Data

- **Platform-internal targeting scores**: Access to the exact prediction scores and features used by the platform's delivery algorithm, which would expand the observable covariate set to include the actual selection variables.
- **Multi-platform attribution**: Linked user-level data across all platforms where the advertiser runs campaigns, to identify users truly unexposed to any campaign touchpoint.
- **Deterministic cross-device identity resolution**: Reliable linkage of user identities across devices to eliminate measurement error from cross-device tracking failure.
- **Longitudinal pre-campaign data with extensive history**: Multiple pre-campaign periods to establish baseline trends, test for pre-existing differences, and potentially construct within-user comparisons if users switch exposure status over multiple campaigns.
- **Bid-level auction data**: Logs of the platform's internal auctions — including bids, predicted conversion rates, and win/loss outcomes — to understand the assignment mechanism.

---

## 19. Threat-Response Table (Explicitly Requested)

| Threat | Description | Response Strategy | Residual Risk |
|---|---|---|---|
| **Selection on unobservables** | Algorithmic targeting uses unobserved user features that predict conversion | Sensitivity analysis (Rosenbaum, Oster, Cinelli-Hazlett); explicit bounding under stated assumptions about maximum confounding; honesty about non-causal interpretation | The analysis cannot rule out that the entire associational difference is selection. Sensitivity analysis tells us how strong confounding must be, not whether it exists. |
| **Lack of common support** | Some user types are deterministically always or never exposed | Trimming and overlap diagnostics; restrict analysis to region of common support; report trimmed sample size and characteristics | The trimmed sample may not represent the population of interest; external validity is compromised. |
| **Cross-platform spillover** | Unexposed users on this platform may see ads elsewhere | If multi-platform data are available, condition on other-platform exposure; if not, acknowledge contamination as a bias toward zero | Cannot be addressed without multi-platform data. |
| **Measurement error in exposure** | Non-viewable impressions, bots, ad-blockers inflate "exposed" group | Sensitivity to impression definition; if viewability data exist, restrict to viewable impressions; report results under alternative definitions | Measurement error remains for unmeasured non-viewability. |
| **Measurement error in outcome** | Cross-device conversion, untracked channels, attribution window mismatch | Vary attribution windows; if identity resolution data exist, link devices; report outcome sensitivity | Outcome measurement error cannot be fully corrected without perfect identity resolution and omni-channel tracking. |
| **Post-treatment bias** | Controlling for campaign-period covariates or clicks introduces collider bias | Restrict covariates to pre-campaign period only; do not condition on clicks for the main associational estimate; analyze clicking as a separate descriptive outcome | Time-varying confounding during the campaign remains unaddressed. |
| **SUTVA violation** | Network effects, social influence, shared devices | Acknowledge; if social graph data exist, check for clustering of outcomes; report limitations | Cannot be credibly addressed without experimental variation in saturation levels. |
| **Model dependence** | Associational estimates vary with model specification | Report results across a range of estimators (logistic, IPW, AIPW, ML); transparently present estimator variation | The "true" associational parameter is not identified; model dependence reveals epistemic uncertainty. |
| **Multiple comparisons** | Many outcomes, subgroups, and exposure definitions inflate false positive rates | Apply Bonferroni or Benjamini-Hochberg correction if hypothesis tests are reported; pre-register primary specifications | Pre-registration requires foresight; post-hoc corrections are conservative. |
| **Temporal confounding** | Seasonality, concurrent marketing, platform changes coincide with campaign | Compare to pre-campaign and post-campaign periods; test for discontinuities at campaign boundaries | Cannot separate campaign effect from coincident shocks without control group. |

---

## 20. Claim-Evidence Table

| # | Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|---|
| 1 | Exposed users have a higher raw conversion rate than unexposed users. | Cross-tabulation of D and Y from campaign logs. | Descriptive | High (directly observed) | No significant raw difference in conversion rates between groups. |
| 2 | Exposed and unexposed users differ systematically on observable pre-campaign covariates. | Standardized mean differences on X between D=1 and D=0 groups. | Descriptive | High (directly computed) | All SMDs are small (< 0.1) across all covariates. |
| 3 | Observable covariate differences account for part, but not necessarily all, of the raw conversion gap. | Comparison of unadjusted and covariate-adjusted associational differences; coefficient stability analysis. | Descriptive | High for "part"; indeterminate for "not all" | Adjusted difference equals zero and remains zero across all reasonable covariate sets and estimators. |
| 4 | The adjusted associational difference could be entirely explained by unobserved confounding of plausible magnitude. | Sensitivity analysis showing δ required to eliminate the adjusted difference, compared to δ observed when adding covariates. | Bound / Sensitivity | Depends on δ magnitude | Sensitivity analysis shows that implausibly strong unobserved confounding would be required to explain away the adjusted difference (δ >> 1). Even then, causal interpretation requires additional assumptions not met here. |
| 5 | The campaign is associated with larger conversion differences in some subgroups than others. | Subgroup-specific adjusted associational estimates. | Descriptive | Moderate (multiple comparisons) | Uniform associational differences across all pre-specified subgroups. |
| 6 | Pre-campaign conversion rates differ between would-be-exposed and would-be-unexposed users. | Pre-period pseudo-exposure classification based on targeting correlates; comparison of pre-period outcomes. | Diagnostic | High (if pre-period data exist) | No pre-period difference in conversion rates between groups defined by exposure-relevant characteristics. |
| 7 | The associational difference is not caused solely by the ad; algorithmic selection is a substantial contributor. | Pre-period outcome differences; coefficient sensitivity to control addition; documented targeting mechanics; sensitivity analysis. | Interpretive / Inferential | High (structural, not statistical) | A randomized experiment showing identical or larger treatment effects than the observational associational difference. |
| 8 | The data do not support a causal claim about ad lift. | Absence of random assignment, instrument, discontinuity, timing shock, or any other quasi-experimental variation; non-ignorable assignment mechanism by design. | Logical / Design-based | Very high (structural feature of the data-generating process) | Discovery of a valid instrument, discontinuity, or natural experiment in the data. |

---

## Conclusion

The data described in this packet — while rich in covariates, outcomes, and business relevance — do not support credible causal identification of advertising effectiveness. The platform's algorithmic targeting creates a fundamental selection problem that no amount of covariate adjustment can solve. The strongest defensible empirical contribution is a transparent descriptive and predictive analysis, accompanied by formal sensitivity analysis that quantifies how strong unobserved confounding would need to be to explain the observed associational differences. This is analytically honest, practically useful (it documents the magnitude of the targeting-selection gap and identifies where experimental investment would be most valuable), and avoids the more consequential error of presenting confounded associations as causal lift estimates that could misinform budget allocation, campaign optimization, and strategic decision-making.

The most productive next step is to design and implement a randomized holdout experiment — ideally using ghost-ad methodology — to obtain the credible causal estimates that the observational data cannot provide.

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260527_225838_98725_14
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_225838_98725_14.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_225838_98725_14.trajectory.jsonl

## Operator Notes

- duration_ms: 337807
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
