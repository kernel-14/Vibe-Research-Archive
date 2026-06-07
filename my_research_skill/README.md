# my_research_skill 

个人写paper / 做调研过程中沉淀下来的 Skill收录。

## 思路

分为**输入侧（idea / topic 探索）** 与 **输出侧（论文产出）**：

- 输入侧：`topic-mentor` / `paper-mentor` → `idea-extension` → `brainstorm-search` → `diffusion-idea`，从入门 → idea 审核打磨 → 全景调研 → 假设验证。其中 `topic-mentor` 从领域脉络入门，`paper-mentor` 从单篇论文锚定入门，`idea-extension` 把粗 idea 审核 + 打磨 + 延展。
- 输出侧：`RA-Skill/` 下的四件套（figure / table / box / layout）+ 历史版本 `paper-figure-imagegen`。

设计原则：

1. **Skill 不内置领域内容**。模板只负责风格和结构，论文内容只能从用户 brief 里来。
2. **Credential 全部走 env / .env**，脚本里没有任何硬编码 API key。
3. **每个 SKILL.md 只放工作流和导航**，长模板/示例放 references/assets，避免触发后上下文爆掉。

## 目录概览

```
my_research_skill/
  topic-mentor/              # 第一性原理 + 费曼学习法导师（领域脉络入门）
  paper-mentor/              # 单篇论文锚定精读 + 第一性原理延展 + idea 孵化
  idea-extension/            # idea 审核 + 打磨 + 延展（review / optimize / extend）
  brainstorm-search/         # 多角度调研 → 文献全景
  diffusion-idea/            # idea 演化 + 多 critic 验证
  RA-Skill/
    skills/
      paper-figure-studio/   # 论文图：可换风格预设
      paper-table-polisher/  # LaTeX 表格美化 + 语义高亮
      paper-layout-fixer/    # 编译日志诊断 + 局部修复
      paper-box-styler/      # 附录 prompt/code/case/theorem 盒子
    shared/                  # 共用 palette / fonts / sty
    proposal.md              # 原始需求
    research.md              # 设计调研与决策依据
  paper-figure-imagegen/     # 单论文专用的初代版本
```

---

## 输入侧 Skill

### topic-mentor — 入门一个新方向

**用途**：从零进入一个领域。Skill 会扮演严格的导师，用费曼学习法 + 第一性原理拆解，**不直接给答案**，而是用 Socratic 提问把你的盲点逼出来。

**触发**：`/topic-mentor X`、"帮我梳理 X 的发展脉络"、"用费曼学习法教我 X"、"grill me on X"。

**5 阶段工作流**：脉络搭建 → 第一性原理拆解 → 费曼诊断 → 前沿延展 → idea 孵化。每阶段有出口问题，不能跳。

**输出**：`<topic>/roadmap.md`，标注已掌握节点 / 仍模糊节点 / 新 idea / 推荐阅读。

### paper-mentor — 以一篇论文为锚点入门

**用途**：手里有一篇具体论文，想真正吃透它并以它为支点理解整个方向。是 `topic-mentor` 的"单篇锚定"变体：topic-mentor 从领域脉络出发，paper-mentor 从一篇 paper 出发，向外辐射到 motivation、related work 发展、方法推导、实验细节，再做第一性原理延展。**不替你读完论文**，而是用 Socratic 提问 + 手推公式逼出盲点。

**触发**：`/paper-mentor <论文>`、"带我精读这篇 paper"、"用这篇论文入门 X"、直接丢来本地路径 / arXiv id / URL / 标题。

**论文读入策略**（第一个成功即停）：本地文件直接 Read → 联网直读（WebFetch，arXiv 优先）→ 直读失败就 `curl` 下载到当前目录再读 → 只有标题就先 WebSearch 定位真实链接。**永远不凭记忆编 arXiv 编号。**

**6 阶段工作流**：定位读入 → Motivation 拆解 → Related Work 脉络 → 方法推导（第一性原理 + 手推公式）→ 实验细节（claim ↔ 证据对照）→ 延展 + idea 孵化 → 基于用户 idea 进一步联网搜索接地。Stage 5 的 idea 评审交给独立的 `idea-extension` skill。

**输出**：单篇笔记 `<paper-short-name>/<paper-short-name>.md`（电梯摘要 / motivation / 脉络 / 推导 / 实验 / 延展 idea / 搜索结论 / 掌握度），全程由 skill 自己维护。

### idea-extension — idea 审核 + 打磨 + 延展

**用途**：手里有一个（或几个）粗糙 idea，想被严格地评一评、磨一磨、再延展成站得住的 problem-method-experiment 方案。三段式：**review**（多视角 critic 打分 + 致命门）→ **optimize**（磨问题、磨机制、定贡献、设计最小证据包）→ **extend**（第一性原理松绑假设 / 迁移机制 / 推到极限）。可单独用，也被 `paper-mentor` Stage 5 调起，给从论文延展出的 idea 做接地评审。

**触发**：`/idea-extension`、"评一下这个 idea"、"这个 idea 能不能做"、"帮我打磨/延展这个想法"、"review/optimize/extend this idea"。

**核心约束**：不编造文献/结果/baseline/reviewer 反应；**绝不单评审**（≥4 个独立视角）；"低新颖"与"未搜索新颖"分开报，未联网前新颖性一律标 `needs-literature-search`；先优化 idea 再谈写作。references 拆成 `idea-intake` / `review-rubric` / `problem-method-blueprint` / `experiment-design` 四个文件按需加载。

**输出**：单 idea 的 idea card + 多视角审核 + 10 维打分 + 致命风险 + fixability + 延展变体 + 推荐；多 idea 时按"扣除致命风险后"的潜力排序。

### brainstorm-search — 全景式调研，不做验证

**用途**：你已经有一个模糊方向，需要先**画一张地图**，看清边界、奠基论文、相邻学科。**不做假设验证、不做实验**——纯调研。

**触发**：自然语言里出现"先帮我做个调研"、"survey 一下这个方向"。

**结构**：
- L1 5 个并行 breadth agent（跨学科类比 / 被挑战的前提 / 新连接 / 方法迁移 / 负结果）
- L2 3 个并行 depth analyst（综合 + 排序 + 找空白点）
- L3 6 个并行 literature 调研 agent（历史 / 经典方法 / 未解 / 流派 / 近期突破 / 理论基础）

**输出**：`artifacts/landscape_report.md`。

### diffusion-idea — idea 演化 + 多 critic 验证

**用途**：你已经有了一个 idea 雏形，要把它从模糊噪声"去噪"成有实验支撑的方案。本质是 **brainstorm-search + 实验快速验证**。

**触发**："帮我把这个 idea 跑一轮验证"、"做几个 critic review"。

**核心约束**：novel research 没有 ground truth，所以验证手段是**多元 critic 对抗审查**。每轮实验必须 spawn 至少 3 个独立 critic（empiricist / theoretician / engineer 视角），不允许单评审。

**输出**：`artifacts/final_idea.md`（含 evolution path / 实验证据 / 后续步骤）或失败回环到调研。

> brainstorm-search ≈ diffusion-idea 去掉 L3 实验环节。前者只到"地图"，后者要走到"假设 + 验证"。

---

## 输出侧 Skill：RA-Skill/

写论文时反复用到的四类操作，每类一个独立 Skill。共用的 palette / font / `.sty` 抽到 `RA-Skill/shared/`。

### paper-figure-studio — 论文图

**用途**：架构图 / 技术路线图 / schema / chart / tracks / 通用解释图。**风格可插拔**，预设包含：
- `default`（baseline，会议安全）
- `minimal-academic`（camera-ready）
- `colorful-method`（vivid 配色 + Comic Sans 标签）
- `grayscale-camera-ready`（黑白印刷）

**最小命令**（凭证读 env 或 `.env`）：
```bash
python skills/paper-figure-studio/scripts/render_figure.py \
  --prompt-file fig/brief.md \
  --figure-type architecture \
  --style colorful-method \
  --palette vivid-academic \
  --font "Comic Sans MS" \
  --out fig/overview.png
```

**关键约束**：style preset 不允许写论文术语；领域内容只能来自用户 brief。`--dry-run` 用于检查 prompt 拼装与配置来源，不会泄露 secret。

### paper-table-polisher — 论文表格

**用途**：把 Markdown / CSV 表转成 booktabs + siunitx 的论文级 LaTeX 表，自动打 best / second / ours 高亮。

**模板**：comparison / ablation / dataset-stat / case-taxonomy / human-eval 五种。
**Style sty**：`assets/latex/ra-table-style.sty` 提供 `\best{}` `\second{}` `\ours{}` `\sig{}` `\tabnote{}`。

**最小命令**：
```bash
python skills/paper-table-polisher/scripts/table_from_csv.py results.csv \
  --type comparison --best-col-mode max --second-best \
  --ours-row 4 --label tab:main --caption "Main Results"
```

**硬规则**：不用 `\hline`、不用竖线、宽度问题先改列名再考虑 `\resizebox`。

### paper-layout-fixer — LaTeX 排版诊断

**用途**：解决"AI 总排不好版"的痛点。**先编译再说话**：解析 .log，分类 overfull / underfull / float / undefined ref / package conflict，给出局部修复建议。

```bash
python skills/paper-layout-fixer/scripts/compile_and_parse.py --root paper.tex --engine latexmk
python skills/paper-layout-fixer/scripts/latex_log_report.py build/paper.log --format markdown --out build/report.md
```

**承诺范围**：浮动错位、双栏 figure*/table* 放置、caption 宽度、algorithm 间距、bib 起页。**不承诺**："让整篇论文看起来更好"——这种诉求不可验证。

### paper-box-styler — 附录盒子

**用途**：附录中长 prompt / 代码 / case / 定理 的统一样式。基于 `tcolorbox`。
- `RAPromptBox`、`RACodeBox`、`RACaseBox`、`RATheoremBox`
- 默认 `breakable`（长 prompt 跨页不爆）
- minted（要 `-shell-escape`）和 listings（不要）双路径
- 与会议模板冲突时切到 `[fallback]` option，自动降级为不带颜色的 quote 样式

### paper-figure-imagegen — 初代单论文版本

最早写的版本，比 `paper-figure-studio` 简单，只针对一篇论文的固定风格。**已删掉硬编码的 API key 和 base URL**——现在凭证全部从 `OPENAI_API_KEY` / `OPENAI_BASE_URL` 或 `.env` 读取。保留它是因为它已经是单论文场景的最小可用形态。

---

## 示例

完整示例放在 `example/` 目录，每个 skill 都有独立输入、调用命令和真实结果。图像类示例已经用 `gpt-image-2` 真实生成 PNG；凭证仍从环境变量或 `.env` 读取。

| Skill | 示例内容 | 结果 |
| --- | --- | --- |
| `topic-mentor` | `example/topic-mentor/prompt.md` | `example/topic-mentor/result.md` |
| `brainstorm-search` | `example/brainstorm-search/prompt.md` | `example/brainstorm-search/result.md` |
| `diffusion-idea` | `example/diffusion-idea/prompt.md` | `example/diffusion-idea/result.md` |
| `paper-figure-studio` | `example/paper-figure-studio/brief.md` + `command.md` | `example/paper-figure-studio/overview.png` |
| `paper-table-polisher` | `example/paper-table-polisher/results.csv` + `command.md` | `example/paper-table-polisher/main_table.tex` |
| `paper-layout-fixer` | `example/paper-layout-fixer/paper.tex` + `command.md` | `example/paper-layout-fixer/build/report.md` |
| `paper-box-styler` | `example/paper-box-styler/sample.tex` + `command.md` | `example/paper-box-styler/build/sample.pdf` |
| `paper-figure-imagegen` | `example/paper-figure-imagegen/prompt.md` + `command.md` | `example/paper-figure-imagegen/research_loop.png` |

---

## 怎么用（实际接入）

### Claude Code

把对应目录复制到 Claude Code 的 skills 位置（项目级 `.claude/skills/<skill-name>/` 或全局 `~/.claude/skills/<skill-name>/`），然后：

```text
/topic-mentor 我想搞懂 GRPO
/paper-mentor https://arxiv.org/abs/2305.18290 带我精读 DPO 这篇
/idea-extension 评一下这个 idea：用对比学习改进长文档检索
/brainstorm-search 用 diffusion 的视角重新看 RAG
用 paper-figure-studio 帮我画一张方法总览图，风格用 colorful-method
用 paper-table-polisher 把 results.csv 转成 ablation 表，best 加粗
用 paper-layout-fixer 看一下 paper.tex 第 7 页为什么图跑飞了
```

### Codex

每个 skill 自带 `agents/openai.yaml`。把目录放到项目的 `.codex/skills/<skill-name>/` 即可被识别。

### 命令行直跑

每个带 `scripts/` 的 skill 都可以脱离 agent 单独跑（接口在各自 SKILL.md 里）。这是为了：
- 调试时可重复
- 批量生成图/表
- CI 里直接调用

---

## 关于凭证

所有脚本现在都是从以下顺序读取：

1. CLI flag（`--api-key` / `--base-url`）
2. 环境变量（`OPENAI_API_KEY` / `OPENAI_BASE_URL`）
3. 当前目录 `.env`
4. 内置默认（仅模型名等非敏感字段；URL 和 key 没有内置默认）

`.dry-run` 模式只会回显"key 是否解析到、来源是哪个 env 字段"，**不会**回显 key 本身。


