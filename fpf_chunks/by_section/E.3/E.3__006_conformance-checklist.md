---
chunk_kind: "child"
pattern_id: "E.3"
pattern_title: "Principle Taxonomy & Precedence Model"
section_id: "E.3:5"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.3/E.3__006_conformance-checklist.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "E.3 — Principle Taxonomy & Precedence Model"
  - "E.3:5 — Conformance Checklist"
line_start: 59334
line_end: 59341
dependencies:
  - "E.2"
keywords:
  - "Arch"
  - "Did"
  - "Epist"
  - "Gov"
  - "Prag"
  - "classification"
  - "conflict resolution"
  - "hierarchy"
  - "precedence"
  - "principles"
  - "taxonomy"
---

### E.3:5 - Conformance Checklist

| ID          | Requirement                                                                                                          | Purpose                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **CC‑PT.1** | Every principle record **MUST** state `class` and may list `precedence_over[]`.                                      | Enables deterministic overrides. |
| **CC‑PT.2** | Precedence graph **MUST** be acyclic.    | Prevents circular law.           |
| **CC‑PT.3** | Any DRR introducing/modifying a principle **MUST** include a *Pillar Impact Analysis* and proposed precedence edges impact on each affected Pillar (P‑1… P‑11)| Aligns evolution with Pillars.   |

