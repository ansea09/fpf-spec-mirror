---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "System-Role Kinds and Assignments"
section_id: "A.2:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__007_archetypal-grounding.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "A.2 — System-Role Kinds and Assignments"
  - "A.2:5 — Archetypal Grounding"
line_start: 2923
line_end: 3011
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10.ROLE"
  - "F.4-F.6"
keywords:
  - "U.SystemRoleAssignment"
  - "ambiguous role wording"
  - "assignment"
  - "holder System"
  - "local System classification"
  - "system-role kind"
  - "work-facing contribution"
---

### A.2:5 - Archetypal Grounding

#### A.2:5.1 - Reviewer Membership and a Non-Circular Subkind

The JournalReview practice declares one local kind from its practice boundary, contribution distinction, and direct holder features:

```text
ReviewerSystemRole : U.Kind
  localPracticeOrSourceBoundary: JournalReview-2026
  localIdentityBasis:
    the assignable contribution distinction “can supply a substantive review judgment
    meeting the current JournalReview acceptance conditions”

KindSignature@ReviewerSystemRole/e3:
  EntityOfConcern: ReviewerSystemRole
  candidateValueKind: U.System
  membershipCriterion:
    one current A.2.2 capability instance has the candidate system as holder,
    names substantive-review Work or its review-judgment result class,
    and satisfies its declared envelope, measures, and currentness;
    the current JournalReview capability-fit predicate confirms the submission,
    review-phase, and judgment-quality conditions for this slice
  sliceApplicabilityConditions:
    the submission, review phase, and temporal selector
  effectiveReferenceScheme: JournalReview-Scheme-2026/e3
  assumptionsAndDependencies:
    the capability instance, currentness condition, and capability-fit predicate
```

The capability and fit predicate are governed under A.2.2. They are features used by the criterion, not substitutes for the kind or judgment. One application can therefore state:

```text
J(Alice, ReviewerSystemRole, KindSignature@ReviewerSystemRole/e3, ReviewSlice-17) = true
J(Alice, ReviewerSystemRole, KindSignature@ReviewerSystemRole/e3, LaterSlice-18) = false
```

The later result follows only from a known failed currentness or fit condition. Ending an assignment alone changes neither judgment because this signature does not use assignment as a feature. If a dependency is unavailable, the result is `unknown`.

For `RoboticsEngineerSystemRole U.SubkindOf EngineerSystemRole`, evaluate the two aligned signatures independently for every admitted candidate and slice needed by the declared domain. Only after every defined true narrower judgment implies a true broader judgment may C.3.1 admit the relation. The proposed edge proves neither judgment. An independently obtaining robotics assignment also proves neither judgment unless the relevant signature explicitly uses it as a non-circular feature.

#### A.2:5.2 - Pump in a Cooling Loop

`CoolingCirculatorSystemRole` is a local kind in `PlantOperations-2026`. Its identity is the assignable plant-operation contribution, while its `KindSignature` tests the directly governed circulation features needed by that contribution. `PumpUnit-3` is judged against that exact edition and slice; the judgment does not change pump identity.

When the plant also claims an assignment, it uses a directly declared species:

```text
PlantCoolingSystemRoleAssignment : U.SystemRoleAssignment
  HolderSystemSlot: U.System
  AssignedSystemRoleKindSlot: PlantOperationsSystemRoleKindDomain
  predicate:
    the holder is selected for the assigned plant-operation contribution
    under the declared operating conditions

PlantCoolingAssignment@PumpUnit3:
  HolderSystemSlot: PumpUnit-3
  AssignedSystemRoleKindSlot: CoolingCirculatorSystemRole
  assignmentInterval: [2026-06-01, open]
```

The interval is assertion content about the known extent; the occurrence continues only while the species predicate obtains without interruption for the same participants. `PlantOperationsSystemRoleVocabulary-2026`, its reference scheme, and the relevant signature can be cited as interpretation evidence. They are not extra assignment participants.

Closing the open interval later refines the same occurrence description when uninterrupted identity is preserved; the stated interval neither makes the relation obtain nor becomes another participant.

The assignment proves neither circulation capability over every operating region nor performed circulation or maintenance Work. Those claims use A.2.2, A.15.1, and the applicable Method, transformation, measurement, and evidence relations.

#### A.2:5.3 - A Standard Used in Design Work

An engineering team uses RFC 9110 while designing an HTTP service. Keep these claims separate:

1. `DesignTeam-2` independently counts under `ProtocolDesignerSystemRole` in the current slice when its signature criterion is satisfied.
2. One design-assignment occurrence may obtain as an instance of a declared `U.SystemRoleAssignment` species.
3. The RFC publication is the source episteme in the direct source-use or external-rule relation selected by the design claim.
4. Dated design Work is performed by `DesignTeam-2` under the exact assignment through F.6 and may produce a MethodDescription or SystemDescription.

The publication neither counts under the system-role kind nor performs the Work.

#### A.2:5.4 - The Same Label in Two Local Practices

An editorial-review practice and a safety-assurance practice can each declare a `ReviewerSystemRole`. They remain two local kinds because the constituting practice boundary and stable contribution distinction together form each identity basis. A shared label, vocabulary source, or reference-scheme spelling establishes neither sameness nor a Bridge.

Suppose a staffing dashboard proposes `u-reviewer-display`: show assignments from both practices in one `Reviewer` column. First recover the two exact local kinds and any F.17 cells needed by the displayed expressions; then establish only the C.3.3 kind relation and F.9 local-sense relation that the display actually consumes. State a separate C.2.1 bounded-use assertion with direction `d-safety-to-editorial-display`, rule `r-preserve-reviewer-differences`, and tolerance `t-shared-label-only`, plus polarity and effective scheme. The rule keeps the practices' admission, independence, evidence, and completion fields separate and tolerates only the shared display label.

Current A.10 provenance and `RelianceDisposition=pass` can support that display use. They do not justify substitution between assignments or merge the two kinds. If the use makes an assurance claim or crosses B.3's material-reliance threshold, only a current positive B.3 claim carrying this same use and sufficient minimum reliance safety assurance supports it; no-assurance, insufficient-record, narrowed, rejected, withdrawn, abstaining, or blocked dispositions stop or narrow the use. A Bridge Card can package the Bridge, bounded-use assertion, evidence, and disposition, but it grants no assignment, eligibility, capability, use suitability, or performed-Work inference. A selected `BoundedModelUseStructure` is cited only in the receiving use whose interpretation it changes.

#### A.2:5.5 - A Relation Participant Slot Named `role`

An external notation may call one relation position `role`. Apply E.10.ROLE and A.6.RSIR to recover the participant meaning and declaration-local SlotKind. Its `ValueKind` is the participant kind. The external label creates neither a system-role kind nor an assignment. A System participates in the relation as declared; it holds a system-role assignment only through a separate occurrence of a declared assignment species.

