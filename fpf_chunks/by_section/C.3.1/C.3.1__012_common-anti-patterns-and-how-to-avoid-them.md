---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:10"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:10 — Common Anti-Patterns and How to Avoid Them"
line_start: 41830
line_end: 41837
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.8"
  - "C.2.3"
  - "C.3"
  - "C.3.2"
  - "C.3.3"
  - "E.24.UK"
  - "F.5"
  - "F.8"
keywords:
  - "kind"
  - "partial order"
  - "subkind"
  - "type hierarchy"
---

### C.3.1:10 - Common Anti-Patterns and How to Avoid Them

* Encoding dependency, part-whole, slot filling, construction, or admission as `U.SubkindOf`.
* Treating a source "type" hierarchy as a public FPF U-kind hierarchy.
* Storing claim scope on `U.Kind` instead of on the claim or capability.
* Treating `U.SubkindOf` as the relation that admits dependent durable U-kinds.
* Using public `U.*` spelling before `E.24.UK` and naming patterns admit it.

