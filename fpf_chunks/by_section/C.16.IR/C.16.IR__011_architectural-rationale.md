---
chunk_kind: "child"
pattern_id: "C.16.IR"
pattern_title: "Determine What a Measurement Indication Can Resolve"
section_id: "C.16.IR:10"
section_title: "Architectural Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.IR/C.16.IR__011_architectural-rationale.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "C.16.IR — Determine What a Measurement Indication Can Resolve"
  - "C.16.IR:10 — Architectural Rationale"
line_start: 54640
line_end: 54647
dependencies:
  - "A.3.3.PI"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.16"
  - "C.16.MR"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### C.16.IR:10 - Architectural Rationale

Indication production and interpretation have different directions. A procedure can map many subject conditions to the same output. Interpreting that output therefore asks which of those conditions remain possible and which distinctions the receiving question needs.

This explains the separate contribution from C.16.MR. A measurement relation can already be available while its inverse use is unresolved. Constructing compatible cases makes that relation usable without requiring a new model or an estimate for every parameter.

The same reasoning connects physical measurement, mathematical inverse relations and computational information loss. Their subject premises differ. A source's loading law, an instrument's clipping order and a counter's event semantics supply the cases to which the common reasoning applies.

