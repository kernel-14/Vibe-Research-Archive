# Box Patterns

## Prompt box
- Long natural-language prompts.
- Title strip carries the role (System, User, Generator-Prompt, etc.).
- Always `breakable`. Prompts are often > 1 page.

## Code box
- Source code or structured config.
- Use `minted` when shell-escape is allowed. Otherwise `listings`.
- Keep line numbers OFF unless code is referenced from the body.
- Wrap long lines; never let code fall off the right margin.

## Case box
- Input / model output / annotation triples.
- Three sub-sections inside one box, separated by `\tcblower` or `\par\noindent\rule{...}`.
- Tag the output with model name + sampling settings in the title strip.

## Theorem / Definition box
- Single-paragraph statements.
- Italic title, plain body.
- Do NOT use accent fills here; theory boxes stay quiet.

## When NOT to use a box

- Inline equation set → use `align`, not a box.
- A few lines of code → inline `\texttt{}` or a plain `verbatim` block.
- Single short prompt → just a quoted paragraph.
