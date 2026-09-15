---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency"
section_id: "E.5.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__002_problem-frame.md"
commit_sha: "368bb772285d22b29eaaf20180500f49f1a2c9d7"
heading_path:
  - "E.5.3 — Unidirectional Dependency"
  - "E.5.3:1 — Problem frame"
line_start: 80090
line_end: 80096
dependencies:
  - "E.4"
  - "E.5"
keywords:
  - "Core"
  - "Pedagogy"
  - "Tooling"
  - "acyclic"
  - "architecture"
  - "dependency"
  - "layers"
  - "modularity"
---

### E.5.3:1 - Problem frame
FPF separates artefacts into stable **Conceptual Core**, executable
**Tooling Reference**, and fast‑evolving **Pedagogical Companion** (see
E.4 FPF Ecosystem Family Architecture).  If dependencies can point *both* ways,
volatile layers will eventually drag the Core into rapid revision
cycles or introduce domain‑specific bias.

