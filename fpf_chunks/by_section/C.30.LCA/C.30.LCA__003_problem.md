---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__003_problem.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:2 — Problem"
line_start: 52333
line_end: 52338
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
  - "C.30.TGA-FLOW-REL"
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

### C.30.LCA:2 - Problem

Control diagrams are persuasive because they look operational: arrows imply feedback, boxes imply responsibility, and layer labels imply separation. In practice that is often enough for orientation, but not enough to make the architecture claim admissible. A control-stack description can quietly overclaim that stability, safety, evidence sufficiency, gate validity, assurance, or causality has already been established.

FPF needs a pattern that preserves the useful recognition of control architecture without letting the recognition cue become a proof. The control roles, feedback relations, externality boundaries, and rate separations belong in an architecture structural view. Claims about dynamics, temporal adequacy, causal use, evidence, assurance, gates, or mathematical lens transfer belong in the exact governing pattern that governs that claim kind.

