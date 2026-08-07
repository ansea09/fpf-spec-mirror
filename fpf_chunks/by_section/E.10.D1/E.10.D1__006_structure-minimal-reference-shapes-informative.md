---
chunk_kind: "child"
pattern_id: "E.10.D1"
pattern_title: "Lexical Discipline for “Context” (D.CTX)"
section_id: "E.10.D1:5"
section_title: "Structure — Minimal reference shapes (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D1/E.10.D1__006_structure-minimal-reference-shapes-informative.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "E.10.D1 — Lexical Discipline for “Context” (D.CTX)"
  - "E.10.D1:5 — Structure — Minimal reference shapes (informative)"
line_start: 76166
line_end: 76173
dependencies:
  - "A.2.1"
  - "A.4"
  - "A.7"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.6"
  - "F.7"
  - "F.9"
keywords:
  - "U.BoundedContext"
  - "anchor"
  - "context"
  - "domain"
  - "frame"
---

### E.10.D1:5 - Structure — Minimal reference shapes (informative)

> Shapes shown **do not** prescribe formats; they are naming conventions.

* **Context Id.** Stable short handle (e.g., `BPMN_2_0`, `PROV_O_2013`, `ITIL4_2020`, `NIST_RBAC_2004`, `SOSA_SSN_2017`).
* **SenseCell.** `(ContextId, Local‑Sense)` where `Local‑Sense` is the Context‑local preferred label (from F.2).
* **ConceptSet Row.** A table row keyed by a row id; columns are `SenseCell`s per Context (F.7).

