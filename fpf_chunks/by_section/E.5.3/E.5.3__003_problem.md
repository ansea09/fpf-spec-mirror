---
chunk_kind: "child"
pattern_id: "E.5.3"
pattern_title: "Unidirectional Dependency"
section_id: "E.5.3:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.3/E.5.3__003_problem.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "E.5.3 — Unidirectional Dependency"
  - "E.5.3:2 — Problem"
line_start: 59774
line_end: 59779
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

### E.5.3:2 - Problem
*Architectural gravity*: a tutorial or helper script adds a new feature,
Core patterns import it “temporarily,” and within months the supposedly
timeless layer depends on transient assets—breaking Pillar **P‑5
FPF Layering**.

