---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__006_archetypal-grounding.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:5 — Archetypal Grounding"
line_start: 25318
line_end: 25378
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "U.WorkPlan"
keywords:
  - "WorkPlan claim content"
  - "actual-use predicate"
  - "baseline replay"
  - "concrete RefKind and policy"
  - "direct owner"
  - "edition pin"
  - "exact declaration member"
  - "intended-performance designator"
  - "no actuality by plan"
  - "open-world omission"
  - "participant/argument/result meaning"
  - "positive planned designation"
  - "semantic cardinality"
---

### A.15.3:5 - Archetypal Grounding

#### A.15.3:5.1 - Planned holder designation against the admitted role-assignment declaration

An inspection team plans a later role assignment and chooses `Robot_8_Ref` as the holder system. **Plan result:** one row points to the cited `RoleAssignmentRelationSignature` edition and its `HolderSystemSlot`; `Robot_8_Ref : U.EntityRef` resolves to admitted `Robot_8 : U.System`. A.2.1 defines the assignment predicate and occurrence identity, while A.6.5 defines the declaration-local SlotKind, ValueKind, and reference mode.

The row establishes neither a `U.RoleAssignment` nor actual participation. Later, an affirmative assignment assertion is available only when all four participants are designated and the A.2.1 predicate holds continuously for them. A type-compatible planned holder can therefore remain the baseline while that predicate either fails under a stated negative criterion or cannot yet be resolved.

**Blocked near-miss:** `Bearing_C isPartOf Pump_P` cannot supply a relation row. A.6.5:5.2 keeps `PartHolonSlot` and `WholeHolonSlot` hypothetical until a part-relation pattern defines their meanings, predicate, applicability, and occurrence identity. Return `missing-governor: planned part-relation participant designation for <Bearing_C, Pump_P>` or keep the choice as ordinary A.15.2 plan content; do not present the sketch as an admitted `RelationSignature`.

#### A.15.3:5.2 - Planned argument and expected result against A.6.1

A team plans one Pump #37 recognition evaluation. It expects the application to use Pump #37 as `candidate` and return `true` if the cited criterion, construction facts, reidentification rule, interpretation basis, and required fastening-relation fact are available and determine satisfaction. The condition reference records that expectation; it makes none of those claims true. `Pump37-Classification-Plan-E1_Ref` identifies the WorkPlan, `HolonRecognitionMechanism-E1_Ref` identifies the cited A.6.1:5.7 mechanism edition, and `Pump37-ExpectedTrue-Conditions-E1_Ref` identifies the separate condition claims.

The WorkPlan carries this copyable planning content:

```text
SlotFillingsPlanItem:
  planItemDesignator: pump37-recognition-baseline
  workPlanRef: Pump37-Classification-Plan-E1_Ref

  intendedPerformanceDesignator: planned-pump37-recognition-use-01
  plannedFillingRows:
    - rowDesignator: candidate-pump37
      targetDeclarationRef: HolonRecognitionMechanism-E1_Ref
      targetOperationDesignator: recognizeAdmittedHolonCandidate
      targetMemberDesignator: candidate
      targetMemberFamily: OperationArgumentDeclaration
      memberDefinitionPattern: A.6.1
      plannedValueOrDesignation: Pump_37_Ref
      planningConditions: Pump37-ExpectedTrue-Conditions-E1_Ref
      declarationEditionPin: HolonRecognitionMechanism-E1
    - rowDesignator: expected-recognition-true
      targetDeclarationRef: HolonRecognitionMechanism-E1_Ref
      targetOperationDesignator: recognizeAdmittedHolonCandidate
      targetMemberDesignator: recognitionJudgment
      targetMemberFamily: OperationResultDeclaration
      memberDefinitionPattern: A.6.1
      plannedValueOrDesignation: true
      planningConditions: Pump37-ExpectedTrue-Conditions-E1_Ref
      declarationEditionPin: HolonRecognitionMechanism-E1
```

In that operation declaration, `candidate` accepts exactly one `U.Entity` through a `U.EntityRef`; `recognitionJudgment` returns exactly one carried-by-value member of `RecognitionJudgmentValue = {true, false, unknown}`. The rows cite those rules instead of redeclaring them.

Later, A.6.1 identifies `Pump37RecognitionApplication-2026-07-21T100000Z`. The application binds Pump #37 as `candidate`, but a required fastening-relation fact is unavailable, so it returns `unknown`. **Comparison result:** the plan expected `true` under its cited conditions; the actual application returned `unknown` because one availability condition failed. An A.6.RCD disposition-2 local compound assertion may state that comparison from the preserved plan edition, application, result binding, and failed condition. It neither rewrites a row nor admits a universal planned-to-actual relation.

The plan rows themselves identify no application, bind no candidate, return no result, prove no A.1 criterion, create no result episteme, and warrant no claim. Those later facts remain with A.6.1, A.1, C.2.1, and the applicable evidence or assurance patterns.

#### A.15.3:5.3 - Hardware-acceptance pseudo-slots rejected

A hardware acceptance method says to use a calibrated instrument, selected reference plane, calibration record or certificate, and threshold. That sentence describes a method; it declares no A.6.5 SlotSpecs. Keep those choices as ordinary A.15.2 plan content, each under the pattern that defines the plane, calibration or evidence reference, and threshold.

Open A.15.3 only when an A.6.1 declaration, a `RelationSignature` SlotSpec, or another declared member already defines both the position and its actual-use rule. Otherwise return `missing-governor` for typed reuse; do not wrap the method description or fixture card in a fictitious slot-bearing declaration. Measurement, evidence sufficiency, readiness, acceptance, and actual instrument use remain separate.

#### A.15.3:5.4 - Edition-sensitive selector or archive planning

A selector or archive plan may need to preserve a comparator, descriptor definition, distance definition, evidence policy, or another edition-sensitive choice. A suite description, archive card, or generated view does not make those labels declaration members.

If a cited declaration exposes an A.6.1 argument or result, a `RelationSignature` SlotSpec, or another member whose defining pattern supplies its meaning, actual-use predicate, and cardinality, record one A.15.3 row per chosen member and pin only editions that affect the plan. Otherwise keep the choice as ordinary A.15.2 content or return `missing-governor` for typed reuse. The later application, dated work, archive or selection result, evidence path, publication, and variance remain separate; the card is a read-only view.

