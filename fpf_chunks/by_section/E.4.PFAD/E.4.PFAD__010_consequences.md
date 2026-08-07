---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__010_consequences.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:9 — Consequences"
line_start: 70362
line_end: 70367
dependencies:
  - "C.32.ADR"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.4"
  - "E.4.DPF.DA"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:9 - Consequences

PFAD makes framework decisions more inspectable, because a later maintainer can recover the decision question, source basis, selected structures, rejected alternatives, and repair conditions. The cost is an extra decision relation before publication.

The pattern also constrains ADR use. ADR-like records remain useful, but they become projections of a decision relation rather than the place where the ontology is invented.

