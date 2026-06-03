---
name: paper-figure-studio
description: Use when generating AI-conference-style paper figures (architecture, roadmap, schema, chart, method-tracks, generic) with image-generation APIs. The skill ships layered prompt templates, swappable style presets (palette + font + layout language), and a render script that reads credentials from env/.env only. Trigger on requests like "draw a method overview figure", "generate an architecture diagram", "我想画一张技术路线图", "用 X 风格画一张论文图".
---

# Paper Figure Studio

Generic, generalized successor of `paper-figure-imagegen`. Produces consistent, publication-grade figures for ANY paper or topic.

**Hard rules:**

- No project / paper / method names are baked into this skill. Domain content comes ONLY from the user's brief.
- No credentials are baked into the script. Always resolved from env / `.env` / explicit flags.
- Style ≠ content. Style preset only governs palette, font, line/icon/background language. The user's brief governs labels, structure, and meaning.

## When to Use

- "画一张方法总览图 / architecture / overview / pipeline"
- "Generate a roadmap / schema / chart / cross-track method figure"
- "用 minimal / colorful / grayscale / claymorphism / vivid 风格再画一张"
- "Use Comic Sans MS for the labels and a vivid academic palette"

## Workflow

1. **Confirm the figure brief.** If anything is missing, ask the user for: figure-type, output path, mandatory in-figure text, palette/font/style preference, anything to forbid.
2. **Resolve config layering** in this priority (highest wins):
   ```
   CLI flags > user-supplied prompt file > project-local style.yaml
     > preset (assets/styles/<preset>.yaml) > built-in default
   ```
3. **Read the relevant references**, lazy-loading only what the figure needs:
   - `references/workflow.md` for end-to-end checklist
   - `references/prompt-contract.md` for the layered prompt schema
   - `references/figure-types.md` for the matching layout language
   - `references/style-presets.md` for the style preset registry
4. **Compose the prompt** by stacking: `figure-base` ⊕ `<figure-type>` template ⊕ `<style>` preset ⊕ user override ⊕ required-text / forbid-text.
5. **Run the renderer**:
   ```bash
   python scripts/render_figure.py \
     --prompt-file fig/brief.md \
     --figure-type architecture \
     --style colorful-method \
     --palette vivid-academic \
     --font "Comic Sans MS" \
     --out fig/overview.png \
     --save-prompt fig/overview_prompt.md
   ```
6. **Inspect** label correctness, alignment, arrow clarity, blank space, and whether the figure explains the method without the caption. Iterate one knob at a time.
7. **Save the rendered prompt** next to the image for reproducibility. Never paste credentials.

## Built-in Knobs

| Flag | Purpose |
| --- | --- |
| `--figure-type` | architecture / roadmap / schema / chart / tracks / generic |
| `--style` | preset key from `assets/styles/*.yaml` |
| `--palette` | preset key from `../../shared/palettes.yaml` |
| `--font` | label font, e.g. `Comic Sans MS`, `Inter`, `Source Sans` |
| `--required-text` / `--text-file` | exact strings that MUST appear in the image |
| `--forbid-text` | strings the model must NOT render |
| `--reference-image` | optional style anchor (when supported by provider) |
| `--dry-run` | print resolved config + composed prompt; never echo secrets |

## Built-in Style Presets

See `assets/styles/`:

- `default.yaml` — the universal fallback (clean, neutral, conference-safe)
- `minimal-academic.yaml` — tight, grayscale-friendly, camera-ready
- `colorful-method.yaml` — vivid indigo/teal/coral, dense but disciplined
- `grayscale-camera-ready.yaml` — pure B/W, print-safe

Add a new preset by dropping a YAML file in `assets/styles/` with the same schema (palette, font, line, icon, background, motion=none).

## Reference Index

- `references/workflow.md` — full step-by-step checklist
- `references/prompt-contract.md` — required prompt schema (style vs content separation)
- `references/figure-types.md` — layout language per figure-type
- `references/style-presets.md` — what each preset is for and when to pick it

Load only the references you need. `SKILL.md` stays a navigator.
