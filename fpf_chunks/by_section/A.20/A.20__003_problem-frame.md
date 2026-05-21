---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "U.Flow.ConstraintValidity — Eulerian"
section_id: "A.20:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__003_problem-frame.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.20 — U.Flow.ConstraintValidity — Eulerian"
  - "A.20:1 — Problem frame"
line_start: 27098
line_end: 27101
dependencies:
  - "A.19.SelectorMechanism"
  - "A.21"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "E.TGA"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
keywords:
  - "ConstraintValidity"
  - "Eulerian"
  - "GateFit"
  - "MVPK"
  - "PathSlice"
  - "Sentinel"
  - "SquareLaw"
  - "TransductionFlow"
  - "flow"
---

### A.20:1 - Problem frame

In E.TGA, *nodes = morphisms* and the graph uses a *single edge kind* (`U.Transfer`). **GateFit** checks aggregate only in `OperationalGate(profile)` with the activation predicate **CV ⇒ GF**: until aggregated **ConstraintValidity = pass**, all **GateFit** checks return **abstain**. Equivalently, while **ConstraintValidity ≠ pass**, any GateFit‑oriented explanation **does not apply**. To keep flows comparable and auditable, this pattern delimits **internal step constraints** (CV) from **external gate fit** (GF), preventing any second process order beside the graph.

