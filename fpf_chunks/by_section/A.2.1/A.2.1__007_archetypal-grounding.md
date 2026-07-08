---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - Contextual Work-Role Assignment"
section_id: "A.2.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__007_archetypal-grounding.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "A.2.1 — U.RoleAssignment - Contextual Work-Role Assignment"
  - "A.2.1:5 — Archetypal Grounding"
line_start: 2520
line_end: 2565
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
keywords:
  - "RCS/RSG"
  - "RoleEnactmentFact"
  - "Standard"
  - "context"
  - "holder"
  - "performedBy"
  - "role"
---

### A.2.1:5 - Archetypal Grounding

#### A.2.1:5.1 - Industrial Inspection Work

A maintenance line assigns an inspection role to a robot for one shift.

```text
Robot_7#InspectorRole:MaintenanceLine_A@2026-06-15T09:00..2026-06-15T11:00
```

The holder is a system. The role value is `InspectorRole`. The bounded context is `MaintenanceLine_A`. The assignment window covers the planned inspection shift.

This does not assert that the robot satisfies the sensor capability-fit condition. Capability stays under `A.2.2`. It does not assert that inspection work already occurred. Performed work stays under `A.15.1`. It only gives later method, plan, role-state, and work-attribution claims a typed assignment relation to cite.

#### A.2.1:5.2 - Motor Assigned as Drive Motor

A water-pump assembly assigns a motor to the drive role for an installed window.

```text
Motor_M1#DriveMotorRole:WaterPumpAssembly_A@installed-window
Work PumpingRun_2026-07-01 performedBy Motor_M1#DriveMotorRole:WaterPumpAssembly_A
```

The holder is the motor as a `U.System`. The role value is `DriveMotorRole`. The bounded context is the pump assembly or plant context that gives the role its meaning. The assignment does not say the motor is a part of the role; it says the motor bears that role in this system context. Torque capability, electrical supply, thermal limits, functional port claims, the pump's transformation-flow structure, and the dated pumping run remain neighboring claims under their own patterns.

#### A.2.1:5.3 - Software Deployment

A release train has a deployment method description with a step that states `DeployerRole` as a role-admission condition.

```text
CI_Service#DeployerRole:ReleaseTrain_2026@2026-Q2
Work DeploymentRun_418 performedBy CI_Service#DeployerRole:ReleaseTrain_2026
```

The assignment relation admits a candidate performer. The work occurrence still needs the method or method-description relation, the assignment window, and any enactable role-state assertion needed under `A.2.5`. A green test suite, ticket approval, or policy rule may justify the assignment or the work gate, but those are neighboring evidence, gate, or policy relations, not hidden role values.

#### A.2.1:5.4 - Review Report and Reviewer

A human reviewer or review service can hold `ReviewerRole` in a review context. The review report produced by that work is an episteme.

Later, another team may use the report as evidence for a claim. That later relation is evidence-use around the report. The report does not hold `ReviewerRole`; the reviewer holder did.

#### A.2.1:5.5 - Standard Used in Safety Work

The source sentence "ISO 26262 has the normative standard role in this safety case" is repaired as a standard-use or requirement-use relation around an episteme. If a safety engineer performs work using that standard, the engineer or engineering team may hold an enactment-facing role assignment. The standard constrains, defines, or supplies source material; it does not perform work and does not become a holder in `U.RoleAssignment`.

