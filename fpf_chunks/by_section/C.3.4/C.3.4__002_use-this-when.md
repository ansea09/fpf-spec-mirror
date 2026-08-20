---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__002_use-this-when.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:0 — Use This When"
line_start: 45277
line_end: 45298
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

Use C.3.4 when a procedure needs a named local way of using a well-known kind without claiming a new kind. Typical cases include:

- accepting `Vehicle` candidates only when they have ABS;
- using the local spelling `X-Auth` for `AuthHeader`; and
- combining a local candidate criterion with vocabulary bindings.

First useful move: identify the exact base kind and `KindSignature` edition, name the receiving use, and write one declaration of the local use. Keep candidate features in the declaration and route context conditions separately through A.2.6 Scope. The first useful result is a named declaration plus a reproducible `true | false | unknown` judgment for one candidate. If the local distinction becomes a stable conceptual distinction, stop using this declaration as a substitute for kind admission: identify a separate local kind and establish any obtaining `U.SubkindOf` relation independently.

Do not use C.3.4 merely to rename a kind, represent a catalog row, narrow claim scope, or avoid deciding whether a stable new kind is needed. A vocabulary-only change adds no candidate predicate. A guard refusal is a separate use decision, not a `false` classification.

**Depends on.**

- **C.3.1 — U.Kind and U.SubkindOf:** kinds are intensional, `U.SubkindOf` is a partial order, and kinds carry no Scope.
- **C.3.2 — Kind intent, judgment, and extension:** `KindSignature` is a declaration episteme; the exact candidate judgment is three-valued; an extension is a pinned-edition representation of true candidates.
- **C.3.3 — KindBridge and CL^k:** cross-context kind correspondence and R-only bridge consequences.
- **A.2.6 — Context slices and Scopes:** Claim and Work scope over `U.ContextSlice`.
- **C.2.2 and C.2.3:** F–G–R and formality characterize the episteme being assessed.

**Non-goals.** This pattern mandates no repository or notation. A kind-use adaptation declaration is not a governance tier, data policy, mini-type system, new kind, or Scope. Context conditions remain A.2.6 Scope predicates.

