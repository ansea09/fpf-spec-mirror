---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:5"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__007_solution.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:5 — Solution"
line_start: 40762
line_end: 40774
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

### C.3.1:5 - Solution

Use `U.Kind` and `U.SubkindOf` only for local typed-reasoning compatibility unless another pattern explicitly brings the value into durable U-kind admission.

Norms:

1. `U.SubkindOf` is reflexive, transitive, and antisymmetric over `U.Kind` values.
2. A `U.Kind` carries no claim scope. Scope belongs to claims or capabilities under USM.
3. Intent and membership are governed by C.3.2, not by this core pattern.
4. Cross-context sameness or translation uses kind bridge discipline, not shared spelling.
5. `U.SubkindOf` is not the relation that makes a dependent durable U-kind under `E.24.UK`.
6. A structural `U.*` name that looks like a root FPF kind is governed by `E.24.UK`.

