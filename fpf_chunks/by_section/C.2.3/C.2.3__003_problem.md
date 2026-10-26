---
chunk_kind: "child"
pattern_id: "C.2.3"
pattern_title: "Formality of an Episteme"
section_id: "C.2.3:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.3/C.2.3__003_problem.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.2.3 — Formality of an Episteme"
  - "C.2.3:2 — Problem"
line_start: 52172
line_end: 52179
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

### C.2.3:2 - Problem

“More formal” can hide several different changes. A document can acquire a clear structure without fixing its ambiguous terms. A precise specification can be non-executable. An executable program can omit the property its user needs established. A checked proof in one logic need not become stricter when translated into another logic. Ranking these changes on one ladder can reject adequate work and reward an irrelevant change of notation or tool.

Composition adds a further difficulty. Several precisely expressed claims can be connected by an informal inference. Their presence does not make that whole argument a formal derivation. Conversely, an informal observation used as empirical evidence does not make the separately stated mathematical claim less precisely expressed. Without an explicit assessed expression and support relation, “the least formal part” can refer to the wrong object.

The practical problem is therefore to establish which expression properties the receiving operation needs, which are present, which must change and how those properties survive combination or translation.

