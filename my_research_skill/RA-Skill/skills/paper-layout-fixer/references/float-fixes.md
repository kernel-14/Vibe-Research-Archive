# Float Placement Playbook

## Symptom: figure jumps to a much later page

1. Check the float specifier. If it is `[h]` only, LaTeX often defers. Use `[tbp]` (top, bottom, page) and let the algorithm decide.
2. For two-column papers, `figure*` only floats to the top of a page. If you wrote `[h]` it is silently ignored.
3. Check `\textfloatsep`, `\floatsep`, `\intextsep` — overrides from a conference template are common.
4. If text is sparse near the float, force placement only with `[!htbp]` (note the `!`), not with `\FloatBarrier` everywhere.

## Symptom: two-column figure spans wrong column

- `figure` = single column. `figure*` = full text width.
- Mixing them on the same page is fragile. Prefer one per page when possible.
- `\caption` width follows the float environment; if caption text wraps oddly, check that you are inside the right env.

## Symptom: previous page has large blank space and the next page is mostly floats

This usually means wide floats are queued. Fix the queue before rewriting prose:

1. Identify the first `figure*` or `table*` after the blank area.
2. If it is an illustrative example, thumbnail, or low-information motivation
   chart, convert it to a single-column `figure`/`table` and set
   `\includegraphics[width=\linewidth]{...}`.
3. Keep the main quantitative table or central method figure wide; shrink or
   move supporting visuals instead.
4. Avoid placing a full-width example figure immediately before a full-width
   main-result table. Put the example in one column, or move it to appendix if
   it is not essential for the main argument.
5. Re-render the affected pages. The fix is successful only if the previous page
   gains body text and the next page is no longer a sparse float page.

## Symptom: figure text overlaps or dominates the panel

- Remove nonessential in-plot prose first. Captions should carry explanation.
- Prefer short panel headers such as "Prior", "Audit", "Waste" over full
  sentence titles.
- Put long annotations such as resend ratios, caveats, and mechanism
  descriptions in the caption or an appendix table.
- If y-axis labels collide across panels, remove low-value labels or increase
  panel spacing; do not simply scale the entire figure down.

## Symptom: caption appears below figure but should be above (table) or vice-versa

- Order in source: `\caption{}` BEFORE `\includegraphics` for above-figure captions when journal mandates it.
- For tables, `\caption{}` must be ABOVE `\begin{tabular}` per most style guides.

## Symptom: figure pushed into the appendix

- Caused by remaining float queue that never drains. Insert `\clearpage` (not `\newpage`) at the section break, or use `\afterpage{\clearpage}` from `afterpage` to drain after the current page completes.
- If using `placeins`, `\FloatBarrier` is the localized version.

## Last-resort knobs (use sparingly, document why)

- `\setcounter{topnumber}{3}`, `\setcounter{totalnumber}{4}`
- `\renewcommand{\topfraction}{0.95}`
- `\renewcommand{\textfraction}{0.05}`

These weaken LaTeX's aesthetic guards. Only set them in `paper-style/` for the whole project, never inline.
