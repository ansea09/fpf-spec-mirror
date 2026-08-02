---
chunk_kind: "child"
pattern_id: "C.30.ASV"
pattern_title: "Architecture Structural View Adequacy (ASV)"
section_id: "C.30.ASV:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ASV/C.30.ASV__005_solution.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "C.30.ASV — Architecture Structural View Adequacy (ASV)"
  - "C.30.ASV:4 — Solution"
line_start: 61252
line_end: 61861
dependencies:
  - "A.1"
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
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureStructureKindRef"
  - "VF.ARCH.STRUCTURE"
  - "architecture structural view"
  - "correspondence"
  - "hidden or lost structure"
  - "source return"
  - "structure kind"
  - "viewpoint bundle"
---

### C.30.ASV:4 - Solution

Govern architecture structural views by first identifying one candidate description episteme, its exact selected `U.Structure` EntityOfConcern, effective `U.ReferenceScheme`, structure kind, exact viewpoint episteme, and the direct conformance occurrence. Then add construction history, correspondence, hidden or lost structure, source-to-use path or work-reliance relation when current, source-return condition when needed, admissible use, and next architecture move. Use `ArchitectureStructuralView` only for the same episteme whose E.17.0 conformance actually obtains.

A conforming `ArchitectureStructuralView` is not a second individual beside its description. The candidate retains one C.2.1 identity `<exact ClaimGraph, one exact selected-structure EntityOfConcern, effective U.ReferenceScheme>`. The exact viewpoint and `EpistemeViewpointConformanceRelation` qualify that same episteme as `U.View`; they do not enter its C.2.1 identity.

C.30.ASV is the selected-structure structural-view adequacy pattern for architecture work. It explains how descriptions of different selected structure kinds may satisfy declared viewpoints and concerns. It is not a complete architecture-description pattern; `C.30.AD` composes separately identified descriptions, view-use claims, and correspondence only when that broader description use is being made.

C.30.ASV does not extend the TEVB core viewpoint set by implication. It defines architecture structure kinds and architecture-specific bindings to exact viewpoint epistemes. TEVB viewpoints are reused when their fixed E.17.0 rules fit; other structure descriptions use exact viewpoints from `VF.ARCH.STRUCTURE`, a declared local viewpoint bundle, or a governing FPF pattern. Source-to-use, work-reliance, project-use, representation, and publication relations remain separate from viewpoint conformance.

#### C.30.ASV:4.1 - Architecture structural view record

`StructuralAspectDescription` describes one selected structural aspect under A.22. It is not an `ArchitectureStructureKindRef` or `U.View` by itself. `ArchitectureStructuralView` names the same architecture-description episteme only after exact E.17.0 conformance obtains.

```text
ArchitectureStructuralView ::= ArchitectureDescription & U.View & {
  viewEpistemeRef: U.EpistemeRef,
  claimGraph: exactly one C.2.1 ClaimGraph,
  entityOfConcernRef: selectedStructureRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue,

  selectedStructureRef: U.StructureRef,
  relatedStructureRefs?: FinSet(U.StructureRef),
  structureKindRef: ArchitectureStructureKindRef,

  viewpointRef: U.ViewpointRef,
  viewpointConformanceRelationRef: EpistemeViewpointConformanceRelationRef,
  concernRefs?: FinSet(U.EntityRef),

  describedHolonRef?: U.HolonRef,
  architectureRelationOccurrenceRefs?: FinSet(ArchitectureRelationRef),
  architectureClaimRefs?: FinSet(U.EpistemeRef constrained to ArchitectureClaim),
  claimScope?: U.ClaimScope, byValue,
  modelUseStructureRef?: U.StructureRef,
  empiricalGroundingRelationRefs?: FinSet(EpistemeEmpiricalGroundingRelationRef),

  recordGoverningPatternRef,
  selectedRelationKindRefs?,
  selectedConstraintRefs?,
  selectedInvariantRefs?,
  selectedOperationDescriptionRefs?,
  selectedDynamicsDescriptionRefs?,
  viewConstruction:
    directDescription | projection | query | extraction |
    coarsening | correspondenceSlice | sourceReturnSlice,
  structuralAspectDescriptionRef?: U.EpistemeRef,
  hiddenOrLostStructure,
  structureKnowledgeState?:
    declared | observed | inferred | generated | simulated |
    extracted | hypothesized | unknownRegionPresent,
  correspondenceClaimOrRelationRefs?: FinSet(U.EpistemeRef | U.RelationRef),
  sourceToUsePathRefs?: FinSet(U.RelationRef),
  workRelianceRelationRefs?: FinSet(U.RelationRef),
  sourceReturnCondition?,

  representationRefs?: FinSet(U.EntityRef),
  publicationOccurrenceRefs?: FinSet(EpistemePublicationRelationRef),
  publicationFormRefs?: FinSet(U.EntityRef),
  carrierRefs?: FinSet(U.EntityRef constrained to U.PresentationCarrier),
  admissibleUse,
  nonAdmissibleUse
}
```

The selected `U.Structure` is the one EntityOfConcern. Before that field can be filled, A.22 identifies the structure from exact constituents, selected independently obtaining relation occurrences, applied constraint claims, and one exact receiving-use frame. A description, query, diagram, bundle, file, representation, or publication creates none of those discriminators. `relatedStructureRefs` may name structures needed to interpret correspondence, allocation, or crossing, but they do not create a union-valued EntityOfConcern. When another selected structure becomes primary, identify another description episteme or use exact C.2.1 edition/retargeting semantics; do not overwrite identity through a view field.

The direct conformance occurrence has exactly two participants: `viewEpistemeRef` as candidate E and `viewpointRef` as exact P. Its fixed E.17.0 predicate requires: (1) independently identified E and admitted P; (2) exact `EntityOfConcern(E)` recovered; (3) P's fixed EntityOfConcern-kind criterion succeeds for that exact object; (4) E has an independently governed episteme kind admitted by P without circular `U.View` use; and (5) E's fixed claim content under its effective scheme satisfies P's concern-coverage, semantic-form, completeness, and admitted-omission rules. The occurrence is participant-determined by `<E,P>`.

An architecture claim can carry positive, negative, unresolved, required, desired, expected, or candidate content. `architectureRelationOccurrenceRefs` is affirmative only for independently obtaining direct `ArchitectureRelation` occurrences. `describedHolonRef` and participant traces keep the subject recoverable; neither an optional claim nor a diagram derives the subject-side occurrence.

`ClaimScope`, concern, model-use structure, and empirical grounding remain optional neighboring qualifiers or relations. `modelUseStructureRef` appears only when an independently selected DDD-style bounded-model-use structure changes interpretation or selection for this use. None enters base episteme or selected-structure identity.

`viewConstruction` records provenance only. Direct authoring, A.6.3 construction, projection, query, extraction, selection, bundle inclusion, diagramming, rendering, publication, evaluation, or current use neither satisfies the conformance predicate nor creates selected structure. Representation, publication occurrence, form, and carrier likewise retain their own identities.

`structureKnowledgeState?` states how the selected structure is known when partial knowledge matters: declared, observed, inferred, generated, simulated, extracted, hypothesized, or with an unknown region present. Unknown or inferred structure may guide inspection or source return; it cannot by itself supply architecture truth, assurance, gate, release, causal proof, or architecture decision.

#### C.30.ASV:4.2 - Architecture structure-kind classifier

`ArchitectureStructureKindRef` is a C.30-local `DiscriminatorToken` enumeration over exact architecture-relevant `U.Structure` references selected under A.22 and used by C.30. It is not `U.Kind`, `U.Viewpoint`, `U.ViewpointBundle`, `StructuralAspectDescription`, `ArchitectureStructuralView`, or a root `U.*` kind. An `ArchitectureStructuralView` uses `structureKindRef` to state which kind of selected structure its claim graph describes; that token neither identifies the structure nor grants `U.View` membership.

```text
ArchitectureStructureKindRef ::= one of {
  FunctionalStructure,
  TransformationFlowStructure,
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
  AllocationResponsibilityStructure,
  EvidenceAssuranceStructure,
  ScaleEvolutionStructure,
  OtherDeclaredStructureKind
}
```

The first group is the seed classifier set for ordinary architecture structural-view use. `SecurityTrustBoundaryStructure`, `WorkMethodStructure`, `AllocationResponsibilityStructure`, `EvidenceAssuranceStructure`, and `ScaleEvolutionStructure` are classifier values over selected `U.Structure` references, not new root kinds. ASV may use them to name the selected architecture-relevant structure, but their full semantics stay in the named security, work and method, allocation-responsibility, evidence and assurance, scale, characterization, or mathematical-lens patterns.

Do not enumerate structure kinds by default. Choose the smallest useful structure-kind set that changes the next architecture move. If no structure kind changes action, keep the phrase as ordinary recognition wording or a source note. This does not weaken kind discipline; it prevents `ArchitectureStructureKindRef` from becoming an audit checklist.

Inside C.30.ASV, `OtherDeclaredStructureKind` is always an architecture-structure-kind classifier value over `U.Structure`; it does not mint a general FPF root kind.

`OtherDeclaredStructureKind` is admissible only when the local text names:

- `declaredStructureKindName`;
- `declaredStructureKindDefinition`;
- allowed relation families;
- locally triggered overreads;
- governing-pattern applications;
- a selected-structure admission test, plus the effective `U.ReferenceScheme` when the local classifier name depends on one.

Each structure kind needs a short definition, allowed relation families, locally triggered overreads, typical governing-pattern applications, and example architecture structural-view records. This is not a new root-kind set; it is a controlled classifier set over exact `U.Structure` values.

#### C.30.ASV:4.3 - Small triage output

Use `ArchitectureStructureKindTriage@Project` before a full view record when the practitioner only needs to identify the structure kind under consideration and next architecture move.

```text
ArchitectureStructureKindTriage@Project ::= {
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work,
  architectureStructuralViewProjectUseRelationRef?: U.RelationRef governed by the exact triage-use or view-use pattern,
  architectureClaimRef?: U.EpistemeRef constrained to ArchitectureClaim,
  architectureRelationOccurrenceRef?: ArchitectureRelationRef,
  describedHolonRef?: U.HolonRef,
  candidateViewEpistemeRef?: U.EpistemeRef,
  exactViewpointRef?: U.ViewpointRef,
  viewpointConformanceRelationRef?: EpistemeViewpointConformanceRelationRef,
  claimScope?: U.ClaimScope, byValue,
  effectiveReferenceScheme?: U.ReferenceScheme, byValue,
  modelUseStructureRef?: U.StructureRef,
  architectureConcernCue?,
  sourcePhrase?,
  inspectedDescriptionOrViewRef?: U.EpistemeRef,
  candidateStructureKindRefs: FinSet(ArchitectureStructureKindRef),
  smallestUsefulStructureKindRefs: FinSet(ArchitectureStructureKindRef),
  selectedStructureRefs?: FinSet(U.StructureRef),
  hiddenOrLostStructureCueRefs?,
  primaryGoverningPatternApplicationRef?,
  admissibleArchitectureMove:
    inspect | split | relate | downgrade | assignGoverningPattern | stop |
    otherDeclared,
  governingPatternApplicationRefs?,
  nonAdmissibleOverread?,
  stopCondition
}
```

`architectureConcernCue?` and `sourcePhrase?` are recognition wording. `inspectedDescriptionOrViewRef?` and `candidateViewEpistemeRef?` name actual epistemes only when identified under C.2.1. None creates an `ArchitectureStructureKindRef`, selected structure, architecture relation, or `U.View`. Fill `exactViewpointRef` and `viewpointConformanceRelationRef` only when the same candidate episteme actually qualifies as a view.

When `architectureClaimRef` is absent, `describedHolonRef`, `architectureRelationOccurrenceRef`, or at least one exact candidate selected structure must keep the subject recoverable for the intended triage. `claimScope`, `effectiveReferenceScheme`, and `modelUseStructureRef` are present only when they change this use. The card publishes no architecture claim and creates no subject relation. A full `ArchitectureStructuralView` requires the candidate episteme's exact C.2.1 identity plus obtaining E.17.0 conformance; it does not require an architecture-claim record when the exact selected-structure EntityOfConcern and subject trace are otherwise recoverable.

Practitioner prompt labels are first-entry cues, not `ArchitectureStructureKindRef` values. FPF-governed records use the Tech values below:

```text
Functional -> FunctionalStructure
Flow -> TransformationFlowStructure
Control -> ControlStructure
Module -> ModuleInterfaceStructure
Method and work -> WorkMethodStructure
Role -> AllocationResponsibilityStructure
Evidence -> EvidenceAssuranceStructure
Scale -> ScaleEvolutionStructure
Security -> SecurityTrustBoundaryStructure
```

#### C.30.ASV:4.3a - Evolutionary-engineering candidate structural view

Use this branch when a retained variant, front member, selected set, or architecture-candidate palette needs structural-description triage. The claim is not "this archive is architecture" and not "this record is already a `U.View`." It is "this candidate makes an exact selected structure or structure kind current for an architecture claim or possible architecture move."

```text
ArchitectureCandidateStructuralDescription:
  CandidateSetOrArchiveRef:
  CandidateRef:
  DescribedHolonOrArchitectureRelationRef:
  SelectedStructureOrStructureKindRef:
  CandidateDescriptionEpistemeRef:
  ExactViewpointRef?:
  ViewpointConformanceRelationRef?:
  AffectedCharacteristicRef:
  CorrespondenceOrLossRef?:
  NextGoverningPatternRef:
```

If the candidate cannot name an exact selected structure or structure kind, keep it in `C.18`, `C.19`, or `G.5`. If the description only publishes, compares, or explains the candidate, use `C.30.AD`, the comparison pattern, or the publication-use pattern named by value. It is an `ArchitectureStructuralView` only when the same candidate description episteme independently conforms to the exact viewpoint under E.17.0.

#### C.30.ASV:4.4 - Architecture viewpoint bundle and binding rows

Architecture structural views can reuse exact viewpoint epistemes collected in `VF.ARCH.STRUCTURE` without turning structure kinds into viewpoints. The bundle is separate from `VF.TEVB.ENG`: it may import TEVB, but it does not expand the TEVB core engineering viewpoint set.

Declaration source: `VF.ARCH.STRUCTURE` is an `E.17.1` and `F.18` declared viewpoint bundle. Its `VP.Architecture*` ids resolve to exact `U.Viewpoint` epistemes. They do not add TEVB viewpoints, name structure kinds, define publication faces, or carry architecture, decision, evidence, gate, or assurance authority.

#### C.30.ASV:4.4a - Structural-view publication-use boundary

This subsection is the C.30.ASV structural-view publication-use boundary. C.30.ASV governs exact description identity, selected architecture-relevant structure, structure kind, E.17.0 viewpoint conformance, construction history, correspondence, hidden structure and lost structure, source return, and next architecture move. When a view, diagram, graph, card, benchmark, probe output, model publication, or architecture note is used for evidence sufficiency, safety assurance, gate passage, release permission, work record, or decision authority, apply the pattern governing that claim; keep only the structural-view record and next architecture move in C.30.ASV.

```text
VF.TEVB.ENG core stays:
  { VP.Functional, VP.Procedural, VP.AllocationResponsibility, VP.ModuleInterface }
```

TEVB is the small engineering viewpoint bundle over holons. The architecture problem is broader than TEVB, but the broader coverage is not solved by putting record sets in a `U.ViewpointBundle`. A bundle carries exact viewpoint epistemes. A separate architecture-local description binds structure-kind classifiers, candidate record sets, construction modes, correspondence expectations, and governing-pattern applications.

```text
VF.ARCH.STRUCTURE : U.ViewpointBundle {
  viewFamilyId = VF.ARCH.STRUCTURE,
  imports = { VF.TEVB.ENG },
  EntityOfConcernClassSpec = {
    e : U.Episteme |
    C.2.1 identity of e is recoverable and
    EntityOfConcern(e) is one exact selected U.Structure
  },
  viewpointRefs = {
    VP.ArchitectureStructure,
    VP.ArchitectureCorrespondence,
    VP.ArchitectureSourceReturn,
    VP.ArchitectureDecisionAffectedStructure
  }
}

ArchitectureStructureKindViewRecordBinding ::= {
  structureKindRef: ArchitectureStructureKindRef,
  allowableViewpointRefs: FinSet(U.ViewpointRef),
  candidateViewRecordSetRef,
  allowedViewConstructionModes,
  requiredConformanceRuleRefs,
  requiredCorrespondenceClaimOrRelationRefs?,
  sourceReturnRequirement?,
  governingPatternApplicationRefs
}
```

`candidateViewRecordSetRef` names an exact collection of permitted description or specification-use record forms for one structure-kind binding. The binding and bundle may help resolve candidate E and exact P, but neither makes the five-part E.17.0 predicate true, identifies an `EpistemeViewpointConformanceRelation` occurrence, grants `U.View` membership, or creates the selected structure. It is not a publication face, package grouping, `ViewFamilyId`, or new TEVB viewpoint.

#### C.30.ASV:4.5 - Initial architecture structure kinds and view records

The initial set is a seed for first architecture moves, not an atlas. Use the table to choose one structure kind under consideration and the governing-pattern application that carries any non-ASV claim kind.

| Seed structure kind | Structural view | Minimum record fields beyond common ASV fields | First boundary |
| --- | --- | --- | --- |
| `FunctionalStructure` | `FunctionalStructureView` | `functionalBehaviorClaimRefs`, `requiredOrDesiredEffectClaimRefs?`, `actualTransformationRefs?`, `selectedTransformationFlowStructureRefs?`, `functionalElementClaimRefs?`, `transformerSideFillerRefs?`, `candidateBearerRefs?`, input-condition refs, output-condition refs, functional-port refs, capability refs, dependency refs, allocation refs, correspondence refs | Required/desired content stays a claim; use `A.3.4` only for independently actual transformations, and use capability, work, module-allocation, or requirement patterns when those claims are being made. |
| `TransformationFlowStructure` | `TransformationFlowStructureView` | `transformationFlowStructureRef`, `pathSliceRefs`, `crossingRefs`, `valuationRefs`, `mathematicalDescriptionRefs?` | Use `E.18` and `C.30.TFS-REL` for selected transformation-flow structure, transformation-flow path, or crossing input; use `E.18.2` and `C.29` for mathematical graph descriptions; use `C.28` for causal claims. |
| `RuntimeInteractionStructure` | `RuntimeInteractionStructureView` | runtime elements, connectors and protocols, event topology and message topology, failure boundaries and latency boundaries | Use temporal, failure, evidence, or assurance patterns when runtime claims exceed structure. |
| `ModuleInterfaceStructure` | `ModuleInterfaceStructureView` | module claim or admitted relation refs, interface specs, admissibility conditions, substitutability policy or change policy | Use `A.6.M` module-claim repair and the direct interface or relation owner when those claims are being made. |
| PlacementDeploymentStructure | PlacementDeploymentStructureView | allocation-to-site refs or environment refs, network locality or physical locality, jurisdiction constraints or safety constraints | Use temporal, evidence, law-domain, regulatory, or safety patterns when claims of those non-placement kinds are being made. |
| `InformationDataStructure` | `InformationDataStructureView` | state bearer and residence refs, schema refs, semantic refs, persistence locus, provenance relation, custody relation, source-return conditions, privacy constraints | Use evidence, privacy, or source-return patterns when those claims are being made. |
| `SecurityTrustBoundaryStructure` | `SecurityTrustBoundaryStructureView` | protected asset or effect refs, trust boundary refs, untrusted input refs, privilege or authority refs, data-flow and control-flow refs, attack exposure refs, abuse or misuse path refs, secure-default or hardening boundary, supply-chain or update-channel refs, detection-response boundary refs when the corresponding claim is being made | Gives a first security-architecture move before evidence, assurance, gate, risk-score, or compliance proof. |
| `ControlStructure` | `ControlStructureView` | control role refs, declared control-rate refs, observer, estimator, controller, planner, and supervisor relations, feedback refs | Use `C.30.LCA`, dynamics, temporal, causal, evidence, and assurance patterns when those claims are being made. |
| `ConstraintRequirementStructure` | `ConstraintRequirementStructureView` | requirement refs, constraint refs, and invariant refs, affected structure refs, admissibility conditions | Requirements shape structures; requirement, gate, evidence, causal, or decision claims apply their governing patterns. |
| `MaterialSpatialStructure` | `MaterialSpatialStructureView` | geometry, adjacency, containment, energy flow or material flow, safety separation | Physical separation is not safety proof; safety, evidence, dynamics, or causal claims apply their governing patterns. |
| `DeclaredLogicalStructure` | `LogicalStructureView` | local logical relation class, relation constraints, correspondence to functional structures, module structures, runtime structures, and data structures | Covers `logical architecture` without making `logical` a universal ontology token. |

Externally governed classifier values remain admissible when they are the architecture-relevant structure under consideration, but C.30.ASV does not define their full record families:

| Externally governed classifier value | ASV use | Full semantics and governing patterns |
| --- | --- | --- |
| `WorkMethodStructure` | Method arrangement or work arrangement changes the architecture move. | Use `MethodDescription`, `WorkPlan`, `WorkEnactment`, exception-handling relation, launch relation or gate relation, and `A.15` governing patterns; do not turn a work-method diagram into work authority. |
| `AllocationResponsibilityStructure` | Responsibility or enactor allocation changes the architecture move. | Use role, enactor, organization, work, and stakeholder patterns when those claim kinds are being made; do not treat an org chart as architecture truth. |
| `EvidenceAssuranceStructure` | Evidence reuse or assurance arrangement changes affected structure or source return. | Use `A.10`, `G.6`, or `B.3` for evidence sufficiency or assurance verdict; ASV only names the structure and loss boundary. |
| `ScaleEvolutionStructure` | Scale window, replacement or change policy, trajectory reference, or coarse-graining changes the architecture move. | Use `C.29`, `C.16`, temporal, source-return, or decision patterns for scale, characterization, or selection claims. |
| `OtherDeclaredStructureKind` | A local structure kind is declared because none of the seed or externally governed values fits. | Name its definition, selected-structure admission test, relation families, governing patterns, and effective reference scheme when local meaning depends on one; do not mint a root kind by label alone. |

Minimum useful seed examples:

| Structure kind | Minimal example | False interpretation | First governing pattern |
| --- | --- | --- | --- |
| `FunctionalStructure` | Capability, required or desired effect claim, or separately actual transformation allocation. | Purpose truth, requirement satisfaction, or a required effect treated as actual change. | `A.6.F`, `A.3.4` only for actual transformation, capability, work, or requirement pattern when that claim kind is being made. |
| `TransformationFlowStructure` | Transformation-flow path, crossing, valuation, or selected transformation slice. | Whole architecture or causal proof. | `E.18`, `C.30.TFS-REL`, `E.18.2`, C.29, or C.28 when selected structure, graph description, transformation-flow path, crossing, mathematical-lens, or causal-use claim kind is being made. |
| `ControlStructure` | Controller, observer, plant, feedback, or rate relation. | Stability, safety, or assurance proof. | `C.30.LCA`, temporal, dynamics, causal, evidence, or assurance pattern when that claim kind is being made. |
| `ModuleInterfaceStructure` | Module relation, interface spec, or substitutability boundary. | Module tree as all architecture. | `A.6.M` module-relation repair, conformance evidence, or decision pattern when that claim kind is being made. |
| `InformationDataStructure` | State bearer, residence, provenance, and custody. | Database label. | Evidence, privacy, or source-return pattern when that claim or reliance use is being made. |
| `SecurityTrustBoundaryStructure` | Trust boundary, untrusted input, privilege path, or attack exposure. | Security proof, risk score, or compliance label. | Evidence, assurance, gate, `C.24` agentic tool-use relation or call-planning relation, C.16, C.25, or C.30.LCA when that security, evidence, assurance, gate, tool-use, measurement, quality, or control claim kind is being made. |
| `MaterialSpatialStructure` | Separation, adjacency, containment, or energy path or material path. | Safety proof or geometry as architecture truth. | Safety, evidence, dynamics, or causal pattern when that claim kind is being made. |
| `DeclaredLogicalStructure` | Local logical relation class with correspondence to other structures. | Universal logical architecture ontology. | Correspondence, function, module, runtime, data, or governing pattern when that relation is being claimed or a claim of that kind is being made. |
Minimal `SecurityTrustBoundaryStructureView` fields:

```text
SecurityTrustBoundaryStructureView ::= {
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
    C.16 | C.25 | C.24 agentic tool-use relation or call-planning relation when tool authority is being claimed | C.30.LCA when a control relation is being claimed
  admissibleUse:
  otherClaimBoundary:
    compliance, risk-score, assurance, checklist-security, and zero-trust claims apply the evidence, assurance, risk, gate, or security pattern governing the claim being made
}
```

`SecurityTrustBoundaryStructure` carries adversarial-boundary interpretation: which protected assets or effects are under consideration, who or what is trusted, where untrusted input crosses, what authority or privilege is exposed, which adversarial paths and attack exposures matter, which data-flow or control-flow security boundaries matter, and where secure defaults, hardening, update or supply-chain channels, detection, or response boundaries change the next architecture move.

Apply evidence, assurance, gate, or compliance patterns only when the architecture move relies on evidence sufficiency, assurance verdict, gate passage, regulatory acceptance, or release authority. If the selected move is structural, first recover the structure: trust boundary, loss-control relation, control relation, evidence reuse structure, or affected structure or affected view.

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

A `FunctionalStructureView` under C.30.ASV does not mint `U.Function`, `U.Transformation`, or a bearer relation. It is the same `ArchitectureStructuralView` episteme whose EntityOfConcern is one selected functional `U.Structure` and whose exact viewpoint conformance obtains. It may carry `FunctionalElementClaim` epistemes when the claim graph relates that selected functional structure to required or desired behavior/effect content and to a bearer or candidate-bearer locus. The claim is not identical with any actual behavior occurrence, bearer, capability, port, allocation, or relation.

Keep three branches explicit:

- **required or desired behavior/effect:** a C.2.1 claim under its requirement, architecture, capability, method, functional-view, or other direct owner;
- **actual transformation:** an independently identified `U.Transformation` only after A.3.4 recovers the changed referent, extent or boundary, boundary conditions, actual before/during/after facts, and continuity or reidentification basis;
- **compound flow organization:** an exact selected `TransformationFlowStructure` under E.18, whose constituents and selected obtaining relations are independently identified; the structure is not itself an actual transformation.

`FunctionalElementClaim` has ordinary C.2.1 identity `<exact ClaimGraph, one exact EntityOfConcern, effective U.ReferenceScheme>`. For this use its EntityOfConcern is the selected functional structure. Its claim content may name:

- one or more required or desired behavior/effect claim refs;
- actual transformation refs only when the complete A.3.4 basis independently obtains;
- selected transformation-flow structure refs for compound flow organization;
- a bearer or candidate-bearer locus, normally a `U.System` or candidate system for a separately governed transformer-role claim;
- capability, input/output condition, functional-port, dependency, allocation, and correspondence refs only under their direct owners.

If no bearer or candidate allocation is current, do not claim a filled functional element. Record a required-behavior gap, required-effect gap, capability gap, functional-behavior slot, or candidate allocation question. This preserves the practical architecture move without pretending that a module, component, diagram row, function word, requirement, or selected flow structure has already supplied the bearer or actual change.

```text
FunctionalStructureViewUse ::= {
  architectureStructuralViewRef: U.EpistemeRef constrained to ArchitectureStructuralView,
  functionalElementClaimRefs?: FinSet(U.EpistemeRef),
  sourceFunctionWordingRefs?,
  functionalBehaviorClaimRefs?: FinSet(U.EpistemeRef),
  requiredOrDesiredEffectClaimRefs?: FinSet(U.EpistemeRef),
  actualTransformationRefs?: FinSet(U.TransformationRef),
  selectedTransformationFlowStructureRefs?: FinSet(U.StructureRef constrained to TransformationFlowStructure),
  transformerSideFillerRefs?: FinSet(U.SystemRef),
  candidateBearerRefs?: candidate system refs; explicit gap refs,
  capabilityRefs?,
  inputConditionRefs?,
  outputConditionRefs?,
  functionalPortRefs?,
  functionalDependencyRefs?,
  allocationRefs?,
  correspondenceClaimOrRelationRefs?,
  nonFunctionClaimNotes?,
  flowRelationRefs?,
  moduleInterfaceClaimOrRelationRefs?,
  admissibleUse,
  nonAdmissibleUse
}
```

**Required-cooling-effect / later-actual-cooling countercase.** Requirement episteme `RequiredCoolingEffect-1` says that Rack 7 should be brought below 30 °C during declared operation. Before the rack or cooling loop has changed, that is required effect claim content: there is no actual `U.Transformation`, even if a functional-view row, flow diagram, or selected `TransformationFlowStructure` cites it. Later, `Rack7CoolingTransformation-42` may be identified under A.3.4 when the exact changed referent and boundary are fixed, operating and ambient boundary conditions are stated, actual before facts show 38 °C, actual during facts recover heat removal, actual after facts show 27 °C, and continuity or reidentification keeps the same referent recoverable. A separate satisfaction or realization predicate is still needed before claiming that the later transformation satisfies `RequiredCoolingEffect-1`; temporal succession or matching labels alone is insufficient.

A selected transformation-flow structure, mathematical graph description, transformation-flow path slice, crossing, or flow valuation is not a functional element or actual transformation by default. When a transformation-flow relation is being used, connect the functional view to the exact `TransformationFlowStructure` through `C.30.TFS-REL`. When a mathematical graph description is being used, connect it through `E.18.2`; when math-lens use is being claimed, connect it through `C.29`. When module allocation is being claimed, connect the functional view to `A.6.M` module-claim repair and the admitted direct allocation/interface owner rather than treating function and module as one kind. Functional ports and module interfaces can both use `U.Signature` discipline, but functional ports govern behavior input and output slots while module interfaces govern substitution, compatibility, boundary, and change-policy claims.

Composability and quality compositionality are separate claims. If the view says parts can be assembled, keep that as a structure claim or use claim. If it says a quality of the whole follows from parts, assign the quality-composition claim to `C.25` and C.16-backed measurement or quality claim.

```text
Composability:
  "A and B can be assembled under interface X."
  recoveredRelationOrRecordKind: ModuleAllocationRelation | InterfaceSpecification
Quality compositionality:
  "The assembled whole preserves safety, latency, or reliability."
  recoveredRelationOrRecordKind: QBundleSlot | structuralCharacteristicQBundleInputSlot | structuralCharacteristicCausalHypothesisForQBundleSlot | structuralCharacteristicEvidenceRelationForQBundleSlot(A.10-governed evidence relation only when evidence provenance is the claim being made)
Non-admissible:
  successful assembly is not quality propagation
```

Compositional formalisms may express explicit composition structures, view relations, and model relations. They do not make required behavior actual, create transformations, or make safety, latency, reliability, or another quality propagate automatically.

#### C.30.ASV:4.7 - Correspondence and source return

Use correspondence records when the view relates functional, flow, control, module-interface, information, runtime, placement, work, evidence, scale, or logical structures. Do not assert cross-view consistency by prose alone.

Correspondence examples:

| Source wording | Recover |
| --- | --- |
| "This function is implemented by that module." | `FunctionToModuleAllocationRef` or the allocation or relation record named by value. |
| "This flow crosses that runtime boundary." | `FlowToRuntimeInteractionCorrespondence`. |
| "This evidence covers the replacement." | `EvidenceReuseToAffectedStructure`; assign sufficiency or verdict to `A.10`, `G.6`, or `B.3`. |
| "This requirement constrains that structure." | `RequirementToStructureConstraint` or a constraint record named by value. |
| "This scale window changes the structure kind." | `ScaleWindowToStructureKindCorrespondence`; assign scale-lens claims to `C.29` when those claims are being made. |

Use `SourceReturnCondition` when compression, extraction, coarsening, evidence reuse, ML evaluation, bounded exception, many-to-many allocation, publication, or decision claim hides a distinction needed for action, assurance, causal use, law-domain review, regulatory review, comparison, or reopening.

If `viewConstruction` is `query`, `extraction`, `coarsening`, `correspondenceSlice`, or `sourceReturnSlice`, and omitted structure changes action, assurance, causal use, law-domain or regulatory review, or subsequent decision reopening, `SourceReturnCondition` is needed.

When the view is used to name affected structures for a next architecture use but no decision record is being used, use C.30 `AffectedArchitectureStructureNote`: affected structure kinds, affected structure refs when known, affected ASV refs, accepted or suspected view loss, source-return condition, and the next admissible use. The note is not an architecture decision, ADR, gate passage, evidence sufficiency, or release authority.

Use the thinnest source or reliance relation that preserves the next architecture move. Use fuller source, evidence, assurance, or claim-kind relation only when the source or reliance relation being used cannot be inspected, used, compared, refreshed, or bounded without it. A `ControlStructureViewNote` may precede full `C.30.LCA` use or proof-governing pattern applications when one control relation and its boundary are enough for the architecture move being made.

Treat source return as a user action, not only a metadata field:

```text
SourceReturnAction:
  returnTo:
    sourceStructure | sourceEpisteme | sourceView | sourceTrace |
    sourceCorpus | sourceModel | sourceEvidence | sourcePublication
  because:
    hiddenRelation | lostConstraint | coarsenedScale |
    ambiguousExtraction | staleEdition | crossViewMismatch |
    lawDomainOrRegulatoryUse | assuranceOrDecisionUse
  nextSourceReturnAction:
    inspect | split | downgradeUse | addCorrespondence |
    openNeighborPattern | stop
```

Do not make source return mandatory for ordinary local recognition when no hidden distinction is being used for action. Do not omit source return when a hidden distinction carries a selected reliance relation, assurance, law-domain, comparison, causal, gate, or decision commitment. The condition is needed only when the repaired text still relies on the hidden source-side distinction.

Model cards, system cards, and evaluation harness reports may publish or substantiate an architecture structural view only when the structural-view claim is recoverable. The view must name the relevant structure kind, such as `RuntimeInteractionStructure`, `InformationDataStructure`, `SecurityTrustBoundaryStructure`, `EvidenceAssuranceStructure`, `ModuleInterfaceStructure`, or another declared structure kind; it must also state intended-use scope, evaluation scope and known loss when evaluation is used, deployment-context mismatch when that mismatch is being claimed, and the evidence or assurance governing pattern when the publication is used beyond transparency. A card or harness is not architecture adequacy, safety proof, or release claim or gate claim by publication alone.

**Currentness and smallest reopen.** When a decisive input changes, reopen only the `ArchitectureStructuralView` locus and use conclusion that depend on it. A changed selected structure or structure kind reopens its exact structure fields and, when another structure becomes the EntityOfConcern, requires a separately identified description episteme; a changed description identity reopens only that episteme's view admission; a changed viewpoint or conformance occurrence reopens only the E.17.0 predicate; changed construction or knowledge state, correspondence, source edition or lost structure reopens the matching provenance, correspondence, source-to-use, hidden/lost-structure, or source-return locus; and a changed admissible-use boundary or direct governor reopens only its dependent use or governed claim. Update that locus, demote the episteme to a structural description or `ArchitectureStructureKindTriage@Project`, narrow use, return to the named source, or stop; unrelated structures, views, and claims stay closed.

#### C.30.ASV:4.8 - Worked slices

**Runtime degradation.** A team says, "The architecture is fine, but incidents happen when failover starts." The first architecture move is to recover runtime interaction, control relation, failover relation, placement, and evidence-assurance structures before turning a dashboard or deployment diagram into proof:

```text
Runtime degradation slice:
  selected structure kinds:
    RuntimeInteractionStructure
    ControlStructure
    InformationDataStructure
    PlacementDeploymentStructure
    EvidenceAssuranceStructure
  first architecture move:
    recover runtime interaction topology, control relation or failover relation,
    state custody, placement relation, locality relation, evidence relation, and observability relation
  nonAdmissibleUse:
    deployment diagram as runtime proof,
    observability dashboard as evidence sufficiency,
    green indicator value as gate authority or release authority
```

Use `C.24` only when tool-use, call planning, call graph, work execution, or budgeted agentic tool-use is the claim being made. Do not absorb those claims into architecture structure.

**CPS or plant architecture.** A plant drawing, P&ID-like publication form, LCA sketch, or safety-case view is not the plant architecture by itself. First recovery can require:

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

**Chiplet or device architecture.** A packaging diagram or interconnect sketch may involve several structure kinds:

```text
Chiplet and device architecture first recovery:
  MaterialSpatialStructure:
    packaging, adjacency, thermal path, energy path
  TransformationFlowStructure:
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
  AllocationResponsibilityStructure:
    responsibility allocation and enactment boundary
  WorkMethodStructure:
    repeatable work method and exception-handling relation
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

**Organization service architecture.** A service organization sketch that shows teams, handoffs, escalation points, and dashboards is not the organization architecture by itself. First recovery can require:

```text
Organization service architecture first recovery:
  describedHolonRef: service organization or service-delivery system
  candidateStructureKindRefs:
    WorkMethodStructure:
      method arrangement, work-plan boundaries, exception handling, and performed-work records
    AllocationResponsibilityStructure:
      role assignments, responsibility split, enactor availability, and escalation relation
    InformationDataStructure:
      ticket state, customer record custody, dashboard source, and source-return condition
    EvidenceAssuranceStructure:
      audit trail, service-level evidence relation, assurance claim, and gate or release record only when those claims are being made
  C30ASVBoundary:
    ASV names selected structure and view boundary; staffing decision, work authority, evidence sufficiency, assurance, and service-quality claims go to their governing patterns
```

**AI agent diagram.** A "planner-memory-tools" diagram is not the agent's architecture by itself. It may start first recovery as a structure-kind set, without minting an AI-domain ontology:

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
    output handling, supply-chain or update channel
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
  C.30.TFS-REL when an E.18 flow relation is being used,
  A.6.M module-relation repair for tool, API, or interface relation claims,
  A.10, G.6, or B.3 when evidence or assurance reliance is being claimed,
  C.24 agentic tool-use relation or call-planning relation, E.16, A.20, or A.21 when tool-call, autonomy, constraint, or gate authority is being claimed
stop condition:
  ASV contains only the structural-view record; evidence sufficiency, assurance, gate, autonomy, and tool-call authority claims are assigned to the governing patterns for those claims
```

Structural AI-agent security is architecture structure when these structure kinds change the next architecture move. When the claim being made is latent representation, decoding, or effect adequacy rather than architecture structure, keep the phrase as a reduced-use source cue until the representation, decode, or effect-adequacy pattern governing that claim carries that claim.

**Generated code-agent relation graph.** A probe JSON or code-agent architecture relation graph can be an architecture structural view publication only after observed, inferred, or unknown observation value, evidence pointers or source pointers, unexplored regions, typed relation semantics, and source-return conditions are present. Belief-state proof and downstream-change safety assurance apply the patterns governing those claims.

**Neural-network block replacement.** Replacing attention, FFN, convolution, SSM, recurrent, memory block or cache block, MoE expert-selection, pruning, distillation, or another block is an architecture move only when the changed structure kind, flow relation, module-interface claim kind, preserved and lost structure, affected characteristic, source relation, and decision or evidence governing pattern are named.

