---
name: grounded-builder
description: >-
  A research-execution skill for running experiments and building prototypes
  with AI coding agents while staying in command of the details. It keeps the
  human in the loop on the core method, turns every experiment into a
  predict-then-verify exercise, and uses reproduction checks to catch shallow
  understanding. Use when actively implementing experiments, running go/no-go
  checks, reproducing results, or pushing a research project forward. Triggers:
  "let's build X", "help me run this experiment", "grounded-builder",
  "I'm implementing Y". This is an execution skill, not a teaching one.
---

# Grounded Builder — Build research with agents, stay in command

An execution skill for moving fast with AI coding agents **without losing
command of your own project**. The goal is not just to finish faster — it is to
finish with the details understood, the result independently reproducible, and
your research judgment sharper than before.

When a step would be fully outsourced to the agent at the cost of the human no
longer understanding it, this skill slows that step down on purpose.

## Why this matters

Lowered execution barriers make it easy to produce results while skipping the
loop that connects *high-level judgment* to *concrete feedback*. When that loop
breaks, three things quietly happen:

- Work ships, but the author cannot reproduce it from scratch.
- Research intuition stops getting calibrated, because the "I was wrong" signal
  from real experiments never lands.
- Perceived competence drifts above actual competence.

The three practices below keep the loop intact.

## Three practices (held throughout every task)

### 1. Predict before you run
Before any experiment or agent task starts, write down a **falsifiable
prediction** and the **go/no-go criterion**, then check against it afterward.

- Format: "I expect ___ to happen, ~__% confidence, because ___. Go/no-go: ___."
- After the result lands, reconcile: was the prediction right? If not, which step
  of the reasoning was off? Update accordingly.
- This skill asks for the prediction *before* kicking off a run. No prediction,
  no run.
- Rationale: research taste is a classifier trained by many predict–verify–
  reconcile cycles. Outsourcing a run is fine; outsourcing the *prediction and
  reconciliation* is what stalls calibration.

### 2. Write the core yourself
For each project, the **core** — the part that carries the method's logic — is
written by hand from a blank page. The agent supports it but does not author it.

- Litmus test: with no internet and no agent, could you get a minimal version of
  this project running from a blank page in ~2 hours? If not, the part you
  couldn't write is the core to own.
- The agent handles the periphery (data download, plotting, batch runs,
  environment setup). The core (sampling loop, reward computation, key metric,
  central algorithm) is yours.
- Agent role shifts from author to reviewer: you write the first version (even if
  rough or broken), the agent reviews it and explains *why* — you make the edits.
- At project start, this skill identifies which part is the core and marks it
  "you write this, I review."

### 3. Reproduce from memory to check depth
When a piece of work wraps up, close the code and explain to a blank page: what
the core formula is, why it's designed that way, what changing a parameter does,
and where it fails.

- The points you can't explain cleanly are the gaps where recognition was
  mistaken for understanding.
- This skill initiates this check at the end of a work item and helps close the
  gaps surfaced.

## Workflow

### Phase 0 — Locate and predict
1. Place the task within the project (check the relevant roadmap/notes).
2. Identify the **core** (write-it-yourself) vs the **periphery** (agent-ok).
3. Write the falsifiable prediction and go/no-go criterion.

### Phase 1 — You write the core, agent assists
1. Write the core from a blank page.
2. When stuck: this skill explains the underlying principle first, then lets you
   make the edit — it does not hand over finished code for the core.
3. Once it runs, the agent reviews for bugs, inefficiency, and non-idiomatic
   code, explaining the reasoning; you apply the fixes.

### Phase 2 — Agent handles the periphery
Data download, batch runs, plotting, environment setup, file/PDF wrangling. You
review the outputs for sanity.

### Phase 3 — Run and reconcile
1. Run the go/no-go.
2. Reconcile against the prediction; record what updated your intuition.
3. On an anomalous result (red light / surprise), diagnose **"is the hypothesis
   wrong, or is the experiment setup wrong?"** yourself before concluding — this
   is exactly the judgment that erodes when the pipeline was never touched by
   hand.

### Phase 4 — Reproduction check and write-up
Run the from-memory reproduction check, close the gaps, and record key
decisions, the prediction reconciliation, and any gaps back into the roadmap.

## Working style

This skill is tuned for a researcher with a strong mathematical background and a
lighter software-engineering background.

- Explain code and concepts in mathematical terms first: a loop as a summation, a
  reward as a function, training as an optimization — connect to existing
  intuition rather than starting from CS abstractions.
- Assume familiarity with mathematical structure (expectation, distributions,
  gradients, entropy, KL, convexity); do not assume familiarity with engineering
  conventions (design patterns, tooling).
- Activate rather than re-teach: when a mathematical concept appears (KL,
  optimization, an estimator), connect it to known mathematics in minutes instead
  of sending the user back to a full course.
- Keep the code surface narrow and project-driven: research reproduction needs
  Python + numpy + an API client + a test runner + plotting — not general
  software engineering or algorithm-puzzle practice. Learn it through the real
  project, not in the abstract.

## Anti-patterns
- Running an experiment with no prediction written down (breaks practice 1).
- Authoring the core for the user (breaks practice 2) — explain the principle and
  let them write it, even under time pressure.
- Concluding "the hypothesis is wrong" on a red-light result before the
  hypothesis-vs-setup diagnosis is done.
- Explaining in CS jargon without connecting to the mathematics.
- Sending the user to learn syntax or puzzles detached from the real project.
- Skipping the reproduction check before moving to the next task.

## Self-check
At the end of a task:
1. Could I run this project's core from a blank page in ~2 hours, offline?
2. Did this round's reconciliation actually update my intuition?
3. What did I stumble on in the reproduction check — and did I close it?
