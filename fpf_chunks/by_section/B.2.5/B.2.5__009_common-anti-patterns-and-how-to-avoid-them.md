---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Loop"
section_id: "B.2.5:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Loop"
  - "B.2.5:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 32224
line_end: 32233
dependencies:
  - "A.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.3"
  - "A.3.4"
  - "A.7"
  - "B.2"
  - "C.30.LCA"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "control architecture"
  - "feedback loop"
  - "layered control"
  - "stability"
  - "supervisor"
---

### B.2.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Ghost coordination | Subholons coordinate, but no supervisor role, shared medium, or feedback relation is named. | Name supervisor role, acting transformer, observation/report side, and influence/constraint side. |
| Functional layer as component | A planning or control layer is modeled as a physical part of the controlled holon. | Separate structural composition from supervisory relation. |
| Perfect communication | The loop assumes instant, complete, or lossless access to subholon state. | Add interaction/publication medium limits and assign timing or information claims to `C.27`, `A.3.3`, or evidence claim. |
| Episteme acts | A theory, model, paper, or dashboard senses, judges, plans, or adapts. | Name the acting system, operator, review practice, or revision practice; keep the episteme as described or revised object. |
| Loop proves safety | The loop is treated as evidence, assurance, gate, or safety proof. | Keep the loop relation and apply the governing pattern for the claim kind being made. |

