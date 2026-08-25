---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "SystemRoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__004_problem.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "F.6 — SystemRoleAssignment and Performed-Work Attribution Check"
  - "F.6:2 — Problem"
line_start: 91237
line_end: 91248
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

### F.6:2 - Problem

Without the direct attribution relation:

1. **Assignment becomes Work.** Current assignment is treated as evidence that a system performed one occurrence.
2. **Performer comes from a label.** `Reviewer` or `Operator` is used without a holder and assignment episode.
3. **A stronger assignment is flattened.** A commission-sensitive appointment is replaced by a weaker generic record.
4. **Episodes do not cover.** Work is attributed outside the interval in which the exact assignment predicate obtains.
5. **Support becomes constitution.** A log, report, standard, dashboard, or decision is treated as what makes attribution obtain.
6. **Enactment is duplicated.** `RoleEnactment` or `RoleEnactmentFact` becomes another object beside Work and attribution.
7. **Locality is hidden.** A context word replaces the exact local kind, assignment species, Work locus, scope, or selected model-use structure.

