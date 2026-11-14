---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency between FPF Families"
section_id: "E.5.3:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__003_problem.md"
commit_sha: "2aea46c8a8ad57c56a81423184fd0d2e19d19cca"
heading_path:
  - "E.5.3 — Unidirectional Dependency between FPF Families"
  - "E.5.3:2 — Problem"
line_start: 101874
line_end: 101877
dependencies:
  - "E.4"
  - "E.5"
keywords:
---

### E.5.3:2 - Problem
A Core pattern can become dependent on a tutorial or helper feature introduced for a local need. Changes to that feature then require reconsidering Core content even when its conceptual subject is unchanged. A cycle prevents the layers from being revised independently and violates **P-5 FPF Layering**.


