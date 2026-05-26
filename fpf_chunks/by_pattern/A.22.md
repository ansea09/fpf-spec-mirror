---
chunk_kind: "parent"
pattern_id: "A.22"
pattern_title: "Structure and Structural Views (STRUCT-CAL)"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/A.22.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "A.22 — Structure and Structural Views (STRUCT-CAL)"
line_start: 28199
line_end: 28573
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

## A.22 - Structure and Structural Views (STRUCT-CAL)

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### A.22:1 - Problem frame

Use this pattern when a practitioner needs to say what organization, relation class, constraint, invariant, variation class, or preserved/lost arrangement is being discussed, without turning a diagram, graph, table, document, mathematical lens, support source, decision, or architecture description into the structure itself.

The first useful move is small:

```text
StructureQuestionCard@Project:
declared support:
bounded context:
candidate structure:
relation, operation, constraint, invariant, or variation class:
what is preserved:
what is lost, hidden, or excluded:
support source, if a support claim is live:
admissible use:
non-admissible use:
neighboringPatternExitRefs, if another claim kind is live:
```

`StructureQuestionCard@Project` is a project-side triage aid, not a new structure kind, not a D/S publication, not evidence, and not a decision.

Ordinary minimum: name the bounded context, the candidate structure, one relation, constraint, invariant, or variation class that changes action, one non-admissible overread, and the neighboring pattern exit or stop. Fill preserved or lost structure, support source, and source-return fields only when extraction, coarsening, support reliance, or action reliance is live. All other fields are conditional and may be `not live`.

Stop at this card when it makes the next move clear. Open the heavier records below only when publication, reuse, extraction, coarsening, comparison, evidence, assurance, C.29 lens use, architecture description, or cross-case support is live.


What goes wrong if A.22 is missed: architecture becomes a document, a module diagram, a TGA graph, a mathematical-lens output, or a decision record; a support source becomes the structure; a view becomes the described object; a coarsened or extracted representation becomes loss-free. Those collapses damage first-principles reasoning because the practitioner cannot see what is organized, what carries the claim, what support exists, and where the use stops.

What A.22 buys in practice: a practitioner can name selected structure, cite support, publish a structural view, state preserved and lost structure, return to source when the loss matters, or exit to the neighboring FPF pattern that carries evidence, assurance, gate, decision, work, release, architecture-description, or mathematical-lens claim kind.

Not this pattern when the live question is architecture-description adequacy. Use `C.30`. If the live question is an architecture structural view, use `C.30.ASV`. If it is mathematical-lens adequacy, use `C.29`. If it is evidence, assurance, gate, decision, work, release, or project authority, use the exact neighboring FPF pattern and keep A.22 only to the structure carrier or structure-view portion.

### A.22:2 - Problem

FPF needs a carrier for structure that is useful before any one domain ontology, mathematical formalism, architecture notation, or publication form takes over. Working projects often notice that "the structure" is doing real work:

- dependencies repeat across cases;
- a method or work description hides an invariant relation;
- a model compresses a trace by preserving one relation class and losing others;
- a diagram shows an arrangement but is mistaken for the arrangement itself;
- a mathematical lens exposes preserved structure but is then overread as ontology;
- an architecture discussion needs selected structure over a holon before it can describe architecture.

How can FPF let a practitioner name structure as an intensional object while preserving the distinction between:

- selected structure and the support from which it was inferred or declared;
- structure and a D/S description or view of that structure;
- structure and a publication face, diagram, table, graph, or carrier;
- structure and mathematical-lens support;
- structure and evidence, assurance, gate, decision, work, or release;
- structure in general and architecture-specific structure selected by `C.30`.

### A.22:3 - Forces

| Force | Tension |
| --- | --- |
| First-principles carrier vs ontology inflation | FPF needs a reusable carrier for relations, constraints, invariants, variation classes, and preserved/lost organization, but adding one carrier can accidentally invite many false root kinds. |
| Useful compression vs source return | Structure makes work easier by compressing cases, but source return opens when compression, extraction, coarsening, or support reuse hides a distinction needed for action. |
| D/S usability vs object confusion | Descriptions and views make structure inspectable, but a useful view can be mistaken for the structure itself. |
| Mathematical support vs mathematical overread | C.29 lenses can expose structure, but lens output does not become the structure and does not license evidence, causal, assurance, or decision claims by itself. |
| Architecture dependency vs architecture takeover | Architecture uses selected structure through `C.30`; A.22 does not import architecture as its parent or make every structure an architecture. |
| Plain engineering speech vs Tech recovery | Words such as structure, graph, architecture, module, function, interface, pattern, block, layer, and stack can remain in Plain prose, but load-bearing use needs recoverable Tech fields and neighboring-pattern exits. |

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

### A.22:5 - Archetypal Grounding

| Tell-Show-Show row | Grounding |
| --- | --- |
| Tell | A practitioner sees an arrangement that matters but does not yet know whether it is a diagram, a model, a graph, an architecture claim, a support source, or a decision. A.22 asks first: what organization is being selected, over what support, under what context, and with what loss? |
| Show: `U.System` | In a plant, vehicle, software system, or neural-network model, the selected structure may be flow/transduction, control, module/interface, placement, information, scale, or declared logical structure. The structure record does not become the system and does not prove that the system is safe, maintainable, or ready. |
| Show: `U.Episteme` | A paper, model, generated relation graph, dashboard, architecture note, or mathematical-lens output can describe or support selected structure. The episteme, view, or publication is not the structure itself; it carries a description, view, or support relation with validation and source-return boundaries. |

### A.22:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto/Epist**, **Prag**, **Did**, **Gov**. Scope: universal within FPF structure claims.

| Bias risk | Mitigation |
| --- | --- |
| Architecture bias | Do not make architecture the parent of all structure. A.22 stays upstream; C.30 carries architecture-description adequacy. |
| Mathematical-formalism bias | A mathematical lens can expose preserved/lost structure, but C.29 remains the governing pattern for lens adequacy and stop condition. |
| Diagram bias | A useful diagram or generated relation graph is attractive enough to be mistaken for the structure. D/S and publication boundaries stay explicit. |
| Review-only bias | Checks leave a repair move: name the structure, cite support, open a structural view, return to source, or exit to a neighboring pattern. |
| Didactic-thinning risk | Semantic repair does not leave inert prose. The recognition text keeps the first useful move and the practical payoff visible before the formal records. |

This checklist verifies the preceding guidance after the practitioner has chosen the live move; it is not a required project control form and not a substitute for the card, note, view, relation, or repair move above.

### A.22:7 - Conformance Checklist


| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-A22-1 Structure carrier.** | A load-bearing structure claim names `candidate:U.Structure` or an existing exact neighboring FPF carrier; it does not mint an unapproved root kind. | Replace the broad noun with `candidate:U.Structure` or assign the claim to the exact neighboring carrier. |
| **CC-A22-2 Non-agentive structure.** | Structure wording does not make the structure act, optimize, prove, decide, warrant, sense, plan, or adapt. | Move agency, proof, decision, or work load to the governing pattern and keep A.22 to selected organization. |
| **CC-A22-3 Support boundary.** | When source, evidence, lens, simulation, extraction, or representation support is live, `StructureClaimSupport@Context` or an exact neighboring support record is named. | Add support posture, validation boundary, admissible use, and non-admissible use, or mark the support claim unsupported. |
| **CC-A22-4 D/S separation.** | A structural description, structural view, extracted view, diagram, table, graph, dashboard, or publication face is not treated as the structure itself. | Downgrade the artifact to description, view, support, carrier, or publication and name the selected structure separately only if it is live. |
| **CC-A22-5 DescriptionContext reuse.** | D/S records reuse `DescriptionContext`, `U.Episteme`, `U.View`, `A.6.3`, and `E.17` machinery; no second architecture-local description/view ontology is introduced. | Replace local description/view fields with the imported D/S fields or assign the claim to the exact existing pattern. |
| **CC-A22-6 Source return.** | `SourceReturnCondition` is present when hidden source-side distinctions are used for action, assurance, causal use, legal or regulatory review, comparison, or decision reopening. | Add one source-return condition or narrow the record's admissible use so the hidden distinction is not relied on. |
| **CC-A22-7 Neighboring claim kind.** | Evidence, assurance, gate, release, causal, dynamics, measurement, work, decision, publication, bridge, and mathematical-lens claims are assigned to their governing patterns. | Name the neighboring FPF locus and the live claim kind; do not add fields to A.22 to absorb it. |
| **CC-A22-8 Architecture exit.** | Architecture claims use `C.30` and `ArchitectureOf@Context`; A.22 does not treat architecture as a root kind or define C.30-specific records. | Open C.30 or a C.30 subpattern and keep A.22 only as the selected-structure support. |
| **CC-A22-9 Plain/Tech recovery.** | Plain structure phrases may remain, but if they carry ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility load, the relevant Tech fields and neighboring pattern exits are recoverable. | Add the missing Tech fields or demote the Plain phrase to ordinary recognition wording. |
| **CC-A22-10 Useful action.** | The repair leaves a surviving admissible practitioner move: name the structure, cite support, open a structural view, return to source, or exit to the neighboring pattern that carries the live claim kind. | Restore that move, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

### A.22:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Structure-as-document** | A diagram, table, dashboard, relation graph, or prose section is called the structure. | Recover publication, carrier, description, or view relation; name the structure separately only when selected organization is live. |
| **Support-as-structure** | A source trace, benchmark, lens output, model, or simulation is treated as the structure. | Add `StructureClaimSupport@Context` and state support posture, validation boundary, and non-admissible use. |
| **Loss-free extraction** | Extracted or coarsened structure is used without lost structure or source return. | Add `preservedStructure`, `lostStructure`, `validationBoundary`, and `sourceReturnCondition`. |
| **Architecture root-kind rebound** | Structure work reintroduces `U.Architecture` or treats architecture as parallel to structure. | Use `ArchitectureOf@Context` and C.30; keep A.22 as the upstream structure carrier. |
| **Lens ontology import** | A mathematical lens output becomes the target ontology. | Use C.29 for the lens, cite it as support, and state stop condition. |
| **Sterile precision rewrite** | The text removes overread but no longer tells the practitioner what to do. | Restore the surviving action: structure card, support record, D/S view, source return, or neighboring-pattern exit. |

### A.22:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| FPF gains a reusable carrier for structure without minting architecture, module, interface, platform, or graph as root kinds. | A conforming use states context, support, preserved/lost structure, and non-admissible use when the claim is load-bearing. |
| Structural views become usable without confusing the view, carrier, publication, support source, and described object. | Existing loose prose that says "the structure is the diagram" needs repair. |
| C.29 mathematical lenses and E.18 TGA graphs can support structure claims without becoming structure ontology. | Neighboring-pattern exits are named when evidence, assurance, causality, gate, work, or decision claims are live. |
| Architecture work can start from selected structure through C.30 instead of forcing architecture to be either a document or a module diagram. | Architecture-specific conformance stays outside A.22, so practitioners may need one extra C.30 application when the architecture-description claim kind is live. |

### A.22:10 - Rationale

FPF needs one general structure carrier because many useful project claims depend on organization before they depend on a specific architecture, mathematical, measurement, or publication pattern. The carrier has to be intensional, dependent, and non-agentive: it can be described, supported, compared, coarsened, extracted, or used by architecture, but it does not act or certify.

The selected design keeps A.22 small enough for first use. A practitioner can write one `StructureQuestionCard@Project` and stop. Heavier D/S, support, extraction, and source-return records open only when the next use would otherwise hide loss, source dependence, or neighboring-pattern claim kind.

The reason to keep C.30 separate is architectural clarity. Architecture is selected structure for a described holon under context and concern; architecture descriptions are D/S publications over that claim. A.22 supplies the structure substrate, not the architecture ontology.

### A.22:11 - SoTA-Echoing

| Practice or source line | FPF adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010:2022 architecture-description practice | Adopt the separation of entity of interest, concern, viewpoint, view, and correspondence as pressure for D/S separation. | A.22 structural descriptions and views reuse `DescriptionContext`, viewpoint, view, and correspondence machinery rather than inventing a local display ontology. | ISO 42010 does not make every structure an architecture and does not add evidence, assurance, gate, or decision authority. |
| OMG SysML v2 view practice | Adapt views-as-queries and model-view discipline as support for treating views as selected renderings over model content. | A structural view states selected, hidden, or lost structure when the selection changes action. | A view is not the structure and not a proof of the described system. |
| C.29 mathematical-lens discipline | Adopt preserved/lost structure, support posture, and stop-condition discipline when a mathematical lens supports a structure claim. | Cite C.29 output as support and keep source return visible. | Lens output is not structure, evidence, assurance, causal support, or decision. |
| arXiv:2603.00601 code-space architecture relation-graph work and related code-probing practice | Adapt partial-observability, typed-relation, uncertainty, and source-return pressure for extracted structural views. | Use extracted structural-view records with validation boundaries, observed/inferred/unknown status where needed, and source-return conditions. | Do not mint `U.CodeSpace` and do not treat probe output, probe JSON, or benchmark output as structure adequacy, assurance, or release support. |
| Coarsening, compression, and RG-adjacent traditions | Adopt the need to say what structure is preserved and what is lost. | Use `StructuralCoarseningDescription@Context` and `SourceReturnCondition` before relying on a coarsened structure for action. | RG, epiplexity, structural information, and equivalence support belong to C.29, C.16, or another admitted receiving pattern named for the live claim. |
| GonzoML neural-network architecture discussions as practitioner-language intake | Adapt block replacement, dataflow change, memory/cache placement, path-selection, pruning, distillation, and architecture-search wording as general architecture-operation recognition material. | When such wording is used, recover changed structure kind, support source, preserved and lost structure, and neighboring exits. | Neural-network labels, benchmark results, ablations, or pruning masks do not become architecture decisions, evidence sufficiency, gate passage, assurance, or architecture adequacy by themselves. |

### A.22:12 - Relations

Builds on: `C.2.1`, `A.6.P`, `A.7`, `A.6.2`, `A.6.3`, `A.14`, `C.16`, `C.29`, `E.10.D2`, `E.10`, `E.10.SEMIO`, `E.17.0`, `E.17.1`, and `F.18`.

Coordinates with: `C.30`, `C.30.ASV`, `C.30.TGA-FLOW-REL`, `C.30.LCA`, `C.30.ILC`, `A.6.F`, `E.18`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `C.28`, `A.15`, `C.11`, `C.16`, `C.25`, `G.5`, and named receiving patterns for structure-information, equivalence, and synthesis claims when those claim kinds are live.

Does not replace: `C.30` for architecture description, `C.29` for mathematical-lens adequacy, `C.16` for measurement and characterization, `C.28` for causal-use support, `B.3` for assurance, `A.10` and `G.6` for evidence, `A.20` and `A.21` for gates and release, `A.15` for work, `C.11` for decisions, or `E.17` for publication.

### A.22:End
