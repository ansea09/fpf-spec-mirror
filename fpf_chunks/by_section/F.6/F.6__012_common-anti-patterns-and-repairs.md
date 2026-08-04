---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:10"
section_title: "Common Anti-Patterns and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__012_common-anti-patterns-and-repairs.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:10 — Common Anti-Patterns and Repairs"
line_start: 91312
line_end: 91322
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.4"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3.1"
  - "A.3.2"
  - "A.6.REL"
  - "E.10"
  - "E.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "actual performing U.System"
  - "assignment coverage"
  - "exact U.RoleAssignment"
  - "performedUnderAssignment"
  - "separate assertion and evidence"
  - "world-side attribution"
---

### F.6:10 - Common Anti-Patterns and Repairs

| Anti-pattern | Failure | Repair |
|---|---|---|
| Assignment proves work | Role holding is confused with dated performance. | Name the `U.Work` occurrence and direct `performedUnderAssignment` relation. |
| Work attributed by role label | Assignment episode and interpretation are unavailable. | Recover the exact `U.RoleAssignment` through its four participants and uninterrupted obtaining extent. |
| Non-covering assignment | Work is attributed outside the assignment episode. | Select the covering assignment occurrence or leave attribution unresolved; do not widen the window by prose. |
| `RoleEnactmentFact` retained | A duplicate object competes with work and attribution. | Replace it with `performedUnderAssignment(WorkOccurrenceSlot, RoleAssignmentSlot)`. |
| Report as performer | A result or evidence episteme is put in holder position. | Keep the report in its work-result, evidence, source, or publication relation. |
| Context shorthand becomes ontology | `Context` is inserted as a universal relation participant. | Recover the exact denoted object and use its direct pattern; generic assignment keeps four participants and derives its episode extent from uninterrupted obtaining. |

