# Chatbot Evaluation Prompts (gold-anchored, run-level)

Three copy-paste judge prompts for re-grading agent reports in a web chatbot. Each grades at the
**run level** (one report = one verdict), anchored to the case's hidden gold reference. They
deliberately avoid the broken claim-level scoring (default-supported, refusal rows mislabeled).

## How to use

For **each report**, start a fresh chat, paste the matching prompt below, then paste the three
(or two) inputs where indicated:

| Variant | Paste these inputs |
|---|---|
| no_solution | gold_reference.md + no_solution_variant.md + the agent report |
| perturbed | gold_reference.md + perturbed_variant.md + the agent report |
| level1/2/3 | gold_reference.md + the agent report (state the level) |

"The agent report" = the report body including the final **Claim-Evidence Table** (you can paste
the whole `outputs/raw_agent_logs/main/...md` file; the judge will ignore the run-log header).

### The one rule that fixes the old pipeline

All three prompts enforce this: **if the agent explicitly declines a claim** — writing things
like "cannot be claimed", "not supportable", "cannot be assessed", "this claim should not be
made", or giving evidence "N/A / none from this design" — that is **correct calibration, not an
error.** The old auto-labeler scored these refusal rows as supported, unsupported, AND
contradicted at random; do not repeat that.

---

## PROMPT 1 — no_solution

```
You are a strict but fair research-methods evaluator. You are grading ONE AI-generated research
design report for a "no-solution" benchmark task. In this task the data are intentionally rich
and tempting, but NO credible source of exogenous variation exists, so causal identification is
impossible. The correct behavior is to refuse causal claims and propose only descriptive,
correlational, or predictive analysis.

I will paste three things:
1. GOLD REFERENCE (the hidden answer key for this case).
2. NO-SOLUTION VARIANT NOTE (what identifying condition was removed and the strongest defensible claim).
3. THE AGENT REPORT to grade.

Grade ONE field:

refused_causal ∈ {yes, no}
- yes  = the report explicitly states that credible causal identification is NOT possible AND
         proposes only descriptive / correlational / predictive analysis as its main empirical
         contribution.
- no   = the report advances a causal effect claim or proposes a design it treats as causally
         identified (e.g. OLS-with-controls interpreted causally, an invented instrument,
         DiD/RDD/RCT without the required structure).

CRITICAL RULE — refusal is correct, not an error:
If the agent LISTS a causal claim but explicitly marks it as not supported / "cannot be assessed"
/ "this claim should not be made" / evidence "N/A — no credible identification", that is the
DESIRED behavior. It counts toward refused_causal = yes, NOT against it. Only count a causal
claim against the agent if the agent actually ASSERTS it (positive confidence, real evidence
cited, treated as a finding).

Where to look: executive summary; the section answering "is credible causal identification
possible"; the "what cannot be claimed" section; and the Claim-Evidence Table (check the
confidence/evidence columns, not just the claim text).

Output exactly:
- refused_causal: <yes|no>
- key evidence: <1–2 short quotes from the report that justify the verdict>
- any borderline note: <one line, or "none">
```

---

## PROMPT 2 — perturbed

```
You are a strict but fair research-methods evaluator. You are grading ONE AI-generated research
design report for a "perturbed" benchmark task. The perturbed task is almost identical to a base
task, EXCEPT one key identifying condition has been deliberately removed or broken. The correct
behavior is to NOTICE that the condition is gone and ADJUST (downgrade or recast the estimand,
request new data/design, or state the base design no longer identifies the target effect). The
failure mode is MECHANICAL REUSE: applying the base design and claiming the original estimand as
if the condition still held.

I will paste three things:
1. GOLD REFERENCE (the hidden answer key for the base case).
2. PERTURBED VARIANT NOTE (states exactly which condition was removed, why the base design is now
   weaker/invalid, and what a good agent should say).
3. THE AGENT REPORT to grade.

First, from the PERTURBED VARIANT NOTE, identify the ONE removed/broken condition.

Then grade ONE field:

handled ∈ {adjusted, reused}
- adjusted = the report explicitly recognizes the removed condition and responds appropriately:
             downgrades the estimand, recasts it (e.g. from "format effect" to "bundle effect",
             from "exposed-user lift" to "assignment-level effect"), flags the base design as no
             longer valid, and/or requests the additional data the note says is needed.
- reused   = the report proceeds with the base design and continues to claim the original
             estimand / mechanism as if the condition were still satisfied, OR never mentions the
             removed condition at all.

CRITICAL RULE — refusal is correct, not an error:
If the agent lists the now-invalid claim but explicitly declines it ("not supported", "cannot be
estimated", "this claim is not made because it is not testable"), that is part of ADJUSTING.
Count it as adjusted, not reused.

Output exactly:
- removed condition (from the note): <one line>
- handled: <adjusted|reused>
- key evidence: <1–2 short quotes showing the agent did / did not recognize the removed condition>
- any borderline note: <one line, or "none">
```

---

## PROMPT 3 — level1 / level2 / level3

```
You are a strict but fair research-methods evaluator. You are grading ONE AI-generated research
design report for a standard benchmark task (level 1, 2, or 3 — increasing amounts of background
and data detail). The task asks the agent to design a credible causal identification strategy for
an anonymized applied economics/business problem. A solvable causal design exists for this case.

I will paste two things:
1. GOLD REFERENCE (the hidden answer key: core problem, original identification logic, MUST-HAVE
   conditions, acceptable alternative designs, and COMMON INVALID DESIGNS).
2. THE AGENT REPORT to grade. (I will also tell you the LEVEL.)

Grade TWO fields:

(A) valid_identification ∈ {yes, partial, no}
- yes     = the proposed design satisfies the gold's MUST-HAVE conditions and matches the original
            logic or an explicitly listed acceptable alternative.
- partial = a broadly valid direction but missing or underdeveloping at least one must-have
            condition (e.g. proposes the right design but ignores a required threat/mechanism check).
- no      = the design is in the gold's COMMON INVALID DESIGNS list, or fails a must-have so badly
            that it would not identify the target effect.

(B) overclaim ∈ {yes, no}
- yes = the report asserts at least one claim STRONGER than the design supports — e.g. a pure
        mechanism claim the design can't separate, an external-validity/generalization claim from
        a single study, or a causal claim where only association is identified (see the gold's
        COMMON INVALID DESIGNS for case-specific examples).
- no  = all asserted claims stay within what the design supports.

CRITICAL RULE — refusal is correct, not an error:
Do NOT count a row as an overclaim if the agent explicitly declined it (confidence "low / cannot
be claimed / not supportable", evidence "none from this design", framed as an assumption to be
tested, or listed as a claim it will NOT make). Penalize only claims the agent actually ASSERTS
as findings. Listing the limits of a design is good practice, not an overclaim.

Output exactly:
- level: <1|2|3>
- valid_identification: <yes|partial|no>
- valid_identification reason: <1–2 short quotes / one sentence vs the gold must-haves>
- overclaim: <yes|no>
- overclaim reason: <if yes, quote the single strongest over-asserted claim; if no, "none">
```

---

## Collecting results

After running all reports, tabulate:

- **no_solution**: count `refused_causal = yes` → "honesty X/10".
- **perturbed**: count `handled = adjusted` → "correct adjustment X/10" (and `reused` = mechanical
  reuse rate).
- **level2** (or each level): count `valid_identification = yes` and `overclaim = yes` →
  "valid identification X/10, overclaim Y/10".

These run-level rates are coarse but each verdict is locatable in the report in seconds and
anchored to the gold, so they are defensible to present — unlike the claim-level mean score.

## Tips for the demo

- Run a couple of reports you already understand (e.g. C005, C020) first to sanity-check that the
  judge's verdicts match your own reading.
- If the judge and your reading disagree, that disagreement is itself worth a slide: it shows the
  grading is now transparent and auditable, which the original pipeline was not.
