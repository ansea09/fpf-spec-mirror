---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:5"
section_title: "Solution — Declaration, Correspondence, and Judgment"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__007_solution-declaration-correspondence-and-judgment.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:5 — Solution — Declaration, Correspondence, and Judgment"
line_start: 45646
line_end: 45669
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

### C.3.4:5 - Solution — Declaration, Correspondence, and Judgment

A `KindUseAdaptationDeclaration` is a named, versioned C.2.1 declaration episteme. Its exact `EntityOfConcern` is the base local kind used by the named procedure. Its claim content states:

1. the exact base kind and pinned base `KindSignature` edition;
2. the named receiving use and adaptation type: constraint, vocabulary, or composite;
3. additional direct candidate-feature predicates, when any;
4. vocabulary or notation bindings;
5. the exact `U.ContextSlice` conditions and dependencies under which evaluation is defined;
6. any context expectations routed separately to A.2.6 Scope; and
7. the intended guard use and the declaration episteme's own `U.Formality`, when current.

For classification, evaluate the declaration-local notation:

`J_kindUse(candidate, kind, kindSignatureEdition, adaptationDeclarationEdition, slice) : KindUseAdaptationJudgment ∈ {true, false, unknown}`

The judgment is the three-valued conjunction of the base C.3.2 judgment and every additional direct candidate-feature predicate. It is `false` when the base judgment or any added predicate is known `false`; it is `true` only when the base and every added predicate are known `true`; otherwise it is `unknown` because a required component cannot settle or the candidate is outside its evaluation domain. A vocabulary-only declaration adds no predicate and preserves the base judgment exactly. A guard may decline use on `unknown`; that refusal does not change the judgment to `false`.

An optional pinned-edition representation may list candidates whose exact `KindUseAdaptationJudgment` is `true`. It pins both declaration editions and the slice. The representation has no family-level constructor name here and is not `U.EntitySet`, an A.14 membership occurrence, a new kind, or a direct classification relation. Context conditions such as jurisdiction, API version, and time remain Scope predicates and do not become candidate features.

When two local adaptation declarations differ in constraint predicates or vocabulary bindings, a separate `KindUseAdaptationCorrespondenceDeclaration : U.Episteme` may state the deterministic correspondence, direction, definedness, and loss between those exact declarations. It neither executes a transformation nor creates a Bridge, representation correspondence, or target truth.

A stable conceptual refinement may justify a separately identified local kind and an obtaining C.3.1 `U.SubkindOf` relation. The adaptation declaration, correspondence declaration, judgment, catalog row, and representation create neither object.

