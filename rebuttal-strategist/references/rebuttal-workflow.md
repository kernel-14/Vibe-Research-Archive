# Rebuttal Workflow

## Phase 1: Verbatim Reviewer Issue Ledger

Start by itemizing reviewer comments. Copy each material concern, question, weakness, and requested addition into a table before drafting. This is the highest-leverage step because it prevents missing comments and forces careful intent reading.

Recommended schema:

| Field | Meaning |
| --- | --- |
| Reviewer | Reviewer id or tag |
| Item | W1, Q1, typo, limitation, experiment request, etc. |
| Original text | Exact quote or faithful compact quote |
| Surface concern | What the reviewer explicitly asks |
| Hidden intent | What decision risk they are really probing |
| Direct answer | The first sentence the rebuttal should give |
| Evidence class | paper-evidence, artifact-evidence, new-analysis, new-experiment, writing-fix |
| Evidence anchor | table, figure, section, appendix, repo-relative path, case id |
| Stance | agree-and-clarify, correct-misunderstanding, new-supporting-analysis, future-work-boundary, objective-error |
| Camera-ready change | Specific text, table, appendix, limitation, or example to add |

Also record positive signals. They are useful for the opening paragraph and for reminding the AC what reviewers already found valuable.

## Phase 2: Brain Dump Possible Responses

For each ledger row, write rough answers without worrying about style or length. Include:

- the direct answer;
- why the reviewer may have asked it;
- existing paper evidence;
- additional code, result, or artifact evidence to mine;
- what can be safely promised for the camera-ready version;
- what not to claim.

Being convincing and concise is a subtractive process. First collect the material, then compress.

## Phase 3: Evidence Classification And Work Plan

Use this decision rule:

- If the answer is already in the paper, cite the paper first and restate the relevant detail.
- If the answer is in released artifacts, summarize the artifact finding and cite repo-relative paths in the working memo or concise artifact names in final text.
- If the answer needs new statistics over existing runs, produce a small reproducible analysis.
- If the answer needs new experiments, run only if the venue permits it, the cost is reasonable, and the result would materially change the response.
- If the reviewer asks for broader scope, clarify the boundary and state a camera-ready limitation or future-work addition.

For substantial tasks, create subgoals tied to the ledger:

```text
Goal: Convince reviewer R that concern X is addressed by existing evidence plus a targeted clarification.
Subgoals:
1. Cite the relevant paper table/section.
2. Mine three representative artifact/code cases.
3. Add one compact statistic from existing results.
4. Draft direct-answer-first response.
5. State the camera-ready addition.
```

## Phase 4: Agent Team Use

Use agent team when concerns are independent and evidence-heavy:

- one reviewer per agent;
- one case study per agent;
- one result table or artifact directory per agent;
- one literature cluster per agent.

Each agent prompt should request:

- evidence;
- paper anchors;
- repo-relative paths or case ids;
- risk assessment;
- candidate wording;
- what not to claim.

The main agent integrates and calibrates. Do not delegate the final rhetorical judgment.

## Phase 5: Position Matrix

Before drafting, make a position matrix:

| Concern | Our stance | Direct answer | Evidence | Wording boundary | Camera-ready change |
| --- | --- | --- | --- | --- | --- |

This prevents defensive rambling and keeps the response aligned with evidence.

## Phase 6: Draft Without Space Anxiety

Default response skeleton:

```text
We thank the reviewer for recognizing [accepted contribution]. [Paper name]'s central contribution is [one or two self-contained sentences].

Concern: "[concise reviewer quote]."
Response: [Direct answer first.] [Paper evidence.] [Artifact/code/result evidence if needed.] [What this means for the reviewer concern.] [Camera-ready change.]

Concern: "[concise reviewer quote]."
Response: [Direct answer first.] [Evidence.] [Scope or limitation if needed.] [Camera-ready change.]

We appreciate the suggestion and will revise the paper to include [specific changes].
```

If a strict word limit applies, compress only after every material concern has a draft answer.

## Phase 7: Review, Revise, And Trim

Check the draft against the original reviews and the ledger:

- Every material concern has a visible answer.
- Major concerns appear before minor points unless reviewer-thread order is required.
- Common concerns are consolidated only when this improves clarity.
- The AC can understand the setup, acronym, and evidence without rereading the paper.
- Direct answers appear before background.
- Statistics or cases support disagreements.
- Camera-ready changes are concrete.
- Tone is polite, receptive, and non-defensive.
