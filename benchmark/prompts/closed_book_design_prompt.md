# Packet-Grounded Design Prompt

Use this exact `Task Rule` block in every agent-facing task packet unless a later audit explicitly revises it.

## Canonical Task Rule

```markdown
## Task Rule

Use the information provided below to design a rigorous empirical strategy for this anonymized applied business/economics research problem. Your goal is to produce a defensible research design, not to write a literature review.

Do not assume that a known paper has already solved the task. Ground your reasoning in the background, data description, institutional details, and constraints provided in this packet.

Do not fill in packet-absent operational details, institutional features, or named design devices as if they were known facts. If multiple concrete implementations fit the packet, describe them generically or label them explicitly as illustrative examples rather than assumptions.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.
```

## Enforcement Notes

- The rule applies equally to Level 1, Level 2, Level 3, `perturbed`, and `no_solution` variants.
- The packet remains the primary evidence source even if a run environment exposes tools or retrieval.
- Task packets should not directly instruct the agent to identify the source paper or reproduce the original published design.
- The rule should actively discourage source-design reconstruction by penalizing unsupported operational specificity.
- Do not add source-paper names, author names, or evaluator-only hints to this block.
