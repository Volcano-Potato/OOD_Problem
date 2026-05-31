# Stage 5: Final Design Memo

**Case ID:** C019 (Perturbed Variant)
**Perturbation:** Pre-trip planned basket and mission capture removed.
**Stage 4 Critic Reconciliation:** All three causal candidates graded `not_defensible`; descriptive fallback graded `defensible_with_caveats`. I accept all four verdicts and structure this memo accordingly.

---

## 1. Executive Summary

The perturbation that defines this variant — removal of the reliable pre-trip planned basket and mission capture — is fatal to causal identification of the effect of in-store route length on unplanned spending. The Stage 4 critic correctly identifies that all three causal candidates (`prompt-zone-iv`, `within-trip-sequential`, `selection-on-observables-matching`) depend on conditions the perturbation breaks: (a) the ability to separate planned from unplanned spending, (b) the ability to control for or instrument trip mission, and (c) the ability to test exclusion or unconfoundedness assumptions using pre-trip benchmarks. No packet-local evidence the critic missed can rehabilitate any of these designs.

The strongest defensible analysis is the descriptive-correlation-decomposition fallback (`descriptive-correlation-decomposition`), which maps partial associations between route length, prompt exposure, and checkout outcomes without claiming causal identification. This memo presents that design, explicitly downgrades all causal claims, and documents what cannot be claimed in light of the critique.

---

## 2. Research Question

Does longer in-store travel cause higher unplanned spending when no reliable pre-trip basket information is available?

As the perturbation makes causal identification of this question impossible with the provided data, the memo also addresses the reframed question: *What descriptive and predictive associations between route length, prompt exposure, and checkout outcomes can be credibly documented, and what additional data would be needed to recover a causal design?*

---

## 3. Target Estimand or Strongest Defensible Estimand

**No causal estimand is defensible.** The strongest defensible analytic target is a set of partial correlations:

- **Primary:** Partial correlation between observed route length and total checkout spending, conditional on observable shopper demographics, store familiarity, time-of-day, and day-of-week.
- **Decomposition 1:** Partial correlation between route length and checkout spending, stratified by whether the shopper passed a category-level prompt before purchasing from that category.
- **Decomposition 2:** Partial correlation between prompt-pass indicators and category-level purchase incidence/spending, stratified by shopper demographic segments.
- **Decomposition 3:** Association between prompt-pass indicators and a constructed "unplanned spending" proxy (e.g., spending on categories the shopper does not purchase on a majority of their observed trips, if repeat-visit data are available; or categories adjacent to but not directly on the shopper's most efficient path), acknowledged as unvalidated.

These are all descriptive or predictive associations. None carries a causal interpretation.

---

## 4. Treatment or Exposure and Main Outcomes

| Construct | Variable | Type |
|---|---|---|
| Exposure | Actual route length (continuous, meters or steps) | Endogenous continuous exposure |
| Exposure | Indicator for whether shopper passed a category-level prompt before purchasing that category | Binary, category-trip level |
| Primary outcome | Total checkout spending (currency units) | Continuous, trip level |
| Secondary outcome | Number of distinct categories purchased | Count, trip level |
| Secondary outcome | Spending per category passed (with/without prompt) | Continuous, category-trip level |
| Proxy outcome | Unplanned spending proxy (see Section 15 for construction and limitations) | Continuous, trip level |

Route length is an *exposure*, not a *treatment*. The packet provides no source of exogenous variation in route length, and Stage 4 confirms no credible instrument or conditioning strategy survives the perturbation.

---

## 5. Data Structure Summary

| Dimension | Description |
|---|---|
| Unit of observation | Individual shopping trip |
| Time structure | Single-trip, cross-sectional (primarily; repeat visits possible but not guaranteed) |
| Stage 1 (Entry) | Shopper enters; no validated pre-trip basket or mission capture available |
| Stage 2 (In-trip) | Route path observed; category-level prompt exposure observed |
| Stage 3 (Checkout) | Final basket and total spending observed |
| Key missing element | Reliable pre-trip planned basket or intended mission (the perturbation) |
| Available covariates | Shopper demographics, store familiarity (if available), time-of-day, day-of-week |
| Sample | Trips with usable route measures and linked checkout records |

The perturbation removes the variable that would anchor identification: what the shopper intended to buy before entering the store. Without it, no design can credibly isolate the causal effect of route length on the *unplanned* component of spending.

---

## 6. Relevant Causal Mechanisms

The packet and institutional context suggest three mechanisms linking route length to spending, operating through different channels with different policy implications:

1. **Route-induced impulse (the mechanism of interest):** Longer or more circuitous walking paths expose shoppers to more products and categories, triggering unplanned purchases they would not have made on a direct path. This is the mechanism the retailer hopes to exploit with path-inducing promotions.

2. **Prompt salience (the direct reminder channel):** A category-level prompt (e.g., "Snacks — 2 for $5") may directly increase demand for that category through salience or price information, without changing the shopper's walking path. This mechanism operates even if route length is unchanged.

3. **Trip-mission-driven co-determination (the confounding mechanism):** The shopper's trip mission — whether a major weekly stock-up, a quick fill-in, or a browse-heavy leisure trip — jointly determines both how far they walk and how much they spend. This mechanism generates a non-causal positive correlation between route length and spending.

The perturbation makes it impossible to separate mechanism 1 from mechanisms 2 and 3 using the available data.

---

## 7. Main Identification Challenge

The identification challenge is twofold and each component is individually fatal:

**Challenge 1: Route length is endogenously chosen.** Shoppers choose their walking path based on their trip intentions, store familiarity, time constraints, and physical ability. Trip mission — the dominant confound — jointly determines both route length and spending. The perturbation removes pre-trip mission data, so this confound is unobserved at the trip level. No covariate set available in the packet (demographics, store familiarity, time-of-day) can proxy for the specific trip's mission: two demographically identical shoppers entering at the same time can have fundamentally different trip objectives with systematically different route-length/spending relationships.

**Challenge 2: "Unplanned spending" is unmeasurable.** The research question targets *unplanned* spending, not total spending. Without the pre-trip planned basket, there is no individual-trip-level definition of what is planned versus unplanned. Any proxy constructed from checkout data alone — e.g., items from rarely-purchased categories, items from categories adjacent to the shopper's most efficient path, prompt-matched items — is an unvalidated classification that will misclassify some planned purchases as unplanned and vice versa. The packet provides no household purchase-history panel to calibrate such proxies.

These two challenges interact: even if route length were exogenously assigned (solving challenge 1), we would still not know whether the additional spending from a longer route was planned or unplanned (challenge 2 remains).

---

## 8. Whether Credible Causal Identification Is Possible

**No.** Credible causal identification of the effect of route length on unplanned spending is not possible with the data described in this packet.

The Stage 4 critic examined all three causal candidate designs and found each `not_defensible`:

- **`prompt-zone-iv`**: The exclusion restriction is unverifiable without pre-trip baskets (prompts may affect spending directly through salience, not only through route length), and the packet provides no evidence of exogenous prompt assignment.
- **`within-trip-sequential`**: Visit order is endogenous to unobserved purchase intentions, and trip-stage effects (fatigue, budget depletion) are inseparable from route-position effects without pre-trip benchmarks.
- **`selection-on-observables-matching`**: The dominant confound — trip mission — is unobserved by construction (the perturbation), and the outcome "unplanned spending" is unmeasurable, forcing reliance on total spending.

No packet-local evidence the critic missed can rehabilitate any of these designs. The perturbation is not a marginal data limitation; it removes the single most important variable for causal identification.

---

## 9. Proposed Empirical Design: Descriptive Correlation Decomposition

The proposed design is a descriptive decomposition of associations between route length, prompt exposure, and checkout outcomes, using only the data the packet provides. It makes no causal identification claims.

### Analysis Components

**A. Aggregate route-spending association**

Regress total checkout spending on route length, controlling for observable covariates:

$$ \text{Spending}_i = \alpha + \beta \cdot \text{RouteLength}_i + \gamma' X_i + \varepsilon_i $$

where $X_i$ includes shopper demographics, store familiarity (if available), time-of-day fixed effects, and day-of-week fixed effects. Interpret $\hat{\beta}$ as the partial association between route length and total spending, **not** as a causal effect. Report it alongside the unconditional correlation for transparency.

**B. Prompt-exposure decomposition**

For each category $c$ and trip $i$, construct the indicator $\text{PassedPrompt}_{ic} = 1$ if the shopper's route passed a prompt for category $c$ before (or without) purchasing from category $c$. Estimate:

$$ \text{Spending}_{ic} = \alpha + \beta_1 \cdot \text{RouteLength}_i + \beta_2 \cdot \text{PassedPrompt}_{ic} + \beta_3 \cdot (\text{RouteLength}_i \times \text{PassedPrompt}_{ic}) + \gamma' X_i + \varepsilon_{ic} $$

This decomposes the route-spending association into: (a) the association for categories without prompt exposure, (b) the additional association when a prompt is passed, and (c) the interaction. Report all coefficients with the caveat that these are descriptive patterns, not causal decomposition.

**C. Category-level prompt-response patterns**

For each category, estimate the association between passing a prompt and purchasing from that category, conditional on demographics and trip timing:

$$ \text{Purchase}_{ic} = \alpha_c + \delta_c \cdot \text{PassedPrompt}_{ic} + \gamma_c' X_i + \varepsilon_{ic} $$

Rank categories by the magnitude of $\hat{\delta}_c$. This provides the retailer with suggestive evidence about which categories show the strongest prompt-purchase associations — useful for exploratory business decisions about prompt placement, but not causal evidence that prompts *cause* purchases.

**D. Segment-level heterogeneity**

Repeat analyses A–C within shopper demographic segments (age groups, inferred income brackets if available, store-familiarity levels) and time windows (weekday morning, weekday evening, weekend). Report segment-level patterns descriptively.

**E. Sensitivity of "unplanned" proxies**

If the researcher constructs an "unplanned spending" proxy (e.g., spending on categories not purchased on a majority of a shopper's observed trips, if repeat-visit data are available), report:
- The distribution of the proxy across trips.
- How the route-spending association changes when using the proxy versus total spending.
- A sensitivity analysis varying the proxy's classification threshold.

All results must be presented with explicit disclaimers that the proxy is unvalidated and that associations with the proxy do not identify causal effects on unplanned spending.

---

## 10. Why the Design Is Valid (as Descriptive) and Why Causal Identification Is Not Credible

### Why causal identification is not credible

The perturbation removes the data element — the pre-trip planned basket — that would be required to:

1. **Define the outcome:** "Unplanned spending" cannot be separated from total spending at the individual-trip level without knowing what was planned.
2. **Control for the dominant confound:** Trip mission (stock-up vs. fill-in vs. browse) simultaneously determines route length and total spending. Demographics and time-of-day are poor proxies for trip-level intentions.
3. **Test or validate any causal identification strategy:** The exclusion restriction in an IV design, the unconfoundedness assumption in matching, and the visit-order independence assumption in a within-trip design all require pre-trip baseline data for falsification.

The Stage 4 critic confirms these failures for each causal candidate with packet-grounded reasoning, and no packet-local evidence contradicts those assessments.

### Why the descriptive design is valid (on its own terms)

The descriptive-correlation-decomposition design is valid because:

1. It uses only variables actually present in the packet's data structure: route length (observed), prompt exposure (observed), checkout spending (observed), demographics and store familiarity (available).
2. It makes no causal identification assumptions. All estimates are presented as partial associations or correlations, with explicit acknowledgment that they do not identify causal effects.
3. It answers the packet's explicit question: "What descriptive or predictive analyses are still defensible?"
4. It provides actionable exploratory information: which categories show the strongest prompt-purchase associations, how route length and spending covary across segments, and how sensitive any "unplanned" proxy is to its construction choices.

The design's limitation — that it cannot answer the causal research question — is not a design flaw; it is a data constraint that the design honestly acknowledges.

---

## 11. Required Assumptions

The descriptive design makes no causal identification assumptions. It requires only:

| Assumption | Type | Defensibility |
|---|---|---|
| Route measures are accurate and consistently recorded across trips | Measurement | Reasonable if the retailer has operational route-tracking infrastructure |
| Checkout records are complete and correctly linked to route measures | Data linkage | Reasonable if the retailer has standard POS-route integration |
| Prompt-exposure coding is accurate (shopper actually saw the prompt when passing its zone) | Measurement | Strong; the packet says "category-level prompts or stimuli may be observed" but does not confirm that *viewing* (as opposed to *availability*) is measured |
| Demographics and store-familiarity data are available and coded consistently | Measurement | Conditional on "if available" language in the packet |
| No systematic differences in data quality across store zones, times, or shopper types | Data quality | Requires diagnostic checks (see Section 13) |

Notably, the design does **not** assume unconfoundedness, exclusion restrictions, independence of visit order, or any other causal identifying condition.

---

## 12. Statistical Model or Analysis Equation

The core analysis is a set of linear regression models. The primary specification:

**Level 1: Trip-level aggregate association**

$$ Y_i = \alpha + \beta R_i + \sum_{k} \gamma_k D_{ik} + \sum_{t} \delta_t T_{it} + \sum_{d} \theta_d W_{id} + \varepsilon_i $$

Where:
- $Y_i$: total checkout spending for trip $i$
- $R_i$: observed route length (continuous, standardized)
- $D_{ik}$: demographic covariate $k$ for the shopper in trip $i$
- $T_{it}$: time-of-day indicator $t$
- $W_{id}$: day-of-week indicator $d$

**Level 2: Category-trip-level prompt decomposition**

$$ Y_{ic} = \alpha + \beta_1 R_i + \beta_2 P_{ic} + \beta_3 (R_i \times P_{ic}) + \gamma' X_i + \eta_c + \varepsilon_{ic} $$

Where:
- $Y_{ic}$: spending on category $c$ in trip $i$
- $P_{ic}$: indicator for whether the shopper passed a prompt for category $c$ before (or without) purchasing from it
- $\eta_c$: category fixed effects

**Level 3: Category-level prompt-purchase association**

$$ \text{Purchase}_{ic} = \alpha_c + \delta_c P_{ic} + \gamma_c' X_i + \varepsilon_{ic} $$

Estimated separately for each category $c$, with $\hat{\delta}_c$ ranked across categories.

**Level 4: Unplanned-proxy sensitivity**

For a given proxy threshold $\tau$ (e.g., classify a category as "unplanned" if the shopper purchases from it in fewer than $\tau$% of their observed trips):

$$ U_i(\tau) = \sum_c Y_{ic} \cdot \mathbf{1}[\text{Freq}_{ic} < \tau] $$

Then estimate Level 1 with $U_i(\tau)$ as the outcome, varying $\tau$ over a grid (e.g., 0.1, 0.25, 0.5) to assess sensitivity.

All standard errors should be clustered at the shopper level if repeat-visit data are available, or use heteroskedasticity-robust standard errors in the purely cross-sectional case.

---

## 13. Robustness, Placebo, Falsification Checks, or Diagnostic Tests

Because the design is descriptive, "placebo" and "falsification" checks in the causal sense are not applicable. The following diagnostic and sensitivity checks are recommended:

| Check | Description | Purpose |
|---|---|---|
| **Route-length measurement sensitivity** | Re-estimate using alternate route-length definitions (total distance vs. excess distance over shortest path, binned/quantile versions) | Assess whether associations are sensitive to the operationalization of route length |
| **Covariate balance diagnostics** | Compare covariate distributions across route-length quartiles; report standardized differences | Characterize selection patterns that preclude causal interpretation |
| **Prompt-exposure coding sensitivity** | Vary the definition of "passed a prompt" (strict: must walk within X meters of display; lenient: any prompt in visited zone) | Assess sensitivity of prompt-purchase associations to exposure coding |
| **Outcome-window sensitivity** | If trip-duration data are available, estimate associations within duration terciles | Assess whether route-spending associations are confounded by trip duration |
| **Leave-one-category-out** | Re-estimate Level 2 excluding each category in turn; report whether any single category drives the aggregate association | Identify category-specific patterns |
| **Time-window stratification** | Estimate separately for weekday mornings, weekday afternoons, weekday evenings, and weekends | Assess whether associations differ by time context (proxy for trip-mission types, albeit weakly) |
| **Data-quality diagnostics** | Tabulate missingness rates for route measures, checkout linkage, and prompt coding by store zone and time window | Identify systematic data-quality patterns that could bias associations |
| **Unplanned-proxy sensitivity** | Vary the proxy threshold $\tau$; report range of $\hat{\beta}$ across $\tau$ values | Document how sensitive the "unplanned" spending association is to the proxy's construction |

An important negative result to report: if the partial association between route length and spending is near zero or negative after controlling for observable covariates, this would be informative for the retailer even without causal identification — it would suggest that the raw positive correlation is largely explained by observable shopper and timing characteristics, and that route-length interventions may not have the expected relationship with spending.

---

## 14. Heterogeneity Analysis If Supportable

Heterogeneity analysis is supportable as descriptive stratification. The following dimensions are available in the packet and worth exploring:

| Dimension | Stratification | Rationale |
|---|---|---|
| **Shopper demographics** | Age groups, inferred income (if available) | Different demographic segments may exhibit different route-spending associations due to different shopping styles, budget constraints, or susceptibility to prompts |
| **Store familiarity** | High vs. low familiarity (if measured) | Familiar shoppers may plan routes more efficiently; unfamiliar shoppers may wander more and be more susceptible to prompt-induced category discovery |
| **Time-of-day** | Morning, midday, afternoon, evening | Morning trips may be more mission-driven (fill-in); evening trips more browse-heavy |
| **Day-of-week** | Weekday vs. weekend | Weekend trips more likely to be major stock-ups with systematically different route-spending relationships |
| **Trip duration** | Short, medium, long (if available) | Route-spending associations may differ by trip duration; controlling for or stratifying by duration may reveal whether the route-length association is driven by time-in-store rather than distance-walked |
| **Prompt category type** | Staples vs. discretionary categories | Prompts for staple categories may show weaker associations (shoppers buy them anyway); discretionary category prompts may show stronger associations |

All heterogeneity results must be reported as descriptive patterns, with explicit acknowledgment that segment-level differences in the route-spending association may reflect differences in unobserved trip-mission composition across segments rather than heterogeneous causal effects.

---

## 15. Measurement, Compliance, Missingness, Spillover, or Implementation Limits

### Measurement Limits

| Issue | Severity | Mitigation |
|---|---|---|
| **Route length measurement error**: The packet says "route through the store is measured" but does not specify the technology (RFID, camera-based, WiFi triangulation). Different technologies have different spatial resolution and may systematically miss certain movements (e.g., vertical movement between floors, brief pauses). | Moderate | Conduct sensitivity analysis with binned/coarsened route-length measures; measurement error in the exposure attenuates associations toward zero, so reported associations are conservative estimates of the true association (though still not causal). |
| **Prompt exposure ≠ prompt viewing**: The packet says "category-level prompts or stimuli *may be observed*" (emphasis added). It does not confirm that the data capture whether the shopper *actually saw* the prompt, only that they were in its vicinity. | High | Report prompt-exposure results as associations with *availability* of prompts along the route, not with prompt *viewing* or *attention*. This is a form of non-differential misclassification that attenuates associations. |
| **Unplanned spending proxy misclassification**: Any proxy constructed without pre-trip baskets will misclassify some planned purchases as unplanned and vice versa. The packet provides no household purchase history to calibrate. | Fatal (for the causal question); manageable (for sensitivity analysis) | Report results using multiple proxy definitions and total spending side by side; treat the proxy as an exploratory outcome, not a validated measure. |

### Compliance

Compliance is not applicable in the traditional sense (there is no assigned treatment). However, the packet notes that "Shoppers may ignore or partially respond to prompts." In the descriptive framework, this is captured by the indicator $\text{PassedPrompt}_{ic}$, which is an exposure measure, not a treatment-assignment measure. The descriptive association between $\text{PassedPrompt}_{ic}$ and $\text{Purchase}_{ic}$ reflects the mixture of shoppers who noticed and responded to the prompt and those who did not.

### Missingness

| Source | Concern | Diagnostic |
|---|---|---|
| Route measures unavailable for some trips | If route-data availability is correlated with trip characteristics (e.g., longer trips have more complete tracking), the sample is selected on the exposure | Compare demographic and spending distributions between trips with and without usable route measures |
| Checkout linkage failure | If linkage failure is correlated with basket size or composition | Compare linked vs. unlinked transaction characteristics |
| Prompt-exposure coding gaps | If prompt data are missing for certain zones or times | Tabulate missingness by zone and time window |

### Spillover

The packet notes "Minimal cross-shopper interference; the main issue is endogenous within-trip exposure." Cross-shopper spillover is not a primary concern for the descriptive design. Within-trip spillover — where a prompt for category A affects purchases in category B — is captured descriptively by the category-level analysis but cannot be causally attributed.

### Implementation Limits

The design requires merging route-tracking data, prompt-exposure data, and checkout records at the trip level. This data infrastructure may not exist. If the retailer cannot link these data sources at the trip level, even the descriptive analysis cannot be executed.

---

## 16. Failure Modes and Alternative Explanations

| Observed Pattern | Alternative Explanation (Non-Causal) | Diagnostic |
|---|---|---|
| Positive partial correlation between route length and spending | Trip-mission confounding: shoppers on major stock-up trips both walk further and spend more. Demographics and time-of-day do not fully control for mission. | Stratify by trip-duration terciles; if route-spending association persists within narrow duration windows, mission confounding is less likely (but not eliminated) |
| Positive association between prompt-pass and category purchase | Reverse causality: shoppers walk past a category *because* they intend to buy from it, not the reverse. The prompt is incidental. | Cannot be diagnosed without pre-trip intentions |
| Late-trip categories show higher spending than early-trip categories | Budget depletion or fatigue, not route-induced impulse. Shoppers may front-load planned purchases and then make smaller impulse buys. | Cannot be diagnosed without pre-trip plans or trip-duration controls |
| Demographic segment A shows stronger route-spending association than segment B | Segment A has different trip-mission composition (e.g., more browse-heavy trips), not a larger causal effect of route length | Cannot be diagnosed without mission data |
| Unplanned-spending proxy shows positive association with route length | Proxy may be systematically correlated with trip mission (e.g., stock-up trips include more "rarely purchased" categories that get misclassified as unplanned) | Sensitivity analysis varying proxy threshold; comparison to total-spending association |

The unifying theme: **every pattern consistent with a causal effect of route length on unplanned spending is equally consistent with trip-mission confounding, which the perturbation renders unobservable.** The descriptive design can document patterns but cannot adjudicate between causal and non-causal explanations.

---

## 17. What Cannot Be Claimed

In light of the Stage 4 critique, the following claims **cannot** be made based on this packet's data:

1. **That longer in-store travel causes higher unplanned spending.** This is the research question and it is unanswerable with the provided data. Any positive association between route length and spending may reflect trip-mission confounding, reverse causality, or prompt-salience effects operating through channels other than route extension.

2. **That any specific route-lengthening intervention (e.g., placing prompts to redirect shopper paths) will increase total or unplanned spending.** Even if a positive descriptive association is observed, it does not imply that an intervention *changing* route length will *change* spending. The association may be entirely driven by shoppers choosing longer routes when they have larger spending needs.

3. **That category-level prompts cause incremental purchases through the route-extension channel (as opposed to the direct salience channel).** The exclusion restriction required to separate these channels is unverifiable without pre-trip baskets. Any prompt-purchase association could reflect direct reminder effects that operate even if the shopper's path is unchanged.

4. **That any constructed "unplanned spending" proxy accurately measures unplanned spending at the individual-trip level.** Without pre-trip baskets as ground truth, the proxy's classification error is unknown and may be systematically correlated with trip characteristics in ways that bias descriptive associations.

5. **That the descriptive associations are externally valid or generalizable to other stores, time periods, or prompt configurations.** The associations are specific to the observed stores, shoppers, and time periods. They carry no causal interpretation, so they do not generalize beyond the estimation sample without strong (and untestable) external-validity assumptions.

6. **That the descriptive design provides "evidence for" or "support for" the effectiveness of path-inducing promotions as a business strategy.** It provides correlational patterns that may inform exploratory decisions (e.g., which categories to test in a future randomized experiment) but does not provide evidence of effectiveness.

---

## 18. Additional Data Needed

To recover a causal design for the effect of route length on unplanned spending, the following data would be needed, in descending order of importance:

| Priority | Data Element | What It Enables |
|---|---|---|
| **Critical** | **Pre-trip planned basket or intended mission**, captured at store entry (e.g., shopper-reported planned categories, mobile-app shopping list, or inferred from household purchase history) | Defines "unplanned spending" at the individual-trip level; controls for the dominant confound (trip mission); enables falsification of exclusion restrictions and within-trip ordering assumptions |
| **Critical** | **Exogenous variation in prompt placement**, such as temporal randomization (different prompts displayed in alternating time windows), spatial randomization (prompt locations rotated across weeks), or zone-level A/B testing | Provides a valid instrument for prompt exposure, enabling IV estimation of prompt effects on route length and spending; the exclusion restriction remains challenging but becomes partially testable with temporal randomization |
| **High** | **Repeat-visit panel data** with household identifiers | Enables within-household differencing that absorbs time-invariant shopper preferences; constructs household-level purchase-frequency baselines for better "unplanned" proxies |
| **High** | **Trip-duration and basket-accumulation metrics** | Enables separation of route-length effects from time-in-store effects and budget-depletion dynamics |
| **Moderate** | **Store-layout change events** (e.g., aisle reconfigurations, category relocations) | Provides quasi-experimental variation in route length for shoppers with fixed purchase intentions visiting the same store before and after a layout change |
| **Moderate** | **Shopper attention or engagement measures** (e.g., gaze tracking, dwell time near prompts) | Enables separation of prompt-exposure from prompt-attention; reduces measurement error in the prompt-exposure variable |
| **Supporting** | **Shopper survey or entry interview** capturing trip mission, time pressure, and planned categories | Provides a validation sample for "unplanned" proxy construction, even if not available for all trips |

The packet perturbation removes the single most important data element (pre-trip baskets). The additional data listed above would address the three remaining identification challenges: endogenous route choice, unmeasured prompt-exposure confounds, and unvalidated outcome measurement. A credible causal design would likely require at least pre-trip mission data *and* one source of exogenous variation in route length or prompt exposure.

---

## 19. Threat-Response Table

| Threat | Source | Severity | Response |
|---|---|---|---|
| **Trip-mission confounding**: Shoppers with larger spending needs walk further; the route-spending association reflects mission, not causation | Unobserved trip mission (perturbation) | **Fatal to causal claims** | Acknowledge explicitly; report all results as descriptive associations; stratify by available proxies (time-of-day, day-of-week) and document that residual confounding is unaddressed |
| **Unmeasurable outcome**: "Unplanned spending" cannot be separated from total spending without pre-trip baskets | Perturbation | **Fatal to causal claims** | Report total spending as primary outcome; present "unplanned" proxies as sensitivity analysis with explicit disclaimers; do not claim the proxy measures unplanned spending |
| **Reverse causality**: Shoppers walk past categories *because* they plan to buy from them, not the reverse | Endogenous route choice | **Fatal to causal claims** | Acknowledge; report prompt-purchase associations descriptively; do not interpret as prompt effects |
| **Prompt salience confound**: Prompts may affect purchases directly (reminder/salience), not through route extension | Multiple channels from prompt to purchase | **Fatal to IV strategy** | Do not present IV results; report prompt-purchase associations without channel attribution |
| **Visit-order endogeneity**: Category visit order reflects planned shopping sequence, not exogenous variation | Shopper routing behavior | **Fatal to within-trip design** | Do not present within-trip sequential analysis as causal; if presented descriptively, acknowledge planned-ordering confound |
| **Measurement error in route length**: Imperfect route tracking attenuates associations | Tracking technology limitations | **Moderate** | Use binned/coarsened route measures; report that attenuation biases associations toward zero |
| **Prompt exposure misclassification**: "Available" prompts ≠ "seen" prompts | Passive measurement | **Moderate to high** | Report results as associations with prompt *availability*, not prompt *viewing* |
| **Sample selection**: Trips without usable route measures or linked checkout may differ systematically | Data infrastructure | **Moderate** | Compare demographics and spending for linked vs. unlinked trips; report any systematic differences |
| **Unplanned-proxy misclassification**: Proxy may systematically misclassify planned purchases | No ground truth | **High (for proxy-based claims)** | Vary proxy threshold; report range of results; do not draw substantive conclusions from proxy-based analyses |
| **External validity**: Descriptive associations may not generalize beyond observed stores, times, and shoppers | Cross-sectional, single-retailer data | **High (for generalization)** | Do not generalize beyond the estimation sample; frame results as specific to the observed context |

---

## 20. Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
| Route length and total checkout spending are positively correlated in the raw data | Observed route length and checkout spending from linked trip-level records | Descriptive | High (directly observable) | A near-zero or negative raw correlation in the data |
| The positive route-spending correlation persists after controlling for observable demographics, store familiarity, time-of-day, and day-of-week | Covariate-adjusted regression of spending on route length with available controls | Descriptive | Moderate (depends on covariate availability and quality) | Coefficient near zero or negative after adjustment; large changes in coefficient magnitude under alternate covariate sets |
| Category-level prompt-pass indicators are positively associated with purchase incidence for some categories | Category-trip-level regressions of purchase on prompt-pass indicators | Descriptive | Moderate (depends on prompt-exposure coding accuracy) | Null or negative associations across all categories; associations that disappear when controlling for category-specific shopper purchase frequency |
| The route-spending association varies across shopper demographic segments | Stratified regressions by demographic group | Descriptive | Low to moderate (segment-level confounding may differ; small segment sizes reduce precision) | Homogeneous associations across segments; associations that are unstable across alternate segmentation schemes |
| The route-spending association varies by time-of-day and day-of-week | Stratified regressions by time window | Descriptive | Low to moderate (time windows are weak proxies for trip mission) | Homogeneous associations across time windows |
| Constructed "unplanned spending" proxies produce different route-spending associations than total spending | Sensitivity analysis varying proxy construction threshold | Descriptive | Low (proxy is unvalidated; differences may reflect measurement artifacts rather than true unplanned/planned distinctions) | No sensitivity to proxy threshold (suggests proxy captures random noise); extreme sensitivity (suggests proxy is arbitrary) |
| No credible causal effect of route length on unplanned spending can be estimated from this packet's data | Logical assessment of identification requirements against available data; Stage 4 critic verdicts | Methodological | High (identification conditions are well-established; perturbation removes the key variable) | The emergence of a valid instrument, exogenous variation source, or pre-trip mission data within the packet's data constraints — but the packet explicitly states these are absent |
| The descriptive design is the strongest defensible analysis given packet constraints | Comparison of all candidate designs against packet data availability; Stage 4 independent critique | Methodological | High | A previously unidentified source of identifying variation in the packet's data that does not depend on pre-trip baskets — but the Stage 4 critic examined all three causal candidates and found each not defensible |

---

*End of Stage 5 Final Design Memo. This memo accepts all four Stage 4 verdicts, presents the descriptive-correlation-decomposition as the primary defensible analysis, and documents that no causal claim about route-length effects on unplanned spending is supportable with the data provided in this perturbed packet.*