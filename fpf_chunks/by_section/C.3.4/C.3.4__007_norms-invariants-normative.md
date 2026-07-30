---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "RoleMask — Contextual Adaptation of Kinds (without cloning)"
section_id: "C.3.4:6"
section_title: "Norms & Invariants (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__007_norms-invariants-normative.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "C.3.4 — RoleMask — Contextual Adaptation of Kinds (without cloning)"
  - "C.3.4:6 — Norms & Invariants (normative)"
line_start: 45510
line_end: 45541
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

### C.3.4:6 - Norms & Invariants (normative)

> The following state RM-01 through RM-10 over the declaration episteme, masked judgment, Scope split, and cross-context adapter boundary.

#### C.3.4:6.1 - Definition and shape

**RM-01 (Definition).** A `RoleMask` SHALL be a named, versioned C.2.1 declaration episteme with exact base kind, pinned `KindSignature` edition, named receiving use, mask type, direct candidate-feature constraints, vocabulary bindings, definedness conditions, intended guard use, and any separately owned Scope expectations. Its formality characterizes this episteme, not the kind or one judgment result.

**RM-02 (Not a new kind).** A RoleMask MUST NOT introduce a new `U.Kind`. If the domain needs a stable conceptual refinement, identify another local kind and establish an obtaining `U.SubkindOf` relation under C.3.1; a catalog row or mask declaration does neither.

**RM-03 (Determinism and three values).** The exact masked judgment MUST be reproducible for fixed candidate, kind, kind-signature edition, RoleMask edition, and slice. It returns `true`, `false`, or `unknown`; implicit `latest` is forbidden and guard refusal does not rewrite `unknown`.

**RM-04 (Mask type).** A declaration SHALL state constraint, vocabulary, or composite. A vocabulary mask preserves the base judgment. Constraint and composite masks use only direct candidate-feature predicates and apply the three-valued conjunction rule: any known `false` conjunct gives `false`, all known `true` conjuncts give `true`, and every other combination gives `unknown`.

#### C.3.4:6.2 - Separation of channels

**RM-05 (Context versus candidate).** Direct governed features of the exact candidate may contribute to `J_mask`. Predicates about ContextSlice, including jurisdiction, standards, environment, and `Gamma_time`, SHALL be enforced through USM Scope. The declaration may cite both, but the guard routes them to different owners and never hides Scope inside classification.

**RM-06 (Guard use).** A guard MAY designate a RoleMask declaration only when its exact edition, base `KindSignature` edition, dependencies, and definedness are recoverable and the required candidate features can be evaluated. A mask name is not a kind synonym. The guard consumes the three-valued masked judgment and makes a separate use decision.

#### C.3.4:6.3 - Stable refinement and catalog representation

**RM-07 (Stable refinement).** When the additional criterion becomes a broadly reused conceptual distinction, review whether another local kind is warranted. If so, identify that kind under C.3/C.3.2 and establish an obtaining `U.SubkindOf` relation under C.3.1. Retire or retain the RoleMask only for its remaining local use; no mask, catalog action, or label performs kind admission.

**RM-08 (Addressability and catalog representation).** Every RoleMask declaration edition used by a guard SHALL have a durable designator or reference that resolves to the exact declaration edition, base `KindSignature` edition, dependencies, definedness, and intended use. A context MAY present those references, constraints, bindings, examples, and bridge/adapter dependencies in a catalog. The catalog row is a representation, not the declaration episteme or a new kind. Consolidation changes the catalog and may motivate a declaration revision; it does not merge kind identities by itself.

#### C.3.4:6.4 - Cross-context use

**RM-09 (Bridge and adapter boundary).** For cross-context masked classification, first establish the obtaining KindBridge relation between the independently identified source and target kinds. Use the target `KindSignature` edition and a target RoleMask declaration. When constraint predicates or vocabulary bindings change, a separate C.2.1 `MaskAdapter` declaration episteme states the deterministic correspondence and loss; it is neither a relation occurrence nor the target judgment. Evaluate the exact target `J_mask`; do not copy the source result. `CL^k` and any scope-bridge consequence affect R only.

**RM-10 (Definedness and fail-closed use).** The RoleMask and any MaskAdapter declarations SHALL each state their definedness. Outside RoleMask definedness, or when its own required evaluation dependency is unavailable, the target masked judgment is `unknown`. Outside MaskAdapter definedness, the adapter correspondence is unavailable and a guard declines the cross-context use without rewriting an independently evaluated target `J_mask`. In both cases fail-closed is a use disposition, not an assertion of `false`.

