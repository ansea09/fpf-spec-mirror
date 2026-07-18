---
chunk_kind: "child"
pattern_id: "A.6.M"
pattern_title: "Module Relation Repair"
section_id: "A.6.M:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.M/A.6.M__005_solution.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "A.6.M — Module Relation Repair"
  - "A.6.M:4 — Solution"
line_start: 16661
line_end: 16825
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

A.6.M specializes `A.6.P` for module, component, interface, platform, and open-architecture wording when the recovered result is a module-interface relation, interface specification, platform grammar, substitutability relation, or open-architecture module-interface claim. Stratification or architecture-operation source labels covered by `C.30.STRAT` are governed by `C.30.STRAT` until that repair recovers a module-interface relation; A.6.M applies only to that recovered module-interface result. A.6.M does not mint root kinds from those source labels.

A module is a `U.Holon` viewed in a declared bounded context as a replaceable, reusable, or separately changed structural unit of a larger `U.Holon` under `VP.ModuleInterface`, with explicit boundary, interface specification, admissibility conditions, substitutability policy when replaceability is claimed, and change policy when separate change is claimed. A functional element is different: `FunctionalElement@Context` is a view-local functional-structure record inside `FunctionalStructureView@Context`, not a root kind and not a module-interface value. It binds required behavior to bearer, capability, functional ports, and allocation when those claims are current. The relation between functional element and module is allocation or correspondence by default, not identity. One module can realize many functional elements; many modules can realize one functional element; a functional element can be abstract before allocation; and a module can be present in a module-interface view with no current functional behavior in the functional view.

Functional ports and module interfaces may both use `U.Signature` discipline, but they govern different claims. A functional port constrains input condition, output condition, accepted-state, and produced-state slots for a functional behavior or transformation. A module interface constrains boundary, substitutability, compatibility, protocol references, schema references, version policy, change policy, and conformance expectations for a module relation. Do not move a functional-port claim into module-interface structure unless a module-interface or substitution claim is actually being made.

For modular synthesis, A.6.M supplies only the module-interface slice. A synthesis action may align required functions or functional-service claims under `VP.Functional`, transformation-flow topology under `E.18` and `C.30.TFS-REL`, control structure under `C.30.LCA`, procedures and work packages under `VP.Procedural`, allocation and responsibility claims under `VP.AllocationResponsibility`, and modules or interfaces under `VP.ModuleInterface`; A.6.M repairs the module-interface relation, while non-module candidate generation, evidence, assurance, decision, work, and characteristic claims are governed by the patterns named in `A.6.M:12` when those claims are being made.

#### A.6.M:4.1 - `moduleIn(...)` relation record
Use `moduleIn(...)` only when the light repair note is not enough:

```text
moduleIn(
  moduleHolonRef: U.HolonRef,
  wholeHolonRef: U.HolonRef,
  boundedContextRef: U.BoundedContextRef,
  viewpointRef: U.ViewpointRef = VP.ModuleInterface,
  boundaryRef: BoundaryRef,
  interfaceSpecRef: InterfaceSpecificationRef,
  functionalCorrespondenceRefs?: FinSet(CorrespondenceRef | KindBridgeRef),
  transformationFlowRelationRefs?: FinSet(PathSliceId | TransferRef | CrossingRef),
  mechanismRefs?: FinSet(MechanismRef),
  dependencyRefs?: FinSet(QualifiedRelationRecordRef),
  substitutabilityPolicyRef?: EpistemeRef,
  changePolicyRef?: EpistemeRef,
  variabilitySlotRefs?: FinSet(SlotRef),
  evidenceOrSourceRelianceRefs?: FinSet(EvidenceRef | SourceRelationRef | RelianceRelationRef),
  admissibleUse,
  nonAdmissibleUse
)
```

Well-formedness: the relation names both holons, one bounded context, one module-interface viewpoint, one boundary, and an interface specification or explicit interface-specification gap. Optional evidence, mechanism, and policy fields are used only when the corresponding evidence, mechanism, policy, conformance, or reliance claim is being made.

#### A.6.M:4.2 - Interface specification is not a label

`InterfaceSpecificationRef` is the local specification reference for an interface specification. It may include:

```text
InterfaceSpecificationRef:
  signatureRefs?: FinSet(SignatureRef)
  slotSpecSetRefs?: FinSet(SlotSpecSetRef)
  portEndpointSpecRefs?: FinSet(PortEndpointSpecRef)
  protocolRefs?: FinSet(EpistemeRef)
  schemaRefs?: FinSet(EpistemeRef)
  admissibilityConditions:
  semanticConditions:
  versionPolicyRef?:
  changePolicyRef?:
  conformanceExpectationRefs?:
  evidenceOrSourceRelianceRefs?:
  nonAdmissibleUse:
```

A signature declares vocabulary, laws, and applicability. A slot or endpoint record names positions and field structure. A protocol or schema constrains interaction. A mechanism reference can substantiate a realization relation. Evidence relations, source relations, reliance relations, and conformance expectations substantiate reliance only when the corresponding evidence, source-use, assurance, or conformance claim is being made. None of these, alone, is the module interface.

#### A.6.M:4.3 - Repair applications for overloaded words

| Source wording | Governing repair application |
| --- | --- |
| `component` | First recover an `A.14` relation such as `ComponentOf`, `ConstituentOf`, `PortionOf`, `MemberOf`, or `PhaseOf`. Apply A.6.M only when a module-interface relation is being claimed. |
| `module` | Recover `moduleIn(...)` or `ModuleRelationRepairNote` over `U.Holon` refs under `VP.ModuleInterface`. |
| `functional element` | Keep as `FunctionalElement@Context` inside `FunctionalStructureView@Context`; use `A.6.F` to repair wording and connect to module-interface structure only through correspondence or allocation. Allow many-to-many allocation: one module may realize many functional elements, many modules may realize one functional element, a functional element may be abstract before allocation, and a module may have no current functional behavior in the view. |
| `work package`, `delivery unit`, or `team boundary` | Keep work, method, work-plan, role-assignment, role, and responsibility claims with `A.15`, `A.2`, `VP.Procedural`, or `VP.AllocationResponsibility` when the wording asserts those claim kinds. Relate them to module-interface structure only through declared correspondence, allocation, or boundary relation. |
| `deployment scope` or `placement` | Recover a deployment or placement structure under `C.30` or `C.30.ASV` when that deployment or placement structure is being claimed. Relate it to module-interface structure only through declared correspondence or boundary relation. |
| `interface` | Recover `InterfaceSpecificationRef`, not a wire, API label, port label, E.18 transformation-flow relation, or function by itself. |
| `signature` | Keep as A.6.0 declaration. It is not an implemented interface, mechanism, gate, evidence row, or substitution policy. |
| `port` or `endpoint` | Recover `SlotSpec`, endpoint field, or interface-specification field when the claim is being made. It is not a module, graph edge, transformation-flow crossing, or proof of integration. |
| `functional link` | Keep under `VP.Functional` or `FunctionalStructureView@Context`; relate to modules only through declared correspondence, allocation, or retargeting. |
| `E.18 transformation-flow relation` or `path` | Keep under `E.18` and `C.30.TFS-REL`; it may inform an architecture-to-transformation-flow relation, but it is not an interface specification. |
| `platform` | Recover `PlatformGrammarRef`: extension rules, variability slots, interface specifications, substitution policy, and conformance expectations when platform extension, variation, substitution, or conformance use is being claimed. |
| stratification or architecture-operation source label | Apply `C.30.STRAT` first. Use A.6.M only when the recovered result is a module-interface relation, interface specification, platform grammar, substitutability policy, change policy, or open-architecture module-interface claim. Otherwise apply `C.30.LCA`, `C.30.ASV`, `A.6.F`, `E.18`, `C.16.P`, `C.29`, `C.2.P`, or use ordinary source-label disposition when no FPF-governed claim remains. |
| `open architecture` | Recover `OpenArchitectureClaim@Context`: published interface specifications, substitution rules, change policy, data-rights or access constraints when those constraints are part of the open-architecture claim, and conformance expectations or evidence, source, or reliance relations when reliance is being claimed. |

#### A.6.M:4.4 - First repair sequence

1. Name the phrase and the practical situation.
2. Select the whole holon and candidate module holon.
3. State whether the source phrase is module relation, component relation, function allocation, procedural or work-package relation, role-assignment or responsibility relation, deployment or placement structure, interface specification, signature, port or endpoint, transformation-flow crossing, mechanism realization, platform grammar, control relation, autonomy-like operation claim, `C.30.STRAT` source-label case, or open-architecture claim.
4. State the boundary and the declared interface specification or explicit interface-specification gap.
5. State the admissibility conditions, substitutability policy, and change policy, or mark any of those fields not established by the repair.
6. State the governing pattern for any non-module claim being made: `C.30`, `C.30.ASV`, `A.6.F`, `A.15`, `A.2`, `E.18`, `C.30.TFS-REL`, `C.31`, `C.31.RSA`, `C.16`, `A.10`, `B.3`, `A.20`, `A.21`, `C.28`, `E.20`, `G.5`, or `C.11`.
7. Stop when the relation and next use are explicit.

#### A.6.M:4.5 - Worked slices

**Ports line up.**

```text
Phrase:
  "The ports line up, so the modules are compatible."

ModuleRelationRepairNote:
  wholeHolonRef: VehicleControlSystem
  candidateModuleHolonRef: BrakeControllerPackage
  boundedContextRef: Release-2026Q2
  boundaryRef: BrakeControlBoundary
  interfaceSpecificationRef or gap: endpoint names present; protocol and semantic conditions missing
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

OpenArchitectureClaim@Context:
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
  boundedContextRef: ProductLine-2026Q2
  boundaryRef: SettlementServiceBoundary
  interfaceSpecificationRef or gap: service API exists; semantic versioning, data schema, and semantic-constraint conditions incomplete
  admissibilityConditions: team delivery responsibility and on-call responsibility declared; substitutability not established
  substitutabilityPolicyRef: missing
  changePolicyRef: missing
  claimBoundary: role-assignment, responsibility, work, and procedural correspondence first; module-interface relation only after boundary and interface specification are declared
  notAModuleBecause: team communication boundary and delivery responsibility do not by themselves establish module interface, substitutability, or compatibility
  governedNonModuleClaimPatternRefs: A.15 and A.2 for team and work claims; C.29 if the team-to-module correspondence is claimed as homomorphism-like or almost-same structure; A.6.M only for the declared module-interface relation
  stopCondition: the correspondence is usable as an architecture diagnostic, not as proof
```

The third slice uses Conway-like mirroring as a diagnostic prompt. It does not make organization structure, communication relations, or delivery responsibility into module-interface structure by identity.

Proxy-cost replay: if a repair proposes more modules, more open interfaces, or more parallel transformation-flow paths, name what may get worse before claiming improvement. Synchronization work, communication overhead, conformance work, shared-resource pressure, hidden exception cost, or cross-boundary change cost can become the claim being made. A.6.M repairs only the module-interface relation; speedup, bottleneck, modularity, measurement, work, and quality tradeoffs are governed by `C.29`, `E.18`, `C.31`, `C.16`, `A.15`, or the related governing pattern named by value when that related claim is being made.

#### A.6.M:4.6 - Lowering and Reopen Conditions

Lower an A.6.M repair to reduced-use cue, quote-only wording, blocked use, or incomplete rewrite when the module-interface relation, interface specification, admissibility conditions, substitutability policy, or change policy cannot be stated by value.

Reopen the repair when any of these change: the whole holon, candidate module holon, boundary, interface specification, explicit interface gap, substitutability policy, change policy, platform grammar, conformance expectation, relied-on evidence relation, relied-on source relation, source-label recovery from `C.30.STRAT`, team-boundary correspondence, work correspondence, or the governing pattern for a related claim being made.

If the reopened material is no longer a module-interface relation, A.6.M keeps only the previous repair as source context and the claim being made is governed by the pattern named in `A.6.M:12`.

