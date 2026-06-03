# Workflow: paper-figure-studio

1. **Brief intake**
   - Required: figure type, output path, required in-figure text.
   - Optional: palette, font, style preset, forbid-text, reference image.
   - If the user is vague, ask one focused clarifying question, do NOT invent a topic.

2. **Style/Content split**
   - Style data flows from preset + flags.
   - Content data flows ONLY from the user's brief.
   - Never let the preset inject a paper title, method name, dataset name, or domain noun.

3. **Compose**
   - Base = `assets/templates/figure-base.md`
   - Type = `assets/templates/<figure-type>.md`
   - Style = `assets/styles/<style>.yaml` (rendered into prose)
   - Override = user `style-notes` / `font` / `palette`
   - Required text / forbid text appended verbatim.

4. **Render**
   - Call `scripts/render_figure.py` with the composed prompt and resolved knobs.
   - Always pass `--save-prompt` so the final composed prompt lives next to the image.

5. **Review**
   - Run the checklist in `references/workflow.md` §Review.
   - Iterate by changing ONE knob at a time. Document the change in the saved prompt.

6. **Reproducibility**
   - The image and its `*_prompt.md` must be enough to regenerate.
   - Never include credentials, base URL, or model id in the saved prompt body.

## Review Checklist

- All required text present and spelled correctly.
- No overlapping labels; line spacing comfortable.
- Arrows are thin and purposeful; no tangled connectors.
- Palette consistent across figures of the same paper.
- Reads correctly when shrunk to single-column width.
- No watermarks, no decorative noise, no photoreal artifacts.
- Saved prompt file has zero credentials.
