---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__006_solution.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:4 — Solution"
line_start: 60306
line_end: 60549
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

Use `ArchitectureDescription` when current work must create, inspect, or rely on a C.2.1 `U.Episteme` about exactly one architecture-side EntityOfConcern: one holon, one obtaining `ArchitectureRelation` occurrence, or one exact selected `U.Structure`. The episteme keeps the C.2.1 identity triple `<exact ClaimGraph, one exact EntityOfConcern, effective U.ReferenceScheme>`. An `ArchitectureClaim` can be cited as carried claim content or trace, but the claim record is not automatically the description's EntityOfConcern and does not replace the described subject.

Keep `ClaimScope`, empirical grounding, concern, viewpoint, view membership, selected model-use structure, representation, publication occurrence, publication form, carrier, project Work, and project-use relation outside that identity triple. Add each only when it independently applies. `modelUseStructureRef` is optional and appears only when an actually selected DDD model-use structure changes interpretation or selection.

`C.30.AD` does not mint `U.Architecture`, does not redefine `U.Viewpoint`, and does not replace generic Description, view, representation, publication, or publication-form machinery. It specializes those objects for architecture-description use while keeping every selected architecture-relevant structure directly recoverable.

Built-asset architecture-description, BIM, IFC, asset-information, digital-twin, and ISO/IEC 81346 reference-designation detail is governed by `C.30.AD.BA`. C.30.AD keeps the general architecture-description bridge and does not absorb that built-asset specialization.

#### C.30.AD:4.1 - Architecture-description record

```text
ArchitectureDescription ::= U.Episteme & {
  architectureDescriptionRef: U.EpistemeRef,
  claimGraph: exactly one C.2.1 ClaimGraph,
  entityOfConcernRef: exactly one of (
    describedHolonRef | architectureRelationOccurrenceRef | selectedStructureRef
  ),
  effectiveReferenceScheme: U.ReferenceScheme, byValue,

  architectureClaimRefs?: FinSet(U.EpistemeRef constrained to ArchitectureClaim),
  selectedStructureRefs: FinSet(U.StructureRef),
  structureKindRefs: FinSet(ArchitectureStructureKindRef),

  claimScope?: U.ClaimScope, byValue,
  concernRefs?: FinSet(U.EntityRef),
  modelUseStructureRef?: U.StructureRef,
  empiricalGroundingRelationRefs?: FinSet(U.RelationRef),

  architectureStructuralViewRefs?: FinSet(U.EpistemeRef constrained to ArchitectureStructuralView),
  viewpointConformanceRelationRefs?: FinSet(EpistemeViewpointConformanceRelationRef),
  descriptionSetUseClaimRefs?: FinSet(U.EpistemeRef),
  correspondenceClaimOrRelationRefs?: FinSet(U.EpistemeRef | U.RelationRef),

  sourceEpistemeRefs?: FinSet(U.EpistemeRef),
  sourceViewRefs?: FinSet(U.ViewRef),
  sourceToUsePathRefs?: FinSet(U.RelationRef),
  sourceReturnCondition?,
  freshnessClaimRefs?: FinSet(U.EpistemeRef),

  representationRefs?: FinSet(U.EntityRef),
  publicationOccurrenceRefs?: FinSet(EpistemePublicationRelationRef),
  publicationFormRefs?: FinSet(U.EntityRef),
  carrierRefs?: FinSet(U.EntityRef constrained to U.PresentationCarrier),
  specificationUseBoundary?,
  publicationUseBoundary?,
  admissibleUse,
  nonAdmissibleUse
}
```

The record identifies one episteme, not a document container. Its one `entityOfConcernRef` is supplied directly and is never derived merely from an architecture-claim field. When the EntityOfConcern is an architecture-relation occurrence or selected structure, participant traces can still recover its holon without changing episteme identity. `architectureClaimRefs` carries relevant claim content or trace only. `selectedStructureRefs` names the architecture-relevant structures described by the claim graph, while `structureKindRefs` classifies those structures.

Minimum conformance for the record:

- the exact claim graph, one exact EntityOfConcern, and effective `U.ReferenceScheme` are all present;
- actual architecture-relation references identify independently obtaining `ArchitectureRelation` occurrences; required, desired, expected, candidate, unresolved, or negative architecture content stays claim content;
- `selectedStructureRefs` names the architecture-relevant structures being described, and `structureKindRefs` classifies those selected structures;
- any cited `ArchitectureStructuralView` is the same description episteme admitted as `U.View` only by a separately obtaining E.17.0 conformance relation to one exact viewpoint episteme;
- cross-view composition uses explicit description-set use claims, correspondence claims, or separately governed obtaining relations; source use names source-to-use paths; a source-return condition appears only when stronger use requires return to a named source or governing pattern;
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
-> admissibleArchitectureMove or governing-pattern application
```

When allocation-responsibility semantics are current, the direct A.15 relation joins the working concern. When a source episteme or source view is used, a source-to-use path joins it to the view or description. Representation adds its own representation relation or object. Publication adds a publication occurrence with its form and carrier kept distinct. Cross-view use adds a correspondence claim or a direct correspondence relation only under its own admitted owner. A source-return condition is added only when a stronger use must return from a derivative or reused expression to a named source or governing pattern.

`E.17.0` carries the generic viewpoint-conformance test and the rule that the same episteme is a `U.View` iff the direct relation obtains. `C.30.ASV` carries selected-structure and architecture-view adequacy. `C.30.AD` carries the architecture-specific composition and use boundary: which exact objects each description is about, which structural views it uses, which correspondence claims or relations connect them, which source-to-use paths support source use, which stronger uses activate a source-return condition, and which architecture move or governing-pattern application remains admissible.

If any link in the chain is absent, do not fill it with a documentation label, query result, bundle membership, diagram, file, or publication. Either add the missing exact reference or independently obtaining relation, reduce the admissible use, or apply the governing pattern that can recover it.

#### C.30.AD:4.2 - View membership, viewpoint, and structure-kind binding

An architecture description episteme is not a `U.View` because it is put in a multi-view set, authored under a viewpoint label, constructed by A.6.3, returned by a query, selected, bundled, diagrammed, rendered, or published. First identify the candidate episteme by its C.2.1 identity. Then identify one exact viewpoint episteme and test the fixed five-part E.17.0 predicate. Only a separately obtaining `EpistemeViewpointConformanceRelation(candidateEpisteme, exactViewpoint)` admits that same episteme as `U.View`.

When a receiving use needs one multi-view description set, recover an exact collection of independently identified description epistemes under `C.13`; set membership is ordinary collection membership. A shared file, bundle, heading, graph, publication, or query result neither identifies that collection nor grants `U.View` membership. The collection keeps no second episteme identity for its members.

`C.30.AD` can record use of already recoverable architecture structural views inside one description set without minting a local relation kind:

```text
ArchitectureDescriptionViewUseClaim ::= U.Episteme & {
  claimGraph: {
    architectureDescriptionSetRef,
    usedArchitectureStructuralViewRef,
    usePurpose:
      orientation | comparison | implementationGuidance |
      assuranceInput | sourceUse | strongerUseReturn | declaredOther,
    correspondenceClaimOrRelationRefs?: FinSet(U.EpistemeRef | U.RelationRef),
    sourceToUsePathRefs?: FinSet(U.RelationRef),
    sourceReturnCondition?,
    admissibleUse,
    nonAdmissibleUse
  },
  entityOfConcernRef: exactly one architectureDescriptionSetRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue
}
```

The use claim does not grant `U.View` membership and does not make its view, set, viewpoint, or selected structure obtain. Each `usedArchitectureStructuralViewRef` must already identify the same description episteme whose exact E.17.0 conformance relation obtains. Use `C.30.ASV` when the current question is whether the episteme has the right selected structure, structure kind, exact viewpoint, conformance relation, hidden or lost structure note, source-to-use path, or source-return condition activated by stronger use. Use `A.22` when the current question is structure as such. Use `C.30` when the current question is an obtaining architecture relation or grounded architecture claim. Use `C.30.AD` only for description identity, description-set use, cross-view correspondence, source use, an applicable source-return condition, freshness, specification use, publication use, or the remaining architecture candidate-use boundary.
Common architecture-description views:

| View use | Required FPF application |
| --- | --- |
| Function or functionality view | `A.6.F` for function or functionality wording and `C.30.ASV` for the structural view. |
| Transformation-flow view | `E.18` plus `C.30.TFS-REL` when the selected transformation-flow structure, path, crossing, valuation, or graph-shaped mathematical description is used by architecture. |
| Control or LCA view | `C.30.LCA` when a control structure view is being used. |
| Module or interface view | `A.6.M`, signature or interface patterns, and `C.30.ASV` when module-interface structure is being used. |
| Mathematical-lens view | `C.29` for lens-use result and preserved and lost structure; `C.30.AD` only for the architecture-description use of the lens result. |
| Boundary, interface, or Markov-blanket view | `A.1`, `A.6.RSIR`, `A.6.P`, `A.6.0`, `A.6.5`, `A.6.M`, `A.6.F`, `C.26`, `C.26.3`, and `C.29` according to the recovered claim; `A.6.B` only when the recovered object is L, A, D, or E statement classification inside a boundary package. `C.30.AD` records only exact description identity, description-set use, cross-view correspondence, source-to-use path when a source is used, an applicable stronger-use return condition, freshness, representation, or publication use. |
| Evidence or assurance reuse view | `A.10`, `B.3`, or assurance or evidence pattern governing the claim for the non-architecture claim. |
| Architecture residual view | `C.30.ILC` governs a cross-scope or interlevel architecture residual. C.30.AD records only the residual view's exact episteme identity, conformance, description-set use, correspondence to other views, and declared use boundary; source-use relations are added only when such a source is actually used. |
| Multilevel-learning or frustration mathematical-lens view | `C.29` when the view contains a recoverable level mapping or scale mapping and preserved structure and lost structure; `C.30.AD` records only the architecture-description use of that lens result. |
| Residual-reducing candidate or optimization view | `C.32.MLAO` governs the residual-reducing multilevel candidate frame; `C.32` governs the candidate architecture palette; `A.19.CPM` or `A.19.SelectorMechanism` governs comparison or selector-policy use; `C.18` and `C.19` govern archive, front, or current-pool treatment; `G.5` governs selected-set publication; `C.11` governs final local choice. C.30.AD records only exact description identity, description-set use, cross-view correspondence, source-to-use path when used, an applicable source-return condition, freshness, representation, publication use, or specification use. |

#### C.30.AD:4.3 - Cross-view correspondence, source use, and return conditions

Architecture descriptions become risky when a reader cannot tell whether two view epistemes concern the same holon, the same architecture-relation occurrence, the same selected structure, related structures, or different EntitiesOfConcern. A description set therefore carries explicit correspondence claims or references an independently admitted direct correspondence relation. Merely placing two views in one file, model, list, or publication creates neither correspondence nor shared identity. Use source-to-use paths when source epistemes, views, generated outputs, representations, or publications enter current use. Add a source-return condition only when stronger use requires return from a derivative or reused description to a named source or governing pattern.

```text
ArchitectureDescriptionCorrespondenceClaim ::= U.Episteme & {
  claimGraph: {
    architectureDescriptionSetRef,
    fromViewRef,
    toViewRef,
    correspondenceKind:
      sameDescribedHolon | sameArchitectureRelationOccurrence |
      sameSelectedStructure | refinement | abstraction | projection |
      sourceDerived | conflict | declaredOther,
    preservedStructureRefs?,
    lostStructureRefs?,
    directCorrespondenceRelationRefs?: FinSet(U.RelationRef),
    sourceToUsePathRefs?: FinSet(U.RelationRef),
    sourceReturnCondition?,
    admissibleUse,
    nonAdmissibleUse
  },
  entityOfConcernRef: exactly one architectureDescriptionSetRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue
}
```

This local record is claim content and does not itself instantiate a world-side correspondence relation. A `directCorrespondenceRelationRef` is affirmative only when that relation's own governing pattern admits it and the occurrence independently obtains. Correspondence is not proof, empirical grounding, assurance, gate passage, shared EntityOfConcern, or architecture identity; it lets a reader use more than one view without silently changing what each episteme is about.

#### C.30.AD:4.4 - Freshness and currentness boundary

Use a freshness claim only when the architecture description's admissible use depends on source edition, structure edition, model version, deployment state, or an external condition. Keep this bounded claim distinct from any publication-currentness relation:

```text
ArchitectureDescriptionFreshnessClaim ::= U.Episteme & {
  claimGraph: {
    sourceEditionRefs,
    structureEditionRefs?,
    modelOrToolEditionRefs?,
    knownRefreshTrigger:
      sourceChange | deploymentChange | interfaceChange |
      controlRateChange | modelEditionChange | evidenceDecay |
      toolApiChange | regulatoryChange |
      incidentFinding | declaredOther | unknown,
    admissibleUseUntil?,
    sourceReturnCondition?
  },
  entityOfConcernRef: exactly one ArchitectureDescriptionRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue
}
```

A freshness claim carries a source-return condition only when a stronger use must return to a named source or governing pattern. It does not make the description empirically grounded, evidence-sufficient, true, or publication-current; it only bounds current use of the exact description episteme under the stated scheme.

#### C.30.AD:4.5 - Specification-use and publication boundary

An architecture description can be used as a specification only when that use is declared. Specification use is not a new architecture kind; it is a bounded use of an exact description episteme or of one of its publications.

```text
ArchitectureDescriptionSpecificationUse@Project ::= {
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work,
  architectureDescriptionProjectUseRelationRef?: U.RelationRef governed by the exact specification-use or work-use pattern,
  architectureDescriptionRef: U.EpistemeRef constrained to ArchitectureDescription,
  sourceEpistemeRef?: U.EpistemeRef,
  sourceViewRef?: U.ViewRef,
  sourceToUsePathRefs?: FinSet(U.RelationRef),
  representationRef?: U.EntityRef,
  publicationOccurrenceRef?: EpistemePublicationRelationRef,
  publicationFormRef?: U.EntityRef,
  carrierRef?: U.EntityRef constrained to U.PresentationCarrier,
  governedUse:
    coordination | implementationGuidance | procurement |
    verificationPlanning | assuranceInput | releaseInput |
    declaredOther,
  directGoverningPatternRef?: U.EntityRef, referencing one U.MethodDescription,
  admissibleUse:
  nonAdmissibleUse:
}
```

The two project fields preserve the ordinary boundary: `projectWorkOccurrenceRef` identifies an actual composite `U.Work`; `architectureDescriptionProjectUseRelationRef` identifies a separately obtaining project-use relation under its direct owner. Neither a project label nor this use record creates that Work or relation.

If specification use becomes pattern-use recommendation, work-entry readiness, evidence, assurance, gate passage, performed work, work authorization, decision claim, causal-use claim, or release authorization, apply the direct pattern governing that claim to the claim being made. The architecture description remains the description boundary, not the governing claim.

Keep the description episteme, its possible `U.View` membership, diagram or other representation, publication occurrence, publication form, and carrier distinct. Authoring, construction, querying, selection, bundling, rendering, filing, or publication creates none of the subject-side architecture relation, selected structure, description truth, empirical grounding, project Work, or project-use relation by itself.

#### C.30.AD:4.6 - Direct governing-pattern applications

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
| Residual-reducing candidate architecture moves, candidate palette, candidate front, shortlist, selected set, or optimization over candidates | `C.32.MLAO` for the residual-reducing frame, `C.32` for the candidate palette, `A.19.CPM` or `A.19.SelectorMechanism` for comparison or selector-policy use, `C.18` and `C.19` for archive, front, or pool treatment, `G.5` for selected-set publication, `C.11` for final local choice, and measurement patterns named by value when those claims are being made |
| Generic description, view, viewpoint, publication, publication form, MVPK face | `A.7`, `E.17.0`, `E.17.1`, `E.17.2`, `E.17`, or `C.2.P` |
| Function or functionality wording | `A.6.F` |
| Module, interface, port, signature, or reusable structure relation | `A.6.M`, a signature or interface pattern named by value, `C.31`, or `C.31.RSA` |
| Mathematical lens or preserved and lost mathematical structure | `C.29` |
| Characteristic, scale, coordinate, score, or quality claim | `C.16.P`, `C.16`, `A.19`, `C.25`, or quality pattern governing the claim |
| Evidence, assurance, gate, work planning, performed work, local choice, project architecture decision, causal-use, release | `A.10`, `B.3`, `A.20`, `A.21`, `A.15.2`, `A.15.1`, `C.11`, `C.32.PAD`, `C.28`, release or admissibility pattern, or governing pattern |

#### C.30.AD:4.6a - Candidate, front, and selected-set description boundary

An architecture description can also carry claims about a project architecture decision or selected structures cited by an ADR-like publication. Use `C.32.PAD` for the project architecture decision relation, `C.32.ADR` for publication projection of an architecture-decision description, and `C.32.ADA` for adequacy of that decision for a declared use. C.30.AD keeps only the exact description identity, possible E.17.0 view conformance, description-set use claims, cross-view correspondence claims or governed relations, source-to-use paths when sources are used, applicable source-return conditions, freshness, representation, publication use, and specification use.

An architecture description may carry claim content about an archive, front, selected set, candidate palette, local choice, or planned architecture move. That does not make the description the archive-governing pattern, selector, choice rule, pattern-use recommendation, work-entry readiness relation, work authorization, or deontic permission. Use `C.32.MLAO` for residual-reducing multilevel candidate frames, `C.32` for candidate architecture palettes, `C.18` for archive and front relations, `C.19` for current-pool treatment, `G.5` only for selected-set publication, `C.11` for local choice, `C.30` for the architecture move, `C.30.ASV` for selected-structure view triage, `E.11.PUR` for recommended pattern use, `A.15.5` for work-entry readiness, and the A.15 family for planning or performed work.

For an architecture-description claim, record exact episteme identity plus only the view conformance, description-set use, viewpoint, cross-view correspondence, source-to-use path, applicable stronger-use return condition, freshness, representation, publication use, and specification use that actually apply. If the current source claim only grounds a first architecture move, return to `C.30`. If it synthesizes alternatives, use `C.32` or `C.32.MLAO` according to the residual frame. If it changes which variants are archived, kept in a pool, compared, selected, published, locally chosen, or decided, return to the pattern that governs that relation.

