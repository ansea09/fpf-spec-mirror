---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind & SubkindOf (Core)"
section_id: "C.3.1:5"
section_title: "Solution — Core Objects (overview)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__006_solution-core-objects-overview.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "C.3.1 — U.Kind & SubkindOf (Core)"
  - "C.3.1:5 — Solution — Core Objects (overview)"
line_start: 39647
line_end: 39653
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

### C.3.1:5 - Solution — Core Objects (overview)

* **`U.Kind`** — a **context‑local intensional** object naming a “kind of thing” claims may quantify over.
* **`U.SubkindOf (⊑)`** — a **partial order** on kinds (reflexive, transitive, antisymmetric). `k₁ ⊑ k₂` reads “`k₁` refines `k₂`.”

> **No Scope on kinds.** Scope is for **claims/capabilities** (USM). Kinds supply **entityOfConcern only**; **membership** and **signature** live in **C.3.2**.

