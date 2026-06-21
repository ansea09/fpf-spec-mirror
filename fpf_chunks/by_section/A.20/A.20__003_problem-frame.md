---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Flow Constraint Validity — Eulerian"
section_id: "A.20:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__003_problem-frame.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.20 — Flow Constraint Validity — Eulerian"
  - "A.20:1 — Problem frame"
line_start: 29215
line_end: 29218
dependencies:
  - "A.19.SelectorMechanism"
  - "A.21"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
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
  - "TransformationFlowStructure"
  - "flow"
---

### A.20:1 - Problem frame

In `E.18`, transformation-flow loci are graph-positioned loci for atomic `U.Transformation` values and transformation-adjacent governed slot fillers, and the graph uses a *single edge kind* (`U.Transfer`). A locus relation may be expressed as a morphism only when the mathematical lens is current; that lens is not the locus kind. **GateFit** checks aggregate only in `OperationalGate(profile)` with the activation predicate **CV => GF**: until aggregated **`CV.Status=pass`**, all **GateFit** checks return **abstain**. Equivalently, while **`CV.Status != pass`**, any GateFit-oriented explanation **does not apply**. To keep flows comparable and auditable, this pattern delimits **internal step constraints** (CV) from **external gate fit** (GF), preventing any second process order beside the graph.

