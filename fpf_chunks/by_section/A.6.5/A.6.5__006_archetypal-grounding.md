---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
section_id: "A.6.5:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__006_archetypal-grounding.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.6.5 — Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
  - "A.6.5:5 — Archetypal Grounding"
line_start: 18373
line_end: 18414
dependencies:
  - "A.15.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.P"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.24.UK"
keywords:
---

### A.6.5:5 - Archetypal Grounding

#### A.6.5:5.1 - Physical assembly

`Bearing_B isPartOf Pump_P` can remain a readable part-relation assertion. When an engineer needs reusable participant typing in maintenance analysis, the direct mereology pattern contains the part and whole participant meanings, and its `RelationSignature` contains the `PartHolonSlot` and `WholeHolonSlot` SlotSpecs, each with ValueKind `U.Holon` and RefKind `U.HolonRef`. The actual relation participants are the bearing and pump. An assertion or relation-occurrence description episteme may designate them through references that resolve to those holons. Under A.14 and the direct part-relation identity rule, removal and reinstallation may distinguish repeated part-relation occurrences.

The bearing and pump do not become SlotKinds, and their references do not replace them as participants. Each remains a holon that participates directly in the world-side relation; the `RelationSignature` separately declares the SlotSpec used by receiving epistemes to distinguish its designation.

After replacement, changing the `PartHolonSlot` designation from `Bearing_B_Ref` to `Bearing_C_Ref` in a maintenance assertion or relation-occurrence description episteme can be type-correct while `Bearing_C isPartOf Pump_P` is still false because installation has not occurred. Exact SlotSpecs make the proposed designation reviewable; they do not substitute type correctness or reference change for the direct part-relation claim.

#### A.6.5:5.2 - Role-assignment assertion in inspection work

In this worked case, the direct role-assignment predicate already obtains, and affirmative assertion polarity is warranted under `A.2.1`; any reliance posture for a receiving use remains separately governed. The assertion designates the four required actual participants and may designate the explicitly individuated occurrence; it is not the `RelationSignature` and does not create the occurrence by being recorded. The following field block represents the assertion episteme under `C.29`:

```text
RoleAssignmentAssertion:
  participantDesignations:
    HolderSystemSlot: Robot_7_Ref
    RoleValueSlot: InspectorRole
    RoleTaxonomyEpistemeSlot: MaintenanceRoles_2026_Ref
    EffectiveReferenceSchemeSlot: MaintenanceScheme_A
  assignmentInterval: [2026-07-13T09:00, 2026-07-13T17:00]
```

The four labels inside `participantDesignations` correspond to SlotKinds in the `RoleAssignmentRelationSignature`. `assignmentInterval` is a different assertion field: it states the currently known temporal extent and corresponds to no relation-participant SlotSpec. `Robot_7_Ref : U.EntityRef` resolves to `Robot_7 : U.System`; `MaintenanceRoles_2026_Ref : U.EpistemeRef` resolves to the role-taxonomy episteme. `InspectorRole : U.Role` and `MaintenanceScheme_A : U.ReferenceScheme` are carried by value. The assignment is an obtaining relation occurrence independently of this assertion. The robot may later perform inspection work by a method. Neither the role, the assertion, nor the assignment performs that work, and the verb **holds** does not turn any of them into a holon.

#### A.6.5:5.3 - Episteme fields are not relation participants by table shape

An evaluation episteme has an EntityOfConcernRef, contains a ClaimGraph, and states an effective ReferenceScheme under `C.2.1`. A card or tuple view may contain visible fields such as `entityOfConcernRef`, `claimGraph`, and `referenceScheme`. Their co-occurrence in one record does not by itself establish another world-side relation, make the fields participants, or declare SlotSpecs for them.

When a direct relation among an episteme and other entities is current, the governing pattern contains the relation kind, participant meanings, obtaining condition, and occurrence identity, and its compatible `RelationSignature` contains the needed SlotSpecs. A.6.5 governs how a receiving assertion types its participant designations. This prevents a convenient episteme form from becoming a pseudo-relation merely because it can be drawn as a tuple or table.

#### A.6.5:5.4 - Relation-dependent result wording

After machining, the machined component can remain the same physical entity in a changed state. It does not acquire a special result kind. When a receiving claim calls it a *result*, first recover the exact current relation or relation-bearing claim: affected-referent and actual-change facts for a continuing component, an entity-identity-inception claim when a new entity first exists, or the direct measurement, evaluation, delivery, acceptance, or transfer relation when that is what the claim means. Use an entity-identity-inception governor only when a current pattern actually supplies it. If that claim or any other needed relation has no current direct governor, keep an exact missing-governor blocker instead of presuming a generic work-result relation.

Only a selected reusable direct relation receives a compatible `RelationSignature` with one SlotSpec per participant meaning. An assertion episteme may then state that exact relation. A local kind of participating entities is introduced only when typed quantification is current in a receiving use. This case demonstrates the three readings in A.6.5:4.6 without naming a participant after a broad result word.

#### A.6.5:5.5 - Formal reduced case

The expression `3 < 5` is notation carried by a mathematical assertion episteme. Its numeral occurrences, comparison sign, and left and right operand places are representation elements under `C.29`; they are not thereby FPF relation participants or SlotSpecs. When a reusable direct-relation declaration is current in an FPF use, the direct pattern content must identify what entities the numerals designate, the lesser-number and greater-number participant meanings, and the obtaining condition. Its `RelationSignature` may then contain local SlotSpecs such as `LesserNumberSlot` and `GreaterNumberSlot`. An explicit correspondence relates the operand places and their designations to those SlotSpecs. Operand order remains local to the mathematical representation, and the notation alone neither establishes the world-side relation nor individuates an occurrence. No receiving use in this case relies on occurrence identity, so the engineer stops at the typed assertion.

