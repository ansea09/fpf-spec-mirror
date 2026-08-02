---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:13"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__017_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:13 — Common Anti-Patterns and How to Avoid Them"
line_start: 95232
line_end: 95242
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.22.CGUS"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "G.11"
  - "U.BoundedContext"
keywords:
---

### F.17:13 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Global glossary row | Removes the exact interpretation basis and local-sense claim. | Add the by-value reference scheme, local expression, and local-sense claim to each scheme-based SenseCell. |
| One row for role and status | Fuses work-capable role with a state-family value. | Split into role row and status row; cite `F.10` or `A.19.SPR` for status. |
| Evidence role bucket | Turns evidence use, source use, assurance, and work into one pseudo-kind. | Recover each claim and cite `A.10`, `B.3`, `E.17`, `E.10.D2`, or role-work patterns. |
| Block as ontology | Treats didactic placement as subtype or part-of claim. | Keep block names as memory aids only. |
| Borrowed locality label as Tech name | Imports one tradition's commitments into the unified row. | Recover the governed value and scheme-based local sense; use F.18 and an actual Bridge rationale before selecting the unified name. |
| Row without direct pattern | Lets F.17 govern the object instead of the term-row publication. | Add direct pattern or mark the row not ready for public reuse. |

