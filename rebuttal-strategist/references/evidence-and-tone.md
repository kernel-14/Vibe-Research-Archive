# Evidence And Tone Rules

## Evidence Hierarchy

Use this order in final author responses:

1. Paper tables, figures, equations, section text, appendix.
2. Official supplementary material or released artifacts.
3. Existing logs, generated repositories, or reproducible analysis from submitted artifacts.
4. New experiments only when allowed, validated, and necessary.
5. Future work for scope extensions not supported by current evidence.

Internal memos may include local paths. Final rebuttals should usually not include local filesystem paths. Prefer:

```text
Table 2 shows...
Appendix Table 9 reports...
The released generated repositories show...
We will add a compact artifact audit table in the camera-ready version.
```

Avoid:

```text
See E:/.../repo/src/file.py:153
```

## Reviewer-Facing Tone

Use:

- "We thank the reviewer for..."
- "We agree that..."
- "The current results support..."
- "The more precise interpretation is..."
- "We will clarify..."
- "We will add..."
- "This is a scope boundary..."

Avoid:

- "The reviewer is wrong..."
- "This is not our problem..."
- "We do not claim..." repeated across paragraphs
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

## Claim Safety

Before finalizing, check:

- Does each strong claim cite paper evidence or released artifacts?
- Is any limitation repeated more than once?
- Does the response promise only changes we can make?
- Does each paragraph answer one reviewer concern?
- Is the final paragraph a concrete revision commitment, not a generic thank-you?

