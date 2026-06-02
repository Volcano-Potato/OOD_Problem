# Stage 5: Final Design Memo

You are writing the final memo after reviewing:

- the original perturbed task packet
- the Stage 0 planner
- the OpenAlex seed summary
- the Stage 2 retrieval summary
- the Stage 3 candidate list
- the Stage 4 independent critique
- the Stage 3b debate response
- the Stage 4b final critique

Your output must follow the existing evidence-aware benchmark report structure.

## Required Reconciliation Rule

You must reconcile the Stage 4 critic verdict.

- If the critic marks a candidate `not_defensible`, do not present it as a credibly identified causal design unless you explicitly point to packet-local evidence that the critic missed.
- If the critic recommends a descriptive fallback, you must either adopt that downgrade or explain, with packet-local evidence, why a stronger design is still defensible.
- If the Stage 4b final critique still leaves a material issue unresolved, your memo must reflect that unresolved status in the estimand and claim scope.
- In section 17, explicitly state what cannot be claimed in light of the critique.

## Required Retrieval Rule

- If Stage 2 retrieval failed, say so explicitly and do not pretend that external evidence was obtained.
- If Stage 2 retrieval was methodologically helpful, use it only to calibrate fragility, fallback logic, or cautionary interpretation.
- Do not import hidden source-paper details from retrieval.

## Required Output Contract

Follow this structure exactly:

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

Use the canonical claim-evidence table header:

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|

## Retrieval Summary

```json
{{STAGE2_JSON}}
```

## Stage 0 Planner

```json
{{STAGE0_JSON}}
```

## OpenAlex Seed Summary

```json
{{OPENALEX_SEED_JSON}}
```

## Original Packet

{{PACKET_TEXT}}

## Stage 3 Candidate JSON

```json
{{STAGE3_JSON}}
```

## Stage 4 Critique

{{STAGE4_CRITIQUE}}

## Stage 3b Debate Response

```json
{{STAGE3B_JSON}}
```

## Stage 4b Final Critique

{{STAGE4B_CRITIQUE}}
