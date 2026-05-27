# Run Configs

This directory stores reproducible OpenClaw / agent run policies for the benchmark.

The current canonical runtime is `benchmark_isolated`: a locally isolated OpenClaw agent that receives exactly one agent-facing task packet per run while keeping remote web and literature tools available by default.

Current canonical file:

- `run_config.md`
- `formal_eval_minimal_isolation.md`
- `batch_runner_spec.md`
- `batch_runner_spec.example.csv`

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
