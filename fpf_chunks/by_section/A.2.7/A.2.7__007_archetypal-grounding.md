---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "Role Relation Structure - Substitution, Incompatibility, Qualification, and Joint Admission"
section_id: "A.2.7:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__007_archetypal-grounding.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "A.2.7 — Role Relation Structure - Substitution, Incompatibility, Qualification, and Joint Admission"
  - "A.2.7:5 — Archetypal Grounding"
line_start: 5953
line_end: 6061
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

### A.2.7:5 - Archetypal Grounding

#### A.2.7:5.1 - Manufacturing Admission Substitution

`PlantMaintenanceRoles-2026` under `Plant-A-Maintenance-Scheme` interprets two role values. Throughout 2026H2, the operating Plant-A pressure-test admission method applies this fixed conditional rule: a current assignment to `SeniorHydraulicsTechnicianRole` may satisfy the condition written for `HydraulicsTechnicianRole` in `PumpPressureTestMethodFamily` only while the exact A.2.5 `PressureTestReady` predicate obtains. The current method configuration and observed admission-gate behavior establish that this rule truthfully characterizes those two interpreted role values for the interval; the fact is not inferred merely from a taxonomy row.

Those case facts satisfy the direct `RoleAdmissionSubstitutionPredicate`. Because the assertion below needs one occurrence as its EntityOfConcern, explicit-individuation work applies the A.2.7 identity rule to the fixed relation species, role-value fillings, predicate, taxonomy episteme, scheme, and maximal continuous predicate-true interval. It recovers the exact occurrence `Plant-A-Pressure-Test-RoleSubstitution-2026H2` with extent `[2026-07-01, 2026-12-31]` before the assertion designates it:

```text
RoleAdmissionSubstitutionAssertion:
  entityOfConcernRef: Plant-A-Pressure-Test-RoleSubstitution-2026H2
  effectiveReferenceScheme: Plant-A-Maintenance-Scheme
  ClaimGraph:
    directClaimFamilyRef: A.2.7 RoleAdmissionSubstitutionRelation
    participantDesignations:
      CandidateAssignmentRoleValueSlot: SeniorHydraulicsTechnicianRole
      AdmissionConditionRoleValueSlot: HydraulicsTechnicianRole
      RoleAdmissionSubstitutionPredicateSlot:
        receiving method belongs to PumpPressureTestMethodFamily
        and candidate assignment has an obtaining A.2.5 PressureTestReady relation
      RoleTaxonomyEpistemeSlot: PlantMaintenanceRoles-2026
      EffectiveReferenceSchemeSlot: Plant-A-Maintenance-Scheme
    assertionPolarity: affirmative
    roleRelationExtent: [2026-07-01, 2026-12-31]
```

The system performing work-admission checking resolves the proposed holder's exact `SeniorHydraulicsTechnicianRole` assignment under A.2.1 and the exact current `PressureTestReady` occurrence or assertion under A.2.5 while applying the selected method. Those objects satisfy inputs named by the substitution predicate; they are not additional substitution-relation participants. Pressure-test capability is evaluated separately under A.2.2. The substitution relation does not prove capability and does not say that pressure-test work occurred.

#### A.2.7:5.2 - Safety Separation of Duties

For one hazard-analysis work item, the same system must not both author and approve during overlapping assignment windows. Since 2026-01-01, `SafetyCaseRoles-2026` under `Safety-Assurance-Scheme` has continuously interpreted the two role values with exactly that same-holder, same-work, overlapping-window incompatibility rule. The operating work-admission method and accepted safety-control history show that the rule remains in force with no demonstrated predicate-false interval; a particular conflicting allocation is only a later case tested by the rule.

Those case facts satisfy the direct `RoleIncompatibilityPredicate`. Because the assertion below needs an exact occurrence as its EntityOfConcern, explicit-individuation work applies the symmetric A.2.7 identity rule to the fixed role-value pair, predicate, taxonomy episteme, scheme, and maximal continuous predicate-true interval. It recovers `HazardAnalysisAuthorApproverIncompatibility-2026` with extent `[2026-01-01, open]` before the assertion designates it:

```text
RoleIncompatibilityAssertion:
  entityOfConcernRef: HazardAnalysisAuthorApproverIncompatibility-2026
  effectiveReferenceScheme: Safety-Assurance-Scheme
  ClaimGraph:
    directClaimFamilyRef: A.2.7 RoleIncompatibilityRelation
    participantDesignations:
      IncompatibleRoleValueSlot[1]: HazardAnalysisAuthorRole
      IncompatibleRoleValueSlot[2]: HazardAnalysisApproverRole
      RoleIncompatibilityPredicateSlot:
        incompatible when one HolderSystem fills both exact assignments
        for the same HazardAnalysisWorkItem
        during overlapping assignment extents
      RoleTaxonomyEpistemeSlot: SafetyCaseRoles-2026
      EffectiveReferenceSchemeSlot: Safety-Assurance-Scheme
    assertionPolarity: affirmative
    roleRelationExtent: [2026-01-01, open]
```

A verifier system applies the work-admission method to two exact A.2.1 assignment occurrences and the target hazard-analysis work item. Those receiving inputs can satisfy the incompatibility rule, but they do not enter the role-value relation signature. The verifier's checking work produces the receiving pattern's rejection outcome for the overlapping allocation. The incompatibility relation neither performs verification nor produces that outcome.

#### A.2.7:5.3 - Clinical Joint Admission

A surgical method description states a joint admission rule: surgeon, anesthetist, and scrub roles must be held by three distinct systems throughout whichever procedure window the receiving check selects. Since 2026-01-01, `OperatingTheatreRoles-2026` under `Hospital-Clinical-Scheme` has continuously interpreted the fixed three-role set with that exact distinct-holder and full-window allocation rule. The operating admission method and accepted clinical-governance history establish that the rule currently characterizes the role-value set; the assignments for one planned procedure are later receiving inputs, not relation participants or occurrence creators.

Those case facts satisfy the direct `JointRoleAdmissionPredicate`. Because the assertion below needs one occurrence as its EntityOfConcern, explicit-individuation work applies the bundle identity rule to the order-insensitive role-value set, fixed predicate, taxonomy episteme, scheme, and maximal continuous predicate-true interval. It recovers `OperatingTheatreThreeRoleBundle-2026` with extent `[2026-01-01, open]` before the assertion designates it:

```text
RoleBundleAssertion:
  entityOfConcernRef: OperatingTheatreThreeRoleBundle-2026
  effectiveReferenceScheme: Hospital-Clinical-Scheme
  ClaimGraph:
    directClaimFamilyRef: A.2.7 RoleBundleRelation
    participantDesignations:
      BundledRoleValueSetSlot:
        {SurgeonRole, AnesthetistRole, ScrubPractitionerRole}
      JointRoleAdmissionPredicateSlot:
        for the declared receiving procedure window:
        each role has one obtaining A.2.1 assignment;
        the three HolderSystems are distinct;
        every assignment extent covers that window
      RoleTaxonomyEpistemeSlot: OperatingTheatreRoles-2026
      EffectiveReferenceSchemeSlot: Hospital-Clinical-Scheme
    assertionPolarity: affirmative
    roleRelationExtent: [2026-01-01, open]
```

For the planned procedure `[2026-07-13T08:00, 2026-07-13T14:00]`, the receiving check records that interval as `declaredRoleRelationEvaluationWindow` and resolves the three exact assignment occurrences separately. The bundle relation supplies the allocation rule; the check supplies the current fillings. Clinical credentials, current readiness, and procedure-specific capability remain separate assertions. The procedure team is not created as a role value by naming this bundle.

#### A.2.7:5.4 - Robotics Qualification and Independent Musician Assignment

Since 2026-01-01, `MusicalRobotLabRoles-2026` under `Musical-Robot-Lab-Scheme` has continuously interpreted `RoboticsEngineerRole` as narrowing `EngineerRole` by participation concerning robotics systems and `RoboticsEngineeringMethodFamily`. The lab's current interpretation practice and accepted role-semantics history agree on that exact restriction with no demonstrated predicate-false interval; a shared word stem or nested taxonomy row alone would not establish it.

Those case facts satisfy the direct `RoleQualificationPredicate`. Because the assertion below needs one occurrence as its EntityOfConcern, explicit-individuation work applies the directional A.2.7 identity rule to the fixed role-value fillings, predicate, taxonomy episteme, scheme, and maximal continuous predicate-true interval. It recovers `RoboticsEngineerQualification-2026` with extent `[2026-01-01, open]` before the assertion designates it:

```text
RoleQualificationAssertion:
  entityOfConcernRef: RoboticsEngineerQualification-2026
  effectiveReferenceScheme: Musical-Robot-Lab-Scheme
  ClaimGraph:
    directClaimFamilyRef: A.2.7 RoleQualificationRelation
    participantDesignations:
      QualifiedRoleValueSlot: RoboticsEngineerRole
      BaseRoleValueSlot: EngineerRole
      RoleQualificationPredicateSlot:
        engineering participation interpreted for robotics systems
        and the RoboticsEngineeringMethodFamily
      RoleTaxonomyEpistemeSlot: MusicalRobotLabRoles-2026
      EffectiveReferenceSchemeSlot: Musical-Robot-Lab-Scheme
    assertionPolarity: affirmative
    roleRelationExtent: [2026-01-01, open]
```

Vasya may separately hold `RoboticsEngineerRole` and `MusicianRole` through two exact `U.RoleAssignment` occurrences. Those assignment identities and extents remain under A.2.1. Robot-engineering work, music-performance work, and teaching-robots-music work remain A.15 work occurrences. If a method description written for `EngineerRole` allows admission of the robotics assignment, add a separate substitution relation; qualification alone does not settle that use.

