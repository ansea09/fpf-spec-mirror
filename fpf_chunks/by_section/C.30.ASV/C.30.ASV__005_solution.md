---
chunk_kind: "child"
pattern_id: "C.30.ASV"
pattern_title: "Architecture Structural View Adequacy (ASV)"
section_id: "C.30.ASV:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ASV/C.30.ASV__005_solution.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "C.30.ASV — Architecture Structural View Adequacy (ASV)"
  - "C.30.ASV:4 — Solution"
line_start: 52732
line_end: 53239
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
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureStructureKindRef"
  - "VF.ARCH.STRUCTURE"
  - "architecture structural view"
  - "correspondence"
  - "hidden/lost structure"
  - "source return"
  - "structure kind"
  - "viewpoint bundle"
---

### C.30.ASV:4 - Solution

Govern architecture structural views by first naming the selected architecture-relevant structure, structure kind, view construction, correspondence, hidden or lost structure, source or reliance relation, source-return condition, admissible use, and next architecture move. Use `ArchitectureStructuralView@Context` as the record form when that view must be durable, reusable, comparable, or reliance-bearing.

A conforming `ArchitectureStructuralView@Context` record is a Description or view over selected `U.Structure` references in one `ArchitectureOf@Context` claim record, under one declared `ArchitectureStructureKindRef` and one `DescriptionContext.ViewpointRef`. The description and view machinery makes the selected-structure move inspectable; it does not replace that move.

C.30.ASV is the selected-structure-kind-to-view relation pattern for architecture work. It explains how different selected structure kinds become views under declared viewpoints and concerns. It is not a complete architecture-description pattern; a durable `ArchitectureDescription@Context` composes one or more structural-view records through C.30 and E.17.0 only when description use is live.

C.30.ASV does not extend the TEVB core viewpoint set by implication. It defines architecture structure kinds and architecture-specific structure-kind and view-record bindings. TEVB viewpoints are reused when the structure-kind view uses one of the TEVB core viewpoints; other structure-kind views use `VF.ARCH.STRUCTURE`, a declared local viewpoint bundle, an exact governing FPF pattern, or a source or reliance record.

#### C.30.ASV:4.1 - Architecture structural view record
`StructuralAspectDescription@Context` describes one selected structural aspect under A.22. It is not an `ArchitectureStructureKindRef` by itself. `ArchitectureStructuralView@Context` is a C.30.ASV view over structures selected by `ArchitectureOf@Context` and typed by `ArchitectureStructureKindRef`.

```text
ArchitectureStructuralView@Context ::= {
  viewId,
  architectureClaimRef: ArchitectureOf@ContextRef,
  descriptionContext: DescriptionContext(
    EntityOfConcernRef = selectedStructureEntityOfConcernRef,
    BoundedContextRef = ArchitectureOf@Context.boundedContextRef,
    ViewpointRef = viewpointRef
  ),
  selectedStructureEntityOfConcernRef: U.StructureRef | FinSet(U.StructureRef) (= structureRefs),
  viewpointRef: U.ViewpointRef (= descriptionContext.ViewpointRef),
  structureRefs: FinSet(U.StructureRef),
  structureKindRef: ArchitectureStructureKindRef,
  recordGoverningPatternRef,
  selectedRelationKinds,
  selectedConstraintRefs?,
  selectedInvariantRefs?,
  selectedOperationOrDynamicsDescriptionRefs?,
  viewConstruction:
    directDescription | projection | query | extraction |
    coarsening | correspondenceSlice | sourceReturnSlice,
  structuralAspectDescriptionRef?,
  hiddenOrLostStructure,
  structureKnowledgeState?:
    declared | observed | inferred | generated | simulated |
    extracted | hypothesized | unknownRegionPresent,
  correspondenceModelRefs?,
  sourceOrRelianceRelationRefs?,
  sourceReturnCondition?,
  admissibleUse,
  nonAdmissibleUse
}
```

`DescriptionContext.EntityOfConcernRef` names the selected structure or selected structure set represented by `structureRefs`. `architectureClaimRef` names the enclosing `ArchitectureOf@Context` claim, and the described holon and bounded context are recovered through that claim record.

**EntityOfConcern discipline.** C.30.ASV treats selected structure as the current `EntityOfConcern` for this view use when the view concerns dependent, non-agentive organization rather than one publication artifact. This does not add a parallel EntityOfConcern head: `DescriptionContext.EntityOfConcernRef`, `selectedStructureEntityOfConcernRef`, and `structureRefs` must converge on the same selected structure or structure set, while `architectureClaimRef` remains the enclosing architecture-claim context.
`viewpointRef` is a recovery label for `descriptionContext.ViewpointRef`, not a second independent viewpoint slot. If the implementation stores only `DescriptionContext`, the viewpoint remains recoverable there.

`structureKnowledgeState?` states how the selected structure is known when partial knowledge matters: declared, observed, inferred, generated, simulated, extracted, hypothesized, or with an unknown region present. Unknown or inferred structure may guide inspection or source return; it cannot by itself supply assurance, gate, release, causal proof, or architecture decision.

#### C.30.ASV:4.2 - Architecture structure-kind classifier

`ArchitectureStructureKindRef` is a C.30-local `DiscriminatorToken` enumeration over architecture-relevant `U.Structure` references selected by `ArchitectureOf@Context`. It is not `U.Kind`, `U.Viewpoint`, `U.ViewpointBundle`, `StructuralAspectDescription`, `StructuralView@Context`, or a root `U.*` kind. `ArchitectureStructuralView@Context` uses `structureKindRef` to say which selected structure kind is being viewed.

```text
ArchitectureStructureKindRef ::= one of {
  FunctionalStructure,
  FlowTransductionStructure,
  ControlStructure,
  ModuleInterfaceStructure,
  RuntimeInteractionStructure,
  PlacementDeploymentStructure,
  InformationDataStructure,
  SecurityTrustBoundaryStructure,
  ConstraintRequirementStructure,
  MaterialSpatialStructure,
  DeclaredLogicalStructure,

  WorkMethodStructure,
  RoleEnactorStructure,
  EvidenceAssuranceStructure,
  ScaleEvolutionStructure,
  OtherDeclaredStructureKind
}
```

The first group is the seed classifier set for ordinary architecture structural-view use. `WorkMethodStructure`, `RoleEnactorStructure`, `EvidenceAssuranceStructure`, and `ScaleEvolutionStructure` are neighbor-governed classifier values: ASV may use them to name the selected architecture-relevant structure, but their full semantics stay in the named work and method, role-enactor, evidence and assurance, scale, characterization, or mathematical-lens patterns.
Do not enumerate structure kinds by default. Choose the smallest useful structure-kind set that changes the next architecture move. If no structure kind changes action, keep the phrase as ordinary recognition wording or a source note. This does not weaken kind discipline; it prevents `ArchitectureStructureKindRef` from becoming an audit checklist.

Inside C.30.ASV, `OtherDeclaredStructureKind` is always an architecture-structure-kind classifier value over `U.Structure`; it does not mint a general FPF root kind.

`OtherDeclaredStructureKind` is admissible only when the local text names:

- `declaredStructureKindName`;
- `declaredStructureKindDefinition`;
- allowed relation families;
- common false interpretations;
- exact governing pattern applications;
- `boundedContextRef`.

Each structure kind needs a short definition, allowed relation families, common false interpretations, typical exact governing pattern applications, and example architecture structural view records. This is not a new root-kind set; it is a controlled classifier set over `U.Structure`.

#### C.30.ASV:4.3 - Small triage output

Use `ArchitectureStructureKindTriage@Project` before a full view record when the practitioner only needs to identify the live structure kind and next architecture move.

```text
ArchitectureStructureKindTriage@Project ::= {
  architectureClaimRef?: ArchitectureOf@ContextRef,
  describedHolonRef?: U.HolonRef,
  boundedContextRef?: U.BoundedContextRef,
  liveArchitectureConcernCue,
  suspectedWrongCollapse,
  plainPromptLabel,
  candidateStructureKindRefs: FinSet(ArchitectureStructureKindRef),
  smallestUsefulStructureKindRefs,
  structureKnowledgeState?,
  primaryGoverningPatternApplicationRef,
  temptingWrongPatternRefs?,
  admissibleArchitectureMove:
    inspect | split | relate | downgrade | assignNeighbor | stop |
    otherDeclared,
  candidateGenerationPatternApplication?: yes | no,
  governingPatternApplicationRefs,
  stopCondition
}
```

`primaryGoverningPatternApplicationRef` names the pattern that carries the next live claim kind. `candidateGenerationPatternApplication?` marks that the next admissible move is to leave ASV for candidate generation; it is not ASV work. `temptingWrongPatternRefs?` names tempting wrong first patterns when that repair is needed. None of these fields governs the triage record itself; C.30.ASV governs the triage record family.
When `architectureClaimRef` is absent, `describedHolonRef` and `boundedContextRef` are required for triage. This pre-claim form does not create a new kind and does not publish an `ArchitectureOf@Context` claim by itself; it only lets the practitioner identify the live structure kind before opening a full architecture claim. A full `ArchitectureStructuralView@Context` still requires `architectureClaimRef`; do not promote triage to a full view record until that architecture claim is available.

Practitioner prompt labels are first-entry cues, not `ArchitectureStructureKindRef` values. FPF-governed records use the Tech values below:

```text
Functional -> FunctionalStructure
Flow -> FlowTransductionStructure
Control -> ControlStructure
Module -> ModuleInterfaceStructure
Method and work -> WorkMethodStructure
Role -> RoleEnactorStructure
Evidence -> EvidenceAssuranceStructure
Scale -> ScaleEvolutionStructure
Security -> SecurityTrustBoundaryStructure

```

#### C.30.ASV:4.4 - Architecture viewpoint bundle and binding rows

Architecture structural views use `VF.ARCH.STRUCTURE` without turning structure kinds into viewpoints. The bundle is separate from `VF.TEVB.ENG`: it may import TEVB, but it does not expand the TEVB core engineering viewpoint set.

Declaration source: `VF.ARCH.STRUCTURE` is an `E.17.1` and `F.18` declared viewpoint bundle for architecture structural-view records. Its `VP.Architecture*` ids are viewpoint ids only. They do not add TEVB viewpoints, name structure kinds, define publication faces, or carry decision, evidence, gate, or assurance authority.

#### C.30.ASV:4.4a - Structural-view publication-use boundary

This subsection is the C.30.ASV structural-view publication-use boundary. C.30.ASV governs architecture structural-view adequacy: selected architecture-relevant structure, structure kind, view construction, correspondence, hidden structure and lost structure, source return, and next architecture move. Generic guards that a view, diagram, graph, card, benchmark, probe output, model publication, or architecture note is not evidence sufficiency, safety proof, assurance verdict, gate passage, release permission, work record, or decision authority belong here or in the exact description-publication neighbor. They do not expand the structural-view record and do not replace the architecture move.

```text
VF.TEVB.ENG core stays:
  { VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface }
```

TEVB is the small engineering viewpoint bundle over holons. The architecture problem is broader than TEVB, but the broader coverage is not solved by placing record sets inside a `U.ViewpointBundle`. The `U.ViewpointBundle` carries viewpoints; a separate architecture-local description binds structure kinds, view record sets, construction modes, correspondence obligations, and exact governing pattern applications.

```text
VF.ARCH.STRUCTURE : U.ViewpointBundle {
  viewFamilyId = VF.ARCH.STRUCTURE,
  imports = { VF.TEVB.ENG },
  EntityOfConcernClassSpec = {
    a : ArchitectureOf@Context |
    a.describedHolonRef and a.boundedContextRef are recoverable
  },
  viewpoints = {
    VP.ArchitectureStructure,
    VP.ArchitectureCorrespondence,
    VP.ArchitectureSourceReturn,
    VP.ArchitectureDecisionAffectedStructure
  }
}

ArchitectureStructureKindViewRecordBinding ::= {
  structureKindRef: ArchitectureStructureKindRef,
  allowableViewpointRefs: FinSet(U.ViewpointRef),
  viewRecordSetRef,
  allowedViewConstructionModes,
  requiredCorrespondenceRefs?,
  sourceReturnRequirement?,
  governingPatternApplicationRefs
}
```

`viewRecordSetRef` names the allowed Description-episteme or specification-use record set for one structure-kind binding. It is not a package grouping, not a `U.ViewpointBundle`, not a `ViewFamilyId`, and not a new TEVB viewpoint.

#### C.30.ASV:4.5 - Initial architecture structure kinds and view records

The initial set is a seed for first architecture moves, not an atlas. Use the table to choose one live structure kind and the exact governing pattern application that carries any stronger claim.

| Seed structure kind | Structural view | Minimum record fields beyond common ASV fields | First boundary |
| --- | --- | --- | --- |
| `FunctionalStructure` | `FunctionalStructureView@Context` | function refs or effect refs, capability refs, dependency refs, allocation refs | Use `A.6.F`, capability, work, or requirement patterns when those claims are live. |
| `FlowTransductionStructure` | `FlowTransductionStructureView@Context` | `transductionGraphRef`, `pathSliceRefs`, `crossingRefs`, `valuationRefs` | Use `E.18` and `C.30.TGA-FLOW-REL` for graph, path, or crossing structure input; use `C.28` for causal claims. |
| `RuntimeInteractionStructure` | `RuntimeInteractionStructureView@Context` | runtime elements, connectors and protocols, event topology and message topology, failure boundaries and latency boundaries | Use temporal, failure, evidence, or assurance patterns when runtime claims exceed structure. |
| `ModuleInterfaceStructure` | `ModuleInterfaceStructureView@Context` | module relation refs, interface specs, admissibility conditions, substitutability policy or change policy | Use `A.6.M` module-relation repair and conformance evidence when those claims are live. |
| `PlacementDeploymentStructure` | `PlacementDeploymentStructureView@Context` | allocation-to-site refs or environment refs, network locality or physical locality, jurisdiction constraints or safety constraints | Use temporal, evidence, legal patterns or regulatory patterns, or safety patterns for those stronger claims. |
| `InformationDataStructure` | `InformationDataStructureView@Context` | state bearer and residence refs, schema refs, semantic refs, persistence locus, provenance relation, custody relation, source-return conditions, privacy constraints | Use evidence, privacy, or source-return patterns when those claims are live. |
| `SecurityTrustBoundaryStructure` | `SecurityTrustBoundaryStructureView@Context` | protected asset or effect refs, trust boundary refs, untrusted input refs, privilege or authority refs, data-flow and control-flow refs, attack exposure refs, abuse or misuse path refs, secure-default or hardening boundary, supply-chain or update-channel refs, detection-response boundary refs when live | Gives a first security-architecture move before evidence, assurance, gate, risk-score, or compliance proof. |
| `ControlStructure` | `ControlStructureView@Context` | control role refs, declared control-rate refs, observer, estimator, controller, planner, and supervisor relations, feedback refs | Use `C.30.LCA`, dynamics, temporal, causal, evidence, and assurance patterns when those claims are live. |
| `ConstraintRequirementStructure` | `ConstraintRequirementStructureView@Context` | requirement refs, constraint refs, and invariant refs, affected structure refs, admissibility conditions | Requirements shape structures; requirement, gate, evidence, causal, or decision claims apply their exact governing patterns. |
| `MaterialSpatialStructure` | `MaterialSpatialStructureView@Context` | geometry, adjacency, containment, energy flow or material flow, safety separation | Physical separation is not safety proof; safety, evidence, dynamics, or causal claims apply their exact governing patterns. |
| `DeclaredLogicalStructure` | `LogicalStructureView@Context` | local logical relation class, relation constraints, correspondence to functional structures, module structures, runtime structures, and data structures | Covers `logical architecture` without making `logical` a universal ontology token. |

Externally governed classifier values remain admissible when they are the live architecture-relevant structure, but C.30.ASV does not define their full record families:

| Externally governed classifier value | ASV use | Full semantics and governing patterns |
| --- | --- | --- |
| `WorkMethodStructure` | Method arrangement or work arrangement changes the architecture move. | Use `MethodDescription`, `WorkPlan`, `WorkEnactment`, exception path, launch relation or gate relation, and `A.15` governing patterns; do not turn a work-method diagram into work authority. |
| `RoleEnactorStructure` | Responsibility or enactor allocation changes the architecture move. | Use role, enactor, organization, work, and stakeholder patterns for the stronger claim; do not treat an org chart as architecture truth. |
| `EvidenceAssuranceStructure` | Evidence reuse or assurance arrangement changes affected structure or source return. | Use `A.10`, `G.6`, or `B.3` for evidence sufficiency or assurance verdict; ASV only names the structure and loss boundary. |
| `ScaleEvolutionStructure` | Scale window, replacement or change policy, trajectory reference, or coarse-graining changes the architecture move. | Use `C.29`, `C.16`, temporal, source-return, or decision patterns for scale, characterization, or selection claims. |
| `OtherDeclaredStructureKind` | A local structure kind is declared because none of the seed or externally governed values fits. | Name definition, relation families, false interpretations, governing patterns, and context; do not mint a root kind by label alone. |

Minimum useful seed examples:

| Structure kind | Minimal example | False interpretation | First governing pattern |
| --- | --- | --- | --- |
| `FunctionalStructure` | Capability, effect, or transformation allocation. | Purpose truth or requirement satisfaction. | `A.6.F`, capability, work, or requirement pattern as live. |
| `FlowTransductionStructure` | Path, crossing, valuation, or transduction slice. | Whole architecture or causal proof. | `E.18`, `C.30.TGA-FLOW-REL`, C.29, or C.28 as live. |
| `ControlStructure` | Controller, observer, plant, feedback, or rate relation. | Stability, safety, or assurance proof. | `C.30.LCA`, temporal, dynamics, causal, evidence, or assurance claim as live. |
| `ModuleInterfaceStructure` | Module relation, interface spec, or substitutability boundary. | Module tree as all architecture. | `A.6.M` module-relation repair, conformance evidence, or decision pattern as live. |
| `InformationDataStructure` | State bearer, residence, provenance, and custody. | Database label. | Evidence, privacy, or source return as live. |
| `SecurityTrustBoundaryStructure` | Trust boundary, untrusted input, privilege path, or attack exposure. | Security proof, risk score, or compliance label. | Evidence, assurance, gate, C.24, C.16, C.25, or C.30.LCA as live. |
| `MaterialSpatialStructure` | Separation, adjacency, containment, or energy path or material path. | Safety proof or geometry as architecture truth. | Safety, evidence, dynamics, or causal claim as live. |
| `DeclaredLogicalStructure` | Local logical relation class with correspondence to other structures. | Universal logical architecture ontology. | Correspondence, function, module, runtime, data, or exact declared-neighbor pattern as live. |
Minimal `SecurityTrustBoundaryStructureView@Context` fields:

```text
SecurityTrustBoundaryStructureView@Context ::= {
  architectureStructuralViewRef:
  protectedAssetOrEffectRefs:
  trustBoundaryRefs:
  untrustedInputRefs:
  privilegeOrAuthorityRefs:
  dataFlowOrControlFlowRefs:
  attackExposureRefs:
  abuseOrMisusePathRefs:
  secureDefaultOrHardeningBoundary:
  updateOrSupplyChainChannelRefs:
  detectionResponseBoundaryRefs?:
  governingPatternApplicationRefs:
    A.10 | G.6 | B.3 | C.28 | A.20 | A.21 |
    C.16 | C.25 | C.24 when tool authority or agentic tool-use is live | C.30.LCA when control relation is live
  admissibleUse:
  nonAdmissibleUse:
    not compliance proof, not risk score, not assurance verdict, not security by checklist, not secure because a diagram says "zero trust"
}
```

`SecurityTrustBoundaryStructure` carries adversarial-boundary interpretation: which protected assets or effects are live, who or what is trusted, where untrusted input crosses, what authority or privilege is exposed, which adversarial paths and attack exposures matter, which data-flow or control-flow security boundaries matter, and where secure defaults, hardening, update or supply-chain channels, detection, or response boundaries change the next architecture move.

Do not open evidence, assurance, gate, or compliance pattern use only because the topic is safety, security, or regulation. Open it when the architecture move relies on evidence sufficiency, assurance verdict, gate passage, regulatory acceptance, or release authority. If the live move is structural, first recover the structure: trust boundary, loss-control relation, control relation, evidence reuse structure, or affected structure or affected view.

Use a `SafetyLossControlStructureNote` when a safety-architecture concern first needs the architecture-side loss-control structure rather than a safety-case verdict:

```text
SafetyLossControlStructureNote:
  lossOrHarm:
  hazardOrUnsafeState:
  unsafeControlActionOrMissingControl:
  controlledProcessOrPlantRef:
  controlConstraintRef:
  feedbackOrObservabilityBoundary:
  timingOrRateBoundary:
  operationalDesignScopeOrMisuseScope:
  foreseeableMisuseRefs?:
  architectureStructureKindRefs:
    ControlStructure | ConstraintRequirementStructure |
    SecurityTrustBoundaryStructure | InformationDataStructure |
    EvidenceAssuranceStructure
  governingPatternApplicationRefs:
    A.3.3 dynamics, C.27 temporal or rate,
    C.28 causal-use, A.10 or G.6 evidence,
    B.3 assurance, A.20 or A.21 gate
  nonAdmissibleUse:
    not safety proof, not safety-case verdict, not regulatory acceptance
```

The note gives a positive first architecture move: find the loss-control structure, controlled process or plant, constraint, foreseeable misuse, operational design scope, and action-relevant boundary. It does not replace evidence, assurance, gate, causal, dynamics, or temporal claims.

#### C.30.ASV:4.6 - Functional structure view boundary

`FunctionalStructureView@Context` under C.30.ASV does not mint `U.Function`. A functional element is a description-side architecture element under `VP.Functional` unless separately grounded as `U.Capability`, `U.Method`, `U.Work`, `U.Role`, or another existing FPF kind.

```text
FunctionalStructureView@Context ::= {
  architectureStructuralViewRef: ArchitectureStructuralView@ContextRef,
  functionOrEffectRefs?,
  capabilityRefs?,
  functionalDependencyRefs?,
  allocationRefs?,
  nonFunctionClaimNotes?,
  flowRelationRefs?,
  moduleInterfaceRelationRefs?,
  admissibleUse,
  nonAdmissibleUse
}
```

A transduction graph, path slice, crossing, or flow valuation is not a functional element. When flow is live, connect the functional view to `FlowTransductionStructure` through `C.30.TGA-FLOW-REL`. When module allocation is live, connect the functional view to `A.6.M` module-relation repair rather than treating function and module as one kind.

Composability and quality compositionality are separate claims. If the view says parts can be assembled, keep that as a structure claim or use claim. If it says a quality of the whole follows from parts, assign the quality-composition claim to `C.25` and C.16-backed measurement or quality claim.

```text
Composability:
  "A and B can be assembled under interface X."
  recoveredRelationOrRecordKind: ModuleAllocationRelation | InterfaceSpecification
Quality compositionality:
  "The assembled whole preserves safety, latency, or reliability."
  recoveredRelationOrRecordKind: QBundleSlot | structuralCharacteristicQBundleInputSlot | structuralCharacteristicCausalHypothesisForQBundleSlot | structuralCharacteristicEvidencePathForQBundleSlot
Non-admissible:
  successful assembly is not quality propagation
```

Compositional formalisms may express explicit composition structures and view relations and model relations. They do not make safety, latency, reliability, or another quality propagate automatically.

#### C.30.ASV:4.7 - Correspondence and source return

Use correspondence records when the view relates functional, flow, control, module-interface, information, runtime, placement, work, evidence, scale, or logical structures. Do not assert cross-view consistency by prose alone.

Correspondence examples:

| Source wording | Recover |
| --- | --- |
| "This function is implemented by that module." | `FunctionToModuleAllocationRef` or the exact allocation or relation record. |
| "This flow crosses that runtime boundary." | `FlowToRuntimeInteractionCorrespondence`. |
| "This evidence covers the replacement." | `EvidenceReuseToAffectedStructure`; assign sufficiency or verdict to `A.10`, `G.6`, or `B.3`. |
| "This requirement constrains that structure." | `RequirementToStructureConstraint` or exact constraint record. |
| "This scale window changes the structure kind." | `ScaleWindowToStructureKindCorrespondence`; assign scale-lens claims to `C.29` when live. |

Use `SourceReturnCondition` when compression, extraction, coarsening, evidence reuse, ML evaluation, bounded exception, many-to-many allocation, publication, or decision claim hides a distinction needed for action, assurance, causal use, legal review, regulatory review, comparison, or reopening.

If `viewConstruction` is `query`, `extraction`, `coarsening`, `correspondenceSlice`, or `sourceReturnSlice`, and omitted structure changes action, assurance, causal use, legal or regulatory review, or subsequent decision reopening, `SourceReturnCondition` is live.

When the view is used to name affected structures for a next move but no decision record is live, use C.30 `AffectedArchitectureStructureNote`: affected structure kinds, affected structure refs when known, affected ASV refs, accepted or suspected view loss, source-return condition, and the next admissible move. The note is not an architecture decision, ADR, gate passage, evidence sufficiency, or release authority.

Use the thinnest source or reliance relation that preserves the next architecture move. Open fuller source, evidence, assurance, or claim-kind relation only when the current source or reliance relation cannot be inspected, used, compared, refreshed, or bounded without it. A `ControlStructureViewNote` may precede full `C.30.LCA` use or proof-governing pattern applications when one control relation and its boundary are enough for the current move.

Treat source return as a user action, not only a metadata field:

```text
SourceReturnAction:
  returnTo:
    sourceStructure | sourceEpisteme | sourceView | sourceTrace |
    sourceCorpus | sourceModel | sourceEvidence | sourcePublication
  because:
    hiddenRelation | lostConstraint | coarsenedScale |
    ambiguousExtraction | staleEdition | crossViewMismatch |
    legalOrRegulatoryUse | assuranceOrDecisionUse
  nextMove:
    inspect | split | downgradeUse | addCorrespondence |
    openNeighborPattern | stop
```

Do not make source return mandatory for ordinary local recognition when no hidden distinction is being used for action. Do not omit source return when a hidden distinction carries a selected reliance relation, assurance, legal, comparison, causal, gate, or decision commitment. The condition is live only when the repaired text still relies on the hidden source-side distinction.

Model cards, system cards, and evaluation harness reports may publish or substantiate an architecture structural view only when the structural-view claim is recoverable. The view must name the relevant structure kind, such as `RuntimeInteractionStructure`, `InformationDataStructure`, `SecurityTrustBoundaryStructure`, `EvidenceAssuranceStructure`, `ModuleInterfaceStructure`, or another declared structure kind; it must also state intended-use scope, evaluation scope and known loss when evaluation is used, deployment-context mismatch when live, and the evidence or assurance governing pattern when the publication is used beyond transparency. A card or harness is not architecture adequacy, safety proof, or release claim or gate claim by publication alone.

#### C.30.ASV:4.8 - Worked slices

**Runtime degradation.** A team says, "The architecture is fine, but incidents happen when failover starts." The first architecture move is to recover runtime interaction, control relation, failover relation, placement, and evidence-assurance structures before turning a dashboard or deployment diagram into proof:

```text
Runtime degradation slice:
  active structure kinds:
    RuntimeInteractionStructure
    ControlStructure
    InformationDataStructure
    PlacementDeploymentStructure
    EvidenceAssuranceStructure
  first architecture move:
    recover runtime interaction topology, control relation or failover relation,
    state custody, placement relation, locality relation, evidence path, and observability relation
  nonAdmissibleUse:
    deployment diagram as runtime proof,
    observability dashboard as evidence sufficiency,
    green indicator value as gate authority or release authority
```

Use `C.24` only when tool-use, call planning, call graph, work execution, or budgeted agentic tool-use is the live claim. Do not absorb those claims into architecture structure.

**CPS or plant architecture.** A plant drawing, P&ID-like artifact, LCA sketch, or safety-case view is not the plant architecture by itself. First recovery may need:

```text
CPS and plant architecture first recovery:
  MaterialSpatialStructure:
    physical separation, adjacency, energy path or material path
  ControlStructure:
    controller, plant, observer, supervisor, control rate
  InformationDataStructure:
    sensor data semantics, provenance, custody, source return
  PlacementDeploymentStructure:
    locality, environment, jurisdiction, safety separation
  EvidenceAssuranceStructure:
    evidence reuse boundary and affected structures
first architecture move:
  relate physical separation, sensor data semantics, control rate,
  placement boundary, and evidence reuse
correspondenceOrLossLine:
  record which separation, data, control-rate, placement, or evidence-reuse
  relation is preserved by the slice and which structure is hidden or lossy
stop condition:
  no P&ID, LCA diagram, or safety case is treated as the architecture
```

**Chiplet or device architecture.** A packaging diagram or interconnect sketch may open several structure kinds:

```text
Chiplet and device architecture first recovery:
  MaterialSpatialStructure:
    packaging, adjacency, thermal path, energy path
  FlowTransductionStructure:
    interconnect topology, data flow path, energy flow path, or signal flow path
  ModuleInterfaceStructure:
    interface specification, protocol, conformance boundary
  PlacementDeploymentStructure:
    physical locality, substrate, host environment
first architecture move:
  separate interconnect topology, packaging path, thermal path, or energy path,
  interface specification, and evidence boundary and conformance boundary
correspondenceOrLossLine:
  record the preserved relation among interconnect, physical package,
  interface, and placement, plus any benchmark or packaging-view loss
stop condition:
  no packaging diagram or benchmark becomes performance, safety,
  evidence, or gate proof by appearance
```

**Organization or operating-model architecture.** An org chart or work-method diagram can be architecture-relevant only after the work, role, information, and evidence records are separated:

```text
Organization and operating-model architecture first recovery:
  RoleEnactorStructure:
    responsibility allocation and enactment boundary
  WorkMethodStructure:
    repeatable work method and exception path
  InformationDataStructure:
    information custody, state residence, provenance
  EvidenceAssuranceStructure:
    evidence reuse, approval, audit trail, source return
first architecture move:
  relate responsibility allocation, work repeatability,
  information custody, and evidence reuse
correspondenceOrLossLine:
  record the preserved relation among role, work, information, and evidence
  structures, plus any org-chart or work-method-diagram loss
stop condition:
  no org chart or work-method diagram is treated as the architecture, decision,
  evidence sufficiency, or assurance verdict
```

**Evidence reuse across product variants.** A certification or test package reused across module variants may be architecture-relevant as an evidence-and-assurance structure view, but it is not an assurance verdict:

```text
Evidence reuse across product variants:
  structureKindRef: EvidenceAssuranceStructure
  structuralFeature:
    evidence package shared across module variants
  affectedQBundleSlot:
    assurance maintainability or release readiness
  architectureMove:
    name affected structures, variant boundary, hidden view losses,
    and source-return condition
  governingPatternApplicationRefs:
    A.10, G.6, or B.3 for evidence sufficiency or assurance verdict
  nonAdmissibleUse:
    evidence-structure view as assurance verdict
```

**AI agent diagram.** A "planner-memory-tools" diagram is not the agent's architecture by itself. It may open first recovery as a structure-kind set, without minting an AI-domain ontology:

```text
AI-agent architecture first recovery:
  RuntimeInteractionStructure:
    model-tool-memory-planner-evaluator-human topology
  InformationDataStructure:
    memory scopes, data custody, provenance, retention,
    context-window relation and source-return relation
  SecurityTrustBoundaryStructure:
    untrusted content channels, prompt-injection or instruction boundary,
    tool authority, secret-bearing contexts, memory custody crossing and data custody crossing,
    output handling, supply-chain or update path
  ModuleInterfaceStructure:
    tool specs, API specs, and interface specs and substitutability limits
  EvidenceAssuranceStructure:
    eval harness, human approval, evidence decay, incident feedback
admissibleArchitectureMove:
  split runtime interaction, information, security boundary, module-interface, and evidence-assurance claims before relying on the diagram
correspondenceOrLossLine:
  record the preserved relation among runtime topology, information custody,
  security boundary, module-interface, and evidence-assurance structures,
  plus any diagram or evaluation-harness loss
governingPatternApplicationRefs:
  C.30.TGA-FLOW-REL when E.18 flow relation is live,
  A.6.M module-relation repair for tool, API, or interface relation claims,
  A.10, G.6, or B.3 when evidence or assurance reliance is live,
  C.24, E.16, A.20, or A.21 when tool-call, autonomy, constraint, or gate authority is live
stop condition:
  no evidence sufficiency, assurance, gate, autonomy, or tool-call authority remains inside ASV
```

Structural AI-agent security is architecture structure when these structure kinds change the next architecture move. When the live claim is latent representation, decoding, or effect adequacy rather than architecture structure, keep the phrase as a reduced-use source cue until the exact governing representation, decode, or effect-adequacy pattern carries that claim.

**Generated code-agent relation graph.** A probe JSON or code-agent architecture relation graph can be an architecture structural view publication only after observed, inferred, or unknown observation value, evidence pointers or source pointers, unexplored regions, typed relation semantics, and source-return conditions are present. It is not proof of the agent's internal belief and not assurance that a downstream code change is safe.

**Neural-network block replacement.** Replacing attention, FFN, convolution, SSM, recurrent, memory block or cache block, MoE expert-selection, pruning, distillation, or another block is an architecture move only when the changed structure kind, flow relation, module-interface claim kind, preserved and lost structure, affected characteristic, source relation, and decision or evidence governing pattern are named.

