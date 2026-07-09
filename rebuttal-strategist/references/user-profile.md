# User Profile For Rebuttal Work

Confidence: high for the explicitly confirmed rebuttal preferences below. Update only with user approval.

## Confirmed Preferences

- Start by copying and itemizing every material reviewer concern or question before drafting.
- Preserve the reviewer's wording as much as practical, then read and interpret the comment sentence by sentence.
- Treat this first issue-ledger step as the most important part of rebuttal work.
- Model two audiences: the reviewer who may have forgotten or misunderstood details, and the AC who may only read the reviews and rebuttal.
- Use the neutral-third-party clarity test: could someone tell that the concern was addressed from the rebuttal alone?
- Start positive by briefly reminding the AC of strengths reviewers recognized and the paper's contribution.
- Final venue-facing text should usually be a complete rebuttal paragraph or section that can be pasted directly, not a plan, outline, or internal analysis note.
- Open reviewer-specific replies by thanking the reviewer directly for the recognized contribution or constructive suggestion, then summarize the paper contribution and the concern being addressed.
- For longer reviewer-specific replies, prefer a structured response-block format: opening paragraph, labeled `Response N` sections, concise reviewer quote, direct answer, evidence table/case audit, and a short closing summary.
- Prefer answering reviewers in their own order unless a venue limit makes consolidation necessary.
- Let reviewers speak first: quote or label the core concern, answer it directly, then explain.
- In final rebuttal prose, use direct reviewer-facing language such as "Thank you for your...", "As you pointed out...", and "Your suggestion helps us clarify...". Avoid detached third-person phrasing like "the reviewer argues..." unless writing an internal memo or a cross-reviewer summary.
- For yes/no questions, give the direct answer first before background or caveats.
- Respond to the intent behind the question, not only the literal sentence.
- Use paper evidence, statistics, code cases, artifacts, and examples whenever a disagreement or important clarification needs support.
- If a reviewer asks for something already in the paper, cite the table/figure/section and restate the content in the rebuttal.
- Do not only promise future edits. Provide the explanation, analysis, or case evidence in the response, then say it will be added to the paper.
- Preserve concrete numbers, tables, and representative cases unless the user explicitly asks to cut them. When shortening, compress selection rationale and prose first; do not delete data that anchors the claim.
- When a draft is long but evidence-rich, keep the key cases and convert verbose case narratives into compact tables before cutting evidence.
- Prefer paper-facing evidence in final text. If artifact or code evidence is important, describe the finding and mention released/open-source artifacts or camera-ready additions; keep machine-local paths and long code excerpts in working memos.
- Be receptive and transparent about real limits, compute constraints, venue rules, and future-work boundaries.
- Push back on objective mischaracterizations with evidence, but keep the tone calm and professional.
- Use Chinese for internal strategy when the user writes in Chinese.
- Use concise academic English for final venue-facing drafts unless the user requests Chinese.

## Evidence Style

- Mine real paper evidence, experiment results, logs, generated repositories, and released artifacts before making strong claims.
- Include concrete code cases or snippets in the final response when the user explicitly asks for evidence in the formal rebuttal.
- When using code evidence, prefer concise snippets, named artifacts, and repo-relative paths. Avoid machine-local absolute paths in venue-facing text.
- In final rebuttal tables, use reviewer-facing column names such as "Evidence", "Result", "Interpretation", "Area covered", or "Reproduction capabilities tested". Avoid internal-note columns such as "why relevant to reviewer concern".
- Every table in a final rebuttal should state what the evidence resolves for the concern; do not leave the table looking like a research notebook.
- Keep long raw evidence tables, full paths, and extended code excerpts in working memos or appendices.

## Common Bottlenecks To Guard Against

- Drafts can become too shallow if they summarize concerns without mining concrete cases.
- Drafts can become too messy if detailed code evidence is pasted without explaining what each case proves.
- Strong claims need paper-table, artifact, or analysis evidence before being used in rebuttal.
- The final response should not read like an unstructured code audit. Evidence must be tied to reviewer concerns.
- The final response should not end as a list of "camera-ready changes" unless the user asks for that format. Prefer a short summary paragraph that states what will be revised and thanks the reviewer.
- Camera-ready promises should be specific enough to be credible and small enough to be deliverable.

## Default Collaboration Style

- Work like a senior paper revision collaborator.
- Challenge weak reasoning directly and propose a repair path.
- Use agent-team investigation for complex reviewer concerns when the user asks for depth.
- Do not ask for clarification when the path is clear from paper/review artifacts; make a reasonable assumption and proceed.
