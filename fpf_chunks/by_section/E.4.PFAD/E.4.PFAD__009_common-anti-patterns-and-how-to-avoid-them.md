---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 70753
line_end: 70763
dependencies:
  - "A.6.RCD"
  - "A.6.REL"
  - "C.32.ADR"
  - "C.32.PAD"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| PFAD as a second decision | Authors reconcile an E.9 answer with another PFAD result. | Keep one selected answer in one E.9 DRR; use PFAD only as the framework-specific profile. |
| Paperwork on the cheap exit | A curated route or stop triggers a DRR without settling a later-used boundary. | Close the exploratory use directly. |
| Mandatory relation row | A PFR row is required before relations among initial patterns can be understood. | State each relation directly and add a row only for a named maintenance use. |
| ADR as decision | A publication projection is treated as the answer or acceptance. | Name the answer and acceptance separately; use ADR only as a projection. |
| Conditional detail made universal | Every decision must supply proposal, naming, quality, admission, source-return, and package records. | Include only details that change this answer or serve a named use. |
| Hidden Core change | A domain or local framework decision silently changes FPF Core meaning. | State dependency direction and keep Core changes in their own accepted decision. |

