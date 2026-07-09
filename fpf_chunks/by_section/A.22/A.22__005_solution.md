---
chunk_kind: "child"
pattern_id: "A.22"
pattern_title: "Structure and Structural Views (STRUCT-CAL)"
section_id: "A.22:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22/A.22__005_solution.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.22 — Structure and Structural Views (STRUCT-CAL)"
  - "A.22:4 — Solution"
line_start: 30930
line_end: 31153
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22.CGUS"
  - "A.6.2"
  - "A.6.3"
  - "A.6.F"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.18.3"
  - "E.24"
  - "E.24.PUB"
  - "F.18"
  - "G.5"
  - "G.6"
keywords:
  - "architecture-description boundary"
  - "preserved and lost structure"
  - "selected structure"
  - "source return"
  - "structural description"
  - "structural view"
  - "structure"
---

### A.22:4 - Solution

Select `U.Structure` as the A.22 ontic head: a dependent, non-agentive `EntityOfConcern` used when selected organization changes a next engineering or reasoning action.

> `U.Structure` is the organization of typed relations, constraints, invariants, variation classes, and admissible references to operation or dynamics descriptions over a declared substrate, or declared A.6.6 base declaration when base-dependence is being claimed, inside a bounded context and admissible-use frame.

The A.22 ontic head is intentionally narrow. `U.Structure` is the selected organization under concern: typed relations, constraints, invariants, variation classes, operation or dynamics references, preserved organization, and lost organization over a declared substrate in a bounded context. The grounding object may be a `U.Holon`, `U.System`, `U.Episteme`, declared substrate, or another declared substrate, EntityOfConcern type, relation kind, or record kind named by the direct governing pattern; the selected structure remains the structure of or over that object.

The first useful A.22 use is about the selected structure itself: name the bounded context, selected structure, relation, constraint, invariant, variation class, operation or dynamics reference that matters, preserved or lost organization, and the structure-use return condition or governing-pattern application needed for work. Description records, views, publications, diagrams, publication forms, and renderings are aids that make that selected-structure use inspectable, reusable, comparable, or safe to rely on; they do not share the center of the Solution.

`U.Structure` may fill `EntityOfConcern` for a structure description, view, or structure-claim relation. When a structure description or view is being used, `DescriptionContext.EntityOfConcernRef` names the selected structure, structure claim, or relation governed by the governing pattern for that use; publication forms, publication units, and renderings only make the episteme or view available.

A.22 governs `U.Structure` as a dependent, non-agentive ontic head. It works first over selected-structure EntityOfConcern records and structure-claim reliance relations. Structural descriptions, structural views, extracted structural views, structural-aspect descriptions, structural-coarsening descriptions, and structure-use return conditions are subordinate record forms used only when they preserve the selected-structure use, expose loss, enable comparison, or state a reliance boundary. A.22 does not govern architecture descriptions directly; `C.30` and its subpatterns govern architecture as a use of selected structure over a described holon.

#### A.22:4.1 - Selected Structure Object

```text
U.Structure ::= {
  structureId,
  declaredStructureSubstrateRef:
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
    functional | mereological | modular | transformationFlow |
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

The field list is a recovery aid, not a demand to fill every field. The ordinary record names only the fields that carry the next admissible use. When state, dynamics, causality, measurement, bridge, evidence, assurance, gate, work, decision, or mathematical-lens claims are being made, the record names the governing pattern instead of absorbing that claim kind into A.22.

A.22 `generalStructureAspectKindRefs` are general structure-aspect cues. C.30.ASV `ArchitectureStructureKindRef` values are architecture-local structure-kind classifiers for structures selected by `ArchitectureOf@Context`. A matching label does not imply identity. Use a declared mapping when an A.22 aspect is used as an architecture structure kind.

#### A.22:4.1a - Compact auxiliary boundary

Use description, publication, source-use, evidence, work, gate, decision, release, architecture-description, and mathematical-lens patterns when those claims are being made. The A.22 application contains the selected-structure portion and the structure-use return condition that protects that structure use; neighboring claims remain with their governing patterns. A publication, diagram, graph, table, dashboard, file, model card, generated representation, or lens output may make a structural description or view available; it does not become the selected structure or supply neighboring claim authority by appearance.

#### A.22:4.1b - Constraint-governed unfolding structure

Use `A.22.CGUS` when the current A.22 structure is an organization among several governed loci and constraints: admitted starting records, already-current starting structures, relation signatures, constraints, invariants, guarded transitions, preserved and lost structure, admissible next forms, and conditions for stop, return, split, or currentness refresh. This structure specialization is still `U.Structure`; it is not a route, workflow, method, work plan, performed work, decision, evidence relation, gate, architecture description, or publication.

Open `A.22.CGUS` only when the candidate has several loci and cross-locus constraints. A route card, table, graph, README entry, narrative, slide, or happy-path example may describe or demonstrate the unfolding structure, but it is not the structure itself.

#### A.22:4.2 - Structure claim reliance relation selection


A.22 does not mint a local generic reliance record. When a structure claim relies on something beyond the selected structure itself, choose the reliance relation kind, name the relation record by value, and name the governing pattern:

| Current reliance relation kind | What is named | Governing ontology to apply |
| --- | --- | --- |
| Source-description relation | source episteme, source view, publication form or rendering where relevant, described structure or structure claim, source-basis pins or structure-use return condition, admissible and non-admissible use | `A.7`, `A.6.3`, `E.17`, `E.17.0`, and local source-publication rules |
| Base-dependence or basedness | `dependent = structure claim or structural description`, `base`, declared `baseRelation`, scope, declared `Γ_time` when temporal scope is claimed, witness refs when witness use is claimed, admissible and non-admissible use | `A.6.6` SWBD or Context-local SWBD specialization |
| EntityOfConcern or grounding-holon grounding | selected EntityOfConcern, `GroundingHolonSlot` when grounding-holon grounding is being claimed, bounded context, viewpoint, reference plane, observation or witness condition if observation or witness use is being claimed | `C.2.1`, `A.6.4`, `A.6.3.RT`, `A.6.6` only if it is a base-dependence claim |
| Evidence or witness reliance | evidence-use relation, evidence-provenance relation, claim ref, witness publication or observation record, timespan and freshness; if an evidence graph is current, its graph path remains a mathematical or provenance expression rather than an action route | `A.10`, `A.2.4`, `G.6` |
| Mathematical-lens reliance | lens candidate, lens card, or lens-use record; primary `EntityOfConcern`; relation record or claim record named by value when lens reliance is being claimed; preserved structure; lost structure; stop condition; `MathLensUseOutputRef`; C.29 lens-use result; or `LensUseAdmissibilityValue` | `C.29`, `C.26`, `F.9`, named mathematical-lens pattern |
| Simulation, generated representation, model, or extracted trace | source publication or representation publication, extraction method, validation boundary, preserved structure, lost structure, structure-use return condition | source-description and Description-context patterns plus `C.29`, `A.10`, or governing pattern when a claim of that kind is being made |

If no reliance relation kind can be selected, keep the wording as a source-finding note, recognition cue, ordinary help, quote-only wording, or reduced-use cue. Do not create a generic reliance record to make the claim look governed.

`U.Structure` does not carry description, representation, extraction, mathematical-lens, simulation, or generic reliance state as an internal structure field. Those are source-description, source-use, base-dependence, evidence, lens, extraction, simulation, or publication relations about a structure. `PublicationRef` is not an admissible substitute for the source episteme, source view, evidence relation, SWBD, or lens output.

#### A.22:4.3 - Structural descriptions and views

Structural descriptions and views reuse existing episteme and view machinery. Architecture does not define a second ontology of descriptions, views, viewpoint bundles, multi-view descriptions, publications, publication forms, or source-pin sets. Every record whose name ends in `Description@Context` here is a specialization of existing `U.Episteme` governed by `C.2.1` and `E.10.D2`. Every record whose name ends in `View@Context` here is a specialization of existing `U.View` or `U.EpistemicViewing` governed by `A.6.3` and `E.17.0`. `DescriptionContext` is imported, not locally redefined.

```text
StructuralDescription@Context ::= {
  descriptionId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, BoundedContextRef, ViewpointRef),
  structureRefs: FinSet(U.StructureRef),
  structureClaimRelianceRefs?: FinSet(U.ScopedWitnessedBaseDeclarationRef | EvidenceRelationRef | EvidenceProvenanceRelationRef | MathLensUseOutputRef | StructureUseReturnConditionRef | NamedClaimGoverningPatternRef),
  describingEpistemeRef,
  admissibleUse,
  nonAdmissibleUse
}

StructuralView@Context ::= {
  viewId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, BoundedContextRef, ViewpointRef),
  structureRefs: FinSet(U.StructureRef),
  structuralAspectDescriptionRefs?,
  selectedRelationsOrOperations,
  hiddenOrLostStructure,
  admissibleUse,
  nonAdmissibleUse
}
```

`descriptionContext.ViewpointRef` is the viewpoint field. Do not duplicate it locally under another name unless the governing pattern supplies a more specific view record.

#### A.22:4.4 - Extracted and transformed structural views

Use extracted or transformed structure records when a corpus, trace, model, lens, simulation, generated representation, coarsening pass, observer boundary, or budget boundary produces a view of structure that may hide distinctions.

```text
ExtractedStructuralView@Context ::= {
  extractedViewId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, BoundedContextRef, ViewpointRef),
  sourceCorpusOrTraceRefs,
  structureRefs: FinSet(U.StructureRef),
  extractionDescriptionRef,
  preservedStructure,
  lostStructure,
  validationBoundary,
  structureUseReturnCondition,
  admissibleUse,
  nonAdmissibleUse
}

StructureExtractionDescription@Context ::= {
  extractionDescriptionId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, BoundedContextRef, ViewpointRef),
  sourceInputKind,
  lensOrMethodRef,
  budgetOrObserverBoundary?,
  preservedStructureKinds,
  lostStructureKinds,
  validationBoundary,
  structureUseReturnCondition,
  admissibleUse,
  nonAdmissibleUse
}

StructuralAspectDescription@Context ::= {
  aspectDescriptionId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, BoundedContextRef, ViewpointRef),
  aspectKindRef,
  structureRefs: FinSet(U.StructureRef),
  structureClaimRelianceRefs?: FinSet(U.ScopedWitnessedBaseDeclarationRef | EvidenceRelationRef | EvidenceProvenanceRelationRef | MathLensUseOutputRef | StructureUseReturnConditionRef | NamedClaimGoverningPatternRef),
  admissibleUse,
  nonAdmissibleUse
}

StructuralCoarseningDescription@Context ::= {
  coarseningDescriptionId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, BoundedContextRef, ViewpointRef),
  sourceStructureRefs: FinSet(U.StructureRef),
  resultStructureRefs: FinSet(U.StructureRef),
  preservedUnder,
  brokenBy,
  lostStructure,
  structureUseReturnCondition,
  admissibleUse,
  nonAdmissibleUse
}
```

#### A.22:4.5 - Structure-use return

`StructureUseReturnCondition` is present when compression, extraction, coarsening, evidence reuse, mathematical-lens use, simulation, ML evaluation, bounded exception, many-to-many allocation, or decision reliance hides a distinction needed for action, assurance, causal use, legal review, regulatory review, comparison, or subsequent decision reopening.

Do not make structure-use return mandatory for ordinary local recognition when no hidden distinction is being used for action. The condition is needed only when the repaired text still relies on a hidden selected-structure, source-basis, source-description, evidence, lens, simulation, extraction, or representation distinction.

#### A.22:4.6 - Relation to architecture
`StructuralAspectDescription@Context` describes one selected structural aspect under A.22. It is not an `ArchitectureStructureKindRef` by itself. `ArchitectureStructuralView@Context` is a C.30.ASV view over structures selected by `ArchitectureOf@Context` and typed by `ArchitectureStructureKindRef`.

A.22 is intentionally upstream of C.30. Architecture uses structure; structure does not import architecture as a parent.

`C.30` uses A.22 by selecting architecture-relevant structures for one described holon through `ArchitectureOf@Context`. `C.30.ASV` then governs architecture structural views over those selected structures. A structure can be used by architecture, but a structure is not an architecture merely because an architecture description refers to it.

Architecture-related records that belong to C.30 or its subpatterns include `ArchitectureOf@Context`, `ArchitectureDescription@Context`, `ArchitectureStructuralView@Context`, `ArchitectureStructureKindRef`, `ArchitectureStructureKindTriage@Project`, `FunctionalStructureView@Context`, `ArchitectureTransformationFlowStructureRelation@Context`, `ControlStructureView@Context`, and `CrossScopeArchitectureResidualTriage@Context`. A.22 may name them as FPF pattern applications. It does not define their architecture-specific conformance.

#### A.22:4.7 - Boundary and repair table

| Tempting collapse | A.22 repair |
| --- | --- |
| The reliance relation is treated as the structure. | Name `declaredStructureSubstrateRef` and, when source-description, source-use, base-dependence, grounding, evidence, lens, simulation, extraction, or representation reliance is being claimed, name the reliance relation record by value and name the governing FPF pattern; keep structure as selected organization over the declared substrate and do not turn that reliance relation into structure. |
| The diagram, graph, table, dashboard, or publication form is the structure. | Treat it as publication, description, view, publication form, source-description relation, base-dependence relation, grounding relation, evidence relation, lens relation, simulation relation, extraction relation, or representation relation only when its relation is explicit. |
| A transformation-flow graph expression is the structure in every sense. | Use `E.18` for graph, path, crossing, and flow valuation; use A.22 only for the selected structure claim; use `C.30.TFS-REL` when an architecture-to-transformation-flow relation claim is being made. |
| A mathematical lens output is the structure. | Use `C.29` for lens-use result and admissibility, and cite `MathLensUseOutputRef` only through C.29 lens-use result, preserved structure, lost structure, and stop-condition discipline. |
| A structure proves evidence, assurance, safety, causality, or gate passage. | Assign those claims to `A.10`, `G.6`, `B.3`, `C.28`, `A.20`, or `A.21`. |
| A structure is a decision or work record. | Use `C.11`, `A.20`, `A.21`, `A.15`, or the project-side decision pattern that governs the claim being made. |
| Architecture is a root kind beside structure. | Use `C.30`: architecture is selected structure for a described holon through `ArchitectureOf@Context`. |
| Function, module, interface, platform, layer, stack, block, expert, cache, router, or gate becomes a root kind by appearing in structure prose. | Use `C.30.STRAT` for source-label recovery, then `A.6.F`, `A.6.M` module-relation repair when a module-interface claim is being made, `A.6.0`, `A.6.5`, `A.6.B`, `A.6.C`, `A.6.8`, `E.18`, `C.30.ASV`, and governing patterns as triggered. |

#### A.22:4.8 - Worked slices

**Architecture kernel slice.** A team says, "the architecture is the graph." A.22 does not accept that sentence as a root-kind claim. The repair is:

```text
declaredStructureSubstrateRef: TransformationFlowStructureRef under E.18, with mathematical graph description under E.18.2 when that expression is the current claim
candidate structure: selected transformation-flow structure
structure-claim reliance relation: selected relation record named by value(
  sourceDescriptionOrPatternApplicationRef = SourceViewRef, E.18 selected structure or crossing record, or E.18.2 mathematical graph description,
  governingPatternRef = E.18, A.6.6, A.10, or C.29 when that reliance claim is being made,
  relationKind = source-description | base-dependence | evidence | lens, selected for this reliance,
  validationBoundary = graph-path currentness boundary, slice currentness boundary, or crossing currentness boundary
)
next FPF pattern application: C.30.TFS-REL when this selected structure is used in an architecture-to-transformation-flow relation
non-admissible use: graph as whole architecture, work, evidence, gate, or decision
```

The useful structure use survives: the practitioner can use the graph as a governed reliance relation for selected flow structure without turning it into architecture ontology.

**Extracted code structure slice.** A code-agent relation graph or probe JSON reports imports, calls, registry wiring, and data-flow links. A.22 treats it as an extracted structural view only when the source codebase or publication, extraction method, preserved structure, lost structure, validation boundary, and structure-use return condition are named. The relation graph or probe output is not the codebase architecture itself and is not proof of internal agent belief, assurance, or release readiness.

```text
ExtractedStructuralView@Context:
  sourceCorpusOrTraceRefs: repo snapshot, probe outputs, traces
  preservedStructure: selected typed relation families
  lostStructure: unexplored regions, dynamic calls, hidden generated code, ambiguous relation kinds
  validationBoundary: probe coverage and source codebase or publication edition
  structureUseReturnCondition: when an architecture decision, assurance use, or repair depends on a relation not observed by the extraction
```

