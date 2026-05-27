<!-- visibility: agent-facing -->
<!-- case_id: C002 -->
<!-- variant: perturbed -->

# Anonymous Research Design Task: Perturbed Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A consumer lender wants to understand why borrowers with different loan terms show different repayment outcomes. Repayment differences may reflect who chooses to borrow under different offer terms, or they may reflect how realized loan terms and later incentives change behavior after borrowing.

The research problem is to design a credit-market study that separates these explanations rather than estimating a single reduced-form price effect on default.

## Research Setting

The lender makes offers to prospective borrowers, observes who responds or accepts, finalizes a contract, and later tracks repayment. Some terms are visible before application or take-up, while other terms or incentives may arise only after the borrower has already entered the borrowing relationship.

## Research Objective

Design a study to estimate whether repayment outcomes in a consumer-credit setting are driven by borrower selection at take-up, incentive effects after borrowing, or both.

## Specific Questions To Answer

1. Which design can estimate how pre-borrowing terms affect take-up and borrower composition?
2. How can the study separate borrower selection from post-borrowing incentives?
3. What happens to that separation if borrowers already know how later contract terms can change before they apply?
4. Which repayment comparisons remain credible, and which become confounded?

## Data Structure Overview

- Stage 1: Eligible prospective borrowers receive loan offers with observable pre-borrowing terms.
- Stage 2: Before deciding whether to apply, borrowers are informed that final contract terms may differ from the initial offer and are shown how later terms can be determined.
- Stage 3: Accepted borrowers receive finalized contract terms and enter repayment.
- Stage 4: The lender observes repayment outcomes and may also vary or observe future-credit consequences tied to repayment behavior.

## Data Card

| field | description |
|---|---|
| unit of observation | Prospective borrower offer, application, accepted loan, and repayment record. |
| time span | Sequential credit process: offer stage, application or acceptance stage, contract finalization stage, repayment period, and possible future-borrowing period. |
| sample construction | Prospective borrowers receive loan offers. Accepted loans are followed through repayment. Non-applicants remain observable for take-up but not repayment outcomes. |
| treatment or exposure variable | Loan terms and incentives that can vary at different stages, including terms shown before application, terms finalized after acceptance, and future-access or pricing incentives tied to repayment behavior. |
| outcome variable | Application or take-up, repayment status, delinquency or default, and future borrowing eligibility or terms. |
| secondary outcomes | Intermediate repayment behavior and accepted loan amount if observed. |
| assignment or variation source | The lender still varies initial offer terms and later contract terms, but borrowers are informed before application that later terms may differ from the initial offer. |
| assignment level | Borrower-offer level for initial terms; later terms may still vary at borrower-loan level after acceptance. |
| outcome measurement level | Borrower-loan repayment record. |
| panel or repeated structure | Borrowers can have linked observations across offer, acceptance, repayment, and future-borrowing stages. |
| compliance or take-up | Not all offered borrowers apply or accept; later incentive variation may matter only within originated loans. |
| spillover or interference | Borrowers may share offer information; staff may treat borrowers differently if they observe assigned terms. |

## Variable Groups

### Treatment Or Exposure Variables

- Pre-borrowing offer terms.
- Realized contract terms.
- Future access or repayment-linked incentive terms.

### Selection Or Sample-Flow Variables

- Offer receipt.
- Application or take-up.
- Acceptance and loan origination.

### Main Outcome Variables

- Take-up.
- Repayment, delinquency, or default.

### Secondary Outcome Variables

- Loan amount if relevant.
- Intermediate repayment behavior.

### Baseline Controls And Design Variables

- Pre-offer borrower risk measures.
- Prior credit history or lender-side information.
- Offer wave, branch, or operational batch indicators.

## Perturbed Condition

Before deciding whether to apply, borrowers are informed that the eventual contract terms may differ from the initial offer and are shown how those later terms can be determined.

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
