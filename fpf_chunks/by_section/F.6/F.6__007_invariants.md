---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:5"
section_title: "Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__007_invariants.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:5 — Invariants"
line_start: 91720
line_end: 91733
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

### F.6:5 - Invariants

1. Every performed-work attribution relates one exact `U.Work` occurrence to one exact `U.RoleAssignment` occurrence.
2. The assignment occurrence `RA` in `RoleAssignmentSlot` keeps exactly four fixed participants and one maximal continuous obtaining extent; no mandatory `U.BoundedContext`, generic context slot, or optional model-use participant is added.
3. The actual maximal continuous extent of the assignment occurrence covers the attributed portion of the work interval; a declared or recorded window alone does not establish coverage.
4. Assignment does not prove performance, and performance attribution does not prove capability, state, method validity, result quality, or acceptance.
5. `RoleEnactment` wording is repaired to dated work plus direct `performedUnderAssignment`; no duplicate enactment object is retained.
6. Assertions, logs, rosters, evidence, identifiers, and publications remain epistemic or representational objects distinct from world-side relation obtaining.
7. An evidence gap yields unresolved reliance, not an inferred non-attribution interval.
8. An episteme does not fill `HolderSystemSlot` merely because it describes, constrains, or supports the work claim.
9. Cross-scheme role correspondence uses a direct bridge relation and does not change either assignment identity.
10. Reduced prose remains admissible until a receiving use needs explicit relation-occurrence identity.
11. For admitted Work `W`, actual `enactsMethod(W, M)` remains a separately obtaining relation to one exact `U.Method`; only the admitted holder system acts, while assignment, role value, capability, method, and method description do not perform the work.

