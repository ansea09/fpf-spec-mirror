---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
section_id: "A.2.5:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__004_problem-frame.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "A.2.5 — RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
  - "A.2.5:1 — Problem Frame"
line_start: 3841
line_end: 3848
dependencies:
  - "A.15"
  - "A.2.1"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:1 - Problem Frame

Work-facing role assignment is not enough for safe work attribution. "Dana holds IncidentCommanderRole" may be true while Dana is off-duty, conflicted by another role assignment, outside the current assignment window, or missing a fresh authorization source. "Robot-7 holds InspectorRole" may be true while the robot is uncalibrated. "Thermometer T-17 holds ObserverRole" may be true while the calibration evidence is stale.

The project needs a small state space for each important role in each bounded context. That state space says which role states exist, which state predicates justify them, and which states admit work. It is not a method order, not a task list, not a capability, not a work log, and not an episteme status ontology.

A.2.5 therefore defines `RoleStateRelation@BoundedContext` as a selected relation structure around a `U.Role` and bounded context. It uses state-machine or graph notation only as a selected mathematical or representation lens where helpful. The FPF object is the role-state relation used for work admission and role-state claims.

