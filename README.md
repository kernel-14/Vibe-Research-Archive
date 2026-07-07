# Vibe Research 相关工作整理

本仓库整理近期看过的 Vibe Research 相关工作 o(*￣▽￣*)ブ 

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

这一章主要是各类 autoresearch loop，大致流程就是 提出候选 -> 实现候选 -> 评估候选 -> 分析失败 -> 记录经验 -> 继续迭代。进一步的变化主要是并行 autoresearch loop、多 agent 架构、memory/database 设计和 evaluator/benchmark 设计。

### 2.1 Autoresearch loop

| 仓库 | 创建时间 | Stars | 在做什么 |
| --- | --- | ---: | --- |
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 2026-03-06 | 83659 | 最小 autoresearch loop：agent 反复改 `train.py`、训练 nanochat、用固定指标决定保留或回滚。 |
| [GAIR-NLP/ASI-Evolve](https://github.com/GAIR-NLP/ASI-Evolve) | 2026-03-27 | 692 | 把任务抽象成 `candidate + evaluator + database/cognition` 的进化式搜索框架。 |
| [algorithmicsuperintelligence/openevolve](https://github.com/algorithmicsuperintelligence/openevolve) | 2025-05-15 | 6429 | AlphaEvolve 风格开源实现，偏通用 LLM 程序进化和优化。 |
| [gepa-ai/gepa](https://github.com/gepa-ai/gepa) | 2025-08-05 | 4749 | Reflective Text Evolution，用 AI 优化 prompt、代码和文本 candidate。 |
| [InternScience/MLEvolve](https://github.com/InternScience/MLEvolve) | 2026-02-14 | 292 | 面向机器学习算法设计和优化的 progressive search + experience memory。 |
| [allenai/codescientist](https://github.com/allenai/codescientist) | 2025-03-10 | 337 | code-based scientific discovery：生成 idea、构建实验、运行调试、写实验报告。 |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | 2024-08-12 | 13787 | 从 idea 到实验再到 paper draft 的自动科学发现系统。 |
| [SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) | 2025-04-08 | 6383 | 用 agentic tree search 做 workshop-level 自动科学发现。 |
| [HKUDS/AI-Researcher](https://github.com/HKUDS/AI-Researcher) | 2025-03-11 | 5389 | Autonomous Scientific Innovation，偏完整 AI researcher 系统。 |

### 2.2 并行 autoresearch loop / 架构优化

| 仓库 | 创建时间 | Stars | 在做什么 |
| --- | --- | ---: | --- |
| [Human-Agent-Society/CORAL](https://github.com/Human-Agent-Society/CORAL) | 2026-03-16 | 675 | 多 agent 并行 autoresearch，每个 agent 在独立 worktree 中探索，共享公共记忆和技能。 |
| [AweAI-Team/AiScientist](https://github.com/AweAI-Team/AiScientist) | 2026-03-30 | 123 | File-as-Bus 长周期研究实验室，把计划、代码、日志、验证结果都落到 workspace。 |
| [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | 2026-01-26 | 3189 | 自我进化 AI Scientist，强调多 agent、memory、MCP、skills 和持续研究工作流。 |
| [InternScience/InternAgent](https://github.com/InternScience/InternAgent) | 2025-05-16 | 1307 | Long-horizon autonomous scientific discovery 统一 agentic framework。 |
| [ResearAI/DeepScientist](https://github.com/ResearAI/DeepScientist) | 2025-09-26 | 2814 | AI scientist / deep research 方向的系统化探索框架。 |
| [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 2026-03-15 | 12771 | 从 idea 到 paper 的全自动、自进化 research workflow，基于 OpenClaw 生态。 |
| [OpenRaiser/NanoResearch](https://github.com/OpenRaiser/NanoResearch) | 2026-03-17 | 1339 | Autonomous AI Research Assistant，偏轻量科研 agent/skills 组合。 |
| [tsingyuai/scientify](https://github.com/tsingyuai/scientify) | 2026-02-04 | 465 | OpenClaw 上的 AI-powered research workflow automation。 |

### 2.3 Benchmark / evaluator

| 仓库 | 创建时间 | Stars | 在做什么 |
| --- | --- | ---: | --- |
| [openai/mle-bench](https://github.com/openai/mle-bench) | 2024-10-08 | 1544 | 评测 AI agent 做机器学习工程任务的 benchmark。 |
| [allenai/asta-bench](https://github.com/allenai/asta-bench) | 2025-03-21 | 108 | 科学任务 agent 能力评测相关 benchmark。 |
| [xyzCS/SciReplicate-Bench](https://github.com/xyzCS/SciReplicate-Bench) | 2025-03-31 | 13 | 评测 LLM agent 从论文复现算法的 benchmark。 |
| [CenterForOpenScience/llm-benchmarking](https://github.com/CenterForOpenScience/llm-benchmarking) | 2025-06-16 | 5 | 评测 LLM agents 在科研生命周期中的能力，包括 replication、peer review、research design。 |
| [No-518/ResearchEnvBench](https://github.com/No-518/ResearchEnvBench) | 2026-03-05 | 3 | Research environment / research agent 相关评测。 |

## 3. AI assistant

这一部分主要有两类工作：一类是比较系统化的 pipeline，把研究材料组织成论文、slides、poster、video、homepage 等产物；另一类是 skills 合集，把科研经验和写作经验整理成 agent 可调用的能力包。

### 3.1 系统化 Pipeline

| 仓库 | 创建时间 | Stars | 在做什么 |
| --- | --- | ---: | --- |
| [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | 2026-02-26 | 968 | Research workspace / AI Lab IDE，把研究计划、任务和产物放到一个工作区里管理。 |
| [QZhang2111/Research-Pilot](https://github.com/QZhang2111/Research-Pilot) | 2026-05-09 | 20 | 用 papers、claims、evidence、experiments 和 human gates 维护研究项目。 |
| [bytedance/pasa](https://github.com/bytedance/pasa) | 2024-12-23 | 1570 | Paper search agent，自动检索、阅读和筛选相关论文。 |
| [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) | 2024-11-20 | 11508 | Deep research workflow，面向检索、综合和报告生成。 |
| [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | 2023-02-05 | 8567 | 面向科学文献的高准确 RAG / paper QA，带 citation。 |
| [OpenDCAI/Open-NotebookLM](https://github.com/OpenDCAI/Open-NotebookLM) | 2026-01-08 | 73 | NotebookLM 开源实现，偏文档/论文材料组织和问答。 |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | 2024-02-29 | 65144 | PDF/Office 文档转 LLM-ready markdown/JSON，是论文材料处理的基础设施。 |
| [OpenDCAI/Paper2Any](https://github.com/OpenDCAI/Paper2Any) | 2025-10-17 | 2502 | 从 paper/text/topic 生成可编辑科研图、技术路线图和 slides。 |
| [HKUDS/Paper2Slides](https://github.com/HKUDS/Paper2Slides) | 2025-12-07 | 3686 | 从论文一键生成 presentation slides。 |
| [Paper2Poster/Paper2Poster](https://github.com/Paper2Poster/Paper2Poster) | 2025-05-16 | 3735 | 多 agent 从论文生成学术 poster。 |
| [showlab/Paper2Video](https://github.com/showlab/Paper2Video) | 2025-10-03 | 2295 | 从科学论文自动生成讲解视频。 |
| [LightChen233/AutoPR](https://github.com/LightChen233/AutoPR) | 2025-09-29 | 103 | 自动化 academic promotion，例如 project page / 宣传材料方向。 |

### 3.2 Skill 合集

| 仓库 | 创建时间 | Stars | 在做什么 |
| --- | --- | ---: | --- |
| [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | 2026-04-19 | 1111 | 博导经验整理成 AI skills，覆盖 idea、论文结构、写作、图表、投稿前检查等。 |
| [mikubaka88/CCFA-Skills](https://github.com/mikubaka88/CCFA-Skills) | 2026-06-04 | 132 | CCF-A 投稿向 skills 合集，覆盖 idea 评审/优化、论文写作、rebuttal、reviewer 等环节。 |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 2026-02-26 | 22519 | Claude Code 学术研究 skills，从 research 到 write、review、revise、finalize。 |
| [HughYau/AcademicForge](https://github.com/HughYau/AcademicForge) | 2026-02-03 | 1292 | 一站式学术研究 skills 平台，偏 curated skill collection。 |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 2025-11-03 | 8978 | 面向 Claude/Codex/Gemini 等 agent 的 AI research / engineering skills 库。 |
| [TenureAI/PhD-Zero](https://github.com/TenureAI/PhD-Zero) | 2026-02-27 | 52 | PhD-level workflows + modular agent skills，偏 autoresearch 工作流操作层。 |
| [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 2026-03-10 | 10808 | ARIS，Markdown-only skills，支持 idea discovery、experiment automation、cross-model review loops。 |
| [Trae1ounG/paper-plot-skills](https://github.com/Trae1ounG/paper-plot-skills) | 2026-04-17 | 295 | 顶会论文图表复现和绘图 skills。 |
| [Tardfyou/ccfa-skills](https://github.com/Tardfyou/ccfa-skills) | 2026-05-03 | 10 | 用于绘制 CCF-A 统计图的绘图 skills。 |
| [MLNLP-World/Paper-Writing-Tips](https://github.com/MLNLP-World/Paper-Writing-Tips) | 2022-04-13 | 4475 | 论文投稿和写作常见问题整理。 |
| [zhaoyang97/Paper-Notes](https://github.com/zhaoyang97/Paper-Notes) | 2026-03-18 | 395 | AI / LLM / NLP / CV 论文速读和笔记集合。 |

## 4. 本仓库自定义 Skill

| Skill | 位置 | 在做什么 |
| --- | --- | --- |
| `table-beautifier` | [`my_research_skill/table-beautifier`](my_research_skill/table-beautifier/SKILL.md) | LaTeX 表格视觉美化模板库，提供 `table-style.sty`、rank cells、pastel groups、ours delta、heatmap、significance、case matrix、compact wide、wrap summary 等样式。PDF 展示见 [`table-gallery.pdf`](my_research_skill/table-beautifier/assets/gallery/table-gallery.pdf)。 |
| `intro-story-rewriter` | [`my_research_skill/intro-story-rewriter`](my_research_skill/intro-story-rewriter/SKILL.md) | 论文 Introduction 逻辑重写：把任务动机、证据来源、问题缺口、方法模块、指标、benchmark 和主结果串成一条清晰 story line。 |

## 5. 写作原则来源

`intro-story-rewriter` 主要沉淀了这次改 paper intro 时验证过的写作原则：

- [MIT Communication Lab: Journal Article Introduction](https://mitcommlab.mit.edu/eecs/commkit/journal-article-introduction/)：Introduction 要先建立 problem context，再给出 gap 和贡献。
- [Jennifer Widom: Tips for Writing Technical Papers](https://cs.stanford.edu/people/widom/paper-writing.html)：开头要尽快说明问题、动机和本文具体贡献，避免空泛背景。
- [Simon Peyton Jones: How to Write a Great Research Paper](https://simon.peytonjones.org/great-research-paper/)：论文 intro 要明确提出 claim，并让后文证据服务于这个 claim。

在实际使用中，我把它整理成一个更机械的检查链：

```text
任务需求 -> 现有方法有效但仍有成本/失败 -> 证据 -> 缺失的问题接口或度量
       -> 方法模块 -> 指标与 benchmark -> 主结果
```

