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
