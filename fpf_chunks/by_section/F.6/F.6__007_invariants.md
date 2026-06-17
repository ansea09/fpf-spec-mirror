---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:5"
section_title: "Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__007_invariants.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:5 — Invariants"
line_start: 73653
line_end: 73665
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "E.10"
  - "E.10.ARCH"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "asserting status"
  - "conceptual moves"
  - "enactment"
  - "role assignment"
---

### F.6:5 - Invariants

1. **Role assignment is local.** Every assignment check names one `U.Role`, one admitted holder, and one `U.BoundedContext`.
2. **Role description is not assignment.** A role-description episteme may identify the role value; it does not assign a holder.
3. **Assignment is not work.** A `U.RoleAssignment` can be admitted without any `U.Work` occurrence.
4. **Work attribution is direct.** Performed work cites the role assignment through `Work.performedBy = RoleAssignment`; `RoleEnactmentFact` is only a named fact over that relation.
5. **No durable `U.RoleEnactment`.** Source `U.RoleEnactment` wording is repaired to direct performed-by wording or `RoleEnactmentFact`.
6. **Status is not a role branch.** Status-use statements are governed by `F.10` or the direct status pattern, not by F.6.
7. **Epistemes are not role holders by use.** Evidence, source, standard, requirement, definition, explanation, publication, assurance, and gate uses of epistemes go to their direct relations.
8. **Window honesty.** If a stronger claim depends on assignment currentness, role state, or work time, missing window content lowers or blocks that claim.
9. **Bridge restraint.** Cross-context role-like labels need `F.9`; a bridge does not mutate a local assignment.
10. **Notation restraint.** `Holder#Role:Context@Window` is source or shorthand notation for a typed assignment relation, not the relation's ontology.

