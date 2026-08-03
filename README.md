# Vibe Research 相关工作整理

本仓库整理近期看过的 Vibe Research 相关工作， 整体来讲我将目前的autoresearch工作分为两大类，一类属于“AI scientist”,主旨在于使用ai加速科学发现/提升系统效率等等，这一类工作希望通过ai工具进行自动化的科研或工程探索（包括更广义的ai4science大多属于这一类，但是本仓库只考虑ML领域的）；另一类属于“AI assistant”，主旨在于使用ai加速科研产物的生成（paper、report流水线），这一类工作希望通过ai加快科研产物的生成。前者的重点是idea的生成，加速具体学科的科学发现本身，探索性更强；后者的重点是加速整套科研行为的工作流，更注重于规范、忠实、可回溯、可验证的完成任务，快速得到相应的科研产物。

## 1. 两条主线

目前相关工作大致分成两条主线。

### 1.1 LLM 加速科研发现（AI Scientist）

这一条线的主要目的是探索LLM如何提出、验证、优化idea，从而加速科学发展或对具体的系统进行优化，代表工作是 autoresearch(https://github.com/karpathy/autoresearch)

代表模式：

- 自动提出研究 idea
- 自动改代码、调参数、跑实验
- 用评分脚本或 benchmark 选择更好的候选
- 把失败经验沉淀成 memory / database / cognition store
- 通过多 agent 或进化式搜索扩大探索空间


### 1.2 LLM 加速科研产物生成（AI-assisted paper writing）

这一条线的主要目的是加速“将已有的研究材料转化为更完整的科研产物”的过程，更多探索的是如何利用LLM进行文献整理、论文写作、图表美化等，在这一点上本人最喜欢的工作是supervisor-skills(https://github.com/HKUSTDial/Supervisor-Skills)

代表模式：

- 读论文和整理 related work。
- 从实验日志生成表格、图和结果描述
- 帮助写 Introduction、Method、Experiment、Conclusion
- 检查 citation、LaTeX、图表、格式和一致性
- 生成 slides、project page、demo、rebuttal


## 2. AI Scientist

这一章按「研究闭环」的粒度分层：最小 loop（2.1）→ 进化式搜索算法（2.2）→ 多 agent 系统（2.3）→ 长周期单 agent（2.4）→ benchmark（2.5）。

### 2.1 Autoresearch loop

最小闭环：给定一个可度量的指标，agent 反复改代码、跑实验、根据分数决定保留还是回滚，目标是刷榜，把一个给定需要优化的指标推上去。

| 仓库 | 创建时间 | Stars | 在做什么 |
| --- | --- | ---: | --- |
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 2026-03-06 | 92848 | 最小 autoresearch loop：agent 反复改 `train.py`、训练 nanochat、用固定指标决定保留或回滚。 |
| [krzysztofdudek/ResearcherSkill](https://github.com/krzysztofdudek/ResearcherSkill) | 2026-03-22 | 252 | 用单个 SKILL.md 把 autoresearch loop 泛化到任意可度量任务：`.lab/` 存经验、失败自动 revert、收敛检测、跨 session 续跑。 |


### 2.2 进化式搜索 / candidate-evaluator 框架

把研究抽象成「候选 + 评估器 + 经验库」的搜索问题，重心在搜索策略和经验沉淀。

| 仓库 | 创建时间 | Stars | 在做什么 |
| --- | --- | ---: | --- |
| [algorithmicsuperintelligence/openevolve](https://github.com/algorithmicsuperintelligence/openevolve) | 2025-05-15 | 6832 | AlphaEvolve 风格开源实现，偏通用 LLM 程序进化和优化。 |
| [gepa-ai/gepa](https://github.com/gepa-ai/gepa) | 2025-08-05 | 5957 | Reflective Text Evolution，用 AI 优化 prompt、代码和文本 candidate。 |
| [InternScience/MLEvolve](https://github.com/InternScience/MLEvolve) | 2026-02-14 | 409 | 面向机器学习算法设计和优化的 progressive search + experience memory。 |
| [Kaimen-Inc/Co-Scientist](https://github.com/Kaimen-Inc/Co-Scientist) | 2026-05-26 | 212 | Google AI Co-Scientist 复现：Generation → Reflection（novelty 审查）→ Elo 锦标赛排序 → Evolution → Meta-review，CLI + WebUI。 |
| [GAIR-NLP/ASI-Evolve](https://github.com/GAIR-NLP/ASI-Evolve) | 2026-03-27 | 825 | 把任务抽象成 `candidate + evaluator + database/cognition` 的进化式搜索框架。 |

### 2.3 多 agent 系统

多个 agent 分工协作或并行探索，重心在 agent 间通信、workspace 隔离和公共记忆共享。

| 仓库 | 创建时间 | Stars | 在做什么 |
| --- | --- | ---: | --- |
| [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | 2026-01-26 | 4479 | 自我进化 AI Scientist，强调多 agent、memory、MCP、skills 和持续研究工作流。 |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 2026-03-15 | 13953 | 从 idea 到 paper 的全自动、自进化 research workflow，基于 OpenClaw 生态。 |
| [Human-Agent-Society/CORAL](https://github.com/Human-Agent-Society/CORAL) | 2026-03-16 | 868 | 多 agent 并行 autoresearch，每个 agent 在独立 worktree 中探索，共享公共记忆和技能。 |
| [AweAI-Team/AiScientist](https://github.com/AweAI-Team/AiScientist) | 2026-03-30 | 141 | File-as-Bus 长周期研究实验室，把计划、代码、日志、验证结果都落到 workspace。 |
| [mims-harvard/AutoScientists](https://github.com/mims-harvard/AutoScientists) | 2026-05-21 | 714 | 10 个 agent 自组织连跑数天，自带三个任务（含直接 wrap karpathy/autoresearch）。代码完整但仅 1 次 commit 后停更。 |
| [synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience) | 2026-07-03 | 3050 | `npx synsci` 即用的浏览器科研 workbench，一个 session 跑完文献→假设→代码→实验→成稿，带 290+ skills 和科学数据库连接器。 |

### 2.4 长周期单 agent

一个 agent 连续跑几天甚至几周，重心在崩溃恢复、常数内存、Slurm 等后端调度和反 reward-hacking。

| 仓库 | 创建时间 | Stars | 在做什么 |
| --- | --- | ---: | --- |
| [InternScience/InternAgent](https://github.com/InternScience/InternAgent) | 2025-05-16 | 1392 | Long-horizon autonomous scientific discovery 统一 agentic framework。 |
| [ResearAI/DeepScientist](https://github.com/ResearAI/DeepScientist) | 2025-09-26 | 3241 | AI scientist / deep research 方向的系统化探索框架。 |
| [tsingyuai/scientify](https://github.com/tsingyuai/scientify) | 2026-02-04 | 1669 | OpenClaw 上的 AI-powered research workflow automation。 |
| [OpenRaiser/NanoResearch](https://github.com/OpenRaiser/NanoResearch) | 2026-03-17 | 1480 | Autonomous AI Research Assistant，偏轻量科研 agent/skills 组合。 |
| [Xiangyue-Zhang/auto-deep-researcher-24x7](https://github.com/Xiangyue-Zhang/auto-deep-researcher-24x7) | 2026-04-08 | 1232 | Leader-Worker 架构、常数内存、YAML 配置、Slurm 后端，专门解决实验连轴跑不崩。 |
| [renee-jia/scholar-loop](https://github.com/renee-jia/scholar-loop) | 2026-06-15 | 465 | 单卡 PhD 式 loop，亮点是反 reward-hacking：冻结打分、编辑白名单、数字溯源。research preview。 |

### 2.5 Benchmark / evaluator

| 仓库 | 创建时间 | Stars | 在做什么 |
| --- | --- | ---: | --- |
| [ApodexAI/AgentHarness](https://github.com/ApodexAI/AgentHarness) | 2026-06-07 | 377 | 在公开 deep-research benchmark 上评估 Apodex-1.0 的 harness。 |
| [Proximal-Labs/frontier-swe](https://github.com/Proximal-Labs/frontier-swe) | 2026-03-10 | 202 | Ultra long-horizon coding agent benchmark，覆盖实现、性能优化和 ML 研究任务。 |
| [autolabhq/autolab](https://github.com/autolabhq/autolab) | 2026-04-01 | 158 | 36 个超长周期 auto-research 任务（系统优化 / CUDA / 模型开发）的 benchmark。 |

## 3. AI assistant

这一章按论文生产线的顺序排：文献进来（3.1）→ 材料处理和研究工作区（3.2）→ 各类产物生成（3.3）→ 投出去前的自查和投出去后的 rebuttal（3.4）→ 把这些经验打包成的 skills 合集（3.5）。

### 3.1 文献入口与个人知识库

流水线的入口。把 arXiv 和自己的 Zotero 库接进 agent，是后面所有环节的前提。

| 仓库 | 创建时间 | Stars | 在做什么 |
| --- | --- | ---: | --- |
| [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) | 2024-11-20 | 12486 | Deep research workflow，面向检索、综合和报告生成。 |
| [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | 2023-02-05 | 8978 | 面向科学文献的高准确 RAG / paper QA，带 citation。 |
| [TideDra/zotero-arxiv-daily](https://github.com/TideDra/zotero-arxiv-daily) | 2024-11-23 | 5763 | 按你自己的 Zotero 库每日推送匹配的 arXiv 新论文。 |
| [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp) | 2025-03-22 | 4521 | Zotero MCP 的事实标准，让 agent 直接读写你的文献库。 |
| [yilewang/llm-for-zotero](https://github.com/yilewang/llm-for-zotero) | 2026-01-29 | 2503 | 打包成 .xpi 直接装进 Zotero 的 research agent。 |
| [bytedance/pasa](https://github.com/bytedance/pasa) | 2024-12-23 | 1636 | Paper search agent，自动检索、阅读和筛选相关论文。 |

### 3.2 材料处理与研究工作区

| 仓库 | 创建时间 | Stars | 在做什么 |
| --- | --- | ---: | --- |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | 2024-02-29 | 76600 | PDF/Office 文档转 LLM-ready markdown/JSON，是论文材料处理的基础设施。 |
| [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | 2026-02-26 | 1039 | Research workspace / AI Lab IDE，把研究计划、任务和产物放到一个工作区里管理。 |

### 3.3 论文产物生成

| 仓库 | 创建时间 | Stars | 在做什么 |
| --- | --- | ---: | --- |
| [Paper2Poster/Paper2Poster](https://github.com/Paper2Poster/Paper2Poster) | 2025-05-16 | 3891 | 多 agent 从论文生成学术 poster。 |
| [HKUDS/Paper2Slides](https://github.com/HKUDS/Paper2Slides) | 2025-12-07 | 3808 | 从论文一键生成 presentation slides。 |
| [OpenDCAI/Paper2Any](https://github.com/OpenDCAI/Paper2Any) | 2025-10-17 | 2750 | 从 paper/text/topic 生成可编辑科研图、技术路线图和 slides。 |
| [showlab/Paper2Video](https://github.com/showlab/Paper2Video) | 2025-10-03 | 2341 | 从科学论文自动生成讲解视频。 |
| [Haojae/scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) | 2026-05-18 | 1564 | 出版级科研配图 copilot，同族还有 scipilot-writing / scipilot-cite。 |
| [LightChen233/AutoPR](https://github.com/LightChen233/AutoPR) | 2025-09-29 | 103 | 自动化 academic promotion，例如 project page / 宣传材料方向。 |

### 3.4 投稿前自查与 Rebuttal

投出去之前的红队自查，和收到审稿意见之后的应对。

| 仓库 | 创建时间 | Stars | 在做什么 |
| --- | --- | ---: | --- |
| [TobiasLee/Rebuttal-Skill](https://github.com/TobiasLee/Rebuttal-Skill) | 2026-07-14 | 445 | NeurIPS 杰出 AC 开源的 rebuttal 规范，含「值不值得 rebuttal / 该不该转投」判定和 P0-P3 实验排序。注意仓库只有一个 README.md，是纯 prompt 规范不是工程。 |
| [runtsang/RebuttalStudio](https://github.com/runtsang/RebuttalStudio) | 2026-02-21 | 215 | npm 起的 rebuttal 编辑器，带 UI、skills 和模板，能实际跑起来。 |
| [xf686/Meet-Reviewer-2](https://github.com/xf686/Meet-Reviewer-2) | 2026-06-22 | 40 | 投稿前红队：模拟审稿 panel 挑刺，输出证据化的 fix list。 |
| [tfscharff/doi-mcp](https://github.com/tfscharff/doi-mcp) | 2025-10-25 | 15 | MCP 形态的引用核验，跨 9 个库交叉比对，防 citation 幻觉。 |

### 3.5 Skill 合集

| 仓库 | 创建时间 | Stars | 在做什么 |
| --- | --- | ---: | --- |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 2026-02-26 | 40630 | Claude Code 学术研究 skills，从 research 到 write、review、revise、finalize。 |
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 2026-04-24 | 32905 | 18 个可安装 skill，一个仓库同时覆盖润色、配图、回审稿 + cover letter、引用核验、paper2ppt。 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 2025-10-19 | 32448 | 面向自然科学各学科的大型 skills 库，偏领域科学而非 ML。 |
| [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 2026-03-10 | 14151 | ARIS，Markdown-only skills，支持 idea discovery、experiment automation、cross-model review loops。 |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 2025-11-03 | 11343 | 面向 Claude/Codex/Gemini 等 agent 的 AI research / engineering skills 库。 |
| [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | 2026-04-19 | 4874 | 博导经验整理成 AI skills，覆盖 idea、论文结构、写作、图表、投稿前检查等。 |
| [MLNLP-World/Paper-Writing-Tips](https://github.com/MLNLP-World/Paper-Writing-Tips) | 2022-04-13 | 4578 | 论文投稿和写作常见问题整理。 |
| [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills) | 2026-05-13 | 2583 | DeepMind 官方科研 skills，强调 grounding 和 token 效率。 |
| [HughYau/AcademicForge](https://github.com/HughYau/AcademicForge) | 2026-02-03 | 2408 | 一站式学术研究 skills 平台，偏 curated skill collection。 |
| [mikubaka88/CCFA-Skills](https://github.com/mikubaka88/CCFA-Skills) | 2026-06-04 | 1414 | CCF-A 投稿向 skills 合集，覆盖 idea 评审/优化、论文写作、rebuttal、reviewer 等环节。 |
| [zhaoyang97/Paper-Notes](https://github.com/zhaoyang97/Paper-Notes) | 2026-03-18 | 1402 | AI / LLM / NLP / CV 论文速读和笔记集合。 |
| [Trae1ounG/paper-plot-skills](https://github.com/Trae1ounG/paper-plot-skills) | 2026-04-17 | 668 | 顶会论文图表复现和绘图 skills。 |

### 3.6 同类整理

- [modelscope/Awesome-Vibe-Research](https://github.com/modelscope/Awesome-Vibe-Research)（384）：定位和本仓库高度重合，按科研全生命周期分类。
- [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools)（1120）：同类整理里 star 最高的。
