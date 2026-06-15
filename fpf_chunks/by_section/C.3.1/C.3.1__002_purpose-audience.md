---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind & SubkindOf (Core)"
section_id: "C.3.1:1"
section_title: "Purpose & Audience"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__002_purpose-audience.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "C.3.1 — U.Kind & SubkindOf (Core)"
  - "C.3.1:1 — Purpose & Audience"
line_start: 39620
line_end: 39627
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

### C.3.1:1 - Purpose & Audience

This pattern gives **one small, stable vocabulary** to say *what* a claim ranges over (its **entityOfConcern**) without entangling that with *where it applies* (Scope) or *how well it is supported* (R). For managers:

* It prevents the costly mistake “more abstract wording ⇒ wider scope.”
* It enables **typed composition** (you cannot combine claims about incompatible “things”).
* It keeps **Scope** and **Assurance** math unchanged and predictable.

