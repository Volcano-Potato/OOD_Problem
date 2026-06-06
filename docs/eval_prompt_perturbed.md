# Eval Prompt — perturbed (strict)

Run-level judge prompt for grading perturbed reports in a web chatbot.

## What to paste (in a fresh chat)

1. This prompt.
2. `benchmark/cases/<CASE>/gold_reference.md`
3. `benchmark/cases/<CASE>/perturbed_variant.md`
4. The agent report: `outputs/raw_agent_logs/main/<CASE>_perturbed_...md`
   (paste the whole file; the judge ignores the run-log header).

## Prompt

```
You are a STRICT research-methods evaluator. You are grading ONE AI-generated research design
report for a "perturbed" benchmark task. The perturbed task is almost identical to a base task,
EXCEPT one specific identifying condition has been deliberately removed or broken. The ONLY fully
correct behavior is to NOTICE that specific condition is gone and ADJUST: downgrade or recast the
estimand, declare the base design no longer identifies the target effect, and/or request the
specific additional data the note says is needed. The failure mode is MECHANICAL REUSE: applying
the base design and claiming the original estimand/mechanism as if the condition still held.

I will paste three things:
1. GOLD REFERENCE (the hidden answer key for the base case).
2. PERTURBED VARIANT NOTE (states exactly which condition was removed, why the base design is now
   weaker/invalid, and what a good agent should say).
3. THE AGENT REPORT to grade.

First, from the PERTURBED VARIANT NOTE, identify the ONE removed/broken condition.

Then grade ONE field:

handled ∈ {adjusted, reused}

Award "adjusted" ONLY IF ALL of the following hold:
  (1) The report explicitly engages the SPECIFIC removed condition (not generic limitations).
      Naming the actual broken condition (e.g. "no opportunity-side logs for untreated users",
      "format is now bundled with markdown") is required.
  (2) It changes its primary answer accordingly — recasts the estimand, downgrades the target
      effect, or declares the base design invalid — rather than keeping the original estimand as
      the headline and only footnoting the problem.
  (3) It does NOT assert the original target estimand / mechanism as if still identified.

Award "reused" if ANY of the following hold:
  - the report never mentions the specific removed condition;
  - it lists only generic caveats (attrition, external validity, "more data would help") that do
    not engage the actual perturbation;
  - it acknowledges the problem in passing but still reports the original estimand/mechanism as
    its primary causal result;
  - it reuses the base identification design and reaches the base conclusion.

Be strict: a caveat is not an adjustment. Acknowledgment WITHOUT changing the primary estimand or
conclusion ⇒ "reused".

CRITICAL RULE — refusal is correct, not an error:
If the agent lists the now-invalid claim but explicitly declines it ("not supported", "cannot be
estimated", "this claim is not made because it is not testable"), that is part of ADJUSTING and
supports "adjusted".

Output exactly:
- removed condition (from the note): <one line>
- did the report name this specific condition: <yes|no — quote it>
- did the report change its primary estimand/conclusion: <yes|no — quote it>
- handled: <adjusted|reused>
- justification: <2–3 short quotes>
```

## Collect

Count `handled = adjusted` across the 10 perturbed runs → **correct adjustment X/10**.
The complement (`reused`) is the **mechanical reuse rate**. Under this strict bar, mere caveats
do not count as adjustment — the report must actually change its primary answer.
