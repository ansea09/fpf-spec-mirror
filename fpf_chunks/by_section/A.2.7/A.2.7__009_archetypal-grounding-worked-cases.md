---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:5"
section_title: "Archetypal Grounding - Worked Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__009_archetypal-grounding-worked-cases.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:5 — Archetypal Grounding - Worked Cases"
line_start: 5132
line_end: 5190
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.5"
keywords:
  - "bundles (⊗)"
  - "incompatibility (⊥)"
  - "requiredRoles substitution"
  - "role algebra"
  - "separation of duties (SoD)"
  - "specialization (≤)"
---

### A.2.7:5 - Archetypal Grounding - Worked Cases

#### A.2.7:5.1 - Role-Requirement Substitution Without Capability Smuggling

`PlantMaintenance_2026` declares:

```text
SeniorHydraulicsTechnician <= HydraulicsTechnician
```

A method step requiring `HydraulicsTechnician` may accept an assignment to `SeniorHydraulicsTechnician`. This does not prove that the technician has the pressure-test capability. The method step may separately require `PressureTestCapability` under `A.2.2`.

#### A.2.7:5.2 - Incompatibility for Independence

`SafetyCase_2026` declares:

```text
HazardAnalysisAuthor incompatibleWith HazardAnalysisApprover
```

The same holder cannot use overlapping assignments for both roles when approving the same hazard analysis. If a source sentence says "the approver role is independent", A.2.7 recovers the role incompatibility relation; evidence of independence, approval work, and approval records stay in their direct patterns.

#### A.2.7:5.3 - Bundle Expression Without New Capability

`IncidentOps_2026` declares:

```text
IncidentLeadOnCall := IncidentCommander and Communicator and DecisionMaker
```

This is a reusable role-bundle expression for method requirements. It does not state that one person has incident-management capability; that remains a capability claim. It does not state that incident work happened; that remains a work claim.

#### A.2.7:5.4 - Naming Engineer-Roboticist and Musician

A project says: "Vasya is an engineer, does robot engineering, is therefore an engineer-roboticist. These are musical robots, and Vasya is also a musician, performs music, and teaches robots music."

Good ordinary rewrite:

> Vasya is our engineer-roboticist and musician: he works on robot engineering, and in the musical-robots project he also performs music and teaches robots music.

This ordinary sentence is admissible because a reader can recover the separate FPF values behind it:

```text
BoundedContextRef: MusicalRobotLab_2026
HolderRef: Vasya
EngineeringRoleExpression: EngineerRole qualified by robotics domain, robotics-engineering method family, practice, or work field
OrdinaryRoleLabel: engineer-roboticist or robotics engineer
IndependentRoleValue: MusicianRole
HolderAssignmentRefs: Vasya assigned to the robotics-qualified engineering role expression or declared RoboticsEngineerRole; Vasya assigned to MusicianRole
MethodOrWorkRefs: robot-engineering method or work; music-performance work; robot-music-teaching method or work
RepresentationLensRefs?: role-algebra, graph, matrix, embedding, or neural representation only if the project explicitly uses such a description of the role relation structure
```

Do not write "engineer and roboticist and musician" unless `EngineerRole`, `RoboticistRole`, and `MusicianRole` are three independent role values with separate assignments.

Do not write "engineer-roboticist-musician" unless the bounded context declares one durable combined role value or one named role-bundle expression with its own role description and naming settlement. Without that declaration, the label hides that musician is a separate role assignment.

Robot-engineering, music performance, and teaching robots music are method or work names when those values are current. They are not produced by a role-algebra lens merely because their labels share words with role names. The role relation structure and a `MethodRelationStructure@BoundedContext` can be coupled in the same working sentence, but the FPF record keeps their typed values distinct.

