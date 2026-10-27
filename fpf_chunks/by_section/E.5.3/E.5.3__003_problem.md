---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency between FPF Families"
section_id: "E.5.3:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__003_problem.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "E.5.3 — Unidirectional Dependency between FPF Families"
  - "E.5.3:2 — Problem"
line_start: 94808
line_end: 94811
dependencies:
  - "E.4"
  - "E.5"
keywords:
---

### E.5.3:2 - Problem
A Core pattern can become dependent on a tutorial or helper feature introduced for a local need. Changes to that feature then require reconsidering Core content even when its conceptual subject is unchanged. A cycle prevents the layers from being revised independently and violates **P-5 FPF Layering**.


