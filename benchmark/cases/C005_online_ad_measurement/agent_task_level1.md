<!-- visibility: agent-facing -->
<!-- case_id: C005 -->
<!-- variant: level1 -->

# Anonymous Research Design Task: Level 1

## Task Rule

You must not search the web, infer the original paper, or use external literature. Use only the information provided below. Your goal is to design a rigorous empirical strategy, not to write a literature review.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A firm wants to measure whether a digital advertising campaign causes users to visit, sign up, or purchase. The central difficulty is that actual ad exposure is not simply random. Online platforms often decide which users receive impressions through auctions, targeting rules, and optimization systems. As a result, users who see ads may already differ from users who do not see ads, especially in baseline purchase intent.

This creates a business measurement problem. A naive exposed-versus-unexposed comparison can overstate or understate the true effect of advertising. A useful design must define the relevant counterfactual for users who receive the campaign while accounting for platform delivery and selection.

## Research Objective

Design a study to estimate the causal effect of actual digital ad exposure on downstream user outcomes in a setting where platform delivery may be optimized and selected.

## Operational Context

An advertiser can run a campaign on an online platform and observe ad delivery logs and downstream user outcomes such as visits, registrations, or purchases. Some campaign-level randomization may be possible, but the task packet does not provide a complete platform protocol, auction logs, user-level covariates, sample size, campaign dates, or brand identity.

The proposed design should explain how it handles the gap between assignment to a campaign condition and actual ad exposure. If a proposed comparison is only an intent-to-treat estimate or only a descriptive association, label it accordingly.

## Known Constraints

- The design should be feasible in the described institutional setting.
- The answer must distinguish causal claims from descriptive claims.
- The answer should state what cannot be learned from the available information.
- Do not assume that observed exposure is as-if random.
- Do not rely on external facts about any named platform, advertiser, campaign, or previous study.

## Required Output

1. Research question
2. Estimand
3. Treatment or exposure
4. Outcome
5. Main identification challenge
6. Proposed empirical design
7. Why the design is valid
8. Required assumptions
9. Statistical model
10. Robustness or placebo checks
11. Heterogeneity analysis
12. Failure modes
13. What cannot be claimed
14. Additional data needed
15. Claim-evidence table

## Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
