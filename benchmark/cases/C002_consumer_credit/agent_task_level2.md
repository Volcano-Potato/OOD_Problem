<!-- visibility: agent-facing -->
<!-- case_id: C002 -->
<!-- variant: level2 -->

# Anonymous Research Design Task: Level 2

## Task Rule

You must not search the web, infer the original paper, or use external literature. Use only the information provided below. Your goal is to design a rigorous empirical strategy, not to write a literature review.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

A consumer lender wants to understand why borrowers with different loan terms show different repayment outcomes. Higher borrowing costs may attract a different pool of applicants, because only certain borrowers accept the offer. Higher borrowing costs may also change repayment behavior after a borrower takes the loan, because the contract changes the incentives and financial burden faced by the borrower.

These two explanations have different business and policy implications. A useful research design must separate borrower selection at take-up from incentive or burden effects after borrowing.

## Research Objective

Design a study to estimate whether repayment outcomes in a consumer-credit setting are driven by borrower selection at take-up, incentive effects after borrowing, or both.

## Data Card

| field | description |
|---|---|
| unit of observation | Prospective borrower offer, application, accepted loan, and repayment record. The analysis may require linked stages for the same borrower. |
| time span | Sequential credit process: offer stage, application or acceptance stage, contract finalization stage, repayment period, and possible future-borrowing period. Exact dates are withheld. |
| geographic or market scope | A lender serving a defined borrower population; exact lender identity and market are withheld. |
| sample construction | Prospective borrowers receive loan offers. Accepted loans are followed through repayment. Non-applicants remain observable for take-up but not repayment outcomes. |
| treatment or exposure variable | Loan terms and incentives that can vary at different stages, including terms shown before application, terms finalized after acceptance, and future-access or pricing incentives tied to repayment behavior. |
| outcome variable | Application or take-up, accepted loan amount if available, repayment status, delinquency/default, and future borrowing eligibility or terms. |
| covariates | Pre-offer borrower risk measures, prior borrowing history, demographics or income proxies if available, offer wave, branch or channel indicators. |
| panel or repeated structure | Borrowers can have linked observations across offer, acceptance, repayment, and future-borrowing stages. Treat stage-level records as linked rather than independent. |
| assignment or variation source | Researcher- or lender-controlled variation in offer terms and later incentive terms across eligible borrowers or offers. |
| assignment level | Borrower-offer level for initial terms; later terms or incentives may be assigned at borrower-loan level after acceptance. |
| outcome measurement level | Borrower-loan repayment record. |
| recommended clustering or inference level | Borrower level if multiple offers or loans can appear; otherwise offer wave or operational batch should be considered if assignment is batched. |
| repeated exposure | Possible if borrowers receive repeated offers or future borrowing opportunities. |
| compliance or take-up | Not all offered borrowers apply; not all applicants accept; later repayment incentives may matter only for accepted borrowers. |
| missingness or attrition | Repayment outcomes can be missing if records are incomplete, loans are transferred, or borrowers exit the lender's tracking system. |
| possible spillover or interference | Borrowers may share offer information; lender staff may treat borrowers differently if they know assigned terms. |

## Known Constraints

- The design should match the data structure above.
- The answer must distinguish causal claims from descriptive claims.
- The answer should state what cannot be learned from the available information.
- Do not assume that comparing high-rate and low-rate borrowers is sufficient.
- Do not rely on external facts about any named lender, country, loan campaign, or prior paper.

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
