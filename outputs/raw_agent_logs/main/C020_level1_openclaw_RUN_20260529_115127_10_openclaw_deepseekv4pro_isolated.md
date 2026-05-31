# Raw Agent Run Log

- `run_id`: RUN_20260529_115127_10_openclaw_deepseekv4pro_isolated
- `case_id`: C020
- `variant_id`: level1
- `level`: level1
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
- `timestamp`: 2026-05-29T11:51:27+0800
- `input_file`: benchmark/cases/C020_price_ending_field_experiment/agent_task_level1.md
- `system_prompt_summary`: workspace=/Users/jiangcanxiang/OpenClawBenchmarkIsolated; thinking=high; actual_tool_use=none; agent=benchmark_isolated
- `contamination_status`: unknown
- `contamination_reason`: pending manual content review; actual tool use=none
- `status`: success

## Raw Agent Output

# Research Design: Price-Ending Format Effects on Consumer Demand

---

## 1. Executive Summary

This design studies whether salient terminal-digit pricing (e.g., .99, .95 endings) causally increases demand beyond what would be expected from the price level alone, and whether any observed effect reflects psychological digit processing, bargain signaling, or interaction with customer product familiarity. The core identification strategy exploits between-group variation in price-ending format for otherwise identical products — a between-subjects experimental logic implemented in a live retail setting. The design explicitly separates the format effect from confounding by sale status, product characteristics, and managerial selection. Where the available information does not support causal claims, the strongest defensible descriptive or correlational analysis is proposed instead.

---

## 2. Research Question

Does presenting a product with a salient terminal-digit price ending (e.g., ending in .99) causally increase the probability or quantity of purchase relative to presenting the same product with a round-number ending, after controlling for the absolute price level, discount status, and product characteristics? And through which mechanism — digit-level perceptual processing, bargain inference, or reduced information friction — does any such effect operate?

---

## 3. Target Estimand

The primary causal estimand is the **average treatment effect (ATE) of the price-ending format on purchase incidence**, defined as:

> **ATE = E[Y(1) − Y(0)]**

where Y(1) is the purchase outcome when the offer displays a salient terminal digit (e.g., ¥19.99) and Y(0) is the outcome when the same offer displays a round-number ending (e.g., ¥20.00), holding all other offer features — including the absolute price level, product, presentation, and channel — constant.

If randomization across all units is not feasible, the estimand narrows to the **conditional average treatment effect (CATE)** within the subpopulation for which treatment assignment is as-good-as-random, or to the **intent-to-treat (ITT) effect** under a group-level assignment rule.

A secondary estimand is the **mechanism-specific treatment effect**: the component of the ATE attributable to digit-level perceptual processing (Pathway A), net of the component attributable to bargain-signal inference (Pathway B). This is identified only under explicit experimental variation in the information environment (see Section 14).

---

## 4. Treatment and Main Outcomes

### Treatment

| Treatment Arm | Definition |
|---|---|
| **T = 1 (Salient ending)** | The offer price ends in a salient terminal digit — typically .99, .95, or .90. The final digit(s) are visually prominent relative to the leading digits. |
| **T = 0 (Round ending)** | The same absolute price or a trivially different price (±0.01–0.10 in the smallest currency unit) presented with a round-number ending (e.g., .00). |

The treatment is **the format of the price ending**, not the absolute price level. The absolute price is controlled by design: T=1 and T=0 conditions are set to identical or near-identical price levels, differing only in the terminal digit(s).

### Main Outcomes

| Outcome | Measurement | Type |
|---|---|---|
| **Purchase incidence** | Binary indicator: did the customer purchase the focal item during the observation window? | Primary |
| **Purchase quantity** | Number of units purchased of the focal item (conditional on any purchase) | Secondary |
| **Basket conversion** | Binary: did the customer complete any purchase in the same session/visit? | Secondary (spillover) |
| **Time-to-decision** | If measurable: time spent on the product page or in the purchase funnel | Process/mechanism |

---

## 5. Data Structure Summary

### Unit of observation

Customer-offer exposure. Each row represents one customer's exposure to one product offer with an assigned price-ending format, along with that customer's subsequent purchase outcome.

### Variables available or constructible

| Variable class | Variables |
|---|---|
| **Treatment assignment** | Indicator for salient vs. round price ending; exact ending digits |
| **Outcome** | Purchase indicator, quantity purchased |
| **Offer characteristics** | Absolute price (amount), product identifier, product category |
| **Discount/sale status** | Whether the item is on markdown, sale flag, discount depth |
| **Customer covariates** | Customer group identifier, past purchase history with this product/category (proxy for familiarity) |
| **Temporal/contextual** | Date, time, channel |

### Variables not available

The packet does not provide: exact customer demographics, browsing behavior, eye-tracking data, post-purchase surveys, or the retailer's complete pricing rule. The absence of these does not invalidate the core design but limits mechanism testing (see Section 17).

---

## 6. Relevant Causal Mechanisms

The packet identifies three candidate pathways and one confounding channel:

1. **Pathway A — Perceptual processing of the digit itself:** The salient terminal digit alters how the customer processes the price magnitude. A price of ¥19.99 may be encoded as "nineteen something" (left-digit bias) rather than as approximately twenty, lowering the perceived price. This is a direct cognitive effect of the digit format, independent of any inference about discounts.

2. **Pathway B — Bargain or discount signaling:** Customers have learned through experience that prices ending in .99 or .95 frequently signal a sale, clearance, or promotional price. The ending format activates a learned association ("this is a deal"), increasing purchase propensity even when the actual discount is zero or trivial.

3. **Pathway C — Information environment moderation:** The format effect may be larger when customers lack prior price knowledge (unfamiliar products, first-time buyers) because they cannot benchmark the price against memory. When customers know the typical price, the ending format provides little additional signal. When they do not, the format looms larger in judgment.

4. **Alternative explanation — Managerial selection:** In observational data, managers do not assign price endings randomly. Items with .99 endings may be systematically different from items with round endings: more likely to be on promotion, in different categories, at different price tiers, or displayed during different seasons. A naive comparison of demand across ending formats in historical data confounds the format effect with all these selection factors.

---

## 7. Main Identification Challenge

The fundamental identification problem is **endogenous treatment assignment**. In historical pricing data, the price-ending format is chosen by the retailer, not randomly assigned. The format co-varies with:

- **Sale/promotion status:** Items ending in .99 are disproportionately sale items.
- **Product characteristics:** Certain categories (e.g., fast-moving consumer goods) are more likely to use .99 endings than others (e.g., luxury goods).
- **Price level:** The ending format may be applied differently at different absolute price ranges.
- **Temporal factors:** Seasonal promotions or clearance cycles may concentrate .99 endings in specific time windows with different baseline demand.
- **Customer self-selection:** If different customer groups see different formats, and the groups also differ in baseline purchase propensity, the comparison is confounded.

A simple cross-sectional regression of purchase on ending-format indicator in historical data does not identify the causal effect of the format.

---

## 8. Whether Credible Causal Identification Is Possible

**Yes, conditional on the available variation.** The packet states that "different customer groups can be exposed to different price formats for otherwise comparable offers." If this exposure is under researcher control or arises from a process that is as-good-as-random conditional on observables, credible causal identification is possible through a **between-subjects experimental design** or a **quasi-experimental design** exploiting plausibly exogenous variation in format assignment.

If the format assignment rule is entirely observational and non-random, and no credible instrument or discontinuity is available, then the strongest defensible analysis is a **rich correlational design with explicit caveats**.

The design below assumes the researcher has at minimum the ability to assign price-ending formats across customer groups for the same products contemporaneously — the scenario described in the packet.

---

## 9. Proposed Empirical Design

### Design: Between-Group Randomized Price-Ending Experiment

#### Setup

1. **Product selection:** Select a set of products across multiple categories, including products with varying levels of customer familiarity (proxied by purchase frequency in historical data).

2. **Treatment assignment:** Randomly partition customers (or customer groups, if individual-level randomization is infeasible) into two arms:
   - **Treatment arm:** Sees all focal products with salient terminal-digit endings (e.g., ¥19.99).
   - **Control arm:** Sees the same products with round-number endings (e.g., ¥20.00).

3. **Price-level matching:** For each product, the absolute price in the two arms differs by at most a trivially small amount (e.g., ¥0.01). This ensures the treatment is the format, not the price level.

4. **Holding other features constant:** Product description, imagery, placement, and all other presentation features are identical across arms. Only the terminal digit(s) of the displayed price differ.

5. **Concurrent exposure:** Both arms are exposed concurrently to avoid confounding by time trends, seasonality, or changing inventory.

#### Analysis: Intent-to-Treat (ITT)

Since the assignment is at the customer-group level and compliance (actual exposure to the assigned format) may be imperfect, the primary analysis estimates the ITT:

```
Purchase_i = α + β × T_group(i) + γ × X_i + ε_i
```

where:
- `Purchase_i` is the binary purchase outcome for customer i's exposure to the focal product.
- `T_group(i)` is the treatment assignment indicator for the group to which customer i belongs.
- `X_i` is a vector of pre-treatment covariates (product category, historical purchase frequency, calendar week fixed effects) included to improve precision.
- β is the ITT estimate: the causal effect of assignment to the salient-ending format on purchase probability.

**Standard errors:** Clustered at the assignment unit (customer group) level.

### Design Feature: Separating Format from Sale Signaling (Pathway A vs. B)

To distinguish Pathway A (perceptual processing) from Pathway B (bargain signaling), introduce a **2×2 factorial design**:

|  | Round Ending | Salient Ending |
|---|---|---|
| **No sale cue** | Control | Format only (Pathway A) |
| **Sale cue present** | Sale signal only | Format + sale (Pathways A+B) |

**Cells:**
- **Round, No Sale:** Pure control. Round price, no discount label, no strikethrough.
- **Salient, No Sale:** Salient ending, no discount label. Any demand increase relative to control isolates the perceptual/digit-processing effect (Pathway A), because there is no bargain cue to confound.
- **Round, Sale:** Round price with a sale badge or strikethrough showing a discount. This captures the effect of a pure bargain signal without the salient-digit format.
- **Salient, Sale:** Both cues present. The incremental effect beyond the additive sum of the two single-cue effects captures any interaction.

This design identifies Pathway A vs. Pathway B under the assumption that the two cues operate additively in the absence of interaction, and that the sale cue manipulation is orthogonal to format assignment. If a factorial design is infeasible in the retail environment, the design defaults to the simpler two-arm experiment and acknowledges that mechanisms cannot be separately identified (see Section 17).

---

## 10. Why the Design Is Valid

The design is valid because:

1. **Randomization breaks the selection problem.** By randomly assigning the format across customer groups, the format is orthogonal to all product characteristics, sale status, temporal factors, and customer baseline propensities. This eliminates the managerial-selection confound (alternative explanation).

2. **Concurrent exposure eliminates time confounding.** Both arms run simultaneously, so calendar effects (holidays, weekends, promotions) affect both arms equally in expectation.

3. **Within-product control eliminates product confounding.** The same products appear in both arms, so any between-product differences in baseline demand do not contaminate the comparison.

4. **Price-level matching isolates the format effect.** The absolute price differs only trivially between arms, so the estimate captures the format effect, not a price-level effect.

5. **ITT preserves randomization.** Even if some customers in the treatment arm do not notice or process the price ending, the ITT estimate is an unbiased estimate of the causal effect of *offering* the salient format — which is the policy-relevant parameter.

If randomization is not feasible and only observational variation is available, the design validity weakens substantially. In that case, the strongest defensible analysis is a **difference-in-differences or event-study design** exploiting a policy change in the retailer's pricing-format rule (e.g., a switch from round to .99 endings for a subset of products at a known date), with products retaining the old format serving as controls. The validity of that design depends on the plausibility of parallel trends, which cannot be assessed without historical data.

---

## 11. Required Assumptions

### For the randomized design:

| Assumption | Description | Plausibility |
|---|---|---|
| **A1. Random assignment** | Customer groups are assigned to treatment/control by a process that is independent of potential outcomes. | High if researcher-controlled; must be verified. |
| **A2. SUTVA (no interference)** | One customer's treatment assignment does not affect another customer's purchase outcome. | Plausible if groups are isolated (e.g., different geographic markets, different online sessions). Less plausible if customers in the same household or social network see different formats and discuss. |
| **A3. Exclusion of the absolute price channel** | The ¥0.01 difference between arms (e.g., ¥19.99 vs. ¥20.00) does not meaningfully affect demand through the budget constraint. | Highly plausible: the real income/budget effect of ¥0.01 is negligible. |
| **A4. No differential attrition** | Customers in treatment and control arms do not differentially drop out of the sample or avoid the purchase event for reasons other than the format. | Requires monitoring of exposure rates. |
| **A5. Format salience** | Customers in the treatment arm actually notice the terminal digit. | This is an ITT assumption: we estimate the effect of assignment, not the effect of noticing. If salience is low, the ITT will be attenuated toward zero but remains unbiased for the assignment effect. |

### For mechanism separation (2×2 factorial extension):

| Assumption | Description |
|---|---|
| **A6. Additive separability (no interaction) for identification** | In the absence of an interaction, Pathway A = (Salient, No Sale) − (Round, No Sale); Pathway B = (Round, Sale) − (Round, No Sale). If interaction exists, the main effects still estimate the average effect of each factor across levels of the other factor, but the pure pathway estimates are not separable. |

---

## 12. Statistical Model and Analysis Equation

### Primary specification (ITT):

```
Y_igp = α + β × T_g + Σ_k γ_k × C_{p,k} + Σ_t δ_t × W_t + ε_igp
```

where:
- **i**: customer exposure event
- **g**: customer group
- **p**: product
- **Y_igp**: binary purchase outcome
- **T_g**: treatment indicator (1 = salient ending, 0 = round ending) assigned at the group level
- **C_{p,k}**: product-category fixed effects (k categories)
- **W_t**: calendar-week fixed effects
- **ε_igp**: error term, clustered at group level g

**β̂** is the ITT estimate of the price-ending format effect on purchase probability.

### For the 2×2 factorial extension:

```
Y_igp = α + β₁ × SalientEnding_g + β₂ × SaleCue_g + β₃ × (SalientEnding_g × SaleCue_g) + γ × X_igp + ε_igp
```

Interpretation:
- **β̂₁**: Effect of salient ending without a sale cue (Pathway A estimate under additivity)
- **β̂₂**: Effect of sale cue with round ending (Pathway B estimate under additivity)
- **β̂₃**: Interaction effect — whether the format effect is amplified or dampened by the presence of a sale cue

### Linear probability model vs. logit/probit:

The linear probability model (OLS) is preferred for the primary specification due to ease of interpretation of interaction terms and straightforward clustering. Logit or probit models are used in robustness checks.

---

## 13. Robustness, Placebo, Falsification Checks, and Diagnostic Tests

### 13.1 Balance tests

Before analyzing outcomes, test whether treatment and control groups are balanced on pre-treatment covariates:
- Historical purchase rate (overall and by product category)
- Average basket size
- Recency of last purchase
- Product-category mix exposed to

Report standardized mean differences for each covariate. If any covariate shows a large imbalance (standardized difference > 0.1), include it as a control and note the potential threat to randomization.

### 13.2 Placebo outcomes

Test whether the treatment predicts outcomes that **should not** be affected by the price-ending format:
- Purchase of products in categories where the format was **not** manipulated (placebo products). If the treatment indicator predicts placebo-product purchases, this suggests a group-level confound (e.g., one group has systematically higher purchase propensity for reasons unrelated to the format manipulation).
- Pre-treatment purchase behavior (retrospectively). If "assignment" predicts past purchases before the experiment began, randomization failed.

### 13.3 Alternative price-ending specifications

Test whether the effect is specific to the chosen salient ending (e.g., .99) or generalizes to other endings:
- Compare .99 vs. .00 (primary)
- Compare .95 vs. .00
- Compare .90 vs. .00
- Compare .99 vs. .49 (both "salient" but different magnitudes)

If the effect is specific to one ending pattern, this supports a learned-association mechanism (Pathway B). If the effect generalizes across multiple salient endings, this supports a perceptual-processing mechanism (Pathway A).

### 13.4 Price-level sensitivity

Vary the absolute price level for the same ending format:
- Test .99 vs. .00 at ¥10/¥20/¥50/¥100 thresholds
- If the format effect is proportionally larger at lower price points, this is consistent with left-digit bias models.

### 13.5 Attrition/dropout check

Compare the proportion of customers in each arm who:
- Are exposed to at least one focal product
- Complete any purchase
- Have missing outcome data

Differential dropout would violate Assumption A4 and suggest the format itself affects whether customers engage with the offer at all.

### 13.6 Randomization inference

As a nonparametric robustness check, conduct Fisher randomization inference: simulate the null distribution of β̂ by randomly reassigning the treatment indicator across groups (or customers, depending on the assignment unit) and re-estimating the model. Report the randomization-based p-value alongside the model-based p-value.

---

## 14. Heterogeneity Analysis

### 14.1 By customer familiarity (Pathway C test)

Operationalize familiarity as:
- Whether the customer has previously purchased the focal product category (binary)
- Number of prior purchases in the category (count)
- Whether the customer has previously purchased the exact focal product (binary)

Estimate:

```
Y_igp = α + β₁ × T_g + β₂ × Familiarity_i + β₃ × (T_g × Familiarity_i) + γ × X_igp + ε_igp
```

**Prediction under Pathway C:** β̂₃ < 0. The format effect is weaker (less positive) for customers with higher familiarity, because familiar customers can benchmark the price against memory and are less influenced by the format cue.

If β̂₃ ≈ 0, the information-environment mechanism (Pathway C) is not supported, and the format effect operates similarly regardless of customer knowledge.

### 14.2 By product category

Test whether the format effect varies across product categories (e.g., groceries vs. electronics vs. apparel). If some categories show larger effects, this may reflect differences in typical pricing conventions (some categories more commonly use .99 endings, strengthening the learned association) or differences in customer price knowledge across categories.

### 14.3 By absolute price tier

Test whether the format effect is concentrated at specific price tiers (e.g., just below round-number thresholds such as ¥10, ¥50, ¥100). An effect concentrated at threshold boundaries would support a left-digit-bias interpretation (Pathway A).

### 14.4 By discount depth (if sale cues present)

In the 2×2 factorial design: test whether the format effect interacts with the magnitude of the discount. If the format effect is larger when the discount is small or zero, this supports the interpretation that the format itself substitutes for a substantive discount signal.

---

## 15. Measurement, Compliance, Missingness, Spillover, and Implementation Limits

### 15.1 Measurement

- **Price-ending format:** Measured without error (the researcher controls it), but the *customer's perception* of the format is not measured. Without eye-tracking or explicit attention checks, we cannot distinguish between "the format has no effect" and "customers did not notice the format."
- **Purchase outcome:** Assumed accurately recorded in the retailer's transaction system. This is standard.
- **Familiarity proxy:** Based on purchase history, which may be incomplete if customers use multiple accounts or purchase through different channels (online vs. in-store).

### 15.2 Compliance

- **One-sided noncompliance:** Customers in the treatment arm may not notice the salient ending (effectively receiving the control). This biases the ITT toward zero relative to the treatment-on-the-treated (TOT) effect but does not bias the ITT itself.
- **Two-sided noncompliance:** If customers in the control arm are exposed to salient endings through other channels (e.g., seeing a friend's screen, seeing the price in a search results page with a different format), the ITT is attenuated. Monitoring for cross-arm exposure is recommended.
- **TOT estimation:** If the format-exposure status can be measured (e.g., through page-view logging that confirms the format version was served), the TOT can be estimated via instrumental variables using random assignment as the instrument.

### 15.3 Missingness

- Customers who never view the focal product page have no outcome: they neither purchased nor did not purchase the focal item. These observations are structurally missing rather than zero-purchases. The analysis should be conditional on exposure (having viewed the offer), with a separate analysis of whether treatment assignment affects the probability of viewing the focal product at all.
- If missingness is differential by arm (e.g., the salient ending attracts more product-page views), the exposure-conditional analysis may be biased. Report both the unconditional ITT (all assigned customers) and the exposure-conditional analysis.

### 15.4 Spillover / SUTVA violations

- **Within-household spillover:** If two members of the same household are assigned to different arms and discuss prices, SUTVA is violated. Mitigation: assign at the household or geographic level rather than the individual level.
- **Cross-product spillover:** The format of one product's price may affect demand for other products (complements or substitutes). The primary analysis focuses on focal-product demand only; cross-product effects require separate modeling.
- **Platform-level spillover:** On e-commerce platforms, search result pages or recommendation algorithms may display prices in a format that overrides the experimental assignment. Mitigation: ensure the experiment controls the display format across all touchpoints for the focal products.

### 15.5 Implementation limits

- **Retail environment constraints:** The retailer may resist showing different prices (even ¥0.01 different) to different customers for the same product, due to fairness concerns or regulatory constraints. If so, the design must use geographic or temporal variation instead of individual-level variation, which may introduce confounding.
- **Sample size and power:** The packet does not specify the number of customer groups or customers. Minimum detectable effect (MDE) calculations should precede the experiment. With group-level assignment and clustered errors, power depends on the number of groups, not the number of customers.
- **Duration:** The experiment must run long enough to capture repeat-purchase behavior and to avoid novelty effects from the format change, but not so long that competitive responses or seasonal changes confound the results.

---

## 16. Failure Modes and Alternative Explanations

| Failure mode | Description | Detection strategy |
|---|---|---|
| **Randomization failure** | Treatment and control groups differ on pre-treatment characteristics despite intended randomization. | Balance tests (Section 13.1); Fisher randomization inference |
| **Novelty effect** | Customers in the treatment arm respond to the unusual format (if the retailer normally uses round prices), not to the format per se. The effect decays over time. | Time-trend analysis within the experiment; test whether the effect size changes over the experiment duration |
| **Demand substitution** | The format increases demand for the focal product but reduces demand for other products in the retailer's assortment. The net effect on retailer revenue is zero or negative. | Track basket-level outcomes (total spend, category-level substitution) |
| **Strategic customer behavior** | Customers learn to associate the treatment condition with better deals and selectively shop in that condition. | Monitor for treatment-arm switching or differential repeat-visit patterns |
| **Experimenter demand / Hawthorne effect** | The act of running an experiment changes customer or staff behavior. | Compare experimental-period demand to pre-experiment baseline for both arms |
| **Seasonal confounding** | If the experiment coincides with a demand shock (holiday, payday, weather event), the treatment effect may be confounded. | Calendar-week fixed effects; pre-registered experiment window |
| **Price-image spillover** | Repeated exposure to .99 endings may change customers' overall perception of the retailer's price image, affecting demand for all products (including control-arm products). | Track long-term changes in control-arm demand relative to a never-treated holdout group |
| **Category-specific conventions** | If a product category conventionally uses .99 endings, the round-ending control may appear strange or suspicious, inflating the estimated treatment effect. | Include a check: survey a subset of customers on perceived "normalness" of the displayed price |

---

## 17. What Cannot Be Claimed

Based on the available information and the proposed design, the following claims **cannot** be made:

1. **The effect generalizes to all retailers, product categories, or contexts.** The estimate is conditional on the specific retailer, product set, and customer population studied.

2. **The psychological mechanism (Pathway A) is definitively isolated from bargain signaling (Pathway B) without the 2×2 factorial extension.** In the basic two-arm design, we estimate the total effect of the format — the sum of perceptual and signaling channels. Only the factorial extension can begin to separate them, and even then, the separation relies on the assumption that the "sale cue" manipulation is a valid and complete proxy for bargain-signal perception.

3. **The effect is permanent.** The experiment captures the effect during a finite window. Long-run effects (after customers adapt to the format, or after competitors respond) are not identified.

4. **The effect is the same for all salient endings.** The design tests specific endings (e.g., .99 vs. .00). Generalization to other endings (.95, .49, .98) requires additional treatment arms.

5. **The effect operates through conscious processing.** Without process-tracing data (eye-tracking, response-time measurement, think-aloud protocols), we cannot distinguish conscious deliberation from automatic, non-conscious processing. We can only infer mechanism from the pattern of results.

6. **The welfare or profitability implications.** The design estimates demand effects. Whether the demand increase is profitable (net of the ¥0.01 revenue reduction per unit, any cannibalization, and any long-run price-image effects) requires a separate cost-benefit analysis.

7. **The effect in the absence of any ¥0.01 price difference.** The design necessarily confounds the format with a trivial price difference. While the ¥0.01 difference is economically negligible, a purist might argue that the design does not estimate the effect of format *with identical absolute price*. This is a conceptual rather than practical limitation.

---

## 18. Additional Data Needed

To strengthen the design beyond what the packet provides:

| Data need | Purpose |
|---|---|
| **Historical pricing and sales data** (12+ months) | Pre-trend analysis, power calculations, familiarity-proxy construction, baseline demand estimation |
| **Customer-level identifiers with purchase history** | Familiarity stratification (Pathway C test), balance checks, heterogeneity analysis |
| **Product-category taxonomy** | Category fixed effects, category-level heterogeneity analysis |
| **Sale/markdown flags and discount depth** | Construct the sale-cue dimension for the 2×2 factorial design; distinguish format effects from genuine discount effects |
| **Customer-group assignment rule** | Verify that assignment is random or to model the selection process if not |
| **Page-view / impression data** | Measure exposure, compute exposure-conditional effects, check for differential exposure |
| **Basket-level transaction data** | Measure spillover, substitution, and net revenue effects |
| **Post-experiment survey (optional)** | Measure explicit price recall, perceived expensiveness, and deal perception — to validate mechanism inferences |

---

## 19. Threat-Response Table

The task packet does not explicitly request this section. Included for completeness.

| Threat to validity | Response |
|---|---|
| **Selection bias (managerial assignment)** | Eliminated by randomization of format across customer groups for the same products |
| **History / time confounding** | Addressed by concurrent exposure in both arms; calendar-week fixed effects |
| **Maturation (customer adaptation)** | Monitored via time-trend analysis within experiment |
| **Instrumentation / measurement error** | Format is researcher-controlled (no measurement error); purchase is system-recorded (low error) |
| **Differential attrition** | Tested by comparing exposure and dropout rates across arms |
| **SUTVA violation** | Addressed by group-level assignment at a sufficiently aggregated level (geography, household); monitored for cross-arm contamination |
| **Hawthorne effect** | Compared to pre-experiment baseline; use of a holdout group if feasible |
| **Statistical power** | Pre-registered MDE calculation; cluster-robust standard errors |
| **Multiple comparisons** | Pre-specify primary outcome and primary heterogeneity cut; apply Holm-Bonferroni correction for any exploratory tests |

---

## 20. Claim-Evidence Table

| # | Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|---|
| 1 | Salient terminal-digit pricing increases purchase probability relative to round-number pricing, holding the absolute price level essentially constant. | ITT estimate β̂ from the between-group randomized experiment | Causal | High (under randomization assumptions) | β̂ ≤ 0 with confidence interval excluding economically meaningful positive values; failed balance tests indicating non-random assignment |
| 2 | The format effect is not fully explained by generic discount signaling. | β̂₁ > 0 in the Salient-No-Sale cell of the 2×2 factorial design (format effect with no sale cue present) | Mechanism / Causal | Moderate (requires factorial design and valid sale-cue manipulation) | β̂₁ ≈ 0 while β̂₃ > 0 (the format effect appears only when a sale cue is present, indicating it operates entirely through bargain-signal interaction) |
| 3 | The format effect is larger for customers with low product familiarity. | β̂₃ < 0 in the treatment × familiarity interaction model | Heterogeneity / Mechanism | Moderate (requires valid familiarity proxy) | β̂₃ ≈ 0; the format effect is constant across familiarity levels |
| 4 | Managerial selection does not explain observed format-demand associations. | Non-significant treatment effect on placebo products; balanced pre-treatment covariates; Fisher randomization p-value consistent with model-based inference | Design validity | High (under successful randomization) | Significant placebo effects; covariate imbalance; divergence between randomization and model-based inference |
| 5 | The format effect generalizes across multiple salient endings (not specific to .99). | Consistent positive effects for .95, .90 endings compared to round in alternative-specification robustness checks | External validity / Mechanism | Moderate (requires additional treatment arms) | Effect is specific to .99 and zero or reversed for other salient endings |
| 6 | The format effect is not driven by novelty or experimenter effects. | Stable or non-decreasing effect over experiment duration; no discontinuity relative to pre-experiment baseline | Design validity | Moderate (requires sufficient experiment duration and pre-period data) | Effect diminishes monotonically to zero over the experiment window |

---

## Summary of Causal Identification Logic

The central identification strategy is straightforward: **randomly assign the price-ending format across customer groups for the same products, held constant on all other dimensions, and compare purchase outcomes.** The randomization breaks the managerial-selection confound that plagues observational pricing data. The between-subjects, within-product, concurrent-exposure design eliminates the major alternative explanations. Mechanism separation (Pathway A vs. B) requires the additional structure of a 2×2 factorial design crossing format with sale cues. The information-moderation hypothesis (Pathway C) is tested through pre-registered heterogeneity analysis by customer familiarity. All claims are bounded by the specific retailer, product set, customer population, and time window of the experiment.

## Tool Log Summary

- actual tool use: none
- trajectory `toolMetas`: []
- toolCall count: 0
- toolResult count: 0
- session_id: isolated_20260529_115127_52386_10
- session_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260529_115127_52386_10.jsonl
- trajectory_log: /Users/jiangcanxiang/.openclaw/agents/benchmark_isolated/sessions/isolated_20260529_115127_52386_10.trajectory.jsonl

## Operator Notes

- duration_ms: 190423
- stderr_excerpt: [plugins] plugins.allow is empty; discovered non-bundled plugins may auto-load: qqbot (/Users/jiangcanxiang/.openclaw/npm/node_modules/@openclaw/qqbot/dist/index.js), openclaw-weixin (/Users/jiangcanxiang/.openclaw/npm/node_modules/@tencent-weixin/openclaw-weixin/dist/index.js). Set plugins.allow to explicit trusted ids. [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/0-autoresearch-skill resolved=~/.orchestra/skills/0-autoresearch-skill [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/brainstorming-research-ideas resolved=~/.orchestra/skills/21-research-ideation/brainstorming-research-ideas [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed root=~/.openclaw/skills reason=symlink-escape requested=~/.openclaw/skills/creative-thinking-for-research resolved=~/.orchestra/skills/21-research-ideation/creative-thinking-for-research [skills] Skipping escaped skill path outside its configured root: source=openclaw-managed r
