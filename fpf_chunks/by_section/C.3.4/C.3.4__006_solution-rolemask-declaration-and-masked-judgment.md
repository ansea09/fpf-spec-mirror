---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "RoleMask — Contextual Adaptation of Kinds (without cloning)"
section_id: "C.3.4:5"
section_title: "Solution — RoleMask declaration and masked judgment"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__006_solution-rolemask-declaration-and-masked-judgment.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "C.3.4 — RoleMask — Contextual Adaptation of Kinds (without cloning)"
  - "C.3.4:5 — Solution — RoleMask declaration and masked judgment"
line_start: 44469
line_end: 44490
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

### C.3.4:5 - Solution — RoleMask declaration and masked judgment

A `RoleMask` is a named, versioned C.2.1 declaration episteme. Its exact `EntityOfConcern` is the base local kind used by the named procedure or role, while its claim content designates:

1. the exact base kind and pinned base `KindSignature` edition;
2. the named receiving use and mask type: constraint, vocabulary, or composite;
3. additional direct candidate-feature predicates, when any;
4. vocabulary or notation bindings;
5. the exact `U.ContextSlice` conditions and dependencies under which evaluation is defined;
6. any context expectations routed separately to USM Scope; and
7. the intended guard use and the declaration episteme's own `U.Formality`, when current.

For classification, evaluate:

`J_mask(candidate, kind, kindSignatureEdition, roleMaskEdition, slice) ∈ {true, false, unknown}`

The masked judgment is the three-valued conjunction of the base C.3.2 judgment and every additional direct candidate-feature predicate: it is `false` when the base judgment or any added predicate is known `false`; it is `true` only when the base and every added predicate are known `true`; otherwise it is `unknown` because a required component cannot settle or the candidate is outside its evaluation domain. A vocabulary-only mask adds no predicate and therefore preserves the base judgment exactly. A guard may decline use on `unknown`; that refusal is not a `false` classification.

An optional `RoleMaskExtension(roleMaskEdition, kindSignatureEdition, slice)` may represent the candidates whose exact masked judgment is `true`, with both declaration editions pinned. It is not `U.EntitySet`, an A.14 membership occurrence, a new kind, or a direct classification relation. Context conditions such as jurisdiction, API version, and time remain USM Scope predicates and do not become candidate features.

A stable conceptual refinement may justify a separately identified local kind plus an obtaining C.3.1 `U.SubkindOf` relation. The RoleMask declaration itself never creates that kind or relation.

