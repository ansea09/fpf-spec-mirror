---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:8"
section_title: "Interactions"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__010_interactions.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:8 — Interactions"
line_start: 45708
line_end: 45728
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

### C.3.4:8 - Interactions

#### C.3.4:8.1 - With Kinds and Subkinds

Use an adaptation declaration for procedural tailoring. If the criterion becomes conceptual and stable, identify another local kind and establish the exact obtaining `U.SubkindOf` relation. Repeated declaration use, promotion language, and a catalog link do not establish that relation.

#### C.3.4:8.2 - With Judgment and Declarations

- The base `KindSignature` episteme supplies the kind criterion and its own F.
- The separate adaptation declaration supplies additional candidate-feature constraints or vocabulary bindings and may have its own F.
- The exact `KindUseAdaptationJudgment` pins both editions and preserves `unknown`; neither formality value belongs to the kind, candidate, or truth value.
- An optional extension-like result remains only a pinned-edition representation of true adaptation judgments.

#### C.3.4:8.3 - With KindBridge

Cross-context use needs an obtaining `KindBridge`, its separate Bridge assertion, the target adaptation declaration, and—when constraints or bindings differ—a separate correspondence declaration. R receives justified penalties while F, G, and the target judgment remain unchanged. If the target constraint is a stable conceptual refinement, consider a target-side local kind and an independently obtaining `U.SubkindOf` relation.

#### C.3.4:8.4 - With Guards

`Guard_KindUseAdaptation` designates the exact adaptation-declaration and base `KindSignature` editions, evaluates `J_kindUse` for the exact candidate and slice, checks A.2.6 Scope separately, and preserves `unknown` when classification cannot settle. For cross-context use, it composes with `Guard_XContext_Typed` only after the `KindBridge`, Bridge assertion, target declarations, and any correspondence declaration are recoverable. The guard applies justified `Phi(CL)` and `Psi(CL^k)` effects to R and then makes its separate use decision; it changes neither F, G, nor classification truth.

