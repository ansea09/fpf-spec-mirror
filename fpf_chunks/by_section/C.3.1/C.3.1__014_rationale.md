---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:12"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__014_rationale.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:12 — Rationale"
line_start: 40284
line_end: 40287
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

### C.3.1:12 - Rationale

The core must stay small because it is used inside many other FPF claims. Once a local kind relation starts carrying construction, admission, naming, scope, or slot discipline, it becomes too heavy and starts creating false ontology. C.3.1 therefore gives only the typed partial order and leaves stronger relations to the patterns that govern those objects.

