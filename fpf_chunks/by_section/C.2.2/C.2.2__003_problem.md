---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__003_problem.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:2 — Problem"
line_start: 54730
line_end: 54738
dependencies:
  - "A.2.6"
  - "A.21"
  - "B.1.3"
  - "B.3"
  - "C.16"
  - "C.2"
  - "C.2.3"
  - "C.21"
  - "C.3"
  - "C.3.3"
  - "C.3.A"
  - "E.14"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.2"
  - "G.6"
  - "G.7"
keywords:
  - "ClaimScope (G)"
  - "Congruence Level (CL / CL^k / CL^plane)"
  - "F–G–R"
  - "Reliability (R)"
  - "TA/VA/LA lanes"
  - "direct relation"
  - "evidence-bound"
  - "pathwise justification (PathId)"
  - "qualitative synthesis"
  - "support dependencies"
  - "warrant"
  - "weakest-link limits"
---

### C.2.2:2 - Problem

FPF needs a reliability coordinate that is:

1. **Auditable.** A reader can recover the grounds for the supported conclusion, the argument connecting them to this claim and use, and the effect of actual reuse limitations.
2. **Composable.** Support can be combined under its warranted meanings and dependencies without illegal scale arithmetic; where no numerical aggregate is justified, the separate contributions remain usable.
3. **Orthogonal.** R is not conflated with F (expression) or G (scope).
4. **Relation-aware.** Any loss declared by an actual scope-translation, kind, plane, notation, source-local, model-use, or evidence-reuse relation is explicit and affects **R only**.

