---
chunk_kind: "child"
pattern_id: "A.2.8.PER"
pattern_title: "Granted Permission, Exercise, and Non-Prohibition"
section_id: "A.2.8.PER:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8.PER/A.2.8.PER__009_conformance-checklist.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.2.8.PER — Granted Permission, Exercise, and Non-Prohibition"
  - "A.2.8.PER:7 — Conformance Checklist"
line_start: 6739
line_end: 6751
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.5"
  - "A.2.8"
  - "A.2.9"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "F.6"
  - "U.Work"
keywords:
  - "checked non-violation"
  - "exact policy rule or decision result"
  - "matching dated-work exercise"
  - "permission or prohibition conflict"
  - "policy-valid strong grant"
  - "weak non-prohibition finding"
---

### A.2.8.PER:7 - Conformance Checklist

| ID | Check |
|---|---|
| `CC-A2.8.PER-1` | The current result is exactly `NonProhibitionFinding@Context`, `GrantedPermissionRelation@Context`, `PermissionExerciseRelation@Context`, `NonViolationFinding@Context`, or `PermissionNormConflictFinding@Context`. |
| `CC-A2.8.PER-2` | Beneficiary uses only `RoleRef | RoleAssignmentRef | PartyRef`, with its exact eligibility branch. |
| `CC-A2.8.PER-3` | A strong grant names the admitted holder `U.System` that performs the instituting act, the exact grantor assignment whose `HolderSystemSlot` resolves to that system, participants, policy/context, scope/window, currentness, and occurrence identity; the assignment is authority ground and never the actor. |
| `CC-A2.8.PER-4` | Weak findings require a current frame explicitly complete enough for the intended use; incompleteness returns `unresolved`. |
| `CC-A2.8.PER-5` | Exercise names dated work, the admitted `U.System` that performed it, the one current grant occurrence, scope, and interval; it answers action match and beneficiary eligibility from those objects and the exact covering assignment or on-behalf-of relation. It does not require generic match, eligibility, or beneficiary-binding findings, and the assignment never performs the work. |
| `CC-A2.8.PER-6` | Neither exercise nor non-exercise establishes `NonViolationFinding@Context`; non-exercise is not violation, and exercise is not obligation satisfaction and does not consume a grant without an explicit policy. |
| `CC-A2.8.PER-7` | A same-scope conflict is settled only by an applicable policy rule that selects the outcome or by a current resolution result produced by dated work of an admitted system under a covering assignment and independently obtaining decision-authority relation. Naming a policy, office, role, assignment, or “owner” alone leaves only the affected work or reliance use `unresolved`. |
| `CC-A2.8.PER-8` | Permit episteme, carrier, evidence, admissibility, readiness, gate, capability, work, and result retain their direct owners. |

