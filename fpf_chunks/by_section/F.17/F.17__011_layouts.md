---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Make a Settled Naming Decision Recoverable for Reuse (Unified Term Sheet)"
section_id: "F.17:9"
section_title: "Layouts"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__011_layouts.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "F.17 — Make a Settled Naming Decision Recoverable for Reuse (Unified Term Sheet)"
  - "F.17:9 — Layouts"
line_start: 122744
line_end: 122761
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

Layout B, comparison-column: keep the scheme, local expression, and sense claim inside `SenseCellRefs` and use presentation columns such as tradition, discipline, language, publication family, or project family. For each compared entry, the reader must still be able to resolve its exact by-value scheme and local-sense claim. The column label helps organize the comparison; that recovered scheme and claim determine its interpretation.

Never mix a scheme column and a discipline or project-family column as if they had the same kind. A `U.ReferenceScheme` is an interpretation basis carried by value; a comparison column is a didactic view.

