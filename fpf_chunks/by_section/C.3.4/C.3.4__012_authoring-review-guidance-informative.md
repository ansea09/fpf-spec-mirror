---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "RoleMask — Contextual Adaptation of Kinds (without cloning)"
section_id: "C.3.4:11"
section_title: "Authoring & Review Guidance (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__012_authoring-review-guidance-informative.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "C.3.4 — RoleMask — Contextual Adaptation of Kinds (without cloning)"
  - "C.3.4:11 — Authoring & Review Guidance (informative)"
line_start: 45509
line_end: 45529
dependencies:
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
keywords:
  - "RoleMask declaration episteme"
  - "candidate-feature constraint"
  - "masked judgment"
  - "stable-refinement review"
  - "vocabulary binding"
---

### C.3.4:11 - Authoring & Review Guidance (informative)

#### C.3.4:11.1 - Authoring a RoleMask card

**Publication fields (suggested).** A card or catalog row may represent the RoleMask declaration's designator, base kind, pinned kind-signature edition, declaration edition, type, intended use, candidate-feature constraints, separately routed Scope expectations, bindings, definedness, examples, known bridge/adapter declarations, and any stable-distinction review note. The card is not the declaration episteme or a new ontic object.
**Rules of thumb.**

* Keep entity predicates **small and testable**.
* Put context predicates in Scope, not in the masked classification criterion.
* If several teams reuse the same stable conceptual constraint, review whether a separately identified local kind and an obtaining `U.SubkindOf` relation are warranted; mask reuse itself establishes neither.

#### C.3.4:11.2 - Reviewer 7‑point checklist

1. Mask **registered** and **versioned**?
2. **Type** declared correctly (constraint/vocabulary/composite)?
3. Entity vs context **split** respected?
4. **Determinism** (no “latest”) satisfied?
5. Does the guard route context to USM, evaluate the exact three-valued masked judgment for the candidate, and keep refusal separate?
6. Does every cross-context use recover the KindBridge relation and assertion, target declarations, any MaskAdapter episteme, target `J_mask`, and only the justified R penalties?
7. Is declaration consolidation sufficient, or does a stable conceptual distinction warrant a separately identified local kind and independently obtaining subkind relation?

