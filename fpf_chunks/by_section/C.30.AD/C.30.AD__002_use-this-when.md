---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__002_use-this-when.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:0 — Use this when"
line_start: 59047
line_end: 59112
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

### C.30.AD:0 - Use this when

Use this pattern when work must create, inspect, compare, reuse, or rely on an architecture description, a set of such descriptions, a generated view of architecture relations, or a description used as a specification. First name what the description is about: one holon, one `ArchitectureRelation` occurrence that actually obtains, or one selected `U.Structure`.

Use it to answer:

- what architecture-side thing each description is about: a holon, an obtaining architecture-relation occurrence, or a selected structure;
- which architecture claim the description carries or lets the practitioner inspect, without confusing that claim with the thing described;
- which selected structures and structure kinds the description covers;
- whether a description really qualifies as `U.View`: name the viewpoint and show that the E.17.0 conformance relation actually holds;
- how views correspond, which sources enter the use, when a stronger use must return to a source, how fresh the description is, and whether specification use is allowed;
- what the description may guide, what it may not be used for, and what architecture move comes next.

**What goes wrong if missed.** A diagram, documentation set, generated relation graph, model card, ADR publication set, file, or architecture model is treated as architecture, selected structure, `U.View`, proof, gate, assurance, decision, work authorization, or release authorization merely because it presents those claims.

**What this buys.** A reader can tell what each description is about, how its views correspond, where reused material came from, how fresh it is, what it may be used for, and which other claims need their own patterns.

**First useful description-use output.** In one or two ordinary sentences, say which description is being used, what it describes, which reference scheme gives its terms meaning, why it is being used, which structure matters, what use is allowed, and what architecture move comes next. If you call it a `U.View`, also name the viewpoint and the conformance relation that actually holds. Stop if this answers the question. Keep `ArchitectureDescriptionUseCard@Project` only when the result must be retained, compared, or handed on:

```text
ArchitectureDescriptionUseCard@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureDescriptionProjectUseRelationRef?: U.RelationRef defined by the pattern for the exact relation by which this description use concerns the Work
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
  nextClaimPatternRef?: PatternRef
```

`@Project` is only a retrieval cue. It creates no project, authority, context, viewpoint, parthood, or Work. When an actual project matters, `projectWorkOccurrenceRef` names the composite `U.Work` recovered under `A.15.6`. Include `architectureDescriptionProjectUseRelationRef` only when a named pattern defines how this description use concerns that Work and the relation actually holds. A Work reference alone is not project locality. If locality matters but the relation is not defined, return `missing-governor`; otherwise omit both project-local fields.

The card is optional and does not identify the description. For its declared use, it retains the described thing, reference scheme, purpose, selected structures and their kinds, allowed and disallowed use, and the next architecture move or pattern needed for a separate claim. If it calls the description a `U.View`, it also retains the viewpoint and the conformance relation that actually holds. Use the fuller `ArchitectureDescriptionUseAccount` only when correspondence, source use or return, freshness, specification or regulated use, comparison, publication, representation, or project locality must remain inspectable. Keep any authority claim in its own pattern and relation.

**Not this pattern when.**

- If the current use is a grounded architecture claim, an obtaining `ArchitectureRelation`, or one first architecture question, use `C.30`.
- If the current use is a selected structure or structural description outside architecture, use `A.22`.
- If the current use is one architecture structural view and its viewpoint-conformance test, use `C.30.ASV`.
- If the current use is built-asset architecture-description, BIM, IFC, asset-information, digital-twin, or reference-designation specialization, use `C.30.AD.BA`.
- If architecture or structure wording is still ambiguous, use `C.30.P`.
- If the current use is only a representation, publication occurrence, publication face or form, report, dashboard, file, carrier, source-expression relation, or publication-currentness relation, use `C.2.P`, `E.17`, `E.24.PUB`, or the pattern that defines or tests that representation, publication, or source-use claim.
- If the description is being used as a pattern-use recommendation, work-entry readiness, evidence, assurance, gate passage, decision, work authorization, causal-use claim, release authorization, deontic permission, or mathematical-lens use, keep `C.30.AD` only for the description boundary and use the pattern that defines or tests the other claim.

