---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__003_problem.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:2 — Problem"
line_start: 61397
line_end: 61402
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
  - "E.18.2"
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

### C.30.LCA:2 - Problem

Control diagrams are persuasive because they look operational: arrows imply feedback, boxes imply responsibility, and recovered control-layer labels imply separation. In practice that is often enough for orientation, but not enough to identify selected structure, make direct relations obtain, admit the description as `U.View`, or establish architecture adequacy. A control-stack description can quietly overclaim stability, safety, evidence sufficiency, gate validity, assurance, or causality; a non-control `layer`, `level`, `tier`, or `stack` label belongs first to `C.30.STRAT`.

FPF needs a pattern that preserves useful recognition without letting the cue become structure, relation, or proof. Direct control relations, their participant meanings, feedback relations, externality boundaries, and rate separations can enter an architecture structural description. The same episteme is a view only through viewpoint conformance. Systems, local kinds, separate System-classification judgments, assignments, Methods, and Work are optional neighboring facts; use the relevant patterns to state or test authority, responsibility, safety, stability, gates, evidence, assurance, and causal effects.

