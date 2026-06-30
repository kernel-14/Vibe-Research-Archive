# Table Style Patterns

Distilled from local Word downloads containing LaTeX table code: `table177_tex.docx`, `table178_tex.docx`, `table179_tex.docx`, `table180_tex.docx`, `table181_tex.docx`, `table183_tex.docx`, `table185_tex.docx`, `table186_tex.docx`, `table187_tex.docx`, `table188_tex.docx`, `table189_tex.docx`, `table190_tex.docx`, `table191_tex.docx`, `table192_tex.docx`, `table193_tex.docx`, and `table194_tex.docx`.

## Pattern Inventory

| Pattern | Source examples | Use for | Visual grammar |
| --- | --- | --- | --- |
| `rank-cells` | 183, 192, 193 | Best/second/third per metric | `\tbbest`, `\tbsecond`, `\tbthird` cell backgrounds |
| `pastel-groups` | 177, 178, 190 | Multiple method families or settings | Full-width group bands, family-tinted cells, `\cmidrule` header groups |
| `ours-delta` | 186, 188, 194 | Baseline plus improved method | Light ours row, positive deltas in calm green, negative/violations in red |
| `heatmap` | 185, 191 | Gradual strength across modules/settings | Low/mid/high intensity cells without rank clutter |
| `significance` | 186, 188, 194 | Robustness or statistical comparison | `\tbsig`, `\tbns`, semantic deltas |
| `case-matrix` | 183, 185, 191 | Qualitative cases, feature support, taxonomy | Check/cross/partial marks and rank badges |
| `compact-wide` | 178, 180, 183, 190 | 12+ metrics or many datasets | `\scriptsize`, small `\tabcolsep`, grouped headers, `\resizebox` only after compression |
| `wrap-summary` | 191 | Small side table | `wraptable`, compact venue/model columns, colored aspect header |

## Palette

Use low-saturation fills so the table still reads as a paper table:

- `tbBest`: light red/pink for top-1 or primary winner.
- `tbSecond`: light blue for second-best.
- `tbThird`: pale yellow/orange for third-best.
- `tbOurs`: light orange for an ours/add-on row.
- `tbBase`: very light gray for baselines or random guess.
- `tbGroup`: very light lavender/blue for group bands.
- `tbHeatLow`, `tbHeatMid`, `tbHeatHigh`: blue intensity ramp for heatmap-style score strength.
- `tbGain`: calm green for positive deltas.
- `tbLoss`: muted red for negative deltas or violations.

## Layout Rules

1. Use `@{}...@{}` to remove outer padding on dense tables.
2. Use `\setlength{\tabcolsep}{3pt}` to `5pt` before reaching for `\resizebox`.
3. Use `\renewcommand{\arraystretch}{1.05}` to `1.25`; higher values look poster-like.
4. Use `\makecell{...}` for multi-line headers instead of overlong headers.
5. Use `\multicolumn{...}{c}{...}` plus `\cmidrule(lr){...}` for dataset/metric groups.
6. Use `\rowcolor` for semantic rows and `\cellcolor` for rank/value semantics.
7. Avoid large saturated fills; strong color should appear mainly in delta text.

## Cleanup Pass

When converting rough source:

- Replace raw red/blue rank styling with `\tbbest{...}`, `\tbsecond{...}`, or `\tbthird{...}`.
- Replace raw light-orange ours rows with `\tboursrow`.
- Replace raw green/red delta text with `\tbpos{...}` / `\tbneg{...}`.
- Replace gradual score shading with `\tbheatlow{...}`, `\tbheatmid{...}`, and `\tbheathigh{...}`.
- Replace repeated group labels with `\tbsection{<ncols>}{<label>}` if the table is too wide for `\multirow`.
- Remove decorative double rules unless they separate major table blocks.
