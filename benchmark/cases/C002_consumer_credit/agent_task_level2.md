<!-- visibility: agent-facing -->
<!-- case_id: C002 -->
<!-- variant: level2 -->

# Anonymous Research Design Task: Level 2

## Task Rule

You must not search the web, infer the original paper, or use external literature. Use only the information provided below. Your goal is to design a rigorous empirical strategy, not to write a literature review.

Do not assume that a known paper has already solved the task. Treat this as an anonymous applied business/economics research problem.

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
3. What information timing is required so that later terms do not contaminate take-up decisions?
4. Which repayment comparisons support mechanism-specific causal claims, and which remain confounded?

## Causal Mechanisms To Distinguish

- Different offer terms may sort different borrower types into the accepted-loan sample.
- Realized contract terms may change repayment burden after acceptance.
- Future access or pricing consequences may alter repayment incentives without changing the initial loan burden.
- Borrower knowledge of later terms can collapse the distinction between selection and post-borrowing incentives.

## Data Structure Overview

- Stage 1: Eligible prospective borrowers receive loan offers with observable pre-borrowing terms.
- Stage 2: Borrowers decide whether to apply for or accept the offer.
- Stage 3: Accepted borrowers receive finalized contract terms and enter repayment.
- Stage 4: The lender observes repayment outcomes and may also vary or observe future-credit consequences tied to repayment behavior.

## Data Card

| field | description |
|---|---|
| unit of observation | Prospective borrower offer, application, accepted loan, and repayment record. The analysis may require linked stages for the same borrower. |
| time span | Sequential credit process: offer stage, application or acceptance stage, contract finalization stage, repayment period, and possible future-borrowing period. Exact dates are withheld. |
| geographic or market scope | A lender serving a defined borrower population; exact lender identity and market are withheld. |
| sample construction | Prospective borrowers receive loan offers. Accepted loans are followed through repayment. Non-applicants remain observable for take-up but not repayment outcomes. |
| treatment or exposure variable | Loan terms and incentives that can vary at different stages, including terms shown before application, terms finalized after acceptance, and future-access or pricing incentives tied to repayment behavior. |
| outcome variable | Application or take-up, accepted loan amount if available, repayment status, delinquency or default, and future borrowing eligibility or terms. |
| secondary outcomes | Intermediate repayment behaviors, survival in good standing, and any downstream borrowing outcomes if observed. |
| covariates | Pre-offer risk measures, prior borrowing history, demographics or income proxies if available, offer wave, branch, or channel indicators. |
| baseline or pre-treatment variables | Borrower characteristics observed before the initial offer and any pre-existing lender information set. |
| panel or repeated structure | Borrowers can have linked observations across offer, acceptance, repayment, and future-borrowing stages. Treat stage-level records as linked rather than independent. |
| assignment or variation source | Researcher- or lender-controlled variation in offer terms and later incentive terms across eligible borrowers or offers. |
| assignment level | Borrower-offer level for initial terms; later terms or incentives may be assigned at borrower-loan level after acceptance. |
| outcome measurement level | Borrower-loan repayment record. |
| recommended clustering or inference level | Borrower level if multiple offers or loans can appear; otherwise offer wave, branch, or operational batch should be considered if assignment is grouped. |
| repeated exposure | Possible if borrowers receive repeated offers or future borrowing opportunities. |
| compliance or take-up | Not all offered borrowers apply; not all applicants accept; later incentive variation may matter only for accepted borrowers. |
| missingness or attrition | Repayment outcomes can be missing if records are incomplete, loans are transferred, or borrowers exit the lender's tracking system. |
| possible spillover or interference | Borrowers may share offer information; staff may treat borrowers differently if they observe assigned terms. |

## Variable Groups

### Treatment Or Exposure Variables

- Pre-borrowing offer terms.
- Realized post-acceptance contract terms.
- Future access or repayment-linked incentive terms.

### Selection Or Sample-Flow Variables

- Offer receipt.
- Application or take-up.
- Acceptance and loan origination.
- Follow-through into the repayment sample.

### Main Outcome Variables

- Take-up or acceptance.
- Repayment, delinquency, or default.

### Secondary Outcome Variables

- Loan amount if relevant.
- Intermediate repayment behavior.
- Future borrowing access or pricing if observed.

### Baseline Controls And Design Variables

- Pre-offer borrower risk measures.
- Prior credit history or lender-side information.
- Offer wave, branch, marketing channel, or operational batch indicators.

## Known Constraints

- The design should match the data structure above.
- The answer must distinguish descriptive associations, causal claims, and mechanism claims.
- The answer should state what cannot be learned from the available information.
- Do not label the final identification strategy by name unless you justify why the data support it.
- Do not rely on external facts about the original paper, lender, or country.

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
