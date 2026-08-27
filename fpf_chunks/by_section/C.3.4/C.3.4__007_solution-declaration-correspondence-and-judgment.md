---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:5"
section_title: "Solution — Declaration, Correspondence, and Judgment"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__007_solution-declaration-correspondence-and-judgment.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:5 — Solution — Declaration, Correspondence, and Judgment"
line_start: 44960
line_end: 44987
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

### C.3.4:5 - Solution — Declaration, Correspondence, and Judgment

A `KindUseAdaptationDeclaration` is a named, versioned C.2.1 declaration episteme about one local use. The base kind is its `EntityOfConcern`; its effective scheme gives meaning to declaration names and predicates. Its claim content states:

1. the exact base kind and pinned base `KindSignature` edition;
2. the receiving use and adaptation type: constraint, vocabulary, or composite;
3. additional directly governed candidate conditions, when any;
4. vocabulary or notation bindings;
5. exact candidate and slice applicability plus dependencies;
6. scope expectations routed separately through A.2.6; and
7. intended guard use and this declaration episteme's formality, when current.

First evaluate adaptation admissibility. A candidate rejected by the base signature's ValueKind, an adaptation-specific candidate requirement needed merely to form the question, or the declared slice applicability is `not-applicable`; no adaptation judgment is formed. For an admissible request, use:

`J_kindUse(candidate, kind, kindSignatureEdition, adaptationDeclarationEdition, slice) ∈ {true, false, unknown}`

The judgment conjoins the base C.3.2 judgment with every added candidate-condition predicate. A known `false` gives `false`; all known `true` gives `true`; unresolved required facts give `unknown`. A vocabulary-only declaration adds no predicate and preserves the base judgment. A guard may decline use on `not-applicable` or `unknown` without rewriting either.

An optional pinned-edition representation may list admissible candidates judged `true`. It is not `U.EntitySet`, A.14 membership, another kind, or a direct classification relation. Scope conditions stay under A.2.6 rather than becoming kind identity.

When a use moves to another practice, source, or team, compare the base-kind membership distinctions first:

- if the same kind continues, use the declaration and signature edition selected for the receiving use and make a fresh receiving judgment; no `KindBridge` exists merely because locality changed;
- if independently identified kinds are distinct and the use claims a directional correspondence, establish the C.3.3 `KindBridge`; use the receiving signature and adaptation declaration and make a fresh receiving judgment; and
- if two adaptation declarations differ in constraints or bindings, a separate `KindUseAdaptationCorrespondenceDeclaration` may name source declaration as EntityOfConcern and state target, direction, deterministic rule, definedness, loss, and effective scheme. It creates no bridge or target truth.

A stable conceptual refinement may justify another kind and an obtaining C.3.1 subkind fact. A declaration, correspondence, judgment, catalog row, or representation creates neither.

