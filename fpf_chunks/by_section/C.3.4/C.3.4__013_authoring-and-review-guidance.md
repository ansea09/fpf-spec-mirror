---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:11"
section_title: "Authoring and Review Guidance"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__013_authoring-and-review-guidance.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:11 — Authoring and Review Guidance"
line_start: 44245
line_end: 44266
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

### C.3.4:11 - Authoring and Review Guidance

An adaptation card may show its declaration designator, base kind, effective scheme, pinned base-signature and declaration editions, adaptation type, intended use, candidate constraints, bindings, separately routed Scope, applicability, examples, known bridge or correspondence declarations, and a stable-distinction review note when current. A correspondence card shows its source declaration as EntityOfConcern and names target, direction, rule, definedness, loss, and effective scheme. A card represents the declaration; it is not the declaration or another kind.

Rules of thumb:

- Keep candidate conditions small and governed.
- Check ValueKind and applicability before the three-valued judgment.
- Put claim-scope conditions in Scope, not kind identity.
- Treat locality as a comparison cue. Require a bridge only for distinct kinds with an obtaining correspondence.
- If several teams reuse one stable conceptual constraint, review whether another kind is warranted; reuse alone establishes none.

Reviewer questions:

1. Are the exact base kind and declaration editions recoverable?
2. Is the type—constraint, vocabulary, or composite—correct?
3. Are candidate conditions, applicability, and ClaimScope separated?
4. Does evaluation distinguish `not-applicable`, `true`, `false`, `unknown`, and guard refusal?
5. On locality change, was kind identity compared before any bridge was claimed?
6. For distinct-kind use, do the bridge predicate, receiving declaration, fresh judgment, any adaptation correspondence, and only justified R consequence remain separate?
7. Does a stable conceptual distinction warrant another kind, or is the declaration sufficient?

