---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Loop"
section_id: "B.2.5:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Loop"
  - "B.2.5:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 31494
line_end: 31503
dependencies:
  - "A.1"
  - "A.12"
  - "A.15"
  - "A.2"
  - "A.3"
  - "A.7"
  - "B.2"
  - "C.30.LCA"
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
| Loop proves safety | The loop is treated as evidence, assurance, gate, or safety proof. | Keep the loop relation and apply the exact governing pattern for the live claim kind. |

