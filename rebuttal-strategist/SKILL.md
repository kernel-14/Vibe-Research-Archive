---
name: rebuttal-strategist
description: Plan, investigate, and draft concise evidence-grounded academic rebuttals for paper reviews. Use when the user asks to respond to reviewers, write a rebuttal/author response, analyze reviewer intent, decide what experiments or code/results to mine, coordinate agent-team investigation, adapt responses to a venue format, or revise rebuttal text to be polite, direct, non-defensive, and claim-safe.
---

# Rebuttal Strategist

## Overview

Use this skill to turn reviews into a clear rebuttal strategy, evidence plan, and venue-ready author response. The default posture is calm, grateful, precise, and non-defensive: understand the reviewer first, fix the claim/evidence chain, then write only the response that matters.

## Required Startup

Read these references before substantial work:

- `references/user-profile.md` for the user's preferred rebuttal workflow and tone.
- `references/rebuttal-workflow.md` for the staged process.
- `references/evidence-and-tone.md` before writing or revising response text.
- `references/venue-patterns.md` when the venue, word limit, or response format matters.
- `references/source-notes.md` only when the user asks why this workflow is designed this way or wants external writing guidance.

## Workflow

### 1. Understand The Review

For each reviewer, extract:

- the reviewer's positive signals;
- the real decision risk behind each weakness;
- what the reviewer likely wants clarified, corrected, or added;
- whether the issue is a misunderstanding, missing evidence, underspecified method, weak experiment, overclaim, or scope concern.

Do not draft yet. Produce a short intent diagnosis first.

### 2. Set Goal And Subgoals

When the task is more than a quick polish, create a goal if requested or clearly useful. Convert reviewer concerns into subgoals:

- claim to defend or calibrate;
- evidence to cite from the paper;
- artifacts, code, logs, or experiments to inspect;
- new experiments needed, if any;
- response paragraph to write;
- camera-ready change to promise.

Keep subgoals reviewer-facing. Avoid work that will not change the response.

### 3. Build The Evidence Plan

Classify each concern:

- `paper-evidence`: already answered by paper tables, figures, appendix, or text.
- `artifact-evidence`: needs released code, generated outputs, logs, or repository inspection.
- `new-analysis`: needs mining existing results into a new table or statistic.
- `new-experiment`: needs a new run; estimate cost, time, and whether it is safe during rebuttal.
- `writing-fix`: needs clearer framing, scope, or claim calibration.

Prefer paper evidence in the final rebuttal. Use artifact paths internally; in reviewer-facing text, cite paper tables/sections and mention released artifacts or camera-ready additions.

### 4. Coordinate Agent Team

Use subagents only when the user asks for agent-team work or parallel investigation. Give each agent a bounded case, reviewer, experiment slice, or code/artifact audit. Ask for:

- concrete findings;
- paper table/section anchors;
- artifact or code paths for internal verification;
- recommended wording;
- risks and overclaim warnings.

Integrate agent output yourself. Do not paste raw agent reports into the rebuttal.

### 5. Decide The Position

For every reviewer concern, choose one stance:

- `agree-and-clarify`: the reviewer is right; clarify and state the camera-ready change.
- `agree-with-evidence`: the reviewer is directionally right; show existing evidence and add a scoped change.
- `correct-misunderstanding`: politely cite the paper evidence that resolves it.
- `new-supporting-analysis`: present a small existing-results analysis, not a rushed unsupported experiment.
- `future-work-boundary`: acknowledge scope and frame it as a boundary without weakening the contribution.

Write down the stance before drafting. Avoid arguing from emotion or fairness.

### 6. Draft Venue-Ready Response

Use this structure unless the venue format requires otherwise:

1. thank the reviewer and name the points they recognized;
2. restate the contribution in one or two sentences;
3. respond to each weakness under short labels;
4. cite existing paper evidence first;
5. mention released artifacts or planned camera-ready additions only when useful;
6. end with a concrete revision commitment.

Keep paragraphs compact. Use direct evidence and precise scope. Do not include local filesystem paths in final author responses.

### 7. Anti-Defensive Final Pass

Apply the anti-defensive writing rules:

- lead with the claim and evidence;
- thank without apologizing;
- state necessary limitations once;
- convert defensive caveats into positive scope;
- remove repeated "we do not claim" framing;
- replace vague hedges with evidence-based precision;
- avoid overpromising new experiments or camera-ready claims.

## Output Modes

Choose the smallest useful output:

- `intent map`: reviewer intent, risks, and response direction.
- `evidence plan`: what to mine, what to run, and what to cite.
- `working memo`: Chinese or English internal analysis with paths and detailed evidence.
- `venue draft`: concise author response in the venue language and format.
- `camera-ready plan`: exact additions to paper sections, tables, appendix, or limitations.

## Evolution Module

At the end of substantial use, summarize one to three observations about the user's rebuttal preferences, recurring bottlenecks, or helpful collaboration patterns. Ask whether each observation is accurate and worth retaining before proposing durable changes.

Use this ladder:

1. `observation`: one-session signal.
2. `profile_update`: repeated or user-confirmed user claim.
3. `skill_patch`: procedural change implied by a profile update.
4. `user_approval`: required before editing profile or skill files.

Never silently mutate `references/user-profile.md` or this skill.
