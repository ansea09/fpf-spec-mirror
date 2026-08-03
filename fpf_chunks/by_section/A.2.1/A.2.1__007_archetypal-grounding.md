---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - System Role Assignment"
section_id: "A.2.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__007_archetypal-grounding.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "A.2.1 — U.RoleAssignment - System Role Assignment"
  - "A.2.1:5 — Archetypal Grounding"
line_start: 3143
line_end: 3200
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "C.2.1"
  - "F.6"
  - "F.9"
  - "U.Role"
keywords:
  - "AssignmentInterval"
  - "assignment occurrence"
  - "effective ReferenceScheme"
  - "holder System"
  - "performedUnderAssignment"
  - "role value"
  - "role-taxonomy episteme"
---

### A.2.1:5 - Archetypal Grounding

#### A.2.1:5.1 - Robot Assigned for One Inspection Shift

```text
RoleAssignmentAssertion:
  participantDesignations:
    HolderSystemSlot: Robot-7
    RoleValueSlot: InspectorRole
    RoleTaxonomyEpistemeSlot: MaintenanceRoles-2026
    EffectiveReferenceSchemeSlot: Maintenance-Scheme-A
  assignmentInterval: [2026-07-13T09:00, 2026-07-13T17:00]
```

The four SlotKind-labelled fields designate the actual relation participants. The `assignmentInterval` field states the assertion's temporal description of the occurrence; it is not a fifth relation-participant designation. During the shift, the direct assignment predicate obtains for the four actual participants—`Robot-7`, `InspectorRole`, `MaintenanceRoles-2026`, and `Maintenance-Scheme-A`; the displayed `RoleAssignmentAssertion` states those participant designations and describes the occurrence's temporal extent. Sensor capability, current role state, the inspection method, and any performed inspection work remain separate claims.

#### A.2.1:5.2 - Repeated Assignment Episodes

`Robot-7` is assigned the same role again on the next day under the same taxonomy and scheme. The four stable participant fillings match, but the assignment predicate does not obtain continuously across the two shifts. The second shift is therefore another `U.RoleAssignment` occurrence. A staffing table that reuses one row identifier must not collapse the two world-side episodes.

#### A.2.1:5.3 - Motor Holding a Drive Role

```text
RoleAssignmentAssertion:
  participantDesignations:
    HolderSystemSlot: Motor-M1
    RoleValueSlot: DriveMotorRole
    RoleTaxonomyEpistemeSlot: PumpAssemblyRoles-v4
    EffectiveReferenceSchemeSlot: Pump-A-Operating-Scheme
  assignmentInterval: [2026-07-01T08:30, open]
```

The open end says that this episteme does not yet state the occurrence's end. Extending or later closing that temporal description does not create another assignment while the direct predicate obtains continuously for the same four participants. The holder is the motor as a `U.System`. Pump Assembly A is the actual system in which installation and work occur; it is not an assignment context slot. Torque capability, electrical interface relations, installation work, and a later pumping run remain direct neighboring claims.

#### A.2.1:5.4 - DDD Model-Use Structure Changes a Receiving Interpretation

Two software teams use `ApproverRole` under different model vocabularies. In the fulfilment model it admits acceptance of a fulfilment-state transition; in the payment model it admits payment authorization. The generic assignment still has exactly four participants:

```text
RoleAssignmentAssertion:
  participantDesignations:
    HolderSystemSlot: ApprovalService-2
    RoleValueSlot: ApproverRole
    RoleTaxonomyEpistemeSlot: FulfilmentRoles-v3
    EffectiveReferenceSchemeSlot: Fulfilment-Approval-Scheme
  assignmentInterval: [2026-07-13T10:00, 2026-07-13T18:00]

ReceivingInterpretationUse:
  roleAssignmentRef: ApprovalService-2-ApproverAssignment
  selectedModelUseStructureRef: Orders-Fulfilment-ModelUseStructure
```

The second block belongs to the receiving assertion or work use. It does not add a fifth participant to `U.RoleAssignment` and does not change generic occurrence identity. The selected structure was independently recovered under `A.1.1`; it neither assigns the service nor performs approval work. If a future dependent relation species truly obtains only with one selected structure, its direct pattern must declare that structure as a required identity-bearing participant.

#### A.2.1:5.5 - Reviewer and Review Report

`ReviewService-4` holds `ReviewerRole` through `ReviewService-4-ReviewerAssignment` and, as that assignment's admitted holder System, performs `ReviewWork-82` under it through `F.6` `performedUnderAssignment(ReviewWork-82, ReviewService-4-ReviewerAssignment)`. `ReviewReport-82` is a separately identified `U.Episteme`; when the work first constitutes that exact episteme and the inception claim matters, A.15.PROD recovers the local work/change/identity claim. Its content may state a review judgment under the direct evaluation pattern. A later evidence relation may use the report for another claim; the report never fills `HolderSystemSlot` merely because it is useful.

