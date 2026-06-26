---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)"
section_id: "A.1:5"
section_title: "Archetypal Grounding (Worked Cases)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__007_archetypal-grounding-worked-cases.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.1 — Holon Ontic Foundation (U.Holon and Admitted Holon Kinds)"
  - "A.1:5 — Archetypal Grounding (Worked Cases)"
line_start: 1534
line_end: 1587
dependencies:
  - "A.1.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.22"
  - "A.3.4"
  - "A.6.5"
  - "A.7"
  - "B.3.5"
  - "C.13"
  - "C.2.1"
  - "C.20"
  - "C.30"
  - "E.10.ARCH"
  - "E.24"
  - "E.24.UK"
keywords:
---

### A.1:5 - Archetypal Grounding (Worked Cases)

#### A.1:5.1 - Pump As Acting System

Pump #37 is a `U.System` holon in a plant maintenance bounded context.

```text
HolonSlotRelation@Context:
  holonRef: Pump #37
  boundedContextRef: PlantLineB.Maintenance.2026
  identityOrRecognitionRule: asset tag plus installed pump boundary
  partRelationRefs: casing, impeller, seals, motor, inlet flange, outlet flange
  holonDelimitationRelationRefs: casing plus inlet and outlet flange delimitation
  holonBoundaryCrossingRelationRefs: water flow, electrical supply, control signal
  admittedHolonKindRef: U.System

SystemParticipationRelation@Context:
  systemRef: Pump #37
  roleAssignmentRefs: cooling-water circulation role
  capabilityRefs: flow-rate envelope
  methodRefs: maintenance method selected by plant rules
  workOccurrenceRefs: performed inspection WO-1842
  transformationParticipationRefs: moving water under operating conditions
```

The pump can bear a role, participate in transformations, and have selected structures. The work order, dashboard, and maintenance procedure are epistemes or publications unless a direct pattern says otherwise.

#### A.1:5.2 - Scientific Theory As Episteme Holon

Newtonian gravitation in a selected edition is a `U.Episteme` holon in a physics-education bounded context.

```text
HolonSlotRelation@Context:
  holonRef: Newtonian gravitation, selected textbook edition
  boundedContextRef: PhysicsEducation.SelectedEdition
  identityOrRecognitionRule: selected claims, definitions, reference scheme, and examples
  partRelationRefs: laws, definitions, derivations, diagrams, exercises, evidence relations
  admittedHolonKindRef: U.Episteme
```

The theory does not teach itself, revise itself, or authorize lab work. A teacher, student, author, reviewer, or software system in role may explain, revise, publish, compare, or use the episteme.

#### A.1:5.3 - Fleet As Collection Or Acting Collective

A fleet list is a membership claim. Fleet availability is a whole-level characteristic. A fleet-coordination organization that coordinates vehicles, drivers, rules, and work can be an acting collective `U.System` only after boundary, coordination, role assignments, capability or method evidence, and work-facing participation are recovered.

If a source says "the fleet responded", A.1 does not accept the sentence by wording. Recover the actual claim: individual vehicle work, fleet-coordination system work, collection-as-whole characteristic, or B.2 whole reidentification.

#### A.1:5.4 - Lathe Changing A Workpiece

A lathe can change a workpiece during manufacturing without becoming the workpiece's super-holon.

Use `A.3.4` for the bounded transformation: transformed object, initial condition, post-state or delta, boundary conditions, acting system participation, method, work occurrence, and evidence. Use A.14 or C.13 for part-whole only when parthood is independently admitted.

