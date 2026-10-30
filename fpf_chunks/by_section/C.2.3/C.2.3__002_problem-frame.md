---
chunk_kind: "child"
pattern_id: "C.2.3"
pattern_title: "Formality of an Episteme"
section_id: "C.2.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.3/C.2.3__002_problem-frame.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.2.3 — Formality of an Episteme"
  - "C.2.3:1 — Problem frame"
line_start: 52674
line_end: 52679
dependencies:
  - "A.16"
  - "A.18"
  - "A.19"
  - "B.3"
  - "C.19.2"
  - "C.2"
  - "C.2.2"
  - "C.2.4"
  - "C.2.7"
  - "C.2.LS"
  - "C.39"
  - "F.9"
keywords:
  - "Formality assessment"
  - "expression properties"
  - "language-state separation"
  - "local ordinal scale"
  - "partial order"
  - "proof"
  - "specification"
---

### C.2.3:1 - Problem frame

Use this when a reader, engineer or researcher must decide whether an expression is precise enough to interpret, compute with, combine or check, or what formalization would make that use possible. A research hypothesis, interface specification, controller model, decision policy and formal proof can all need this judgement, but they need different properties of expression.

The first useful move is to name the expression and the operation it must support. A reviewer may need unambiguous acceptance conditions; an interpreter needs an execution rule; a proof checker needs a statement and derivation in its admitted calculus. This assessment identifies the needed repair without requiring a more elaborate formalism for every task. Use an already sufficient expression directly. Readability alone is a different question; truth, empirical support, organizational approval and permission to act retain their own grounds.

