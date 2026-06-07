# Idea Intake — 把粗糙 idea 规整成卡片

idea 粗糙、欠定义、散在几个 bullet 里，或要比较多个候选时用本文件。

## 采集字段

收集或推断：

```text
目标场景 / 受众:
领域与子领域:
原始 idea:
最接近的已知工作:
可用数据 / 代码 / 算力:
预期方法成分:
预期证据:
时间线与资源约束:
非目标（不做什么）:
```

字段未知时从方法和场景名推断；目标场景未知时假设一个通用顶会目标，并把场景相关建议标为低 confidence。

## 规整后的 idea card

优化前先把每个 idea 转成下面结构：

```text
Task / 现象:
Gap:
Root challenge:
Core insight:
Proposed mechanism:
Contribution type:
Expected evidence:
Why now:
Main risk:
Best venue fit:
```

硬规则：root challenge 只是"现有方法效果差"时，细化成具体的技术 / 科学 / 实证 / 人因 / 系统瓶颈。

## 缺失输入标签（别猜，用标签）

- `needs-literature-search`：最接近的工作未知，或方向更新快。
- `needs-feasibility-check`：数据 / 算力 / 实现复杂度 / 时间线不清。
- `needs-domain-constraint`：真实场景 / 威胁模型 / 用户群 / 负载没定义。
- `needs-evidence-design`：claim 比实验计划清楚（不知怎么验）。
- `needs-venue-selection`：idea 也许不错，但受众还不明显。

## 多 idea 规整

多个草稿时，**先全部 normalize，再比较**，不要过早优化第一个。排序依据：

1. 问题-方法契合最强；
2. 扣除可能的 prior art 后新颖性最站得住；
3. 证据可行性最好；
4. 受众 / 场景契合最好；
5. 一轮现实迭代后致命风险最少。
