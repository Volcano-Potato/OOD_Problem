<!-- visibility: agent-facing -->
<!-- case_id: C010 -->
<!-- variant: level3 -->

# Anonymous Research Design Task: Level 3

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

Small producers underuse a seasonal agricultural input even though modest use appears privately profitable. The practical policy question is whether adoption requires heavy subsidies or whether smaller interventions offered at the right point in the seasonal cycle can improve follow-through at much lower cost.

The key challenge is to distinguish a true timing or procrastination mechanism from more conventional explanations such as large subsidy effects, reminders, or general liquidity constraints.

## Research Setting

Producers receive income or liquidity at one point in the cycle and must later decide whether to purchase and apply the input before a seasonal deadline. The researcher can randomize when and how an offer is made, whether there is a small reduction in acquisition cost or hassle, whether a later offer is available, and whether producers receive reminders or timing options.

## Research Objective

Design a study to estimate whether an early small intervention changes actual seasonal input adoption and whether the resulting pattern is more consistent with procrastination or present-bias than with simple price sensitivity.

## Specific Questions To Answer

1. Does early intervention timing matter for actual seasonal adoption?
2. How should the design compare early and later offers so that subsidy size is not confused with timing?
3. What evidence would separate follow-through problems from reminder effects or static liquidity stories?
4. What mechanism claims about procrastination or commitment can be defended from the observed data?

## Causal Mechanisms To Distinguish

- Producers may plan to adopt but postpone the purchase until later and fail to act.
- A small early reduction in acquisition cost or hassle may work because it moves the decision to an earlier moment.
- Larger later price reductions may raise adoption through price alone without addressing the same mechanism.
- Reminder or salience interventions may change awareness without solving follow-through problems.

## Data Structure Overview

- Stage 1: The researcher observes producers around an early post-income moment in the seasonal cycle, before the input normally needs to be applied.
- Stage 2: Producers are randomly assigned to offer arms that vary timing, convenience, or economic value.
- Stage 3: Some offers occur early in the cycle, while others occur later, closer to the application period.
- Stage 4: The researcher records actual seasonal input purchase or use and may also observe stated intentions, program take-up, or chosen timing options.

## Data Card

| field | description |
|---|---|
| unit of observation | Producer-season or household-season adoption outcome. |
| time span | Early post-income moment, later application period, and within-season follow-up; exact dates are withheld. |
| geographic or market scope | Multiple local communities operating under similar seasonal production conditions. |
| sample construction | Producers familiar with the input are observed before the seasonal application period and followed to determine actual adoption or use. |
| treatment or exposure variable | Randomized offer arm varying timing of offer, acquisition-cost reduction, ordering convenience, reminder, or later subsidy intensity. |
| outcome variable | Actual input purchase or use in the relevant season. |
| secondary outcomes | Stated plans to adopt, chosen timing option, or program take-up if observed. |
| covariates | Baseline producer characteristics, prior adoption history, timing within the season, and other pre-treatment farm or household variables. |
| baseline or pre-treatment variables | Prior input use, prior production behavior, baseline resources, and other pre-offer characteristics. |
| panel or repeated structure | Some producers may appear across more than one season or intervention round. |
| assignment or variation source | Researcher-controlled random assignment to early or later offer conditions and comparison arms. |
| assignment level | Producer or household. |
| outcome measurement level | Producer-level actual adoption or use. |
| recommended clustering or inference level | Producer level or local randomization cluster if assignment is grouped operationally. |
| repeated exposure | Possible across seasons or across intervention rounds for subsets of producers. |
| compliance or take-up | Not all producers offered a program use it, and purchase through the program may not perfectly map into eventual use. |
| missingness or attrition | Seasonal follow-up and self-reported use may be incomplete for some producers. |
| possible spillover or interference | Producers may discuss offers or learn from neighbors within local communities. |

## Variable Groups

### Treatment Or Exposure Variables

- Early small acquisition-cost reduction or low-hassle ordering option.
- Later comparable offer.
- Later larger price reduction or other benchmark arm.
- Reminder or timing-choice arm if available.

### Selection Or Sample-Flow Variables

- Eligibility for the intervention.
- Program take-up or purchase through the offered channel.
- Completion of follow-up measurement.

### Main Outcome Variables

- Actual seasonal input purchase.
- Actual seasonal input use.

### Secondary Outcome Variables

- Stated intention to adopt.
- Chosen delivery or purchase timing.
- Short-run take-up of the offer itself.

### Baseline Controls And Design Variables

- Prior adoption history.
- Baseline household or farm characteristics.
- Timing of the post-income moment relative to the offer.

## Institutional Details Relevant For Identification

The intervention is controlled by the researcher or implementing team rather than by the producers themselves. Producers learn about the offer at different points in the seasonal cycle, and those points matter because cash on hand, planning, and later application decisions occur at different times.

Units can always decide whether to accept the offer, buy the input, and later use it. This means take-up and eventual use are separate objects. The packet includes pre-treatment information on past behavior, which can be used for balance checks and heterogeneity analysis. Outcomes are measured at the producer level, but some measures may rely on seasonal follow-up or self-report. Producers in the same local area may also talk to one another, so spillovers cannot be ruled out automatically.

## Potential Threats

- Potential selection or endogenous exposure issue: take-up of the offer is not random even if the offer assignment is.
- Potential timing, anticipation, or trend issue: some observed differences could reflect when producers have liquidity or are anticipating later offers rather than the intended mechanism.
- Potential mechanism-confounding issue: a larger later subsidy might raise adoption for price reasons even if timing does not matter.
- Potential measurement issue: stated plans and actual use may differ, and self-reported use can be imperfect.
- Potential spillover or interference issue: producers may learn about offer conditions from neighbors in nearby communities.
- Potential compliance, take-up, attrition, or missingness issue: not all assigned producers accept the offer or complete follow-up.
- Potential inference or clustering issue: if implementation is grouped by locality or visit schedule, naive household-level inference may overstate precision.

## Required Threat-Response Table

In addition to the standard output, include this table. If a threat cannot be addressed with the available data, say so.

| Threat | Why It Matters | Proposed Diagnostic Or Design Response | Remaining Limitation |
|---|---|---|---|

## Known Constraints

- The design should match the data, institutional details, and threats above.
- The answer must distinguish descriptive associations, randomized or quasi-random causal claims, and mechanism claims.
- The answer should state what cannot be learned from the available information.
- Do not turn the threat list into a generic robustness checklist. Connect each threat to the proposed design.
- Do not rely on unsupported source-specific facts about the original paper, place, institution, crop, or program.

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
