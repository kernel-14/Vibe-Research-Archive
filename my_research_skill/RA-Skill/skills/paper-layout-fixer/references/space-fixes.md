# Width and Spacing Fixes

## Overfull `\hbox` in body text

Order of remedies, cheapest first:

1. Rewrite the offending word/phrase. A 6pt excess usually disappears with a single shorter synonym.
2. `\url{}` or `\href{}{}` for long URLs/identifiers; they get to break.
3. Wrap the paragraph in `\begin{sloppypar} ... \end{sloppypar}`. Local relaxation only.
4. `\hyphenation{ex-am-ple-word}` for one stubborn token used many times.
5. Last resort: `\sloppy` for a section. Never globally.

## Overfull `\hbox` in a table

1. Shorten column header acronyms; define expansion in caption or footnote.
2. Drop a column or merge with `\multicolumn`.
3. Switch to `tabularx` and let one verbose column reflow.
4. `\small` / `\footnotesize` table-wide.
5. Last resort: `\resizebox{\linewidth}{!}{...}`. Document why.

## Table visually too large despite fitting the width

1. Ask whether the table is carrying statistics or prose. If prose, move the
   prose to the caption or surrounding paragraph and keep cells as short
   phrases.
2. Remove total rows when the same total can live in the caption.
3. Use `\scriptsize` only for compact overview tables; avoid it for main result
   tables unless necessary.
4. Reduce `\arraystretch` slightly (for example `0.94`) and `\tabcolsep`
   locally. Do not change global table spacing.
5. If a table has only three to five rows, avoid a wide paragraph column. A
   compact `lll` or `lcl` schema often reads better than fixed-width `p{}`
   columns.

## Caption too long

- Use `\caption[short]{long}` so the LOF entry stays compact.
- Break long captions with `\\` between sentences only when justified — many conferences prefer no manual breaks.

## Algorithm / listing block touches body text

- Add `\vspace{2pt}` before `\begin{algorithm}` / `\begin{lstlisting}`.
- Or wrap with `\begin{tcolorbox}[boxrule=0pt, top=2pt, bottom=2pt]` from `paper-box-styler`.

## Bibliography / appendix start at wrong page

- Use `\clearpage` not `\newpage` before `\bibliography{}` and before `\appendix`.
- For two-column with `\onecolumn` switch, balance with `multicol` or `flushend`.
- For `acl_natbib` and similar: load `cleveref` AFTER `hyperref`; never before.

## Spacing around floats

```
\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
\setlength{\floatsep}{6pt plus 2pt minus 2pt}
\setlength{\intextsep}{6pt plus 2pt minus 2pt}
```

Set in `paper-style/`, never inline.

## Sparse pages caused by low-information figures

- Shrinking `\includegraphics` width can help, but it does not solve a float
  queue. If a full-width figure is visually sparse, first decide whether it
  should be single-column, moved later, or moved to the appendix.
- For plotted motivation figures, use fewer in-plot labels before reducing the
  whole figure. Scaling a crowded plot makes it harder to read; simplifying the
  plot makes it smaller and clearer.
