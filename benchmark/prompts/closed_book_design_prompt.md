# Closed-Book Design Prompt

Use this exact `Task Rule` block in every agent-facing task packet unless a later audit explicitly revises it.

## Canonical Task Rule

```markdown
## Task Rule

You must not search the web, infer the original paper, or use external literature. Use only the information provided below. Your goal is to design a rigorous empirical strategy, not to write a literature review.

Do not assume that a known paper has already solved the task. Treat this as an anonymous applied business/economics research problem.

If credible causal identification is not possible from the provided information, do not invent an identification strategy. State the strongest defensible descriptive or correlational analysis instead.
```

## Enforcement Notes

- Closed-book means no external search, no paper-guessing, and no retrieval from outside the task packet.
- The rule applies equally to Level 1, Level 2, Level 3, `perturbed`, and `no_solution` variants.
- If a run environment exposes tools, the run config must still mark the task as closed-book and log any contamination.
- Do not add source-paper names, author names, or evaluator-only hints to this block.
