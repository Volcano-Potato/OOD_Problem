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
<!-- case_id: C004 -->
<!-- variant: perturbed -->

# Anonymous Research Design Task: Perturbed Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A consumer-facing firm wants to know whether paid placements in query-driven digital traffic generate incremental purchases or mainly intercept users who would have reached the firm anyway. Managers still care about whether effects differ across less active and already active users.

## Research Setting

The firm records repeated downstream sales outcomes across multiple market areas during a campaign. Campaign managers can choose to reduce or suspend paid-search availability in some markets while keeping it active elsewhere. Users differ in prior familiarity and can still reach the firm through unpaid or direct channels.

## Research Objective

Assess whether changes in paid-search availability affect downstream purchases and whether any measured effect can be interpreted causally.

## Specific Questions To Answer

1. Can the researcher still estimate a credible causal effect of paid-search availability on downstream sales?
2. How should the researcher separate genuine ad effects from underlying market demand differences?
3. What happens to the interpretation of user-segment heterogeneity if treatment assignment is no longer clearly exogenous?
4. Which claims, if any, remain defensible under the available variation?

## Data Structure Overview

- Stage 1: The researcher observes historical sales patterns and baseline market characteristics for multiple market areas.
- Stage 2: During the campaign, some markets have paid-search availability reduced or suspended while others remain active.
- Stage 3: The researcher records downstream sales or purchase outcomes over time for all markets.
- Stage 4: Outcomes can also be summarized for user-history segments defined by prior familiarity, recency, or frequency of activity.

## Data Card

| field | description |
|---|---|
| unit of observation | Market-by-time sales observation, optionally split by prior user-history segment. |
| time span | Pre-period and intervention-period repeated observations. |
| sample construction | Markets are observed continuously for downstream sales, and campaign managers can change paid-search availability during the intervention period. |
| treatment or exposure variable | Indicator for paid-search availability in a market during the intervention window. |
| outcome variable | Downstream purchases, orders, sales, or revenue. |
| secondary outcomes | Segment-specific purchases or related downstream sales summaries if observed. |
| assignment or variation source | Campaign managers choose where to reduce or suspend paid-search availability based on operational or demand considerations rather than using a pre-committed experimental rule. |
| assignment level | Market or market-time cell. |
| outcome measurement level | Market-by-time or market-by-time-by-segment sales outcome. |
| panel or repeated structure | Yes; repeated market-by-time observations before and during the campaign. |
| compliance or take-up | Market-level ad availability does not map one-to-one into individual exposure, clicks, or purchases. |
| spillover or interference | Users may substitute across unpaid search, direct navigation, neighboring markets, or other acquisition channels. |

## Variable Groups

### Treatment Or Exposure Variables

- Market-level paid-search availability during the intervention window.
- Intensity or duration of paid-search availability if observed.

### Selection Or Sample-Flow Variables

- Market membership of demand observations.
- User-history segment assignment based on pre-period familiarity or activity.

### Main Outcome Variables

- Downstream purchases or sales.
- Revenue or order counts.

### Secondary Outcome Variables

- Segment-specific sales outcomes.
- New-to-firm or less-active-user purchase outcomes if available.

### Baseline Controls And Design Variables

- Historical market-level sales.
- Market fixed characteristics, seasonality controls, and time indicators.
- Prior familiarity, recency, or frequency segment summaries.

## Perturbed Condition

Paid-search availability is no longer varied according to a clearly exogenous or pre-committed experimental rule. Instead, campaign managers choose which markets to reduce or suspend based on operational judgments, expected demand, or budget considerations.

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
      "name": "Staggered Difference-in-Differences",
      "estimand": "Average treatment effect on the treated (ATT) of paid-search suspension on downstream sales, estimated from staggered timing of suspension across markets.",
      "identifying_variation": "Differential timing of paid-search availability reduction or suspension across markets, exploiting the panel structure with pre-period and intervention-period repeated observations.",
      "critical_assumption": "Parallel trends: markets that suspend paid-search would have followed sales trajectories parallel to markets that do not, absent the suspension. This requires that manager decisions to suspend are not driven by market-specific time-varying demand shocks.",
      "packet_support": "Repeated market-by-time observations before and during the campaign; pre-period historical sales patterns; market fixed characteristics; seasonality controls and time indicators; staggered suspension by campaign managers across market areas.",
      "fragility": "Campaign managers select markets based on operational judgments, expected demand, or budget considerations. If expected demand drives both suspension decisions and future sales, parallel trends is violated and the ATT is biased. Pre-trend tests can detect some violations but not those arising from forward-looking selection on anticipated shocks contemporaneous with treatment.",
      "is_fallback": false
    },
    {
      "name": "Synthetic Control Method",
      "estimand": "Market-specific treatment effect of paid-search suspension on sales, aggregated across treated markets, estimated by comparing each treated market to a weighted synthetic counterfactual constructed from untreated markets.",
      "identifying_variation": "Pre-period sales trajectories and baseline market characteristics used to construct a convex combination of untreated donor markets that reproduces the treated market's pre-intervention path.",
      "critical_assumption": "The synthetic control reproduces the counterfactual post-suspension sales path the treated market would have followed had paid-search remained active. This requires that the pre-period fit captures all relevant determinants of the counterfactual, including any unobserved factors driving the manager's suspension decision.",
      "packet_support": "Multiple market areas with repeated observations before and during the campaign; historical sales patterns; baseline market characteristics available as matching covariates; multiple untreated markets available as donor pool.",
      "fragility": "If managers suspend paid-search in markets experiencing idiosyncratic demand declines or anticipating future weakness, the synthetic control constructed from markets not facing those same pressures will overstate the treatment effect. Sparse donor pools or limited pre-period observations weaken the fit. No formal inference without multiple treated units or permutation methods.",
      "is_fallback": false
    },
    {
      "name": "Selection-on-Observables with Pre-Trend Adjustment",
      "estimand": "Conditional average treatment effect of paid-search availability on sales, estimated from residual variation after controlling for observed market characteristics, historical sales, and pre-period trends.",
      "identifying_variation": "Cross-market and within-market variation in paid-search availability that remains after conditioning on historical market-level sales, market fixed characteristics, seasonality controls, and time indicators.",
      "critical_assumption": "Unconfoundedness (selection on observables): after conditioning on historical sales, market fixed characteristics, seasonality, and pre-period trends, the suspension decision is independent of potential outcomes. No unobserved time-varying confounders jointly determine suspension and sales.",
      "packet_support": "Historical market-level sales; market fixed characteristics; seasonality controls; time indicators; panel structure enabling within-market differencing; segment-level covariates on prior familiarity, recency, and frequency.",
      "fragility": "Managers use private forward-looking demand expectations and operational judgments when deciding where to suspend. These expectations are not in the observed covariate set. Conditioning on observables cannot recover causal effects if unobserved expected demand shocks drive both the suspension decision and subsequent sales.",
      "is_fallback": false
    },
    {
      "name": "Descriptive Correlational Benchmarking",
      "estimand": "Conditional and unconditional associations between paid-search availability and downstream sales, described across markets, time periods, and user-history segments without causal interpretation.",
      "identifying_variation": "All observed cross-market and within-market variation in paid-search availability and sales outcomes during the campaign window, including pre-post comparisons within suspended markets and cross-sectional contrasts between suspended and active markets.",
      "critical_assumption": "No causal identifying assumptions are required. The analysis reports what the data show rather than what causes what.",
      "packet_support": "All data structures described in the packet: market-by-time sales, treatment indicators, user-history segments, baseline controls, and pre-period observations. Can produce rich descriptive summaries including raw difference-in-means, pre-post changes, and segment-level patterns.",
      "fragility": "Cannot support any causal claim about whether paid-search drives incremental purchases versus intercepting existing demand. All observed associations confound treatment effects with selection, demand heterogeneity, and substitution patterns. Descriptive patterns may be misleading if interpreted causally by readers.",
      "is_fallback": true
    }
  ],
  "recommended_primary": "Staggered Difference-in-Differences",
  "notes": "All quasi-experimental candidates share a common fragility: campaign managers choose suspension markets based on expected demand and operational judgments, creating selection on unobservables that plausibly violates parallel trends, synthetic control fit, and unconfoundedness. The staggered DiD is recommended as the primary candidate because it uses the richest identifying structure available in the packet (panel with pre-trend diagnostics, event-study specification, and fixed effects), but its causal credibility hinges on whether the researcher can defend—through institutional knowledge, pre-trend tests, and falsification exercises—that the manager's decision rule is orthogonal to market-specific time-varying demand shocks. No candidate achieves strong causal identification under the perturbed condition without additional design elements not present in the packet."
}
```

## Stage 4 Critique

## Independent Critique: Stage 3 Candidates vs. Perturbed Packet C004

### Perturbation Recap

The packet's perturbed condition explicitly replaces exogenous or pre-committed assignment with manager discretion: *"campaign managers choose which markets to reduce or suspend based on operational judgments, expected demand, or budget considerations."* This is not a minor weakening — it introduces forward-looking, private-information selection directly into the treatment assignment mechanism. Every causal candidate must survive scrutiny under this condition.

---

### Candidate 1: Staggered Difference-in-Differences

**Threat 1 — Forward-looking selection on anticipated demand shocks.** The packet states managers choose suspension markets based on "expected demand." If a manager anticipates a market-specific downturn and suspends paid-search there, the post-suspension sales decline reflects both the treatment effect AND the anticipated demand shock. Parallel trends is violated because treatment timing is correlated with future potential outcomes. Pre-trend tests only detect pre-existing divergence; they are silent on shocks contemporaneous with treatment that the manager foresaw but the econometrician did not.

**Threat 2 — Endogenous treatment timing with heterogeneous effects.** The packet provides no commitment device, no phased roll-out rule, and no quasi-random variation in timing. Under recent staggered-DiD decompositions (Goodman-Bacon 2021; Sun & Abraham 2021; Callaway & Sant'Anna 2021), when treatment adoption timing correlates with unit-specific trend differentials and effects are heterogeneous across cohorts or over time, the two-way fixed-effects estimator recovers a contaminated weighted average that can have the wrong sign. The packet's institutional details — manager discretion tied to demand and budget — are precisely the conditions that produce such contamination.

**Does this candidate depend on a condition the perturbed packet has broken?** Yes, directly. The original unperturbed design would have relied on exogenous or pre-committed assignment, under which parallel trends might be defensible. The perturbation removes this and introduces forward-looking selection by managers using private demand information. Parallel trends is no longer credible.

**Verdict:** `not_defensible`

---

### Candidate 2: Synthetic Control Method

**Threat 1 — Idiosyncratic selection pressures cannot be synthesized from untreated donors.** If managers suspend paid-search in markets experiencing (or anticipating) unique demand weakness, no convex combination of untreated markets — which by construction did not face those same pressures — can reproduce the treated market's counterfactual sales path. The synthetic control will systematically attribute a demand-driven decline to the treatment, inflating the estimated effect. This is not a minor bias; it is a structural failure of the donor pool.

**Threat 2 — Sparse donor pool and limited pre-period under packet ambiguity.** The packet says "multiple market areas" without specifying numbers. SCM requires a sufficiently large donor pool with a sufficiently long pre-period to achieve a good pre-intervention fit. If only a handful of markets are suspended, and the remaining untreated markets are few or systematically different, the pre-period fit will be poor or the post-period counterfactual will be unreliable. The perturbation makes systematic difference likely because manager selection targets specific markets for reasons correlated with outcomes.

**Does this candidate depend on a condition the perturbed packet has broken?** Yes. SCM relies on selection being driven by factors that can be captured through pre-period outcomes and observed covariates. The perturbation introduces forward-looking demand expectations — time-varying, unobserved, and market-specific — that cannot be reconstructed from donor markets that lacked those same expectations.

**Verdict:** `not_defensible`

---

### Candidate 3: Selection-on-Observables with Pre-Trend Adjustment

**Threat 1 — Explicitly named unobserved confounders in the packet.** The perturbation states that managers use "expected demand" and "operational judgments" when deciding where to suspend. Neither appears in the observed covariate set (historical sales, market fixed characteristics, seasonality controls, time indicators, segment summaries). Expected demand is forward-looking and inherently unobserved by the researcher. Operational judgments are private managerial information. The unconfoundedness assumption is violated by construction — the packet names the unobserved confounders.

**Threat 2 — Pre-trend adjustment cannot substitute for forward-looking information.** Including pre-period sales trends as controls can absorb divergent historical trajectories but cannot capture information the manager possesses about future market conditions that has not yet materialized in any observed variable. If a manager suspends paid-search in a market because they anticipate a local competitor entering next quarter, that rationale is not in pre-trends, not in historical sales, and not in market fixed characteristics. It is private, forward-looking, and jointly determines both treatment and future outcomes.

**Does this candidate depend on a condition the perturbed packet has broken?** Yes. Selection-on-observables requires that all confounders are observed and conditioned on. The perturbation explicitly introduces private, forward-looking confounders (expected demand, operational judgments) that are absent from the data card. No conditioning strategy can recover identification when treatment decisions incorporate information about future outcomes that the researcher cannot access.

**Verdict:** `not_defensible`

---

### Candidate 4: Descriptive Correlational Benchmarking

**Threat 1 — Patterns confound treatment effects with selection, demand heterogeneity, and substitution.** The packet documents that users substitute across unpaid search, direct navigation, neighboring markets, and other channels. A simple pre-post comparison in suspended markets will reflect not only any causal effect of paid-search removal but also demand seasonality, substitution to other channels, and the manager's reason for suspension. Even as description, the raw associations have no clear structural interpretation without a model of the manager's selection rule and user substitution behavior.

**Threat 2 — Segment-level heterogeneity is uninterpretable under non-random assignment.** The packet asks about differences across "less active and already active users." Under non-random assignment, any observed difference in paid-search associations across segments conflates (a) genuine differential treatment effects, (b) differential manager selection of which markets to treat — correlated with market segment composition, and (c) differential substitution elasticities across segments. A descriptive analysis cannot disentangle these, and presenting segment-level contrasts may actively mislead if readers impose causal interpretations.

**Does this candidate depend on a condition the perturbed packet has broken?** No. This candidate explicitly disclaims causal identification and does not rely on exogenous assignment, parallel trends, unconfoundedness, or any quasi-experimental identifying assumption. The perturbation weakens what can be learned (the descriptive patterns become harder to interpret meaningfully), but it does not break the descriptive method itself.

**Verdict:** `defensible_with_caveats` — The descriptive approach is valid as a fallback precisely because it makes no causal claims requiring exogenous assignment. However, it requires stringent caveats: (a) all associations confound treatment effects with selection, demand heterogeneity, and substitution; (b) segment-level descriptive contrasts have no clear interpretation; (c) no finding can distinguish incremental purchases from demand interception; (d) the direction of any observed association cannot be attributed to paid-search without a model of why managers suspended it.

---

### Overall Assessment

All three quasi-experimental candidates (`Staggered Difference-in-Differences`, `Synthetic Control Method`, `Selection-on-Observables with Pre-Trend Adjustment`) depend on identifying conditions that the perturbation explicitly breaks: exogenous or unconfounded assignment. The perturbation replaces experimental or quasi-experimental variation with manager discretion driven by forward-looking demand expectations — private information that is unobserved, time-varying, and jointly determines both treatment and outcomes. No amount of pre-trend testing, covariate adjustment, or synthetic matching can recover identification when the selection mechanism itself incorporates information about future potential outcomes that the researcher cannot access.

Only the descriptive fallback survives, and only with strong caveats. A descriptive fallback is recommended.

---

