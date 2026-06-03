# RA-Skill 调研与实现方案

## 结论

这个工作可以做，而且更适合做成一组论文生产力 skills，而不是把所有能力塞进一个巨型 skill。推荐拆成四个独立 skill，加一个共享资源层：

1. `paper-figure-studio`: 论文图生成与风格控制。
2. `paper-table-polisher`: LaTeX 表格美化与模板化。
3. `paper-layout-fixer`: LaTeX 智能排版诊断与修复。
4. `paper-box-styler`: 附录代码框、prompt 框、case study 框等样式组件。
5. `shared/`: 共用配色、字体、LaTeX style 文件、prompt 片段、编译脚本。

这样拆的原因很直接：绘图调用图像 API，表格主要是 LaTeX 模板和数据结构，排版需要编译日志诊断，代码框/prompt 框是可复用宏包组件。四者的输入、失败模式、验证方式都不同，拆开后更容易触发正确 skill，也更容易迭代。

## 交互形态

主入口应该是 Codex / Claude Code 的 skill 调用，而不是要求用户手动运行 CLI。

用户理想交互应当是：

```text
用 paper-figure-studio 帮我画一张方法总览图，风格用 colorful-method，字体用 Comic Sans MS，输出到 fig/overview.png。

用 paper-table-polisher 把这个 markdown 表格改成 ACL 风格 LaTeX 表格，best 加粗，second-best 下划线。

用 paper-layout-fixer 看一下 paper.tex 为什么第 7 页图表跑飞了。
```

然后由 Codex / Claude Code 做这些事：

1. 读取 skill 的 `SKILL.md` 判断工作流。
2. 按需读取 `references/` 中的风格、模板、排版规则。
3. 必要时调用 `scripts/` 里的脚本生成图片、转换表格、编译 LaTeX、解析日志。
4. 把结果写回项目文件，并向用户汇报生成了什么、改了什么、还需要人工确认什么。

CLI 脚本应该只是 skill 的内部工具和可选接口：

- 对 Codex/CC：脚本提供稳定、可重复的执行能力，避免每次临时重写 API 调用或 LaTeX log parser。
- 对用户：如果用户想脱离 agent 批量生成图表，也可以直接运行 CLI。
- 对调试：CLI 能提供 `--dry-run`、`--save-prompt`、`--report` 等可检查输出。

所以文档里的脚本设计不表示用户必须手动运行命令。更准确的架构是：自然语言请求触发 skill，skill 决定是否调用脚本，脚本只是实现细节。

## 依据

- 本地 Codex skill 规范建议一个 skill 至少包含 `SKILL.md`，可选 `agents/openai.yaml`、`scripts/`、`references/`、`assets/`。`SKILL.md` 应保持精简，把长模板、示例、配置放进 references/assets，按需加载。
- OpenAI 图像文档显示，当前图像生成可走 Image API 或 Responses API；单次生成适合 Image API，多轮编辑和引用图像适合 Responses API。官方当前推荐 GPT Image 系列，`gpt-image-1.5` 是更先进的图像模型，输出可配置 size、quality、format、background。来源：https://platform.openai.com/docs/guides/image-generation
- LaTeX 表格建议基于 `booktabs` 做出版质量横线与间距，基于 `siunitx` 做数值列对齐。来源：https://tug.ctan.org/macros/latex/contrib/booktabs/booktabs.pdf 和 https://mirrors.ctan.org/macros/latex/contrib/siunitx/siunitx.pdf
- 代码高亮和 prompt/code 框建议基于 `minted` 或 `listings`，如果允许 shell escape，`minted` 质量更好；否则用 `listings` 兜底。来源：https://ctan.org/pkg/minted 和 https://www.overleaf.com/learn/latex/Code_Highlighting_with_minted
- 样式化盒子建议基于 `tcolorbox`，它支持 breakable boxes、listings/minted 集成、skins、poster/raster 等模块。来源：https://www.ctan.org/tex-archive/macros/latex/contrib/tcolorbox

## 推荐目录结构

```text
RA-Skill/
  proposal.md
  research.md
  skills/
    paper-figure-studio/
      SKILL.md
      agents/openai.yaml
      scripts/render_figure.py
      scripts/merge_style.py
      references/workflow.md
      references/prompt-contract.md
      references/figure-types.md
      references/style-presets.md
      assets/styles/default.yaml
      assets/styles/minimal-academic.yaml
      assets/styles/colorful-method.yaml
      assets/styles/grayscale-camera-ready.yaml
      assets/templates/figure-base.md
      assets/templates/architecture.md
      assets/templates/roadmap.md
      assets/templates/schema.md
    paper-table-polisher/
      SKILL.md
      agents/openai.yaml
      scripts/table_from_csv.py
      references/table-patterns.md
      assets/latex/ra-table-style.sty
      assets/templates/ablation-table.tex
      assets/templates/comparison-table.tex
      assets/templates/stat-table.tex
    paper-layout-fixer/
      SKILL.md
      agents/openai.yaml
      scripts/compile_and_parse.py
      scripts/latex_log_report.py
      references/layout-playbook.md
      references/float-fixes.md
      references/space-fixes.md
    paper-box-styler/
      SKILL.md
      agents/openai.yaml
      references/box-patterns.md
      assets/latex/ra-box-style.sty
      assets/templates/code-box.tex
      assets/templates/prompt-box.tex
      assets/templates/case-box.tex
  shared/
    palettes.yaml
    fonts.yaml
    latex/
      ra-colors.sty
      ra-common.sty
```

## Skill 1: `paper-figure-studio`

目标：把当前 `.codex/paper-figure-imagegen` 升级为通用论文图 skill，支持架构图、技术路线图、schema 图、方法对比图、流程图、附录示意图。

核心改造：

- 不硬编码任何项目名、方法名、论文术语、固定轨道、固定模块。
- API key 和 base URL 只从运行参数、环境变量、`.env` 读取，不写进脚本。
- 模型默认建议改成可配置：`PAPER_FIGURE_MODEL`，默认值可设为当前官方推荐的 GPT Image 模型。
- 风格系统用 YAML 表达，而不是散落在 prompt 中。
- prompt 采用分层合成：base template + figure-type template + style preset + user override + required text。

建议的配置优先级：

```text
运行参数 > 用户 prompt 文件 > 项目 style.yaml > 预设 style yaml > 内置默认
```

脚本接口示例。正常情况下由 Codex/CC 根据用户请求调用；用户也可以手动运行作为可选路径：

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

关键设计点：

- `--style` 控制整体视觉语言。
- `--palette` 控制颜色系统。
- `--font` 控制字体。
- `--required-text` 或 `--text-file` 显式列出必须出现在图中的文字。
- `--forbid-text` 显式禁止模型乱写某些词。
- `--reference-image` 后续可支持已有图风格迁移。
- `--dry-run` 只输出 prompt 和配置来源，不输出 key/base URL。

对应的 skill 使用方式不应暴露成命令行要求，而应写成：

```text
当用户要求生成论文图时：
1. 先确认 figure type、输出路径、必须出现的文字、风格偏好。
2. 读取对应 style preset 和 figure-type template。
3. 合成 prompt。
4. 调用 scripts/render_figure.py。
5. 检查输出和 prompt copy，必要时迭代。
```

模板设计：

```text
figure-base.md:
  只写通用质量标准：清晰、无重叠、短标签、连接线清楚、学术图风格。

architecture.md:
  只写架构图布局范式：pipeline、layered stack、hub-and-spoke、feedback loop。

roadmap.md:
  只写技术路线图范式：阶段、依赖、里程碑、输入输出。

style preset:
  只写配色、字体、线条、图标、背景、阴影，不写领域内容。
```

最重要的边界：领域内容只能来自用户 brief，不能来自 skill 内置 prompt。

## Skill 2: `paper-table-polisher`

目标：让 AI 能稳定生成漂亮、可投稿的 LaTeX 表格，而不是每次临时写 `tabular`。

推荐能力：

- 输入自然语言表格需求，输出 LaTeX 表格。
- 输入 CSV/Markdown 表格，转换为论文表格。
- 内置常见模板：方法对比、ablation、dataset statistics、human evaluation、case taxonomy、error analysis。
- 内置配色：灰阶安全、轻量强调色、best/second-best 高亮、分组 header。
- 支持 `booktabs`、`siunitx`、`tabularx`、`multirow`、`xcolor`。

建议模板原则：

- 默认不用竖线。
- `\toprule \midrule \bottomrule` 是基础。
- 数字列用 `S` 列对齐。
- 表格太宽时优先改列名、分组、字号和 `tabularx`，不要直接暴力 `\resizebox{\textwidth}{!}`。
- 高亮只表达真实语义：best、second-best、ours、statistically significant。

建议 assets：

```text
assets/templates/comparison-table.tex
assets/templates/ablation-table.tex
assets/templates/dataset-stat-table.tex
assets/templates/case-study-table.tex
assets/latex/ra-table-style.sty
```

`ra-table-style.sty` 可以提供：

```latex
\newcommand{\best}[1]{\textbf{#1}}
\newcommand{\second}[1]{\underline{#1}}
\newcommand{\ours}[1]{\cellcolor{RAAccent!12}\textbf{#1}}
\newcommand{\tabnote}[1]{\vspace{2pt}\footnotesize #1}
```

## Skill 3: `paper-layout-fixer`

目标：解决“AI 不理解我说的排版问题，总是排不好”。这里不要做成纯 prompt skill，要做成诊断型 skill：先编译、读日志、定位问题，再改。

推荐能力：

- 运行 `latexmk` 或项目已有编译命令。
- 解析 `.log`，提取 overfull/underfull hbox、float too large、undefined references、duplicate labels、missing citations。
- 读取目标 `.tex` 附近内容，给出小范围修复。
- 修复后重新编译并汇报还剩哪些 warning。

它能解决的问题：

- 图表浮动乱跑。
- 双栏论文中 `figure*`/`table*` 放置不稳定。
- 表格太宽。
- caption 太长或 spacing 不一致。
- appendix 盒子跨页失败。
- algorithm/listing 与正文间距难看。
- bibliography 或 appendix 起页不符合预期。

不建议承诺的问题：

- “自动把整篇论文排得很好看”。这太宽泛。
- “完全不改内容只靠 LaTeX 解决所有溢出”。很多 overfull 需要改句子或表头。

建议工作流：

```text
1. 确认目标：修哪一页、哪张图表、哪类 warning。
2. 编译并生成 layout report。
3. 分类问题：float / width / spacing / labels / package conflict。
4. 只改最小范围。
5. 再编译，输出 before/after。
```

建议脚本：

```bash
python scripts/compile_and_parse.py --root paper.tex --engine latexmk
python scripts/latex_log_report.py build/paper.log --format markdown
```

## Skill 4: `paper-box-styler`

目标：为附录中的代码框、prompt 框、case study 框、definition 框提供统一样式。

推荐技术：

- `tcolorbox` 做外框、标题、背景、分页。
- `minted` 做代码高亮，适合本地可开 `-shell-escape` 的环境。
- `listings` 做无 shell-escape 兜底。
- 所有颜色从 `ra-colors.sty` 引入，避免每个 box 自己定义一套颜色。

建议内置组件：

```latex
\begin{RAPromptBox}[title={Prompt for Figure Generation}]
...
\end{RAPromptBox}

\begin{RACodeBox}[language=Python,title={Verifier}]
...
\end{RACodeBox}

\begin{RACaseBox}[title={Case Study: Failure Repair}]
...
\end{RACaseBox}
```

设计要求：

- 支持跨页：`breakable`。
- 标题短、背景浅、边框细。
- 默认适合黑白打印。
- 不能显著增加论文视觉噪音。
- 如果会议模板和 `tcolorbox` 冲突，提供 plain fallback。

## 共享设计系统

建议抽出统一 palette/font/token 文件，否则四个 skill 会各自长出一套风格。

`shared/palettes.yaml` 示例：

```yaml
vivid-academic:
  primary: "#4F46E5"
  secondary: "#0891B2"
  accent: "#F97316"
  success: "#10B981"
  warning: "#F59E0B"
  neutral_bg: "#F8FAFC"
  neutral_text: "#111827"

grayscale-camera-ready:
  primary: "#111827"
  secondary: "#4B5563"
  accent: "#6B7280"
  neutral_bg: "#FFFFFF"
  neutral_text: "#111827"
```

`shared/fonts.yaml` 示例：

```yaml
figure_default:
  label: "Comic Sans MS"
  fallback: "Arial"
latex_default:
  text: "default conference template"
  mono: "inconsolata if available, otherwise ttdefault"
```

## 实现顺序

### Phase 1: 清理现有 figure skill

目标：把当前 `paper-figure-imagegen` 变成可迁移的通用版本。

任务：

- 删除 River/ReproAgent/具体方法名硬编码。
- 删除脚本中的 API key/base URL 默认值。
- 改为 `.env` 和环境变量读取。
- 把风格 prompt 移入 `assets/styles/*.yaml` 或 `references/style-presets.md`。
- 增加用户 override：font、palette、style-notes、required-text、forbid-text。

验收：

- skill 内不出现具体论文名、项目名、方法名。
- dry-run 不泄露 key/base URL。
- 用户 brief 改成完全不同论文方向时，生成 prompt 不带旧项目术语。

### Phase 2: 做 table skill

目标：最快产生论文写作收益。

任务：

- 写 `paper-table-polisher/SKILL.md`。
- 准备 4 个高频表格模板。
- 写 `ra-table-style.sty`。
- 提供 CSV/Markdown 到 LaTeX 的简单转换脚本。

验收：

- 给一个 Markdown 表格，能生成可编译 LaTeX。
- ablation/comparison/statistics 三类表格风格统一。
- 表格不默认用竖线，不乱用 resizebox。

### Phase 3: 做 box skill

目标：统一附录视觉风格。

任务：

- 写 `ra-box-style.sty`。
- 做 prompt/code/case 三类 box。
- 提供 minted 和 listings 两套路径。

验收：

- 不开 shell-escape 时仍有 fallback。
- 长 prompt 可以跨页。
- 盒子样式和 table/figure 配色一致。

### Phase 4: 做 layout skill

目标：降低排版调试时间。

任务：

- 写 LaTeX 编译日志解析脚本。
- 建 layout playbook。
- 把常见 warning 映射到修复策略。

验收：

- 能输出明确报告：问题位置、类型、建议修复。
- 对 overfull hbox、float placement、undefined refs 至少三类问题有效。
- 修复建议尽量局部，不大改论文结构。

## 风险与建议

### 风险 1: skill 过大导致触发后上下文爆炸

解决：`SKILL.md` 只保留工作流和导航。模板、风格、示例都放 references/assets。

### 风险 2: 图像 prompt 偷偷带入旧论文内容

解决：强制区分 style prompt 和 content prompt。style 只允许颜色、字体、布局、线条、图标；content 只能来自用户 brief。

### 风险 3: API key 泄露

解决：脚本不硬编码 key；dry-run 不打印 key；prompt copy 不写 credential；`.env` 加入 `.gitignore`。

### 风险 4: LaTeX 模板和会议模板冲突

解决：每个 style 都提供 full 和 minimal 两档。默认 minimal，只使用稳定包；full 才启用 `tcolorbox`、`minted` 等高级组件。

### 风险 5: 智能排版变成玄学

解决：layout skill 必须围绕编译日志和具体页码工作。没有 log 或截图时，只能给建议，不应直接大改。

## 最小可行版本

建议先做一个 MVP，不要一开始做完整 suite。

MVP 包含：

1. 清理并重构 `paper-figure-imagegen` 为 `paper-figure-studio`。
2. 新增 `paper-table-polisher`，只支持 comparison/ablation/statistics 三类表。
3. 新增 `paper-box-styler`，只提供 prompt/code/case 三类 box。
4. `paper-layout-fixer` 先只做 log report，不自动修。

这个 MVP 大约就能覆盖你 proposal 里的 80% 使用场景，而且不会陷入“大而全”的实现泥潭。

## 下一步建议

下一步应该先动现有 `.codex/paper-figure-imagegen`，因为它已经证明有用，并且也是后续共享风格系统的样板。具体顺序：

1. 先清理硬编码和 credential。
2. 抽出 style preset。
3. 改 render 脚本支持 style merge。
4. 再复制这个结构，创建 table/box/layout 三个 skill。

如果只投入一天，优先做 Phase 1 和 Phase 2；如果投入两到三天，可以把 box skill 也做出来；layout skill 建议最后做，因为它依赖真实 LaTeX 项目和日志样本来打磨规则。
