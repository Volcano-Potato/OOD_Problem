# Agent Design Memo

## Research Question
What is the causal effect of making an add-on charge visible at the point of product choice (visible all-in pricing) on consumer demand, holding the underlying economic price constant? ---

## Target Estimand


## Treatment And Outcomes


## Identification Logic
The central identification problem is that treated and untreated product-category-store cells may differ in ways that independently affect demand trajectories. The retailer selects which categories and stores receive the display change — selection is non-random and may be correlated with demand characteristics (e.g., high-volume categories, stores with price-sensitive customers, categories where add-on charges are large). The challenge is to construct a credible counterfactual for what would have happened to treated cells had the display not changed. This breaks down into four sub-problems: 1. Selection into treatment: Treated cells may have different baseline demand levels or trends. 2. Confounding shocks: Store-level or time-level events may coincide with the display change. 3. Simultaneous price changes: If actual shelf prices or add-on charge rates change during the intervention wind

## Defensibility Assessment
Yes, credible causal identification is possible under the design described below, provided that: - The add-on charge amount does not change during the analysis window, and actual shelf prices are observed and can be controlled. - Multiple pre-intervention time periods are available to assess and support parallel pre-trends. - At least one credible comparison group exists (untreated categories within treated stores or treated categories in untreated stores). - The number of treated clusters is sufficient for cluster-robust inference (at minimum, treatment varies across enough store-category cells to avoid overfitting). The primary threat that cannot be fully ruled out with the given data structure is the distinction between salience (cognitive prominence) and information (consumers learning the add-on charge amount for the first time). Both are consequences of the same display change, and

## Proposed Design
### 9.1 Core Design: Staggered Difference-in-Differences with High-Dimensional Fixed Effects The design exploits three sources of variation: 1. Within-store, across-category: Compare pre-post changes for treated categories vs. untreated categories in the same store. This differences out store-level time shocks. 2. Within-category, across-store: Compare pre-post changes for the same category in treated stores vs. untreated stores. This differences out category-level time shocks. 3. Within-category-store, across-time: Compare post-treatment periods to pre-treatment periods, using the pre-period to estimate counterfactual trends. The preferred specification combines all three, using a two-way fixed effects (TWFE) event-study framework: Step 1 — Event-study specification: \[ Y_{it} = \alpha_i + \lambda_t + \sum_{k = -K, k \neq -1}^{L} \beta_k \cdot \mathbf{1}[t - g_i = k] + \gamma \cdot X_{it} + \varepsilon_{it} \] where: - \(Y_{it}\): quantity sold (log or level) for cell \(i\) at time \(t\) - \(\alpha_i\): product-category × store fixed effect (absorbs time-invariant cell characteristics) - \(\lambda_t\): time (week) fixed effect (absorbs common time shocks) - \(g_i\): the first time period cell \(i\) is treated - \(k\): event time relative to treatment (negative = pre-treatment le

## What Cannot Be Claimed
1. Pure salience (as distinct from information): The design estimates the combined effect of making the add-on charge visible. This effect operates through both (a) increasing the cognitive salience of a charge consumers already knew about and (b) providing new information to consumers who were previously unaware of the charge. These cannot be separated without additional data on consumer knowledge. 2. Long-run equilibrium effects: The intervention window covers multiple weeks. If consumers eventually learn about add-on charges through experience (checkout receipts, word of mouth, media), the estimated effect may overstate the long-run impact. The design captures short-to-medium-run demand responses only. 3. Welfare effects: Changes in quantity demanded do not directly imply welfare changes. Consumers may be better off (making more informed choices) or worse off (overreacting to a charge
