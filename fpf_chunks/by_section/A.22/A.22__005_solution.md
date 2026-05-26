---
chunk_kind: "child"
pattern_id: "A.22"
pattern_title: "Structure and Structural Views (STRUCT-CAL)"
section_id: "A.22:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22/A.22__005_solution.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "A.22 — Structure and Structural Views (STRUCT-CAL)"
  - "A.22:4 — Solution"
line_start: 28269
line_end: 28487
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.6.2"
  - "A.6.3"
  - "A.6.F"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.D2"
  - "E.10.SEMIO"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "F.18"
  - "G.5"
  - "G.6"
keywords:
  - "architecture support"
  - "preserved/lost structure"
  - "selected structure"
  - "source return"
  - "structural description"
  - "structural view"
  - "structure"
---

### A.22:4 - Solution

Select `candidate:U.Structure` as a dependent, non-agentive intensional object:

> `candidate:U.Structure` is the organization of typed relations, constraints, invariants, variation classes, and admissible references to operation or dynamics descriptions over declared support, inside a bounded context and admissible-use frame.

`candidate:U.Structure` is not the support itself, not a `U.Holon` by default, not Work, not Evidence, not Gate, not Decision, not Architecture, and not a mathematical lens. It does not act, optimize, prove, warrant, or decide. Claims about a structure are carried by `U.Episteme`, `U.View`, evidence, publication, decision, or neighboring support records. Descriptions and views of structure are D/S epistemes under I/D/S, not the structure itself.

A.22 governs `candidate:U.Structure` as a dependent, non-agentive intensional object and the D/S descriptions and views that describe selected structure in one bounded context. It governs structure carriers, structure-claim support records, structural descriptions, structural views, extracted structural views, structural-aspect descriptions, structural-coarsening descriptions, and structure-general source-return conditions. It does not govern architecture descriptions directly; `C.30` and its subpatterns govern architecture as a use of selected structure over a described holon.

#### A.22:4.1 - Structure carrier

```text
candidate:U.Structure ::= {
  structureId,
  declaredSupportRef:
    U.EntityRef | U.HolonRef | U.EpistemeRef | DeclaredSubstrateRef,
  boundedContextRef,
  relationSignatureRefs?,
  operationOrDynamicsDescriptionRefs?,
  constraintRefs?,
  invariantRefs?,
  symmetryRefs?,
  topologyOrGeometryRefs?,
  stateSpaceRefs?,
  causalOrPredictiveDescriptionRefs?,
  informationRegularityRefs?,
  coarseGrainingRefs?,
  generalStructureAspectKindRefs:
    functional | mereological | modular | flowTransduction |
    control | workMethod | roleEnactor | evidenceAssurance |
    semantic | informational | causalPredictive | dynamical |
    algebraic | topological | geometric | scaleCoarseGrained |
    otherDeclared,
  granularityOrScaleRef?,
  equivalenceOrIsomorphismCriterion?,
  variationClassRefs?,
  preservedUnder?,
  brokenBy?,
  admissibleUse,
  nonAdmissibleUse
}
```

The field list is a recovery aid, not a demand to fill every field. The ordinary record names only the fields that carry the next admissible move. When state, dynamics, causality, measurement, bridge, evidence, assurance, gate, work, decision, or mathematical-lens claims are live, the record cites the neighboring pattern instead of absorbing that claim kind into A.22.

A.22 `generalStructureAspectKindRefs` are general structure-aspect cues. C.30.ASV `ArchitectureStructureKindRef` values are architecture-local structure-kind classifiers for structures selected by `ArchitectureOf@Context`. A matching label does not imply identity. Use a declared mapping when an A.22 aspect is used as an architecture structure kind.

#### A.22:4.2 - Structure claim support

Use a support record when the structure claim relies on a source, observation, mathematical lens, simulation, generated representation, evidence relation, or declared source set.

```text
StructureClaimSupport@Context ::= {
  structureRef: candidate:U.StructureRef,
  supportSourceRef:
    SourceEpistemeRef | SourceEpistemePublicationRef | SourceViewRef |
    A10EvidenceSupportRef | C29LensOutputRef |
    SimulationDescriptionRef | ModelRepresentationDescriptionRef |
    DeclaredSourceSetRef | OtherDeclaredSupportRef,
  supportSourceGoverningPatternRef,

  supportPosture:
    sourceDerived | observationSupported | mathematicalLensSupported |
    simulationSupported | representationSupported | evidenceSupported |
    reportOnly,
  validationBoundary,
  sourceReturnCondition?,
  admissibleUse,
  nonAdmissibleUse
}
```

`candidate:U.Structure` does not carry `descriptionOfStructure`, `representationOfStructure`, `extractedStructureClaim`, `mathematicalLensStructureClaim`, or `simulationSubstrateClaim` as internal postures. Those are support, description, lens, extraction, or simulation claims about a structure. `PublicationRef` is not an admissible substitute for the source episteme, source view, evidence relation, or lens output.

#### A.22:4.3 - D/S structural descriptions and views

Structural descriptions and views reuse existing episteme and view machinery. Architecture does not define a second ontology of descriptions, views, viewpoint bundles, multi-view descriptions, publications, carriers, or source-pin sets. Every record whose name ends in `Description@Context` here is a specialization of existing `U.Episteme` governed by `C.2.1` and `E.10.D2`. Every record whose name ends in `View@Context` here is a specialization of existing `U.View` or `U.EpistemicViewing` governed by `A.6.3` and `E.17.0`. `DescriptionContext` is imported, not locally redefined.

```text
StructuralDescription@Context ::= {
  descriptionId,
  descriptionContext: DescriptionContext(DescribedEntityRef, BoundedContextRef, ViewpointRef),
  structureRefs: FinSet(candidate:U.StructureRef),
  structureSupportRefs?: FinSet(StructureClaimSupportRef),
  describingEpistemeRef,
  admissibleUse,
  nonAdmissibleUse
}

StructuralView@Context ::= {
  viewId,
  descriptionContext: DescriptionContext(DescribedEntityRef, BoundedContextRef, ViewpointRef),
  structureRefs: FinSet(candidate:U.StructureRef),
  structuralAspectDescriptionRefs?,
  selectedRelationsOrOperations,
  hiddenOrLostStructure,
  admissibleUse,
  nonAdmissibleUse
}
```

`descriptionContext.ViewpointRef` is the viewpoint field. Do not duplicate it locally under another name unless a neighboring pattern supplies a more specific view record.

#### A.22:4.4 - Extracted and transformed structural views

Use extracted or transformed structure records when a corpus, trace, model, lens, simulation, generated representation, coarsening pass, or observer/budget boundary produces a view of structure that may hide distinctions.

```text
ExtractedStructuralView@Context ::= {
  extractedViewId,
  descriptionContext: DescriptionContext(DescribedEntityRef, BoundedContextRef, ViewpointRef),
  sourceCorpusOrTraceRefs,
  structureRefs: FinSet(candidate:U.StructureRef),
  extractionDescriptionRef,
  preservedStructure,
  lostStructure,
  validationBoundary,
  sourceReturnCondition,
  admissibleUse,
  nonAdmissibleUse
}

StructureExtractionDescription@Context ::= {
  extractionDescriptionId,
  descriptionContext: DescriptionContext(DescribedEntityRef, BoundedContextRef, ViewpointRef),
  sourceInputKind,
  lensOrMethodRef,
  budgetOrObserverBoundary?,
  preservedStructureKinds,
  lostStructureKinds,
  validationBoundary,
  sourceReturnCondition,
  admissibleUse,
  nonAdmissibleUse
}

StructuralAspectDescription@Context ::= {
  aspectDescriptionId,
  descriptionContext: DescriptionContext(DescribedEntityRef, BoundedContextRef, ViewpointRef),
  aspectKindRef,
  structureRefs: FinSet(candidate:U.StructureRef),
  structureSupportRefs?: FinSet(StructureClaimSupportRef),
  admissibleUse,
  nonAdmissibleUse
}

StructuralCoarseningDescription@Context ::= {
  coarseningDescriptionId,
  descriptionContext: DescriptionContext(DescribedEntityRef, BoundedContextRef, ViewpointRef),
  sourceStructureRefs: FinSet(candidate:U.StructureRef),
  targetStructureRefs: FinSet(candidate:U.StructureRef),
  preservedUnder,
  brokenBy,
  lostStructure,
  sourceReturnCondition,
  admissibleUse,
  nonAdmissibleUse
}
```

#### A.22:4.5 - Source return

`SourceReturnCondition` is present when compression, extraction, coarsening, evidence reuse, mathematical-lens use, simulation, ML evaluation, bounded exception, many-to-many allocation, or decision support hides a distinction needed for action, assurance, causal use, legal review, regulatory review, comparison, or subsequent decision reopening.

Do not make source return mandatory for ordinary local recognition when no hidden distinction is being used for action. The condition is live only when the repaired text still relies on the source-side distinction.

#### A.22:4.6 - Relation to architecture
`StructuralAspectDescription@Context` describes one selected structural aspect under A.22. It is not an `ArchitectureStructureKindRef` by itself. `ArchitectureStructuralView@Context` is a C.30.ASV view over structures selected by `ArchitectureOf@Context` and typed by `ArchitectureStructureKindRef`.

A.22 is intentionally upstream of C.30. Architecture uses structure; structure does not import architecture as a parent.

`C.30` uses A.22 by selecting architecture-relevant structures for one described holon through `ArchitectureOf@Context`. `C.30.ASV` then governs architecture structural views over those selected structures. A structure can be used by architecture, but a structure is not an architecture merely because an architecture description refers to it.

Architecture-related records that belong to C.30 or its subpatterns include `ArchitectureOf@Context`, `ArchitectureDescription@Context`, `ArchitectureStructuralView@Context`, `ArchitectureStructureKindRef`, `ArchitectureStructureKindTriage@Project`, `FunctionalStructureView@Context`, `ArchitectureFlowStructureRelation@TGA`, `ControlStructureView@Context`, and `CrossScopeArchitectureResidualTriage@Context`. A.22 may name them as neighboring exits. It does not define their architecture-specific conformance.

#### A.22:4.7 - Boundary and repair table

| Tempting collapse | A.22 repair |
| --- | --- |
| The support source is the structure. | Name `declaredSupportRef` and, when support is live, `StructureClaimSupport@Context`; keep structure as selected organization over support. |
| The diagram, graph, table, dashboard, or carrier is the structure. | Treat it as publication, description, view, or support only when its relation is explicit. |
| A TGA graph is the structure in every sense. | Use `E.18` for graph, path, crossing, and flow valuation; use A.22 only for the selected structure claim; use `C.30.TGA-FLOW-REL` when architecture-flow description is live. |
| A mathematical lens output is the structure. | Use `C.29` for lens adequacy and cite `C29LensOutputRef` only as support. |
| A structure proves evidence, assurance, safety, causality, or gate passage. | Assign those claims to `A.10`, `G.6`, `B.3`, `C.28`, `A.20`, or `A.21`. |
| A structure is a decision or work record. | Use `C.11`, `A.20`, `A.21`, `A.15`, or the project-side decision pattern that governs the live claim. |
| Architecture is a root kind beside structure. | Use `C.30`: architecture is selected structure for a described holon through `ArchitectureOf@Context`. |
| Function, module, interface, platform, layer, or stack becomes a root kind by appearing in structure prose. | Use `A.6.F`, the exact module/interface repair pattern when that claim kind is live, `A.6.0`, `A.6.5`, `A.6.B`, `A.6.C`, `A.6.8`, `E.18`, `C.30.ASV`, and neighboring patterns as triggered. |

#### A.22:4.8 - Worked slices

**Architecture kernel slice.** A team says, "the architecture is the graph." A.22 does not accept that sentence as a root-kind claim. The repair is:

```text
declaredSupportRef: TransductionGraphRef under E.18
candidate structure: selected flow/transduction structure
support record: StructureClaimSupport@Context(
  supportSourceRef = SourceViewRef or E18 graph/path/crossing record,
  supportSourceGoverningPatternRef = E.18,
  supportPosture = sourceDerived | representationSupported,
  validationBoundary = path/slice/crossing currentness boundary
)
next exit: C.30.TGA-FLOW-REL when this supports an architecture-flow description
non-admissible use: graph as whole architecture, work, evidence, gate, or decision
```

The useful move survives: the practitioner can use the graph as flow-structure support without turning it into architecture ontology.

**Extracted code structure slice.** A code-agent relation graph or probe JSON reports imports, calls, registry wiring, and data-flow links. A.22 treats it as an extracted structural view only when the source, extraction method, preserved structure, lost structure, validation boundary, and source-return condition are named. The relation graph or probe output is not the codebase architecture itself and is not proof of internal agent belief, assurance, or release readiness.

```text
ExtractedStructuralView@Context:
  sourceCorpusOrTraceRefs: repo snapshot, probe outputs, traces
  preservedStructure: selected typed relation families
  lostStructure: unexplored regions, dynamic calls, hidden generated code, ambiguous relation kinds
  validationBoundary: probe coverage and source edition
  sourceReturnCondition: when an architecture decision, assurance use, or repair depends on a relation not observed by the extraction
```

