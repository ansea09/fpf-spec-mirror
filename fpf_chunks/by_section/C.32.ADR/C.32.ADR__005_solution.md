---
chunk_kind: "child"
pattern_id: "C.32.ADR"
pattern_title: "Architecture Decision Record Projection"
section_id: "C.32.ADR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADR/C.32.ADR__005_solution.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "C.32.ADR — Architecture Decision Record Projection"
  - "C.32.ADR:4 — Solution"
line_start: 79467
line_end: 79508
dependencies:
  - "A.10"
  - "A.15"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32.ADA"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.11.PUR"
  - "E.17"
  - "E.24.PUB"
  - "E.8"
keywords:
  - "ADR projection"
  - "ArchitectureDecisionDescription@Project"
  - "ArchitectureDecisionRecordProjection@Project"
  - "architecture decision record"
  - "consequences"
  - "method-use instruction"
  - "publication boundary"
  - "rationale"
  - "section function"
  - "supersession"
---

### C.32.ADR:4 - Solution

Publish the recoverable decision and its description for the declared readers. If the decision content is missing, develop it through `C.32.PAD`; the same written account can support that work and later describe its result. A draft or template does not establish that a decision was made.

Work in this order:

1. Name the publication carrier and intended readers. Use a file or other carrier for the Markdown ADR, decision memo, trade-study record, engineering change note, certification rationale, design-review record, or other decision-description form.
2. Make the decision relation and its description recoverable by reference or by value. If either remains unresolved, develop the missing content and keep the draft's status truthful.
3. Choose the smallest scope that lets intended readers use the decision. Include the explanatory slice they need, with access to the fuller architecture or Method description when needed; avoid duplicating material that adds no useful content.
4. Choose headings or carrier positions that make the needed decision functions recoverable. A separate mapping table is useful only when the relationship would otherwise be unclear.
5. Carry the candidate basis. Record candidate options from `C.32` or the reason no candidate-set question is live. Do not invent options in the ADR after the decision.
6. Carry the decision outcome. State the selected architecture option, bounded exception, or supersession relation from PAD.
7. Carry rationale, accepted losses, and consequences. Include architecture-characteristic trade-offs and guardrails, not only benefits.
8. Carry Method-use instructions and work split when the decision guides developer work. State the required action and expected structure effect plainly; cite the Method, pattern-use guidance or readiness rule when the reader needs it.
9. Carry confirmation, eval, or violation-detection exits. Use `C.32.ACE`, `C.16`, `A.10`, `B.3`, `A.21`, or governance patterns when those claims are live.
10. Carry the applicable publication and source-return boundaries. Use `E.24.PUB` for publication occurrences and audience availability, `E.17` when a source-backed face and source return are needed, and `C.30.AD` for architecture-description claims.
11. Carry status, supersession, and update conditions. Old records remain useful as history when superseded; the active decision relation tells which one governs current work.

#### C.32.ADR:4.1 - Required section functions

Select the following functions by the declared reader use, retaining what is needed to understand, apply, check or reconsider the decision. Explain a consequential omission when the reader could otherwise infer a missing option, instruction or confirmation. The table does not require a heading or an omission statement for every inapplicable function.

| Section function | What the record must let the reader recover |
|---|---|
| Identity and status | Record id, title, status, date or version, relation to superseded or superseding records. |
| Problem frame and decision question | The bounded architecture question, described holon, context, and current reader use. |
| Forces and architecture characteristics | The architecture characteristics, constraints, concerns, and trade-offs that made the decision nontrivial. |
| Candidate options | Candidate options, rejected options, bounded exception, or stated reason no candidate-set question is live. |
| Decision outcome | The selected architecture option and affected selected structures. |
| Rationale | Why this outcome is acceptable now, including accepted losses and protected guardrails. |
| Consequences | Expected effects on structures, methods, teams, costs, risks, evidence, operation, and later change. |
| Method-use instruction | Required style, pattern use, method description, or work practice, when the decision changes developer work. |
| Work split | Prospective allocation or instruction content through the plan, policy, commitment, permission, decision, responsibility, authority, or other direct relation that actually states it; otherwise the exact missing governor. Also show readiness or gate exits and the source-return condition. Professional titles are audience cues, not ownership predicates. |
| Confirmation or eval exit | How the decision can be checked, evaluated, monitored, or found violated. |
| Publication boundary | Links to architecture descriptions, views, evidence, assurance, and source material without making the ADR the source object. |

#### C.32.ADR:4.2 - ADR package use

When readers need navigation among several records, provide a package map or an adequate existing index that identifies active, proposed, superseded and related records. A package map is a publication navigation aid. It does not merge decisions, replace PAD relations, or decide record priority by file order alone.

When one decision changes another, use explicit supersession or amendment links. Do not rewrite history by deleting the old record unless the project has a governed archival policy.

