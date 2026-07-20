---
chunk_kind: "child"
pattern_id: "A.2.8.PER"
pattern_title: "Granted Permission, Exercise, and Non-Prohibition"
section_id: "A.2.8.PER:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8.PER/A.2.8.PER__007_archetypal-grounding.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "A.2.8.PER — Granted Permission, Exercise, and Non-Prohibition"
  - "A.2.8.PER:5 — Archetypal Grounding"
line_start: 5992
line_end: 6001
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.5"
  - "A.2.8"
  - "A.2.9"
  - "A.6.B"
  - "A.6.C"
  - "U.Work"
keywords:
  - "actual non-violation finding"
  - "permission exercise"
  - "permission or prohibition conflict"
  - "policy-valid strong grant"
  - "weak non-prohibition finding"
---

### A.2.8.PER:5 - Archetypal Grounding

**Strong grant and exercise.** A policy-valid grant speech act institutes `GrantedPermissionRelation@Context` for `MaintenanceTechnicianRole` to run `CalibrationProcedure-v3` during one service window. Its beneficiary is a `RoleRef`. Assignment `Tech-17@Shift-B` instantiates that role and performs dated calibration work that matches the action specification within scope. A `PermissionExerciseRelation@Context` obtains from that work to the still-current grant. The grant remains current for the rest of the window because the policy is not single-use. No obligation, readiness, capability, gate passage, safe result, or successful calibration is inferred.

**Weak finding.** A policy reviewer checks a named, current, sufficiently complete plant-access frame and finds no prohibition applicable to the role, action specification, zone, and window. The result is `NonProhibitionFinding@Context(result=nonProhibited)`, not an instituted grant. If the emergency-policy register cannot be checked, the result is `unresolved`.

**Actual-work non-violation.** After `CalibrationWork-17B` is performed, a compliance reviewer evaluates that exact work against `PlantCalibrationNormativeFrame-2026-07-19-e3`, whose currentness and sufficient completeness for the technician, procedure, zone, and service-window use are named and whose applicable prohibitions are checked. The result is `NonViolationFinding@Context(actionOrWorkRef=CalibrationWork-17B, normativeFrameRef=PlantCalibrationNormativeFrame-2026-07-19-e3, result=nonViolating)`. The separate exercise relation shows which grant the work exercised; exercise alone does not establish non-violation, and non-exercise alone does not establish it either. If the frame is stale or insufficiently complete for this use, the non-violation result is `unresolved`.

**Conflict and non-use.** The role-level calibration grant remains published while an emergency prohibition forbids entry into the contaminated zone during an overlapping interval. `PermissionNormConflictFinding@Context` names both exact claims and the emergency-policy precedence owner; work entry remains unresolved. A visible permit and green readiness tile cannot repair it. If no calibration work occurs, the permission is neither exercised nor violated.

