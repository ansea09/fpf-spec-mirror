---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__004_problem.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:2 — Problem"
line_start: 1929
line_end: 1940
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.5"
  - "A.6.RSIR"
  - "E.24"
keywords:
  - "U.RoleAssignment"
  - "assignment"
  - "context"
  - "function vs identity"
  - "holder"
  - "responsibility"
  - "role"
---

### A.2:2 - Problem

Without this pattern:

1. **Type explosion returns.** Each contextual use becomes a new system kind such as `PumpAsCoolingCirculator` or `ReviewerReportSystem`.
2. **Role and assignment collapse.** The role value, the holder, the context, and the time window are treated as one vague label.
3. **Role and capability collapse.** A role name is treated as if it created ability.
4. **Role and method collapse.** A role name is treated as if it contained the method by which work is done.
5. **Role and evidence collapse.** A document, dataset, standard, proof, or model card is treated as a role holder because it is used as evidence or source material.
6. **Role and work collapse.** A role label is treated as evidence that work was performed.
7. **Argument-position drift appears.** "Role" is used for relation argument positions or slot positions, competing with `A.6.5` SlotSpec discipline.

