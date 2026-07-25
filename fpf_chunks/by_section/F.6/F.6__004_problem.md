---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__004_problem.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:2 — Problem"
line_start: 88459
line_end: 88469
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

### F.6:2 - Problem

Without the direct attribution relation, recurring engineering failures appear:

1. **Assignment-as-work.** Current role holding is treated as evidence that the assigned system performed a particular occurrence.
2. **Performer by label.** A name such as `Reviewer` or `Operator` is used without the assignment episode that fixes holder, role interpretation, and time.
3. **Assignment-episode mismatch.** The assignment interval does not cover the work interval, yet attribution is accepted.
4. **Support-as-constitution.** A log, report, standard, dashboard, or decision is treated as what makes the attribution obtain rather than as an assertion or support relation.
5. **Duplicate enactment ontology.** `RoleEnactment` or `RoleEnactmentFact` becomes a second object beside the dated work and its direct `performedUnderAssignment` relation.
6. **Hidden locality.** A generic context field replaces the role-taxonomy episteme, effective reference scheme, assignment window, or an independently selected model-use structure.

