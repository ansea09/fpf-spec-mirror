---
chunk_kind: "child"
pattern_id: "C.3.5"
pattern_title: "KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
section_id: "C.3.5:1"
section_title: "Purpose"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.5/C.3.5__002_purpose.md"
commit_sha: "169e3e09c04a4174ce4c26682cf181a0d255b6f7"
heading_path:
  - "C.3.5 — KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
  - "C.3.5:1 — Purpose"
line_start: 58531
line_end: 58544
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

Teams need a quick answer to a planning question: is this local kind intended as a curated instance-like cohort, a behavioral pattern, a formal invariant-bearing kind, or a kind considered up to structural equivalence? The answer can guide where declaration rigor and assurance effort are likely to pay off. An ordinary description of those planning needs is sufficient when a shared tag adds no useful distinction.

KindAT records how one local kind is treated for catalogue and planning work. Comparing the levels of abstraction of two models requires a shared inquiry and interpretation (B.5.MR). Suppose one-day and three-day schedules both satisfy a service policy. A revised model keeps the earlier commitments and limits the interval to at most two days. If the one-day schedule is still feasible, the three-day schedule shows which previously possible answer the model excludes. The kind of service order can keep the same K tag throughout.

Use the governing objects for their respective decisions:

- the local kind and its order remain under C.3/C.3.1;
- the `KindSignature` remains a declaration episteme whose expression properties may change under C.2.3;
- for an admissible request, `J(candidate, kind, signatureEdition, slice)` remains `true`, `false`, or `unknown`;
- any `KindExtension` remains a pinned-edition representation of true candidates; and
- bridge and kind-use adaptation objects retain the ontology assigned by C.3.3 and C.3.4.

