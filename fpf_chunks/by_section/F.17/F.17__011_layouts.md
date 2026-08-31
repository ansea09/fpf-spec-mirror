---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:9"
section_title: "Layouts"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__011_layouts.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:9 — Layouts"
line_start: 98285
line_end: 98302
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.22.CGUS"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.10.LRN"
  - "E.10.MOVE"
  - "E.11"
  - "E.17.0"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
---

### F.17:9 - Layouts

F.17 admits two common layouts.

Layout A, scheme-first: keep the left rail fixed and add one exact reference-scheme column per selected interpretation basis. Use this when the reader's comparison concerns local senses under named schemes.

```text
UTSRowId | Unification thread | Block | Governed value | Governed value kind | Defining or constraining pattern
Unified Tech name | Unified Plain name | NameCardRef
Reference scheme A | Reference scheme B | Reference scheme C
BridgeRefs | Row rationale | Admissible use | Not this use
Row edition | Currentness condition | Notes
```

Layout B, comparison-column: keep the scheme, local expression, and sense claim inside `SenseCellRefs` and use a smaller set of presentation columns such as tradition, discipline, language, publication family, or project family. These columns are teaching aids; they have interpretation authority only when each cell still resolves to its exact by-value scheme and local-sense claim.

Never mix a scheme column and a discipline or project-family column as if they had the same kind. A `U.ReferenceScheme` is an interpretation basis carried by value; a comparison column is a didactic view.

