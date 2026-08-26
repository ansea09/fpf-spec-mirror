---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__002_use-this-when.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:0 — Use This When"
line_start: 44137
line_end: 44154
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

### C.3.4:0 - Use This When

Use C.3.4 when a procedure needs a named local way of using an existing kind without claiming another kind. Typical cases include accepting `Vehicle` candidates only when they have ABS, using local spelling `X-Auth` for `AuthHeader`, or combining a candidate constraint with vocabulary bindings.

First identify the base kind, exact `KindSignature` edition, receiving use, and meanings of local names or predicates. Write one declaration for candidate constraints or vocabulary bindings and route claim-scope conditions separately. Check candidate and slice admissibility, then evaluate one candidate. Stop with the declaration and first reproducible result. If the distinction becomes a stable kind, identify it separately and establish any obtaining `U.SubkindOf` fact under C.3.1.

Do not use C.3.4 merely to rename a kind, represent a catalog row, narrow claim scope, or avoid deciding whether another kind is needed. A vocabulary-only change adds no candidate predicate. `not-applicable`, `unknown`, and a guard refusal are different results.

**Depends on.**

- **C.3.1 — U.Kind and U.SubkindOf:** kind identity follows the membership distinction; `U.SubkindOf` facts form a preorder and kinds carry no Scope.
- **C.3.2 — Kind intent, admissibility, judgment, and extension:** `KindSignature` is a declaration episteme; admissibility precedes the three-valued judgment.
- **C.3.3 — KindBridge and CL^k:** a directional correspondence only between independently identified distinct kinds, plus R-only bridge consequences.
- **A.2.6 — Context slices and Scopes:** Claim and Work scope over `U.ContextSlice`.
- **C.2.2 and C.2.3:** F–G–R and formality characterize the episteme being assessed.

**Non-goals.** This pattern mandates no repository or notation. A kind-use adaptation declaration is not a governance tier, data policy, mini-type system, kind, `KindBridge`, or Scope.

