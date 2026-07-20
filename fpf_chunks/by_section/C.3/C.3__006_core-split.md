---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:4"
section_title: "Core Split"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__006_core-split.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:4 — Core Split"
line_start: 42822
line_end: 42834
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

### C.3:4 - Core Split

Keep four objects separate:

| Object | Meaning |
| --- | --- |
| `U.Kind` | Local kind value naming what a claim quantifies over under an effective `U.ReferenceScheme`. |
| Intent | The kind's signature, predicates, invariants, and formality-bearing definition. |
| Extent | The instances belonging to the kind in one context slice. |
| Scope | Where a claim holds; this belongs to claims or capabilities, not to kinds. |

Typed reasoning composes with F-G-R and USM by order: first typed compatibility, then scope coverage, then assurance and freshness penalties where relevant.

