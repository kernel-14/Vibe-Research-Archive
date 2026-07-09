# Venue Patterns

Use official venue instructions first. If unknown, infer a conservative conference-style response.

## ARR / ACL-Style

Typical posture:

- brief, factual, and focused on serious misunderstandings or key clarifications;
- avoid large new experiments during the response window;
- write in a way that helps action editors update the metareview.

Pattern:

```text
Thank you for the careful review. We address the main concern about [X].
[Clarification with paper evidence.]
[Revision commitment.]
```

## AAAI-Style

Typical posture:

- single compact response;
- prioritize all reviewers' highest-impact concerns;
- do not add URLs if prohibited by the current venue instructions;
- avoid relying on rushed new experiments.

Pattern:

```text
We thank the reviewers for recognizing [X]. We address the main concerns:
R1/W1: ...
R2/W1: ...
```

## NeurIPS / ICLR / OpenReview-Style

Typical posture:

- respond in threads or grouped bullets;
- reviewers may update scores after discussion;
- direct replies to actionable concerns work better than broad persuasion.

Pattern:

```text
Thank you for the question. The key point is [claim].
Evidence: [table/figure/appendix].
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
Response: [answer]
Revision: [section/line change]
```

## Format Decision

Choose format by venue constraints:

- strict global word/character limit: compress across reviewers and prioritize decision risks;
- OpenReview thread: answer each reviewer separately and keep each reply short;
- camera-ready response letter: include exhaustive comment-response pairs;
- internal memo: include paths, raw evidence, and longer reasoning.

