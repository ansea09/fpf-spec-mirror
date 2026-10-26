---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__010_consequences.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:9 — Consequences"
line_start: 73375
line_end: 73380
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.3"
  - "B.2.5"
  - "B.3"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.LCA"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.32.LCA"
  - "E.17.0"
  - "E.18"
  - "E.18.2"
  - "G.6"
keywords:
  - "control-structure view"
  - "controller"
  - "feedback closure"
  - "layered control architecture"
  - "observer"
  - "plant"
  - "rate band"
  - "supervisor"
---

### C.30.LCA:9 - Consequences

The gain is a small, usable control-structure output that preserves common architecture language while blocking structure, view, and proof overread. Practitioners can still say `controller`, `plant`, `supervisor`, `feedback`, and `control layer`, but the record shows the selected structure, the boundary between description and view, and the direct relations those words carry; generic stratification labels use `C.30.STRAT` first.

The cost is recovering missing control facts or checking the conformance or property on which the use depends. Reuse an adequate existing account. Recognition can finish with an ordinary sentence; view membership, safety, stability, evidence, assurance or gate passage requires its own applicable basis.

