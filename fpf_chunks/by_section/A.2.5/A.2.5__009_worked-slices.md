---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation - Windowed Role-State Recognition and Work Admission"
section_id: "A.2.5:6"
section_title: "Worked Slices"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__009_worked-slices.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "A.2.5 — RoleStateRelation - Windowed Role-State Recognition and Work Admission"
  - "A.2.5:6 — Worked Slices"
line_start: 4610
line_end: 4670
dependencies:
  - "A.15"
  - "A.2.1"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:6 - Worked Slices

#### A.2.5:6.1 - Robot Inspection After Recalibration

`Robot-7` already has the assignment occurrence governed by `A.2.1`:

```text
RoleAssignmentAssertion@Robot7Inspection:
  participantDesignations:
    HolderSystemSlot: Robot-7
    RoleValueSlot: InspectorRole
    RoleTaxonomyEpistemeSlot: MaintenanceRoles-2026
    EffectiveReferenceSchemeSlot: Maintenance-Scheme-A
  assignmentInterval: [2026-07-13T09:00, 2026-07-13T17:00]
```

The method description for a bearing inspection declares the by-value admission predicate `InspectionReady`, interpreted as calibration current, clock synchronization inside the declared tolerance, operating-envelope fit, and no active quarantine relation throughout the inspection window. The following filled assertion refers to one obtaining role-state occurrence; it is not the `RelationSignature` and does not create the occurrence by being recorded.

```text
RoleStateAssertion:
  directClaimFamilyRef: A.2.5 RoleStateAssertion
  RoleAssignmentSlot: Robot-7-InspectorAssignment-2026-07-13
  StatePredicateSlot:
    DesignatorUnderScheme: InspectionReady under Maintenance-Scheme-A
    TruthCondition: CalibrationCurrent(Robot-7)
                    and ClockSynchronizationWithinTolerance(Robot-7)
                    and InspectionOperatingEnvelopeFit(Robot-7)
                    and no ActiveQuarantineRelation(Robot-7)
    TemporalReading: continuous truth over the declared inspection interval
  assertionPolarity: affirmative
  roleStateExtent: [2026-07-13T09:20, 2026-07-13T12:00]
```

The calibration report is a `U.Episteme`. An A.2.4 evidence-use relation targets the assertion that this role-state occurrence obtains. At noon the declared calibration-validity interval ends, so `InspectionReady` ceases to hold under its own truth condition. The evidence-use relation may also cease to support a current assertion when its relevance interval ends, but that is a separate claim. The assignment continues until 17:00. Recalibration at 12:30 can begin another `InspectionReady` occurrence under the same assignment.

#### A.2.5:6.2 - Drive Motor in a Pump Assembly

`Motor-M1` holds `DriveMotorRole` under `PumpAssemblyRoles-v4` and `Pump-A-Operating-Scheme`. The current work claim needs `DriveReady`, whose predicate names the exact supply relation, torque capability-fit relation, thermal band, and installed-connection relation.

The pump assembly is the grounding system for those claims. It is not a mandatory context slot. No `BoundedModelUseStructure` is needed because the role taxonomy, scheme, assignment, direct physical relations, and state window determine the claim.

This case also shows why capability and role state differ. The motor can retain torque capability while a missing supply relation makes `DriveReady` false. Conversely, an affirmative current `DriveReady` assertion does not say that pumping work has occurred, and its receiving-use reliance remains separately governed.

#### A.2.5:6.3 - Socially Constituted Credential State

A clinician holds `ProcedureOperatorRole` for one shift. The selected admission predicate `CredentialCurrentForProcedure-X` depends on an accepted credential decision, its declared validity interval, and absence of a suspending decision.

Here the accepted decision relation helps constitute the institutional predicate because the credential ontology says so. A certificate publication may evidence that decision, but the publication does not substitute for it. The role-state occurrence still has assignment and predicate as its participants and derives its actual extent from uninterrupted obtaining; evidence and publication remain direct neighboring relations.

#### A.2.5:6.4 - DDD Model-Use Structure Changes a Receiving Interpretation

`ApprovalService-2` holds `ApproverRole`. In one selected model-use structure, `ApprovalReady` concerns a fulfilment-state change. In another, the same source label concerns payment authorization. The generic `RoleStateRelation` still has only the exact assignment and by-value predicate as participants.

When the fulfilment-side assertion is evaluated, its ClaimGraph or receiving-use relation may designate `Orders-Fulfilment-ModelUseStructure` beside the state claim. That designation selects how the receiving use interprets the predicate; it does not enter the generic relation signature or occurrence identity. The structure must already exist under `A.1.1`. It neither evaluates `ApprovalReady` nor performs approval work.

#### A.2.5:6.5 - Approved Standard or Evidence Dataset Is a Different Relation

Suppose a project says, "Standard S is approved." The standard is an episteme, not a system holding a work-facing role. Recover the direct status-use, decision, source-use, or publication-use relation.

Likewise, a dataset or report described as having an "evidence role" remains an episteme used through direct evidence, source, measurement, freshness, provenance, or assurance relations. Apply A.2.5 only if an admitted system's role assignment has a by-value predicate whose truth condition depends on one of those separately governed relations; neither the standard nor dataset becomes the holder, state, or role-state occurrence.

