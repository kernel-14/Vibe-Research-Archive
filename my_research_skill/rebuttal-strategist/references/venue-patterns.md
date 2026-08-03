# Venue Patterns

Use official venue instructions first. If unknown, infer a conservative conference-style response.

## General AC-Facing Pattern

Write so the AC can evaluate the response without rereading the paper:

```text
Thank you for recognizing [shared strengths]. The paper introduces [one-sentence contribution]. We address the main concerns below.
R1/W1: [direct answer + evidence + change].
R2/Q1: [direct answer + evidence + change].
```

If reviewer-specific threads are allowed, still make each reply self-contained.

For long reviewer-specific replies, use a structured block format:

```text
Thank you for your careful review and for recognizing [strengths]. In this work, [brief contribution]. We address your main concerns below.

Response 1: [Concern title]
> Weakness 1: [concise quote]
[direct answer + compact evidence + interpretation + change]

Response 2: [Concern title]
> Weakness 2: [concise quote]
[direct answer + compact evidence + interpretation + change]

In summary, [takeaway + concrete revision commitment]. Thank you again.
```

## ARR / ACL-Style

Typical posture:

- brief, factual, and focused on serious misunderstandings or key clarifications;
- be careful with new experimental results if current instructions restrict them;
- write in a way that helps action editors update the metareview.

Pattern:

```text
Thank you for your careful review and for recognizing [X]. We address your main concern about [Y].
Concern: "[reviewer quote]."
Response: [Direct clarification with paper evidence.]
Change: [specific camera-ready edit.]
```

When ARR/OpenReview provides separate reviewer threads, prefer `Response 1`, `Response 2`, etc. for that reviewer rather than a global combined memo. This helps the reviewer map each answer back to their own weakness/question.

## AAAI-Style

Typical posture:

- single compact response;
- prioritize all reviewers' highest-impact concerns;
- do not add URLs if prohibited by the current venue instructions;
- avoid relying on rushed new experiments.

Pattern:

```text
Thank you for recognizing [X]. We address the main concerns:
R1/W1: [direct answer + evidence + change].
R2/W1: [direct answer + evidence + change].
```

## NeurIPS / ICLR / OpenReview-Style

Typical posture:

- respond in threads or grouped bullets;
- reviewers may update scores after discussion;
- direct replies to actionable concerns work better than broad persuasion.

Pattern:

```text
Thank you for the question. The key point is [claim].
Evidence: [table/figure/appendix/case].
Change: [camera-ready edit].
```

## Journal-Style Response Letter

Typical posture:

- more formal and exhaustive;
- quote reviewer comments or number each comment;
- include "Response" and "Revision" blocks;
- include manuscript line/section changes when available.

Pattern:

```text
Comment 1: [quoted or summarized comment]
Response: [direct answer + evidence]
Revision: [section/line change]
```

## Format Decision

Choose format by venue constraints:

- strict global word/character limit: compress across reviewers and prioritize decision risks;
- OpenReview thread: answer each reviewer separately and keep each reply short;
- camera-ready response letter: include exhaustive comment/response/revision pairs;
- internal memo: include paths, raw evidence, and longer reasoning;
- user asks for formal evidence: include concise case evidence in the draft, not only in the memo.

## Reviewer Labels

Make relevant replies easy to spot:

- use reviewer tags such as `R1/W1`, `mU8h-Q1`, or the venue's official reviewer ids;
- group shared concerns only when a merged answer is clearer;
- when grouping, mention all affected reviewer ids in the label.
