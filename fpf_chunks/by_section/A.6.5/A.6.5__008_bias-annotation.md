---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
section_id: "A.6.5:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__008_bias-annotation.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "A.6.5 — U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
  - "A.6.5:6 — Bias-Annotation"
line_start: 16428
line_end: 16435
dependencies:
  - "A.1"
  - "A.2.1"
  - "A.6.0"
  - "A.6.2"
  - "A.6.4"
  - "A.7"
  - "C.2.1"
  - "C.3"
  - "E.10"
  - "E.17.0"
  - "E.8"
  - "F.6"
  - "U.EpistemeSlotRelation"
  - "U.MultiViewDescribing"
  - "U.Signature"
keywords:
  - "argument position"
  - "pass-by-reference"
  - "pass-by-value"
  - "reference"
  - "signature"
  - "slot"
  - "substitution"
  - "value"
---

### A.6.5:6 - Bias-Annotation

This pattern has a typed-structure bias: it prefers explicit positions and filler kinds over conversational shorthand. That bias is intentional because relation-bearing FPF prose must remain reusable across epistemes, signatures, roles, interfaces, methods, evidence, status, and architecture.

This pattern also has an episteme-example bias because `C.2.1` is the mature precedent for slot relation discipline. The Solution generalizes beyond epistemes and explicitly includes work-facing role assignments, evidence-use relations, status-use relations, interfaces, ports, and transformation-flow structures.

The anti-bias guard is that `A.6.5` never makes description or publication the center unless the current EntityOfConcern is itself a description or publication relation. It starts from the relation-bearing EntityOfConcern and only then describes how its slots may be specified or published.

