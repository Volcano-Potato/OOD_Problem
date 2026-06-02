# Stage 2: Retrieval And Calibration

You are working on an anonymized business or economics research-design task packet.

You are given:

- the original packet
- the Stage 0 planner JSON
- an OpenAlex seed summary produced outside the model

Your job in this stage is not to write the final report. Your job is to perform a targeted retrieval pass that checks:

- methodological fragility of candidate causal designs
- whether the packet likely supports only weaker descriptive fallback claims
- what external methodological cautions are relevant without reconstructing the hidden source paper

## Retrieval Rules

1. Treat the packet as the primary evidence source.
2. You may use remote web or scholarly search tools for methodological checking and design calibration.
3. Do not search for the hidden paper's title, authors, exact setting, location, or publication year.
4. Do not use retrieval to reverse-engineer evaluator-only materials.
5. You must attempt retrieval before finalizing this stage.
6. Use the Stage 0 planner to prioritize which threats and fallback triggers matter most.
7. You are also given an `OpenAlex` seed summary produced outside the model. Treat it as structured scholarly context, not as hidden-paper evidence.
8. Your first action in this stage must be a real retrieval tool call. Use this mandatory first-query template or a very close variant:
   - `{{MANDATORY_FIRST_QUERY}}`
9. You must make at least one real tool call using an available live retrieval tool:
   - prefer `deepxiv__search_papers`
   - if that is unavailable, use `web_search`
10. `semantic-scholar` is optional. Do not block the stage on it if `deepxiv` or `web_search` works.
11. Do not merely claim that you searched. A response with zero real tool calls is invalid and will be discarded.
12. If live retrieval fails because of rate limits, timeouts, or unavailable tools, record that failure explicitly and continue with a packet-grounded fallback summary.
13. Output JSON only. No prose before or after the JSON.

## Required JSON Schema

```json
{{RETRIEVAL_OUTPUT_SCHEMA_HINT}}
```

## OpenAlex Seed Summary

```json
{{OPENALEX_SEED_JSON}}
```

## Stage 0 Planner

```json
{{STAGE0_JSON}}
```

## Packet

{{PACKET_TEXT}}
