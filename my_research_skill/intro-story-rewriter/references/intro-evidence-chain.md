# Introduction Evidence Chain

## Core Chain

Use this chain when revising a technical-paper Introduction:

```
Task need
  -> existing methods work in an important sense
  -> concrete cost/failure remains
  -> evidence for the cost/failure
  -> missing interface or missing measurement
  -> method modules matched to failures
  -> metrics and benchmark
  -> headline result
```

Each arrow must be visible in prose. If the reader must infer an arrow, rewrite.

## Evidence Placement

- Put borrowed evidence in a sentence that names the source:
  "As reported by SWE-Pruner, read actions account for 76.1% of
  Mini-SWE-Agent trajectory tokens."
- Put local evidence in a sentence that names the protocol:
  "We audit 720 Mini-SWE-Agent SWE-QA trajectories and find ..."
- If a figure contains both, say:
  "Panel A reports the prior macro audit; Panel B reports our local trajectory
  audit."

## Good Patterns

### Agent harness paper

```
Code agents need to search repositories before they can answer questions,
verify claims, or make edits. Agentic code search has become effective enough
to support these tasks, but its working cycle remains costly. As reported by
X, read actions account for Y% of trajectory tokens. This cost is paid after
candidate locations are found, when the agent reads, remembers, and decides
when to stop.
```

### Benchmark plus method paper

```
This bottleneck is hard to evaluate with top-k retrieval accuracy, because the
agent is not only retrieving code. It is buying evidence under a token budget.
We therefore define token-efficiency metrics and introduce a benchmark with
hidden evidence units and paid-token accounting.
```

## Rewrite Traps

- Do not write "the full search cycle can consume many tokens" when a concrete
  reported number exists.
- Do not write "repository search is cheap" when the claim is about agentic
  search cost. The safer claim is that candidate finding and candidate reading
  are different parts of the loop.
- Do not use "repository search" as the main noun if the paper studies a base
  agent plus tools, memory, and stopping. Use "agentic code search" or
  "agentic repository search".
- Do not describe a local audit before explaining what it is diagnosing.
- Do not present a benchmark before the reader understands the missing metric.
