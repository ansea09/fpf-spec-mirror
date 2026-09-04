---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "SystemRoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:9"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__011_conformance-checklist.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "F.6 — SystemRoleAssignment and Performed-Work Attribution Check"
  - "F.6:9 — Conformance Checklist"
line_start: 94804
line_end: 94824
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

### F.6:9 - Conformance Checklist

1. `WorkOccurrenceSlot` names one dated `U.Work` occurrence already admitted by A.15.1 without relying on F.6; its actual performers already have the A.13 core for the exact action, scope, working situation, and window, and any characteristic profile is required only by its own Grade, autonomy, criterion-dependent, profile, or assurance use.
2. `SystemRoleAssignmentSlot` names one assignment occurrence of a declared species under `U.SystemRoleAssignment` through `U.RelationRef`.
3. The assignment's declared species, all identity-bearing participants, rule, applicability, and uninterrupted occurrence identity remain recoverable. Each species keeps its SlotSpec `ValueKind` domains distinct from the participant values supplied by the occurrence; `AssignedSystemRoleKindSlot` takes one kind value from its declared local system-role-kind domain.
4. The case establishes that W was performed under RA; the assignment's existence, matching holder, and temporal overlap do not establish that link.
5. The assignment holder is the System that actually performed W.
6. The assignment predicate covers the selected Work interval; attribution to a Work part first identifies that part as `U.Work`.
7. Checks 2, 3, 5, and 6 constrain a valid attribution but do not by themselves establish it.
8. Overlapping assignments are distinguished by all their participants and by checking each Work–assignment link from the case; an unresolved case yields no blanket attribution.
9. Every positive precise attribution for a top-level or child Work occurrence has its own covering assignment and F.6 link to that already admitted Work; lead, team, member, allocation, coordination, and responsibility claims do not substitute.
10. A passive assigned System receives no performer attribution from assignment or overlap; any claimed passive participation uses the rule that defines it or returns the A.6.RCD `missing-governor` result.
11. F.6 uses `performedUnderAssignment` and introduces no `RoleEnactmentFact` or generic assignment duplicate.
12. Assertions and evidence may support reliance on the attribution claim but do not make it true.
13. Classification, assignment state, capability, Method, result, evidence, source reliance, publication, responsibility, authority, gate, and decision claims use direct patterns.
14. Any selected model-use structure is designated by the receiving assertion or use, not by an optional generic slot.
15. Missing evidence leaves reliance unresolved rather than proving non-attribution; missing pair grounding leaves the positive relation unasserted.
16. Source shorthand is unfolded before a receiver depends on hidden values.
17. The Method enacted by W remains a separate fact, and no kind, assignment, capability, Method, or description is made the actor.
18. A short practitioner sentence may omit declaration and occurrence detail only after the Work–assignment link and its constraints are established.

