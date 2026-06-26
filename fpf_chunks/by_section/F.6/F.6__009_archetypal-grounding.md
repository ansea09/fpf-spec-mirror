---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "RoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:7"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__009_archetypal-grounding.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "F.6 — RoleAssignment and Performed-Work Attribution Check"
  - "F.6:7 — Archetypal Grounding"
line_start: 81588
line_end: 81644
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

### F.6:7 - Archetypal Grounding

#### F.6:7.1 - Robot Inspection

A maintenance line has a role-description episteme for `InspectorRole`. A shift note says Robot-7 inspected Pump-12.

F.6 recovers:

```text
CandidateHolderRef: Robot_7
CandidateRoleValueRef: InspectorRole
BoundedContextRef: MaintenanceLine_A
AssignmentWindowDisposition: filled by shift window
WorkOccurrenceRef: InspectionWork_2026-06-15-09
PerformedByRelation: InspectionWork_2026-06-15-09 performedBy Robot_7#InspectorRole:MaintenanceLine_A@shift
Result: workAttributionAdmitted, if A.2.1 and A.15.1 checks pass
```

This does not prove the robot's sensor capability, the inspection method's adequacy, or the quality of the result. Those claims use capability, method, evidence, and assurance patterns.

#### F.6:7.2 - Review Report and Reviewer

A review report is an episteme. The reviewer is a person, service, or team modeled as an acting holon.

The sentence "Report R has reviewer role" is repaired by asking two questions:

- Who or what performed the review work under `ReviewerRole`?
- How is report R being used now: as evidence, source, publication, or result?

The reviewer holder may be assigned a `U.RoleAssignment`. The report does not hold the role. Evidence use of the report goes to the evidence-use pattern.

#### F.6:7.3 - Standard Used in Safety Work

A safety method description cites ISO 26262. The source phrase says that the standard has the "normative role" in the safety case.

F.6 result:

```text
Result: claimGovernedOutsideF6
NotCarried: no HolderSlot, no U.RoleAssignment, no performed work
```

The standard is an episteme used through standard-use, source-use, requirement-use, or specification-use relations. A safety engineer or tool service may separately hold `SafetyAnalystRole` when performing work with that standard.

#### F.6:7.4 - Access Label and Actual Approval Work

An RBAC directory says Alice has `DB-Admin`. That directory state is an access or policy status in its own bounded context. It is not automatically a work-facing `ApproverRole`.

If Alice approves a database migration, F.6 can check a separate assignment and work attribution:

```text
Alice#ApproverRole:MigrationApprovalContext@approval-window
ApprovalWork_481 performedBy Alice#ApproverRole:MigrationApprovalContext@approval-window
```

The RBAC status may justify or constrain the approval only through the direct access, policy, evidence, source, or gate pattern that admits that use.

