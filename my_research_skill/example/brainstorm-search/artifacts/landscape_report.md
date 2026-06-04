# Research Landscape: Diffusion View of Agentic Workflow Optimization

## 1. Origin

把 diffusion 的逐步去噪视角迁移到 agentic workflow 优化：能否把一次 research / coding / planning workflow 看作从 noisy proposal 到 clean artifact 的 iterative denoising process？

本报告只做 landscape survey，不设计实验，不声称假设已验证。

## 2. Search Map

### 2.1 Cross-Domain Analogies

- **Diffusion sampling**：每一步不是重新生成，而是在当前状态上去掉一部分噪声。对应 agent workflow 中的 revise / critique / retrieve / re-rank。
- **Control theory**：critic feedback 像 closed-loop controller；关键问题是误差信号是否稳定、是否滞后、是否过度修正。
- **Evolutionary search**：多个 candidate artifact 并行演化，selection signal 决定哪些分支继续扩展。
- **Scientific peer review**：开放研究没有 ground truth，靠不同偏置的 reviewers 暴露不同 failure modes。

### 2.2 Challenged Premises

| Premise | Why questionable | Research consequence |
| --- | --- | --- |
| More agent steps are better | 后续步骤可能引入 drift 或 overfitting to critic | 需要 stop criterion |
| One judge score is enough | 单一 judge 共享生成器盲点 | 需要 diverse critic disagreement |
| Self-refinement improves by default | 已有研究显示 self-correction 不稳定 | 需要外部 evidence / tool signal |
| Debate reveals truth | 多 agent 可能互相强化错误叙事 | 需要 disagreement pattern，而非流畅辩论 |

### 2.3 Emerging Connections

- Test-time compute scaling 与 agent workflow 的共同问题：预算不是越多越好，而是要分配给最有信息增益的分支。
- Process supervision 与 workflow trace evaluation 接近：评价中间 artifact，而非只评价最终答案。
- Retrieval-augmented workflows 可以作为“evidence store”，让 critic 不只评价文本流畅度。

### 2.4 Methodological Transfers

- **Denoising schedule**：从 coarse critique 到 fine critique，避免早期过拟合细节。
- **Annealed selection**：早期保留多样性，后期提高筛选强度。
- **Uncertainty-triggered branching**：只有 critic disagreement 高时才展开更多分支。
- **Process reward model**：把每轮 revision 的局部改善当作训练信号。

### 2.5 Negative Results & Limitations

- Self-refinement 常受限于模型无法发现自己的错误。
- Multi-agent debate 可能增加说服力而不是正确性。
- Critic 输出如果不绑定证据，会变成风格偏好。
- Workflow traces 很长，评价成本可能超过生成成本。

## 3. Promising Research Directions

1. **Disagreement as denoising signal**：用 critic disagreement 的结构决定下一步修正方向。
2. **Evidence-grounded critic routing**：critic 必须引用 evidence store 中的证据，否则 review 不计入选择信号。
3. **Adaptive workflow stopping**：当新增 critic 不再带来新的 fatal flaw，停止扩展。

## 4. Foundational Literature Map

| Dimension | Must-read |
| --- | --- |
| Reasoning traces | Chain-of-Thought Prompting, Self-Consistency |
| Step evaluation | Let's Verify Step by Step |
| Search over thoughts | Tree of Thoughts |
| Agentic workflow risk | self-refine / debate / multi-agent evaluation literature |
| Diffusion analogy | denoising diffusion probabilistic models and sampling schedules |

## 5. Synthesis

“Diffusion view of agent workflows”最有价值的地方不是把 diffusion 术语搬过来，而是强迫 workflow 设计回答三个问题：

1. 当前 artifact 的 noise 是什么？
2. 哪个 critic / tool 能观测到这种 noise？
3. 这一步 revision 是否真的降低了 noise，而不是换了一种表述？

## 6. Research Entry Points

- 先复现一个小型 workflow：generate proposal -> 3 critics -> revise -> final report。
- 记录每轮 critic 的 fatal flaw 类型。
- 比较三种 selection：single judge score、majority vote、disagreement-pattern routing。
- 观察哪种方式最少产生共享 fatal flaw。

## 7. Open Questions

- Disagreement 是 signal 还是 noise，取决于 critic 是否足够独立。
- 证据引用能否防止 critic hallucination。
- 开放研究任务的“clean artifact”是否可以定义为“没有独立 critic 能指出 fatal flaw”。
