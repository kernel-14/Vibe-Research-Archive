---
name: intro-story-rewriter
description: "Rewrite technical-paper introductions around a clear task-motivation-evidence-gap-method-contribution chain. Use when an intro feels vague, defensive, mechanically structured, overuses broad nouns, buries the real motivation, mixes evidence sources, or needs a stronger opening story for AI, systems, benchmark, or agent papers."
---

# Intro Story Rewriter

Use this skill to revise an Introduction so the reader can state the paper's
problem, evidence, method, metrics, benchmark, and result after one pass.

## Workflow

1. Identify the real headline claim.
   - State the target task in the first sentence.
   - Name the actual object of study, not a nearby generic object.
   - Prefer concrete terms such as "agentic code search" over broad terms such as
     "repository search" when the paper studies an agent loop.
2. Anchor the motivation with evidence.
   - Put the strongest reported or measured number next to the claim it supports.
   - Keep sources separated. Do not make a figure, table, or sentence appear to
     report a measurement it did not produce.
   - Use "As reported by X, ..." when the number is borrowed from prior work.
   - Use "We audit/measure/find ..." only for the paper's own analysis.
3. Move from cost or failure to the missing interface.
   - Describe what current methods already do well before stating what remains
     expensive or unmanaged.
   - Avoid weak transitions such as "however, this remains challenging" unless
     the next sentence names the concrete bottleneck.
   - For agent papers, distinguish "finding candidates" from "reading,
     remembering, and stopping after candidates are found."
4. State the goal in economic or operational terms.
   - Convert the bottleneck into a measurable objective.
   - For cost papers, define the objective as a cost-utility tradeoff, not only
     lower tokens or higher accuracy.
5. Introduce the method as a response to the diagnosed failures.
   - Use one sentence for the framework.
   - Map each module to one failure mode.
   - Keep implementation details for the method section.
6. Introduce metrics and benchmark only after the method goal is clear.
   - Explain why existing metrics do not capture the paper's target tradeoff.
   - State what the benchmark exposes, what it hides for scoring, and what it
     measures.
7. End with three concrete contributions.
   - Method contribution.
   - Metric or problem-formulation contribution.
   - Benchmark or evidence contribution.
   - Include one result sentence after the contribution list if the result is a
     major selling point.

## Paragraph Shape

Use this six-paragraph shape for most AI conference introductions:

1. Task and motivation: what agents/models need to do, what already works, and
   what cost or failure remains.
2. Diagnostic evidence: reported evidence plus the paper's own audit, clearly
   separated.
3. Problem essence: the missing interface, definition, or objective.
4. Method overview: one framework, one module per diagnosed failure.
5. Evaluation setup: metrics and benchmark that make the objective measurable.
6. Contributions and headline results.

## Style Rules

- Start with the task, not the method name.
- Prefer "but" for direct contrast and "as reported by" for borrowed evidence.
- Avoid defensive phrasing: "rather than", "not merely", "we do not claim",
  and "this is only" often weaken the story.
- Avoid premature abstraction. Use the specific object first, then generalize.
- Do not overuse "modern", "novel", "comprehensive", or "framework" unless the
  sentence still carries concrete information without them.
- Keep figure captions honest: state which panel comes from prior work and which
  panel comes from the paper's own experiment.

## Reference

For a compact checklist with examples and banned rewrites, read
`references/intro-evidence-chain.md`.
