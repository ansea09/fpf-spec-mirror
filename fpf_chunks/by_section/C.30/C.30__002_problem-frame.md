---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Grounded Architecture and Selected-Structure Adequacy"
section_id: "C.30:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__002_problem-frame.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "C.30 — Grounded Architecture and Selected-Structure Adequacy"
  - "C.30:1 — Problem frame"
line_start: 70335
line_end: 70390
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "F.18"
  - "G.5"
  - "G.6"
keywords:
  - "ArchitectureClaim"
  - "ArchitectureOf@Context"
  - "ArchitectureRelation"
  - "actual and candidate architecture"
  - "architecture question"
  - "grounded architecture"
  - "next architecture move"
  - "selected structure"
---

### C.30:1 - Problem frame

Use this pattern when you need to recover or consider the architecture of a particular holon (`U.Holon`) and choose the next architecture action. Distinguish actual relations and selected structure from a candidate or expected structure, and distinguish that subject from claims and descriptions about it.

For an actual architecture claim, recover the obtaining subject relations, the selected A.22 structure and whether the direct `ArchitectureRelation` obtains. For a candidate or expected arrangement, state that mode without inventing actual relations. In either case, identify the holon, structure kind, concern, intended use and next move; constitute a C.2.1 claim when the receiving use needs one.

The first useful architecture move is small. In ordinary prose, name the holon; say whether the structure is actual, candidate, or expected; name the structure kind and architecture concern; state how any inspected material is being used; and give the next move. If one or two sentences make those values clear, stop.

For example: “For the payment system, the diagram shows a candidate module-interface structure, not an established architecture relation. Next recover the actual dependency relations before deciding whether to replace the fraud-scoring module.” This is already a usable result and may be retained or shared as written. Use the card below when the receiving use needs its distinctions organized beyond what that ordinary account supplies:

```text
ArchitectureQuestionCard@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureQuestionProjectUseRelationRef?: U.RelationRef, only when a named pattern defines this project-use relation and the occurrence obtains
  architectureClaimRef?: ArchitectureClaimRef
  describedHolonRef:
  architectureRelationDisposition:
    actualRelationNamed | actualRelationStillToRecover |
    candidateOrExpectedOnly | nonArchitectureQuestion
  architectureRelationRefs?: FinSet(U.RelationRef)
  claimScope?:
  effectiveReferenceScheme?:
  modelUseStructureRef?: only when one selected bounded model-use structure changes this architecture use
  architectureConcernCue:
  architectureConcernClaimRefs?: FinSet(U.EpistemeRef)
  sourcePhrase?, if useful:
  questionDisposition:
    concernCueOnly | problemCardReady | architectureClaimReady | nonArchitectureClaimReady
  selectedStructureRefs?: FinSet(U.StructureRef)
  candidateOrExpectedStructureRefs?: FinSet(U.StructureRef)
  selectedStructureKindRefs or candidateStructureKindRefs:
  inspectedMaterialUse, if current: claim content | description | view | representation | publication form | source | decision | mathematical lens | other exact use
  inspectedMaterialUseRelationRefs?: references to exact obtaining relations that establish the inspected-material use
  firstArchitectureMove:
  architectureDescriptionBridge, if durable description use is current:
  claimPatternRefs?: FinSet(PatternRef), if another claim is being made:
  non-admissible overread:
```

The card can stop before a durable claim. An `actualRelationNamed` result requires exact obtaining `ArchitectureRelation` occurrences and their A.22 structure participants. A candidate, planned, required, desired, expected, modeled, or diagrammed structure remains in `candidateOrExpectedStructureRefs` and makes no subject relation obtain.
`architectureConcernCue` is recognition wording only until it helps choose one selected structure kind and one architecture move. When a controlled cue is useful, use `changeLocalization`, `substitutionOrReplacement`, `flowBottleneck`, `controlOrRateMismatch`, `dataCustodyOrStateResidence`, `physicalSeparationOrPlacement`, `evidenceReuseOrAssuranceReuse`, `scaleWindowOrCoarseningLoss`, `runtimeFailureMode`, `crossScopeResidual`, `descriptionViewLoss`, or `otherDeclared`. Local phrases such as change localization failure, hidden crossing, source return, generated-view loss, or state-residence uncertainty may remain in `sourcePhrase?` or Plain prose. If the described holon, distinction between actual and candidate structure, architecture concern, and first move cannot yet be named, set `questionDisposition` to `concernCueOnly` or `problemCardReady`; wording alone promotes neither a claim nor an obtaining relation.

`ArchitectureQuestionCard@Project` is a triage aid for choosing one architecture move. `questionDisposition` records whether to keep a concern cue, prepare a separate `ProblemCard`, constitute an `ArchitectureClaim`, or name the pattern for a non-architecture claim. `architectureRelationDisposition` separately records whether an actual direct relation has been recovered or the content is candidate or expected only. `claimPatternRefs` contains PatternIDs whose content defines, constrains, or tests any separate claim; it does not identify a pattern-application occurrence. The card is not an evidence record, gate, decision, release record, quality score, risk rating, or publication-use authority claim.

Across C.30, `@Project` in a record name is a compatibility and retrieval cue only. It identifies neither a project entity nor a composite project `U.Work`, and it establishes no context, authority, viewpoint, or parthood. When the card is genuinely local to one actual project, `projectWorkOccurrenceRef` identifies the exact composite `U.Work` recovered under A.15.6. Include `architectureQuestionProjectUseRelationRef` only when a named pattern defines the relation by which this card use concerns that Work and an occurrence of that relation obtains. A Work reference alone does not establish project locality. If that locality matters but the relation is not yet defined, record `missing-governor`; if locality does not matter, omit both project-local fields. Description publication and other project-local uses follow the same rule. A described holon, architecture claim, or architecture relation does not become project Work by retrieval suffix.

Use the `ArchitectureDescription` bridge when the next architecture move depends on a description whose subject, correspondence or use conditions need recovery. Cross-team reuse or a regulated use can create that need; retaining an already sufficient explanation does not. Ordinary prose or a question card can finish the question. Use `C.30.AD` when the description itself needs construction or repair.

What goes wrong if C.30 is missed: the practitioner reasons from a document, module diagram, transformation-flow graph description, mathematical lens, benchmark, maturity score, or decision record instead of recovering the described holon, selected structures, first architecture move, and non-architecture claim kind.

What C.30 buys in practice: the practitioner can determine whether the next work concerns the actual organization, a proposed change, or the description through which it is understood. This selects a concrete architecture action and the basis it still needs.

Do not use C.30 when the question does not concern the architecture of one exact holon, an obtaining `ArchitectureRelation`, a selected architecture-relevant structure, an `ArchitectureClaim`, or the thin architecture-description bridge needed for one architecture move. Use the pattern that defines or tests the actual source, description, view, publication-use, or other non-architecture relation. If one piece remains an architecture claim, use C.30 only for that piece. Common non-architecture claim boundaries are summarized in `C.30:12`.

Thin precision-restoration pointer: if the issue under repair is still whether *architecture*, *architecture description*, *structural view*, *module diagram*, *model*, *source material*, *functional architecture*, or a source label such as *layer*, *level*, *tier*, *stack*, *block*, *expert*, *cache*, *router*, or *gate* names an architecture claim, description, view, representation, publication form, source relation, structure, or claim defined or tested by another pattern, use `C.30.P` or `C.30.STRAT` as triggered before applying C.30 to the recovered architecture portion. If the recovered issue is mathematical-lens use, apply `C.29`; when no mathematical-lens use changes the architecture work, keep ordinary prose or use `NoMathLensUseNeededNote` under C.29 rather than creating a C.30-local lens result. Keep trigger tables in those patterns; C.30 is applied only after an `ArchitectureClaim`, exact selected architecture-relevant structure, conditional `ArchitectureDescription` bridge use, `C.30.AD` application, or other claim named by value is recoverable.

