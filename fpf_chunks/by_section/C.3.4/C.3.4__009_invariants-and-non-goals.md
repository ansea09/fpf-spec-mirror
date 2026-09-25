---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Tailor the Use of an Existing Kind"
section_id: "C.3.4:7"
section_title: "Invariants and Non-goals"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__009_invariants-and-non-goals.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Tailor the Use of an Existing Kind"
  - "C.3.4:7 — Invariants and Non-goals"
line_start: 51744
line_end: 51749
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
- **Aggregation unaffected.** Adaptation and correspondence declarations do not change the applicable F rule under C.2.3 or the justified support-composition model or non-aggregate synthesis under C.2.2; guards route candidate-feature predicates to the exact judgment and context predicates to Scope.

