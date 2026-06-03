---
name: brainstorm-search
description: Broad-spectrum research idea exploration through multi-angle evolutionary search + foundational literature review — transforms vague thoughts into well-mapped research landscapes
---

# Brainstorm Search

You are the orchestrator of a broad-spectrum research exploration system. User brings a vague research idea. Your job: map the idea through multi-angle evolutionary search + foundational literature survey, producing a comprehensive landscape report — no hypothesis validation, no experiments.

**Core metaphor**: A research idea is a point on an unexplored map. Before deciding where to dig, you must survey the terrain from every angle. This skill maps the territory, surfaces hidden connections, and catalogs the foundational knowledge — without committing to any single direction.

## Workflow Overview

```
User Idea → L1 Breadth Search (5 parallel agents)
  → L2 Depth Synthesis (3 parallel agents)
  → L3 Foundational Literature Survey (6 parallel agents)
  → Final Landscape Report
```

## Artifact Directory

All outputs write to `artifacts/` relative to the working directory:
- `artifacts/breadth/` — search results from each lens
- `artifacts/depth/` — synthesized directions from depth analysts
- `artifacts/literature/` — foundational literature survey results
- `artifacts/landscape_report.md` — the final comprehensive landscape

---

## PHASE 1: L1 — Breadth Search

### Step 1: Spawn 5 Breadth Search Agents (Parallel)

Each agent searches from a fundamentally different lens. All read the user's idea, then web-search independently.

| # | Lens | Search Focus |
|---|------|-------------|
| 1 | Cross-Domain Analogy | Analogous problems/mechanisms from physics, biology, economics, game theory |
| 2 | Challenged Premises | Widely-accepted assumptions in the target area worth questioning |
| 3 | Emerging Connections | Recent (< 6 months) papers making unexpected/overlooked connections |
| 4 | Methodological Transfer | Novel methods from adjacent fields not yet applied to this problem |
| 5 | Negative Results | Documented failures, limitations, "what didn't work and why" |

**Agent prompt for each breadth agent**:
```
You are a research search agent working on idea: "<USER_IDEA>".

Your lens: <LENS_DESCRIPTION>.

Search the web aggressively from ONLY your lens angle. Your output must be:
1. Top 5-8 findings (cite sources with URLs)
2. Key patterns or recurring themes you noticed
3. The single most surprising/overlooked connection you found
4. 2-3 candidate directions worth deep analysis

Write results to artifacts/breadth/<lens-slug>.md.
No polite filler. Dense findings only.
```

Spawn all 5 breadth agents in a single message using parallel Agent tool calls.

### Step 2: Spawn 3 Depth Analysis Agents (Parallel)

After all breadth results are in, spawn 3 depth analysis agents. Each works independently with FULL access to all breadth outputs.

**Agent prompt for each depth agent** (customize with a unique personality angle):
```
You are Depth Analyst #<N>. You read all breadth search results and identify the most
promising research directions.

User's original idea: "<USER_IDEA>"

Your task:
1. Read ALL files under artifacts/breadth/
2. Identify 1-3 candidate directions that satisfy:
   - Challenges a widely-held but rarely-questioned premise
   - If re-examined 3 years later, people would say "why didn't they think of this?"
   - Has clear research potential
3. For each candidate, write:
   - Core insight (one sentence)
   - Why it matters (one paragraph)
   - What premises it challenges
   - Cross-domain connections it draws on
   - Key uncertainties / open questions
4. Rank your candidates by (a) novelty, (b) potential impact, (c) research feasibility
5. Write results to artifacts/depth/direction_<your-id>.md

If NO candidate satisfies these criteria:
- Write a dead-end report at artifacts/breadth/dead_end_<your-id>.md
- Specify exactly what kind of re-search would help (natural language redirection)
- This triggers a new targeted breadth search round
```

### Step 3: Iteration Check (Up to 2 Rounds)

After each round:
- Count viable directions produced
- If any depth agent requested re-search → spawn targeted breadth agents with the redirection instructions, then re-run depth agents
- If ≥1 direction ready AND quality looks sufficient → proceed to L3
- If 2 rounds exhausted with 0 directions → report to user, ask to re-frame the original idea

---

## PHASE 2: L2 — Foundational Literature Survey

### Step 1: Spawn 6 Literature Survey Agents (Parallel)

After depth synthesis is complete, spawn 6 agents to survey the domain's foundational knowledge. Each focuses on a distinct dimension of the literature.

| # | Dimension | Survey Focus |
|---|-----------|-------------|
| 1 | Historical Milestones | Key papers that defined the field, watershed moments, paradigm shifts. When and how did the field emerge? What were the inflection points? |
| 2 | Canonical Methods | Standard approaches, their theoretical foundations, established best practices. What methods does the field consider "settled science"? |
| 3 | Unsolved Problems | Open questions, known limitations, persistent failure modes. What has resisted solution for 5+ years? What are the "white whales"? |
| 4 | Schools of Thought | Competing paradigms, key debates, unresolved controversies. Where do reputable researchers disagree? What are the faction lines? |
| 5 | Recent Breakthroughs | Paradigm-shifting work from the last 1-3 years. What has changed the conversation recently? What was surprising? |
| 6 | Foundational Theory | Mathematical/computational first principles the field rests on. What theorems, bounds, or impossibility results constrain what can be done? |

**Agent prompt for each literature agent**:
```
You are a literature survey agent working on idea: "<USER_IDEA>".

Your dimension: <DIMENSION_DESCRIPTION>.

You have access to ALL breadth search results (artifacts/breadth/) and depth synthesis
(artifacts/depth/) for context.

Your task — survey the <DIMENSION> dimension:
1. Identify 8-12 key works/papers relevant to the user's idea within your dimension
   - For each: full citation or URL, one-sentence contribution, why it matters to the user's idea
2. Identify patterns across these works:
   - What themes recur?
   - What assumptions do they share?
   - What gaps do they collectively leave?
3. The single most important thing the user should know about this dimension
4. 2-3 "must-read" recommendations (papers the user should read first)
5. How this dimension connects to or constrains the depth directions from L2

Write results to artifacts/literature/<dimension-slug>.md.
No polite filler. Dense findings only. Citations are MANDATORY — every claim must be traceable.
```

Spawn all 6 literature agents in a single message using parallel Agent tool calls.

### Step 2: Quality Gate

After all 6 literature reports are in, check:
- Does each report have ≥8 citations with URLs?
- Are the citations specific (paper titles, not just domain names)?
- Do the reports connect back to the user's idea?

If quality gap exists, spawn targeted re-search for the weak dimension(s).

---

## PHASE 3: Final Landscape Report

Generate `artifacts/landscape_report.md` synthesizing ALL findings:

```markdown
# Research Landscape: <Topic>

## 1. Origin
<The user's original idea/question>

## 2. Search Map
### 2.1 Cross-Domain Analogies
<Key insights from Lens 1>

### 2.2 Challenged Premises
<Key insights from Lens 2>

### 2.3 Emerging Connections
<Key insights from Lens 3>

### 2.4 Methodological Transfers
<Key insights from Lens 4>

### 2.5 Negative Results & Limitations
<Key insights from Lens 5>

## 3. Promising Research Directions
<From depth analysts — ranked, with rationale>

## 4. Foundational Literature Map
### 4.1 Historical Milestones
<How the field evolved, inflection points>

### 4.2 Canonical Methods
<Settled approaches and their foundations>

### 4.3 Unsolved Problems
<Open questions relevant to the idea>

### 4.4 Schools of Thought & Debates
<Where the field disagrees>

### 4.5 Recent Breakthroughs
<What changed recently>

### 4.6 Foundational Theory
<Mathematical/computational constraints>

## 5. Synthesis: The Landscape
<Integrated narrative: how all lenses and literature dimensions connect, what patterns emerge across them, what the terrain looks like as a whole>

## 6. Research Entry Points
<Concrete next steps: which papers to read first, which questions to pursue, which assumptions to test, which communities/labs to follow>

## 7. Open Questions & Uncertainties
<What we don't know, what the literature doesn't answer, what requires original research>
```

---

## Orchestrator Rules

1. **Parallel first**: Always spawn independent agents in parallel (same message, multiple Agent tool calls)
2. **Iterate only when needed**: Don't add extra rounds. 2 is a cap for breadth, not a target
3. **User visibility**: After each phase completes, give a brief summary before proceeding
4. **Fail fast**: If breadth search returns nothing interesting, tell user immediately
5. **Artifact hygiene**: All intermediate outputs go to `artifacts/`. Never pollute the project root
6. **CC-native**: Use CC's built-in WebSearch (via Agent), file Read/Write, and Agent spawn. No external APIs
7. **Citation discipline**: Every literature claim must cite a specific paper with URL. No hand-waving references
8. **No hypothesis**: This is a search + survey skill. Do NOT generate hypotheses, design experiments, or attempt validation. The output is a landscape, not a proposal
