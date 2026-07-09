---
chunk_kind: "child"
pattern_id: "B.2"
pattern_title: "Meta-Holon Transition - Whole Reidentification"
section_id: "B.2:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2/B.2__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "B.2 — Meta-Holon Transition - Whole Reidentification"
  - "B.2:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 33519
line_end: 33529
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.3.4"
  - "B.1"
  - "B.2"
  - "B.2.2"
  - "B.2.3"
  - "B.2.4"
  - "B.2.P"
  - "C.13"
  - "C.16"
  - "C.29"
  - "C.30.ILC"
  - "C.32.P2S"
  - "E.24.UK"
  - "U.Episteme"
keywords:
---

### B.2:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Emergence by adjective | A capability or property is called emergent without reidentifying the whole. | Use `B.2.P` to recover claim kind, then B.2 only if whole reidentification is current. |
| Record as ontology | Trigger profile, result field, or record name is treated as a U-kind. | Keep profile and record as forms; admit the result holon kind through direct owners. |
| KPI jump as MHT | A metric improves and MHT is declared. | Run `ExistingWholeExplanationCheck@Context`; use measurement, characteristic, method, work, or architecture owners if sufficient. |
| Agency shortcut | Agency threshold crossing creates a new root kind. | Use characteristic-space threshold owners; B.2 only when closure, supervision, objective, or identity changes. |
| Math result as MHT | Graph, RG-like, MSPD, or benchmark expression declares new whole. | Use `C.29`; recover holon identity before B.2. |
| Transformation as containment | A system changes another holon and is treated as its super-holon. | Use A.12, A.3.4, A.15.1, and boundary-crossing relation owners; use parthood only if independently admitted. |

