# Prompt Contract

A figure prompt MUST be the concatenation of these blocks, in this order, with no merging:

1. **Base** — universal quality bar (no domain content).
2. **Figure-type layout** — composition language for the chosen type (no domain content).
3. **Style preset** — palette, font, line, icon, background, motion. (No domain content.)
4. **User override** — `--style-notes`, `--font`, `--palette`. (No domain content.)
5. **Brief** — the figure request from the user. THIS is the only place domain content may appear.
6. **Required text** — exact strings that must render verbatim.
7. **Forbid text** — strings that must NOT render.
8. **Avoid block** — generic anti-patterns (watermark, photoreal, etc.).

## Hard separation

A style preset must NEVER contain:

- paper titles, project names, method names, dataset names
- domain nouns ("retrieval", "diffusion", "GRPO", etc.)
- step labels, module names, axis labels

Domain content lives only in user brief and required-text.

## Variables exposed to templates

```
{{figure_request}}    # the user's brief, verbatim
{{figure_title}}      # optional, only if useful
{{figure_type}}       # one of architecture/roadmap/schema/chart/tracks/generic
{{layout_guidance}}   # from figure-type template
{{required_text}}     # bullet list of mandatory strings
{{aspect_ratio}}      # default per type, override allowed
{{avoid}}             # generic + user-provided
{{style_notes}}       # user override
{{palette_block}}     # rendered from palette yaml
{{font_block}}        # rendered from font yaml
```

Anything else is project-specific and must come through the brief.
