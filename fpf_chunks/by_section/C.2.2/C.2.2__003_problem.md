---
chunk_kind: "child"
pattern_id: "C.2.2"
pattern_title: "Reliability R in the F–G–R triad"
section_id: "C.2.2:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.2/C.2.2__003_problem.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.2.2 — Reliability R in the F–G–R triad"
  - "C.2.2:2 — Problem"
line_start: 41525
line_end: 41534
dependencies:
  - "A.2.6"
  - "A.21"
  - "B.1.3"
  - "B.3"
  - "B.3.3"
  - "B.3.4"
  - "C.16"
  - "C.2"
  - "C.2.3"
  - "C.21"
  - "C.25"
  - "C.3"
  - "C.3.3"
  - "C.3.A"
  - "E.14"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.9"
  - "G.6"
  - "G.7"
keywords:
  - "Bridge-only reuse"
  - "ClaimScope (G)"
  - "Congruence Level (CL / CL^k / CL^plane)"
  - "F–G–R"
  - "Reliability (R)"
  - "TA/VA/LA lanes"
  - "evidence-bound"
  - "no implicit averaging"
  - "pathwise justification (PathId)"
  - "warrant"
  - "weakest-link"
---

### C.2.2:2 - Problem

FPF needs a reliability coordinate that is:

1. **Auditable.** A reader can trace R to concrete evidence and see how reuse penalties were applied.
2. **Composable.** R can be propagated through claim graphs conservatively, without illegal scale arithmetic.
3. **Orthogonal.** R is not conflated with F (expression) or G (scope).
4. **Bridge-safe.** Any loss from transport across contexts/kinds/planes is explicit and affects **R only**.
5. **Minimal.** The solution does not introduce new core types or new face-kinds.

