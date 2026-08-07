---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:12"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__014_rationale.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:12 — Rationale"
line_start: 44724
line_end: 44727
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.22.CGUS"
  - "A.6.0"
  - "A.7.1"
  - "A.8"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
  - "F.18"
  - "F.8"
  - "F.9"
keywords:
  - "KindBridge"
  - "SubkindOf"
  - "bounded-context local kind"
  - "effective ReferenceScheme"
  - "intent-bearing KindSignature"
  - "optional slice-indexed extension"
  - "three-valued candidate judgment"
---

### C.3:12 - Rationale

The kind, its declaration, one classification judgment, and a representation of current true members answer different engineering questions and change for different reasons. Keeping them separate lets a kind continue across compatible declaration revisions, lets candidate state change an extension without changing the kind, and lets evidence or a guard change reliance without rewriting the world-side classification.

