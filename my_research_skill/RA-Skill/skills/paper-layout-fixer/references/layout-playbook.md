# Layout Playbook — Categorize → Localize → Fix

## Categories produced by `latex_log_report.py`

| Category | Trigger pattern in log |
| --- | --- |
| `overfull-hbox` | `Overfull \hbox (... too wide)` |
| `underfull-hbox` | `Underfull \hbox` |
| `overfull-vbox` | `Overfull \vbox` |
| `float-too-large` | `Float too large for page by ...` |
| `undefined-ref` | `LaTeX Warning: Reference '...' on page ... undefined` |
| `multiply-defined-label` | `LaTeX Warning: Label '...' multiply defined` |
| `missing-citation` | `LaTeX Warning: Citation '...' on page ... undefined` |
| `package-conflict` | `Package ... clash` / `Option clash` |
| `font-shape` | `LaTeX Font Warning: ...` |
| `cleveref-mismatch` | `Package cleveref Warning: ...` |

## Fix order

1. Cheap structural fixes first: missing citations, undefined refs (recompile + bibtex).
2. Float placement (`references/float-fixes.md`).
3. Width / spacing (`references/space-fixes.md`).
4. Package conflicts last; surface to user before changing `\usepackage` order.

## When NOT to "fix"

- Underfull hbox with badness < 5000 in body text is usually fine.
- Overfull `\hbox` of a few points in a long URL needs `\url{}` or `\sloppy` ONLY around that paragraph (`\begin{sloppypar} ... \end{sloppypar}`), not globally.
- Single-page float drift from compile non-determinism resolves on a third pass; check before "fixing".

## Reporting format

Each finding in `report.md`:

```
### overfull-hbox @ paper.tex:412 (page 7)
Severity: medium
Excess: 12.4pt
Context: "The proposed method ... evaluation harness." (line 412)
Suggested fix: rewrite line 412 to drop "the evaluation"; or wrap with sloppypar.
```

No bulk fixes without itemized findings.
