<!-- visibility: evaluator-only -->
<!-- do_not_include_in_agent_context: true -->
<!-- case_id: C002 -->

# Gold Reference: C002

## Hidden Answer Summary

This evaluator-only gold reference defines what a valid answer must handle for the consumer-credit information-asymmetry case. A valid answer does not need to reproduce the exact source experiment, but it must separate borrower selection before take-up from repayment incentives after borrowing.

## Core Research Problem

- Research question: Are repayment outcomes in consumer credit driven by adverse selection, moral hazard, or both? Evidence: F002.
- Benchmark objective: Design a credit-market experiment that separates borrower selection at take-up from incentive effects after borrowing. Evidence: F003.
- Target mechanism or estimand: Mechanism-specific effects of loan offer terms, final contract terms, and future-loan incentives on borrowing and repayment. Evidence: F004, F010-F015.
- Treatment or exposure: Initial loan offer rate, later contract rate, and future repayment incentive. Evidence: F010-F013.
- Outcome: Borrowing/take-up and repayment/default. Evidence: F014-F015.
- Unit of analysis: Potential borrower offer/application/loan repayment observation. Evidence: F005-F007.

## Data Structure

- Observation unit: Loan offer, application, or loan repayment observation. Evidence: F005.
- Assignment level: Borrower-offer level for initial offer and contract-rate dimensions, with exact implementation details still uncertain. Evidence: F006, U001.
- Outcome measurement level: Borrower-loan repayment/default. Evidence: F007.
- Time structure: Offer stage, application/acceptance stage, contract revelation stage, repayment/future incentive stage. Evidence: F008.
- Required information structure: Borrowers must not know the later contract-rate realization when deciding whether to apply. Evidence: F013, F016.
- Current uncertainty: Exact sample counts, dynamic-incentive randomization level, and standard-error level are not fully extracted. Evidence: U001-U002.

## Original Identification Logic

The source design is a staged/factorial randomized field experiment. Selection is identified by comparing repayment among borrowers who accepted different initial offer rates but ultimately received the same low contract rate. Moral hazard is identified using future-loan incentives that affect later benefits without changing the initial repayment burden. A blind-application check supports the timing and information assumptions. Evidence: F017-F020.

## Linchpin Detail

- Linchpin 1: Separate the initial offer rate from the later contract rate. Evidence: L001.
- Why it matters: It creates take-up selection variation while holding final repayment terms fixed for the adverse-selection comparison. Evidence: F018.
- What fails without it: A single randomized interest rate confounds selection into borrowing with repayment incentives. Evidence: L001, N001.
- Linchpin 2: Use a dynamic repayment incentive that does not change the initial loan burden. Evidence: L002.
- Why it matters: It isolates incentive effects after borrowing. Evidence: F019.
- Linchpin 3: Borrowers must be blind to the later contract rate at application. Evidence: L003.

## Must-Have Conditions

- The design must separately identify take-up selection and post-borrowing repayment incentives.
- The design must include at least two distinct randomized margins; a single loan-price randomization is insufficient.
- The design must observe both borrowing/take-up and repayment/default outcomes.
- The design must preserve an information structure where borrowers cannot select based on the later randomized contract term.
- The design must state what assumptions are needed to interpret repayment differences as adverse selection or moral hazard.

## Acceptable Alternative Designs

| design | conditions under which it is acceptable | supports what claim | cannot support what claim |
|---|---|---|---|
| Two-stage randomized offer and final contract terms | Final contract terms must be hidden at take-up and later randomly assigned. | Can identify selection into borrowing separately from repayment burden effects. | Cannot identify pure moral hazard unless a post-borrowing incentive margin is also varied. |
| Factorial design with offer price, realized repayment price, and future access incentive | Each margin must be randomized or plausibly exogenous; take-up and repayment must be observed. | Can separate adverse selection and moral hazard channels. | Cannot identify channels if borrowers anticipate all later terms at take-up. |
| Encouragement design for future repayment incentives among accepted borrowers | Future incentive must not alter initial debt burden and must be assigned independently of risk. | Can support moral-hazard evidence among borrowers. | Cannot estimate adverse selection into borrowing without separate take-up variation. |

## Common Invalid Designs

| design or claim | why unacceptable | error label |
|---|---|---|
| Randomize only one interest rate and compare default rates. | Default responses can reflect adverse selection or moral hazard. Evidence: N001. | Mechanism Confounding |
| Compare high-rate and low-rate borrowers without equalizing final contract terms. | Repayment differences mix selection into borrowing with repayment incentives. Evidence: N002. | Critical Design Omission |
| Use future incentives that also change the current repayment burden. | This no longer isolates post-borrowing moral hazard. Evidence: N003. | Mechanism Confounding |
| Claim adverse selection from higher default among high-offer borrowers without a common contract-rate comparison. | The repayment burden itself may drive default. Evidence: F018, L001. | Unsupported Claim |
| Ignore borrower information about later contract terms. | If borrowers anticipate later terms, take-up can be selected on final price. Evidence: L003. | Contradiction |

## Claim-Evidence Expectations

| expected claim | required supporting evidence | claim type | confidence |
|---|---|---|---|
| A single randomized interest rate is insufficient for mechanism separation. | F004, N001 | limitation | high |
| Adverse selection requires comparing borrowers with different offer rates but common final terms. | F018, L001 | mechanism | high |
| Moral hazard requires a post-borrowing incentive margin that does not change initial burden. | F019, L002 | mechanism | high |
| Blindness to the contract-rate randomization is a validity condition. | F013, F016, L003 | assumption | high |

## Scoring Notes

- Full-credit answer: Proposes a staged/factorial credit experiment with separate offer, realized contract, and post-borrowing incentive margins; observes take-up and repayment; states borrower information assumptions.
- Partial-credit answer: Recognizes adverse selection and moral hazard but only partially separates them, for example with offer and contract rates but no clean moral-hazard margin.
- Critical omission: No design feature separating take-up selection from repayment incentives.
- Automatic failure: Claims one randomized interest rate, OLS risk controls, or borrower observables alone identify adverse selection versus moral hazard.
