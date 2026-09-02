---
chunk_kind: "child"
pattern_id: "A.6.S"
pattern_title: "TargetSignature and optional ConstructorSignature - demand-driven signature engineering"
section_id: "A.6.S:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.S/A.6.S__012_rationale.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "A.6.S — TargetSignature and optional ConstructorSignature - demand-driven signature engineering"
  - "A.6.S:10 — Rationale"
line_start: 21061
line_end: 21070
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.3.1"
  - "A.3.2"
  - "A.6"
  - "A.6.0"
  - "A.6.2-A.6.6"
  - "A.6.5"
  - "A.6.6"
  - "A.6.B"
  - "A.7"
  - "C.2.1"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.6"
keywords:
  - "appear"
  - "quadrant classification is governed by A.6.B)"
---

### A.6.S:10 - Rationale

Stable boundaries sometimes benefit from a reusable description of how they are revised. That is the useful two-signature technique: one `U.Signature` is the current target declaration, and another `U.Signature` declares constructor operations for a named reuse. It is not a universal architecture for editing and does not require a third pair object.

A.6.5, A.6.6, A.6.2-A.6.4, and E.17 supply distinct optional moves. Treating all of them as mandatory constructor primitives would recreate the ambiguity and overhead those patterns are meant to remove. The direct move comes first; the reusable ConstructorSignature packages only the operation language that has an actual receiver.

The result keeps viewing, declaration edits, episteme succession, reference retargeting, EntityOfConcern retargeting, application, and Work distinct. A.6.B likewise keeps laws, gates, duties, and evidence-use claims from competing in one “contract” paragraph.

**SoTA source note (informative).** Modern effect systems support the separation between an operation declaration and effectful realization; categorical optics inform explicit preservation claims; and architecture-description practice informs accountable views. A.6.S adopts those limited separations without importing a tool ontology or making a ConstructorSignature mandatory.

