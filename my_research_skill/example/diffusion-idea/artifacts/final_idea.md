# Diffusion Idea: Critic Disagreement as Selection Signal

## 1. Origin

The starting idea was to use multi-critic disagreement patterns as a reward or selection signal for research-agent workflows where no ground-truth answer exists.

## 2. Evolution Path

The idea evolved from “replace judge score with critics” into a stricter mechanism:

1. Generate multiple candidate artifacts.
2. Review each artifact with critics that have explicitly different biases.
3. Encode each review as structured findings: fatal flaw, uncertainty, evidence gap, suggested revision.
4. Select artifacts not by average score, but by the pattern of agreement and disagreement.
5. Revise only the parts that critics can connect to evidence or a clear logical failure.

## 3. Final Structured Hypothesis

Structured disagreement among diverse critics is a better open-ended selection signal than a single scalar judge score, because it exposes which weaknesses are shared, which are critic-specific, and which parts of an idea survive independent attacks.

## 4. Experimental Evidence

This example run produced a structured hypothesis and a first-round critic status board:

- `artifacts/hypotheses/hypothesis_critic_disagreement.json`
- `artifacts/experiments/STATUS.md`

The simulated critic panel converged on one robust weakness: critic independence is the core risk. That is a useful result because it identifies the next experiment rather than merely giving the idea a high or low score.

## 5. The Idea Story

The diffusion analogy is useful only if “noise” is made concrete. In this workflow, noise means unresolved fatal flaws, unsupported claims, and overconfident leaps. Critics are not oracles; they are noise detectors with biased sensors. The signal is therefore not critic agreement alone, but the structure of where they agree and disagree.

## 6. Next Steps

1. Build a small artifact schema for critic reviews.
2. Generate 12 candidate ideas from one seed.
3. Compare single-score selection with disagreement-pattern selection.
4. Run a held-out critic pass and count unanimous fatal flaws.
5. Treat critic independence as the first ablation.
