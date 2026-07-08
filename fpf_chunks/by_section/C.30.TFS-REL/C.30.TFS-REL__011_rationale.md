---
chunk_kind: "child"
pattern_id: "C.30.TFS-REL"
pattern_title: "Architecture Transformation-Flow Structure Relation"
section_id: "C.30.TFS-REL:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TFS-REL/C.30.TFS-REL__011_rationale.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "C.30.TFS-REL — Architecture Transformation-Flow Structure Relation"
  - "C.30.TFS-REL:10 — Rationale"
line_start: 58160
line_end: 58165
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.0"
  - "A.6.5"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.32"
  - "C.32.P2S"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "E.18.2"
  - "F.18"
  - "G.6"
keywords:
  - "architecture structural view"
  - "architecture-to-transformation-flow relation"
  - "candidate architecture input"
  - "functional behavior"
  - "selected structure"
  - "transformation-flow structure"
---

### C.30.TFS-REL:10 - Rationale

E.18 is the governing FPF pattern for selected transformation-flow structures, paths, crossings, flow valuations, and related pins. Architecture needs to use that work without letting it become generic architecture ontology. The smallest stable relation is therefore a C.30-side record that points to E.18 objects and states admissible and non-admissible architecture use.

This pattern also protects functional architecture. A functional structure view may correspond to a transformation-flow structure, and in some cases both may refer to the same selected `U.StructureRef`; that identity is not automatic. The relation is useful precisely because it preserves the difference while allowing correspondence or positive co-reference.

