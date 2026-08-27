---
chunk_kind: "child"
pattern_id: "E.24.UK"
pattern_title: "U-kind Admission and Ontic Settlement"
section_id: "E.24.UK:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.UK/E.24.UK__008_bias-annotation.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "E.24.UK — U-kind Admission and Ontic Settlement"
  - "E.24.UK:6 — Bias-Annotation"
line_start: 90792
line_end: 90795
dependencies:
  - "A.1.1"
  - "A.11"
  - "A.2.6"
  - "A.22"
  - "A.6.0"
  - "A.6.5"
  - "A.6.RCD"
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
  - "F.17"
  - "F.18"
  - "F.8"
  - "U.Kind"
  - "U.SubkindOf"
keywords:
---

### E.24.UK:6 - Bias-Annotation

This pattern blocks punctuation-bias and taxonomy-bias. A `U.*` spelling, title, filename, table row, or imported type word is not enough to create a durable FPF kind. Recover the governed individuals, their identity or membership rule, and the PatternID that locates that rule first. When the candidate instead names participation in a relation, a SlotSpec, an assertion or description field, a selected `U.Structure`, an `E.24.PUB` form, or a `C.29` representation element, retain that exact object and its defining or testing rule. For a structure specialization, first recover the same base individual through A.22's four discriminators; a context, system, team, subsystem, label, scope, method, work, result, view, representation, publication, or use creates neither that base identity nor dependent membership. Only then decide whether any durable U-kind distinction remains.

