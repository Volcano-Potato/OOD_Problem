# Eval Prompt — level1 / level2 / level3 (strict, continuous 0–10 design score)

Run-level judge prompt for grading standard (solvable) reports in a web chatbot, scored against
both the hidden gold reference AND the original source paper.

## What to paste (in a fresh chat)

1. This prompt.
2. `benchmark/cases/<CASE>/gold_reference.md` (the hidden answer key).
3. The ORIGINAL SOURCE PAPER for this case (you provide it).
4. The agent report: `outputs/raw_agent_logs/main/<CASE>_level<N>_...md`
   (paste the whole file; the judge ignores the run-log header). Tell the judge the LEVEL.

## Prompt

```
You are a STRICT research-methods evaluator. You are grading ONE AI-generated research design
report for a standard benchmark task (level 1, 2, or 3 — increasing background and data detail).
The task asks the agent to design a credible causal identification strategy for an anonymized
applied economics/business problem. A solvable causal design exists for this case.

I will paste three things:
1. GOLD REFERENCE (hidden answer key: core problem, original identification logic, MUST-HAVE
   conditions, ACCEPTABLE ALTERNATIVE designs, and COMMON INVALID designs).
2. ORIGINAL SOURCE PAPER (the real study this case is based on — the reference for a strong design).
3. THE AGENT REPORT to grade. I will tell you the LEVEL.

Framing:
- The agent need NOT reproduce the paper's exact method. The paper and the gold's "acceptable
  alternative designs" both count as full-credit identification. Credit any design meeting the
  gold's MUST-HAVE conditions, even if it differs from the paper.
- Judge the LEVEL fairly (lower levels disclose less), but apply the rubric strictly within the level.

Be a STRICT grader. Default to skepticism. High scores must be EARNED, not given for fluent
writing or for merely listing standard methods. Reserve 9–10 for designs that would satisfy a
demanding referee; most competent-but-imperfect reports should land in the 5–7 range; a design
that fails identification should score low regardless of presentation.

Score on a CONTINUOUS 0–10 scale (one decimal) as the sum of three components. Score each, then
add. Within each band, pick the LOW end unless the report clearly earns the high end.

A. Identification validity (0–4)
   Does the design credibly identify the TARGET estimand, meeting ALL of the gold's must-have
   conditions (or matching the paper / a listed acceptable alternative)?
   - 4   = all must-have conditions met; identification is airtight for the target estimand.
   - 3   = essentially valid but ONE must-have is under-specified.
   - 2   = right family of design but a real identification gap (a key source of variation is not
           pinned down).
   - 0–1 = a design from the gold's COMMON INVALID list, OR fails to identify the target estimand.

B. Threat & mechanism handling (0–3)
   Does it explicitly address THIS case's central linchpin(s) and named threats (selection,
   mechanism confounding, the specific identification threats in the gold)?
   - 3   = addresses the central linchpin AND the main named threats concretely.
   - 2   = addresses the central linchpin but misses a named threat.
   - 1   = only generic/boilerplate threat discussion.
   - 0   = ignores the central threat.

C. Claim calibration (0–3)
   Are the report's ASSERTED claims matched to what the design supports?
   - 3   = all asserted claims are within scope; key limits/assumptions stated explicitly.
   - 2   = exactly one minor overclaim.
   - 1   = one major overclaim (pure-mechanism claim the design can't separate, external-validity/
           generalization from a single study, or causal language where only association holds).
   - 0   = multiple or pervasive overclaims.

GATING RULES (apply after scoring, to keep the total honest):
  - If A ≤ 1 (identification fails), the TOTAL must not exceed 3.0, regardless of B and C.
  - If there is any major overclaim (C ≤ 1), the TOTAL must not exceed 6.5.

CRITICAL RULE — refusal is correct, not an error (component C):
Do NOT penalize a claim the agent explicitly DECLINED (confidence "low / cannot be claimed / not
supportable", evidence "none from this design", framed as an assumption to be tested, or listed as
a claim it will NOT make). Stating a design's limits is GOOD calibration → toward 3, not against
it. Penalize ONLY claims the agent actually ASSERTS as findings.

Output exactly:
- level: <1|2|3>
- A. identification validity: <0–4> — <one-line reason vs gold must-haves / paper>
- B. threat & mechanism handling: <0–3> — <one-line reason>
- C. claim calibration: <0–3> — <one-line reason>
- gating applied: <none | which cap and why>
- TOTAL design score: <0.0–10.0>
- strongest asserted overclaim: <quote it, or "none">
- vs original paper: <one line: matches / falls short of / valid alternative to the paper's design>
```

## Collect

Per level, average the TOTAL design score across the 10 runs → **mean design score (0–10) by
level**. Running all of level1/2/3 gives the information-gradient story (does the mean rise from
level1 → level3?). Under this strict rubric, expect most competent reports in the 5–7 band, with
identification failures and major overclaims capped low by the gating rules.
