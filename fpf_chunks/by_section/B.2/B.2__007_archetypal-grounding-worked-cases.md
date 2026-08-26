---
chunk_kind: "child"
pattern_id: "B.2"
pattern_title: "Meta-Holon Transition - Whole Reidentification"
section_id: "B.2:5"
section_title: "Archetypal Grounding (Worked Cases)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2/B.2__007_archetypal-grounding-worked-cases.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "B.2 — Meta-Holon Transition - Whole Reidentification"
  - "B.2:5 — Archetypal Grounding (Worked Cases)"
line_start: 36799
line_end: 36859
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.3.4"
  - "B.1"
  - "B.1.2"
  - "B.2"
  - "B.2.2"
  - "B.2.3"
  - "B.2.4"
  - "B.2.5"
  - "B.2.P"
  - "B.3"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.29"
  - "C.30.ILC"
  - "C.32.P2S"
  - "E.24.UK"
  - "G.11"
  - "U.Episteme"
keywords:
---

### B.2:5 - Archetypal Grounding (Worked Cases)

#### B.2:5.1 - Closed-Loop Regulated System

Parts: plant, sensor, controller, actuator.

Existing-whole repair may be enough if only a sensor improved or a controller parameter changed. B.2 becomes current only when exact constructive relations and a governed assembly close the feedback and supervision around an objective, yielding one exact new whole proposed for recognition under the already admitted `U.System` kind, whose boundary, external commitments, and capability envelope are no longer explainable as changes of the existing whole. That proposed whole can satisfy A.1 only if its actual boundary, interfaces, relevant characteristics, and identity-preservation conditions also satisfy at least one applicable governed larger-assembly construction method or rule—for example, a rule under which the regulated system can remain one constituent of a larger plant or production system. If that compatibility condition does not hold, the proposed whole fails A.1; if the needed evidence or dependency is unavailable, evaluation remains `unknown`. Loop closure, a record, or a measurement supplies none of those facts.

```text
MHTTriggerProfile@Control : U.Episteme
  entityOfConcernRef: plant-plus-devices configuration
  content:
    changedSupervisionRelationRefs: closed feedback relation
    changedObjectiveClaimRef: maintain output y near reference r
    changedCapabilityClaimRef: capability envelope after closure

HolonReidentificationRecord@Control : U.Episteme
  entityOfConcernRef: regulated control system
  content:
    existingWholeRef: plant-plus-devices configuration
    selectedTriggerProfileRef: MHTTriggerProfile@Control
    existingWholeExplanationResultRef: ClosedLoopExistingWholeResult
    resultHolonRef: regulated control system
    resultHolonKindRef: U.System
    resultHolonClassificationAssertionRef: RegulatedControlSystemClassificationAssertion
    wholeReidentificationClaimRef: ClosedLoopWholeReidentificationClaim
    changedClaimPatternLocators: A.1, B.1.2, B.2.2, C.30.LCA, A.2.2
```

The exact EntityOfConcern is an actual participant in the C.2.1 `EpistemeConstitutionRelation`; `EntityOfConcernSlot` is only the corresponding declaration-local participant meaning inside `EpistemeConstitutionRelationSignature`. The `entityOfConcernRef` field and indented content fields carry participant or claim designations in each episteme; they are not SlotKinds or participants of a new MHT relation. The feedback and capability relations retain their direct identities, while the optional classification assertion retains its own C.2.1 identity and does not establish world-side holonhood.

#### B.2:5.2 - Compendium Becomes Theory

A collection of results can remain a catalogue. B.2 becomes current only when the knowledge body is reidentified as an episteme whole with its own claim-bearing structure, explanatory objective, reference scheme, and evidence relations.

`B.2.3` specializes this case when the exact candidate new holon named by the MHT claim is recognized under the already admitted `U.Episteme` kind. C.2.1 defines episteme constitution and identity; E.17 and E.24.PUB define publication occurrences, forms, and carriers; C.2.P recovers source-expression and source-to-use distinctions; A.10 and G.6 supply evidence-provenance relations when the receiving use relies on them.

#### B.2:5.3 - Capability Envelope Appears

Several systems, methods, and work occurrences align and a new capability envelope appears. Apply the direct capability, characteristic, function, transformation, method, work, evidence, and architecture patterns first.

Use `B.2.4` only when separately governed capability or functioning facts make a whole-reidentification question live under B.2. Evidence can support the claim about those facts; it creates neither the facts nor the question.

#### B.2:5.4 - Lathe And Workpiece

A lathe transforms a workpiece. That is transformation and work, not MHT and not parthood. B.2 becomes current only if the manufacturing arrangement creates or reveals a new whole that must be reidentified, such as a production cell with exact constituents, obtaining coordination and supervision relations, a governed assembly, an objective, a whole-level capability, and a reidentification rule that the earlier arrangement lacks. A.1 recognition additionally requires the cell's actual boundary, interfaces, relevant characteristics, and identity-preservation conditions to fit at least one applicable governed construction method or rule under which the cell can remain a constituent of a larger production system.

#### B.2:5.5 - Same Whole, New Whole, And Lost Evidence

Replacing Pump #37's seal is an ordinary constituent change when the pump's reidentification rule admits that maintenance phase. The same pump remains the EntityOfConcern; use the direct maintenance, part-relation, work, transformation, and characteristic patterns and stop B.2.

Closing a controller-sensor-actuator loop can yield a new regulated-system whole only when the exact candidate assembly, supervision and coordination relations, boundary, objective, whole-level capability, admitted `U.System` kind, and reidentification rule satisfy A.1 and the system criterion. Its actual boundary, interfaces, relevant characteristics, and identity-preservation conditions must also satisfy at least one applicable governed larger-assembly construction method or rule under which the regulated system can remain a constituent. If that condition fails, the candidate fails A.1; if the needed evidence or dependency is unavailable, evaluation returns `unknown`. A wiring diagram, commissioning record, loop closure, or capability measurement alone supplies none of those construction or compatibility facts.

If the support for the reidentification assertion is present and its edition is current, a person or system performing receiving work may rely on it. If the same evidence is unavailable, evaluation can return `unknown`; use G.11 to test whether the edition is current for this use; and the actor may decline, defer, or reopen. None of those branches changes whether the regulated-system whole actually exists or whether the prior configuration remains the same whole.

#### B.2:5.6 - Selected Structure And Transformation Stops

A selected `BoundedModelUseStructure` organizes exact model-use relations. It is not the new holon named by an MHT claim and gains no parts, agency, or whole identity from selection, naming, or a Context Map.

Several actual changes during assembly may each be exact `U.Transformation` occurrences. B.2 does not treat them as constituents of one composite transformation. If whole reidentification would require positive transformation composition, transformation parthood, or composite-transformation identity and no direct governor supplies contribution, compatibility, boundary, interfaces, and reidentification, retain the exact blocker and the independently identified changes. The missing composition facts do not show that any change is atomic.

