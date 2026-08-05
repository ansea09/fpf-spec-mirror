---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__002_use-this-when.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:0 — Use this when"
line_start: 60197
line_end: 60262
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

### C.30.AD:0 - Use this when

Use this pattern when current work must create, inspect, compare, reuse, or rely on a durable architecture-description episteme, a multi-view description set, a generated architecture-relation view, or a specification-use record. Open it only after the practitioner can name the exact described object: one holon, one obtaining `ArchitectureRelation` occurrence, or one exact selected `U.Structure`.

Use `C.30.AD` when the practitioner needs to know:

- which exact holon, architecture-relation occurrence, or selected structure each description episteme is about;
- which architecture claim is being carried or inspected, without substituting that claim for the description's EntityOfConcern;
- which selected structures or architecture structure kinds are described;
- which descriptions qualify as `U.View` under which exact `U.Viewpoint` epistemes and independently obtaining `EpistemeViewpointConformanceRelation` occurrences;
- which cross-view correspondence claims, source-to-use paths, source-return conditions for stronger use, freshness boundaries, and specification-use boundaries make the description usable;
- what the description can guide and which uses are non-admissible.

**What goes wrong if missed.** A diagram, documentation set, generated relation graph, model card, ADR publication set, file, or architecture model starts acting as architecture, selected structure, `U.View`, proof, gate, assurance, decision, work authorization, or release authorization by presentation alone.

**What this buys.** The practitioner can keep architecture descriptions inspectable across exact subjects, views, viewpoints, selected structures, cross-view correspondence claims or separately governed relations, source-to-use paths, applicable source-return conditions, representations, publications, and direct governing-pattern applications.

**First useful description-use output.** Write one `ArchitectureDescriptionUseCard@Project`:

```text
ArchitectureDescriptionUseCard@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureDescriptionProjectUseRelationRef?: U.RelationRef governed by the exact description-use or work-use pattern
  architectureDescriptionRef?: U.EpistemeRef constrained to ArchitectureDescription
  entityOfConcernRef: exactly one of (
    describedHolonRef | architectureRelationOccurrenceRef | selectedStructureRef
  )
  effectiveReferenceScheme: U.ReferenceScheme, byValue
  architectureClaimRefs?: FinSet(U.EpistemeRef constrained to ArchitectureClaim)
  claimScope?: U.ClaimScope, byValue
  concernRefs?: FinSet(U.EntityRef)
  modelUseStructureRef?: U.StructureRef
  empiricalGroundingRelationRefs?: FinSet(U.RelationRef)
  descriptionPurpose:
  selectedStructureRefs: FinSet(U.StructureRef)
  structureKindRefs: FinSet(ArchitectureStructureKindRef)
  viewpointRefs?: FinSet(U.EpistemeRef constrained to U.Viewpoint)
  architectureStructuralViewRefs?: FinSet(U.EpistemeRef constrained to ArchitectureStructuralView)
  viewpointConformanceRelationRefs?: FinSet(EpistemeViewpointConformanceRelationRef)
  correspondenceClaimOrRelationRefs?: FinSet(U.EpistemeRef | U.RelationRef)
  sourceToUsePathRefs?: FinSet(U.RelationRef)
  sourceReturnCondition?:
  representationRefs?: FinSet(U.EntityRef)
  publicationOccurrenceRefs?: FinSet(EpistemePublicationRelationRef)
  publicationFormRefs?: FinSet(U.EntityRef)
  carrierRefs?: FinSet(U.EntityRef constrained to U.PresentationCarrier)
  specificationUseBoundary?:
  admissibleUse:
  nonAdmissibleUse:
  firstGoverningPatternApplication?:
```

`@Project` is a compatibility and retrieval cue for a project-side use card. The suffix supplies no project identity, authority, context, viewpoint, parthood, or work occurrence. When one actual project matters, `projectWorkOccurrenceRef` identifies the composite `U.Work` recovered under `A.15.6`, and `architectureDescriptionProjectUseRelationRef` identifies the exact obtaining relation by which this description use concerns that work. Name that relation's direct governing pattern; the reference to work alone does not establish project locality.

The card is a controlled first-pass slice, not an identity constructor. It can close ordinary use only when it names one exact EntityOfConcern, the effective `U.ReferenceScheme`, one usable description purpose, the selected structures and their structure-kind classifications, admissible use, non-admissible use, and one remaining architecture candidate use or direct governing-pattern application. If it calls the description a `U.View`, it also names the exact viewpoint episteme and the separately obtaining conformance relation. Expand to the fuller `ArchitectureDescription` record when cross-view correspondence, source use, a stronger-use source-return condition, freshness, specification use, regulated use, comparison, publication, representation, or project-side authority use is current.

**Not this pattern when.**

- If the current use is a grounded architecture claim, an obtaining `ArchitectureRelation`, or one first architecture question, use `C.30`.
- If the current use is a selected structure or structural description outside architecture, use `A.22`.
- If the current use is one architecture structural view and its viewpoint-conformance test, use `C.30.ASV`.
- If the current use is built-asset architecture-description, BIM, IFC, asset-information, digital-twin, or reference-designation specialization, use `C.30.AD.BA`.
- If architecture or structure wording is still ambiguous, use `C.30.P`.
- If the current use is only a representation, publication occurrence, publication face, publication form, report, dashboard, file, carrier, source-expression relation, or publication-currentness relation, use `C.2.P`, `E.17`, `E.24.PUB`, or the direct representation, publication, or source-use pattern governing the claim.
- If the description is being used as pattern-use recommendation, work-entry readiness, evidence, assurance, gate passage, decision, work authorization, causal-use claim, release authorization, deontic permission, or mathematical-lens use, keep `C.30.AD` only for the description boundary and apply the direct pattern governing that claim to the claim being made.

