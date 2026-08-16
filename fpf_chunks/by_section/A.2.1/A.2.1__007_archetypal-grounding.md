---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.SystemRoleAssignment - Contextual System-Role Assignment"
section_id: "A.2.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__007_archetypal-grounding.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.2.1 — U.SystemRoleAssignment - Contextual System-Role Assignment"
  - "A.2.1:5 — Archetypal Grounding"
line_start: 3329
line_end: 3373
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.3.3"
  - "F.6"
  - "F.9"
keywords:
  - "assignment predicate"
  - "direct assignment species"
  - "holder System"
  - "identity"
  - "maximal interval"
  - "performedUnderAssignment"
  - "system-role kind"
---

### A.2.1:5 - Archetypal Grounding

#### A.2.1:5.1 - Robot Assigned for One Inspection Shift

The maintenance domain declares a simple species and an occurrence:

```text
MaintenanceInspectionAssignment <: U.SystemRoleAssignment
  HolderSystemSlot: U.System, U.EntityRef
  AssignedSystemRoleKindSlot: MaintenanceSystemRoleKindDomain, ByValue

InspectionAssignment-17:
  HolderSystemSlot: Robot-7
  AssignedSystemRoleKindSlot: InspectorSystemRole
  assignmentInterval: [2026-07-13T09:00, 2026-07-13T17:00]
```

The two fields designate the species participants. The interval is assertion content about the occurrence extent. `MaintenanceSystemRoleVocabulary-2026`, its effective scheme, and the relevant `KindSignature` can be cited to interpret the claim without becoming participants. Sensor capability, assignment state, inspection Method, and any performed inspection Work remain separate.

#### A.2.1:5.2 - Repeated Assignment Episodes

Robot-7 is assigned again on the next day under the same species and kind. The predicate does not obtain continuously across the two shifts, so the second shift is another `U.SystemRoleAssignment` occurrence. Reusing one staffing-row identifier cannot collapse the episodes.

#### A.2.1:5.3 - Motor Assigned as Drive

For a current equipment assignment, declare the species and identify its occurrence: `Motor-M1` is the holder and `DriveMotorSystemRole` is the assigned-kind value. `PumpAssembly-A` remains the actual assembly System and Work locus rather than a generic context participant. If installation in that exact assembly distinguishes assignment identity, the domain species must declare a real installation-locus participant and predicate, and the occurrence must supply its actual value.

The separate claim “Motor-M1 drives PumpAssembly-A during PumpRun-17” is not established by assignment. Until a domain predicate supplies its participants, applicability, and identity, return `missing-governor` for the motor-drive-functioning relation. Torque capability, installation Work, pumping Work, and the assignment remain usable independently.

#### A.2.1:5.4 - DDD Model-Use Structure Changes a Receiving Interpretation

Two software contexts each use `ApproverSystemRole`. `ApprovalService-2` can hold an assignment that obtains in the fulfilment context; name both the occurrence and its declared species. A receiving interpretation use can cite both the assignment-occurrence reference and `Orders-Fulfilment-ModelUseStructure` when the selected structure changes that use.

The structure was independently recovered under A.1.1. It neither assigns the service nor performs approval Work, and it does not enter the generic family. A future species that truly depends on it must declare the structure as a required participant and state the stronger predicate and identity law.

#### A.2.1:5.5 - Two Review Commissions

Alice is independently admitted as `U.System`. `Commission-A` and `Commission-B` satisfy the admitted `ProjectReviewCommission` kind. Two overlapping `ProjectReviewAppointmentAssignment` occurrences have the same holder and `ReviewerSystemRole` but different commission participants.

`ReviewWork-A` is attributed to `ReviewAssignment-A`; `ReviewWork-B` is attributed to `ReviewAssignment-B`. “Alice is the reviewer” can remain a recognition sentence, but it does not merge the appointments or identify which Work belongs to which occurrence.

#### A.2.1:5.6 - Reviewer and Review Report

`ReviewService-4` holds an exact review assignment and performs `ReviewWork-82` under it through F.6. `ReviewReport-82` is a separately identified `U.Episteme`. When the Work first constitutes that episteme and the inception claim matters, A.15.PROD recovers the relation among Work, change, and identity. A later evidence relation can use the report; the report never fills `HolderSystemSlot` merely because it is useful.

