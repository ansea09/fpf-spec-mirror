---
chunk_kind: "child"
pattern_id: "A.6.M"
pattern_title: "Module Relation Repair"
section_id: "A.6.M:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.M/A.6.M__005_solution.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.6.M — Module Relation Repair"
  - "A.6.M:4 — Solution"
line_start: 18931
line_end: 19125
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.6.5"
  - "A.6.B"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.28"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.RSA"
  - "E.18"
  - "E.20"
  - "G.5"
keywords:
  - "are used only for pattern users"
  - "claims"
  - "component"
  - "conformance items"
  - "evidence records"
  - "interface"
  - "interface specification"
  - "layer"
  - "module relation"
  - "open architecture"
  - "or assurance records. Modeled modules and interfaces are not written as agents with duties"
  - "or publication records"
  - "platform"
  - "port"
  - "records"
  - "stack"
  - "substitutability"
---

### A.6.M:4 - Solution

A.6.M specializes `A.6.P` for module, component, interface, platform, and open-architecture wording when the recovered result is module-interface claim content, an interface specification, platform grammar, substitutability claim, or open-architecture module-interface claim. Stratification or architecture-operation source labels covered by `C.30.STRAT` are governed by `C.30.STRAT` until that repair recovers this module-interface content. A.6.M neither mints root kinds from those labels nor admits a direct module relation from record syntax.

A candidate module is an exact `U.Holon` used in a claim that treats it as a replaceable, reusable, or separately changed structural unit of a larger `U.Holon`, ordinarily under the exact `VP.ModuleInterface` viewpoint episteme. The claim names its boundary, interface specification, admissibility conditions, substitutability policy when replaceability is claimed, and change policy when separate change is claimed. Effective `U.ReferenceScheme` and `U.ClaimScope` qualify the claim; an optional selected model-use structure appears only when its organization changes module meaning. None replaces the two holons or makes a module relation obtain. A `FunctionalElementClaim` is different: it is view-local claim content inside a functional structural-view episteme, not a root kind and not a module relation. It binds required behaviour or effect to bearer or candidate bearer, capability, functional ports, and allocation claims when those claims are current; required or desired content is not an actual `U.Transformation`. The relation between functional and module claims is separately governed allocation or correspondence, not identity. One module candidate can correspond to many functional elements; many module candidates can correspond to one functional element; a functional element can remain unallocated; and a module candidate can be present in a module-interface view with no current functional behaviour in the functional view.

Functional ports and module interfaces may both use `U.Signature` discipline, but they govern different claims. A functional port constrains input condition, output condition, accepted-state, and produced-state slots for a functional behavior or transformation. A module interface constrains boundary, substitutability, compatibility, protocol references, schema references, version policy, change policy, and conformance expectations for a module relation. Do not move a functional-port claim into module-interface structure unless a module-interface or substitution claim is actually being made.

For modular synthesis, A.6.M supplies only the module-interface claim slice. A synthesis action may align required functional claims under `VP.Functional`, transformation-flow topology under `E.18` and `C.30.TFS-REL`, control structure under `C.30.LCA`, procedures and work packages under `VP.Procedural`, and module and interface claims under `VP.ModuleInterface`. `VP.AllocationResponsibility` is only a recognition cue for allocation or responsibility concerns: a positive responsibility claim needs its admitted direct domain predicate, actual participants, applicability, and occurrence identity, or the exact A.6.RCD missing-governor result. Use A.6.M to repair claims about modules and their interfaces; non-module candidate generation, allocation, responsibility, evidence, assurance, decision, Work, and characteristic claims remain with their direct patterns.

#### A.6.M:4.1 - `ModuleInterfaceClaim` record

Use `ModuleInterfaceClaim` only when the light repair note is not enough and durable claim content is needed. Its Plain reading is *claim about a module and its interface in a larger whole*.

The F.18 comparison also covered `ModuleUseClaim`, `ModuleInWholeClaim`, and `ModuleRelationClaim`. The selected pair keeps the claim and interface visible without predicate syntax. `ModuleUseClaim` can suggest operational use, `ModuleInWholeClaim` can suggest a spatial or part-whole predicate, and `ModuleRelationClaim` can suggest that a direct relation has already been admitted. Reopen the naming choice only if the governed content changes or repeated reader error shows that this distinction is still not recoverable.

```text
ModuleInterfaceClaim:
  claimEpistemeRef: U.EpistemeRef
  entityOfConcernRef:
    moduleHolonRef | selectedDependencyStructureRef |
    admittedDirectModuleRelationOccurrenceRef
  effectiveReferenceScheme: U.ReferenceScheme, byValue
  claimScope?: U.ClaimScope, byValue
  modelUseStructureRef?: U.StructureRef
  moduleHolonRef: U.HolonRef
  wholeHolonRef: U.HolonRef
  viewpointRef?: U.ViewpointRef = VP.ModuleInterface
  selectedDependencyStructureRef?: U.StructureRef
  boundaryRef: BoundaryRef
  interfaceSpecificationRef?: U.EpistemeRef constrained to InterfaceSpecification
  interfaceSpecificationGap?: exact missing-specification result
  functionalCorrespondenceRelationRefs?: FinSet(U.RelationRef)
  transformationFlowStructureRefs?: FinSet(U.StructureRef)
  transformationFlowRelationOccurrenceRefs?: FinSet(U.RelationRef)
  mechanismRefs?: FinSet(U.EntityRef constrained by the selected mechanism pattern)
  dependencyRelationOccurrenceRefs?: FinSet(U.RelationRef)
  substitutabilityPolicyRef?: U.EpistemeRef
  changePolicyRef?: U.EpistemeRef
  variabilitySlotRefs?: FinSet(SlotSpecRef)
  evidenceOrSourceRelianceRelationRefs?: FinSet(U.RelationRef)
  directModuleRelationDisposition:
    noDirectRelationClaimed | admittedRelationAndOccurrence | missingGovernor
  admittedRelationKindOrDeclarationRef?:
  obtainingRelationOccurrenceRef?: U.RelationRef
  missingRelationParticipantRefs?:
  proposedPredicate?:
  affectedUse?:
  futureDefinitionNeed?:
  definingPatternLocator?: PatternID used only as a locator
  admissibleUse
  nonAdmissibleUse
```

This form is claim content in one C.2.1 episteme. Its identity uses that content, the one exact `entityOfConcernRef`, and the effective `U.ReferenceScheme`. `claimScope` qualifies the claim when its coverage matters. `modelUseStructureRef` is present only when one independently selected model-use structure changes the meaning of *module* for this claim; it is not a module participant, whole, boundary, or source of relation obtaining. `VP.ModuleInterface` is a reference to the exact viewpoint episteme when viewpoint use matters; citing it does not make this claim a `U.View`. The interface-specification and direct-relation fields obey the same exclusive branches as `ModuleRelationRepairNote`. If `entityOfConcernRef` names an admitted direct module-relation occurrence, the disposition is `admittedRelationAndOccurrence` and `obtainingRelationOccurrenceRef` resolves that same occurrence. Under the other two dispositions, `entityOfConcernRef` stays with the module holon or selected dependency structure.

A `ModuleInterfaceClaim` record, package path, file boundary, graph edge, list position, common name, or publication does not make a world-side module relation obtain. Current A.6.M admits no general direct module relation kind. If repeated engineering use genuinely needs one direct module relation occurrence, first use the applicable subject rule and `A.6.RCD` to recover the exact module and whole participant meanings, obtaining predicate, applicability, recurrence rule, and occurrence-identity rule. Use `A.6.REL` only after that relation is admitted and a later use must distinguish one obtaining occurrence from another. A separately constituted `RelationSignature` may then declare reusable SlotSpecs; neither the signature nor this claim creates the occurrence.

Well-formedness: the claim names both holons, one exact EntityOfConcern, an effective reference scheme, one boundary, and exactly one of an interface-specification reference and an explicit interface-specification gap. Its direct-relation disposition has exactly the fields required by the selected branch. Optional structure, relation, evidence, mechanism, policy, conformance, source, and reliance references are used only when those exact objects and claims are current under their direct rules.

#### A.6.M:4.2 - Interface specification is not a label

A.6.M calls the independently identified specification episteme an `InterfaceSpecification`. It is one `U.Episteme` under C.2.1 whose `EntityOfConcern` is the exact boundary named by the module claim. Its identity is `<exact ClaimGraph, that one EntityOfConcern, effective U.ReferenceScheme>`. Its claim content may include:

```text
InterfaceSpecification claim content:
  signatureRefs?: FinSet(SignatureRef)
  slotSpecSetRefs?: FinSet(SlotSpecSetRef)
  portEndpointSpecRefs?: FinSet(PortEndpointSpecRef)
  protocolRefs?: FinSet(EpistemeRef)
  schemaRefs?: FinSet(EpistemeRef)
  admissibilityConditions
  semanticConditions
  versionPolicyRef?
  changePolicyRef?
  conformanceExpectationRefs?
  evidenceOrSourceRelianceRefs?
  nonAdmissibleUse
```

`interfaceSpecificationRef` is one `U.EpistemeRef` constrained to that specification form. Under the effective reference scheme it resolves one already identified `InterfaceSpecification`; it carries none of the specification content itself. Two spellings or serialized references may resolve the same unchanged specification. Retargeting the reference selects another already identified specification without changing the previous one. Changing identity-bearing specification content, its `EntityOfConcern`, or its effective reference scheme yields another episteme. When no complete specification is established, keep an explicit `interfaceSpecificationGap` rather than a partly filled reference.

A signature declares vocabulary, laws, and applicability. A slot or endpoint record names positions and field structure. A protocol or schema constrains interaction. A mechanism reference can substantiate a realization relation. Evidence relations, source relations, reliance relations, and conformance expectations substantiate reliance only when the corresponding evidence, source-use, assurance, or conformance claim is being made. None of these, alone, is the module interface.

#### A.6.M:4.3 - Repair applications for overloaded words

| Source wording | Governing repair application |
| --- | --- |
| `component` | First recover the claim actually made under `A.14`: for example `ComponentOf`, `ConstituentOf`, `PortionOf`, belonging under the collection's own rule, or `PhaseOf`. Apply A.6.M only when a module-interface relation is being claimed. |
| `module` | Recover a `ModuleInterfaceClaim` or `ModuleRelationRepairNote` over exact `U.Holon` refs under the exact `VP.ModuleInterface` viewpoint episteme when needed. Do not infer a direct relation occurrence; use an admitted direct relation only when its defining rule exists and current facts make its predicate obtain. |
| `functional element` | Keep it as `FunctionalElementClaim` inside a functional structural-view episteme; use `A.6.F` to repair wording and connect it to module-interface structure only through an exact allocation or correspondence relation. Keep required or desired behaviour as claim content. Cite an actual `U.Transformation` only when A.3.4 independently supplies its changed referent, boundary, conditions, actual before/during/after facts, and continuity basis. |
| `work package`, `delivery unit`, or `team boundary` | Keep Work, Method, WorkPlan, exact system-role kind and assignment, and responsibility claims separate. Use `A.15`, `A.2`, and `VP.Procedural` for their own objects; treat `VP.AllocationResponsibility` only as a cue, then cite the direct allocation or responsibility predicate or the exact missing governor. Relate those facts to module-interface structure only through a declared correspondence, allocation, or boundary relation. |
| `deployment scope` or `placement` | Recover a deployment or placement structure under `C.30` or `C.30.ASV` when that deployment or placement structure is being claimed. Relate it to module-interface structure only through declared correspondence or boundary relation. |
| `interface` | Recover the independently identified `InterfaceSpecification` episteme and an `interfaceSpecificationRef` that resolves it, not a wire, API label, port label, E.18 transformation-flow relation, or function by itself. |
| `signature` | Keep as A.6.0 declaration. It is not an implemented interface, mechanism, gate, evidence row, or substitution policy. |
| `port` or `endpoint` | Recover `SlotSpec`, endpoint field, or interface-specification field when the claim is being made. It is not a module, graph edge, transformation-flow crossing, or proof of integration. |
| `functional link` | Keep it as claim content in a functional structural-view episteme; relate it to module claims only through an exact correspondence, allocation, or retargeting relation. |
| `E.18 transformation-flow relation` or `path` | Keep under `E.18` and `C.30.TFS-REL`; it may inform an architecture-to-transformation-flow relation, but it is not an interface specification. |
| `platform` | Recover `PlatformGrammarRef`: extension rules, variability slots, interface specifications, substitution policy, and conformance expectations when platform extension, variation, substitution, or conformance use is being claimed. |
| stratification or architecture-operation source label | Apply `C.30.STRAT` first. Use A.6.M only when the recovered result is a module-interface relation, interface specification, platform grammar, substitutability policy, change policy, or open-architecture module-interface claim. Otherwise apply `C.30.LCA`, `C.30.ASV`, `A.6.F`, `E.18`, `C.16.P`, `C.29`, `C.2.P`, or use ordinary source-label disposition when no FPF-governed claim remains. |
| `open architecture` | Recover an `OpenArchitectureClaim` episteme: published interface specifications, substitution rules, change policy, data-rights or access constraints when those constraints are part of the claim, and exact conformance, evidence, source, or reliance relations only when that stronger reliance claim is being made. |

#### A.6.M:4.4 - First repair sequence

1. Name the phrase and the practical situation.
2. Select the whole holon and candidate module holon.
3. State whether the source phrase is module relation, component relation, function allocation, procedural or work-package relation, exact system-role-assignment occurrence, direct responsibility relation, deployment or placement structure, interface specification, signature, port or endpoint, transformation-flow crossing, mechanism realization, platform grammar, control relation, autonomy-like operation claim, `C.30.STRAT` source-label case, or open-architecture claim.
4. State the boundary and the declared interface specification or explicit interface-specification gap.
5. State the admissibility conditions, substitutability policy, and change policy, or mark any of those fields not established by the repair.
6. State the subject pattern for any non-module claim being made: `C.30`, `C.30.ASV`, `A.6.F`, `A.15`, `A.2`, `E.18`, `C.30.TFS-REL`, `C.31`, `C.31.RSA`, `C.16`, `A.10`, `B.3`, `A.20`, `A.21`, `C.28`, `E.20`, `G.5`, or `C.11`.
7. Stop when the claim, direct-relation disposition, and next use are explicit. Do not open A.6.RCD or A.6.REL unless a named receiving use genuinely needs a reusable direct relation or distinguishable obtaining occurrence.

#### A.6.M:4.5 - Worked slices

**Ports line up.**

```text
Phrase:
  "The ports line up, so the modules are compatible."

ModuleRelationRepairNote:
  wholeHolonRef: VehicleControlSystem
  candidateModuleHolonRef: BrakeControllerPackage
  effectiveReferenceScheme: VehicleControlInterfaceScheme-2026Q2
  claimScope: BrakeControllerReleaseUse-2026Q2
  directModuleRelationDisposition: noDirectRelationClaimed
  boundaryRef: BrakeControlBoundary
  interfaceSpecificationGap: endpoint names are present, but protocol and semantic conditions are still missing
  admissibilityConditions: not yet declared
  substitutabilityPolicyRef: missing
  changePolicyRef: missing
  claimBoundary: interface-spec repair; no evidence or gate claim yet
  notAModuleBecause: port labels alone do not establish implemented interface compatibility
  governedNonModuleClaimPatternRefs: A.6.5 for endpoint slots; A.6.B only if L, A, D, or E boundary-package statement classification is current; A.6.M only if a module-interface or substitution claim remains
  stopCondition: endpoint slots and missing interface-spec fields are visible
```

**Open platform claim.**

```text
Phrase:
  "This is an open platform."

OpenArchitectureClaim:
  architectureClaimRef:
  platformGrammarRef:
  interfaceSpecificationRefs:
  variabilitySlotRefs:
  substitutabilityPolicyRef:
  changePolicyRef:
  conformanceExpectationRefs:
  evidenceOrSourceRelianceRefs?:
  nonAdmissibleUse:
    "open" does not by itself prove substitutability, interoperability,
    assurance, procurement suitability, or architecture quality
```

The first slice repairs the claim without requiring measurement. The second slice applies MOSA-like conformance expectations and substitution policy only for the conformance or substitution claim being made.

Supplier-diversity, procurement suitability, use-context compatibility, business constraint, policy authorization, and provider-selection claims are not module-interface fields. If those claims are being made, A.6.M names only the module-interface slice; non-module selection, procurement, work, role, evidence, assurance, gate, release, and mechanism claims are governed by the patterns named in `A.6.M:12`.

**Team boundary claim.**
```text
Phrase:
  "The team communication boundary matches the module boundary."

ModuleRelationRepairNote:
  wholeHolonRef: PaymentsPlatform
  candidateModuleHolonRef: SettlementService
  effectiveReferenceScheme: PaymentsPlatformInterfaceScheme-2026Q2
  claimScope: SettlementServiceProductLineUse-2026Q2
  directModuleRelationDisposition: noDirectRelationClaimed; team/module correspondence remains diagnostic
  boundaryRef: SettlementServiceBoundary
  interfaceSpecificationGap: the service API exists, but semantic versioning, data schema, and semantic conditions are incomplete
  admissibilityConditions: admitted team-delivery and on-call responsibility predicates obtain for their actual Systems, scopes, and intervals; otherwise record the exact missing governor; substitutability not established
  substitutabilityPolicyRef: missing
  changePolicyRef: missing
  claimBoundary: exact system-role assignment, direct responsibility relation, Work, and procedural correspondence first; module-interface relation only after boundary and interface specification are declared
  notAModuleBecause: team communication boundary and an independently obtaining delivery-responsibility relation do not by themselves establish module interface, substitutability, or compatibility
  governedNonModuleClaimPatternRefs: A.15 and A.2 for team and work claims; C.29 if the team-to-module correspondence is claimed as homomorphism-like or almost-same structure; A.6.M only for the declared module-interface relation
  stopCondition: the correspondence is usable as an architecture diagnostic, not as proof
```

The third slice uses Conway-like mirroring as a diagnostic prompt. It does not make organization structure, communication relations, a system-role assignment, or delivery responsibility into module-interface structure by identity. The responsibility claim remains valid only through its own admitted direct predicate or returns the exact missing governor.

Proxy-cost replay: if a repair proposes more modules, more open interfaces, or more parallel transformation-flow paths, name what may get worse before claiming improvement. Synchronization work, communication overhead, conformance work, shared-resource pressure, hidden exception cost, or cross-boundary change cost can become the claim being made. A.6.M repairs only the module-interface relation; speedup, bottleneck, modularity, measurement, work, and quality tradeoffs are governed by `C.29`, `E.18`, `C.31`, `C.16`, `A.15`, or the related subject pattern named by value when that related claim is being made.

#### A.6.M:4.6 - Lowering and Reopen Conditions

Lower an A.6.M repair to reduced-use cue, quote-only wording, blocked use, or incomplete rewrite when the module-interface relation, interface specification, admissibility conditions, substitutability policy, or change policy cannot be stated by value.

Reopen the repair when any of these change: the whole holon, candidate module holon, boundary, interface specification, explicit interface gap, substitutability policy, change policy, platform grammar, conformance expectation, relied-on evidence relation, relied-on source relation, source-label recovery from `C.30.STRAT`, team-boundary correspondence, work correspondence, or the subject pattern for a related claim being made.

If the reopened material is no longer a module-interface relation, A.6.M keeps only the previous repair as source context and the claim being made is governed by the pattern named in `A.6.M:12`.

