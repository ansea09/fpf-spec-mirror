---
chunk_kind: "child"
pattern_id: "A.12"
pattern_title: "Acting-Side Externalization and Reflexive Split"
section_id: "A.12:5"
section_title: "Archetypal Grounding (Worked Cases)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.12/A.12__007_archetypal-grounding-worked-cases.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.12 — Acting-Side Externalization and Reflexive Split"
  - "A.12:5 — Archetypal Grounding (Worked Cases)"
line_start: 20314
line_end: 20368
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.1"
  - "A.2.7"
  - "A.3.4"
  - "B.2"
  - "B.2.5"
  - "C.13"
  - "C.2.1"
  - "C.30"
  - "E.17"
keywords:
---

### A.12:5 - Archetypal Grounding (Worked Cases)

#### A.12:5.1 - Robot Self-Calibration

Source wording: "the robot calibrates itself."

Recovered A.12 use:

```text
ReflexiveSplit@RobotInternals:
  containingHolonRef: Robot R17
  actingPartOrSubsystemRef: CalibrationController
  changedPartOrSubsystemRef: SensorSuite
  actingRoleAssignmentRef: CalibrationController as calibration acting system
  transformationRef: sensor calibration change, if A.3.4 is current
  workOccurrenceRef: calibration run, if A.15.1 is current
```

The robot may remain the containing holon. The calibration controller and sensor suite are distinct positions for the current claim. The fact that the change occurs inside the robot does not remove the acting side.

#### A.12:5.2 - Document Cross-Reference Update

Source wording: "the document updates its cross-references."

Recovered A.12 use:

```text
ActingSideExternalization@DocumentBuild:
  changedHolonRef: publication file or episteme slot relation under direct owner
  actingSystemRef: build script or editing system
  actingRoleAssignmentRef: cross-reference update role in DocumentBuild
  workOccurrenceRef: build run, if A.15.1 is current
  evidenceRelationRefs: build log, diff, validation check, or stronger evidence owner
```

The document does not act. If the changed object is a publication form, use publication owners. If the changed object is a claim-bearing episteme relation, use episteme owners.

#### A.12:5.3 - Lathe And Workpiece

Source wording: "the lathe makes the workpiece, so the workpiece belongs to the lathe during manufacturing."

Recovered A.12 use:

```text
ActingSideExternalization@Machining:
  changedHolonRef: workpiece
  actingSystemRef: lathe
  actingRoleAssignmentRef: machining acting system
  transformationRef: bounded machining transformation, if A.3.4 is current
  workOccurrenceRef: machining work occurrence, if A.15.1 is current
  holonBoundaryCrossingRelationRef: cutting force, fixture relation, control relation, or material-removal relation under direct owner
```

The lathe can transform the workpiece without being the workpiece's super-holon. Use part-whole owners only if the workpiece is independently admitted as part of a containing holon.

