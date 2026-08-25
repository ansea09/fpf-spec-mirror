---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "SystemRoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:10"
section_title: "Common Anti-Patterns and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__012_common-anti-patterns-and-repairs.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "F.6 — SystemRoleAssignment and Performed-Work Attribution Check"
  - "F.6:10 — Common Anti-Patterns and Repairs"
line_start: 91489
line_end: 91505
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
  - "A.3"
  - "A.6.9"
  - "A.6.REL"
  - "C.3.3"
  - "E.10.ROLE"
  - "E.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
keywords:
  - "Work attribution"
  - "exact assignment occurrence"
  - "holder equality"
  - "performedUnderAssignment"
  - "performer System"
  - "separate evidence"
  - "temporal coverage"
---

### F.6:10 - Common Anti-Patterns and Repairs

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Assignment proves Work | Holding is confused with dated performance. | Name the Work and assignment, then establish from the case that the Work was performed under that assignment. |
| Holder plus interval constructs attribution | Any covering assignment held by the performer is treated as the assignment under which W occurred. | Treat the matching holder and interval coverage as necessary checks; establish from the case which assignment the Work was performed under. |
| Overlap attributes to every commission | Two assignments with a common holder and interval both receive the same Work. | Recover all participants; establish only the Work–assignment link supported by the case, or leave it unresolved. |
| Lead or team assignment covers everyone | One assignment substitutes for the actual performer set. | Give every actual performer of top-level or child Work its own covering assignment and F.6 link to that Work. |
| Passive article becomes performer | A test-subject assignment and overlap are read as Work attribution or passive participation. | Attribute Work only to actual performers; use the rule that defines passive participation or return the A.6.RCD `missing-governor` result. |
| Work attributed by a system-role label | The holder and assignment occurrence are unavailable. | Recover the declared assignment occurrence, all its participants, and its holder. |
| F.6 creates a generic assignment | A stronger appointment is flattened or duplicated. | Keep RA's declared species and let `SystemRoleAssignmentSlot` consume the family. |
| Non-covering assignment | Work lies outside RA's predicate-true episode. | Use the covering assignment only when the case also links it to the Work; otherwise leave attribution unresolved. |
| `RoleEnactmentFact` retained | A duplicate object competes with Work and attribution. | Replace it with the F.6 relation between the Work and assignment. |
| Assertion or evidence creates the pair | A report or support path is treated as what makes the Work–assignment fact true. | Keep the assertion and evidence in their own relations; use them only to support reliance on the attribution claim. |
| Report as performer | A result or evidence episteme fills holder position. | Keep the report in its result, evidence, source, or publication relation. |
| Context shorthand becomes ontology | `Context` is inserted as a universal participant. | Recover the denoted object and the relation that actually applies. |

