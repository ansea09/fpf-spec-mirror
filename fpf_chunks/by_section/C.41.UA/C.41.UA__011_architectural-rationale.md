---
chunk_kind: "child"
pattern_id: "C.41.UA"
pattern_title: "Use a Checklist to Answer Questions and Act on the Results"
section_id: "C.41.UA:10"
section_title: "Architectural Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.41.UA/C.41.UA__011_architectural-rationale.md"
commit_sha: "d325a051ac7b2bb37cd870f90b4ed8b2d0426e58"
heading_path:
  - "C.41.UA — Use a Checklist to Answer Questions and Act on the Results"
  - "C.41.UA:10 — Architectural Rationale"
line_start: 94332
line_end: 94337
dependencies:
  - "A.10"
  - "A.15.1"
  - "C.41"
  - "C.41.OF"
  - "C.41.QC"
  - "C.41.TF"
keywords:
---

### C.41.UA:10 - Architectural Rationale

Question selection and checker qualification happen at different scopes from an answer. Repeating them in every use wastes effort; omitting them when their premises fail produces unsupported certainty. This Method uses adequate supplied criteria and checking means; when either proves inadequate, return the affected question to C.41 or C.41.QC.

Keeping decision and corrective work separate preserves the user's choice to revise a mistaken description.

