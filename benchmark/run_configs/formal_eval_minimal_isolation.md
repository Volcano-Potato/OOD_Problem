# Formal Eval Minimal Isolation

This file defines the minimum isolation standard for a **formal** benchmark run intended to measure research-design reasoning under local-file isolation, while still allowing remote web and literature tools.

## Core Principle

```text
One run should expose exactly one agent-facing task packet and nothing else.
```

Operationally:

- one run = one `case_id`
- one run = one `variant_id`
- one run = one `agent_task_*.md`
- do not combine multiple packets from the same case
- do not append hidden notes, operator summaries, or evaluator hints

## Minimal Isolation Requirements

### 1. Input Isolation

- Pass exactly one file matching:

```text
benchmark/cases/*/agent_task_*.md
```

- Do not inject:
  - `metadata.yaml`
  - `source_packet.md`
  - `source_facts.md`
  - `gold_reference.md`
  - `audit.md`
  - `perturbed_variant.md`
  - `no_solution_variant.md`
- Do not give the agent multiple variants from the same case in the same run.

### 2. Session Isolation

- Use a fresh session for every formal run.
- Do not reuse a session that has already seen another case or another variant.
- If the platform has persistent memory, disable it or treat the run as `suspected`.

### 3. Workspace Isolation

- Prefer a clean workspace outside the benchmark repository, or a sandbox workspace containing no evaluator-only files.
- If the benchmark repository remains accessible on disk and file tools are enabled, the run is not clean by default.
- If file tools are enabled, document this explicitly and downgrade the contamination status accordingly.

### 4. Tool Isolation

For the benchmark's canonical formal configuration, disable:

- local file-reading tools
- local file-writing tools
- directory listing tools
- any MCP server that can access local repository content

Keep enabled by default:

- web search tools
- web fetch tools
- literature tools
- remote MCP servers that operate only on remote content

If remote tools are enabled, record that configuration and the actual tool-use trace in the raw log. Remote-tool availability alone does not make the run `suspected`.

### 5. Retrieval Isolation

- Do not allow the agent to identify the source paper as an explicit sub-goal.
- Do not use prompts that encourage literature matching or paper reconstruction.
- If the agent names the source paper or reconstructs case-specific design machinery not present in the packet, mark the run `suspected` or `contaminated` depending on severity.

### 6. Prompt Isolation

- Keep the system prompt minimal and benchmark-specific.
- Do not add helper instructions that summarize hidden gold logic.
- Do not ask the model to be “as specific as possible” without also constraining unsupported specificity.

### 7. Packet-Boundary Discipline

The agent may propose concrete designs, but it must not present packet-absent details as known facts.

Acceptable:

- “One possible implementation is ...”
- “If the intervention can be randomized at the borrower-offer level ...”
- “A generic low-cost avoidance mechanism could be used ...”

Not acceptable:

- asserting a specific opt-out device, ghost-auction system, undisclosed second-stage contract workflow, or triple-difference structure as if the packet had already established it

### 8. Logging Requirements

Every formal run should record:

- exact input packet path
- exact model and provider
- exact tool configuration
- whether file tools were enabled
- whether web or literature tools were enabled
- session identifier
- workspace path
- contamination status and reason

## Clean vs Suspected vs Contaminated

### `clean`

Use only when all of the following hold:

- exactly one agent-facing packet was exposed
- evaluator-only files were unreachable
- local file tools were disabled or provably harmless
- remote-tool availability and actual tool-use trace were logged
- no session-memory leakage risk is present

### `suspected`

Use when:

- tools were enabled in a way that might have exposed hidden local material
- session isolation is incomplete
- the model filled in packet-absent operational specifics
- the model appears to reconstruct source-design details
- actual tool use cannot be reconstructed from logs

### `contaminated`

Use when:

- evaluator-only files entered context
- the agent actually accessed hidden answer materials
- exact input reconstruction is impossible
- the operator cannot rule out direct answer exposure

## Recommended Formal Configuration

For the benchmark's canonical formal run, the preferred setup is:

- fresh session
- isolated workspace
- one `agent_task_*.md` pasted or passed directly
- file tools disabled
- web tools enabled
- literature MCP enabled if remote-only
- memory disabled
- full manifest and raw-log recording

## Current Local Setup

The repository now maintains a dedicated local OpenClaw agent for this pattern:

- `agent_id`: `benchmark_isolated`
- fixed workspace: `/Users/jiangcanxiang/OpenClawBenchmarkIsolated`
- no local file-read/write tools exposed to the agent
- remote web and literature tools allowed by default
- task packet passed as external message text
- fresh session recommended for every run

Recommended launcher:

```bash
./scripts/run_isolated_packet.sh benchmark/cases/C001_charitable_giving/agent_task_level2.md
```

This launcher:

- reads the packet outside OpenClaw
- sends the packet as plain message text
- uses the isolated agent
- generates a fresh explicit session id for the run
- defaults to `86400` seconds timeout unless a shorter value is passed explicitly
