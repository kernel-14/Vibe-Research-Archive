# Table Patterns

Decision tree per table type.

## comparison
Rows = methods. Columns = metrics. One row is "Ours".
- `S[table-format=2.2]` columns for metrics.
- `\cmidrule` to group metric families.
- Mark `\best`, `\second`, `\ours`.

## ablation
Rows = variants of the same method (Full → minus-X, plus-Y). Often ends with "Full" anchor.
- Use a tinted `\ours` for the Full row.
- Order by descending performance for the headline metric.
- Provide a "$\Delta$" column or a footnote with deltas.

## dataset-stat
Rows = datasets. Columns = #train, #dev, #test, avg-len, vocab, splits.
- Right-align ints with `S[group-separator={,}]`.
- Footnote citations per dataset (not in row labels — keep labels short).

## case-taxonomy
Rows = categories. Columns = description, example, count, %.
- `tabularx` with `X` column for example text.
- Use `\seqsplit` or manual breaks for long examples.
- Counts and % share a column with `(n=12, 4%)` notation when space is tight.

## human-eval
Rows = systems / models. Columns = evaluation dimensions (Helpful, Honest, etc.).
- Likert means with `±std` in a smaller secondary cell or footnote.
- Mark `\best` per dimension.
- Disclose annotator count and IAA (κ or α) in `\tabnote`.

## When in doubt

- Default to `comparison` template; specialize from there.
- Never duplicate the same data in two formats. Pick one; reference it.
- If a table has more than ~10 rows × 10 cols, split into two tables or move to appendix.
