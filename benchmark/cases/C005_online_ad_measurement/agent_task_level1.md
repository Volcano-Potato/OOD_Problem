<!-- visibility: agent-facing -->
<!-- case_id: C005 -->
<!-- variant: level1 -->

# Anonymous Research Design Task: Level 1

## Task Rule

You must not search the web, infer the original paper, or use external literature. Use only the information provided below. Your goal is to design a rigorous empirical strategy, not to write a literature review.

Do not assume that a known paper has already solved the task. Treat this as an anonymous applied business/economics research problem.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A firm wants to measure whether a digital advertising campaign actually changes user behavior. The central problem is that observed ad exposure is not purely random. Online delivery systems often use auctions, targeting rules, pacing, and optimization, so the users who see an ad may differ systematically from the users who do not.

This matters because a naive exposed-versus-unexposed comparison may confuse advertising impact with pre-existing purchase intent. The research task is to design a measurement strategy that identifies a credible counterfactual for users who were realistically in a position to see the campaign.

## Research Setting

An advertiser runs a campaign on an online platform, and the researcher can observe some combination of campaign assignment, ad delivery logs, and downstream conversion outcomes such as visits, registrations, or purchases. The platform controls which users actually receive impressions, even when some higher-level experimentation is possible.

The task packet does not reveal the original advertiser, platform, campaign window, or source-specific implementation details. The design should therefore focus on the logic of exposure opportunity and downstream measurement.

## Research Objective

Design a study to estimate the causal effect of actual digital ad exposure on downstream user outcomes in a setting where platform delivery may be optimized and selected.

## Specific Questions To Answer

1. How should the researcher define the causal estimand when campaign assignment and actual ad exposure are not the same thing?
2. What comparison group would make exposed users comparable to an untreated counterfactual?
3. How should the design distinguish a campaign-level assignment effect from the effect of actual exposure?
4. Which claims about ad lift remain credible if exposure opportunity is measured imperfectly?

## Mechanism Intuition

- Endogenous exposure channel: users who receive impressions may already have higher baseline intent.
- Platform-delivery channel: auction and optimization rules determine who is actually shown the ad.
- Measurement channel: attribution windows and conversion tracking affect what is observed as an outcome.
- Interpretation risk: a clean campaign assignment effect may still answer a different question from exposed-user causal lift.

## Available Information

The researcher can observe an online campaign environment, downstream conversion outcomes, and at least some information on assignment, delivery, or exposure opportunity. Repeated user-level or opportunity-level observations may also be available.

## Information Not Provided

This task packet does not provide the original source, exact platform, exact advertiser, exact sample size, exact campaign dates, or the source paper's named method. It also does not provide the full logging implementation.

## Known Constraints

- The design should be feasible in the described institutional setting.
- The answer must distinguish descriptive associations, causal claims, and mechanism claims.
- The answer should state what cannot be learned from the available information.
- Do not assume that observed exposure is as-if random.
- Do not infer missing facts from external knowledge or from a suspected source paper.

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
