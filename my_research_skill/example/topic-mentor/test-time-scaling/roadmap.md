# Roadmap: Test-Time Scaling for LLM Reasoning

## 主线

普通 prompting 只能让模型直接吐答案；CoT 先让模型把中间推理外显；self-consistency 用多条推理路径投票降低单路径偶然性；verifier / process supervision 开始评估推理过程本身；Tree-of-Thoughts / search-based reasoning 把“多想一会儿”变成显式搜索；现代 test-time compute scaling 则研究怎样把额外推理预算分配给最值得搜索的分支。

## 关键节点

| # | 节点 | 它解决了上一篇什么问题 | Key idea | 仍留下的问题 |
| --- | --- | --- | --- | --- |
| 1 | Chain-of-Thought Prompting, Wei et al. 2022, arXiv:2201.11903 | 直接预测答案缺少中间状态，复杂数学/符号任务容易跳错 | few-shot examples 中写出自然语言推理链，让大模型先推理再回答 | CoT 是否 faithful；单条推理链不稳定 |
| 2 | Self-Consistency, Wang et al. 2022, arXiv:2203.11171 | 单条 CoT 可能碰巧走错路径 | sample 多条 reasoning paths，用最终答案一致性投票 | 投票只看答案，不知道哪条过程更可靠 |
| 3 | Process Supervision / Step Verifier, Lightman et al. 2023, OpenAI | outcome reward 只能评价最终答案，无法定位哪一步错 | 对每个中间步骤训练 verifier，奖励过程正确性 | step label 成本高；verifier 也可能被分布外推理欺骗 |
| 4 | Tree of Thoughts, Yao et al. 2023, arXiv:2305.10601 | 采样多条链仍是扁平枚举，缺少回溯和规划 | 把中间 thought 当作搜索节点，结合 generation、evaluation、selection | 搜索代价高；评估函数决定上限 |
| 5 | Test-Time Compute Scaling / Best-of-N / search allocation | “多采样”不是预算最优分配 | 把推理预算当资源，研究什么时候继续展开、什么时候停止 | 如何在开放任务上定义可泛化的 verifier signal |

## 已掌握节点

- CoT 的核心不是“解释给人看”，而是给模型生成中间状态的 token 空间。
- Self-consistency 是 test-time compute 的最早实用形态之一：多采样换稳定性。
- Verifier 把“多想”从 blind sampling 推向 guided search。

## 仍模糊节点

- CoT faithfulness：模型写出的推理是否等价于内部因果机制。
- Verifier generalization：训练在数学步骤上的 verifier 能否迁移到开放研究任务。
- Compute allocation：预算应该平均分配给候选，还是集中给高潜力分支。

## 费曼测试问题

在进入下一阶段前，回答这个问题：

> 为什么 self-consistency 必须出现在 CoT 之后？如果没有 CoT，只对最终答案做多采样投票，会少掉什么信息？

## 推荐阅读顺序

1. Wei et al., 2022, Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, https://arxiv.org/abs/2201.11903
2. Wang et al., 2022, Self-Consistency Improves Chain of Thought Reasoning in Language Models, https://arxiv.org/abs/2203.11171
3. Lightman et al., 2023, Let's Verify Step by Step, https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf
4. Yao et al., 2023, Tree of Thoughts: Deliberate Problem Solving with Large Language Models, https://arxiv.org/abs/2305.10601
