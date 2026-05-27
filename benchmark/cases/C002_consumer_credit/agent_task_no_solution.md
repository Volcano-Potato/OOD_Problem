<!-- visibility: agent-facing -->
<!-- case_id: C002 -->
<!-- variant: no_solution -->

# Anonymous Research Design Task: No-Solution Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A consumer lender wants to understand whether higher borrowing costs cause worse repayment, or whether borrowers offered or accepting higher-cost loans are simply riskier to begin with.

This is commercially important because pricing, screening, and collections policies depend on whether observed default differences reflect causal incentives or borrower composition.

## Research Setting

The lender holds a large historical portfolio of consumer loan offers, accepted loans, realized prices, and repayment outcomes. Loan pricing is set by the lender's internal underwriting and risk segmentation system, and final terms can differ across borrowers because of negotiated or operational adjustments.

## Research Objective

Assess whether higher loan prices are associated with lower repayment and whether observed repayment patterns are more consistent with selection, incentives, or both.

## Specific Questions To Answer

1. Are higher-priced loans associated with lower take-up or worse repayment?
2. Can the available historical data separate selection into borrowing from post-borrowing incentive effects?
3. What can be learned descriptively from rich borrower covariates and realized pricing records?
4. What additional design change would be needed to identify adverse selection or moral hazard causally?

## Data Structure Overview

- Stage 1: The lender records borrower characteristics and assigns price offers using its risk model.
- Stage 2: Borrowers choose whether to apply for or accept the offer.
- Stage 3: Accepted borrowers receive finalized loan terms and enter repayment.
- Stage 4: The lender tracks delinquency, default, and future borrowing outcomes in its administrative records.

## Available Data

| field | description |
|---|---|
| unit of observation | Borrower offer, accepted loan, and repayment record. |
| time span | Historical administrative panel over multiple lending waves. |
| sample construction | Borrowers who received offers from the lender, with accepted loans followed through repayment. |
| treatment or exposure variable | Initial offer price, finalized contract price, loan amount, and any future borrower status outcomes. |
| outcome variable | Take-up, delinquency, default, and repayment outcomes. |
| secondary outcomes | Accepted loan amount, time to delinquency, and future borrowing if observed. |
| covariates | Risk scores, prior borrowing, income proxies, demographics, branch, wave, and lender-side underwriting information. |
| panel or repeated structure | Borrowers may appear in multiple lending waves, but pricing is generated endogenously by underwriting rather than randomization. |
| assignment or variation source | Loan pricing is determined by internal risk models, staff discretion, and portfolio rules rather than experimental assignment. |
| assignment level | Borrower-offer and borrower-loan level. |
| outcome measurement level | Borrower-loan repayment record. |
| missingness or attrition | Some repayment histories or later borrower outcomes may be incomplete or censored. |
| possible spillover or interference | Borrowers may learn from each other, but the main problem is endogenous pricing rather than interference. |

## Variable Groups

### Treatment Or Exposure Variables

- Offer price.
- Finalized contract price.
- Loan amount and maturity if observed.

### Selection Or Sample-Flow Variables

- Offer receipt.
- Application or take-up.
- Loan origination.

### Main Outcome Variables

- Delinquency.
- Default.
- Repayment completion.

### Secondary Outcome Variables

- Time to delinquency.
- Future borrowing.

### Baseline Controls And Design Variables

- Underwriting risk measures.
- Demographics and income proxies.
- Branch, wave, and staff indicators.

## Identification Limitations

- No randomized assignment or quasi-random variation is provided.
- No credible instrument, threshold, boundary, or externally imposed timing shock is provided.
- Higher-priced borrowers may differ in unobserved risk, liquidity, or demand from lower-priced borrowers even after rich controls.
- Observed price and repayment patterns cannot cleanly separate adverse selection from moral hazard.

## Known Constraints

- The task should still look empirically tempting: many covariates, clear outcomes, and real business relevance.
- The answer must explicitly distinguish what is causally identifiable from what is only descriptive or correlational.
- If causal identification is not credible, the answer must say so plainly rather than inventing a design.

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
