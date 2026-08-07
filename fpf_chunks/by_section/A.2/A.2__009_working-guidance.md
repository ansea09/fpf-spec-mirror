---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:7"
section_title: "Working Guidance"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__009_working-guidance.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:7 — Working Guidance"
line_start: 2904
line_end: 2914
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
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

### A.2:7 - Working Guidance

1. Identify the candidate holder. `U.Role` applies only when an admitted `U.System` is what the current participation claim classifies.
2. Name the role value, the role-taxonomy episteme, and the effective reference scheme that interprets it.
3. When another claim relies on who holds the role or when, state `U.RoleAssignment` under `A.2.1`.
4. State role state, capability fit, method admission, responsibility, commitment, work, transformation, evidence, and reliance through their direct patterns; do not put them inside the role value.
5. When a proposed subrole appears, use `A.2.7` only for substitution, incompatibility, qualification, or joint-admission bundle relations among role values. Use A.2 for another role value, and send role state, capability fit, responsibility, commitment, method, or work to its direct owner. Do not assume `partOf`.
6. When an independently selected `BoundedModelUseStructure` changes a receiving interpretation, designate it in that receiving assertion or use rather than in a generic role relation.
7. For a cross-scheme role use, establish the exact F.9 Bridge, state the separate C.2.1 bounded-use assertion, and recover current A.10 or B.3 reliance; a matching label, profile, Bridge, or card alone grants no use.
8. If the source phrase only says that a non-system entity contributes, recover the direct relation with `A.6.RSIR` and stop before creating `U.Role`.

