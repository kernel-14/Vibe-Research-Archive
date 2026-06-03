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
