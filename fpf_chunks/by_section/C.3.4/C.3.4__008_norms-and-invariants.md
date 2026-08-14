---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:6"
section_title: "Norms and Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__008_norms-and-invariants.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:6 — Norms and Invariants"
line_start: 45371
line_end: 45402
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

### C.3.4:6 - Norms and Invariants

The following norms apply to the declaration epistemes, three-valued judgment, Scope split, and cross-context correspondence boundary.

#### C.3.4:6.1 - Definition and Shape

**KUA-01 (Definition).** A `KindUseAdaptationDeclaration` SHALL be a named, versioned C.2.1 declaration episteme with exact base kind, pinned `KindSignature` edition, named receiving use, adaptation type, direct candidate-feature constraints, vocabulary bindings, definedness conditions, intended guard use, and Scope expectations stated separately under the applicable scope rule. Its formality characterizes this episteme, not the kind or one judgment result.

**KUA-02 (Not a new kind).** A declaration MUST NOT introduce a new `U.Kind`. If the domain needs a stable conceptual refinement, identify another local kind and establish an obtaining `U.SubkindOf` relation under C.3.1; a catalog row or declaration does neither.

**KUA-03 (Determinism and three values).** `KindUseAdaptationJudgment` MUST be reproducible for a fixed candidate, kind, kind-signature edition, adaptation-declaration edition, and slice. It returns `true`, `false`, or `unknown`; implicit `latest` is forbidden and guard refusal does not rewrite `unknown`.

**KUA-04 (Adaptation type).** A declaration SHALL state constraint, vocabulary, or composite. A vocabulary declaration preserves the base judgment. Constraint and composite declarations use only direct candidate-feature predicates and apply the three-valued conjunction rule: any known `false` conjunct gives `false`, all known `true` conjuncts give `true`, and every other combination gives `unknown`.

#### C.3.4:6.2 - Separation of Channels

**KUA-05 (Context versus candidate).** Direct governed features of the exact candidate may contribute to `J_kindUse`. Predicates about `U.ContextSlice`, including jurisdiction, standards, environment, and `Gamma_time`, SHALL be enforced through A.2.6 Scope. The declaration may cite both, but a guard routes them separately and never hides Scope inside classification.

**KUA-06 (Guard use).** A guard MAY designate a `KindUseAdaptationDeclaration` only when its exact edition, base `KindSignature` edition, dependencies, and definedness are recoverable and the required candidate features can be evaluated. A declaration name is not a kind synonym. The guard consumes the three-valued judgment and makes a separate use decision.

#### C.3.4:6.3 - Stable Refinement and Catalog Representation

**KUA-07 (Stable refinement).** When an additional criterion becomes a broadly reused conceptual distinction, review whether another local kind is warranted. If so, identify it under C.3 and C.3.2 and establish any obtaining `U.SubkindOf` relation under C.3.1. Retire or retain the adaptation declaration only for its remaining local use; no declaration, catalog action, or label performs kind admission.

**KUA-08 (Addressability and catalog representation).** Every adaptation-declaration edition used by a guard SHALL have a durable designator or reference that resolves to its exact edition, base `KindSignature` edition, dependencies, definedness, and intended use. A context MAY present those references, constraints, bindings, examples, and cross-context dependencies in a catalog. The catalog row represents the declaration; it is neither the declaration episteme nor a new kind. Consolidation changes the catalog and may motivate a declaration revision, but it does not merge kind identities.

#### C.3.4:6.4 - Cross-Context Use

**KUA-09 (Bridge and correspondence boundary).** For cross-context adapted classification, first establish the obtaining `KindBridge` relation between independently identified source and target kinds. Use the target `KindSignature` edition and a target `KindUseAdaptationDeclaration`. When constraint predicates or vocabulary bindings differ, a separate `KindUseAdaptationCorrespondenceDeclaration` states deterministic correspondence and loss between the exact declaration endpoints. It is not the Bridge occurrence, Bridge assertion, executable adapter, mapping Method, representation correspondence, or target judgment. Evaluate the target `KindUseAdaptationJudgment`; do not copy the source result. `CL^k` and any scope-bridge consequence affect R only.

**KUA-10 (Definedness and fail-closed use).** Each adaptation declaration and correspondence declaration SHALL state its definedness. Outside an adaptation declaration's definedness, or when its required evaluation dependency is unavailable, the target judgment is `unknown`. Outside the correspondence declaration's definedness, that correspondence is unavailable and a guard declines the cross-context use without rewriting an independently evaluated target judgment. In both cases fail-closed is a use disposition, not an assertion of `false`.

