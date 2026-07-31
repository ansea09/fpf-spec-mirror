---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:11"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__013_consequences.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:11 — Consequences"
line_start: 44731
line_end: 44738
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

### C.3:11 - Consequences

**Benefits.** C.3 supports local typed claims, subkind reasoning, classification, and queryable extensions without premature ontology growth or evidence-created membership.

**Costs.** Repeated uses must pin a declaration edition and context slice, and receiving uses must distinguish `false` from `unknown`.

**Risks avoided.** False sameness, implicit time, scope-on-kind, record ontology, accidental relation minting, kind/individual substitution, and mathematical-set overread are blocked at the first use.

