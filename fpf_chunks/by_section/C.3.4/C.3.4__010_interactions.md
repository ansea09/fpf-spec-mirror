---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Tailor the Use of an Existing Kind"
section_id: "C.3.4:8"
section_title: "Interactions"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__010_interactions.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Tailor the Use of an Existing Kind"
  - "C.3.4:8 — Interactions"
line_start: 58634
line_end: 58654
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

Use an adaptation declaration for procedural tailoring. If the receiving uses need a stable conceptual distinction as a kind, identify it under C.3.1 and establish any claimed `U.SubkindOf` relation. Repeated declaration use or a catalog link does not establish that relation.

#### C.3.4:8.2 - With Judgment and Declarations

- The base `KindSignature` episteme supplies the kind criterion and its own F.
- The separate adaptation declaration supplies additional candidate-feature constraints or vocabulary bindings and may have its own F.
- The `KindUseAdaptationJudgment` pins both editions and preserves `unknown`; neither formality assessment belongs to the kind, candidate, or truth value.
- An optional extension-like result remains only a pinned-edition representation of true adaptation judgments.

#### C.3.4:8.3 - With KindBridge

A locality change first prompts kind-identity comparison. When the same base kind continues, select the receiving signature and adaptation declaration without a `KindBridge`; establish any candidate judgment under the receiving declaration using KUA-09. When two independently identified kinds are distinct and an exact directional correspondence is relied on, establish the C.3.3 `KindBridge`, its assertion, the receiving declaration, and any needed adaptation-correspondence declaration. Only justified bridge penalties affect R; F, G, admissibility, and classification truth remain unchanged.

#### C.3.4:8.4 - With Guards

`Guard_KindUseAdaptation` designates exact adaptation and base-signature editions, checks admissibility, evaluates an admissible candidate, checks Scope separately, and keeps `not-applicable`, `unknown`, and refusal distinct. For distinct-kind cross-local use, it composes with the C.3.3 guard only after the bridge and receiving declarations are recoverable. For same-kind reuse, establish the receiving candidate's status under KUA-09. A prior evaluation can settle it when its grounds still apply. Perform a new receiving evaluation when the commission or the receiving conditions require one.

