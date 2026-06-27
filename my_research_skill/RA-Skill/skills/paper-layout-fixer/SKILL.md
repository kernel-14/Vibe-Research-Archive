---
name: paper-layout-fixer
description: Use when LaTeX layout misbehaves — overfull/underfull hboxes, floats jumping pages, two-column figure*/table* placement issues, undefined references, duplicate labels, package conflicts. The skill compiles the project, parses the .log into a categorized report, and proposes minimal local fixes. Trigger on "fix the overfull on page 7", "图表跑飞了", "为什么图3 跨到了下一页", "解决 LaTeX 警告", "排版 bug".
---

# Paper Layout Fixer

A diagnose-first skill. NEVER guess at layout fixes — compile, read the log, locate, fix small.

## When to Use

- "Page N has a floating figure on the wrong column."
- "Overfull hbox warning, no idea why."
- "我的 figure* 总是跑到下一页 / appendix."
- "Caption太长压在了图上."
- "References 编号错乱 / undefined."

## Workflow

1. **Confirm scope.** What page / figure / warning class? If unspecified, ask before compiling.
2. **Compile and capture**:
   ```bash
   python scripts/compile_and_parse.py --root paper.tex --engine latexmk
   ```
   Produces `build/paper.log` and `build/layout-report.json`.
3. **Generate the human report**:
   ```bash
   python scripts/latex_log_report.py build/paper.log --format markdown --out build/report.md
   ```
4. **Triage** by category (see `references/layout-playbook.md`):
   - Float placement → `references/float-fixes.md`
   - Width / spacing → `references/space-fixes.md`
   - Labels / refs → in-doc fixes only
   - Package conflict → propose minimal `\usepackage` reorder; do not silently disable hyperref/cleveref/etc.
5. **Inspect rendered pages.** For visual complaints ("too much blank space",
   "figure/table too large", "text overlaps"), compile and render the affected
   pages to images. The log alone will not catch oversized floats, sparse
   pages, or labels that collide inside a plotted figure.
6. **Apply minimal local edits.** Touch only the smallest scope that addresses
   the warning.
7. **Re-compile**, diff before/after, report the residual warnings.

## Visual Layout Heuristics

- Treat `figure*` and `table*` as scarce. Use them for central results or
  genuinely full-width diagrams; convert illustrative examples and small
  motivation charts to single-column floats when they create a float-only page
  or leave the previous page half empty.
- When a page has large blank areas, inspect the next page first. The cause is
  often a queued wide float, not missing prose on the blank page.
- Do not stack multiple wide floats in sequence unless the page is intended to
  be a dense results plate. Move one float earlier, convert one to single
  column, shrink a low-information figure, or move supporting visuals to the
  appendix.
- For data figures, prefer small multiples with short axis labels and numeric
  annotations. Put explanatory prose in the caption instead of large titles or
  full sentences inside the plot.
- For dataset overview tables, keep table cells phrase-like. Put total dataset
  size and partition definitions in the caption or surrounding text instead of
  using a large "purpose" paragraph column.

## Hard Boundaries

- Do not auto-rewrite paragraphs to fix overfull hboxes; suggest the rewrite to the user, do not silently change wording.
- Do not switch document class or template silently. If a conference template fights the fix, surface the conflict to the user and pause.
- Do not `\sloppy` globally to "make warnings go away". Localize with `\begin{sloppypar}` only when needed.
- Never disable warnings with `\hbadness=10000` or similar. That hides bugs.

## Promised Coverage

This skill helps reliably with:

- Overfull / underfull `\hbox`
- Float positioning (`figure`, `figure*`, `table`, `table*`) including two-column edge cases
- Visual page-density problems caused by oversized figures, long captions, or
  float queues
- Caption width and `\caption` line breaking
- Algorithm / listing block spacing
- Undefined references and duplicate labels
- Bibliography / appendix start-page issues

This skill does NOT promise:

- "Make the whole paper look better."
- "Fit content that genuinely doesn't fit without changing prose."

## Output Contract

Every fix run produces:

```
build/
  paper.log
  layout-report.json   # structured findings
  report.md            # human-readable triage
  fixes-applied.md     # what was changed and why
```
