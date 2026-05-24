# Evidence-Aware Output Contract

This file is the canonical output contract for every agent-facing benchmark task.

## Canonical Required Output

```markdown
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
```

## Canonical Claim-Evidence Table

```markdown
## Claim-Evidence Table

| Claim | Evidence Used | Claim Type | Confidence | What Would Falsify This Claim |
|---|---|---|---|---|
```

## Output Rules

- The entire response must be in English.
- If causal identification is not credible, the agent must say so explicitly in sections 8, 9, 10, and 17.
- `Evidence Used` must cite packet-local evidence such as `Research Setting`, `Data Card: assignment or variation source`, `Potential Threats`, or named variables. Do not cite external literature.
- `Claim Type` should use concise labels such as `causal`, `descriptive`, `mechanism`, `assumption`, or `limitation`.
- If a section is unsupported by the packet, the agent should write `Not supportable from the provided information` rather than invent content.
- If the task packet includes a required threat-response table, the agent must include it using the exact table requested in the packet.
