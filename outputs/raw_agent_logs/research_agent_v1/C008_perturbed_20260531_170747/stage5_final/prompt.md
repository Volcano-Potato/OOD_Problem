# Stage 5: Final Design Memo

You are writing the final memo after reviewing:

- the original perturbed task packet
- the Stage 3 candidate list
- the Stage 4 independent critique

Your output must follow the existing evidence-aware benchmark report structure.

## Required Reconciliation Rule

You must reconcile the Stage 4 critic verdict.

- If the critic marks a candidate `not_defensible`, do not present it as a credibly identified causal design unless you explicitly point to packet-local evidence that the critic missed.
- If the critic recommends a descriptive fallback, you must either adopt that downgrade or explain, with packet-local evidence, why a stronger design is still defensible.
- In section 17, explicitly state what cannot be claimed in light of the critique.

## Required Output Contract

Follow this structure exactly:

1. Executive summary
2. Research question
3. Target estimand or strongest defensible estimand
4. Treatment or exposure and main outcomes
5. Data structure summary
6. Relevant causal mechanisms
7. Main identification challenge
8. Whether credible causal identification is possible
9. Proposed empirical design or strongest defensible descriptive analysis
10. Why the design is valid or why causal identification is not credible
11. Required assumptions
12. Statistical model or analysis equation
13. Robustness, placebo, falsification checks, or diagnostic tests
14. Heterogeneity analysis if supportable
15. Measurement, compliance, missingness, spillover, or implementation limits
16. Failure modes and alternative explanations
17. What cannot be claimed
18. Additional data needed
19. Threat-response table if explicitly requested by the task packet
20. Claim-evidence table

Use the canonical claim-evidence table header:

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|

## Original Packet

<!-- visibility: agent-facing -->
<!-- case_id: C008 -->
<!-- variant: perturbed -->

# Anonymous Research Design Task: Perturbed Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

Consumers sometimes face add-on charges that are paid at checkout but are not fully visible when they choose products. If shoppers focus mainly on the posted shelf price, making the full cost more visible at the point of decision may change demand even when the underlying economic price is unchanged.

The research problem is to estimate a salience effect rather than a generic correlation between an in-store intervention and changing sales.

## Research Setting

A retailer can change how price information is displayed for some products or categories while observing sales over time. Transaction or scanner data are available, and untreated products may provide comparison groups inside the same store.

## Research Objective

Design a study to estimate the causal effect of making an add-on charge visible at the point of product choice on consumer demand.

## Specific Questions To Answer

1. How should the researcher estimate the effect of visible all-in pricing on product demand?
2. What comparison groups remain available if no untreated comparison stores are observed?
3. How should the design distinguish salience effects from actual price or promotion changes?
4. Which claims can still be made credibly, and which become weaker without untreated markets?

## Data Structure Overview

- Stage 1: The retailer records pre-intervention transaction outcomes for treated and untreated products or categories in the focal store.
- Stage 2: Selected products or categories in that store receive a display change that makes the add-on charge visible at the point of decision.
- Stage 3: The researcher observes transaction outcomes during the intervention window for treated and untreated products in the same store.
- Stage 4: The data no longer include untreated comparison stores from the same operating environment.

## Data Card

| field | description |
|---|---|
| unit of observation | Product or product-category by store by time-period sales record. |
| time span | Pre-intervention and intervention periods over multiple weeks. |
| sample construction | Include treated products or categories and comparable untreated products or categories within the focal store, using consistent transaction data over time. |
| treatment or exposure variable | Whether the product's displayed price information makes the add-on charge visible at the point of choice during a given store-time period. |
| outcome variable | Quantity sold, revenue, transactions, or category demand from scanner or transaction records. |
| secondary outcomes | Category substitution, product-level demand shifts, and any auxiliary execution indicators if observed. |
| assignment or variation source | Retailer-controlled display intervention applied to selected products or categories in the focal store. |
| assignment level | Product category or product group within store-time period. |
| outcome measurement level | Product or category by store by time-period transaction record. |
| panel or repeated structure | Repeated product or category observations over time in the focal store. |
| compliance or take-up | Store execution may be imperfect if tags are misplaced, missing, or implemented late. |
| spillover or interference | Shoppers may substitute between treated and untreated products; display changes may draw attention to nearby products or categories. |

## Variable Groups

### Treatment Or Exposure Variables

- Indicator for visible all-in price display.
- Treatment timing and treated-category indicators.

### Selection Or Sample-Flow Variables

- Whether a product-category-time cell is included in the analysis window.
- Whether the display intervention is actually implemented in that cell.

### Main Outcome Variables

- Quantity sold.
- Revenue or transaction counts.

### Secondary Outcome Variables

- Nearby-category substitution.
- Product-level demand composition.

### Baseline Controls And Design Variables

- Product, category, and time indicators.
- Actual paid price, discounts, and promotions.
- Pre-period sales levels or trends if available.

## Perturbed Condition

The data no longer include untreated comparison stores. The researcher observes treated and untreated product groups over time only within the focal store.

## Known Constraints

- The business setting and most of the data structure are intentionally similar to the base task.
- One key identification condition has changed.
- The answer must explain whether the original design logic still works, becomes weaker, or fails.
- If strong causal identification is no longer justified, the answer must explicitly downgrade the claim or propose additional design changes.

## Required Output

1. Executive summary
2. Research question
3. Target estimand or strongest defensible estimand
4. Treatment or exposure and main outcomes
5. Data structure summary
6. Relevant causal mechanisms
7. Main identification challenge
8. Whether credible causal identification is possible
9. Proposed empirical design or strongest defensible descriptive analysis
10. Why the design is valid or why causal identification is not credible
11. Required assumptions
12. Statistical model or analysis equation
13. Robustness, placebo, falsification checks, or diagnostic tests
14. Heterogeneity analysis if supportable
15. Measurement, compliance, missingness, spillover, or implementation limits
16. Failure modes and alternative explanations
17. What cannot be claimed
18. Additional data needed
19. Threat-response table if explicitly requested by the task packet
20. Claim-evidence table

## Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|


## Stage 3 Candidate JSON

```json
{
  "candidates": [
    {
      "name": "Within-Store Difference-in-Differences",
      "estimand": "Average treatment effect on the treated (ATT) of visible all-in pricing on quantity sold, using untreated product categories within the focal store as the comparison group.",
      "identifying_variation": "Pre-post change in demand for treated product categories relative to the pre-post change for untreated product categories, both observed within the same store over the same time window.",
      "critical_assumption": "Parallel trends: in the absence of the display intervention, treated and untreated product categories would have followed the same demand trajectory. Also requires no within-store SUTRA violations from substitution or attention spillover.",
      "packet_support": "Packet states untreated products 'may provide comparison groups inside the same store'; repeated product/category observations over time in the focal store are available; pre-intervention sales levels and trends are recorded.",
      "fragility": "Within-store spillover is explicitly noted in the data card ('Shoppers may substitute between treated and untreated products; display changes may draw attention to nearby products or categories'), which violates SUTVA and biases the untreated-group counterfactual. Treated and untreated categories may be fundamentally different product types with divergent seasonal or promotional dynamics, making parallel trends implausible. No untreated stores exist to validate the parallel-trends assumption or to benchmark the untreated-product trend.",
      "is_fallback": false
    },
    {
      "name": "Staggered Event Study",
      "estimand": "Dynamic average treatment effect on the treated by event time, capturing how the salience effect evolves after the display change is introduced to each product category.",
      "identifying_variation": "Within-category variation in treatment timing across product categories, exploiting that not all categories receive the display change simultaneously. Newly treated categories are compared to not-yet-treated categories at the same calendar time.",
      "critical_assumption": "Treatment timing is conditionally independent of demand shocks — i.e., the sequence in which categories receive the display change is as-good-as-random after conditioning on category and time fixed effects. No anticipation effects before implementation.",
      "packet_support": "Treatment timing and treated-category indicators are listed among treatment variables, suggesting possible staggered or phased rollout. Panel structure with repeated observations over time supports event-study estimation. Pre-period data allow testing for pre-trends and anticipation.",
      "fragility": "If all treated categories receive the intervention simultaneously, this design collapses to a simple pre-post comparison. Even if staggered, the rollout order may be endogenous (e.g., high-margin or high-volume categories treated first), which biases the not-yet-treated counterfactual. Standard two-way fixed-effects estimators with staggered timing can produce biased estimates under treatment-effect heterogeneity; newer estimators (e.g., Callaway-Sant'Anna, Sun-Abraham) would be needed but their validity still hinges on parallel trends conditional on covariates.",
      "is_fallback": false
    },
    {
      "name": "Interrupted Time Series on Treated Products",
      "estimand": "Change in the level and/or slope of demand for treated products at the point of intervention, where the counterfactual is the extrapolated pre-intervention trend.",
      "identifying_variation": "Time-series break in the outcome series for treated products at the known intervention date, compared to a counterfactual trend fit on pre-period data and projected forward.",
      "critical_assumption": "No other events, shocks, or interventions coincide with the display-change timing that could independently shift demand for the treated products. The pre-period trend is a valid model of what would have occurred absent the intervention.",
      "packet_support": "Pre-intervention and intervention periods span multiple weeks, providing a time series long enough to model pre-trends. The intervention date is known. Actual prices, discounts, and promotions are observable and can be included as time-varying controls.",
      "fragility": "Without a comparison group, the design cannot distinguish the display-change effect from any other event occurring at the same time (seasonal shifts, competitor actions, supply changes, other in-store changes). The intervention is a single point in time, so there is no replication. Credible causal identification is weak; at best this identifies a structural break in the time series that is consistent with a salience effect but cannot rule out confounds. This is a quasi-experimental design with low internal validity.",
      "is_fallback": false
    },
    {
      "name": "Descriptive Pre-Post with Price Controls",
      "estimand": "Conditional association between the visible all-in price display and product demand, net of observed price changes, discounts, and promotions.",
      "identifying_variation": "Before-after comparison of demand outcomes for treated products only, controlling for the actual paid price, promotional intensity, and discount depth observed in each period.",
      "critical_assumption": "All determinants of demand that change around the intervention timing are captured by the observed price, promotion, and discount controls. No unobserved confounders are correlated with both the display change and demand.",
      "packet_support": "Packet provides actual paid price, discounts, and promotions as baseline controls. Pre-intervention outcomes are available for descriptive comparison. The packet explicitly instructs: 'If credible causal identification is no longer justified, the answer must explicitly downgrade the claim or propose additional design changes.'",
      "fragility": "This design cannot support a causal claim. The display change may be coincident with other unobserved changes (e.g., supplier negotiations, inventory adjustments, manager reassignments, local demand shocks). Even with price controls, the display change is perfectly collinear with time, so the salience effect cannot be separated from any other time-varying confound. At best, the analysis can describe whether demand changed after the intervention and whether that change persists after controlling for observed price movements, but cannot attribute the change to salience versus other mechanisms.",
      "is_fallback": true
    }
  ],
  "recommended_primary": "Within-Store Difference-in-Differences",
  "notes": "The Within-Store DiD is the strongest candidate because it uses the only available comparison group (untreated products in the same store) and exploits both cross-sectional and temporal variation. However, its validity is severely threatened by within-store spillover, which the packet explicitly flags. The Staggered Event Study would be preferable if rollout was phased, but the packet does not confirm staggered timing. The ITS is a weaker quasi-experimental fallback. The purely descriptive pre-post analysis is listed as the fallback because it transparently downgrades the claim to association rather than causation. Without untreated stores, no candidate can achieve the same level of internal validity as the base design."
}
```

## Stage 4 Critique

Now let me carefully analyze each candidate against the packet, focusing on the perturbed condition ("no untreated comparison stores") and the packet's explicit constraints.

---

## Independent Critique

### Candidate 1: Within-Store Difference-in-Differences

**Packet-grounded threats:**

1. **Explicit within-store spillover (SUTVA violation).** The data card directly warns: "Shoppers may substitute between treated and untreated products; display changes may draw attention to nearby products or categories." This means the untreated-product counterfactual is contaminated — demand for untreated products changes *because of* the treatment, not independently of it. This biases the DiD estimate in an unknown direction and magnitude. The packet does not provide any design device (e.g., physical separation, product category distance) that could credibly mitigate this.

2. **Parallel trends cannot be validated.** The perturbed condition — "the data no longer include untreated comparison stores" — removes the only external benchmark that could test whether untreated product trends are a valid counterfactual. Without untreated stores, the researcher cannot conduct a placebo-in-time test against an untreated market, cannot check whether untreated product trends in the focal store diverge from trends in untreated stores, and cannot implement a triple-difference design. The DiD relies entirely on the untestable assertion that treated and untreated product categories — which may be fundamentally different goods — share common demand dynamics.

3. **No evidence of trend commonality across categories.** The packet provides no information suggesting that treated products (e.g., those selected for the display intervention) and untreated products share similar seasonal patterns, promotional cycles, or demand elasticities. The assignment mechanism is "retailer-controlled" — meaning categories were selected deliberately, not randomly — making systematic differences in demand trajectories likely.

**Does this candidate depend on a condition the perturbed packet has broken, weakened, or made ambiguous?** Yes. The perturbation removes untreated stores. This does not directly break the within-store DiD — the candidate uses untreated *products*, not untreated *stores* — but it removes the only validation layer that could test parallel trends and assess spillover magnitude. The design becomes untestable rather than strictly broken. The perturbation *weakens* the DiD from a design that could be validated externally to one that must be taken entirely on faith.

**Verdict:** `defensible_with_caveats`

---

### Candidate 2: Staggered Event Study

**Packet-grounded threats:**

1. **Staggered timing is not confirmed in the packet.** The candidate's identifying variation — "not all categories receive the display change simultaneously" — is an assumption the candidate makes, not a fact the packet provides. The packet lists "treatment timing and treated-category indicators" among treatment variables, but this is consistent with a *single* timing where all treated categories switch on the same date. The packet's description of assignment — "Retailer-controlled display intervention applied to selected products or categories in the focal store" — contains no language suggesting phasing, rollout waves, or sequential adoption. If treatment is simultaneous, this design collapses to a simple pre-post with no valid comparison group at treatment time.

2. **Endogenous rollout order.** Even if timing were staggered, the packet gives no reason to believe the sequence is exogenous. The retailer controls the intervention. High-revenue, high-margin, or strategically important categories would plausibly be treated first — exactly the categories whose demand trajectories differ from later-treated categories. The candidate's "conditional independence" assumption has zero packet support.

3. **The perturbation magnifies the identification problem.** Without untreated stores, the staggered design must rely entirely on not-yet-treated categories as controls. But if rollout is strategic (categories selected for treatment timing based on expected demand), then not-yet-treated categories are a selected — not random — comparison group. The perturbation removes the possibility of benchmarking the not-yet-treated trend against true untreated stores.

**Does this candidate depend on a condition the perturbed packet has broken, weakened, or made ambiguous?** Yes, in two ways. First, it depends on staggered timing — a condition the packet does not provide, and the perturbation does not change this absence. Second, even under staggered timing, the perturbation removes the untreated-store benchmark that could validate the not-yet-treated counterfactual. The design is doubly fragile: it assumes a packet-absent feature (staggering) and operates in a setting where that feature's validity cannot be checked.

**Verdict:** `not_defensible`

---

### Candidate 3: Interrupted Time Series on Treated Products

**Packet-grounded threats:**

1. **No comparison group of any kind.** The perturbation removes untreated stores, and this design does not even use untreated products within the store. The counterfactual is purely a statistical extrapolation of the pre-period trend. The packet explicitly notes that "the intervention is a single point in time, so there is no replication" — meaning there is exactly one treated unit observed over one treatment episode. Any event coinciding with the intervention date (seasonal change, competitor entry, supplier contract renegotiation, other in-store merchandising changes) will be absorbed into the treatment effect estimate. The packet provides no information ruling out such confounds.

2. **The perturbation makes ITS the default, not a choice.** Because the packet removes untreated stores, the researcher is forced toward designs with no comparison group. But "forced to use ITS" is not the same as "ITS is credible." The design's low internal validity is inherent to single-group time-series designs, and the perturbation does not create any compensating feature (e.g., multiple treated units, staggered timing, a long pre-period with stable trends) that would elevate ITS above a quasi-experimental case study.

3. **The packet's own instruction applies.** "If credible causal identification is no longer justified, the answer must explicitly downgrade the claim." ITS cannot credibly distinguish the salience effect from any contemporaneous change. The candidate's own fragility section acknowledges "at best this identifies a structural break consistent with a salience effect but cannot rule out confounds" and rates it as "low internal validity." This is an admission that the design does not meet the bar for credible causal identification.

**Does this candidate depend on a condition the perturbed packet has broken, weakened, or made ambiguous?** Yes. The perturbation removes untreated stores, eliminating any comparison-based identification. ITS attempts to work around this by using only the treated unit's own pre-trend, but this is a fundamental downgrade in identification strategy — not a successful adaptation. The perturbation *breaks* comparison-based identification, and ITS is the residual design that remains, not a design that overcomes the perturbation.

**Verdict:** `not_defensible`

---

### Candidate 4: Descriptive Pre-Post with Price Controls

**Packet-grounded threats:**

1. **No causal identification possible.** The display change is perfectly collinear with time. Observed price controls cannot disentangle salience from any unobserved time-varying confound because the treatment indicator itself has no residual variation after conditioning on time. The design estimates a conditional association, not a causal effect. The candidate transparently acknowledges this.

2. **Selection on unobservables is unaddressed.** The retailer chose which categories to treat and when to treat them. The choice may reflect expected demand conditions, margin optimization, supplier relationships, or inventory management — all unobserved in the data. Controlling for prices and promotions does not address selection into treatment.

3. **This is the design the packet instructs when causal identification fails.** The packet explicitly states: "If credible causal identification is no longer justified, the answer must explicitly downgrade the claim or propose additional design changes" and "do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead." Candidate 4 follows this instruction exactly: it downgrades the claim, avoids inventing identification, and proposes the strongest descriptive analysis the available data support.

**Does this candidate depend on a condition the perturbed packet has broken?** No — quite the opposite. This candidate *responds to* the perturbation by abandoning causal claims that the perturbation makes indefensible. It does not depend on untreated stores, parallel trends, staggered timing, or any condition the perturbation removed. It works entirely within the remaining data structure.

**Verdict:** `defensible`

---

## Summary Assessment

The perturbation — removing untreated comparison stores — is not a minor inconvenience. It eliminates the core identification strategy that would underpin any credible causal design (cross-store or cross-market comparisons). Among the four candidates:

- **Candidate 1** (Within-Store DiD) tries to salvage comparison-based identification using untreated products. It is weakened by untestable parallel trends and explicit spillover, but not entirely broken. It remains the best *causal* candidate available, with heavy caveats.
- **Candidate 2** (Staggered Event Study) assumes a packet-absent condition (staggered rollout) and is therefore not defensible.
- **Candidate 3** (ITS) abandons comparison groups entirely and cannot support causal claims.
- **Candidate 4** (Descriptive Pre-Post) is the only candidate that fully respects the perturbation's implications and follows the packet's explicit instruction to downgrade.

The recommended primary is Candidate 4 because it is the only design that is fully defensible under the perturbed packet's constraints. If the task insists on a causal design, Candidate 1 is the least-bad option but requires caveats that substantially weaken confidence.

