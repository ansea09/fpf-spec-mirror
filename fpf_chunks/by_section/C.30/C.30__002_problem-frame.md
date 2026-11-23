---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Architecture and Selected-Structure Adequacy"
section_id: "C.30:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__002_problem-frame.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "C.30 — Architecture and Selected-Structure Adequacy"
  - "C.30:1 — Problem frame"
line_start: 74829
line_end: 74884
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

Use this pattern to establish how a holon (`U.Holon`) is organized, explain what that organization makes possible, or identify what a design would change. A description may show an existing arrangement, propose a different one or specify conditions that an arrangement has to meet.

Begin with the work the architecture account must support. Which property, relationship or unrealized requirement does the recipient need to understand? For an actual arrangement, establish which subject relations hold and how the selected A.22 structure organizes the holon. For a proposal, show how its parts would work together under the stated conditions. Constitute a C.2.1 claim when its later use requires one.

Select the structures the question turns on. Follow the constituent relation for each relevant kind of holon far enough to account for the property at issue. Where the result depends on several structures, trace the connections through which they contribute to the result under the same admissible conditions. Some connect constituents of one holon. Others connect independent holons through an exchange, a shared rule or an interaction. Establish composition where the explanation relies on it. Choose the detail of each model by asking what it would treat alike that the requested explanation or design needs to distinguish. A request to identify the next architecture action can end when that action and its grounds are clear.

For example, a team wants to know what to investigate before replacing a module. Its diagram proposes a payment-system interface. Establishing whether the running payment service actually depends on that interface is a useful next inquiry. A commission to explain the existing system requires the answer to that inquiry and what the dependency means for service behavior. Use the card below when its fields help the recipient keep these facts together.

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
  selectedStructureRefs?: FinSet(SelectedStructureReference)
  candidateOrExpectedStructureClaimRefs?: FinSet(U.EpistemeRef)
  selectedStructureKindRefs or candidateStructureKindRefs:
  inspectedMaterialUse, if current: claim content | description | view | representation | publication form | source | decision | mathematical lens | other use
  inspectedMaterialUseRelationRefs?: references to obtaining relations that establish the inspected-material use
  firstArchitectureMove:
  architectureDescriptionBridge, if durable description use is current:
  claimPatternRefs?: FinSet(PatternRef), if another claim is being made:
  non-admissible overread?:
```

The card can stop before a durable claim. An `actualRelationNamed` result requires obtaining `ArchitectureRelation` occurrences and their A.22 structure participants. Candidate, planned, required, desired, expected, modeled, or diagrammed organization remains claim content. When that content is carried by a separate identified episteme, `candidateOrExpectedStructureClaimRefs` refers to it. Use `selectedStructureRefs` only for independently identified A.22 structures; neither designation makes an architecture relation obtain.
`architectureConcernCue` briefly describes the concern and helps identify the structures on which the question depends. When a controlled cue is useful, use `changeLocalization`, `substitutionOrReplacement`, `flowBottleneck`, `controlOrRateMismatch`, `dataCustodyOrStateResidence`, `physicalSeparationOrPlacement`, `evidenceReuseOrAssuranceReuse`, `scaleWindowOrCoarseningLoss`, `runtimeFailureMode`, `crossScopeResidual`, `descriptionViewLoss`, or `otherDeclared`. Local phrases such as change localization failure, hidden crossing, source return, generated-view loss, or state-residence uncertainty may remain in `sourcePhrase?` or Plain prose. If the described holon, distinction between actual and candidate structure, architecture concern, and first move cannot yet be named, set `questionDisposition` to `concernCueOnly` or `problemCardReady`.

`ArchitectureQuestionCard@Project` is a triage aid for choosing one architecture move. `questionDisposition` records whether to keep a concern cue, prepare a separate `ProblemCard`, constitute an `ArchitectureClaim`, or name the pattern for a non-architecture claim. `architectureRelationDisposition` separately records whether an actual relation has been recovered or the content is candidate or expected only. `claimPatternRefs` contains PatternIDs whose content defines, constrains, or tests any separate claim; it does not identify a pattern-application occurrence. The card is not an evidence record, gate or decision. Include `non-admissible overread?` or a `nonAdmissibleUse?` field only for a supported limitation that changes the receiving use; an unused field needs no invented exclusion.

Across C.30, `@Project` in a record name is a compatibility and retrieval cue only. It identifies neither a project entity nor a composite project `U.Work`, and it establishes no context, authority, viewpoint, or parthood. When the card is local to one actual project, `projectWorkOccurrenceRef` identifies the composite `U.Work` recovered under A.15.6. Include `architectureQuestionProjectUseRelationRef` only when a named pattern defines the relation by which this card use concerns that Work and an occurrence of that relation obtains. A Work reference alone does not establish project locality. If that locality matters but the relation is not yet defined, record `missing-governor`; if locality does not matter, omit both project-local fields. Description publication and other project-local uses follow the same rule.

Use the `ArchitectureDescription` bridge when the next architecture move depends on a description whose subject, correspondence or use conditions need recovery. Cross-team reuse or a regulated use can create that need; retaining an already sufficient explanation does not. Ordinary prose or a question card can finish the question. Use `C.30.AD` when the description itself needs construction or repair.

What goes wrong if C.30 is missed: the practitioner reasons from a document, module diagram, transformation-flow graph description, mathematical lens, benchmark, maturity score, or decision record instead of recovering the described holon, selected structures, first architecture move, and non-architecture claim kind.

What C.30 buys in practice: the practitioner can determine whether the next work concerns the actual organization, a proposed change, or the description through which it is understood. This selects an architecture action and the basis it still needs.

Do not use C.30 when the question does not concern the architecture of one holon, an obtaining `ArchitectureRelation`, a selected architecture-relevant structure, an `ArchitectureClaim`, or the thin architecture-description bridge needed for one architecture move. Use the pattern that defines or tests the source, description, view, publication-use, or other non-architecture relation. If one piece remains an architecture claim, use C.30 only for that piece. Common non-architecture claim boundaries are summarized in `C.30:12`.

Precision-restoration pointer: if the issue under repair is whether *architecture*, *architecture description*, *structural view*, *module diagram*, *model*, *source material*, *functional architecture*, or a source label such as *layer*, *level*, *tier*, *stack*, *block*, *expert*, *cache*, *router*, or *gate* names an architecture claim, description, view, representation, publication form, source relation, structure, or claim defined or tested by another pattern, use `C.30.P` or `C.30.STRAT` as triggered before applying C.30 to the recovered architecture portion. Use `C.29` for an unresolved mathematical formulation, transfer or reliance question that changes the architecture work. An adequate domain calculation or ordinary explanation can finish without a separate lens-use note. Keep trigger tables in those patterns; C.30 is applied only after an `ArchitectureClaim`, selected architecture-relevant structure, conditional `ArchitectureDescription` bridge use, `C.30.AD` application, or other claim named by value is recoverable.

