---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:9"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__011_conformance-checklist.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:9 — Conformance Checklist"
line_start: 39996
line_end: 40005
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

### C.3.1:9 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C31-1` | Every `U.Kind` use is context-local unless a bridge says otherwise. |
| `CC-C31-2` | Every `U.SubkindOf` use is a partial-order claim over `U.Kind` values. |
| `CC-C31-3` | Scope is not stored on the kind value. |
| `CC-C31-4` | Dependent durable U-kind relations are not modeled as `U.SubkindOf` by default. |
| `CC-C31-5` | U-kind admission and structural `U.*` repair are governed by `E.24.UK`; public naming demand is handled by Part F after the governed value is recovered. |

