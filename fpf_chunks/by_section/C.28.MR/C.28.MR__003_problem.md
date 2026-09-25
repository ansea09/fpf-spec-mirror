---
chunk_kind: "child"
pattern_id: "C.28.MR"
pattern_title: "Derive an Intervention Consequence by Mechanism Replacement"
section_id: "C.28.MR:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28.MR/C.28.MR__003_problem.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "C.28.MR — Derive an Intervention Consequence by Mechanism Replacement"
  - "C.28.MR:2 — Problem"
line_start: 63907
line_end: 63914
dependencies:
  - "A.3.3.TR"
  - "B.5.MPC"
  - "B.5.RR"
  - "C.28"
  - "C.29.1"
keywords:
---

### C.28.MR:2 - Problem

An observed value tells us something about how the existing mechanisms operated. An intervention changes a mechanism. Conditioning on the observed value can therefore answer a different question from imposing that value.

A second difficulty appears when a mathematical or software operation has an unclear physical interpretation. Assigning a value to an indicator, replacing a controller and forcing a physical quantity can change different mechanisms. Reusing the same variable name hides that difference.

Even a clearly specified replacement can change the solvability of a model or its subsequent dynamics. The useful result requires both the model transformation and a derivation for the question actually asked.

