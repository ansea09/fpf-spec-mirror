---
chunk_kind: "child"
pattern_id: "A.22"
pattern_title: "Structure and Structural Views (STRUCT-CAL)"
section_id: "A.22:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22/A.22__005_solution.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "A.22 — Structure and Structural Views (STRUCT-CAL)"
  - "A.22:4 — Solution"
line_start: 33704
line_end: 34005
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.22.CGUS"
  - "A.3.1"
  - "A.6.0"
  - "A.6.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.5"
  - "A.6.F"
  - "A.6.P"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
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
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.18.3"
  - "E.18.NET"
  - "E.24"
  - "E.24.PUB"
  - "F.18"
  - "G.5"
  - "G.6"
keywords:
---

### A.22:4 - Solution

Select `U.Structure` as the A.22 ontic head: a dependent, non-agentive organization selected from independently identified constituents and exact obtaining relation occurrences under applied constraints for one named use frame.

The constituents keep their own identities and kinds. Every selected relation occurrence must already satisfy its defining predicate and retain identity under that predicate's occurrence rule. A.22 neither creates those participants nor makes their relations obtain. A system or practitioner selects their organization; A.22 supplies the identity and boundary rule for that selected organization.

The applied constraints are the exact constraint claims used in the selection judgment, not the identity of the document, table, rule card, or constraint episteme that carries them. The named use frame states the question being answered, the admissible action, and the non-admissible overread. A generic phrase such as “current use” or “appropriate structure” is not a use frame.

A system may perform dated structure-selection work by an exact method and may create a result episteme about the selected structure. The system acts; the pattern, constraints, graph, result, and structure do not. The method, work, A.6.1 binding or direct participation relation, decision, and C.2.1 result episteme are neighboring objects. None constitutes or reidentifies the structure.

A diagram, graph, table, model, description, view, or publication may designate, represent, or describe the selected organization and its already identified constituents. Its form does not establish a constituent's identity, make a relation obtain, or select a structure. Use C.29, C.2.1, E.17.0, and the exact publication or source-use patterns for those neighboring claims.

#### A.22:4.1 - Base `U.Structure` Identity and Selection

For a selected structure `S`, recover four identity discriminators:

```text
StructureIdentity(S) = <
  exact independently identified constituents,
  exact selected obtaining relation occurrences,
  exact constraints as applied,
  one named selection-use frame
>
```

Base `U.Structure` identity has no ambient context field. A bounded-context label, `U.ContextSlice`, `U.ClaimScope`, project record, description, view, graph, table, or publication is not automatically an additional discriminator. If an exact scope is referenced by an applied constraint, that constraint contributes through the third discriminator. If a model-use structure is independently selected as a constituent of another structure, it contributes through the first discriminator.

The first discriminator is an exact plurality, not a graph node set created by notation. A separately useful C.13 collection may designate the same constituents, but collection membership neither proves parthood nor replaces their direct identities. The second discriminator contains the exact relation occurrences chosen for this organization; a relation name, edge label, tuple position, or adjacency row is insufficient. The third contains the semantic constraints actually applied; changing only the rationale, formatting, or publication of an unchanged constraint claim does not change this discriminator. The fourth names the use question and its admissible action or stop.

Two references resolve to the same `U.Structure` when all four discriminators resolve to the same values. A changed designator, selecting system, method, work occurrence, result episteme, description, graph, representation scheme, view, or publication leaves the structure unchanged when the four discriminators remain unchanged. Replacing a constituent, a selected relation occurrence, an applied constraint, or the named use frame can identify another structure. If a relation occurrence itself may have been reidentified, apply its direct relation pattern before reapplying A.22.

If no current predicate definition, applicability condition, or occurrence rule can identify the required constituent or test the obtaining-relation claim for this use, stop at the exact description or representation and return `missing-governor`. If the governor exists and the available case basis is sufficient to apply its positive test but that test fails, return `factually unsupported`; if a fact needed to decide the test is unavailable, return `missing-information`. State a negative only when an applicable non-obtaining criterion or complete closure basis and satisfying facts establish it. If the constraints or named use frame are absent, name that exact gap: the material may show an arrangement, but it does not yet support the claimed selected `U.Structure`.

The following two compact records are recovery aids, not new ontic kinds. In `SelectedStructureBasis`, the selected structure, constituents, selected obtaining relations, applied constraints, and use frame state identity; the preserved/lost and action/stop rows state the use-return boundary rather than adding identity fields.

```text
SelectedStructureBasis:
  selectedStructureRef:
  constituentRefs:
  selectedObtainingRelationOccurrenceRefs:
  appliedConstraintClaimRefs:
  namedSelectionUseFrame:
  preservedStructure:
  lostHiddenOrExcludedStructure:
  admissibleAction:
  stopOrNonAdmissibleUse:

StructureSelectionUse:
  selectingSystemRef:
  selectionMethodRef:
  selectionWorkRef:
  directParticipationOrOperationBindingRefs:
  selectedStructureRef:
  selectionResultEpistemeRef?, when the judgment must persist:
  selectionDecisionRef?, when an accountable choice is current:
```

`StructureSelectionUse` records how a system performed the selection and reached the judgment. `SelectedStructureBasis` records the four identity discriminators plus the use-return boundary. Do not copy the system, work, method, result episteme, or decision into the structure basis. A `U.ClaimScope`, effective `U.ReferenceScheme`, or model-use structure that merely qualifies a claim about either record does not enter base identity. A scope referenced by an applied constraint or a model-use structure selected as a constituent enters only through that already declared discriminator.

A.22 structure-aspect names such as functional, mereological, modular, transformation-flow, control, semantic, causal, dynamical, algebraic, topological, geometric, or coarse-grained remain cues for which relations and constraints to recover. They do not identify a structure without the four discriminators. C.30.ASV `ArchitectureStructureKindRef` values remain architecture-local classifiers; a matching label does not imply identity.

#### A.22:4.1a - Compact auxiliary boundary

Use description, publication, source-use, evidence, work, gate, decision, release, architecture-description, and mathematical-lens patterns when those claims are being made. The A.22 application contains the selected-structure portion and the structure-use return condition that protects that structure use; use each neighboring pattern only for the definition or test it contributes. A publication, diagram, graph, table, dashboard, file, model card, generated representation, or lens output may make a structural description or view available; it does not become the selected structure or supply neighboring claim authority by appearance.

#### A.22:4.1b - Constraint-governed unfolding structure

Use `A.22.CGUS` when the current A.22 structure has several locally declared loci whose bindings identify the independently selected constituents for the unfolding question, and when the selected obtaining relation occurrences together with the applied constraint claims define at least two potential continuations across allowed cases. The loci are not free-standing A.6.5 slots. A separate case- and time-indexed result may enable zero, one, or several candidates. This specialization remains `U.Structure`; it is not a route, workflow, method, work plan, performed work, decision, evidence relation, gate, architecture description, or publication.

Use `A.22.CGUS` only when the candidate has several loci and cross-locus constraints. A route card, table, graph, README entry, narrative, slide, or happy-path example may describe or demonstrate the unfolding structure, but it is not the structure itself.

#### A.22:4.1c - Bounded And Cross-Context Model-Use Structure Specializations

`BoundedModelUseStructure` is a `U.Structure` selected over one exact model episteme, exact admitted model-use holons, the obtaining model-applicability, actual model-use, and model-expression-coherence occurrences defined and tested by A.1.1, exact applied constraint claims used by the selection judgment, and one named bounded-model-use frame. Its A.22 identity uses exactly those constituents, selected occurrences, exact constraint claims, and frame. A claim scope, membership outcome, boundary display, or carrier is not an applied constraint by itself; a constraint claim may instead state a proposition about that scope or its A.2.6 membership predicate. No boundary crossing participates in that identity. Continuity across model editions additionally requires the exact C.2.1 episteme-edition relation and declared A.1.1 continuity rule. It is not a holon, description, view, or endpoint manufactured by a later crossing.

`CrossContextRelationStructure` is a conditional specialization of a different already identified `U.Structure`. Membership requires exact obtaining crossing occurrences that satisfy independently defined predicates, selected among several bounded model-use structures, applied constraints, and one named crossing-analysis use, with all four A.22 base discriminators established. Until a compatible crossing predicate and current facts establish those occurrences, a Context Map can describe only a proposed crossing organization and no positive `CrossContextRelationStructure` member is asserted. The selecting system and its work remain separate. Sharing a participant does not merge structures, and overlap does not prove parthood.

**Pending local name settlement.** The following F.18 NameCard is local to A.22 while the positive crossing-occurrence basis is unavailable. It does not create the structures, crossing relations, mapping method, or view.

```text
NameCard:
  NameCardId: NC-CROSS-CONTEXT-RELATION-STRUCTURE
  GovernedValueRef: U.Structure selected over several BoundedModelUseStructure values and their exact crossing relations
  SubjectPatternLocator: A.22
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseRef: conditional selected organization of independently defined obtaining crossings among several bounded model-use structures under all four A.22 base discriminators; a Context Map may describe only a proposed organization until that exact positive basis exists
  TechLabel: CrossContextRelationStructure
  PlainLabel: relations among bounded contexts
  CandidateSet: CrossContextRelationStructure; BoundedContextRelationStructure; ContextRelationStructure; ContextMapStructure
  RejectedCandidates: BoundedContextRelationStructure hides plurality; ContextRelationStructure leaves the endpoint kind unresolved; ContextMapStructure confuses the structure with the DDD view and FPF Map
  SelectionRationale: reserve one local retrieval label for the conditional cross-structure rule without retyping its proposed description, view, diagram, or publication as an admitted structure
  PublicRowStatus: pending
  LineageEntries: replaces broad context-map and bounded-context-relation wording
  RefreshCondition: reopen when an independently defined crossing relation obtains and one positive A.22 membership witness is available; only then rerun F.18/F.17 for public reuse
```

This pending card has no `UnifiedTermRowRef`. Until its refresh condition is met, `CrossContextRelationStructure` is an A.22-local provisional designator only; other Core hosts must cite the descriptive A.22 conditional cross-structure rule rather than consume that label as public vocabulary.

DDD `Context Mapping` names a repeatable `U.Method`. A.15.2 defines the intended mapping plan; A.15.1 identifies each exact dated mapping Work individual admitted under `U.Work`, the performer system and obtaining system-role assignment, and the exact `enactsMethod` relation. C.2.1 independently identifies the candidate episteme called a `Context Map`. While exact independently defined crossing occurrences or the four A.22 base discriminators are missing, its EntityOfConcern is the proposed or described crossing organization, not an exact `CrossContextRelationStructure`. Only after both conditions are met may a corresponding C.2.1 episteme designate the exact structure. Either episteme is additionally a `U.View` only when the E.17.0 test establishes `EpistemeViewpointConformanceRelation(E, P)`. Use C.29 for any representation relation and E.17/E.24.PUB for rendering or publication; form and carrier remain separate. Thus method, plan, work, proposal, selected structure, candidate episteme, dependent view membership, representation, and publication stay distinct while the external source terms remain retrievable.

#### A.22:4.1d - Transformation-flow structure network profile

Use `E.18.NET` when one engineering use selects two or more independently identified transformation-flow structures, or nested networks of them, together with exact obtaining relations across their boundaries. Apply the four A.22 discriminators directly: the exact TFS or nested-network members are the constituents; the exact cross-member relation occurrences satisfy their defining predicates and identity rules; the exact applied endpoint, boundary-exposure, and acyclic direct-member constraints are selected under E.18.NET; and the named network-use frame states the practical question or action and the forbidden overread. Record the return condition separately; it reopens selection when a member, relation, constraint, or use-frame value changes and is not a fifth identity discriminator. The result is one dependent, non-agentive `U.Structure` specialization. E.18.NET defines the network's detailed identity, reference, recursion, local-state, and conformance rules; A.22 does not copy those fields.

Selecting a constituent in the first discriminator does not create a separately re-identifiable membership occurrence. A member row, graph edge, containment picture, or shared label proves neither membership nor another relation. If a receiving use genuinely needs a world-side membership relation, recover its participants, obtaining predicate, and identity rule; otherwise use the exact constituent discriminator and do not mint a generic membership edge.

#### A.22:4.2 - Structure claim reliance relation selection


A.22 does not mint a local generic reliance record. When a structure claim relies on something beyond the selected structure itself, choose the reliance relation kind, name the relation record by value, and name the definition or test used for that relation:

| Current reliance relation kind | What is named | Definition or test to apply |
| --- | --- | --- |
| Source-description relation | source episteme, source view, publication form or rendering where relevant, described structure or structure claim, source-basis pins or structure-use return condition, admissible and non-admissible use | `A.7`, `A.6.3`, `E.17`, `E.17.0`, and local source-publication rules |
| Base-dependence or basedness | `dependent = structure claim or structural description`, `base`, declared `baseRelation`, scope, declared `Γ_time` when temporal scope is claimed, witness refs when witness use is claimed, admissible and non-admissible use | `A.6.6` SWBD, or an admitted subject-specific base relation whose definition supplies the stated participants, applicability, and identity rule |
| EntityOfConcern or empirical grounding | exact claim-bearing episteme, its EntityOfConcern, and effective ReferenceScheme; when empirical grounding is claimed, the exact grounding holon, covered claim subgraph, and obtaining C.2.1 `EpistemeEmpiricalGroundingRelation`; claim scope, optional model-use structure, describing-use viewpoint, reference plane, and observation or witness condition only when current | `C.2.1`, `A.2.6`, `A.1.1`, `E.17.0`, `A.6.4`, `A.6.3.RT`, and `A.6.6` only for a separate base-dependence claim |
| Evidence or witness reliance | evidence-use relation, evidence-provenance relation, claim ref, witness publication or observation record, timespan and freshness; if an evidence graph is current, its graph path remains a mathematical or provenance expression rather than an action route | `A.10`, `A.2.4`, `G.6` |
| Mathematical-lens reliance | lens candidate, lens card, or lens-use record; primary `EntityOfConcern`; relation record or claim record named by value when lens reliance is being claimed; preserved structure; lost structure; stop condition; `MathLensUseOutputRef`; C.29 lens-use result; or `LensUseAdmissibilityValue` | `C.29`, `C.26`, `F.9`, named mathematical-lens pattern |
| Simulation, generated representation, model, or extracted trace | exact source episteme and publication when source availability matters, representation or extraction method, validation boundary, preserved structure, lost structure, and structure-use return condition | `C.29` for representation or extraction correspondence; `E.10.D2` and `E.17.0` for description and view claims; `E.17` and `E.24.PUB` for publication; `C.2.1` only for exact episteme identity or an explicitly claimed empirical-grounding relation; `A.10` for evidence; or the pattern that defines or tests the exact simulation, extraction, or validation claim |

If no reliance relation kind can be selected, keep the wording as a source-finding note, recognition cue, ordinary help, quote-only wording, or reduced-use cue. Do not create a generic reliance record to make the claim look resolved.

`U.Structure` does not carry description, representation, extraction, mathematical-lens, simulation, or generic reliance state as an internal structure field. Those are source-description, source-use, base-dependence, evidence, lens, extraction, simulation, or publication relations about a structure. `PublicationRef` is not an admissible substitute for the source episteme, source view, evidence relation, SWBD, or lens output.

#### A.22:4.3 - Structural descriptions and views

Structural descriptions and views reuse existing episteme and view machinery. Architecture does not define a second ontology of descriptions, views, viewpoint bundles, multi-view descriptions, publications, publication forms, or source-pin sets. Every record whose name ends in `Description@Context` here designates an existing `U.Episteme`: C.2.1 supplies its identity and E.10.D2 constrains its describing use. Every record whose name ends in `View@Context` remains that same episteme and has `U.View` membership only when the E.17.0 conformance test to an exact viewpoint episteme passes. A.6.3 supplies only an optional source-to-receiving construction. The `@Context` suffix is a local retrieval convention; it does not add a context object or identity field.

```text
StructuralDescription@Context ::= {
  descriptionId,
  entityOfConcernRef,
  effectiveReferenceScheme,
  selectedViewpointRef?,
  selectedModelUseStructureRef?,
  structureRefs: FinSet(U.StructureRef),
  structureClaimRelianceRefs?: FinSet(U.ScopedWitnessedBaseDeclarationRef | EvidenceRelationRef | EvidenceProvenanceRelationRef | MathLensUseOutputRef | StructureUseReturnConditionRef | U.EpistemeRef),
  describingEpistemeRef,
  admissibleUse,
  nonAdmissibleUse
}

StructuralView@Context ::= {
  viewId,
  entityOfConcernRef,
  effectiveReferenceScheme,
  selectedViewpointRef?,
  selectedModelUseStructureRef?,
  structureRefs: FinSet(U.StructureRef),
  structuralAspectDescriptionRefs?,
  selectedRelationsOrOperations,
  hiddenOrLostStructure,
  admissibleUse,
  nonAdmissibleUse
}
```

The exact EntityOfConcern and effective scheme identify the episteme with its claim content under C.2.1. `selectedViewpointRef`, when present, records that this named describing use selects exact viewpoint P; it does not establish conformance or `U.View` membership. `selectedModelUseStructureRef`, when present, resolves one independently selected `BoundedModelUseStructure` used by the receiving assertion or calculation; it is neither episteme identity nor another viewpoint field. When reliance is on a named claim, `U.EpistemeRef` resolves the exact C.2.1 claim-bearing episteme; a PatternID normally locates the definition, constraint, or test it uses, and an exact ClaimGraph is added only when that identity changes the use.

#### A.22:4.4 - Extracted and transformed structural views

Use extracted or transformed structure records when a corpus, trace, model, lens, simulation, generated representation, coarsening pass, observer boundary, or budget boundary produces a view of structure that may hide distinctions.

```text
ExtractedStructuralView@Context ::= {
  extractedViewId,
  entityOfConcernRef,
  effectiveReferenceScheme,
  selectedViewpointRef?,
  selectedModelUseStructureRef?,
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
  entityOfConcernRef,
  effectiveReferenceScheme,
  selectedViewpointRef?,
  selectedModelUseStructureRef?,
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
  entityOfConcernRef,
  effectiveReferenceScheme,
  selectedViewpointRef?,
  selectedModelUseStructureRef?,
  aspectKindRef,
  structureRefs: FinSet(U.StructureRef),
  structureClaimRelianceRefs?: FinSet(U.ScopedWitnessedBaseDeclarationRef | EvidenceRelationRef | EvidenceProvenanceRelationRef | MathLensUseOutputRef | StructureUseReturnConditionRef | U.EpistemeRef),
  admissibleUse,
  nonAdmissibleUse
}

StructuralCoarseningDescription@Context ::= {
  coarseningDescriptionId,
  entityOfConcernRef,
  effectiveReferenceScheme,
  selectedViewpointRef?,
  selectedModelUseStructureRef?,
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

`C.30` uses A.22 by selecting architecture-relevant structures for one described holon through `ArchitectureOf@Context`. `C.30.ASV` then defines and tests architecture structural views over those selected structures. A structure can be used by architecture, but a structure is not an architecture merely because an architecture description refers to it.

Architecture-related records that belong to C.30 or its subpatterns include `ArchitectureOf@Context`, `ArchitectureDescription@Context`, `ArchitectureStructuralView@Context`, `ArchitectureStructureKindRef`, `ArchitectureStructureKindTriage@Project`, `FunctionalStructureView@Context`, `ArchitectureTransformationFlowStructureRelation@Context`, `ControlStructureView@Context`, and `CrossScopeArchitectureResidualTriage@Context`. A.22 may name them as FPF pattern applications. It does not define their architecture-specific conformance.

#### A.22:4.7 - Boundary and repair table

| Tempting collapse | A.22 repair |
| --- | --- |
| The reliance relation is treated as the structure. | Recover the exact constituents, selected obtaining relation occurrences, applied constraints, and named use frame. When a neighboring source-description, source-use, base-dependence, grounding, evidence, lens, simulation, extraction, or representation reliance claim is current, name that exact relation and the content that defines or tests it separately. |
| The diagram, graph, table, dashboard, or publication form is the structure. | Treat it as publication, description, view, publication form, source-description relation, base-dependence relation, grounding relation, evidence relation, lens relation, simulation relation, extraction relation, or representation relation only when its relation is explicit. |
| A transformation-flow graph expression is the structure in every sense. | Use `E.18` for one selected TFS and its internal paths, crossings, and valuations; use `E.18.NET` for a selected network of independently identified TFS members and exact cross-member relations; use `E.18.2` and `C.29` for the graph expression. A.22 supplies only the selected-structure identity, and `C.30.TFS-REL` defines and tests the architecture-to-transformation-flow relation claim. |
| A mathematical lens output is the structure. | Use `C.29` for lens-use result and admissibility, and cite `MathLensUseOutputRef` only through C.29 lens-use result, preserved structure, lost structure, and stop-condition discipline. |
| A structure proves evidence, assurance, safety, causality, or gate passage. | Assign those claims to `A.10`, `G.6`, `B.3`, `C.28`, `A.20`, or `A.21`. |
| A structure is a decision or work record. | Use `C.11`, `A.20`, `A.21`, `A.15`, or the project-side decision pattern whose test answers the claim being made. |
| Architecture is a root kind beside structure. | Use `C.30`: architecture is selected structure for a described holon through `ArchitectureOf@Context`. |
| Function, module, interface, platform, layer, stack, block, expert, cache, router, or gate becomes a root kind by appearing in structure prose. | Use `C.30.STRAT` for source-label recovery, then `A.6.F`, `A.6.M` module-relation repair when a module-interface claim is being made, `A.6.0`, `A.6.5`, `A.6.B`, `A.6.C`, `A.6.P:4.11a`, `E.18`, `C.30.ASV`, and any other definition or test required by the recovered claim. |

#### A.22:4.8 - Worked slices

**Maintenance-isolation structure selection.** A planner needs to choose which relations matter when isolating a pump skid for maintenance.

```text
named selection use: choose isolation points before Pump_37 maintenance
constituents: independently identified Pump_37, Motor_12, Valve_In_4, Valve_Out_4, and Bus_7
selected obtaining relations: exact installed-with, connected-to, supplied-by, and upstream-of occurrences that currently satisfy their defining predicates
applied constraints: isolate every live energy and material path to Pump_37; retain only relations relevant to this isolation use
selecting system: MaintenancePlanner_A
method and work: IsolationStructureSelectionMethod enacted in SelectionWork_2026-07-25
selected structure: Pump37_MaintenanceIsolationStructure
admissible action: prepare the isolation sequence from the selected paths
stop: reopen selection when a constituent, selected occurrence, or isolation constraint changes
```

`Pump37_MaintenanceIsolationStructure` is identified by the exact constituents, exact selected obtaining occurrences, applied isolation constraints, and maintenance-isolation use frame. `SelectionWork_2026-07-25`, the enacted method, and any C.2.1 episteme that records the judgment remain separate. A graph can represent the same organization under C.29; an edge in that graph neither makes its relation obtain nor replaces the exact relation occurrence. A near miss is a visually identical graph assembled from labels when one connection has not been established: it is a representation candidate, not the selected structure claimed above.

**Architecture kernel slice.** A team says, "the architecture is the graph." A.22 does not accept that sentence as a root-kind claim. The repair is:

```text
declaredStructureSubstrateRef: TransformationFlowStructureRef under E.18, with mathematical graph description under E.18.2 when that expression is the current claim
candidate structure: selected transformation-flow structure
structure-claim reliance relation: selected relation record named by value(
  sourceDescriptionOrPatternApplicationRef = SourceViewRef, structure or crossing record selected under E.18, or E.18.2 mathematical graph description,
  relationContribution = E.18 selected-structure or crossing definition | A.6.6 base-dependence test | A.10 evidence, source-provenance, or reliance test | C.29 mathematical-lens result, chosen for the claim being made,
  relationKind = source-description | base-dependence | evidence | lens, selected for this reliance,
  validationBoundary = graph-path currentness boundary, slice currentness boundary, or crossing currentness boundary
)
next FPF pattern application: C.30.TFS-REL when this selected structure is used in an architecture-to-transformation-flow relation
non-admissible use: graph as whole architecture, work, evidence, gate, or decision
```

The useful structure use survives: the practitioner can use the graph through the selected source-description, base-dependence, evidence, or lens relation without turning it into architecture ontology.

**Extracted code structure slice.** A code-agent relation graph or probe JSON reports imports, calls, registry wiring, and data-flow links. A.22 treats it as an extracted structural view only when the source codebase or publication, extraction method, preserved structure, lost structure, validation boundary, and structure-use return condition are named. The relation graph or probe output is not the codebase architecture itself and is not proof of internal agent belief, assurance, or release readiness.

```text
ExtractedStructuralView@Context:
  sourceCorpusOrTraceRefs: repo snapshot, probe outputs, traces
  preservedStructure: selected typed relation families
  lostStructure: unexplored regions, dynamic calls, hidden generated code, ambiguous relation kinds
  validationBoundary: probe coverage and source codebase or publication edition
  structureUseReturnCondition: when an architecture decision, assurance use, or repair depends on a relation not observed by the extraction
```

