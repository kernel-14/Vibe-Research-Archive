# Response Assembly Patterns

Use this reference when turning a long evidence memo into a polished final rebuttal. The structure is adapted from RebuttalStudio's useful workflow ideas, without requiring the external application.

## Five-Stage Mental Model

Use this compact pipeline:

1. `Breakdown`: split the review into atomic issues. Preserve strengths, weaknesses, questions, scores, and exact concern wording.
2. `Reply`: draft one response per issue from author-controlled evidence. The model polishes; it must not invent technical content.
3. `First-round assembly`: combine per-issue responses into a coherent, reviewer-facing document with labels, quotes, tables, and length checks.
4. `Follow-up condensation`: if discussion continues, condense each reviewer thread into key questions and main answers before writing follow-up replies.
5. `Final remarks`: summarize reviewer-recognized strengths, key concerns resolved, and concrete revision commitments for the AC.

Do not skip `Breakdown` when the review is dense. Missing an atomic concern is worse than writing a slightly longer response.

## Per-Issue Response Block

Default final block:

```markdown
## Response 1: [Short Concern Title]

> **Weakness 1 / Question 2:** [concise reviewer quote]

[Thank or acknowledge in one sentence when appropriate.] [Direct answer first.] [Evidence: paper table/figure/appendix first, then artifact/code/new analysis if needed.] [Explain what the evidence resolves.] [Camera-ready change.]
```

Use this block for reviewer-specific replies. For a global author response, use shorter labels such as `R1/W1`, `R2/Q3`, or the venue's official reviewer id.

## Opening And Closing

Opening paragraph:

- thank the reviewer directly;
- name the strengths they recognized;
- restate the paper contribution in one or two self-contained sentences;
- preview the concerns being addressed.

Closing paragraph:

- summarize the core clarification in one or two sentences;
- state concrete paper changes;
- thank the reviewer again.

Avoid a separate "Camera-ready changes" section unless the user asks for it. Fold commitments into the relevant response or closing summary.

## Formatting Rules

Use formatting to improve scanability, not decoration.

- Use `> blockquotes` for concise reviewer quotes.
- Use `Response 1`, `Response 2`, or `R1/W1` labels for fast navigation.
- Use tables for numeric comparisons, ablations, and compact case audits.
- Use bold only for the answer the reviewer must not miss.
- Keep table column names audience-facing: `Evidence`, `Result`, `Interpretation`, `What this shows`.
- Avoid UI-like color syntax, HTML spans, local paths, and decorative formatting in final text.
- Check the final response in the target submission platform because Markdown table support varies.

## Length Management

Treat long evidence drafts as source material, not final rebuttals.

When compressing:

1. Preserve meaning, stance, reviewer quotes, technical claims, named entities, numbers, equations, and commitments.
2. Remove repeated framing, case-selection explanations, filler, and duplicated interpretations.
3. Keep concrete data tables and representative cases by default.
4. Compress case audits into `case | score evidence | key difference | interpretation` tables.
5. If a response is still long, shorten prose before deleting data.
6. If the platform has a strict character limit, split only at natural response-block boundaries.

## Submission-Readiness Checks

Before finalizing, run this pass:

- Coverage: every material issue in the ledger appears in the assembled response.
- Tone: each block opens collaboratively and avoids defensive pivots.
- Factual accuracy: every number matches the paper, appendix, logs, or artifact analysis.
- Structure: the reader can navigate reviewer -> issue -> answer in under 30 seconds.
- Clarity: each block states the conclusion before background.
- Tables: each table is readable without surrounding notebook context.
- Human style: remove generic AI filler and vary sentence rhythm.

