---
name: paper-figure-imagegen
description: Use when creating AI-conference-style paper figures with Codex and gpt-image-2, especially reusable colorful method diagrams. The skill ships with a prompt template and a render script; credentials are loaded from environment variables or a local `.env` file at run time.
---

# Paper Figure Imagegen

Use this skill when the user wants Codex to generate a paper figure or a consistent family of paper illustrations through `gpt-image-2`, with a reusable template and repo-local output files.

## Workflow

1. Understand the paper/repo context and decide the figure role: architecture, schema, chart, method-line/coupling, or generic explanatory illustration.
2. Read `references/template-prompt.md` when using the default style. Keep exact in-figure text short and explicit.
3. Compose a focused figure brief. Preserve the user's domain terms verbatim, but remove ambiguous shorthand unless the user explicitly requires it.
4. Generate with `scripts/render_paper_figure.py`. The script does NOT carry baked-in credentials — supply them through `OPENAI_API_KEY` / `OPENAI_BASE_URL` env vars, a project `.env` file, or explicit `--api-key` / `--base-url` flags.
5. Inspect the output for label readability, text correctness, line thickness, arrow clutter, spacing, and whether the visual explains the method.
6. Iterate with one targeted prompt change at a time, saving each final prompt next to the image for reproducibility.

## Credential Handling

- This skill ships with **no hardcoded provider URL or API key**. Always supply them at run time.
- Recommended: place `OPENAI_API_KEY` and `OPENAI_BASE_URL` in a project-local `.env` file that is gitignored.
- Never paste credentials into chat, prompt files, LaTeX sources, or generated documentation.
- `--dry-run` reports only whether credentials were resolved and from which source class (e.g. `env:OPENAI_API_KEY`, `file:OPENAI_API_KEY`); it does not echo the secret value.

## Environment Resolution

The script resolves settings in this order:

1. Explicit CLI flags such as `--api-key`, `--base-url`, `--model`, or `--env-file`
2. Terminal environment variables such as `OPENAI_API_KEY`, `OPENAI_BASE_URL`, or `PAPER_FIGURE_IMAGEGEN_MODEL`
3. The current directory `.env` file
4. Built-in defaults for non-secret fields only (e.g. model name `gpt-image-2`); URL and key have no built-in default

Use `PAPER_FIGURE_IMAGEGEN_ENV_FILE` to point at a different `.env` file if needed.

## Default Command

From the project root:

```bash
python .codex/skills/paper-figure-imagegen/scripts/render_paper_figure.py \
  --prompt "Draw a dense architecture figure for a research workflow: prepare context, generate artifacts, validate outputs, and report results." \
  --figure-type architecture \
  --title "Research Workflow Overview" \
  --out fig/architecture.png \
  --size 2048x1152 \
  --quality high
```

If the script reports `Missing API key`, populate `.env` or export `OPENAI_API_KEY` (and `OPENAI_BASE_URL` when using a non-default endpoint) before re-running.

## Style Contract

Use this style unless the user asks otherwise:

- Natural, human-edited AI conference figure, not a generic AI-art poster.
- Rich but controlled palette: indigo, cobalt, teal, coral, emerald, amber, lavender, and clean neutrals.
- Comic Sans MS for labels, with normal proportions, comfortable line height, and readable spacing.
- Functional flat icons: robot, document, search, link, blueprint, code file, checklist, container, wrench, checkmark.
- Dense but readable composition; content should fill the canvas without feeling cramped.
- Thin tidy connectors; avoid thick, tangled arrows.
- No numbered stage badges unless the user explicitly asks.
- Do not use unexplained abbreviations.

## Review Checklist

Before finalizing, verify:

- All required text appears correctly and is readable.
- No text overlaps or gets squeezed inside labels/cards.
- Arrows are thin and purposeful.
- The figure can be understood without reading the prompt.
- The saved prompt file does not contain credentials.
- Outputs are saved under the project, usually `fig/`.
