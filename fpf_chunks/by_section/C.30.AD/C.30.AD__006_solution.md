---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__006_solution.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:4 — Solution"
line_start: 57181
line_end: 57417
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.3.NAR"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD.BA"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D2"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "G.5"
keywords:
  - "ArchitectureDescription@Context"
  - "architecture description"
  - "architecture description use card"
  - "architecture structural view"
  - "candidate-description boundary"
  - "correspondence"
  - "source return"
  - "specification-use boundary"
  - "viewpoint"
---

### C.30.AD:4 - Solution

An `ArchitectureDescription` is the local name for a C.2.1 `U.Episteme` that describes one architecture-side EntityOfConcern: a holon, an obtaining `ArchitectureRelation` occurrence, or a selected `U.Structure`. Use the name only when its ClaimGraph makes that subject, the described structures, purpose, and use boundary recoverable. It remains an episteme identified by `<ClaimGraph, EntityOfConcern, ReferenceScheme>`; it is not a record or a new root kind. A cited `ArchitectureClaim` is content or trace, not automatically the thing described.

Keep `ClaimScope`, empirical grounding, concern, viewpoint, view membership, selected model-use structure, representation, publication occurrence, publication form, carrier, project Work, and project-use relation outside that identity triple. Add each only when it independently applies. `modelUseStructureRef` is optional and appears only when an actually selected DDD model-use structure changes interpretation or selection.

`C.30.AD` does not mint `U.Architecture`, redefine `U.Viewpoint`, or replace generic Description, view, representation, publication, or publication-form machinery. It defines their architecture-description use while keeping every selected architecture-relevant structure directly recoverable.

For built-asset architecture descriptions, BIM, IFC, asset information, digital twins, and ISO/IEC 81346 reference designation, use `C.30.AD.BA`. C.30.AD keeps the general architecture-description bridge and does not absorb that specialization.

#### C.30.AD:4.1 - Architecture-description use account

```text
ArchitectureDescriptionUseAccount:
  architectureDescriptionRef: U.EpistemeRef constrained to ArchitectureDescription
  claimGraphRef: exactly one C.2.1 ClaimGraph
  entityOfConcernRef: exactly one of (
    describedHolonRef | architectureRelationOccurrenceRef | selectedStructureRef
  )
  effectiveReferenceScheme: U.ReferenceScheme, byValue

  architectureClaimRefs?: FinSet(U.EpistemeRef constrained to ArchitectureClaim)
  selectedStructureRefs: FinSet(U.StructureRef)
  structureKindRefs: FinSet(ArchitectureStructureKindRef)

  claimScope?: U.ClaimScope, byValue
  concernRefs?: FinSet(U.EntityRef)
  modelUseStructureRef?: U.StructureRef
  empiricalGroundingRelationRefs?: FinSet(U.RelationRef)

  architectureStructuralViewRefs?: FinSet(U.EpistemeRef constrained to ArchitectureStructuralView)
  viewpointConformanceRelationRefs?: FinSet(EpistemeViewpointConformanceRelationRef)
  descriptionSetUseClaimRefs?: FinSet(U.EpistemeRef)
  correspondenceClaimOrRelationRefs?: FinSet(U.EpistemeRef | U.RelationRef)

  sourceEpistemeRefs?: FinSet(U.EpistemeRef)
  sourceViewRefs?: FinSet(U.ViewRef)
  sourceToUsePathRefs?: FinSet(U.RelationRef)
  sourceReturnCondition?
  freshnessClaimRefs?: FinSet(U.EpistemeRef)

  representationRefs?: FinSet(U.EntityRef)
  publicationOccurrenceRefs?: FinSet(EpistemePublicationRelationRef)
  publicationFormRefs?: FinSet(U.EntityRef)
  carrierRefs?: FinSet(U.EntityRef constrained to U.PresentationCarrier)
  specificationUseBoundary?
  publicationUseBoundary?
  admissibleUse
  nonAdmissibleUse
```

The account points to an already constituted episteme; it is not the episteme and does not add slots to it. Its first three references simply expose the ClaimGraph, EntityOfConcern, and reference scheme that identify the episteme. When the described thing is a relation occurrence or selected structure, the participant trace can still recover its holon. `architectureClaimRefs` carries relevant claim content or trace; `selectedStructureRefs` names the structures described, and `structureKindRefs` classifies them.

Minimum conformance for a retained `ArchitectureDescriptionUseAccount`:

- the account resolves to one exact architecture-description episteme and exposes its exact ClaimGraph, one exact EntityOfConcern, and effective `U.ReferenceScheme`;
- actual architecture-relation references identify independently obtaining `ArchitectureRelation` occurrences; required, desired, expected, candidate, unresolved, or negative architecture content stays claim content;
- `selectedStructureRefs` names the architecture-relevant structures being described, and `structureKindRefs` classifies those selected structures;
- any cited `ArchitectureStructuralView` is the same description episteme admitted as `U.View` only by a separately obtaining E.17.0 conformance relation to one exact viewpoint episteme;
- cross-view composition uses explicit description-set use claims, correspondence claims, or independently obtaining relations; source use names source-to-use paths; a source-return condition appears only when stronger use requires return to a named source or exact defining or constraining ClaimGraph;
- representation and publication fields identify their own objects and occurrences; they do not establish the description, architecture, selected structure, view membership, empirical grounding, or truth;
- `admissibleUse` and `nonAdmissibleUse` say what the description can and cannot carry.

#### C.30.AD:4.1a - Traceable architecture multi-view description chain

A full architecture description is traceable only when the reader can recover the chain that makes a view useful without turning the view into the architecture or letting a list create view membership. The chain is a trace requirement, not a prescribed method or work plan:

```text
workingConcernRef
-> exact viewpoint episteme
-> independently obtaining EpistemeViewpointConformanceRelation
-> the same ArchitectureDescription episteme admitted as U.View
-> exact entityOfConcernRef
-> selectedStructureRef and, when actual, ArchitectureRelationOccurrenceRef
-> optional ArchitectureClaimRef
-> ArchitectureDescriptionUseCard or multi-view description-set use claim
-> admissibleArchitectureMove or pattern needed for a separate claim
```

When allocation or responsibility is current, add the exact direct relation separately. A system-role kind or assignment can support the work context but does not establish responsibility; `VP.AllocationResponsibility` only helps recognize the concern. When a source episteme or source view is used, a source-to-use path joins it to the view or description. Representation adds its own representation relation or object. Publication adds a publication occurrence with its form and carrier kept distinct. Cross-view use adds a correspondence claim or a direct correspondence relation only when its exact predicate obtains. A source-return condition is added only when a stronger use must return from a derivative or reused expression to a named source or exact defining or constraining ClaimGraph.

`E.17.0` tests whether the description is a `U.View`; `C.30.ASV` tests whether it carries the right selected structure and structure kind. `C.30.AD` records how the description is composed and used: what it describes, which views and correspondence it uses, where source material enters, when stronger use must return to a source, and what architecture move or separate claim remains.

If a needed link is absent, do not substitute a label, query result, bundle, diagram, file, or publication. Add the missing reference or relation that actually holds, narrow the allowed use, or use the pattern that defines how to recover it.

#### C.30.AD:4.2 - View membership, viewpoint, and structure-kind binding

An architecture description episteme is not a `U.View` because it is put in a multi-view set, authored under a viewpoint label, constructed by A.6.3, returned by a query, selected, bundled, diagrammed, rendered, or published. First identify the candidate episteme by its C.2.1 identity. Then identify one exact viewpoint episteme and test the fixed five-part E.17.0 predicate. Only a separately obtaining `EpistemeViewpointConformanceRelation(candidateEpisteme, exactViewpoint)` admits that same episteme as `U.View`.

When a receiving use needs one multi-view description set, recover an exact collection of independently identified description epistemes under `C.13`; set membership is ordinary collection membership. A shared file, bundle, heading, graph, publication, or query result neither identifies that collection nor grants `U.View` membership. The collection keeps no second episteme identity for its members.

`C.30.AD` can record use of already recoverable architecture structural views inside one description set without minting a local relation kind:

```text
ArchitectureDescriptionViewUseClaim content:
  architectureDescriptionSetRef:
  usedArchitectureStructuralViewRef:
  usePurpose:
    orientation | comparison | implementationGuidance |
    assuranceInput | sourceUse | strongerUseReturn | declaredOther
  correspondenceClaimOrRelationRefs?: FinSet(U.EpistemeRef | U.RelationRef)
  sourceToUsePathRefs?: FinSet(U.RelationRef)
  sourceReturnCondition?
  admissibleUse:
  nonAdmissibleUse:
C.2.1 constitution:
  entityOfConcernRef: exactly one architectureDescriptionSetRef
  effectiveReferenceScheme: U.ReferenceScheme, byValue
```

`ArchitectureDescriptionViewUseClaim` is a C.2.1 episteme about one description set. The block separates what the claim says from the objects that identify it; it does not add slots to the episteme. The claim cannot make anything a `U.View` or make a view, set, viewpoint, or structure obtain. Each referenced view must already satisfy E.17.0. Use `C.30.ASV` to check viewpoint conformance and selected structure, `A.22` for structure itself, and `C.30` for an obtaining architecture relation or grounded architecture claim. Use `C.30.AD` only for description identity and use, cross-view correspondence, source use or return, freshness, specification or publication use, and the remaining architecture move.
Common architecture-description views:

| View use | Required FPF application |
| --- | --- |
| Function or functionality view | `A.6.F` for function or functionality wording and `C.30.ASV` for the structural view. |
| Transformation-flow view | `E.18` plus `C.30.TFS-REL` when the selected transformation-flow structure, path, crossing, valuation, or graph-shaped mathematical description is used by architecture. |
| Control or LCA view | `C.30.LCA` when a control structure view is being used. |
| Module or interface view | `A.6.M`, signature or interface patterns, and `C.30.ASV` when module-interface structure is being used. |
| Mathematical-lens view | `C.29` for lens-use result and preserved and lost structure; `C.30.AD` only for the architecture-description use of the lens result. |
| Boundary, interface, or Markov-blanket view | `A.1`, `A.6.RSIR`, `A.6.P`, `A.6.0`, `A.6.5`, `A.6.M`, `A.6.F`, `C.26`, `C.26.3`, and `C.29` according to the recovered claim; `A.6.B` only when the recovered object is L, A, D, or E statement classification inside a boundary package. `C.30.AD` records only exact description identity, description-set use, cross-view correspondence, source-to-use path when a source is used, an applicable stronger-use return condition, freshness, representation, or publication use. |
| Evidence or assurance reuse view | Use `A.10`, `B.3`, or the relevant evidence or assurance pattern for the non-architecture claim. |
| Architecture residual view | Use `C.30.ILC` for a cross-scope or interlevel architecture residual. C.30.AD records only the view episteme, its conformance, description-set use, correspondence to other views, and allowed use; add a source-use relation only when a source is actually used. |
| Multilevel-learning or frustration mathematical-lens view | `C.29` when the view contains a recoverable level mapping or scale mapping and preserved structure and lost structure; `C.30.AD` records only the architecture-description use of that lens result. |
| Residual-reducing candidate or optimization view | Use `C.32.MLAO` for the residual-reducing multilevel candidate frame, `C.32` for the candidate architecture palette, `A.19.CPM` or `A.19.SelectorMechanism` for comparison or selector-policy use, `C.18` and `C.19` for archive, front, or current-pool treatment, `G.5` for selected-set result declaration, and `C.11` for final local choice. Record with C.30.AD only the exact description identity, description-set use, cross-view correspondence, source-to-use path when used, applicable source-return condition, freshness, representation, publication use, or specification use. |

#### C.30.AD:4.3 - Cross-view correspondence, source use, and return conditions

Before combining two views, establish whether they describe the same holon, the same architecture-relation occurrence, the same selected structure, related structures, or different subjects. State that correspondence as a claim or cite a direct relation that actually holds; merely placing views in one file, list, model, or publication creates no correspondence. When source material enters the current use, record its source-to-use path. Add a return condition only when stronger use must go back to a named source or defining or constraining ClaimGraph.

```text
ArchitectureDescriptionCorrespondenceClaim content:
  architectureDescriptionSetRef:
  fromViewRef:
  toViewRef:
  correspondenceKind:
    sameDescribedHolon | sameArchitectureRelationOccurrence |
    sameSelectedStructure | refinement | abstraction | projection |
    sourceDerived | conflict | declaredOther
  preservedStructureRefs?
  lostStructureRefs?
  directCorrespondenceRelationRefs?: FinSet(U.RelationRef)
  sourceToUsePathRefs?: FinSet(U.RelationRef)
  sourceReturnCondition?
  admissibleUse:
  nonAdmissibleUse:
C.2.1 constitution:
  entityOfConcernRef: exactly one architectureDescriptionSetRef
  effectiveReferenceScheme: U.ReferenceScheme, byValue
```

`ArchitectureDescriptionCorrespondenceClaim` is a C.2.1 episteme about one description set. The block separates claim content from its C.2.1 identity; it does not add slots or create a world-side relation. Cite a direct correspondence relation only when its predicate is defined, the facts satisfy it, and the relation actually holds. Correspondence helps a reader combine views without changing what each is about; it does not establish proof, grounding, assurance, gate passage, shared subject, or architecture identity.

#### C.30.AD:4.4 - Freshness and currentness boundary

Use a freshness claim only when the architecture description's admissible use depends on source edition, structure edition, model version, deployment state, or an external condition. Keep this bounded claim distinct from any publication-currentness relation:

```text
ArchitectureDescriptionFreshnessClaim content:
  sourceEditionRefs:
  structureEditionRefs?
  modelOrToolEditionRefs?
  knownRefreshTrigger:
    sourceChange | deploymentChange | interfaceChange |
    controlRateChange | modelEditionChange | evidenceDecay |
    toolApiChange | regulatoryChange |
    incidentFinding | declaredOther | unknown
  admissibleUseUntil?
  sourceReturnCondition?
C.2.1 constitution:
  entityOfConcernRef: exactly one ArchitectureDescriptionRef
  effectiveReferenceScheme: U.ReferenceScheme, byValue
```

`ArchitectureDescriptionFreshnessClaim` is a C.2.1 episteme about one architecture description. The block separates claim content from its C.2.1 identity. Add a source-return condition only when stronger use must go back to a named source or defining or constraining ClaimGraph. Freshness bounds current use; it does not make the description true, grounded, evidence-sufficient, or publication-current.

#### C.30.AD:4.5 - Specification-use and publication boundary

An architecture description can be used as a specification only when that use is declared. Specification use is not a new architecture kind; it is a bounded use of an exact description episteme or of one of its publications.

```text
ArchitectureDescriptionSpecificationUseAccount@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureDescriptionProjectUseRelationRef?: U.RelationRef defined by the pattern for the exact relation by which this specification use concerns the Work
  architectureDescriptionRef: U.EpistemeRef constrained to ArchitectureDescription
  sourceEpistemeRef?: U.EpistemeRef
  sourceViewRef?: U.ViewRef
  sourceToUsePathRefs?: FinSet(U.RelationRef)
  representationRef?: U.EntityRef
  publicationOccurrenceRef?: EpistemePublicationRelationRef
  publicationFormRef?: U.EntityRef
  carrierRef?: U.EntityRef constrained to U.PresentationCarrier
  declaredUse:
    coordination | implementationGuidance | procurement |
    verificationPlanning | assuranceInput | releaseInput |
    declaredOther
  claimPatternRefs?: FinSet(PatternRef)
  admissibleUse:
  nonAdmissibleUse:

```

This account records how an existing description or publication is used as a specification. It is not an episteme, relation, MethodDescription, Method, pattern application, or Work occurrence. `claimPatternRefs` cites PatternIDs for separate claims. When project locality matters, name the composite `U.Work` and include the project-use relation only if a pattern defines it and it actually holds. If locality matters but the relation is undefined, return `missing-governor`; otherwise omit both project fields. A project label or this account creates neither Work nor relation.

If specification use is also claimed to be a pattern-use recommendation, work-entry readiness, evidence, assurance, gate passage, performed work, work authorization, decision, causal use, or release authorization, use the pattern that defines or tests that other claim. The description remains only the description boundary.

Keep the description episteme, its possible `U.View` membership, diagram or other representation, publication occurrence, publication form, and carrier distinct. Authoring, construction, querying, selection, bundling, rendering, filing, or publication creates none of the subject-side architecture relation, selected structure, description truth, empirical grounding, project Work, or project-use relation by itself.

#### C.30.AD:4.6 - Other claims and applicable patterns

| Question after the architecture-description boundary is clear | FPF application |
| --- | --- |
| Grounded architecture claim, selected structures, first architecture move | `C.30` |
| Recommended FPF pattern use after reading the description | `E.11.PUR` |
| Work-entry readiness or full-kit condition for intended architecture work | `A.15.5` |
| Architecture or structure wording is still overloaded | `C.30.P` |
| Architecture structural view or structure-kind and viewpoint relation | `C.30.ASV` |
| Transformation-flow relation or graph description used by architecture | `C.30.TFS-REL` and `E.18` |
| Control structure view | `C.30.LCA` |
| Cross-scope or interlevel architecture residual, conflict, or frustration in the described holon | `C.30.ILC` |
| Multilevel-learning or frustration mathematical-lens result with recoverable level mapping or scale mapping and preserved structure and lost structure | `C.29` with the admitted C.29-local lens output |
| Residual-reducing candidate architecture moves, candidate palette, candidate front, shortlist, selected set, or optimization over candidates | `C.32.MLAO` for the residual-reducing frame, `C.32` for the candidate palette, `A.19.CPM` or `A.19.SelectorMechanism` for comparison or selector-policy use, `C.18` and `C.19` for archive, front, or pool treatment, `G.5` for selected-set result declaration, `C.11` for final local choice, and measurement patterns named by value when those claims are being made |
| Generic description, view, viewpoint, publication, publication form, MVPK face | `A.7`, `E.17.0`, `E.17.1`, `E.17.2`, `E.17`, or `C.2.P` |
| Function or functionality wording | `A.6.F` |
| Module, interface, port, signature, or reusable structure relation | `A.6.M`, a signature or interface pattern named by value, `C.31`, or `C.31.RSA` |
| Mathematical lens or preserved and lost mathematical structure | `C.29` |
| Characteristic, scale, coordinate, score, or quality claim | `C.16.P`, `C.16`, `A.19`, `C.25`, or the pattern that defines or tests the quality claim |
| Evidence, assurance, gate, work planning, performed work, local choice, project architecture decision, causal use, or release | `A.10`, `B.3`, `A.20`, `A.21`, `A.15.2`, `A.15.1`, `C.11`, `C.32.PAD`, `C.28`, or the pattern for the particular release, admissibility, or other claim |

#### C.30.AD:4.6a - Candidate, front, and selected-set description boundary

An architecture description may also carry a project architecture decision or selected structures cited by an ADR-like publication. Use `C.32.PAD` for the decision relation, `C.32.ADR` for its publication projection, and `C.32.ADA` for decision adequacy. C.30.AD retains only description identity, E.17.0 view conformance, description-set use, correspondence claims or relations that actually hold, source paths and applicable return conditions, freshness, representation, publication use, and specification use.

An architecture description may contain claims about an archive, front, selected set, candidate palette, local choice, or planned architecture move. That content does not turn the description into any of those things or establish recommendation, readiness, authorization, or permission. Use `C.32.MLAO` and `C.32` for candidates, `C.18` and `C.19` for archives, fronts, and pools, `G.5` for a selected-set result, `C.11` for local choice, `C.30` for the architecture move, `C.30.ASV` for the structural view, `E.11.PUR` for recommended pattern use, and `A.15.5` or the A.15 family for readiness and Work. If the content is published, use `E.17` for the source-backed face and source return, and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. C.30.AD still records only the architecture description and its publication use.

For an architecture-description claim, record its C.2.1 identity and only the view conformance, set use, viewpoint, correspondence, source path or return condition, freshness, representation, publication use, and specification use that actually apply. If a source only grounds the first architecture move, use `C.30`. If it synthesizes alternatives, use `C.32` or `C.32.MLAO`. If it changes which variants are archived, pooled, compared, selected, published, locally chosen, or decided, use the pattern that defines or constrains that relation.

