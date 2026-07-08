---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:13"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__015_sota-echoing.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:13 — SoTA-Echoing"
line_start: 40874
line_end: 40877
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

### C.3.1:13 - SoTA-Echoing

Formal type systems, ontology engineering, and bounded-context modeling all distinguish a local classification relation from the public ontology or schema governance that may later reuse it. C.3.1 follows that separation: `U.Kind` is a local typed-reasoning value and `U.SubkindOf` is a partial-order claim over those values. Durable FPF U-kind admission needs `E.24.UK` because it carries ontic identity, slot relation, naming, construction, and parsimony obligations that a local subkind order does not carry.

