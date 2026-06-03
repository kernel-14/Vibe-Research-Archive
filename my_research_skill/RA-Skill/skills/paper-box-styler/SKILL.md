---
name: paper-box-styler
description: Use when adding stylized boxes to paper appendices — code, prompt, case-study, definition, theorem-proof boxes — with consistent palette, breakable across pages, and a shell-escape-free fallback. Trigger on "appendix code box", "prompt box", "case study box", "把这段 prompt 框成漂亮的 box", "definition box".
---

# Paper Box Styler

Generic, generalized version of "appendix prompt/code box" patterns. Built on `tcolorbox`, with `minted` (shell-escape) and `listings` (no shell-escape) paths.

## When to Use

- Long prompts in appendix that must break across pages.
- Code blocks (Python, JSON, LaTeX, shell) with quiet syntax highlighting.
- Case-study boxes (input → model output → annotation).
- Definition / theorem / proof boxes for theory papers.

## Workflow

1. **Pick the box type**:
   - `prompt`   → `assets/templates/prompt-box.tex`
   - `code`     → `assets/templates/code-box.tex` (`minted` and `listings` variants)
   - `case`     → `assets/templates/case-box.tex`
   - `definition` / `theorem` → `assets/templates/theorem-box.tex`
2. **Drop `ra-box-style.sty`** into the paper's style folder. It depends on:
   `tcolorbox`, `xcolor`, `etoolbox`. `minted` is optional and gated.
3. **Choose syntax-highlighting path**:
   - Build allows `-shell-escape` → use `minted` for prompts/code.
   - No shell-escape → use `listings`. Same macros, different rendering.
4. **Use semantic environments**, not raw `tcolorbox`:
   ```latex
   \begin{RAPromptBox}[title={Prompt for Figure Generation}]
   ...
   \end{RAPromptBox}
   ```
5. **Always pass `breakable`-aware boxes** for anything that may exceed half a page.

## Hard Rules

- All colors come from `\RAAccent`/`\RAMuted` defined once in `ra-box-style.sty`. No box defines its own palette inline.
- Default to subtle: thin border, light tint, restrained title.
- Default to grayscale-printable: tints under 15%, never deep saturations.
- Provide BOTH `minted` and `listings` paths; never assume shell-escape.
- Never wrap a `figure*` or `table*` in a tcolorbox; floats and boxes do not nest cleanly.

## Asset Index

```
assets/latex/ra-box-style.sty
assets/templates/code-box.tex          # minted + listings variants
assets/templates/prompt-box.tex
assets/templates/case-box.tex
assets/templates/theorem-box.tex
references/box-patterns.md             # which box for which content
```

## Defaults

| Box | Title strip | Border | Tint | Breakable |
| --- | --- | --- | --- | --- |
| Prompt | Accent fill, white text | thin accent | none | yes |
| Code | Muted strip, white text | thin muted | none | yes |
| Case  | Light tint, accent rule | thin accent | 6% accent | yes |
| Theorem | Title inline italic | thin muted | none | yes |

## Fallback

If the conference template clashes with `tcolorbox`:

- Provide `\RAFallback{true}` flag in `ra-box-style.sty` that switches to `quote`-like environments without color. The same `\begin{RAPromptBox}` keeps working but renders plainer.
