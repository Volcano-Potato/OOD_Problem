# Run Configs

This directory will contain OpenClaw / agent run configurations.

Run configs should point only to files matching:

```text
benchmark/cases/*/agent_task_*.md
```

They must not load:

- `metadata.yaml`
- `source_packet.md`
- `source_facts.md`
- `gold_reference.md`
- `perturbed_variant.md`
- `no_solution_variant.md`
- `audit.md`
