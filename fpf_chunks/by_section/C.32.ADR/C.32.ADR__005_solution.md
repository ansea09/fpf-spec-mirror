---
chunk_kind: "child"
pattern_id: "C.32.ADR"
pattern_title: "Architecture Decision Record Projection"
section_id: "C.32.ADR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADR/C.32.ADR__005_solution.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "C.32.ADR — Architecture Decision Record Projection"
  - "C.32.ADR:4 — Solution"
line_start: 65719
line_end: 65760
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

Create `ArchitectureDecisionRecordProjection@Project` from an existing `ArchitectureDecisionRelation@Project` and `ArchitectureDecisionDescription@Project`. If the decision relation is missing, return to `C.32.PAD` before writing the record.

Work in this order:

1. Name the publication carrier and intended readers. The carrier can be a Markdown ADR file, decision memo, trade-study record, engineering change note, certification rationale, design-review record, or another typed file or record.
2. Cite the decision relation and decision description. If the record cannot cite them, draft them first.
3. Choose the smallest record scope that lets intended readers use the decision. Avoid copying architecture descriptions or full method descriptions; cite them by value where possible.
4. Map section functions to headings or carrier slots. Use local headings if needed, but keep the function rows recoverable.
5. Carry the candidate basis. Record candidate options from `C.32` or the reason no candidate-set question is live. Do not invent options in the ADR after the decision.
6. Carry the decision outcome. State the selected architecture option, bounded exception, or supersession relation from PAD.
7. Carry rationale, accepted losses, and consequences. Include architecture-characteristic trade-offs and guardrails, not only benefits.
8. Carry method-use instruction and work split when the decision guides developer work. Cite `A.15`, method descriptions, pattern-use refs, readiness exits, and expected structure effects rather than burying them in prose.
9. Carry confirmation, eval, or violation-detection exits. Use `C.32.ACE`, `C.16`, `A.10`, `B.3`, `A.21`, or governance patterns when those claims are live.
10. Carry publication and source-return boundaries. Use `E.17`, `E.24.PUB`, and `C.30.AD` for publication-face and architecture-description claims.
11. Carry status, supersession, and update conditions. Old records remain useful as history when superseded; the active decision relation tells which one governs current work.

#### C.32.ADR:4.1 - Required section functions

The following section functions are required unless the decision relation states why the function is not live for this record use.

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
| Work split | Architect-owned selected structures, developer-owned refinement, readiness or gate exits, and source-return condition. |
| Confirmation or eval exit | How the decision can be checked, evaluated, monitored, or found violated. |
| Publication boundary | Links to architecture descriptions, views, evidence, assurance, and source material without making the ADR the source object. |

#### C.32.ADR:4.2 - ADR package use

When several records form a package, create a package map that names active, proposed, superseded, and related records. A package map is a publication navigation aid. It does not merge decisions, replace PAD relations, or decide record priority by file order alone.

When one decision changes another, use explicit supersession or amendment links. Do not rewrite history by deleting the old record unless the project has a governed archival policy.

