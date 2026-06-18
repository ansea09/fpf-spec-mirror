---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__010_consequences.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:9 — Consequences"
line_start: 54567
line_end: 54572
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
  - "C.30.ASV"
  - "C.30.LCA"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "E.18"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller/plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:9 - Consequences

The gain is a small, usable control-structure output that preserves common architecture language while blocking proof overread. Practitioners can still say `controller`, `plant`, `supervisor`, `feedback`, and `control layer`, but the record shows what those words carry; generic stratification labels use `C.30.STRAT` before they are allowed to enter this pattern.

The cost is an extra relation note before downstream reliance. When the claim being made is only recognition, that cost is small. When the claim being made is safety, stability, evidence, assurance, or gate passage, the cost is appropriate because those claims were never carried by the diagram alone.

