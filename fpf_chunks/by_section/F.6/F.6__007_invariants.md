---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "SystemRoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:5"
section_title: "Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__007_invariants.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "F.6 — SystemRoleAssignment and Performed-Work Attribution Check"
  - "F.6:5 — Invariants"
line_start: 94040
line_end: 94058
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.13"
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
  - "already admitted U.Work"
  - "complete post-admission A.13/A.15.1/F.6 basis"
  - "conditional profile"
  - "deprecated performedBy compatibility only"
  - "direct case fact"
  - "exact Work-assignment relation"
  - "holder equality"
  - "performedUnderAssignment"
  - "same obtaining A.13 assignment"
  - "separate evidence"
  - "temporal coverage"
---

### F.6:5 - Invariants

1. Every positive performed-Work attribution links one dated `U.Work` occurrence to one assignment occurrence of a declared `U.SystemRoleAssignment` species.
2. `SystemRoleAssignmentSlot` accepts the family and preserves the assignment's declared species, all participants, rule, applicability, and occurrence identity.
3. The actual performer is the admitted System in `RA.HolderSystemSlot`; the assignment and kind do not act.
4. RA's predicate obtains throughout the attributed Work interval; a declared window alone does not establish coverage.
5. The species declaration, occurrence participant identity, holder match, and time coverage constrain but do not establish the Work–assignment link.
6. Overlapping assignments are checked pair by pair; an unresolved basis never licenses attribution to every covering assignment.
7. Every positive precise assignment-bound performer attribution starts from an already admitted Work whose actual performer has the A.13 core for the exact action, scope, working situation, and window, then adds its own F.6 link through the same covering assignment occurrence. A characteristic profile remains conditional on its receiving use. A lead, team, member, coordination, allocation, or responsibility claim substitutes for none of these.
8. A passive assigned System is not thereby a performer. Any claimed passive participation needs a rule that defines it; otherwise A.6.RCD returns `missing-governor`.
9. Assignment does not prove performance, and attribution proves neither classification, capability, state, Method validity, result quality, responsibility, authority, nor acceptance.
10. `RoleEnactment` wording is repaired to Work plus `performedUnderAssignment`; no duplicate object remains.
11. Assertions, logs, rosters, evidence, identifiers, and publications can support or designate an attribution but do not constitute it.
12. Missing evidence leaves reliance unresolved; a missing case fact linking Work and assignment leaves the positive attribution unasserted.
13. An episteme does not fill `HolderSystemSlot` because it describes or supports Work.
14. Cross-context correspondence changes neither assignment identity nor Work attribution.
15. Reduced prose may omit only an assignment identifier unused by the receiving claim, and only after the complete Work–assignment basis remains recoverable.
16. The Method enacted by W remains a separate fact; only the admitted holder System performs W.

