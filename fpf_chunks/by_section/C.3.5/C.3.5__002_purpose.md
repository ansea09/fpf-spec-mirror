---
chunk_kind: "child"
pattern_id: "C.3.5"
pattern_title: "KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
section_id: "C.3.5:1"
section_title: "Purpose"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.5/C.3.5__002_purpose.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "C.3.5 — KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
  - "C.3.5:1 — Purpose"
line_start: 45547
line_end: 45558
dependencies:
  - "A.2.6"
  - "C.2.2"
  - "C.2.3"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.4"
  - "C.3.A"
keywords:
  - "K0-K3"
  - "KindAT"
  - "assurance planning"
  - "declaration planning"
  - "editorial facet"
---

### C.3.5:1 - Purpose

Teams need a quick answer to a planning question: is this local kind intended as a curated instance-like cohort, a behavioral pattern, a formal invariant-bearing kind, or a kind considered up to structural equivalence? The answer can guide where declaration rigor and assurance effort are likely to pay off without pretending that abstraction itself widens scope, raises formality, settles classification, or increases reliability.

KindAT gives that planning vocabulary while keeping the governing objects separate:

- the local kind and its order remain under C.3/C.3.1;
- the `KindSignature` remains a declaration episteme whose own `U.Formality` may change;
- `J(candidate, kind, signatureEdition, slice)` remains `true`, `false`, or `unknown`;
- any `KindExtension` remains a pinned-edition representation of true candidates; and
- bridge and mask objects retain the ontology assigned by C.3.3 and C.3.4.

