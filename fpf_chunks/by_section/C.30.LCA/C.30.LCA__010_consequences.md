---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__010_consequences.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:9 — Consequences"
line_start: 62523
line_end: 62528
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
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "E.17.0"
  - "E.18"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller and plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:9 - Consequences

The gain is a small, usable control-structure output that preserves common architecture language while blocking structure, view, and proof overread. Practitioners can still say `controller`, `plant`, `supervisor`, `feedback`, and `control layer`, but the record shows the exact selected structure, description/view boundary, and direct relations those words carry; generic stratification labels use `C.30.STRAT` first.

The cost is an extra relation or conformance note before downstream reliance. When the claim is only recognition, that cost is small. When it is view membership, safety, stability, evidence, assurance, or gate passage, the cost is appropriate because none was carried by the diagram alone.

