---
chunk_kind: "child"
pattern_id: "E.18.3"
pattern_title: "Constraint-Governed Transformation-Flow Unfolding Structure"
section_id: "E.18.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.3/E.18.3__006_solution.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "E.18.3 — Constraint-Governed Transformation-Flow Unfolding Structure"
  - "E.18.3:4 — Solution"
line_start: 82380
line_end: 82499
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.3.NAR"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.30.TFS-REL"
  - "C.32.P2S"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.23"
  - "G.11"
  - "G.5"
keywords:
---

### E.18.3:4 - Solution

Select `ConstraintGovernedTransformationFlowUnfoldingStructure@Context <: U.Structure` as the E.18 transformation-flow specialization of `ConstraintGovernedUnfoldingStructure@Context`.

```text
ConstraintGovernedTransformationFlowUnfoldingStructure@Context <: U.Structure:
  unfoldingStructureRef: U.EntityRef, referencing one ConstraintGovernedUnfoldingStructure@Context
  boundedContextRef: U.BoundedContextRef
  transformedEntityRef: U.EntityRef
  transformedEntityKindRef: U.KindRef
  transformationPositionRefs[]: U.EntityRef, each referencing one ConstraintGovernedUnfoldingPosition@Context
  governingPatternPositionRelationRefs[]: U.EntityRef, each referencing one TransformationFlowGoverningPatternPositionRelation@Context
  transferRelationReferenceEpistemeRefs[]: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with structuralFunction=transfer
  dependencyRelationReferenceEpistemeRefs[]: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with structuralFunction=dependency
  pathIds[]: E.18 PathId
  pathSliceIds[]: E.18 PathSliceId
  demonstrativeSliceRefs[]: U.EpistemeRef, each referencing one DemonstrativeUnfoldingSlice@Context
  crossingRelationReferenceEpistemeRefs[]: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with structuralFunction=crossing
  guardRelationReferenceEpistemeRefs[]: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with structuralFunction=guard
  transformationFlowValuationRef?: U.EntityRef, referencing one E.18 TransformationFlowValuation
  methodWorkLinkageRef?: U.EntityRef, referencing one MethodWorkUnfoldingLinkage@Context
  evidenceRelationReferenceEpistemeRefs[]?: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with subjectUse=evidence
  assuranceRelationReferenceEpistemeRefs[]?: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with subjectUse=assurance
  architectureUseReferenceRefs[]?: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with subjectUse=architecture
  narrativeUseReferenceRefs[]?: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with subjectUse=narrative
  publicationUseReferenceRefs[]?: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with subjectUse=publication
  preservedTransformationStructureRefs[]: U.EntityRef, each referencing one U.Structure
  structureInformationAdequacyNoteRefs[]?: U.EpistemeRef, each referencing one StructuralInformationAdequacyNote@Context
  governingPatternReturnBoundaryRefs[]: U.EntityRef, each referencing one UnfoldingStructureUseBoundaryCondition@Context
  stopBoundaryRef: U.EntityRef, referencing one UnfoldingStructureUseBoundaryCondition@Context
```

`unfoldingStructureRef` names the generic `ConstraintGovernedUnfoldingStructure@Context` whose `specializedStructureRef` points to this narrower transformation-flow structure. The reciprocal references state the specialization relation; they do not split the primary EntityOfConcern or create a second transformation-flow structure.

The transformed entity and its kind are both present. A flow position points to one typed `ConstraintGovernedUnfoldingPosition@Context`; an external governed position is related through `TransformationFlowGoverningPatternPositionRelation@Context`, not put into a heterogeneous adjacency list.

Paths and demonstrations remain different. `pathIds[]` and `pathSliceIds[]` identify E.18 flow structure. `demonstrativeSliceRefs[]` identify post-admission A.22.CGUS epistemes whose EntityOfConcern is the already-admitted wider structure. A pre-admission flow card, worked example, or explanation remains a separate `ProvisionalUnfoldingDemonstrationDescription@Context` and does not fill `demonstrativeSliceRefs[]`. An admitted demonstrative slice can be linear while the current flow structure branches, joins, cycles, or keeps alternatives live.

A pattern-selection flow, selected-pattern-application flow, and downstream-subject-work flow keep different EntitiesOfConcern, changes, work occurrences, results, direct governing patterns, constraints, and returns. One flow's result may fill an input, tool, context, or constraint position in another flow without changing kind. E.18 relates those positions without turning the flows into one workflow. When a `DemonstrativeUnfoldingSlice@Context` asserts this cross-flow provenance, its `transformationFlowStructureRef`, `pathSliceId`, and `designRunTag` are all present; otherwise all three are absent. Those fields locate the demonstration in one flow valuation. They do not merge the demonstrated structures, rows, work occurrences, or result claims. A nested pattern-selection slice is present only when selection provenance is current; it returns a candidate, fit finding, or recommendation to the enclosing demonstrated-pattern-use row rather than borrowing that row's application result.


Preserved transformation structure is carried by exact `U.Structure` refs. Captured, expected-but-uncaptured, lost, and hidden structure for a declared use is carried by C.33 `StructuralInformationAdequacyNote@Context`. E.18.3 does not mint parallel free-text loss fields. Stop and governing-pattern return are different boundary relations. Source currentness and decay remain with G.11; E.18 slice-local flow refresh remains with E.18.

`methodWorkLinkageRef?` appears only when a named receiving use relies on an inspectable method-to-work relation. A method, method description, WorkPlan, work-entry readiness relation, or performed Work remains governed by its exact A.3 or A.15 pattern.

#### E.18.3:4.0 - Application sequence

1. Start from one admitted generic CGUS and name this narrower structure through the reciprocal specialization refs.
2. Name the transformed entity and kind, then the typed transformation positions that matter to the current use.
3. Reference the exact transfer, dependency, crossing, or guard relations. Add a subject-use classifier only when the same relation supports a separately governed evidence, assurance, architecture, narrative, or publication use.
4. Connect every neighboring governed position through its exact kind, ref, governing pattern, connection kind, rationale, and supporting relation when that connection kind needs one.
5. Name paths and path slices as transformation-flow structure; name demonstrative slices separately as presentation epistemes. Add the E.18 flow locator triple only when cross-flow demonstration provenance is current.
6. Name preserved transformation structures and use C.33 for omitted or hidden structure needed by the declared use.
7. Add a stop boundary and separate returns to the direct patterns governing stronger claims. If the transformation substrate, exact relation, or typed connection is absent, keep the artifact as a `ProvisionalUnfoldingDemonstrationDescription@Context`, route card, graph description, or broader A.22.CGUS admission question; do not fill `demonstrativeSliceRefs[]`.

#### E.18.3:4.0a - Exact relation references

`E.18.3` governs `TransformationFlowRelationReference@Context`, a reference-bearing episteme whose EntityOfConcern is one exact transformation-flow relation instance. The episteme records two independent classifications without becoming the referenced relation:

```text
TransformationFlowRelationReference@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact relation instance
  entityOfConcernKindRef: U.KindRef, referencing that relation kind
  boundedContextRef: U.BoundedContextRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  FlowStructureSlot = <FlowStructureSlot, ConstraintGovernedTransformationFlowUnfoldingStructure@Context, U.EntityRef>
  StructuralFunctionSlot? = <StructuralFunctionSlot, TransformationFlowStructuralFunctionValue, by-value>
  SubjectUseSlot? = <SubjectUseSlot, TransformationFlowSubjectUseValue, by-value>
  RelationSignatureSlot = <RelationSignatureSlot, U.Signature, U.EntityRef>
  DirectGoverningPatternSlot = <DirectGoverningPatternSlot, U.MethodDescription, U.EntityRef>
```

`TransformationFlowStructuralFunctionValue` is `transfer | dependency | crossing | guard`. It states what the referenced relation does inside the flow structure. `TransformationFlowSubjectUseValue` is `evidence | assurance | architecture | narrative | publication`. It states which separately governed subject use the same relation supports. At least one classifier is present; both may be present when both claims are true. Neither classifier changes the exact relation signature, value kind, value ref, or direct governing pattern.

For example, one crossing relation can also support evidence use. It remains one exact relation with `structuralFunction=crossing` and `subjectUse=evidence`; the two classifiers do not create two relations or let E.18.3 own the evidence claim.

#### E.18.3:4.1 - Connections to positions governed elsewhere

```text
TransformationFlowGoverningPatternPositionRelation@Context <: U.Relation:
  FlowStructureSlot = <FlowStructureSlot, ConstraintGovernedTransformationFlowUnfoldingStructure@Context, U.EntityRef>
  FlowPositionSlot = <FlowPositionSlot, ConstraintGovernedUnfoldingPosition@Context, U.EntityRef>
  NeighborGoverningPatternSlot = <NeighborGoverningPatternSlot, U.MethodDescription, U.EntityRef>
  NeighborPositionKindSlot = <NeighborPositionKindSlot, U.Kind, U.KindRef>
  NeighborPositionRefSlot = <NeighborPositionRefSlot, U.Entity, U.EntityRef>
  PositionConnectionKindSlot = <PositionConnectionKindSlot, TransformationFlowPositionConnectionKindValue, by-value>
  SupportingRelationReferenceSlot? = <SupportingRelationReferenceSlot, TransformationFlowRelationReference@Context, U.EpistemeRef>
  ConnectionRationaleSlot = <ConnectionRationaleSlot, U.Episteme, U.EpistemeRef>
  RelationRefKind = U.EntityRef
  Direction = FlowPositionSlot -> NeighborPositionRefSlot
  Dependence = bounded-context local to FlowStructureSlot and NeighborGoverningPatternSlot editions
  Identity = <FlowStructureSlot, FlowPositionSlot, NeighborGoverningPatternSlot, NeighborPositionRefSlot, PositionConnectionKindSlot>
```

`TransformationFlowPositionConnectionKindValue` is `basisDependency | producedResult | governingConstraint | returnTarget | comparisonPeer`. `basisDependency`, `producedResult`, `governingConstraint`, and `returnTarget` carry an exact supporting relation reference. `basisDependency` states a dependency on a basis position governed elsewhere; it creates no obligation. `comparisonPeer` permits the supporting reference to remain absent because this E.18.3 relation itself states the exact pairwise comparison connection and rationale. The neighbor ref is always paired with its exact kind.

This connection relation keeps the neighboring pattern visible without importing its result kind into transformation-flow ontology. Recommendation, method, work, evidence, assurance, gate, architecture, narrative, publication, and currentness claims remain under their direct governing patterns.

#### E.18.3:4.2 - Provisional flow demonstration and admitted slice

Before a `ConstraintGovernedTransformationFlowUnfoldingStructure@Context` passes admission, a path fragment, flow card, worked example, replay, or first-use explanation remains a `ProvisionalUnfoldingDemonstrationDescription@Context`. Its subject is the transformed entity, current flow question, or proposed continuation set. Candidate positions and relation descriptions may guide discovery, but they are not admitted transformation positions or relation instances.

After the generic CGUS and this transformation-flow specialization are admitted, a separate `DemonstrativeUnfoldingSlice@Context` may teach or demonstrate one admissible traversal. It names the admitted CGUS as EntityOfConcern and states included typed positions, C.33 notes for relevant omitted structure, loop-compression rule, presentation-ordering rule, alternatives, and return boundary when those affect use. It may cite the provisional description as derivation basis; it does not retype that description or the transformed entity.

Do not infer that demonstrated order is project work order. If work order is current, open the work-plan or method-description pattern. Do not infer that a demonstrated path is the whole transformation-flow topology. If the admitted flow has branches, joins, cycles, alternatives, or partial orders, name what the slice omits or compresses before relying on it for comparison, architecture, evidence, or work planning.

A pre-admission flow card can still help slot discovery. Each visible candidate position states the subject-domain object or question it concerns and the exact admission coordinate still unresolved. Once the transformed entity, typed positions, exact crossing or guard relations, valuation, preserved structures, C.33 notes, governing-pattern connections, and boundaries are recoverable, admit the structure first and create the slice second. This preserves the practical aid without circularly using a supposed slice as evidence for its own whole.

#### E.18.3:4.3 - Boundary

This `U.Structure` specialization is not a second transformation ontology, workflow, method, work plan, performed work, mathematical graph, publication, evidence relation, gate decision, architecture decision, or architecture description. It is a transformation-flow structure over typed transformation positions and exact relation references, together with explicit connections and returns to the patterns governing stronger claims.

#### E.18.3:4.4 - Replay and change localization

Replay one use from the reciprocal CGUS specialization refs, transformed entity and kind, typed transformation positions, exact relation signatures and values, structural-function and subject-use classifiers, governed-position connections, path and slice ids, optional valuation, preserved structures, C.33 adequacy notes, and stop and return boundaries. For each continuation, recover the exact relation or guard that admits it and the pattern governing any stronger claim.

Localize changes by the relation they affect. A changed relation value reopens its classifiers, dependent guards, and continuations. A changed neighbor value or kind reopens that governed-position connection and its supporting relation. A changed path or valuation reopens only the dependent path slices and demonstrations. Changed omitted structure reopens the C.33 note. Source edition, freshness, telemetry, and decay remain G.11 changes; E.18 owns only slice-local flow refresh. Reconstruct the wider specialization only when the transformed entity, transformation-position set, relation topology, preserved structure, or declared use boundary changes.

