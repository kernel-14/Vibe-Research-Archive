---
name: table-beautifier
description: "Beautify LaTeX tables for AI papers using distilled table patterns: pastel row/cell highlights, rank coloring, heatmap intensity cells, colored ours rows, delta subscripts, significance marks, grouped headers, dense wide-table layouts, wraptable summary tables, and a compiled PDF style gallery. Use when asked to polish a TeX table, create publication-ready table templates, convert rough tabular code into a cleaner style, or choose a table visual style inspired by downloaded LaTeX table examples."
---

# Table Beautifier

Create polished LaTeX paper tables using style patterns distilled from downloaded local Word examples containing LaTeX table code.

## Workflow

1. Identify the table role:
   - `comparison`: methods x metrics, often grouped by dataset or benchmark.
   - `ablation`: variants grouped by modules, settings, or pruning rates.
   - `leaderboard`: many metrics, compact columns, stage/backbone metadata.
   - `ranking`: best/second/third visualized with pastel cells.
   - `heatmap`: relative score strength encoded by low/mid/high intensity fills.
   - `delta`: baseline row plus colored improvement/loss annotations.
   - `significance`: stars, neutral marks, and explicit deltas.
   - `case-matrix`: qualitative checks, partial marks, and rank badges.
   - `summary`: compact wraptable or single-column table.
2. Pick a visual pattern from `references/style-patterns.md`.
3. Copy `assets/latex/table-style.sty` into the paper style folder or keep it next to the target `.tex`.
4. Start from the closest file in `assets/templates/`.
5. Use semantic macros instead of ad hoc styling:
   - `\tbbest{...}`, `\tbsecond{...}`, `\tbthird{...}`
   - `\tbheatlow{...}`, `\tbheatmid{...}`, `\tbheathigh{...}`
   - `\tboursrow`, `\tbbaserow`, `\tbsection{n}{label}`
   - `\tbpos{...}`, `\tbneg{...}`, `\tbzero{...}`, `\tbsig`, `\tbns`
   - `\tbcheck`, `\tbxmark`, `\tbpartial`, `\tbrankbadge{color}{text}`
6. Keep captions above tables and make the first sentence state what is compared.
7. Prefer `booktabs` rules. Preserve vertical separators only when a very wide table needs explicit family boundaries.

## Style Selection

- Use `rank-cells` when every metric column needs best/second/third highlighting.
- Use `pastel-groups` for method families such as zero-shot, same-dataset, cross-dataset, MLLM families, or planner categories.
- Use `ours-delta` when the story is "baseline + our method improves it"; put the delta directly after the value.
- Use `heatmap` when absolute rank is less important than gradual strength across modules or settings.
- Use `significance` when reported improvements need statistical or robustness caveats.
- Use `case-matrix` for qualitative examples, feature support, or taxonomy rows.
- Use `compact-wide` for 12+ metric columns; reduce `\tabcolsep` before using `\resizebox`.
- Use `wrap-summary` for a side table that supports a nearby figure or paragraph.

## Hard Rules

- Do not color for decoration. Every color must encode group, rank, ours, baseline, intensity, positive delta, negative delta, warning, or qualitative status.
- Do not use saturated red/blue blocks for large areas; use pastel backgrounds and reserve strong colors for text deltas.
- Do not bold every number in an ours row. Bold only actual best values or the main result column.
- If `\resizebox` is needed, first try `\scriptsize`, `\setlength{\tabcolsep}{...}`, shorter headers, and `makecell`.
- Align numeric columns consistently. For final camera-ready tables, consider `siunitx` if the table is not too complex.
- Use `\cmidrule(lr){...}` under grouped headers.
- For repeated group labels, use `\multirow` or a full-width pastel group band.

## Resources

- `assets/latex/table-style.sty`: reusable macros and pastel colors.
- `assets/templates/rank-cells-table.tex`: best/second/third cell highlighting.
- `assets/templates/ours-delta-table.tex`: baseline + ours rows with positive deltas.
- `assets/templates/pastel-group-table.tex`: group-band and row-family styles.
- `assets/templates/heatmap-table.tex`: low/mid/high intensity score cells.
- `assets/templates/significance-table.tex`: significance marks and robust deltas.
- `assets/templates/case-matrix-table.tex`: qualitative status matrix with badges.
- `assets/templates/wrap-summary-table.tex`: compact wraptable summary style.
- `assets/gallery/table-gallery.tex`: compilable gallery showing supported styles.
- `references/style-patterns.md`: style decisions and mapping from source examples.

## Demo

Compile the gallery from the skill folder:

```bash
pdflatex -interaction=nonstopmode -halt-on-error assets/gallery/table-gallery.tex
```

The output PDF demonstrates the supported style families.

