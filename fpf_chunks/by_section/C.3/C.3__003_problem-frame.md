---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__003_problem-frame.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:1 — Problem Frame"
line_start: 42804
line_end: 42807
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.22.CGUS"
  - "A.7.1"
  - "A.8"
  - "C.2.3"
  - "C.3"
  - "C.3.1"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
  - "F.5"
  - "F.8"
keywords:
  - "classification"
  - "extension"
  - "intension"
  - "kind"
  - "subkind"
  - "type"
  - "typed reasoning"
  - "vocabulary"
---

### C.3:1 - Problem Frame

Across source ontologies, reference schemes, and project slices, "type" can mean ontology class, programming type, schema shape, category, source label, or public FPF U-kind. C.3 provides a smaller discipline: `U.Kind` is a local value used for one typed-reasoning use under an effective `U.ReferenceScheme`, and its extent is evaluated over named `U.ContextSlice` values. It is not automatically a durable FPF U-kind and it does not by itself admit a `U.*` structural name. A C.3 `U.Kind` may be backed by construction, recognition, membership, or extent criteria for that use, but that basis remains local typed-reasoning law until `E.24.UK` admits durable FPF kindhood.

