---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Relation"
section_id: "B.2.5:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Relation"
  - "B.2.5:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 39199
line_end: 39208
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15.1"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.3.4"
  - "A.6.M"
  - "B.1"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.13"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30.LCA"
  - "G.6"
keywords:
---

### B.2.5:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Ghost coordination | Subholons coordinate, but no supervising acting system, medium, or feedback relation is named. | Fill `SupervisorSubholonFeedbackRelation@Context`; add a system-role kind or assignment only when separately current. |
| Functional layer as component | A planning or control layer is modeled as a physical part of the controlled holon. | Separate parthood from feedback relation; use `C.30.LCA` for the view. |
| Perfect communication | State access is assumed instant, complete, or lossless. | Name medium or publication limits; use `C.27`, `A.3.3`, or evidence-use patterns for timing and information claims. |
| Episteme acts | A theory, model, paper, dashboard, or standard senses, judges, plans, or adapts. | Recover each exact acting System through A.13 and let A.15.1 independently admit the dated revision Work. Add F.6 only when the account expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; F.6 identifies neither assignment nor performer, and missing or failed F.6 leaves the Work intact. A short sentence may omit an unused assignment identifier. Name the Method or review practice structuring the Work when current, and any publication or source-use relation. This Work rule does not make assignment or system-role classification a condition of the supervisor-subholon feedback relation itself. |
| Relation certifies safety | The feedback relation is treated as evidence, assurance, gate, or safety result. | Keep the relation and use the pattern for the stronger claim. |

