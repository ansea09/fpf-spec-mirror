---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:3"
section_title: "Norms"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__005_norms.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:3 — Norms"
line_start: 38570
line_end: 38578
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

### C.3.1:3 - Norms

1. `U.SubkindOf` is reflexive, transitive, and antisymmetric over `U.Kind` values.
2. A `U.Kind` carries no claim scope. Scope belongs to claims or capabilities under USM.
3. Intent and membership are governed by C.3.2, not by this core pattern.
4. Cross-context sameness or translation uses kind bridge discipline, not shared spelling.
5. `U.SubkindOf` is not the relation that makes a dependent durable U-kind under `E.24.UK`.
6. A structural `U.*` name that looks like a root FPF kind is governed by `E.24.UK`.

