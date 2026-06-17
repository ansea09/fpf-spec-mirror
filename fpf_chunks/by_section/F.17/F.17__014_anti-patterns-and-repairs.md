---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:13"
section_title: "Anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__014_anti-patterns-and-repairs.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:13 — Anti-patterns and repairs"
line_start: 77715
line_end: 77725
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "F.1"
  - "F.1-F.12"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "UTS"
  - "Unified Term Sheet"
  - "glossary"
  - "human-readable output"
  - "publication"
  - "summary table"
---

### F.17:13 - Anti-patterns and repairs

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Global glossary row | Removes bounded-context meaning. | Add context and edition to each sense cell. |
| One row for role and status | Fuses work-capable role with a state-family value. | Split into role row and status row; cite `F.10` or `A.19.SPR` for status. |
| Evidence role bucket | Turns evidence use, source use, assurance, and work into one pseudo-kind. | Recover each claim and cite `A.10`, `B.3`, `E.17`, `E.10.D2`, or role-work patterns. |
| Block as ontology | Treats didactic placement as subtype or part-of claim. | Keep block names as memory aids only. |
| Borrowed context name as Tech name | Imports one tradition's commitments into the unified row. | Use `F.18` and bridge rationale before selecting the unified name. |
| Row without direct pattern | Lets F.17 govern the object instead of the term-row publication. | Add direct pattern or mark the row not ready for public reuse. |

