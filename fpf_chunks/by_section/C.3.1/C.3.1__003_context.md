---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind & SubkindOf (Core)"
section_id: "C.3.1:2"
section_title: "Context"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__003_context.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "C.3.1 — U.Kind & SubkindOf (Core)"
  - "C.3.1:2 — Context"
line_start: 36660
line_end: 36664
dependencies:
  - "A.1"
  - "A.2.6"
  - "C.3.2"
  - "C.3.3"
keywords:
  - "kind"
  - "partial order"
  - "subkind"
  - "type hierarchy"
---

### C.3.1:2 - Context

across Contexts, “type” means OWL class, SHACL shape, code type, BORO category, etc. A **neutral, minimal** object is needed to name *the kind of entities* a claim quantifies over **without** importing a full type system or altering USM. **`U.Kind`** fills that role; **ordering** between kinds captures “is‑a/refines” relationships a Context relies on.


