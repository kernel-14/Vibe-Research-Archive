---
name: rebuttal-strategist
description: Plan, investigate, and draft evidence-grounded academic rebuttals for paper reviews. Use when the user asks to respond to reviewers, write a rebuttal or author response, itemize reviewer comments verbatim, infer reviewer intent, decide what paper/code/results evidence to mine, plan or run rebuttal analyses, coordinate agent-team investigation, adapt responses to a venue format, or revise text to be polite, direct, AC-friendly, non-defensive, and claim-safe.
---

# Rebuttal Strategist

## Overview

Use this skill to turn reviews into a clear issue ledger, evidence plan, and venue-ready author response. The default posture is calm, grateful, precise, and non-defensive: understand the reviewer sentence by sentence, answer the direct question first, support the answer with evidence, and make the Area Chair able to judge the response without rereading the paper.

Audience model:

- Reviewers have read the paper to varying degrees, may have forgotten details, and may have misunderstood some design choices.
- The AC is likely less familiar with the paper. Assume the AC may read only the reviews and the rebuttal.
- A neutral third party should be able to tell whether each concern was addressed from the rebuttal alone.

## Required Startup

Read these references before substantial work:

- `references/user-profile.md` for the user's preferred rebuttal workflow and tone.
- `references/rebuttal-workflow.md` for the staged process and issue-ledger schema.
- `references/evidence-and-tone.md` before writing or revising response text.
- `references/venue-patterns.md` when the venue, word limit, reviewer threading, or response format matters.
- `references/response-assembly.md` when producing a polished final rebuttal, adapting RebuttalStudio-style per-issue structure, managing response labels, or compressing a long evidence draft into a submission-ready document.
- `references/source-notes.md` only when the user asks why this workflow is designed this way or wants external writing guidance.

For any nontrivial rebuttal, do not draft immediately. First create a reviewer issue ledger that quotes each material concern or question as faithfully as space allows, then analyze intent, evidence, and stance.

## Workflow

### 1. Build The Verbatim Issue Ledger

For each reviewer, copy the material comments, weaknesses, and questions into an itemized table before answering them. Preserve the original meaning and, when practical, the original wording. Then read each item sentence by sentence.

Minimum columns:

- reviewer and item id;
- original reviewer text or concise exact quote;
- surface question or weakness;
- hidden intent and decision risk;
- direct answer needed;
- evidence class: `paper-evidence`, `artifact-evidence`, `new-analysis`, `new-experiment`, `writing-fix`;
- response stance;
- camera-ready change.

Do not skip positive comments. Capture strengths first so the rebuttal can start from accepted contributions.

### 2. Diagnose Reviewer Intent

For each item, determine what the reviewer likely needs:

- clarification of an already-present detail;
- correction of a misunderstanding or factual error;
- stronger evidence for a benchmark, annotation, judge, or experiment claim;
- code, artifact, or case-study evidence;
- a new statistic over existing results;
- a limited new experiment;
- claim calibration or a clearer limitation.

Respond to the intent, not only to the literal phrasing. If a reviewer asks "Why not X?", decide whether the real concern is coverage, validity, fairness, reproducibility, novelty, or scope.

### 3. Set Goal And Subgoals

When the task is more than a quick polish, create a formal goal only if the user explicitly requests it. Otherwise, maintain local reviewer-facing subgoals:

- claim to defend, clarify, or calibrate;
- paper evidence to cite;
- artifacts, code, logs, generated repositories, or experiments to inspect;
- new analysis or experiment needed, if any;
- response paragraph to write;
- camera-ready edit to commit to.

Keep subgoals tied to decision risks. Avoid work that will not change the rebuttal.

### 4. Build The Evidence Plan

Classify every concern:

- `paper-evidence`: already answered by paper tables, figures, appendix, equations, or text.
- `artifact-evidence`: needs released code, generated outputs, logs, examples, or repository inspection.
- `new-analysis`: needs mining existing results into a new table, statistic, or case taxonomy.
- `new-experiment`: needs a new run; estimate cost, time, and whether the venue permits it.
- `writing-fix`: needs clearer framing, scope, or claim calibration.

Stats and concrete cases beat opinion. When disagreeing with a reviewer, first ask whether a table, paper line, artifact path, code excerpt, or small result analysis can settle the point.

### 5. Coordinate Agent Team

Use subagents only when the user asks for agent-team work or parallel investigation. Give each agent a bounded reviewer, concern, case study, result table, artifact directory, or literature cluster. Ask for:

- concrete findings;
- paper table, figure, section, or appendix anchors;
- repo-relative artifact or code paths for internal verification;
- concise evidence snippets when needed;
- recommended wording;
- risks and overclaim warnings.

Integrate and calibrate the output yourself. Do not paste raw agent reports into the rebuttal.

### 6. Decide The Position

For every item, choose one stance before drafting:

- `agree-and-clarify`: the reviewer is right; clarify and state the camera-ready change.
- `agree-with-evidence`: the reviewer is directionally right; show existing evidence and add a scoped change.
- `correct-misunderstanding`: politely cite evidence that resolves the issue.
- `new-supporting-analysis`: present a small existing-results analysis, not a rushed unsupported claim.
- `future-work-boundary`: acknowledge scope and frame it as a natural extension.
- `objective-error`: correct a factual mischaracterization directly, with evidence and a calm tone.

Avoid arguing from emotion or fairness. If a review is objectively wrong, spotlight the factual issue for the AC without attacking the reviewer.

### 7. Draft The Response

Use this order unless the venue format requires otherwise:

1. Thank the reviewer directly and name the strengths they recognized.
2. Restate the contribution in one or two self-contained sentences.
3. Quote or label each concern concisely.
4. Answer directly first. If the question is yes/no, start with yes/no or the nearest precise answer.
5. Give evidence: paper table/figure/section first, then artifact/code/results evidence if needed.
6. State the camera-ready change.
7. End with a concise appreciation or concrete revision summary.

Default to a complete venue-facing response that could be pasted into the rebuttal, not a plan, note, or evidence memo, unless the user asks for an internal draft. Use reviewer-facing language such as "Thank you for your..." or "As you pointed out..." instead of detached phrases such as "the reviewer says..." in final response text.

Do not merely promise. Explain the clarification, statistic, case evidence, or limitation in the rebuttal itself, then say it will be added to the paper.

For final venue drafts, assemble responses using an issue-block structure inspired by RebuttalStudio: opening paragraph, one block per material concern, concise quoted concern, direct response, evidence, and a closing summary. Keep labels scannable (`Response 1`, `W1`, `Q2`) and use Markdown blockquotes/tables when they help the reviewer and AC navigate.

### 8. Review, Trim, And Stress Test

Before finalizing:

- compare the draft against the issue ledger and ensure every material concern is addressed;
- check whether a neutral AC can understand the answer without rereading the paper;
- prioritize major decision risks over minor typos under strict limits;
- merge common concerns across reviewers only when it saves space without hiding reviewer-specific answers;
- keep reviewer labels easy to scan;
- ensure headings, table columns, and summaries read like author-response text, not internal analysis notes;
- remove defensive caveats, repeated apologies, and unsupported promises.

## Output Modes

Choose the smallest useful output:

- `issue ledger`: verbatim comments, intent, risk, evidence class, stance, and planned answer.
- `intent map`: reviewer intent, positive signals, risks, and response direction.
- `evidence plan`: what to mine, what to run, what to cite, and what not to claim.
- `working memo`: Chinese or English internal analysis with paths, code snippets, and detailed evidence.
- `venue draft`: concise author response in the venue language and format.
- `camera-ready plan`: exact additions to paper sections, tables, appendix, examples, or limitations.

## Evolution Module

At the end of substantial use, summarize one to three observations about the user's rebuttal preferences, recurring bottlenecks, or helpful collaboration patterns. Ask whether each observation is accurate and worth retaining before proposing durable changes.

Use this ladder:

1. `observation`: one-session signal.
2. `profile_update`: repeated or user-confirmed user claim.
3. `skill_patch`: procedural change implied by a profile update.
4. `user_approval`: required before editing profile or skill files.

Never silently mutate `references/user-profile.md` or this skill.
