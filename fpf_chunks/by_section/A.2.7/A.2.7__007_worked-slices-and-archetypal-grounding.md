---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "SystemRoleKindRelationStructure - Relations among System-Role Kinds"
section_id: "A.2.7:5"
section_title: "Worked Slices and Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__007_worked-slices-and-archetypal-grounding.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.2.7 — SystemRoleKindRelationStructure - Relations among System-Role Kinds"
  - "A.2.7:5 — Worked Slices and Archetypal Grounding"
line_start: 6510
line_end: 6636
dependencies:
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.22"
  - "A.6.REL"
  - "C.3"
  - "C.3.1"
  - "E.10.ROLE"
keywords:
  - "U.SubkindOf"
  - "incompatibility"
  - "joint assignment requirement"
  - "relations among system-role kinds"
  - "selected structure"
  - "substitution"
---

### A.2.7:5 - Worked Slices and Archetypal Grounding

#### A.2.7:5.1 - Manufacturing Admission Substitution

Plant A admits `SeniorHydraulicsTechnicianSystemRole` and `HydraulicsTechnicianSystemRole` as exact local kinds. During 2026H2, the pressure-test admission Method uses this rule: an assignment to the senior kind may satisfy the condition written for the technician kind only for `PumpPressureTestMethodFamily` and only while the candidate assignment satisfies A.2.5 predicate `PressureTestReady`.

The direct species uses the local `PlantMaintenanceSystemRoleKindDomain`:

```text
PlantPressureTestSystemRoleKindSubstitution :
  U.Relation
RelationSignature:
  CandidateSystemRoleKindSlot:
    PlantMaintenanceSystemRoleKindDomain, ByValue
  RequiredSystemRoleKindSlot:
    PlantMaintenanceSystemRoleKindDomain, ByValue
  AdmissionSubstitutionPredicateSlot:
    PlantPressureTestAdmissionSubstitutionPredicate, ByValue
```

The predicate names the ordered two kinds, receiving Method family, `PressureTestReady` rule, 2026H2 applicability, and the exact semantic basis whose edition changes either clause. `PlantMaintenanceRoles-2026` and `Plant-A-Maintenance-Scheme` may be cited in the assertion; they are not extra relation participants. If a later compatible edition preserves all identity-bearing clauses, an explicit continuity decision preserves the predicate. Otherwise another predicate and occurrence are required.

```text
PlantPressureTestSubstitutionAssertion:
  entityOfConcernRef: Plant-A-Pressure-Test-Substitution-2026H2
  ClaimGraph:
    directClaimFamilyRef:
      PlantPressureTestSystemRoleKindSubstitution
    participantDesignations:
      CandidateSystemRoleKindSlot:
        SeniorHydraulicsTechnicianSystemRole
      RequiredSystemRoleKindSlot:
        HydraulicsTechnicianSystemRole
      AdmissionSubstitutionPredicateSlot:
        PlantPressureTestAdmissionSubstitutionPredicate
    assertionPolarity: affirmative
    systemRoleKindRelationExtent: [2026-07-01, 2026-12-31]
```

The system performing admission checking resolves the candidate's exact A.2.1 assignment and its current `PressureTestReady` state occurrence. Those are inputs to the receiving rule, not substitution-relation participants. Capability is checked separately. A claim about performed pressure-test Work needs its own A.15 basis.

#### A.2.7:5.2 - Safety Separation of Duties

For one hazard-analysis Work item, the same system must not hold both author and approver assignments during overlapping windows. The direct species uses the exact `SafetyCaseSystemRoleKindDomain` and a predicate identified by the unordered pair `{HazardAnalysisAuthorSystemRole, HazardAnalysisApproverSystemRole}`, same-holder rule, same-Work rule, overlap test, applicability, and meaning-bearing semantic basis.

```text
HazardAnalysisAuthorApproverIncompatibility :
  U.Relation
RelationSignature:
  IncompatibleSystemRoleKindSlot[1]:
    SafetyCaseSystemRoleKindDomain, ByValue
  IncompatibleSystemRoleKindSlot[2]:
    SafetyCaseSystemRoleKindDomain, ByValue
  IncompatibilityPredicateSlot:
    HazardAnalysisSeparationPredicate, ByValue
```

The predicate has characterized these kinds continuously since 2026-01-01. A particular pair of assignments with the same holder and Work item during overlapping windows is a later case satisfying the rule; it does not create the kind relation.

```text
HazardAnalysisAuthorApproverIncompatibilityAssertion:
  entityOfConcernRef:
    HazardAnalysisAuthorApproverIncompatibility-2026
  ClaimGraph:
    directClaimFamilyRef:
      HazardAnalysisAuthorApproverIncompatibility
    participantDesignations:
      IncompatibleSystemRoleKindSlot[1]:
        HazardAnalysisAuthorSystemRole
      IncompatibleSystemRoleKindSlot[2]:
        HazardAnalysisApproverSystemRole
      IncompatibilityPredicateSlot:
        HazardAnalysisSeparationPredicate
    assertionPolarity: affirmative
    systemRoleKindRelationExtent: [2026-01-01, open]
```

A verifier system applies the work-admission Method to two exact assignment occurrences and the target Work item. The checking Work produces the receiving decision.

#### A.2.7:5.3 - Clinical Joint Admission

A surgical MethodDescription states a joint rule: assignments to `SurgeonSystemRole`, `AnesthetistSystemRole`, and `ScrubPractitionerSystemRole` must be held by three distinct systems throughout the procedure window selected by the receiving check.

```text
OperatingTheatreThreeSystemRoleBundle :
  U.Relation
RelationSignature:
  BundledSystemRoleKindSetSlot:
    OperatingTheatreSystemRoleKindDomain, ByValue
  JointAdmissionPredicateSlot:
    ThreeDistinctHoldersForProcedurePredicate, ByValue
```

The set is order-insensitive. The predicate names the three exact kinds, distinct-holder rule, full-window rule, procedure applicability, and meaning-bearing semantic basis. The taxonomy episteme and clinical reference scheme may help an assertion designate or interpret the kinds; they are not participants of the bundle relation.

```text
OperatingTheatreThreeSystemRoleBundleAssertion:
  entityOfConcernRef: OperatingTheatreThreeSystemRoleBundle-2026
  ClaimGraph:
    directClaimFamilyRef: OperatingTheatreThreeSystemRoleBundle
    participantDesignations:
      BundledSystemRoleKindSetSlot:
        {SurgeonSystemRole,
         AnesthetistSystemRole,
         ScrubPractitionerSystemRole}
      JointAdmissionPredicateSlot:
        ThreeDistinctHoldersForProcedurePredicate
    assertionPolarity: affirmative
    systemRoleKindRelationExtent: [2026-01-01, open]
```

For one planned procedure, the receiving check separately names its evaluation window and resolves three independently obtaining assignments. The bundle supplies the allocation rule; the three system-role kinds remain distinct even when the holders form one procedure team. Credentials, state, capability, gate decisions, and procedure Work remain separate.

#### A.2.7:5.4 - Robotics Kind Order and Independent Musician Assignment

The lab proposes:

```text
RoboticsEngineerSystemRole U.SubkindOf EngineerSystemRole
```

The proposal is not a premise for classifying Vasya or any other system. Under the exact aligned `KindSignature` editions and effective reference-scheme edition, direct robotics-engineering features are evaluated against both kinds. Only if every defined true `RoboticsEngineerSystemRole` judgment implies a true `EngineerSystemRole` judgment may C.3.1 establish the relation.

A known robotics-engineer `true` with engineer `false` refutes the relation. If a dependency required by the broader judgment is unavailable, the result is `unknown` and the order remains unresolved. A restriction concerning only one Method family, project phase, or allocation condition that fails monotonicity uses a residual qualification relation instead.

Vasya may separately hold assignments to `RoboticsEngineerSystemRole` and `MusicianSystemRole`. Those assignment identities and extents remain under A.2.1. Robot-engineering Work, music-performance Work, and teaching-robots-music Work remain A.15 occurrences. Establish capability and admission substitution separately when the receiving use needs them.

