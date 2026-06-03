# Highlight Semantics

Highlighting MUST encode meaning. If you cannot point at a rule below, do not apply the highlight.

| Macro | Meaning | Visual |
| --- | --- | --- |
| `\best{x}` | Best (max or min, declared in caption) result in a column. | Bold |
| `\second{x}` | Second-best result in a column. | Underline |
| `\ours{x}` | Result on the row representing the paper's method. | Cell tint with `RAAccent!12` + bold |
| `\sig{x}` | Statistically significant difference vs baseline. | Trailing dagger † (declare in caption) |
| `\tabnote{...}` | Table-width footnote (ALL caveats live here). | Footnotesize, tight spacing |

## Rules

- Best and second are computed PER COLUMN, not per row.
- Multiple `\best` in one column means a tie; mark all of them.
- `\ours` may co-occur with `\best` and/or `\second`.
- Never use color alone to encode meaning; color must come WITH bold/underline so grayscale prints survive.
- Never highlight a row just because it is "ours" if it is not best, second, or significant — that is decoration.

## Caption template

```
\caption{<Statement of what is shown>. \textbf{Bold} = best per column;
\underline{underlined} = second-best; tinted row = our method;
$\dagger$ = statistically significant ($p<0.05$, paired bootstrap, $n=...$).}
```
