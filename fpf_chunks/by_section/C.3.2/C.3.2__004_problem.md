---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__004_problem.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:2 — Problem"
line_start: 45024
line_end: 45027
dependencies:
  - "A.14"
  - "A.2.6"
  - "A.6.0"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.3"
  - "C.3.4"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
keywords:
  - "KindExtension representation"
  - "KindSignature declaration episteme"
  - "candidate classification"
  - "local kind"
  - "true/false/unknown"
---

### C.3.2:2 - Problem

The shorthand `MemberOf(e,k,slice)` is unsafe for this problem because readers can take it as an A.14 collection relation, an ontic classification-relation occurrence, a three-valued evaluation, a database lookup, or a guard. Likewise, `U.EntitySet(slice)` makes a set representation look like an admitted entity kind. Deterministic-looking notation then carries the wrong ontology. C.3.2 restores an explicit declaration, a judgment, and an optional representation while leaving candidate identity and direct features with their actual governors.

