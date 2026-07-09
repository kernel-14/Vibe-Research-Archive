# Rebuttal Workflow

## Phase 1: Reviewer Intent Map

For each reviewer, create a compact map:

| Item | Meaning |
| --- | --- |
| Positive signals | What the reviewer already accepts |
| Core risk | What could block acceptance |
| Hidden intent | What they need to be convinced of |
| Response stance | agree-and-clarify, correct-misunderstanding, new-supporting-analysis, future-work-boundary |
| Evidence needed | paper-evidence, artifact-evidence, new-analysis, new-experiment, writing-fix |

Do not start with a rebuttal paragraph. First decide what problem the response must solve.

## Phase 2: Goal And Subgoals

For a substantial rebuttal task, set:

- one goal for the target reviewer or full rebuttal;
- subgoals tied to each weakness or question;
- owners if using agent team;
- stop criteria for enough evidence.

Example:

```text
Goal: Convince reviewer R that the reported model gap reflects model-scaffold interaction, not scaffold irrelevance.
Subgoals:
1. Extract paper-table evidence for fixed-backbone scaffold gains.
2. Mine released artifacts for three high-gap cases.
3. Find external literature supporting model/harness interaction.
4. Draft response with calibrated claim and camera-ready promise.
```

## Phase 3: Evidence Classification

Use this decision rule:

- If the answer is in the paper, cite the paper first.
- If the answer is in released artifacts, summarize the artifact finding and promise a camera-ready table.
- If the answer needs new statistics over existing runs, produce a small reproducible analysis.
- If the answer needs expensive new experiments, propose only if the result could materially change the reviewer response.
- If the reviewer is asking for future scope, clarify boundaries and revision text instead of overpromising.

## Phase 4: Agent Team Use

Use agent team when concerns are independent and evidence-heavy:

- one reviewer per agent;
- one case study per agent;
- one result table or artifact directory per agent;
- one literature cluster per agent.

Each agent prompt should request:

- evidence;
- relative paths or paper anchors;
- risk assessment;
- candidate wording;
- what not to claim.

The main agent integrates and calibrates. Do not delegate the final rhetorical judgment.

## Phase 5: Position Matrix

Before drafting, make a position matrix:

| Concern | Our stance | Evidence | Wording boundary | Camera-ready change |
| --- | --- | --- | --- | --- |

This prevents defensive rambling and keeps the response aligned with evidence.

## Phase 6: Draft

Default reviewer response skeleton:

```text
We thank the reviewer for recognizing [accepted contribution]. ReproAgent's central contribution is [one-sentence contribution].

On [Weakness 1 label]. [Agree/clarify in one sentence]. [Paper evidence]. [Artifact or analysis summary if needed]. [Camera-ready change].

On [Weakness 2 label]. [Agree/clarify]. [Evidence]. [Scope statement]. [Camera-ready change].

We appreciate the suggestion and will revise the paper to include [concrete changes].
```

For a strict word limit, compress to:

```text
Thank you for recognizing [X]. We address the two concerns below.
W1: [stance + evidence + change].
W2: [stance + evidence + change].
We will add [specific camera-ready changes].
```

