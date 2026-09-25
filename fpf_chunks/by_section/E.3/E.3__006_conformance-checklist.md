---
chunk_kind: "child"
pattern_id: "E.3"
pattern_title: "Principle Taxonomy, Precedence and Agent Autonomy Profiles (ABL)"
section_id: "E.3:5"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.3/E.3__006_conformance-checklist.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "E.3 — Principle Taxonomy, Precedence and Agent Autonomy Profiles (ABL)"
  - "E.3:5 — Conformance Checklist"
line_start: 79017
line_end: 79025
dependencies:
  - "E.1"
  - "E.2"
keywords:
  - "ABL"
  - "Arch"
  - "BLP waiver"
  - "Did"
  - "Epist"
  - "Gov"
  - "Prag"
  - "autonomy budget"
  - "conflict resolution"
  - "oversight"
  - "precedence"
  - "principle taxonomy"
  - "profile change"
---

### E.3:5 - Conformance Checklist

| ID          | Requirement                                                                                                          | Purpose                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **CC‑PT.1** | Every principle record **MUST** state `class` and may list `precedence_over[]`.                                      | Makes declared priorities inspectable. |
| **CC‑PT.2** | Precedence graph **MUST** be acyclic.    | Prevents circular law.           |
| **CC‑PT.3** | Any DRR introducing/modifying a principle **MUST** include a *Pillar Impact Analysis* and the impact of proposed precedence edges on each affected Pillar (P‑1… P‑11). | Aligns evolution with Pillars.   |
| **CC‑PT.4** | Incompatible applicable rules without a winner **MUST** return the unresolved pair and hold the dependent action until an authorized resolution under §4.2. | Prevents an arbitrary tie-break from acting as authority. |

