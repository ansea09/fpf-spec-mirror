---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
section_id: "A.6.5:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__006_archetypal-grounding.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "A.6.5 — Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
  - "A.6.5:5 — Archetypal Grounding"
line_start: 19386
line_end: 19434
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

#### A.6.5:5.1 - System-role assignment: first minute, substitution, and repeated occurrence

**First minute.** Assume the case facts explicitly: `Robot_7` is an admitted `U.System`; `InspectorSystemRole` is a local system-role kind; and `InspectionShiftAssignment <: U.SystemRoleAssignment` declares only two participant positions, holder System and assigned system-role kind. `InspectionShiftAssignment-17` is the occurrence with those values that obtains without interruption from 09:00 to 17:00 on 13 July. A.2.1 defines the species predicate and continuity rule; it does not inspect this robot or warrant the assertion. The stated case facts satisfy that predicate, and the `SystemRoleAssignmentAssertion` records affirmative polarity. Any evidence and reliance posture remain separately established. The following field block represents that assertion episteme under `C.29`:

```text
SystemRoleAssignmentAssertion:
  directClaimFamilyRef: A.2.1 InspectionShiftAssignment
  participantDesignations:
    HolderSystemSlot: Robot_7_Ref
    AssignedSystemRoleKindSlot: InspectorSystemRole
  assignmentInterval: [2026-07-13T09:00, 2026-07-13T17:00]
```

The two labels inside `participantDesignations` are convenient source-side labels in this compact representation. An explicit C.29 correspondence relates each label to the matching SlotKind in the `InspectionShiftAssignmentRelationSignature`; equal spelling does not identify field and SlotKind, and another source field keeps its own name. `assignmentInterval` is a different assertion field and corresponds to no relation-participant SlotSpec. `Robot_7_Ref : U.EntityRef` resolves to `Robot_7 : U.System`; `InspectorSystemRole` is carried by value under the declaration-local `InspectorSystemRoleKindDomain`. The assertion does not create the assignment, and neither the system-role kind, assertion, nor assignment performs inspection Work.

If inspection admission also needs `InspectionReady`, A.2.5 tests `InspectionShiftAssignment-17` against that exact `SystemRoleAssignmentStatePredicate`. The resulting `SystemRoleAssignmentStateRelation` is separate from the assignment and has its own maximal continuous truth interval. The assignment may continue while that state relation ceases to obtain.

**Substitution.** Assume `Robot_8_Ref : U.EntityRef` resolves to another admitted `Robot_8 : U.System`. Replacing only the `HolderSystemSlot` designation with `Robot_8_Ref` passes the declared ValueKind check, but it does not create an assignment for `Robot_8`. Current case facts must separately satisfy the direct `InspectionShiftAssignment` predicate before an affirmative assertion is warranted. The proposed designation can therefore be type-correct while the direct claim remains negative or unresolved.

**Repeated occurrence.** If the same two participants enter another inspection shift after a demonstrated non-assignment period, the A.2.1 continuity rule ends the first occurrence and starts another. A copied field block or reused row key does not merge them. Conversely, closing an open `assignmentInterval` for one uninterrupted assignment refines the same occurrence; an evidence gap alone does not split it. Under that continuing assignment, `true → false → true` for one fixed A.2.5 predicate creates two assignment-state-relation occurrences without creating another assignment.

#### A.6.5:5.2 - Hypothetical physical-assembly boundary

`Bearing_B isPartOf Pump_P` may remain a readable source claim, but current A.14 supplies no generic or installed-part occurrence-identity rule based on removal, reinstallation, installation interval, or installation work. `PartHolonSlot`, `WholeHolonSlot`, and their RefKinds are therefore only a hypothetical declaration candidate until an accepted direct part-relation pattern states the participant meanings, predicate, applicability, and same-versus-new-occurrence rule. Do not claim current conformance or an individuated part-relation occurrence from this sketch.

Conditional on such a future declaration, changing a proposed part designation from `Bearing_B_Ref` to `Bearing_C_Ref` could be ValueKind-compatible while the direct relation remains false because current case facts do not satisfy its predicate. Until that parthood relation is defined, keep the bearings, pump, installation work, proposed part relation, assertion, designations, and representation separate. The counterexample demonstrates that typed substitution cannot create obtaining; it does not supply the missing parthood settlement.

#### A.6.5:5.3 - Episteme fields are not relation participants by table shape

An evaluation episteme has an EntityOfConcernRef, contains a ClaimGraph, and states an effective ReferenceScheme under `C.2.1`. A card or tuple view may contain visible fields such as `entityOfConcernRef`, `claimGraph`, and `referenceScheme`. Their co-occurrence in one record does not by itself establish another world-side relation, make the fields participants, or declare SlotSpecs for them.

When a direct relation among an episteme and other entities is current, its definition states the relation kind, participant meanings, obtaining condition, and occurrence identity, and its compatible `RelationSignature` contains the needed SlotSpecs. A.6.5 supplies the rules for typing participant designations in a receiving assertion. This prevents a convenient episteme form from becoming a pseudo-relation merely because it can be drawn as a tuple or table.

#### A.6.5:5.4 - Relation-dependent result wording

After machining, the machined component can remain the same physical entity in a changed state. It does not acquire a special result kind. Start with one question: **did this same component continue through the change, or did a new entity begin?**

1. **Same component continued.** Name that component, the characteristic that changed, and the actual machining transformation. Use the pattern that defines that characteristic and A.3.4 for the bounded change. The component's identity continues; calling it the work's “result” adds no kind, participant meaning, or relation.
2. **A new entity began.** Use this branch only when a current definition supplies an admitted identity-inception predicate and identity rule and the current Work and change facts satisfy them. If no such definition exists, return one missing identity-inception result naming the candidate entity, relevant work and change facts, required inception predicate, and receiving use. Do not infer a generic work-result relation.
3. **The sentence names another relation.** Rewrite it with its one concrete verb and participants before declaring slots. For example, `Component_C was delivered to AssemblyCell_2` selects one candidate delivery claim about that item and receiver, not a `result` kind. Recover that direct relation's definition and any additional participant meanings it requires; if it does not close, return a missing-relation result. Handle an evaluation or acceptance sentence separately when that is the actual wording rather than listing possible pattern families.

Only the direct relation selected by one of those concrete sentences receives a compatible `RelationSignature`, and only when reusable typed use is current. Its assertion episteme records that relation; A.6.5 neither invents a broad result participant nor turns the domain choice into a catalogue.

#### A.6.5:5.5 - Formal reduced case

The expression `3 < 5` is notation carried by a mathematical assertion episteme. Its numeral occurrences, comparison sign, and left and right operand places are representation elements under `C.29`; they are not thereby FPF relation participants or SlotSpecs. When a reusable direct-relation declaration is current in an FPF use, the relation definition must identify what entities the numerals designate, the lesser-number and greater-number participant meanings, and the obtaining condition. Its `RelationSignature` may then contain local SlotSpecs such as `LesserNumberSlot` and `GreaterNumberSlot`. An explicit correspondence relates the operand places and their designations to those SlotSpecs. Operand order remains local to the mathematical representation, and the notation alone neither establishes the world-side relation nor individuates an occurrence. No receiving use in this case relies on occurrence identity, so the engineer stops at the typed assertion.

