---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:11"
section_title: "Authoring and Review Guidance"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__013_authoring-and-review-guidance.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:11 — Authoring and Review Guidance"
line_start: 45465
line_end: 45486
dependencies:
  - "A.2.6"
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
  - "F.9"
keywords:
  - "base KindSignature"
  - "candidate-feature constraint"
  - "correspondence declaration"
  - "kind-use adaptation declaration"
  - "three-valued judgment"
  - "vocabulary binding"
---

### C.3.4:11 - Authoring and Review Guidance

#### C.3.4:11.1 - Authoring a Declaration Card

A card or catalog row may represent the adaptation declaration's designator, base kind, pinned kind-signature edition, declaration edition, type, intended use, candidate-feature constraints, separately routed Scope expectations, bindings, definedness, examples, known Bridge and correspondence declarations, and any stable-distinction review note. The card is not the declaration episteme or a new ontic object.

Rules of thumb:

- Keep candidate predicates small and testable.
- Put context predicates in Scope, not in the adaptation judgment.
- If several teams reuse the same stable conceptual constraint, review whether a separately identified local kind and an obtaining `U.SubkindOf` relation are warranted; declaration reuse establishes neither.

#### C.3.4:11.2 - Reviewer Checklist

1. Is the adaptation declaration durably identified and versioned?
2. Is its type—constraint, vocabulary, or composite—stated correctly?
3. Are candidate features and context conditions separated?
4. Is evaluation deterministic, with no implicit `latest`?
5. Does the guard evaluate the exact three-valued judgment, check Scope separately, and keep refusal distinct?
6. Does every cross-context use recover the `KindBridge`, Bridge assertion, target declarations, any correspondence declaration, target judgment, and only justified R penalties?
7. Is declaration consolidation sufficient, or does a stable conceptual distinction warrant a separately identified local kind and independently obtaining subkind relation?

