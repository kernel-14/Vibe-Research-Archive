# Example Result: diffusion-idea

真实产物路径：

```text
artifacts/hypotheses/hypothesis_critic_disagreement.json
artifacts/experiments/STATUS.md
artifacts/final_idea.md
```

运行结果摘录：

```json
{
  "id": "critic-disagreement-as-signal",
  "core_claim": "Structured disagreement among diverse critics is a better selection signal for open-ended research tasks than a single scalar judge score.",
  "challenged_premise": "A single judge can approximate research quality well enough for selection.",
  "measurable_prediction": "Ideas selected by disagreement-pattern analysis produce fewer shared fatal flaws under later independent review.",
  "experiment_design": {
    "setup": "Generate candidate ideas, review them with three critic profiles, compare single-score selection vs. disagreement-pattern selection.",
    "success_criterion": "The disagreement-selected set has fewer unanimous-fatal-flaw reviews in a held-out critic pass.",
    "estimated_time": "<=2h"
  }
}
```
