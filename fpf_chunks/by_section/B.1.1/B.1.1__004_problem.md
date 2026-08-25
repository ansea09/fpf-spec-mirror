---
chunk_kind: "child"
pattern_id: "B.1.1"
pattern_title: "Dependency Structure and Relation Grounding"
section_id: "B.1.1:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.1/B.1.1__004_problem.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "B.1.1 — Dependency Structure and Relation Grounding"
  - "B.1.1:2 — Problem"
line_start: 34772
line_end: 34781
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15.1"
  - "A.22"
  - "A.6.5"
  - "B.1"
  - "B.1.4"
  - "B.3.5"
  - "C.13"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.AD.BA"
keywords:
---

### B.1.1:2 - Problem

Without B.1.1:

1. **Edge drift spreads.** `ComponentOf`, a collection's belongs-to relation, `PhaseOf`, `SerialStepOf`, `RepresentationOf`, source use, evidence relation, and control relation all become generic graph edges.
2. **Boundary crossing becomes parthood.** A power grid, supplier, teacher, measuring instrument, model, or source record is drawn as a part because it affects the holon.
3. **Design and run objects mix.** Planned structure, design description, actual work occurrence, and telemetry are placed in one dependency expression without a DesignRunTag or a distinction among the patterns that define those claims.
4. **Acyclic graph discipline overclaims.** A graph check says something about the drawing, but the ontology-side relation remains ungrounded.
5. **Mappings become parts.** A digital twin, dashboard, diagram, or architecture description is treated as a constituent of the object it describes.

