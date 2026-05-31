# Stage 3: Candidate Identification Strategies

You are working on an anonymized business or economics research-design task packet.

Your job in this stage is not to write the final report. Your job is to enumerate candidate designs before any final commitment.

## Instructions

1. Read the packet carefully.
2. List at least 3 distinct candidate strategies.
3. Do not collapse multiple ideas into one bundled candidate.
4. If no credible causal design is defensible from the packet, at least one candidate must be a descriptive fallback and set `is_fallback` to `true`.
5. Stay inside the packet. Do not reconstruct hidden paper details.
6. Output JSON only. No prose before or after the JSON.

## Required JSON Schema

```json
{
  "candidates": [
    {
      "name": "short candidate name",
      "estimand": "target estimand or strongest defensible target",
      "identifying_variation": "what variation would identify it",
      "critical_assumption": "most important identifying assumption",
      "packet_support": "which packet-local evidence motivates this candidate",
      "fragility": "why this candidate may fail in this packet",
      "is_fallback": false
    }
  ],
  "recommended_primary": "candidate name or null",
  "notes": "optional short note"
}
```

## Packet

<!-- visibility: agent-facing -->
<!-- case_id: C010 -->
<!-- variant: perturbed -->

# Anonymous Research Design Task: Perturbed Variant

## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.

## Research Background

Small producers underuse a seasonal agricultural input even though modest use appears privately profitable. Managers want to know whether a well-timed early intervention can improve follow-through relative to later offers.

## Research Setting

Producers receive income or liquidity at one point in the cycle and must later decide whether to purchase and apply the input before a seasonal deadline. The researcher can vary the timing and form of offers, and can follow producers through the season to observe adoption.

## Research Objective

Assess whether early intervention timing changes actual seasonal input adoption and whether the observed pattern supports a procrastination or timing-based mechanism.

## Specific Questions To Answer

1. Can the researcher still cleanly identify the role of early timing in adoption?
2. How should the design separate timing effects from mere anticipation of a later offer?
3. What mechanism claims become weaker under the changed information structure?
4. Which claims remain defensible with the available data?

## Data Structure Overview

- Stage 1: Producers are observed around an early post-income moment in the seasonal cycle.
- Stage 2: Producers are randomly assigned to offer arms that differ in the timing and form of later purchase opportunities.
- Stage 3: Every producer is informed early in the season about whether and when a later offer window will occur.
- Stage 4: The researcher records actual seasonal input purchase or use and may also observe stated plans or program take-up.

## Data Card

| field | description |
|---|---|
| unit of observation | Producer-season or household-season adoption outcome. |
| time span | Early post-income moment, later application period, and within-season follow-up. |
| sample construction | Producers familiar with the input are observed before the seasonal application period and followed to determine actual adoption or use. |
| treatment or exposure variable | Randomized offer arm varying timing of the purchase window, convenience, or economic value, but all assigned schedules are announced early. |
| outcome variable | Actual input purchase or use in the relevant season. |
| secondary outcomes | Stated plans to adopt, stated preferred timing, or program take-up if observed. |
| assignment or variation source | Researcher-controlled random assignment to different offer schedules, all announced at the start of the decision period. |
| assignment level | Producer or household. |
| outcome measurement level | Producer-level actual adoption or use. |
| panel or repeated structure | Some producers may appear across more than one season or intervention round. |
| compliance or take-up | Not all producers accept the offer or follow through. |
| spillover or interference | Producers may discuss offer timing with others in nearby communities. |

## Variable Groups

### Treatment Or Exposure Variables

- Offer schedule announced early in the cycle.
- Timing and size of the later purchase opportunity.

### Selection Or Sample-Flow Variables

- Eligibility for the intervention.
- Program take-up.
- Completion of follow-up measurement.

### Main Outcome Variables

- Actual seasonal input purchase.
- Actual seasonal input use.

### Secondary Outcome Variables

- Stated intention to adopt.
- Stated timing preferences.

### Baseline Controls And Design Variables

- Prior adoption history.
- Baseline household or farm characteristics.
- Timing of the post-income moment relative to the assigned offer schedule.

## Perturbed Condition

Producers learn early in the season whether a later purchase window or later offer will be available to them. This means later intervention arms are anticipated well before the later purchase moment arrives.

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

