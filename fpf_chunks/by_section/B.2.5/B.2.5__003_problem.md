---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Loop"
section_id: "B.2.5:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__003_problem.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Loop"
  - "B.2.5:2 — Problem"
line_start: 30835
line_end: 30844
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

### B.2.5:2 - Problem

Layered supervision is useful across engineered, biological, organizational, and epistemic cases, but it is easy to model incorrectly. The common error is to collapse three different structures into one drawing:

1. Structural composition: part-whole or structural composition of a holon.
2. Supervisory relation: a `Transformer` or transformer-bearing system playing a supervisor role over one or more subordinate holons.
3. Interaction or publication network: observation, signal, command, constraint, report, review, or publication channels through which the loop is enacted or supported.

When these are confused, a functional or supervisory layer is treated as a physical part, a publication is treated as an acting agent, a diagram is treated as proof, or a controller label is treated as a gate or assurance result.

