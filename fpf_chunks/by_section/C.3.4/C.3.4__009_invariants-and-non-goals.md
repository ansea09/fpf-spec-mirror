---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Tailor the Use of an Existing Kind"
section_id: "C.3.4:7"
section_title: "Invariants and Non-goals"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__009_invariants-and-non-goals.md"
commit_sha: "a9845e2c1029313e518c91a459ff7fab39e2831e"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Tailor the Use of an Existing Kind"
  - "C.3.4:7 — Invariants and Non-goals"
line_start: 58564
line_end: 58569
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

- **No Scope leakage.** A constraint adaptation adds a test of candidate features. A vocabulary-only adaptation binds a local name and preserves the base judgement. Each declaration identifies the slices in which its constraint or vocabulary binding applies. A separate claim has its own scope G under A.2.6. To use the declarations as models and claim strict refinement, compare them for the same inquiry under B.5.MR. An additional condition already implied by the base criterion can leave every answer unchanged.
- **Identity preservation.** The base kind remains `k`; the declaration does not change its `EntityOfConcern`.
- **Aggregation unaffected.** Adaptation and correspondence declarations do not change the applicable F rule under C.2.3 or the justified support-composition model or non-aggregate synthesis under C.2.2; guards route candidate-feature predicates to the adaptation judgment and context predicates to Scope.

