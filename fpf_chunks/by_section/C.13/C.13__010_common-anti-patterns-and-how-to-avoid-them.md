---
chunk_kind: "child"
pattern_id: "C.13"
pattern_title: "Constructional Mereology (Compose‑CAL)"
section_id: "C.13:7.1"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.13/C.13__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "C.13 — Constructional Mereology (Compose‑CAL)"
  - "C.13:7.1 — Common Anti-Patterns and How to Avoid Them"
line_start: 42449
line_end: 42455
dependencies:
  - "A.14"
  - "B.3.5"
keywords:
  - "composition"
  - "extensional identity"
  - "mereology"
  - "part-whole"
  - "set"
  - "slice"
  - "sum"
---

### C.13:7.1 - Common Anti-Patterns and How to Avoid Them

* **Constructor as public relation.** A `Gamma_m` trace is shown as the relation the working reader should use. Keep `ComponentOf`, `MemberOf`, and `AspectOf` in the Working-Model layer and attach the trace only as grounding.
* **Member as component.** A `set` construction is used to infer integrated assembly structure. Use `sum` for component identity and keep `set` as collection-as-whole grounding.
* **Temporal constructor drift.** A phase, schedule, or assembly order is modeled as a Compose-CAL constructor. Keep temporal and method claims in their own planes.
* **New constructor inflation.** A special case gets a new constructor before `sum`, `set`, or `slice` has failed across several domains. Try the triad first and reopen parsimony only when the triad cannot narrate the case.

