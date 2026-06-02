# Stage 0: Planner

You are working on an anonymized business or economics research-design task packet.

Your job in this stage is not to write the final memo. Your job is to create a concise execution plan that will guide:

- what estimands are even worth considering
- which packet-local threats must be checked before any causal claim
- what live retrieval should prioritize
- when the pipeline should downgrade to a descriptive fallback

## Planner Rules

1. Treat the packet as the primary evidence source.
2. Do not reconstruct the hidden paper's title, authors, location, or evaluator-only details.
3. Focus on identification, threat recognition, retrieval priorities, and downgrade conditions.
4. Keep the planner specific enough to constrain later stages.
5. `primary_estimand_hypotheses`, `threat_checks`, `search_priorities`, and `fallback_triggers` must each be JSON arrays of plain strings.
6. Do not use JSON objects, key:value maps, or labeled subfields inside those arrays.
7. Output JSON only. No prose before or after the JSON.

## Required JSON Schema

```json
{{PLANNER_OUTPUT_SCHEMA_HINT}}
```

## Packet

{{PACKET_TEXT}}
