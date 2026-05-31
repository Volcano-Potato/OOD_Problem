# Raw Agent Run Log

- `run_id`: RUN_20260527_235916_28_openclaw_deepseekv4pro_isolated
- `case_id`: C019
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
- `timestamp`: 2026-05-27T23:59:16+0800
- `input_file`: benchmark/cases/C019_in_store_travel_distance/agent_task_level2.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: In-Store Travel Distance and Unplanned Spending

---

## 1. Executive Summary

This design addresses whether longer in-store travel causes higher unplanned spending. The central empirical challenge is that route length is not randomly assigned: shoppers with larger planned baskets, more complex missions, or greater openness to unplanned purchases may endogenously select into longer routes. I propose that **credible causal identification is possible only under an experimental design where additional travel distance is exogenously induced**, either through randomized path-inducing promotions or through randomized re-routing of store layout features. Absent such randomization, the strongest defensible analysis is a descriptive decomposition that separates the observed route–unplanned-spending association into (a) a pre-trip mission channel, (b) a reverse-causality channel (unplanned purchases extending the route), and (c) a residual exposure channel, using the rich pre-trip planned-basket data to bound the role of selection.

The design further analyzes promotion strategies that redirect shoppers to off-route categories by randomizing promotion distance from the planned route, enabling estimation of how incremental detour distance affects redemption and incremental unplanned spending.

---

## 2. Research Question

Does increasing the distance a shopper travels through a physical retail store cause an increase in unplanned spending? A secondary question is whether path-inducing promotions — offers that intentionally redirect shoppers toward categories off their planned route — can increase unplanned purchases, and how the distance of the promotion from the planned route moderates this effect.

---

## 3. Target Estimand or Strongest Defensible Estimand

**Three distinct estimands are relevant**, and the design must be explicit about which it targets:

### 3.1 Causal estimand (requires experimental variation)

The Average Treatment Effect (ATE) of exogenously increasing in-store travel distance by Δ meters on unplanned spending:

$$ATE(\Delta) = E[Y_i(D_i + \Delta) - Y_i(D_i)]$$

where $D_i$ is the shopper's travel distance in the absence of intervention and $Y_i$ is unplanned spending. This estimand is identified only under randomized assignment of an instrument that shifts travel distance independently of shopper and trip characteristics.

### 3.2 Reduced-form causal estimand (preferred when route length cannot be randomized directly)

The Intention-to-Treat (ITT) effect of assignment to a path-inducing promotion on unplanned spending. This is the strongest estimand that can be credibly identified without the strong exclusion restriction that promotions affect spending *only* through route length.

### 3.3 Strongest descriptive estimand (when causal identification is not possible)

The partial association between observed route length and unplanned spending, conditional on a rich set of pre-trip planned-basket and mission covariates. This is a descriptive estimand, not a causal one, but can be decomposed into components attributable to (a) pre-trip selection, (b) simultaneous determination, and (c) a residual that is closest to (but not equal to) a route-exposure channel.

---

## 4. Treatment or Exposure and Main Outcomes

### Treatment/Exposure Variables

| Variable | Type | Description |
|---|---|---|
| $R_i$ | Observed exposure | Actual in-store route length (meters), measured during the trip |
| $Z_i$ | Randomized assignment | Indicator: shopper $i$ is assigned to receive a path-inducing promotion |
| $Dist_i$ | Randomized intensity | Distance (meters) of the promoted category from the shopper's pre-trip planned route, for those assigned $Z_i = 1$ |

### Main Outcomes

| Variable | Definition |
|---|---|
| $Y_i^{unplanned}$ | Unplanned spending = total checkout spending − pre-trip planned spending (in currency units) |
| $Y_i^{unplanned\_cats}$ | Number of product categories purchased that were not in the planned basket |

---

## 5. Data Structure Summary

The design operates on a single-trip cross-section with four measurement stages:

1. **Pre-trip (entry):** Planned basket composition, expected expenditure, shopping mission type, budget slack, store familiarity, demographics.
2. **In-trip (exposure):** Shopper movement tracking yielding route length and path coordinates.
3. **Checkout (outcome):** Final basket composition and total spending.
4. **Optional experimental stage:** Randomized assignment of path-inducing promotions to a subset of trips, with promotion distance from planned route computed from the pre-trip planned basket and store layout.

The unit of observation is the shopping trip. If repeat trips per shopper exist, shopper-level clustering is recommended. Route measurement may be noisy or missing for some trips; checkout linkage may also be incomplete.

---

## 6. Relevant Causal Mechanisms

The observed correlation between route length and unplanned spending can arise through at least four distinct channels:

| Channel | Direction | Mechanism |
|---|---|---|
| **A. Product exposure** | Route → Spending | Longer travel mechanically exposes shoppers to more product displays, category cues, and reminders, triggering unplanned purchases |
| **B. Mission selection** | Confounding | Shoppers with larger planned missions (more categories, larger budgets) must travel farther *and* may have more/less budget slack for unplanned spending |
| **C. Reverse causality** | Spending → Route | Making an unplanned purchase sends the shopper to an additional aisle or section, mechanically extending observed route length |
| **D. Environmental confounds** | Confounding | Congestion, endcap displays, store familiarity, and shopping companions affect both route choices and spending propensity |

Channels B and C make the observed association between route length and unplanned spending uninterpretable as a causal effect of travel on spending, even after including observable controls. Channel D introduces additional omitted-variable bias.

---

## 7. Main Identification Challenge

The core identification problem is that route length $R_i$ is endogenously determined within the shopping trip by the same factors that drive unplanned spending. Formally:

$$Y_i = \beta R_i + X_i\gamma + \varepsilon_i$$
$$R_i = X_i\delta + \eta_i$$

where $Cov(\varepsilon_i, \eta_i) \neq 0$ because unobserved trip-level factors (impulsivity, time pressure, store familiarity, actual mission complexity beyond what is recorded) drive both route length and unplanned spending. Moreover, $Y_i$ can also *cause* $R_i$ (reverse causality), so even an instrument that shifts $R_i$ exogenously must be timed to precede the shopping trip to avoid contaminating the exclusion restriction.

The pre-trip planned-basket data provide rich controls for Channel B (mission selection), but they do not resolve Channels C and D. Controlling for planned basket does not break the simultaneity between in-trip route decisions and in-trip unplanned purchases.

---

## 8. Whether Credible Causal Identification Is Possible

**Credible causal identification of the effect of route length on unplanned spending is possible only under an experimental design where additional travel distance is exogenously induced.** Without experimental variation, the richest possible analysis is descriptive: decomposing the observed association using pre-trip covariates to bound the selection component, but never recovering a clean causal effect of route length itself.

For the **secondary question on path-inducing promotions**, credible causal identification is possible through randomized promotion assignment, yielding the ITT effect of promotion assignment on unplanned spending. This is a different estimand (effect of a promotional intervention, not effect of route length per se) but addresses the retailer's operational question.

---

## 9. Proposed Empirical Design

### 9.1 Descriptive baseline analysis (always feasible)

**Step 1: Mission-control decomposition.** Regress unplanned spending on route length, controlling for the richest available pre-trip covariates:

$$Y_i^{unplanned} = \alpha + \beta R_i + \mathbf{X}_i^{pre}\gamma + \varepsilon_i$$

where $\mathbf{X}_i^{pre}$ includes planned basket size, planned categories count, expected expenditure, budget slack, trip mission indicators, store familiarity, day-of-week, time-of-day, and demographics. The coefficient $\hat{\beta}$ is a partial association, not a causal effect.

**Step 2: Bounding selection.** Compare $\hat{\beta}$ from the uncontrolled regression to the controlled regression. The difference is attributable to observable mission selection (Channel B). The residual $\hat{\beta}$ after controls reflects a combination of Channels A, C, and D plus any remaining unobserved selection. Report a Gelbach or Oster-style decomposition to quantify how much of the unconditional association each covariate group explains.

**Step 3: Reverse-causality bounding.** Construct an adjusted route length $R_i^{adj}$ that subtracts the minimum additional distance required to reach the categories where unplanned purchases were actually made. Regress unplanned spending on $R_i^{adj}$ (with pre-trip controls) and compare to the coefficient on $R_i$. The attenuation from $R_i$ to $R_i^{adj}$ bounds the mechanical reverse-causality contribution (Channel C).

### 9.2 Experimental design for the route-length effect (preferred, if feasible)

**Intervention:** Randomly assign shoppers at store entry to one of several treatment arms that vary the amount of induced additional travel:

- **Control:** No route intervention. Shoppers follow their natural path.
- **Low-detour arm:** Shoppers receive an incentivized prompt (e.g., a coupon or loyalty-point bonus) to visit a category that requires a small detour (e.g., +Δ₁ meters) from their planned route.
- **High-detour arm:** Shoppers receive an incentivized prompt requiring a larger detour (+Δ₂ meters).

**Key design elements:**

1. **Randomization at entry**, after pre-trip planned basket is elicited but before the shopper begins navigating the store. This ensures $Z_i \perp (X_i^{pre}, \varepsilon_i, \eta_i)$.

2. **Route-length measurement for all arms**, including control, to compute both ITT and IV estimates.

3. **The IV estimand** uses randomized arm assignment $Z_i$ as an instrument for actual route length $R_i$:
   - **First stage:** $R_i = \pi_0 + \pi_1 Z_i + \mathbf{X}_i^{pre}\pi_2 + \nu_i$
   - **Second stage:** $Y_i^{unplanned} = \beta_{IV} \hat{R}_i + \mathbf{X}_i^{pre}\gamma + \varepsilon_i$
   - $\beta_{IV}$ estimates the Local Average Treatment Effect (LATE) for compliers: shoppers whose route length changes in response to the promotion assignment.

4. **Critical:** The exclusion restriction requires that the promotion affects unplanned spending *only* through its effect on route length. This is unlikely to hold perfectly, because the promotion itself may stimulate unplanned spending at the promoted category independent of the additional travel. The design therefore **prioritizes the ITT as the more defensible estimand** and treats the IV as exploratory, with an explicit discussion of exclusion-restriction violations.

### 9.3 Experimental design for path-inducing promotions (primary interest)

**Design:** Randomize shoppers to receive a promotion for a category that is (a) on their planned route, (b) a short detour from their planned route (+Δ₁ meters), or (c) a long detour from their planned route (+Δ₂ meters). The promotion offer (coupon value, discount rate) is held constant across arms, isolating the effect of detour distance.

**Estimand:** $E[Y_i^{unplanned} | Dist_i = d] - E[Y_i^{unplanned} | Dist_i = 0]$, for $d \in \{\Delta_1, \Delta_2\}$, estimated via:

$$Y_i^{unplanned} = \alpha + \beta_1 \cdot I(Dist_i = \Delta_1) + \beta_2 \cdot I(Dist_i = \Delta_2) + \mathbf{X}_i^{pre}\gamma + \varepsilon_i$$

This yields the causal effect of assigning a promotion at varying detour distances on unplanned spending. The *distance gradient* $\hat{\beta}_2 - \hat{\beta}_1$ estimates how incremental detour distance affects the outcome.

**Compliance analysis:** Not all assigned shoppers will redeem the promotion or follow the detour. The ITT captures the policy-relevant effect of *offering* the promotion. The treatment effect on the treated (TOT) can be estimated via IV using assignment as an instrument for actual detour behavior, under a weaker exclusion restriction (promotion assignment affects spending *only* through detour-taking), which is more defensible than the route-length IV above.

---

## 10. Why the Design Is Valid

### Descriptive design validity

The decomposition approach is valid because it transparently separates the observed association into components attributable to observable selection (planned basket and mission controls), mechanical reverse causality (subtracting distance to unplanned-purchase locations), and a residual. It makes no claim beyond what the data support and explicitly acknowledges the sources of remaining endogeneity.

### Experimental design validity

Randomization of promotion assignment at store entry ensures that assignment is independent of all pre-trip and in-trip confounders. The ITT on unplanned spending is identified under the weakest assumption (random assignment only). The dose-response design (varying detour distance) identifies the causal effect of promotion distance on outcomes without requiring an exclusion restriction for route length.

### Why the route-length IV is supplementary, not primary

The route-length IV requires the exclusion restriction that promotions affect unplanned spending *only* through route length, which is implausible: a promotion for cereal may trigger an unplanned cereal purchase because of the discount, not because the shopper walked an extra 30 meters. The design therefore treats the IV as an exploratory sensitivity analysis, bounded by the ITT and by a monotonicity assumption (promotions weakly increase route length for all shoppers).

---

## 11. Required Assumptions

### For the descriptive decomposition (always required)

1. **No unobserved route–spending confounders beyond pre-trip covariates, or acknowledged bounded bias.** The decomposition is transparent about residual endogeneity.
2. **Pre-trip planned basket is measured without systematic error.** If shoppers misreport plans, the unplanned-spending measure is misclassified.
3. **Route measurement is reasonably accurate.** Systematic measurement error in route length (e.g., GPS drift indoors) attenuates or biases estimates depending on the error structure.
4. **The reverse-causality adjustment using distance to unplanned-purchase locations is a valid lower bound.**

### For the randomized promotion ITT

1. **Successful randomization:** Assignment is independent of potential outcomes.
2. **Stable Unit Treatment Value Assumption (SUTVA):** One shopper's promotion assignment does not affect another shopper's outcomes. Plausible in a physical retail setting if promotions are delivered privately (e.g., via loyalty app).
3. **No selective attrition:** Shoppers assigned to promotions are no more likely to have missing route or checkout data than controls.

### For the route-length IV (exploratory only)

4. **Relevance:** Promotion assignment significantly affects route length.
5. **Exclusion restriction:** Promotion assignment affects unplanned spending only through route length. Likely violated; results are interpreted as upper bounds under specific sign assumptions.
6. **Monotonicity:** No shoppers reduce route length in response to promotion assignment (no defiers).

---

## 12. Statistical Model or Analysis Equation

### Primary specification: ITT of randomized promotion distance

$$Y_i^{unplanned} = \alpha + \sum_{k=1}^{K} \beta_k \cdot I(Dist_i = d_k) + \mathbf{X}_i^{pre}\gamma + \varepsilon_i$$

where $d_k$ are the randomized detour-distance levels (including $d=0$ as the on-route or no-promotion control). Standard errors are clustered at the shopper level if repeat trips exist; otherwise, heteroskedasticity-robust standard errors are used.

### Secondary specification: descriptive route-length decomposition

$$Y_i^{unplanned} = \alpha + \beta R_i + \mathbf{X}_i^{pre}\gamma + \varepsilon_i$$

reported alongside the same specification without $\mathbf{X}_i^{pre}$ (uncontrolled) and with $R_i^{adj}$ (reverse-causality-adjusted route length).

### Exploratory IV specification

**First stage:**
$$R_i = \pi_0 + \sum_{k=1}^{K} \pi_k \cdot I(Dist_i = d_k) + \mathbf{X}_i^{pre}\phi + \nu_i$$

**Second stage:**
$$Y_i^{unplanned} = \beta_{IV} \hat{R}_i + \mathbf{X}_i^{pre}\gamma + \varepsilon_i$$

Report the first-stage F-statistic (threshold > 10 for weak-instrument concern), the Anderson-Rubin confidence set (robust to weak instruments), and a formal discussion of exclusion-restriction plausibility.

### Mediation analysis for promotion mechanisms

$$M_i = \alpha_M + \sum_k \delta_k \cdot I(Dist_i = d_k) + \mathbf{X}_i^{pre}\gamma_M + \varepsilon_i^M$$

where $M_i$ includes: actual route length, redemption of the promotion, number of categories visited beyond planned, and time spent in store. This decomposes *how* the promotion affects unplanned spending.

---

## 13. Robustness, Placebo, Falsification Checks, and Diagnostic Tests

### Randomization balance checks

- Compare pre-trip covariates (planned basket size, expected expenditure, mission type, demographics) across randomized arms. Report normalized differences; flag any imbalance exceeding 0.1 standard deviations.
- If imbalance is detected, include the imbalanced covariates as controls and report both adjusted and unadjusted estimates.

### Placebo outcomes

- Test whether promotion assignment predicts **planned spending** (which should not be affected by an in-store promotion). A significant effect on planned spending would indicate either pre-trip measurement error or a failure of randomization.
- Test whether promotion assignment predicts pre-trip planned basket composition. No effect should be present.

### Robustness to route-measurement error

- If route data are available at multiple granularities (e.g., step count, time in motion, zone-to-zone transitions), replicate the analysis using alternative route-length proxies.
- If route data are missing for some shoppers, report bounds under worst-case assumptions (e.g., Lee bounds for the ITT).

### Sensitivity to unobserved confounding (descriptive analysis)

- Report Oster's $\delta$: the degree of selection on unobservables relative to observables that would be required to reduce $\hat{\beta}$ to zero.
- Report Rosenbaum bounds for the promotion ITT if matching or stratification is used for covariate adjustment.

### Functional form

- Replace the linear route-length term with indicator variables for route-length bins to test for nonlinearity in the route–spending association.
- Test whether the effect of promotion distance is linear in detour length or exhibits threshold behavior.

### Attrition analysis

- Compare the fraction of shoppers with missing route data, missing checkout linkage, or incomplete planned-basket elicitation across randomized arms. Differential attrition threatens internal validity.
- Report the characteristics of attritors vs. completers to assess external validity.

---

## 14. Heterogeneity Analysis (If Supportable)

With sufficient sample size, heterogeneity can be explored along dimensions that are measured before route realization (to avoid post-treatment bias):

| Dimension | Motivation | Estimation Approach |
|---|---|---|
| **Planned basket size** | Shoppers with larger missions may have less budget slack for unplanned purchases | Interact treatment with planned-basket-size quartiles |
| **Store familiarity** | Familiar shoppers may have more fixed routes and be less responsive to path prompts | Interact treatment with a familiarity indicator (e.g., self-reported or visit-frequency proxy) |
| **Shopping mission type** | "Quick trip" vs. "major stock-up" missions may respond differently | Stratify by mission category or interact |
| **Budget slack** | Shoppers with tighter budgets may be less responsive | Interact treatment with expected-expenditure-to-budget ratio |
| **Demographics** | Age, household size, and income may moderate responsiveness | Include interaction terms for key demographics |

All heterogeneity analyses are pre-specified and reported with multiple-hypothesis-testing adjustments (e.g., Romano-Wolf stepdown p-values or Benjamini-Hochberg FDR corrections).

---

## 15. Measurement, Compliance, Missingness, Spillover, and Implementation Limits

### Measurement

- **Route length:** Indoor positioning systems (WiFi triangulation, Bluetooth beacons, camera-based tracking) vary in accuracy. Systematic over- or under-estimation of route length that is correlated with store zone (e.g., worse signal near metal shelving in certain categories) could bias estimates. The design should include validation data (e.g., known-distance calibration paths) if possible.
- **Unplanned spending:** Constructed as checkout total minus pre-trip planned expenditure. This measure is vulnerable to (a) shoppers forgetting planned items at entry elicitation, inflating "unplanned" spending, and (b) shoppers remembering planned items *during* the trip that were not elicited, deflating "unplanned" spending. Item-level reconciliation (planned items vs. purchased items) is preferable to aggregate-spending subtraction when basket-level data permit.
- **Planned basket elicitation:** The timing and method (survey, app-based list, verbal interview) may affect accuracy. Social desirability bias could lead shoppers to underreport planned treat or impulse categories.

### Compliance

- In the experimental design, not all shoppers assigned to a path-inducing promotion will notice, understand, or act on it. The ITT captures the policy-relevant effect. The TOT can be estimated under standard IV assumptions but requires measuring actual promotion engagement (e.g., coupon scan, app click).
- Two-sided noncompliance: some control shoppers may organically visit the promoted category. This attenuates the ITT and complicates TOT estimation.

### Missingness

- Trips may lack route data (device failure, opt-out, signal loss), checkout linkage (unmatched loyalty ID), or planned-basket elicitation (refusal). If missingness exceeds 5–10%, report the fraction missing by stage and by treatment arm. Use multiple imputation for covariate missingness only (never impute outcomes or treatment status).
- For outcome missingness (checkout data unavailable), the design cannot recover the estimand without strong assumptions. Report the fraction of trips lost at each linkage stage (entry → route → checkout) and the effective analysis sample.

### Spillover

- Physical spillover is possible if shoppers in the same party (e.g., family shopping together) are assigned to different treatment arms, or if promotions are visible to other shoppers (e.g., displayed on a public screen). The design should randomize at the shopping-party level if party shopping is common, and deliver promotions privately (app-based or receipt-printed at entry).

### Implementation limits

- The experimental design requires real-time computation of planned-route distance to promoted categories, which demands a store-layout graph and routing algorithm. Implementation feasibility depends on the retailer's technology infrastructure.
- The promotional budget must account for redeemed coupons; this is a design cost, not an identification concern, but it constrains feasible sample sizes.

---

## 16. Failure Modes and Alternative Explanations

| Failure Mode | Consequence | Mitigation |
|---|---|---|
| Promotions affect spending through discount value, not route length | ITT captures a bundle of discount + route effects; route-length IV exclusion restriction violated | Report ITT as primary; do not overinterpret IV as pure route-length effect |
| Shoppers in treatment arms spend *less* on planned items due to budget reallocation | Total spending may not change even if unplanned spending increases | Report both unplanned spending and total spending as outcomes |
| Shoppers anticipate promotion assignment and adjust planned-basket elicitation | Pre-trip covariates become post-treatment; randomization balance checks on covariates fail | Minimize time between elicitation and assignment revelation; check balance |
| In-store displays, stockouts, or congestion differ systematically across arms | Confounds the promotion effect unless balanced by randomization | Report arm-specific store conditions; include time-of-day and store-zone fixed effects |
| Hawthorne effects: route tracking changes shopper behavior | Biases baseline route length and spending upward for all arms | Compare tracked vs. untracked trips if available; acknowledge as a generalizability limitation |
| Differential attrition by treatment arm | ITT estimate is biased if attrition is related to treatment | Report attrition rates by arm; compute Lee bounds; use inverse-probability weighting with caution |

---

## 17. What Cannot Be Claimed

1. **The descriptive regression coefficient $\hat{\beta}$ on observed route length is not a causal effect.** Even with rich pre-trip controls, it reflects a mixture of exposure, selection, and reverse causality.

2. **The route-length IV estimate cannot be interpreted as the pure causal effect of travel distance.** It captures the effect of an additional meter of induced travel *specific to the promotion mechanism*, not the effect of any additional meter of travel through any means.

3. **The promotion ITT does not separate the effect of additional travel from the effect of exposure to the promoted category itself.** The ITT is an estimate of a bundled intervention, not of route length in isolation.

4. **Results from one store format or geographic market do not generalize to all retail settings.** Store size, layout, category adjacency, and shopper demographics moderate the route–spending relationship.

5. **The design cannot distinguish whether unplanned purchases triggered by longer travel are truly incremental or merely accelerated** (i.e., purchased in this trip rather than the next). Panel data on repeat trips are needed to assess inter-temporal substitution.

6. **The design cannot estimate general equilibrium effects** of widespread promotion deployment on store congestion, shelf-stocking patterns, or long-run shopper route adaptation.

---

## 18. Additional Data Needed

| Data Element | Purpose | Priority |
|---|---|---|
| Store layout graph with aisle/category coordinates | Computing planned-route distance and detour distances for promotions | Essential |
| Item-level (SKU) basket data | Item-level reconciliation of planned vs. purchased baskets; more accurate unplanned-spending classification | High |
| Promotion engagement indicators | Measuring compliance for TOT estimation; distinguishing noticed, considered, and redeemed promotions | High |
| Repeat-trip panel (shopper ID across visits) | Assessing inter-temporal substitution; shopper fixed effects for descriptive analysis | Medium |
| Store-condition data (crowding, displays, stockouts by time and zone) | Controlling for environmental confounds (Channel D) | Medium |
| Validation data for route measurement | Known-distance calibration to assess systematic measurement error | Medium |
| Exit survey on shopping experience | Self-reported unplanned purchases, time pressure, satisfaction, and awareness of promotions | Low |
| Shopper location at promotion delivery | Determining whether the shopper had already passed the promoted category before receiving the offer | Low |

---

## 19. Threat-Response Table

| Threat | Response |
|---|---|
| **Endogenous route selection (mission confounding)** | Control for richest pre-trip planned-basket and mission covariates. Report Oster's $\delta$ to bound unobserved selection. For the experimental design, randomization of promotion assignment addresses this threat for the ITT estimand. |
| **Reverse causality (unplanned purchases extend routes)** | Construct reverse-causality-adjusted route length $R_i^{adj}$. Compare coefficients with and without adjustment to bound the mechanical reverse-causality contribution. In the experimental design, random assignment of promotions at entry breaks the reverse-causality link for the ITT. |
| **Simultaneity (in-trip decisions drive both variables)** | Acknowledge that cross-sectional trip-level data cannot resolve simultaneity without an instrument. The promotion experiment provides an instrument timed before route realization. |
| **Exclusion restriction violation (route-length IV)** | Do not rely on the route-length IV as a primary estimand. Use it only as an exploratory estimate, bounded by the ITT (upper bound) and zero (lower bound under monotonicity and a sign assumption). Report results transparently with caveats. |
| **Measurement error in route length** | If validation data exist, calibrate route-measurement accuracy. If multiple route proxies exist (step count, time in motion, zone transitions), replicate the analysis with each. Report attenuation-bias implications. |
| **Measurement error in unplanned spending** | Construct unplanned spending at the item level (planned-vs.-purchased reconciliation) rather than aggregate-spending subtraction when basket-level data permit. Report sensitivity to alternative definitions. |
| **Differential attrition** | Report attrition rates by stage and by treatment arm. Compute Lee bounds or Horowitz-Manski bounds for the ITT under worst-case assumptions about missing outcomes. |
| **Spillover between shoppers within a trip** | If party shopping is common, randomize at the shopping-party level. If point-of-sale promotions are publicly visible, acknowledge potential contamination. |
| **Hawthorne effects from tracking** | Compare behavior of tracked vs. untracked shoppers if a non-tracked baseline exists. Otherwise, acknowledge as a generalizability limitation (the study measures behavior under observation). |
| **Heterogeneous treatment effects across shoppers** | The ATE/ITT averages over heterogeneous effects. Report treatment-effect distributions or quantile treatment effects if sample size permits. The IV recovers a LATE for compliers, not the ATE. |
| **Store-level confounds (layout changes, promotions, seasonality)** | Include store fixed effects if multiple stores are used. Restrict data collection to a single promotional calendar period or control for concurrent promotions. Include day-of-week and time-of-day fixed effects. |
| **Discount effect confounded with detour effect** | Hold promotion value constant across detour-distance arms. The remaining variation is detour distance only. |
| **Planned-basket elicitation changes behavior** | Elicit the planned basket as unobtrusively as possible (e.g., app-based list import). If an explicit survey is used, acknowledge potential priming effects. |

---

## 20. Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
| Longer observed route length is associated with higher unplanned spending | OLS coefficient $\hat{\beta}$ in regression of unplanned spending on route length | Descriptive association | High | $\hat{\beta} \leq 0$ with tight confidence interval |
| Pre-trip mission characteristics explain part (but not all) of the route–spending association | Change in $\hat{\beta}$ when adding pre-trip covariates; Oster decomposition | Descriptive decomposition | High | $\hat{\beta}$ unchanged or increases after adding controls |
| Reverse causality (unplanned purchases → longer route) accounts for part of the association | Attenuation of $\hat{\beta}$ when using $R_i^{adj}$ instead of $R_i$ | Descriptive decomposition | Medium | No attenuation; $R_i^{adj}$ indistinguishable from $R_i$ |
| Random assignment of path-inducing promotions increases unplanned spending | ITT estimate $\hat{\beta}_k > 0$ for $d_k > 0$ in the experimental specification | Causal (ITT) | High (if experimental) | ITT estimates ≤ 0 and precisely estimated |
| Larger detour distances reduce promotion redemption or net unplanned spending | Gradient: $\hat{\beta}_{d_{large}} < \hat{\beta}_{d_{small}}$ or negative and significant difference | Causal (ITT) | Medium | No detectable gradient; flat dose-response curve |
| Induced additional travel (via promotion) causes additional unplanned spending | IV estimate $\hat{\beta}_{IV} > 0$ with instrument = promotion assignment | Causal (LATE, exploratory) | Low | First-stage F < 10; Anderson-Rubin CI includes zero; exclusion-restriction analysis suggests discount effects dominate travel effects |
| The effect of promotions on unplanned spending operates partly through additional categories visited | Mediation analysis: promotion assignment → categories visited → unplanned spending | Mechanism (descriptive mediation) | Low–Medium | No effect of promotion on categories visited; direct effect dominates |
| Store familiarity moderates responsiveness to path-inducing promotions | Significant interaction term between familiarity and treatment in heterogeneity analysis | Heterogeneous treatment effect | Medium | Interaction term not significant after multiple-testing adjustment |
| Shoppers with larger planned missions have less budget slack for unplanned spending | Negative interaction between planned basket size and treatment effect | Heterogeneous treatment effect | Medium | Interaction term positive or zero; no budget-constraint evidence |
| Results from this store/format do not generalize to all retail settings | Design logic; single-market/format constraint | External validity caveat | N/A (logical) | N/A (cannot be falsified without multi-site replication) |

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260527_235916_98725_28
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_235916_98725_28.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_235916_98725_28.trajectory.jsonl

## Operator Notes

- duration_ms: 232564
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
