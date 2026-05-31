# Raw Agent Run Log

- `run_id`: RUN_20260527_230906_16_openclaw_deepseekv4pro_isolated
- `case_id`: C008
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
- `timestamp`: 2026-05-27T23:09:06+0800
- `input_file`: benchmark/cases/C008_retail_tax_salience/agent_task_level3.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: Estimating the Causal Effect of Add-On Charge Salience on Consumer Demand

---

## 1. Executive Summary

This design proposes estimating the causal effect of making an add-on charge visible at the point of product choice—a **salience intervention**—on consumer demand. The core analytic strategy is a **difference-in-differences (DiD)** framework exploiting variation in which product-category × store cells receive a display change that makes the total (all-in) price salient, while holding the underlying economic price constant. The design relies on the retailer's controlled rollout of the intervention across selected product categories, stores, and time periods, with untreated products and stores serving as comparison groups. The central identification requirement is that the all-in economic price does not change when the display changes; only the **visibility** of the already-present add-on charge changes. The design incorporates staggered adoption, pre-trend diagnostics, triple-difference tests using auxiliary store-categories, and within-store substitution analyses to separate salience from confounds including actual price changes, store-wide shocks, differential trends, and spillovers. The strongest defensible estimand is the average treatment effect on the treated (ATT) for quantity sold among product-categories and time periods where the display intervention was implemented, estimated under parallel-trends assumptions. Long-run consumer learning, general equilibrium effects, and welfare consequences fall outside what the data can support.

---

## 2. Research Question

What is the causal effect of making an add-on charge visible at the point of product choice (i.e., increasing the salience of the all-in price) on consumer demand for the affected products, holding the underlying economic price constant?

---

## 3. Target Estimand or Strongest Defensible Estimand

**Target estimand:** The average treatment effect on the treated (ATT) — the difference between the observed post-intervention demand for treated product-category × store cells and the counterfactual demand those same cells would have experienced had the display change not occurred.

Formally, let \( i \) index a product-category × store cell, and let \( t \) index time periods. Let \( D_{it} \in \{0,1\} \) indicate whether cell \( i \) is treated (display makes the add-on charge visible) at time \( t \). Let \( Y_{it}(1) \) and \( Y_{it}(0) \) denote potential outcomes (e.g., log quantity sold) under treatment and control respectively.

\[
\tau_{ATT} = \mathbb{E}[Y_{it}(1) - Y_{it}(0) \mid D_{it} = 1, \text{post-period}]
\]

**If credible causal identification is not possible** (e.g., if the add-on charge amount itself varies with the display change, or if assignment is fully confounded with unobserved demand shifters), the strongest defensible estimand narrows to a **conditional difference in means** between exposed and unexposed cells after adjusting for observable covariates, interpreted descriptively rather than causally.

---

## 4. Treatment or Exposure and Main Outcomes

### Treatment/Exposure
- **Primary treatment:** A binary indicator equal to 1 for product-category × store × time cells where the displayed price information makes the add-on charge (previously only revealed at checkout) visible at the point of product choice.
- **Treatment timing:** Defined by the date the display change is implemented in each treated store for each treated category.
- **Treated-category indicators:** Capture which product categories are subject to the intervention.

### Main Outcomes
- **Quantity sold** (primary): Units sold per product or product-category × store × time period.
- **Revenue** (secondary): Total revenue per product or category × store × time.
- **Transaction counts** (secondary): Number of transactions involving the product/category.

### Secondary Outcomes
- **Category-level substitution:** Quantity sold in nearby or substitute categories within the same store.
- **Product composition shifts:** Within-category distribution of demand across products.
- **Execution indicators:** Any observable proxies for whether the display tag was present (if recorded).

---

## 5. Data Structure Summary

| Dimension | Description |
|---|---|
| **Unit of observation** | Product (or product-category) × store × time-period sales record |
| **Time** | Multiple weeks of pre-intervention and intervention periods; exact calendar dates withheld |
| **Geography** | One or more retail stores with potential comparison stores from a common operating environment |
| **Panel structure** | Repeated observations of the same products/categories across stores and time |
| **Assignment level** | Product category or product group × store × time cell |
| **Treatment variation** | Within-store across categories, across-store within categories, and across time (staggered rollout possible) |
| **Controls** | Price, discounts, promotions, product/category/store/time fixed effects, pre-intervention demand |

---

## 6. Relevant Causal Mechanisms

The design must distinguish among the following mechanisms:

**(a) Salience channel (the mechanism of interest):** Consumers' demand changes because the *visibility* of the add-on charge at the point of choice alters their perception of the total cost, even though the actual all-in price customers pay is unchanged. This is a pure information-salience effect.

**(b) Actual price change channel (confound):** The add-on charge itself changes (or a discount is adjusted) simultaneously with the display change, so demand responds to a genuine economic price change rather than to salience.

**(c) Store-wide or time-specific shocks (confound):** Demand in treated stores or time periods moves for reasons unrelated to the intervention — e.g., seasonal patterns, local economic conditions, marketing campaigns, or supply disruptions.

**(d) Differential pre-trends (confound):** Treated product categories were already on a different demand trajectory before the intervention, so post-intervention differences may reflect continuation of pre-existing trends rather than a salience response.

**(e) Attention spillover (confound/mechanism):** The display change draws attention to the broader aisle or category, increasing demand for nearby untreated products. This may inflate or deflate the estimated effect depending on whether control products are contaminated.

**(f) Substitution across products (confound):** If consumers substitute from treated products (now perceived as more expensive) to untreated substitutes, the category-level effect may differ from the product-level effect, and control products within the same store may be contaminated.

---

## 7. Main Identification Challenge

The core challenge is **isolating the salience mechanism**: the estimated demand response must be attributable to the *visibility* of the all-in price rather than to any concurrent change in the economic price itself, any pre-existing differences between treated and untreated products, or any contemporaneous shocks affecting treated stores or time periods. This requires:

1. **Price-invariance:** Confirming that the actual all-in price paid by consumers does not change when the display changes. If the add-on charge is a fixed dollar amount or percentage that remains constant, this can be verified directly. If it varies across products or time, the design must explicitly control for it.

2. **Unconfounded assignment:** The retailer's choice of which products, categories, stores, and time periods receive the display change must not be systematically correlated with factors that independently affect demand.

3. **Parallel trends:** In the absence of treatment, treated and control cells must have followed comparable demand trajectories. This is fundamentally untestable for the post-period but can be assessed in the pre-period.

---

## 8. Whether Credible Causal Identification Is Possible

**Conditional yes**, provided the following institutional conditions hold (and cannot be verified from the packet alone):

1. The **all-in economic price is unchanged** when the display changes — i.e., the add-on charge existed before the intervention and its amount or rate is identical in treated and untreated periods. If the packet-supplied data confirms this, identification is credible. If the add-on charge varies with the intervention timing or differs systematically across treated and untreated products, causal identification of a *salience-only* effect fails.

2. The retailer's assignment of treatment to product categories, stores, and time periods is **not systematically correlated with unobserved demand shifters**. If assignment is quasi-random (e.g., phased rollout by store or category for operational reasons unrelated to demand expectations), DiD is credible. If assignment targeted high-margin or fast-growing categories, identification is weakened and requires stronger covariate adjustment with appropriate caveats.

3. **Sufficient pre-intervention time periods** exist to evaluate parallel pre-trends.

If any of these conditions demonstrably fails in the data, the design remains a **descriptive conditional difference** rather than a credible causal estimate.

---

## 9. Proposed Empirical Design

### Primary Design: Difference-in-Differences with Staggered Adoption

Given that the retailer controls implementation timing and treatment varies by product-category × store × time, the core design is a staggered difference-in-differences (DiD) with two-way fixed effects.

**Design structure:**

- **Treated units:** Product-category × store cells that receive the display change during the intervention window.
- **Control units (primary):** Product-category × store cells that do NOT receive the display change, selected from:
  - (a) The same product categories in untreated (comparison) stores (cross-store control).
  - (b) Untreated product categories within the same treated store (within-store, across-category control).
  - (c) Pre-intervention time periods for treated cells (before-after within-cell comparison).
- **Event time:** Defined relative to the date the display change goes live in each treated cell.

### Triple-Difference Extension (If Feasible)

If treated and untreated categories within the same store exhibit differential pre-trends, a triple-difference (DDD) estimator can be deployed:

\[
DDD = (\text{Treated category, treated store, post} - \text{Treated category, treated store, pre}) \\
- (\text{Untreated category, treated store, post} - \text{Untreated category, treated store, pre}) \\
- [(\text{Treated category, untreated store, post} - \text{Treated category, untreated store, pre}) \\
- (\text{Untreated category, untreated store, post} - \text{Untreated category, untreated store, pre})]
\]

This nets out both (i) store-specific time trends that affect all categories equally and (ii) category-specific time trends that affect all stores equally, leaving only the store × category interaction that should be attributable to the treatment.

### Within-Store Substitution Analysis

To assess substitution and spillover, estimate the same DiD specification using **untreated products within the same store but in nearby or substitute categories** as the outcome. A positive coefficient on these secondary outcomes suggests attention spillover (the display draws shoppers to the broader aisle); a negative coefficient suggests substitution away from untreated products.

---

## 10. Why the Design Is Valid or Why Causal Identification Is Not Credible

### Validity Argument (Under Supportive Conditions)

1. **Within-cell variation:** The DiD estimator exploits within-product-category × store variation over time, absorbing all time-invariant unobserved heterogeneity via fixed effects.

2. **Multiple comparison groups:** Cross-store and within-store across-category controls provide distinct counterfactuals; consistency across both strengthens the causal interpretation.

3. **Price-constant design:** If the add-on charge rate is unchanged, any observed demand response cannot be attributed to an economic price change. This is the key feature that distinguishes a salience estimate from a generic price-elasticity estimate.

4. **Event-study framework:** Estimating dynamic treatment effects around the intervention date allows visual inspection of pre-trends and the timing of any demand response, ruling out anticipatory effects or gradual pre-existing divergence.

### Why Causal Identification Fails (If Conditions Are Not Met)

1. If the add-on charge amount varies with treatment timing or differs across cells, the salience estimate is contaminated by actual price variation, and the design cannot separate the two channels.

2. If assignment is confounded (e.g., the retailer selectively treats categories expected to benefit from the display change), DiD estimates are biased.

3. If pre-trends are non-parallel and DDD is infeasible (e.g., only one untreated store exists), selection bias remains.

---

## 11. Required Assumptions

| # | Assumption | Testable? |
|---|---|---|
| A1 | **Parallel trends:** In the absence of treatment, treated and control cells would have followed parallel demand trajectories. | Partially — pre-treatment trends can be tested; post-treatment counterfactual cannot. |
| A2 | **No contemporaneous price changes:** The all-in economic price (base price + add-on charge) is identical in treated and control periods for the same product. | Yes — directly testable in the transaction data by comparing the total amount paid. |
| A3 | **No anticipation:** Consumers and store staff do not change behavior in advance of the display change. | Partially — event-study coefficients for leads should be near zero. |
| A4 | **Stable unit treatment value assumption (SUTVA):** Treatment of one product-category × store cell does not affect outcomes in other cells through channels other than the treatment itself. | Violated by design (substitution and attention spillovers are expected); addressed through secondary analyses. |
| A5 | **No differential attrition or entry:** Product entry/exit, stockouts, and data recording quality do not differ systematically between treated and control cells around the intervention date. | Yes — can compare rates of missingness, stockout indicators, and product churn between groups. |
| A6 | **Correct treatment timing:** The date the display change becomes visible to consumers is accurately recorded. | Partially — can be verified against implementation logs if available; otherwise relies on retailer reporting. |
| A7 | **No compositional change in shoppers:** The mix of shoppers visiting treated stores does not change systematically at the time of the intervention. | Not directly testable without individual shopper data; can be partially assessed via aggregate store traffic. |

---

## 12. Statistical Model or Analysis Equation

### Primary Specification: Two-Way Fixed Effects Event Study

Let \( y_{icst} \) be the outcome (e.g., log quantity sold) for product \( i \) in category \( c \) in store \( s \) at time \( t \).

\[
y_{icst} = \alpha_{ics} + \lambda_t + \sum_{k = -K, k \neq -1}^{L} \beta_k \cdot \mathbf{1}[t - t^*_{cs} = k] + \gamma X_{icst} + \varepsilon_{icst}
\]

Where:
- \( \alpha_{ics} \): product × category × store fixed effect (absorbs time-invariant product characteristics)
- \( \lambda_t \): time fixed effect (absorbs common time shocks)
- \( t^*_{cs} \): date when category \( c \) in store \( s \) receives the display change
- \( \mathbf{1}[t - t^*_{cs} = k] \): event-time indicators for \( k \) periods relative to treatment
- \( k = -1 \) is the omitted reference period (immediately before treatment)
- \( \beta_k \) for \( k < 0 \): tests for differential pre-trends
- \( \beta_k \) for \( k \geq 0 \): dynamic treatment effects
- \( X_{icst} \): vector of time-varying controls (actual paid price, discount indicator, promotion indicator)
- \( \varepsilon_{icst} \): error term, clustered at the store-category level

### Alternative: Stacked/Binned DiD Specification

If the staggered rollout has few adoption cohorts or the two-way FE estimator raises concerns about heterogeneous treatment effects with staggered timing, a **stacked DiD** approach can be used:

\[
y_{icstg} = \alpha_{icsg} + \lambda_{tg} + \beta \cdot \text{Treat}_{cs} \times \text{Post}_{tg} + \gamma X_{icstg} + \varepsilon_{icstg}
\]

Where \( g \) indexes treatment cohorts (sets of categories treated at the same time), and each cohort is paired with its own set of never-treated or not-yet-treated controls. This avoids the negative-weighting problem in staggered DiD with heterogeneous effects.

### Specification with Price Controls (Salience-Price Decomposition)

To explicitly separate salience from price effects:

\[
y_{icst} = \alpha_{ics} + \lambda_t + \beta_1 \cdot \text{DisplayVisible}_{cst} + \beta_2 \cdot \text{AllInPrice}_{icst} + \beta_3 \cdot \text{DisplayVisible}_{cst} \times \text{AllInPrice}_{icst} + \gamma X_{icst} + \varepsilon_{icst}
\]

Here, \( \beta_1 \) captures the **salience effect** (demand shift from visibility, holding the all-in price constant). \( \beta_2 \) captures the standard own-price effect. If the add-on charge is a uniform amount, \( \beta_1 \) is the parameter of interest; if the add-on charge varies across products, the interaction term \( \beta_3 \) tests whether salience effects vary with the magnitude of the add-on.

### Triple-Difference Specification

\[
y_{icst} = \alpha + \beta_1 \cdot \text{TreatedCat}_c \times \text{TreatedStore}_s \times \text{Post}_t + \beta_2 \cdot \text{TreatedCat}_c \times \text{Post}_t + \beta_3 \cdot \text{TreatedStore}_s \times \text{Post}_t + \beta_4 \cdot \text{TreatedCat}_c \times \text{TreatedStore}_s + \delta \cdot \text{FE} + \gamma X_{icst} + \varepsilon_{icst}
\]

\( \beta_1 \) is the DDD estimate — the differential effect of treatment net of common trends in treated stores and treated categories.

---

## 13. Robustness, Placebo, Falsification Checks, or Diagnostic Tests

### (a) Pre-Trend Assessment
Plot event-study coefficients \( \beta_k \) for \( k < 0 \). If these are statistically indistinguishable from zero and show no systematic slope, parallel pre-trends are supported.

### (b) Placebo Timing Test
Shift the pseudo-treatment date backward by several periods (e.g., 4 weeks before actual implementation) and re-estimate the DiD on the pre-intervention data only. A null "effect" of the placebo treatment supports the identifying assumption.

### (c) Placebo Category Test
Randomly assign the treatment indicator to untreated categories in treated stores (or to treated categories in untreated stores, pre-intervention) and estimate the model. The distribution of placebo estimates should center on zero.

### (d) Price-Invariance Verification
Directly test whether the all-in price paid (base price + add-on charge) differs between pre- and post-intervention periods for treated products. A null difference is required for the salience interpretation. Additionally, test whether discount frequency or promotion intensity changes at the intervention date.

### (e) Leave-One-Out Sensitivity
Re-estimate the main specification omitting one store, one category, or one time period at a time to assess whether results are driven by any single unit.

### (f) Alternative Control Group Construction
Report results using (i) only cross-store controls, (ii) only within-store across-category controls, and (iii) both. Consistency across specifications strengthens credibility. Divergence signals substitution or spillover contamination.

### (g) Donut RD / Narrow Window
Restrict the sample to a narrow time window around the intervention date (e.g., ±2 weeks) to reduce the influence of longer-run trends while preserving pre-post comparisons.

### (h) Falsification Using Pre-Determined Outcomes
Test whether pre-intervention covariates (baseline demand levels, pre-period price levels, category characteristics) predict treatment assignment. If assignment is as-good-as-random conditional on observables, these should have no predictive power.

### (i) Bounds for Non-Random Attrition
If stockouts or product churn differ by treatment status, construct Lee (2009)-style bounds on the treatment effect by trimming the distribution of the outcome in the group with less attrition.

---

## 14. Heterogeneity Analysis if Supportable

If the data support it (sufficient within-cell variation and statistical power), the following heterogeneity dimensions are informative:

| Dimension | Rationale |
|---|---|
| **Magnitude of the add-on charge** | If the add-on is a fixed dollar amount, salience effects may be larger where the add-on is larger relative to the base price. If the add-on is a uniform percentage, this dimension is not available. |
| **Product price tier** | Consumers may be more attentive to total prices for expensive durables than for inexpensive convenience goods, or vice versa. |
| **Category type** | Staples vs. discretionary categories; frequently purchased vs. infrequently purchased categories. |
| **Store characteristics** | If multiple stores are available, heterogeneity by store size, format, or shopper demographics (if available) sheds light on external validity. |
| **Time since intervention** | Whether the salience effect attenuates (consumers learn/adjust) or persists over the intervention window. |
| **Baseline add-on awareness** | If any pre-intervention survey or proxy for consumer awareness of the add-on exists, effects should be larger where baseline awareness is lower. Without such data, this is not testable. |

**Important caveat:** Heterogeneity analyses are exploratory. Without pre-registration or sufficient multiple-hypothesis correction, they should be interpreted as hypothesis-generating rather than confirmatory.

---

## 15. Measurement, Compliance, Missingness, Spillover, or Implementation Limits

### Compliance / Implementation Fidelity
The packet notes that "store execution may be imperfect if tags are misplaced, missing, or implemented late." The treatment indicator in the primary analysis is based on **intent-to-treat** (ITT): a product-category × store cell is coded as treated if it was *scheduled* to receive the display change, regardless of actual compliance. If implementation audits or execution proxies exist (e.g., photos, staff checklists, or scanner logs of tag printing), a **local average treatment effect (LATE)** can be estimated via instrumental variables, where scheduled treatment instruments actual visible display.

**Remaining limitation:** If compliance is low and unobserved, the ITT estimate is attenuated toward zero but retains a valid causal interpretation under random assignment. Without implementation data, the complier-specific effect is not identifiable.

### Missingness / Attrition
The packet identifies stockouts, product entry/exit, scanner recording problems, and incomplete promotion records as sources of missing data.

- **Stockouts:** If stockout indicators are available, include them as controls or test whether stockout probability changes at the intervention date. If stockouts increase after treatment (because demand responds), this introduces a selection problem in observed sales.
- **Product churn:** Compare rates of product entry and exit between treated and untreated categories around the intervention date. Differential churn may indicate that the composition of products available for sale changes with treatment.
- **Scanner errors:** If recording quality is consistent across treatment status and time, this introduces classical measurement error in the dependent variable, which inflates standard errors but does not bias DiD estimates.
- **Incomplete promotion records:** If promotions are systematically unrecorded in treated stores or periods, the price-invariance check fails and the salience estimate is biased.

### Spillover / Interference
The packet explicitly notes that shoppers may substitute between treated and untreated products, and display changes may draw attention to nearby products or categories.

- **Within-store substitution:** Estimate DiD models using untreated products in the same store as the outcome. A negative coefficient indicates demand shifted *away* from untreated products toward treated ones (substitution). A positive coefficient indicates attention spillover.
- **Cross-category attention:** If product adjacency or aisle layout data are available, test whether untreated products physically proximate to treated displays experience larger demand changes than products farther away. Without layout data, this is not testable.
- **SUTVA violation consequence:** If substitution is present, the within-store control group is contaminated, and the cross-store control group becomes the more reliable counterfactual.

### Measurement Error in Treatment Timing
If the actual date the display became visible to consumers differs from the recorded implementation date (e.g., tags were printed on day \( t \) but not placed on shelves until day \( t+2 \)), the event-study coefficients will be biased toward finding gradual rather than sharp effects. The design is robust to modest mis-timing if the mis-timing is non-differential; sharp effects may appear smoothed.

---

## 16. Failure Modes and Alternative Explanations

| Failure Mode | Alternative Explanation | Detection Strategy |
|---|---|---|
| Post-intervention demand drop | Consumers respond to the *visibility* of the add-on (salience) — the intended mechanism. | Verify the all-in price is unchanged. If it is, the demand response is consistent with salience. |
| Post-intervention demand drop | The retailer simultaneously raised the add-on charge or reduced discounts, so consumers face a higher all-in price. | Falsified by testing whether the all-in price paid changes at the intervention date. |
| Post-intervention demand drop | Seasonal or calendar-driven demand decline coinciding with the intervention date. | Time fixed effects absorb common shocks. Placebo timing tests in prior years or untreated stores detect seasonality. |
| Post-intervention demand drop | Treated categories were already declining relative to controls. | Pre-trend test. If pre-trends are non-parallel, the DiD estimate is biased. |
| Post-intervention demand drop | Stockouts increased for treated products (demand-driven or supply-driven), mechanically reducing observed sales. | Test stockout probability around the intervention date. |
| No demand response observed | The add-on charge was too small to matter to consumers, the display was poorly executed (compliance failure), or consumers already knew about the charge (ceiling effect). | Cannot distinguish among these without add-on magnitude data, implementation audits, or pre-intervention awareness measures. |
| Demand response in untreated products | Attention spillover from the display change drawing shoppers to the broader category. | Not a "failure" per se but a mechanism nuance. Consistent with salience operating through attention rather than price perception alone. |
| Demand response in untreated products | A store-wide promotion or marketing campaign launched simultaneously with the display change. | Falsified by checking whether untreated products show effects in treated stores but NOT in untreated stores at the same time. |

---

## 17. What Cannot Be Claimed

1. **Long-run equilibrium effects:** The design estimates short-run demand responses over the intervention window. It cannot speak to whether consumers learn to ignore the display over time, adjust their shopping behavior, or whether the effect attenuates after repeated exposure. A longer panel would be needed.

2. **Welfare effects:** The design estimates quantity responses, not consumer surplus, deadweight loss, or retailer profit. Without a structural demand model and cost data, welfare claims are unsupported.

3. **Mechanism decomposition:** While the design can distinguish salience-driven demand responses from actual price changes, it cannot distinguish between specific psychological mechanisms (e.g., "the add-on charge was genuinely overlooked" vs. "consumers knew about it but the display made it more cognitively available"). These are observationally equivalent in the transaction data.

4. **External validity:** The results apply to the specific retailer, product categories, stores, and time period studied. Generalization to other retailers, product types, add-on charge structures, or market contexts requires additional evidence.

5. **Individual-level heterogeneity:** Without shopper-level data (e.g., loyalty card records), the design cannot estimate how effects vary by consumer income, price sensitivity, or shopping frequency.

6. **Causal effect of the add-on charge itself:** The design estimates the effect of making an existing add-on charge *visible*, not the effect of *introducing* an add-on charge, which would confound salience with a genuine price change.

7. **Optimal disclosure policy:** The design does not address whether the observed demand response is normatively desirable, whether consumers are making "better" decisions, or what the socially optimal disclosure regime would be.

---

## 18. Additional Data Needed

| Data Element | Why Needed |
|---|---|
| **All-in price decomposition** (base price and add-on charge as separate fields) | Required to verify that the add-on charge amount is unchanged when the display changes. Without this, salience cannot be separated from price effects. |
| **Implementation fidelity records** (e.g., staff checklists, tag-printing logs, in-store audit photos) | Enables estimation of complier-specific effects (LATE) and diagnosis of null results due to non-compliance. |
| **Product adjacency or store layout data** | Enables testing of spatial spillover patterns (whether effects decay with physical distance from treated displays). |
| **Store traffic or shopper count data** | Enables testing for compositional changes in the shopper pool that could confound demand estimates. |
| **Longer post-intervention panel** | Required to distinguish short-run salience effects from long-run adaptation or learning. |
| **Shopper-level panel (e.g., loyalty card data)** | Enables analysis of individual-level heterogeneity, within-shopper substitution patterns, and whether effects operate on the extensive or intensive margin. |
| **Pre-intervention survey of add-on awareness** | Enables testing whether salience effects are larger for consumers with lower baseline awareness. |
| **Additional untreated stores** | Strengthens the cross-store control group and enables more precise estimation of store-specific shocks. |
| **Multiple pre-intervention years** | Enables placebo tests using the same calendar period in prior years to rule out seasonality. |

---

## 19. Threat-Response Table

| Threat | Why It Matters | Proposed Diagnostic or Design Response | Remaining Limitation |
|---|---|---|---|
| **Timing/trend:** Demand for treated products may have been changing before the intervention for unrelated reasons. | Violates the parallel-trends assumption; post-intervention differences may reflect continuation of pre-existing trends rather than a salience response. | Event-study specification with leads and lags; visual and statistical test that pre-treatment coefficients are jointly zero. Placebo timing test shifting the pseudo-treatment date backward. | Parallel pre-trends do not guarantee parallel post-treatment counterfactual trends. Unobserved time-varying confounders coinciding with the intervention date remain possible. |
| **Selection:** Products/categories chosen for the display change may differ systematically from comparison products in baseline demand, promotion intensity, or seasonality. | If treatment assignment is correlated with demand determinants, the DiD estimate is biased (selection on unobservables). | Falsification test: regress treatment assignment on pre-intervention covariates. Use multiple control groups (cross-store, within-store across-category). Triple-difference if differential trends exist. | If selection is on unobservable time-varying factors correlated with the intervention timing, no design feature can fully address it without an instrument or exogenous variation in assignment. |
| **Measurement:** Observed demand changes may reflect stockouts, scanner-recording errors, changes in discounts, or actual paid prices rather than salience. | The core claim — that salience drives demand — is invalid if the all-in price actually changed or if measurement artifacts drive the result. | Directly test whether the all-in price paid differs between pre- and post-periods. Control for actual price, discounts, and promotions in all specifications. Test for differential missingness and stockout probability around the intervention date. Lee bounds if attrition is non-random. | If discounts or promotions are incompletely recorded, the price-invariance test may falsely "pass." Scanner errors that are correlated with treatment timing cannot be detected without independent verification. |
| **Spillover/interference:** Shoppers may substitute from treated to untreated products, or the display may alter attention to the broader aisle/category. | Violates SUTVA; within-store control groups may be contaminated, and the estimated treatment effect captures net (not gross) demand shifts. | Estimate treatment effects on untreated products in same store and nearby categories. Report separate estimates using cross-store controls vs. within-store controls. If spillover is present, the cross-store estimate is preferred. | Without product adjacency data, spatial spillover patterns cannot be precisely mapped. Substitution to products outside the observed category set (e.g., other stores, online) is unobservable. |
| **Compliance/take-up:** Store staff may implement display changes inconsistently across products or time periods. | ITT estimates are attenuated toward zero; null results may reflect non-compliance rather than absence of a salience effect. | Report ITT as the primary estimate. If implementation data exist, estimate LATE via IV. Test whether results are stronger in stores or time periods with higher expected compliance. | Without implementation fidelity data, compliance cannot be measured, and the attenuation bias cannot be quantified. |
| **Scope:** A short intervention window may estimate only short-run demand responses and may not reveal long-run consumer learning or adaptation. | The estimated effect may overstate the persistent effect of salience-based disclosure if consumers learn to disregard the display over time. | Report results separately by time since intervention (early vs. late in the intervention window). Test for trend in treatment effect magnitude over the post-period. | Cannot distinguish between attenuation due to learning, attention decay, or other time-varying factors without a much longer panel or an experimental design that varies exposure duration. |

---

## 20. Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
| Making the add-on charge visible at the point of choice reduces demand for treated products. | Estimated \( \beta \) coefficient from DiD specification on log quantity sold; event-study plot showing a drop at \( k = 0 \) relative to \( k = -1 \). | Causal (under assumptions A1–A7) | Moderate to high if all-in price is verified constant and pre-trends are parallel. Low if these checks fail. | Null or positive DiD coefficient; event-study shows no discontinuity at the intervention date. |
| The demand response is driven by salience rather than by an actual price change. | The all-in price paid does not change at the intervention date; controlling for actual price does not attenuate the DiD coefficient. | Mechanism (salience vs. price) | Moderate — requires the add-on charge to be separately observable in the data and demonstrably unchanged. Without separate price components, this claim cannot be made. | The all-in price or the add-on component differs between pre- and post-periods; or the DiD coefficient shrinks substantially when actual price is controlled. |
| Pre-existing trends do not explain the estimated effect. | Pre-treatment event-study coefficients (\( k < 0 \)) are individually and jointly indistinguishable from zero; placebo timing test yields null results. | Diagnostic | High for the pre-period; moderate for the counterfactual post-period trend. | Non-zero pre-trend coefficients or significant placebo-timing estimates. |
| The estimated effect is not driven by differential selection of treated categories. | Falsification test showing pre-intervention covariates do not predict treatment assignment. Consistency of estimates across cross-store and within-store control groups. | Diagnostic | Moderate — can rule out selection on observables; cannot rule out selection on unobserved time-varying confounders. | Pre-intervention covariates strongly predict treatment assignment; estimates differ substantially across control group constructions. |
| Substitution or attention spillover to untreated products exists. | DiD estimates using untreated product categories in treated stores as outcomes are non-zero. | Descriptive / correlational | Moderate — non-zero estimates on untreated products are consistent with spillover but could also reflect common shocks not absorbed by fixed effects. | Null estimates on untreated product outcomes in treated stores. |
| The effect operates on quantity rather than only on revenue. | Separate DiD estimates for quantity and revenue; if quantity falls but revenue does not (because price per unit is unchanged), the effect is on volume. | Mechanism (quantity vs. revenue decomposition) | High — directly testable in the transaction data. | Revenue moves proportionally with price changes, or revenue falls by the same percentage as quantity without price changes. |
| The estimated effect is not driven by a few outlier categories or time periods. | Leave-one-out sensitivity analysis; estimates are stable when any single store, category, or time period is excluded. | Robustness | High — directly testable. | Coefficient changes sign or loses significance when a single unit is removed. |
| The effect reflects short-run salience and may not persist. | The treatment effect estimate is based on the intervention window only; formal persistence cannot be tested without longer follow-up. | Descriptive / caveat | Low for persistence claims — explicitly limited by data. | Cannot be falsified or verified with available data; a longer panel is needed. |

---

## Summary Assessment

This design can produce a **credible causal estimate of the salience effect** of making an add-on charge visible at the point of choice if and only if:

1. The **add-on charge is separately identifiable in the data** and demonstrably unchanged between pre- and post-intervention periods.
2. **Pre-intervention parallel trends** hold between treated and control product-category × store cells.
3. The retailer's assignment is **not systematically correlated with unobserved demand shifters** (or the DDD design successfully nets out differential trends).

If any of these conditions fails, the strongest defensible output is a **descriptive conditional difference in means** between exposed and unexposed cells after adjusting for observable price, promotion, category, store, and time covariates — interpreted as an association rather than a causal effect.

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260527_230906_98725_16
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_230906_98725_16.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260527_230906_98725_16.trajectory.jsonl

## Operator Notes

- duration_ms: 220375
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
