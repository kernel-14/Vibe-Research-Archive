# Command: paper-figure-imagegen

From `my_research_skill/`:

```powershell
python paper-figure-imagegen/scripts/render_paper_figure.py \
  --prompt-file example/paper-figure-imagegen/prompt.md \
  --figure-type architecture \
  --title "Research Loop" \
  --env-file ../../.env \
  --text "Question" \
  --text "Critique" \
  --out example/paper-figure-imagegen/research_loop.png \
  --prompt-copy example/paper-figure-imagegen/research_loop_prompt.md \
  --size 2048x1152 \
  --quality high
```
