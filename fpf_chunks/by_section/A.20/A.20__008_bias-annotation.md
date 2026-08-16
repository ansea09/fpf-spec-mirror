---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Flow Constraint Validity — Eulerian"
section_id: "A.20:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__008_bias-annotation.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.20 — Flow Constraint Validity — Eulerian"
  - "A.20:6 — Bias-Annotation"
line_start: 33704
line_end: 33707
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

### A.20:6 - Bias-Annotation

The pattern constrains *how* CV status and witnesses are carried; it does not encode `GateProfile`-bound thresholds, system-role classification or assignment fit, or channel fit. Those questions sit in GateFit under their direct neighboring governors. This separation keeps GateFit criteria out of mechanism semantics.

