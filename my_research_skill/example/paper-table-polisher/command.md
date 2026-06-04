# Command: paper-table-polisher

From `my_research_skill/`:

```bash
python RA-Skill/skills/paper-table-polisher/scripts/table_from_csv.py \
  example/paper-table-polisher/results.csv \
  --type ablation \
  --best-col-mode max \
  --second-best \
  --ours-row 4 \
  --label tab:critic-ablation \
  --caption "Ablation on critic diversity" \
  --note "Higher Accuracy/F1 is better; Cost is shown for reference." \
  --out example/paper-table-polisher/main_table.tex
```
