---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:7"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__009_archetypal-grounding.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:7 — Archetypal Grounding"
line_start: 91249
line_end: 91286
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

### F.6:7 - Archetypal Grounding

#### F.6:7.1 - Robot Inspection

```text
RoleAssignmentAssertion@RoleAssignment17:
  participantDesignations:
    HolderSystemSlot: Robot-7
    RoleValueSlot: InspectorRole
    RoleTaxonomyEpistemeSlot: MaintenanceRoles-2026
    EffectiveReferenceSchemeSlot: Maintenance-Scheme-A
  assignmentInterval: [2026-07-13T09:00, 2026-07-13T17:00]

performedUnderAssignment:
  WorkOccurrenceSlot: InspectionWork-17
  RoleAssignmentSlot: RoleAssignment-17
```

The assertion interval describes the known extent of `RoleAssignment-17`; the direct assignment predicate must actually obtain throughout `InspectionWork-17` before `performedUnderAssignment` obtains. The relation attributes the inspection occurrence to Robot-7 under that assignment. Separately, `enactsMethod(InspectionWork-17, TurbineInspection@Maintenance-2026)` names the exact enacted method, while `TurbineInspectionProcedure-v3` may be cited as a distinct description episteme only if the receiving use needs it. Robot-7 is the actor; `InspectorRole`, a sensor capability or statement that Robot-7 possesses an inspection algorithm, the method, and the procedure do not perform the inspection. Algorithm-possession wording alone establishes neither the work attribution nor `TurbineInspectionProcedure-v3 : U.MethodDescription`. Calibration state, inspection-method adequacy, report quality, and acceptance remain separate claims.

#### F.6:7.2 - Reviewer and Review Report

Engineer Alice is identified as the exact holder and satisfies the A.1 `U.System` criterion. `ReviewAssignment-82` assigns her `ReviewerRole` under `ReviewRoles-v5` and `Review-Scheme-A` for one uninterrupted review assignment episode. `ReviewWork-82 performedUnderAssignment ReviewAssignment-82` attributes the dated work.

`ReviewReport-82` is a separately identified `U.Episteme`. When `ReviewWork-82` first constitutes that exact episteme and the inception claim matters, A.15.PROD recovers the local work/change/identity claim. A later evidence relation may use the report for a decision. The report never fills `HolderSystemSlot` and never becomes the attribution relation.

#### F.6:7.3 - Standard Used During Safety Work

A safety method description cites a standard, and source prose says that the standard has a "normative role". F.6 does not create a work-facing assignment for the standard. The standard is an episteme used through the exact external-rule, source-use, specification-use, or evidence relation selected by the claim.

A safety engineer or tool system may separately hold `SafetyAnalystRole` and perform dated safety work. That attribution names the engineer's or tool system's assignment; it does not use the standard as performer.

#### F.6:7.4 - Access Label and Approval Work

An access directory says Alice has `DB-Admin`. That entry describes an access or policy relation under its own scheme. It is not automatically a work-facing `ApproverRole` assignment.

If Alice performs `ApprovalWork-481`, recover a separate `U.RoleAssignment` under the role taxonomy used by the approval method and relate the work through `performedUnderAssignment`. The directory entry may support authorization or gate reasoning through its direct pattern; it does not substitute for the work assignment.

