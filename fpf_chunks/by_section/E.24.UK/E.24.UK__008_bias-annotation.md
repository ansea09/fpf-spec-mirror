---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Admission and Ontic Settlement"
section_id: "E.24.UK:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__008_bias-annotation.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "E.24.UK — U-kind Admission and Ontic Settlement"
  - "E.24.UK:6 — Bias-Annotation"
line_start: 85957
line_end: 85960
dependencies:
  - "A.11"
  - "A.3.2"
  - "A.6.0"
  - "A.6.3"
  - "A.6.5"
  - "A.6.REL"
  - "A.8"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10"
  - "E.17.0"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "F.18"
  - "U.MethodDescription"
  - "U.View"
  - "U.Viewpoint"
keywords:
---

### E.24.UK:6 - Bias-Annotation

This pattern blocks punctuation-bias and taxonomy-bias. A `U.*` spelling, title, filename, table row, or imported type word is not enough to create a durable FPF kind. Recover the governed individuals, their direct governing pattern, and their identity or membership rule first. When the candidate instead names participation in a relation, a SlotSpec, an assertion or description field, a selected `U.Structure`, an `E.24.PUB` form, or a `C.29` representation element, retain that exact object and its governing pattern. Only then decide whether any durable U-kind distinction remains.

