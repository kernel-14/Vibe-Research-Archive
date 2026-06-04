# Skill Examples

每个子目录对应一个 skill，包含最小输入、调用方式和运行结果摘录。

## Index

| Skill | Example |
| --- | --- |
| `topic-mentor` | `topic-mentor/prompt.md` + `topic-mentor/result.md` |
| `brainstorm-search` | `brainstorm-search/prompt.md` + `brainstorm-search/result.md` |
| `diffusion-idea` | `diffusion-idea/prompt.md` + `diffusion-idea/result.md` |
| `paper-figure-studio` | `paper-figure-studio/brief.md` -> `paper-figure-studio/overview.png` |
| `paper-table-polisher` | `paper-table-polisher/results.csv` -> `paper-table-polisher/main_table.tex` |
| `paper-layout-fixer` | `paper-layout-fixer/paper.tex` -> `paper-layout-fixer/build/report.md` |
| `paper-box-styler` | `paper-box-styler/sample.tex` -> `paper-box-styler/build/sample.pdf` |
| `paper-figure-imagegen` | `paper-figure-imagegen/prompt.md` -> `paper-figure-imagegen/research_loop.png` |

图像类示例已经用 `gpt-image-2` 真实生成 PNG；凭证从 env / `.env` 读取，不写入 prompt 或结果文件。
