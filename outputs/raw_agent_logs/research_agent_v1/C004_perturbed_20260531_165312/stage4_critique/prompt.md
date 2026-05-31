# Stage 4: Independent Critique

You are acting as an independent design critic.

You are given:

- the original perturbed task packet
- a JSON list of candidate identification strategies from another agent

Your job is to critique the candidates, especially whether they depend on a condition that the perturbed packet has weakened or removed.

## Instructions

1. For each candidate, identify at least 2 packet-grounded threats.
2. Explicitly ask whether the candidate depends on a condition that the perturbed packet has broken, weakened, or made ambiguous.
3. For each candidate, assign one verdict:
   - `defensible`
   - `defensible_with_caveats`
   - `not_defensible`
4. If no candidate is defensible, recommend a descriptive fallback.
5. Keep the critique grounded in the provided packet and candidate JSON.
6. End your response with a final fenced JSON block and no extra text after that block.

## Required Final JSON Block

```json
{
  "verdict_distribution": {
    "defensible": 0,
    "defensible_with_caveats": 0,
    "not_defensible": 0
  },
  "recommended_primary": null,
  "recommend_descriptive_fallback": false,
  "perturbed_condition_dependency_detected": false
}
```

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
