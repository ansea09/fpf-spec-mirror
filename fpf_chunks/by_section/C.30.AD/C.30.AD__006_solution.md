---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__006_solution.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:4 — Solution"
line_start: 53856
line_end: 54044
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.8"
  - "F.18"
keywords:
  - "ArchitectureDescription@Context"
  - "architecture description"
  - "architecture description use card"
  - "architecture structural view"
  - "correspondence"
  - "source return"
  - "specification-use boundary"
  - "viewpoint"
---

### C.30.AD:4 - Solution

Use `ArchitectureDescription@Context` when the EntityOfConcern under repair is the description episteme or specification-use record over one `ArchitectureOf@Context`. The described holon is recovered through `ArchitectureOf@Context.describedHolonRef`; the `DescriptionContext.EntityOfConcernRef` for the architecture description points to the architecture claim record.

`C.30.AD` does not mint `U.Architecture`, does not redefine `U.Viewpoint`, and does not replace generic Description, view, publication, or carrier machinery. It specializes those records for architecture descriptions whose views remain tied to selected architecture-relevant structures.

#### C.30.AD:4.1 - Architecture-description record

```text
ArchitectureDescription@Context ::= {
  architectureDescriptionId: ArchitectureDescriptionId,
  architectureClaimRef: ArchitectureOf@ContextRef,
  descriptionContext: DescriptionContext(
    EntityOfConcernRef = architectureClaimRef,
    BoundedContextRef = ArchitectureOf@Context.boundedContextRef,
    ViewpointRef = primaryViewpointRef?
  ),
  describedHolonRef: U.HolonRef,
  selectedStructureRefs: FinSet(U.StructureRef),
  structureKindRefs: FinSet(ArchitectureStructureKindRef),
  architectureStructuralViewRefs: FinSet(ArchitectureStructuralViewRef),
  correspondenceRefs: FinSet(CorrespondenceRef),
  sourceEpistemeRefs?: FinSet(U.EpistemeRef),
  sourceViewRefs?: FinSet(U.ViewRef),
  sourceReturnCondition?,
  freshnessCueRefs?: FinSet(ArchitectureDescriptionFreshnessCueRef),
  specificationUseBoundary?,
  publicationUseBoundary?,
  admissibleUse,
  nonAdmissibleUse
}
```

`describedHolonRef` is a recoverable field copied from the referenced `ArchitectureOf@Context`; it is not the architecture description's `DescriptionContext.EntityOfConcernRef`.

Minimum conformance for the record:

- `architectureClaimRef` names one `ArchitectureOf@Context`;
- `selectedStructureRefs` or `structureKindRefs` name the architecture-relevant structures being described;
- every architecture structural view names its viewpoint and selected structure or structure kind;
- `correspondenceRefs` or a source-return condition is present when cross-view or source reuse is being made;
- `admissibleUse` and `nonAdmissibleUse` say what the description can and cannot carry.

#### C.30.AD:4.1a - Traceable architecture multi-view description chain

A full architecture description is traceable only when the reader can recover the chain that makes a view useful without turning the view into the architecture. The chain is a trace obligation, not a prescribed method or work plan:

```text
workingConcernRef
  or A15RoleEnactorFamilyRef when A.15 role-enactor semantics apply
-> viewpointRef
-> selectedStructureRef or structureKindRef
-> ArchitectureOf@ContextRef
-> ArchitectureStructuralView@ContextRef governed by C.30.ASV
-> ArchitectureDescription@ContextRef governed by C.30.AD
-> sourceEpistemeRef or sourceViewRef when source use is being made
-> PublicationUnitRef, publication face, or publication form only when published
-> correspondenceRef or sourceReturnCondition when cross-view or source reuse is being made
-> admissibleArchitectureMove or neighboring-pattern application
```

`E.17.0` carries the generic multi-view Description machinery. `C.30.ASV` carries the selected-structure-kind-to-view relation and view adequacy. `C.30.AD` carries the architecture-specific composition and use boundary: which architecture claim the description is about, which structural views it uses, what correspondence or source return keeps the use honest, and which architecture move or neighboring pattern remains admissible.

If any link in the chain is absent, do not fill it with a documentation label. Either add the missing reference, reduce the admissible use, or return to the governing pattern that can recover the missing relation.

#### C.30.AD:4.2 - View membership, viewpoint, and structure-kind binding

Architecture descriptions can contain several `ArchitectureStructuralView@Context` records. Each such view remains governed by `C.30.ASV`; C.30.AD does not mint a second structural-view record and does not decide whether the view has the right structure kind, viewpoint, hidden or lost structure note, correspondence, or source return.

C.30.AD records only membership or use of an already recoverable architecture structural view inside one architecture description:

```text
ArchitectureDescriptionViewMembership@Context ::= {
  architectureDescriptionRef: ArchitectureDescriptionRef,
  architectureStructuralViewRef: ArchitectureStructuralViewRef,
  architectureClaimRef: ArchitectureOf@ContextRef,
  membershipPurpose:
    orientation | comparison | implementationGuidance |
    assuranceInput | sourceReturn | declaredOther,
  correspondenceRefs?: FinSet(CorrespondenceRef),
  sourceReturnCondition?,
  admissibleUse:
  nonAdmissibleUse:
}
```

Use `C.30.ASV` when the question under repair is whether the view has the right structure kind, viewpoint, hidden or lost structure note, correspondence, or source return. Use `A.22` when the question under repair is structure as such. Use `C.30` when the question under repair is the grounded architecture claim. Use `C.30.AD` only for the description's membership, composition, correspondence, source-return, freshness, specification-use, publication-use, or remaining-move boundary.

Common architecture-description views:

| View use | Required FPF application |
| --- | --- |
| Function or functionality view | `A.6.F` for function or functionality wording and `C.30.ASV` for the structural view. |
| Transformation-flow view | `E.18` plus `C.30.TFS-REL` when the selected transformation-flow structure, path, crossing, valuation, or graph-shaped mathematical description is used by architecture. |
| Control or LCA view | `C.30.LCA` when a control structure view is being used. |
| Module or interface view | `A.6.M`, signature or interface patterns, and `C.30.ASV` when module-interface structure is being used. |
| Mathematical-lens view | `C.29` for lens-use result and preserved and lost structure; `C.30.AD` only for the architecture-description use of the lens result. |
| Evidence or assurance reuse view | `A.10`, `B.3`, or assurance or evidence pattern governing the claim for the non-architecture claim. |
| Architecture residual view | `C.30.ILC` when the view is about a cross-scope or interlevel architecture residual. If the view uses conflict wording or frustration wording, C.30.AD records only membership, correspondence, and source return; C.30.ILC governs the residual. |
| Multilevel-learning or frustration mathematical-lens view | `C.29` when the view contains a recoverable level mapping or scale mapping and preserved structure and lost structure; `C.30.AD` records only the architecture-description use of that lens result. |
| Residual-reducing candidate or optimization view | `G.5` for candidate sets and residual-reducing candidate moves; `C.11` for final local choice. C.30.AD records only description membership, correspondence, source return, freshness, publication use, or specification use. |

#### C.30.AD:4.3 - Correspondence and source return

Architecture descriptions become risky when a reader cannot tell whether two views describe the same architecture claim, the same selected structure, related structures, or different entities of concern. Use correspondence records or source-return conditions when the description is reused across viewpoints, source editions, tool outputs, generated views, or regulated use.

```text
ArchitectureDescriptionCorrespondence@Context ::= {
  architectureDescriptionRef:
  architectureClaimRef:
  fromViewRef:
  toViewRef:
  correspondenceKind:
    sameArchitectureClaim | sameSelectedStructure |
    refinement | abstraction | projection |
    sourceDerived | conflict | declaredOther,
  preservedStructureRefs?:
  lostStructureRefs?:
  sourceReturnCondition?:
  admissibleUse:
  nonAdmissibleUse:
}
```

Correspondence is not proof, assurance, or gate passage. It is a relation that lets a reader use more than one architecture view without silently changing the EntityOfConcern.

#### C.30.AD:4.4 - Freshness and currentness boundary

Use a freshness cue only when the architecture description's admissible use depends on source edition, structure edition, model version, deployment context, or external condition.

```text
ArchitectureDescriptionFreshnessCue:
  sourceEditionRefs:
  structureEditionRefs?:
  modelOrToolEditionRefs?:
  knownRefreshTrigger:
    sourceChange | deploymentChange | interfaceChange |
    controlRateChange | modelEditionChange | evidenceDecay |
    toolApiChange | legalRegulatoryChange |
    incidentFinding | declaredOther | unknown,
  admissibleUseUntil?:
  sourceReturnCondition:
```

Freshness does not make the description evidence-sufficient. It only bounds the use of the description.

#### C.30.AD:4.5 - Specification-use and publication boundary

An architecture description can be used as a specification only when that use is declared. Specification use is not a new architecture kind; it is a use boundary over a Description episteme or its publication.

```text
ArchitectureDescriptionSpecificationUse@Project ::= {
  architectureDescriptionRef:
  sourceEpistemeRef | sourceViewRef,
  publicationUnitRef?:
  governedUse:
    coordination | implementationGuidance | procurement |
    verificationPlanning | assuranceInput | releaseInput |
    declaredOther,
  exactNeighborPatternRef?:
  admissibleUse:
  nonAdmissibleUse:
}
```

If the specification use becomes evidence, assurance, gate, work, decision, causal-use, or release authority, apply the neighboring pattern governing that claim to that authority claim. The architecture description remains the description boundary, not the authority.

Publication forms, diagrams, model faces, files, cards, dashboards, and generated relation graphs remain publications, views, faces, carriers, source-current records, or renderings unless the source episteme and use boundary are explicit.

#### C.30.AD:4.6 - Neighboring-pattern applications

| Question after the architecture-description boundary is clear | FPF application |
| --- | --- |
| Grounded architecture claim, selected structures, first architecture move | `C.30` |
| Architecture or structure wording is still overloaded | `C.30.P` |
| Architecture structural view or structure-kind and viewpoint relation | `C.30.ASV` |
| Transformation-flow relation or graph description used by architecture | `C.30.TFS-REL` and `E.18` |
| Control structure view | `C.30.LCA` |
| Cross-scope or interlevel architecture residual, conflict, or frustration in the described holon | `C.30.ILC` |
| Multilevel-learning or frustration mathematical-lens result with recoverable level mapping or scale mapping and preserved structure and lost structure | `C.29` with the admitted C.29-local lens output |
| Residual-reducing candidate architecture moves, candidate palette, candidate front, shortlist, selected set, or optimization over candidates | `G.5` for candidate sets, `C.11` for final local choice, and measurement or comparison patterns named by value when those claims are being made |

| Generic description, view, viewpoint, publication, carrier, MVPK face | `A.7`, `E.17.0`, `E.17.1`, `E.17.2`, `E.17`, or `C.2.P` |
| Function or functionality wording | `A.6.F` |
| Module, interface, port, signature, or reusable structure relation | `A.6.M`, a signature or interface pattern named by value, `C.31`, or `C.31.RSA` |
| Mathematical lens or preserved and lost mathematical structure | `C.29` |
| Characteristic, scale, coordinate, score, or quality claim | `C.16.P`, `C.16`, `A.19`, `C.25`, or quality pattern governing the claim |
| Evidence, assurance, gate, work, decision, causal-use, release | `A.10`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, `C.28`, release or admissibility pattern, or governing pattern |

