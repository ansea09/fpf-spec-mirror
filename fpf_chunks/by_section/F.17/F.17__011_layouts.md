---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:9"
section_title: "Layouts"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__011_layouts.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:9 — Layouts"
line_start: 86543
line_end: 86560
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "F.1"
  - "F.1-F.12"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "UTS"
  - "Unified Term Sheet"
  - "glossary"
  - "human-readable output"
  - "publication"
  - "summary table"
---

### F.17:9 - Layouts

F.17 admits two common layouts.

Layout A, context-first: keep the left rail fixed and add one bounded-context column per selected context. Use this when the reader must compare local senses across named contexts.

```text
UTSRowId | Block | Governed kind or value | Direct pattern
Unified Tech name | Unified Plain name | NameCardRef
Context A, edition | Context B, edition | Context C, edition
BridgeRefs | Row rationale | Admissible use | Not this use
Row edition | Currentness condition | Notes
```

Layout B, comparison-column: keep context and edition inside `SenseCells` and use a smaller set of comparison columns such as tradition, discipline, language, or project family. Use this for teaching when the direct bounded-context cells would be too wide. The comparison columns are presentation aids; they have context authority only when each cell still cites the bounded context and edition.

Never mix a context column and a discipline column as if they had the same kind. A bounded context is a meaning scope; a discipline column is a didactic comparison view.

