---
name: paper-table-polisher
description: Use when generating, converting, or beautifying LaTeX tables for AI papers. Ships booktabs/siunitx/multirow templates for comparison, ablation, dataset-stats, and case-taxonomy tables, plus a `ra-table-style.sty` with semantic helpers (\\best, \\second, \\ours, \\tabnote). Trigger on "make this a publication table", "把这个表转 LaTeX", "ablation 表", "comparison table", "best 加粗 second-best 下划线".
---

# Paper Table Polisher

Generates investable, no-vertical-line, booktabs-grade LaTeX tables for ANY paper.

## When to Use

- Convert Markdown / CSV table → LaTeX paper-grade table.
- Author a fresh comparison / ablation / dataset-stat / case-taxonomy / human-eval table.
- Apply best/second-best highlighting with consistent semantics.
- Re-style an existing table that uses `\hline`, vertical bars, or `\resizebox` abuse.

## Workflow

1. **Identify the table type**:
   - `comparison` — methods × metrics
   - `ablation` — variants × metrics, with a "Full"/"Ours" anchor
   - `dataset-stat` — datasets × statistics
   - `case-taxonomy` — qualitative categories with examples
   - `human-eval` — judges × dimensions, often Likert-style
2. **Pick the template** from `assets/templates/` matching the type.
3. **Apply `ra-table-style.sty`** (drop into `paper-style/` and `\usepackage{ra-table-style}`).
4. **Use semantic helpers**, not raw `\textbf{}`/`\underline{}`:
   - `\best{0.812}` — best result in a column
   - `\second{0.799}` — second-best
   - `\ours{0.815}` — our row, painted accent
   - `\tabnote{...}` — small caption-aligned footnote under the table
5. **Convert from CSV/Markdown** with `scripts/table_from_csv.py`:
   ```bash
   python scripts/table_from_csv.py results.csv --type comparison \
     --best-col-mode max --second-best --label tab:main --caption "Main Results"
   ```
6. **Width fixes — in this order, never `\resizebox` first**:
   1. Shorten column headers (acronyms with footnote definition).
   2. Drop low-value columns or merge with `\multicolumn`.
   3. Switch to `tabularx` and let one verbose column reflow.
   4. Step the font down to `\small` or `\footnotesize`.
   5. Last resort: `\resizebox{\linewidth}{!}{...}`. Document the reason.

7. **Page-density fixes for small overview tables**:
   - Keep cells as short phrases; do not put paragraph-length purpose
     descriptions inside a table cell.
   - Move dataset totals, construction notes, and partition definitions to the
     caption or surrounding text.
   - For three-to-five-row dataset overview tables, prefer compact `lll`/`lcl`
     columns with local `\scriptsize`, reduced `\arraystretch`, and reduced
     `\tabcolsep` over fixed-width `p{}` paragraph columns.
   - Do not let a small table force a float-only page or a half-empty column;
     compact the table before tuning global float spacing.

## Hard Rules

- No `\hline`. Use `\toprule \midrule \bottomrule`.
- No vertical bars `|`. Use `\cmidrule` or whitespace for grouping.
- Number columns use `S` columns from `siunitx` for alignment.
- Highlighting must encode meaning: best, second, ours, statistically significant. Decoration is forbidden.
- Captions go ABOVE tables. Footnotes use `\tabnote{}` so they stay table-width.
- Small dataset-stat tables should not include a "Total" row if the same total
  can be stated once in the caption.

## Asset Index

```
assets/latex/ra-table-style.sty          # macros + colors
assets/templates/comparison-table.tex
assets/templates/ablation-table.tex
assets/templates/dataset-stat-table.tex
assets/templates/case-taxonomy-table.tex
assets/templates/human-eval-table.tex
references/table-patterns.md             # decision tree per type
references/highlight-semantics.md        # what \best/\second/\ours mean
```

## Sanity Checklist (before commit)

- Compiles with `pdflatex`/`xelatex` without warnings on width.
- No `Overfull \hbox` over 5pt.
- All numbers in a column align on the decimal point.
- Columns grouped with `\cmidrule(lr){...}` where headers span groups.
- Caption stands alone (reader does not need text body to parse the table).
