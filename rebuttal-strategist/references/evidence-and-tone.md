# Evidence And Tone Rules

## Evidence Hierarchy

Use this order in final author responses:

1. Paper tables, figures, equations, section text, appendix.
2. Official supplementary material or released artifacts.
3. Existing logs, generated repositories, code cases, or reproducible analysis from submitted artifacts.
4. New experiments only when allowed, validated, and necessary.
5. Future work for scope extensions not supported by current evidence.

Internal memos may include local paths. Final rebuttals should usually use paper anchors, artifact names, repo-relative paths, or short snippets instead of machine-local absolute paths.

Prefer:

```text
Table 2 shows...
Appendix Table 9 reports...
In the released artifacts, case X implements the same formula through a refactored helper, while case Y is a genuine mismatch.
We will add a compact artifact audit table in the camera-ready version.
```

Avoid:

```text
See E:/.../repo/src/file.py:153
```

## Direct-Answer Rule

Let the reviewer speak first, then answer directly.

Pattern:

```text
Concern: "How does the judge handle refactored but equivalent code?"
Response: It can handle some refactorings when the SAU evidence is explicit, but we agree static judging can still produce false negatives in harder equivalence cases. In our audit, ...
```

If asked yes/no, start with yes/no or a precise equivalent. Do not begin with background that forces the reviewer or AC to infer the answer.

## AC Self-Containment Rule

Assume the AC reads only the reviews and the rebuttal. Reintroduce:

- the paper's core contribution in one or two sentences;
- acronyms and task setup needed for the answer;
- what a table, metric, or case demonstrates;
- why the evidence resolves the concern.

Do not require the AC to connect unstated dots.

## Distilled Writing Rules

- Start positive: briefly mention strengths reviewers recognized.
- In reviewer-specific final responses, speak directly to the reviewer: "Thank you for your...", "As you pointed out...", "Your suggestion helps us clarify...".
- Preserve reviewer order by default; consolidate only under strict limits or shared concerns.
- Quote or label the concern before responding.
- Answer the direct question first, then provide context.
- Respond to the reviewer's intent, not only the surface wording.
- Use emphasis through sentence structure, not aggressive formatting.
- If reviewers missed a central point, set the stage in a concise recap.
- Keep the response self-contained.
- Get credit for details already in the paper by citing and restating them.
- Use data, statistics, and concrete cases before intuitive argument.
- Preserve concrete data tables and representative cases by default. When trimming, shorten prose and case-selection explanations before deleting evidence.
- Make tables read like rebuttal evidence, not internal notes. Use audience-facing column names and explain what each table resolves.
- Do not only promise; provide the explanation or evidence in the rebuttal.
- Be receptive and reasonable when the reviewer is right.
- Be transparent about constraints, venue rules, or compute limits.
- Correct objective errors clearly, without attacking the reviewer.
- Thank reviewers for constructive effort.
- Remember that rebuttal is both scientific communication and human interaction.

## Reviewer-Facing Tone

Use:

- "Thank you for your careful review and for recognizing..."
- "As you pointed out..."
- "Your suggestion helps us clarify..."
- "We agree that..."
- "The current results support..."
- "The more precise interpretation is..."
- "We will clarify..."
- "We will add..."
- "This is a scope boundary..."

Avoid:

- detached final-response phrasing such as "the reviewer says..." when replying to one reviewer;
- internal-note table columns such as "why relevant to the reviewer concern";
- "The reviewer is wrong..."
- "This is not our problem..."
- repeated "We do not claim..."
- "Obviously..."
- "It is unfair..."
- "Unfortunately..."

## Anti-Defensive Rewrite Patterns

Defensive:

```text
We do not claim the method works for every domain.
```

Stronger:

```text
The evaluation focuses on ML/AI reproduction; broader scientific domains are a natural next evaluation target.
```

Defensive:

```text
Although Gemini is much worse, this does not mean our scaffold is bad.
```

Stronger:

```text
The Gemini ablations isolate the scaffold contribution: the full contract improves over both channel removals under the same backbone.
```

Defensive:

```text
We are sorry the paper did not discuss this enough.
```

Stronger:

```text
We will add a dedicated discussion of this boundary in the camera-ready version.
```

Notebook-like:

```text
| Category | Examples | Why relevant to R2's concern |
```

Reviewer-facing:

```text
| Area covered in the benchmark | Representative tasks | Reproduction capabilities tested |
```

Detached:

```text
The reviewer asks whether PaperBench covers multimodal tasks.
```

Reviewer-facing:

```text
Thank you for raising the question of generalization beyond the evaluated setting. PaperBench Code-Dev spans multiple AI/ML subfields, including vision-related and RL tasks.
```

## Claim Safety Checklist

Before finalizing, check:

- Does each strong claim cite paper evidence, released artifacts, or a reproducible analysis?
- Does each code case explain what it proves, rather than just displaying a snippet?
- Is any limitation repeated more than once?
- Does the response promise only changes we can make?
- Does each paragraph answer one reviewer concern?
- Is the final paragraph a concrete revision commitment, not a generic thank-you?
