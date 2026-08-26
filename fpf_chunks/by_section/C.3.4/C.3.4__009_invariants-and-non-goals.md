---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:7"
section_title: "Invariants and Non-goals"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__009_invariants-and-non-goals.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:7 — Invariants and Non-goals"
line_start: 44248
line_end: 44253
dependencies:
  - "A.2.6"
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
  - "F.9"
keywords:
---

### C.3.4:7 - Invariants and Non-goals

- **No Scope leakage.** An adaptation declaration cannot widen or narrow Claim scope G; context conditions are enforced by A.2.6 guards.
- **Identity preservation.** The base kind remains `k`; the declaration does not change its `EntityOfConcern`.
- **Weakest-link unaffected.** Adaptation and correspondence declarations do not alter weakest-link rules on F or R; guards route candidate-feature predicates to the exact judgment and context predicates to Scope.

