---
chunk_kind: "child"
pattern_id: "A.2.8.PER"
pattern_title: "Granted Permission, Exercise, and Non-Prohibition"
section_id: "A.2.8.PER:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.8.PER/A.2.8.PER__007_archetypal-grounding.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "A.2.8.PER — Granted Permission, Exercise, and Non-Prohibition"
  - "A.2.8.PER:5 — Archetypal Grounding"
line_start: 6218
line_end: 6227
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

### A.2.8.PER:5 - Archetypal Grounding

**Strong grant and exercise.** Admitted system `MaintenanceCoordinator-A` performs a policy-valid grant speech act under `MaintenanceCoordinator-A@DayShift`, the exact grantor assignment whose holder is that system. The act institutes `MaintenanceCalibrationGrant-2026-07-19 : GrantedPermissionRelation@Context` for `MaintenanceTechnicianRole` to run `CalibrationProcedure-v3` during one service window. Its beneficiary is a `RoleRef`. Beneficiary assignment `Tech-17@Shift-B` instantiates that role for admitted technician system `Tech-17`; `Tech-17` performs dated `CalibrationWork-17B` under that assignment. The Work instantiates `CalibrationProcedure-v3` within the grant's zone, window, and scope, so the action-match predicate holds; `Tech-17@Shift-B` covers the Work and instantiates the beneficiary role, so the beneficiary predicate holds. `CalibrationExercise-17B : PermissionExerciseRelation@Context` therefore connects `CalibrationWork-17B` to `MaintenanceCalibrationGrant-2026-07-19`, cites `beneficiaryAssignmentRef=Tech-17@Shift-B`, and states the work interval and scope. No auxiliary match or eligibility finding is created. The assignments ground the grant and work attribution but perform neither act. The grant remains current for the rest of the window because the policy is not single-use. No obligation, readiness, capability, gate passage, safe result, or successful calibration is inferred.

**Weak finding.** A policy reviewer checks a named, current, sufficiently complete plant-access frame and finds no prohibition applicable to the role, action specification, zone, and window. The result is `NonProhibitionFinding@Context(result=nonProhibited)`, not an instituted grant. If the emergency-policy register cannot be checked, the result is `unresolved`.

**Actual-work non-violation.** After `CalibrationWork-17B` is performed, `CalibrationComplianceEvaluation-17B : U.Work` checks that Work against `PlantCalibrationNormativeFrame-2026-07-19-e3`, whose currentness and sufficient completeness for the technician, procedure, zone, and service-window use are named and whose applicable prohibitions are checked. The result is `NonViolationFinding@Context(workRef=CalibrationWork-17B, performerAssignmentRefs={Tech-17@Shift-B}, normativeFrameRef=PlantCalibrationNormativeFrame-2026-07-19-e3, evaluationWorkRef=CalibrationComplianceEvaluation-17B, result=nonViolating)`. It needs no beneficiary-binding episteme: the covering assignment already relates the performer system to the beneficiary role. The separate exercise relation shows which grant the work exercised; exercise alone does not establish non-violation, and non-exercise alone does not establish it either. If the frame is stale or insufficiently complete for this use, the non-violation result is `unresolved`.

**Conflict and non-use.** The role-level calibration grant remains published while `ContaminatedZoneEntryProhibition-7` forbids the same beneficiary and calibration action in Zone 7 during an overlapping interval. In the direct-rule case, `EmergencyCalibrationPrecedencePolicy-e5` contains applicable claim `CZ7-Prohibition-Overrides-CalGrant`; the rule's conditions match, so the finding is `settledByApplicableRule`, cites that rule, and returns “do not enter Zone 7” for the blocked work. In a discretionary Zone 8 case, admitted system `SafetyDirector-3` performs `CalibrationConflictDecisionWork-8` under `SafetyDirector-3@EmergencyShift`; the separately obtaining `PlantEmergencyExceptionAuthority-8` relation authorizes that decision, and current `CalibrationConflictResolutionResult-8` selects the prohibition claim for the stated scope/window. Only then is the finding `settledByDecisionResult`. A second Zone 8 request that merely names the Safety Director but has no dated decision work or current result remains `unresolved`. A visible permit and green readiness tile cannot repair either gap. If no calibration work occurs, the permission is neither exercised nor violated.

