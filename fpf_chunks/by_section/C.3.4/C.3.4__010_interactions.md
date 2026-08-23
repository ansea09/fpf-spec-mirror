---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:8"
section_title: "Interactions"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__010_interactions.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:8 — Interactions"
line_start: 44292
line_end: 44312
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

### C.3.4:8 - Interactions

#### C.3.4:8.1 - With Kinds and Subkinds

Use an adaptation declaration for procedural tailoring. If the criterion becomes conceptual and stable, identify another local kind and establish the exact obtaining `U.SubkindOf` relation. Repeated declaration use, promotion language, and a catalog link do not establish that relation.

#### C.3.4:8.2 - With Judgment and Declarations

- The base `KindSignature` episteme supplies the kind criterion and its own F.
- The separate adaptation declaration supplies additional candidate-feature constraints or vocabulary bindings and may have its own F.
- The exact `KindUseAdaptationJudgment` pins both editions and preserves `unknown`; neither formality value belongs to the kind, candidate, or truth value.
- An optional extension-like result remains only a pinned-edition representation of true adaptation judgments.

#### C.3.4:8.3 - With KindBridge

A locality change first prompts kind-identity comparison. When the same base kind continues, select the receiving signature and adaptation declaration and evaluate a fresh candidate result without a `KindBridge`. When two independently identified kinds are distinct and an exact directional correspondence is relied on, establish the C.3.3 `KindBridge`, its assertion, the receiving declaration, and any needed adaptation-correspondence declaration. Only justified bridge penalties affect R; F, G, admissibility, and classification truth remain unchanged.

#### C.3.4:8.4 - With Guards

`Guard_KindUseAdaptation` designates exact adaptation and base-signature editions, checks admissibility, evaluates an admissible candidate, checks Scope separately, and keeps `not-applicable`, `unknown`, and refusal distinct. For distinct-kind cross-local use, it composes with the C.3.3 guard only after the bridge and receiving declarations are recoverable. For same-kind reuse, it performs the fresh receiving evaluation without inventing a bridge.

