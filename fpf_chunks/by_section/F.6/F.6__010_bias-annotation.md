---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "SystemRoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:8"
section_title: "Bias Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__010_bias-annotation.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "F.6 — SystemRoleAssignment and Performed-Work Attribution Check"
  - "F.6:8 — Bias Annotation"
line_start: 92359
line_end: 92370
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

### F.6:8 - Bias Annotation

| Bias risk | Failure | Repair |
| --- | --- | --- |
| Record-first bias | A log or roster identifier is treated as a world-side relation. | Recover Work and assignment occurrences; keep the record as assertion or publication. |
| Generic-duplicate bias | F.6 demands a weaker assignment beside a stronger appointment. | Accept the family ValueKind and project the holder from the assignment occurrence through its declared species. |
| Universal-context bias | One context field replaces kind, species, extent, scope, locus, and model-use selection. | Recover each object and direct relation; add no optional generic participant. |
| Enactment reification | `RoleEnactmentFact` duplicates Work and attribution. | Use `performedUnderAssignment`. |
| Support-as-constitution | Evidence becomes an attribution participant. | Keep it in the relation supporting the assertion. |
| Assignment-as-performance | Staffing is treated as completed Work. | Name dated `U.Work` before attribution. |
| Bridge overreach | A corresponding kind or assignment licenses local attribution. | Recover the local assignment and preserve Work's exact attribution. |

