---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__003_problem-frame.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:1 — Problem Frame"
line_start: 82542
line_end: 82549
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

### F.6:1 - Problem Frame

Role assignment sits between a role description and performed work. A role description lets a reader recognize `InspectorRole` or `ReviewerRole`; it does not assign a holder. A work occurrence may be performed by a holder under a role assignment; it is not the assignment itself. A status value, evidence relation, standard-use relation, requirement-use relation, or publication cue may constrain, evidence, qualify, or display a work-admission relation; it is not a role holder and not performed work.

A common source shape mixes these questions into one "role assignment and enactment cycle" with a status branch. That made the pattern convenient but ontologically noisy. A status assertion and a work-facing role assignment have different subjects, slots, evidence, windows, and direct governing patterns. Putting them into one cycle made status look like a kind of role assignment and made `RoleEnactment` look like a durable run-time object.

F.6 therefore becomes a check pattern. It asks whether the current local claim can use a recovered `U.RoleAssignment`, and whether a current `U.Work` occurrence can cite that assignment. If the current claim is status, evidence, source, publication, bridge, capability, or method, F.6 names the direct governing pattern and stops.

