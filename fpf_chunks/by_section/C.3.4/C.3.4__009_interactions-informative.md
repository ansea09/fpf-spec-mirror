---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "RoleMask — Contextual Adaptation of Kinds (without cloning)"
section_id: "C.3.4:8"
section_title: "Interactions (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__009_interactions-informative.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "C.3.4 — RoleMask — Contextual Adaptation of Kinds (without cloning)"
  - "C.3.4:8 — Interactions (informative)"
line_start: 45087
line_end: 45107
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

### C.3.4:8 - Interactions (informative)

#### C.3.4:8.1 - With Kinds & Subkinds (C.3.1)

Use a RoleMask declaration for procedural tailoring. If the criterion becomes conceptual and stable, identify another local kind and establish the exact obtaining `U.SubkindOf` relation; do not treat mask reuse, promotion language, or a catalog link as that relation.

#### C.3.4:8.2 - With judgment and declarations (C.3.2)

* The base `KindSignature` episteme supplies the kind criterion and its own F.
* The separate RoleMask declaration supplies additional candidate-feature constraints or vocabulary bindings and may have its own F.
* The exact masked judgment pins both editions and preserves `unknown`; neither formality value belongs to the kind, candidate, or truth value.
* Any `RoleMaskExtension` is only a pinned-edition representation of true masked judgments.

#### C.3.4:8.3 - With KindBridge (C.3.3)

Cross-context use needs an obtaining KindBridge relation, its separate bridge assertion, the target RoleMask declaration, and—when constraints or aliases change—a separate MaskAdapter declaration episteme. R receives the justified penalties while F, G, and the target judgment remain unchanged. If the target constraint is a stable conceptual refinement, consider a target-side local kind and an independently obtaining `U.SubkindOf` relation.

#### C.3.4:8.4 - With guards (Annex C.3.A)

`Guard_MaskedUse` designates the exact RoleMask and base KindSignature editions, evaluates `J_mask` for the exact candidate and slice, checks USM Scope separately, and preserves `unknown` when the classification cannot settle. For cross-context use, it composes with `Guard_XContext_Typed` only after the KindBridge relation, bridge assertion, target declarations, and any MaskAdapter declaration are recoverable. The guard applies justified `Phi(CL)` and `Psi(CL^k)` effects to R and then makes its separate use decision; it changes neither F, G, nor classification truth.

