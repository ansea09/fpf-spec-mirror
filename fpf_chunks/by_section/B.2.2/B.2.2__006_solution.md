---
chunk_kind: "child"
pattern_id: "B.2.2"
pattern_title: "Meta-System Transition - System Specialization of MHT"
section_id: "B.2.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.2/B.2.2__006_solution.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "B.2.2 — Meta-System Transition - System Specialization of MHT"
  - "B.2.2:4 — Solution"
line_start: 34722
line_end: 34811
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.2.1"
  - "A.2.2"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "B.1.2"
  - "B.2"
  - "B.2.5"
  - "B.3"
  - "B.3.5"
  - "C.13"
  - "C.16"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
keywords:
---

### B.2.2:4 - Solution

After `B.2` leaves an MHT question open, admit the system-result case with a system-focused slice of the `HolonReidentificationRecord@Context`.

#### B.2.2:4.1 - System-Result MHT Slice

Use this slice when `mhtResultSystemRef` is selected.

```text
SystemMHTSlice@Context:
  existingWholeRef: U.Holon
  mhtResultSystemRef: U.System
  boundedContextRef:
  selectedTriggerProfileRef: MHTTriggerProfile@Context
  existingWholeExplanationCheckRef: ExistingWholeExplanationCheck@Context
  systemKindAdmissionRef: A.1 or B.1.2 admission
  resultDelimitationRelationRef:
  resultBoundaryCrossingRelationRefs:
  objectiveOrEvaluationRelationRef?
  supervisionOrCoordinationRelationRef?
  capabilityEnvelopeRef?
  roleAssignmentRefs?
  methodOrMechanismRefs?
  transformationParticipationRefs?
  workOccurrenceRefs?
  functioningRelationRefs?
  architectureClaimRefs?
  evidenceOrAssuranceRefs?
  temporalOrDynamicsRefs?
  blockedOverreads:
```

This slice is not a U-kind. It is the system-result part of the B.2 record, written so that every system-dependent claim can return to its direct owner.

#### B.2.2:4.2 - System Participation Re-Basing

When the result is `U.System`, re-base system participation slots for the result system:

- role assignments through `A.2.1` and role-relation owners;
- capabilities through `A.2.2` and `C.16`;
- methods and mechanisms through `A.15`, `A.6.1`, and their current direct owners;
- transformations through `A.3.4`;
- work occurrences through `A.15.1`;
- functioning and functional structure through `A.6.F` and `C.30.TFS-REL`;
- architecture through `C.30`, `A.22`, and `C.30.ASV`;
- evidence and assurance through `A.10`, `B.3`, and `B.3.5`;
- temporal and dynamics claims through `C.27`, `A.19`, and the direct temporal owners.

Do not reuse old component evidence as if it automatically covered the result system. Carry continuities by explicit relation; re-declare changed slots for the result system.

#### B.2.2:4.3 - System Trigger Interpretation

The B.2 trigger profile can be interpreted for systems as follows:

| Trigger family in `MHTTriggerProfile@Context` | System-result reading | Direct owner kept visible |
| --- | --- | --- |
| Delimitation change | The operating whole now has an external delimitation and crossing relations that differ from the old aggregate. | `A.1`, `B.1.2`, `A.14`, `C.13` |
| Objective or evaluation change | The whole is now evaluated by a system-level objective, mission, SLO, safety case, or viability claim. | `C.16`, `E.13`, `A.10`, decision or assurance owners |
| Supervision or coordination change | A controller, protocol, governance relation, or distributed coordination relation regulates constituent behavior for the result whole. | `B.2.5`, `A.12`, `A.3.4`, `A.15.1` |
| Capability or closure evidence | The capability envelope belongs to the result system, not to any one constituent alone. | `A.2.2`, `C.16`, `B.2.4` when whole reidentification is current |
| Agency threshold | The result whole crosses a concern-specific agency threshold in characteristic space. | `A.13`, `A.19`, `C.16` |
| Temporal consolidation | A commissioning, phase, release, or operating-time consolidation changes the current system identity claim. | `C.27`, `A.15.1`, temporal owners |
| Context reframe | The relevant bounded context changes the operating whole under concern. | `A.1`, bounded-context owners, architecture owners |

No single row is enough by itself. The row names evidence to inspect. B.2 decides whether the whole must be reidentified.

#### B.2.2:4.4 - Delimitation and External Acting Systems

For system-result MHT, distinguish:

- a part of the result system;
- an external acting system that changes the result system or a constituent;
- an environment or resource that participates in work;
- a description, dashboard, twin, model, diagram, or publication about the result system.

A lathe making a workpiece, a controller steering a plant, or a teacher changing a learner does not become a super-holon merely because it changes another holon. Use `A.12`, `A.3.4`, and `A.15.1` for acting side, transformation, and work. Use part-whole owners only when parthood itself is admitted.

#### B.2.2:4.5 - Assurance Re-Basing

When `mhtResultSystemRef` is admitted, old assurance must be tested against the result system.

Ask:

- Which component evidence still applies unchanged?
- Which evidence applies only through explicit correspondence or source-use relation?
- Which assurance claims must be rewritten for the result system?
- Which architecture, capability, functioning, work, temporal, or evidence claims now have different owners?

The result system can inherit evidence only through named relations. It does not inherit safety, reliability, responsibility, or performance claims by label.

