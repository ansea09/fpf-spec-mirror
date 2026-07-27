---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:8"
section_title: "Bias Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__010_bias-annotation.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:8 — Bias Annotation"
line_start: 88931
line_end: 88941
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

### F.6:8 - Bias Annotation

| Bias risk | Failure | Repair |
|---|---|---|
| Record-first bias | A log row or roster identifier is treated as the world-side relation. | Recover the work and assignment occurrences; keep the row as an assertion or publication. |
| Universal-context bias | One context field replaces taxonomy, scheme, occurrence extent, scope, and model-use selection. | Restore the four assignment participants, state its actual extent separately, and route every remaining context-denoted object by kind. |
| Enactment reification | `RoleEnactmentFact` duplicates work and attribution. | Use the direct `performedUnderAssignment` relation. |
| Support-as-constitution | Evidence existence is made an attribution participant. | Keep evidence in the relation supporting use of an attribution assertion. |
| Assignment-as-performance | A staffing decision is treated as completed work. | Name a dated `U.Work` occurrence before attribution. |
| Bridge overreach | A role word from another scheme licenses local attribution. | Recover each local assignment and use `F.9` for correspondence. |

