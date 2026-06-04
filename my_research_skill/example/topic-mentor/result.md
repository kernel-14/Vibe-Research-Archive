# Example Result: topic-mentor

真实产物：

- `test-time-scaling/roadmap.md`

产物摘录：

```markdown
# Roadmap: Test-Time Scaling for LLM Reasoning

主线：普通 prompting -> CoT -> self-consistency -> verifier / process supervision -> search-based reasoning

| # | 节点 | 它解决了上一篇什么问题 | Key idea |
| --- | --- | --- | --- |
| 1 | Chain-of-Thought Prompting | 直接预测答案缺少中间状态 | few-shot examples 中写出自然语言推理链 |
| 2 | Self-Consistency | 单条 CoT 可能碰巧走错路径 | sample 多条 reasoning paths，用最终答案投票 |
| 3 | Process Supervision | outcome reward 无法定位哪一步错 | 对每个中间步骤训练 verifier |
| 4 | Tree of Thoughts | 多条链缺少回溯和规划 | 把 thought 当作搜索节点 |

Stage 1 出口问题：
为什么 self-consistency 必须出现在 CoT 之后？如果没有 CoT，只对最终答案做多采样投票，会少掉什么信息？
```
