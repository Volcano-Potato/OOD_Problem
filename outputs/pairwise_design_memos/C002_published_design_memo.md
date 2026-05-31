# Published Design Memo

## Research Question
Research question: Are repayment outcomes in consumer credit driven by adverse selection, moral hazard, or both? Evidence: F002.

## Target Estimand
Target mechanism or estimand: Mechanism-specific effects of loan offer terms, final contract terms, and future-loan incentives on borrowing and repayment. Evidence: F004, F010-F015.

## Treatment And Outcomes
- Treatment or exposure: Initial loan offer rate, later contract rate, and future repayment incentive. Evidence: F010-F013.
- Outcome: Borrowing/take-up and repayment/default. Evidence: F014-F015.
- Unit of analysis: Potential borrower offer/application/loan repayment observation. Evidence: F005-F007.

## Identification Logic
The source design is a staged/factorial randomized field experiment. Selection is identified by comparing repayment among borrowers who accepted different initial offer rates but ultimately received the same low contract rate. Moral hazard is identified using future-loan incentives that affect later benefits without changing the initial repayment burden. A blind-application check supports the timing and information assumptions. Evidence: F017-F020.

## Key Data Structure
- Observation unit: Loan offer, application, or loan repayment observation. Evidence: F005.
- Assignment level: Borrower-offer level for initial offer and contract-rate dimensions, with exact implementation details still uncertain. Evidence: F006, U001.
- Outcome measurement level: Borrower-loan repayment/default. Evidence: F007.
- Time structure: Offer stage, application/acceptance stage, contract revelation stage, repayment/future incentive stage. Evidence: F008.
- Required information structure: Borrowers must not know the later contract-rate realization when deciding whether to apply. Evidence: F013, F016.
- Current uncertainty: Exact sample counts, dynamic-incentive randomization level, and standard-error level are not fully extracted. Evidence: U001-U002.

## Linchpin Conditions
- Linchpin 1: Separate the initial offer rate from the later contract rate. Evidence: L001.
- Why it matters: It creates take-up selection variation while holding final repayment terms fixed for the adverse-selection comparison. Evidence: F018.
- What fails without it: A single randomized interest rate confounds selection into borrowing with repayment incentives. Evidence: L001, N001.
- Linchpin 2: Use a dynamic repayment incentive that does not change the initial loan burden. Evidence: L002.
- The design must separately identify take-up selection and post-borrowing repayment incentives.
- The design must include at least two distinct randomized margins; a single loan-price randomization is insufficient.
- The design must observe both borrowing/take-up and repayment/default outcomes.
- The design must preserve an information structure where borrowers cannot select based on the later randomized contract term.

## Defensibility Assessment
Linchpin 1: Separate the initial offer rate from the later contract rate. Evidence: L001. Why it matters: It creates take-up selection variation while holding final repayment terms fixed for the adverse-selection comparison. Evidence: F018. The design must separately identify take-up selection and post-borrowing repayment incentives. The design must include at least two distinct randomized margins; a single loan-price randomization is insufficient.

## Proposed Design
- Treatment or exposure: Initial loan offer rate, later contract rate, and future repayment incentive. Evidence: F010-F013.
- Outcome: Borrowing/take-up and repayment/default. Evidence: F014-F015.
- Unit of analysis: Potential borrower offer/application/loan repayment observation. Evidence: F005-F007.
- Required information structure: Borrowers must not know the later contract-rate realization when deciding whether to apply. Evidence: F013, F016.
- Current uncertainty: Exact sample counts, dynamic-incentive randomization level, and standard-error level are not fully extracted. Evidence: U001-U002.
- The design must separately identify take-up selection and post-borrowing repayment incentives.
- The design must include at least two distinct randomized margins; a single loan-price randomization is insufficient.

## What Cannot Be Claimed Or Omitted
- Randomize only one interest rate and compare default rates. Why invalid: Default responses can reflect adverse selection or moral hazard. Evidence: N001.
- Compare high-rate and low-rate borrowers without equalizing final contract terms. Why invalid: Repayment differences mix selection into borrowing with repayment incentives. Evidence: N002.
- Use future incentives that also change the current repayment burden. Why invalid: This no longer isolates post-borrowing moral hazard. Evidence: N003.
- Claim adverse selection from higher default among high-offer borrowers without a common contract-rate comparison. Why invalid: The repayment burden itself may drive default. Evidence: F018, L001.
