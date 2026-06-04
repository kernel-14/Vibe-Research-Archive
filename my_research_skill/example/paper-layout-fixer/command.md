# Command: paper-layout-fixer

From `example/paper-layout-fixer/`:

```bash
python ../../RA-Skill/skills/paper-layout-fixer/scripts/compile_and_parse.py \
  --root paper.tex \
  --engine pdflatex \
  --build-dir build

python ../../RA-Skill/skills/paper-layout-fixer/scripts/latex_log_report.py \
  build/paper.log \
  --format markdown \
  --out build/report.md
```
