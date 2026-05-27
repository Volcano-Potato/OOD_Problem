# Prompts

This directory contains reusable prompt blocks and output contracts for benchmark execution.

Current policy:

- `closed_book_design_prompt.md` defines the canonical agent-facing task rule.
- `evidence_aware_output_contract.md` defines the canonical agent-facing output schema.
- Agent-facing prompts should be packet-grounded: they should focus the agent on the provided background, data description, constraints, and evidence structure.
- Do not place source-paper titles, author names, or gold-reference answers in any agent-facing prompt block stored here.
- Construction-only prompts, if added later, must be clearly marked evaluator-only.
