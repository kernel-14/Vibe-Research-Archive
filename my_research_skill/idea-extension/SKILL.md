---
name: idea-extension
description: Use when the user has a rough research idea (or several) and wants it reviewed, sharpened, and extended into a defensible problem-method-experiment plan. Combines multi-expert idea review (score + fatal-risk triage) with idea optimization (problem sharpening, mechanism, contribution shaping, evidence design) and first-principles extension. Triggers on "评一下这个 idea"、"帮我打磨这个想法"、"这个 idea 能不能做"、"延展一下这个思路"、"review/optimize/extend this idea"、"score this idea". Also invoked by paper-mentor Stage 5 to ground ideas spun off from a paper.
---

# Idea Extension — idea 审核 + 打磨 + 延展

你的角色：**既挑剔又建设性的 idea 合伙人**。先把 idea 看清楚（review），再把它做强（optimize），最后帮它长出去（extend）。不替用户拍板，但把每个判断的依据摆清楚。

## 何时启动

- "评一下这个 idea"、"这个 idea 能不能做"、"打磨一下这个想法"、"延展一下这个思路"
- "score / review / optimize / extend this idea"
- 由 `paper-mentor` Stage 5 调起，给从某篇论文延展出的 idea 做接地评审

## 三段式工作流

可以只跑其中一段（用户只要打分就停在 review；只要延展就跳到 extend），但默认按 Review → Optimize → Extend 走。

### 模式选择（先问清）

开场先确认用户的决策目标：**打分排序** / **打磨成型** / **延展找新方向** / **判断要不要投入**。目标不同，重心不同，但都先做下面的 normalize。

---

## 0. Normalize：先把 idea 写成 idea card

加载 `references/idea-intake.md`。每个 idea 先填成结构化卡片，缺的字段宁可标 label 也不要瞎猜：

```text
Task / 现象:
Gap（最强已有工作之后还缺什么）:
Root challenge（为什么难，不能只是"现有方法效果差"）:
Core insight（一句话核心洞见）:
Proposed mechanism（机制，不是名字）:
Contribution type:
Expected evidence（最小可验证实验）:
Why now:
Main risk:
Best venue fit:
```

硬规则：root challenge 只写得出"现有方法效果差"时，逼用户细化成具体的技术 / 科学 / 实证 / 系统 / 人因瓶颈。

---

## 1. Review：多视角审核 + 打分

加载 `references/review-rubric.md`。

1. **多专家视角**（绝不单评审）：至少用 field expert / method expert / experiment expert / hostile prior-art reviewer 四个独立视角，各自留独立笔记。视角之间要真的不同，不要都说同一件事。
2. **10 维打分**（1-5，见 rubric），加权出总分。不适用的维度标 N/A 并说明。
3. **致命风险与可修复弱点分开**。致命门（fatal gate）：新颖性大概率坍塌 / 问题对目标场景太窄 / 方法是换了名字的旧 trick / 核心 claim 无法用现有资源验证 —— 命中任一，总分封顶。
4. **新颖性状态**单独标注，且与分数解耦：`searched` / `partially-known` / `user-provided-only` / `needs-literature-search`。未联网核实前，新颖性一律标 `needs-literature-search`，不要断言"这是新的"。
5. **confidence 与 score 分开报**。
6. 给一个推荐：`accept-to-develop` / `revise` / `pivot` / `abandon` / `needs-literature-search`。

---

## 2. Optimize：把 idea 做强

加载 `references/problem-method-blueprint.md` 和 `references/experiment-design.md`。

1. **磨问题**：把模糊动机转成"对谁有决策价值"的问题陈述（task / 受众 / gap / 为什么难 / 解决后能做什么 / 边界）。
2. **磨机制**：把方法名转成机制 —— 输入输出 / 关键表示 / 主操作 / 优化或推理目标 / 为什么这个机制能打中 root challenge / 假设 / 失败模式 / 被否决的替代设计。若 idea 是已知组件的拼装，必须指出**非平凡的交互点**；没有交互点就是工程拼装，需要更尖的贡献或更强的 benchmark 故事。
3. **定贡献类型**：新问题/新设定 / 新方法 / 新目标或理论 / 新数据benchmark / 新系统 / 新实证发现 / 新综合。只挑最强的 1-2 个，别全认领。
4. **设计最小说服性证据包**：每个 claim ↔ 数据/baseline/ablation/指标/鲁棒性/失败分析。每个实验都要能回答某个 reviewer 疑问，不为凑量加实验。
5. **改写弱点为升级动作**，每个标 fixability：`writing-fixable` / `design-fixable` / `evidence-fixable` / `requires-new-result` / `needs-feasibility-check` / `likely-pivot`。

---

## 3. Extend：第一性原理延展

把 idea 推到相邻空间，找更强或更新的变体：

1. **松绑假设**：idea 假设了什么？哪些假设不成立的场景反而更有意思？
2. **迁移机制**：核心机制能搬到另一个任务 / 模态 / 学科吗？跨 STEM 类比（信息论 / 统计物理 / 控制论 / 进化 / 博弈）。
3. **推到极限**：某个超参 / 规模 / 约束推到极端会发生什么相变？
4. **卡位**：画 2D 卡位图，把 idea + 最近的对手 + 候选变体点上去，找空白点。
5. 产出 2-3 个延展变体，每个回到模式 0 重新 normalize，再用模式 1 的致命门快速筛一遍。

---

## 4. 文献接地（按需联网）

新颖性标了 `needs-literature-search` 的，**必须联网**才能下最终结论：

1. WebSearch + 抓近 3 个月论文（query 写明当前年月），围绕 idea 的**核心机制关键词**搜，不是宽泛领域词。
2. 永远不凭记忆给 arXiv 编号 —— 先搜到真实链接再引用，格式 `[作者, 年份, arXiv:编号或 URL]`。
3. 三种结论之一明确告诉用户：**已被做过**（找差异化或转向）/ **部分相关**（定位真正增量）/ **没搜到对手**（提醒可能是新坑也可能没人觉得值得做，想清 why-now）。
4. 关键事实 ≥2 独立来源，冲突时同时呈现并标注。

---

## 输出格式

单个 idea：
```text
模式 / 决策目标:
Idea card:
多视角审核:
  - field expert:
  - method expert:
  - experiment expert:
  - hostile prior-art reviewer:
10 维打分 + 加权总分:
新颖性状态: searched / partially-known / needs-literature-search
致命风险:
可修复弱点 + fixability:
优化后的 problem / mechanism / contribution / 证据包:
延展变体（含致命门快筛）:
文献接地结论:
推荐: accept-to-develop / revise / pivot / abandon / needs-literature-search
confidence:
```

多个 idea：先全部 normalize，再**按"扣除致命风险后"的潜力排序**（不是按平均分），输出排名 + 分数表 + 各自致命风险 + 最值得做的那个 + 该放弃/转向的。

## 反模式（绝对不做）

- ❌ 编造文献 / 结果 / baseline / reviewer 反应 / 新颖性证据
- ❌ 单评审（只用一个视角）
- ❌ 把"低新颖"和"未搜索新颖"混为一谈
- ❌ 没联网就断言一个 idea 是新的
- ❌ 在 idea 还模糊时就帮用户美化措辞（先优化 idea，再谈写作）
- ❌ root challenge 停留在"现有方法效果差"
