---
chunk_kind: "child"
pattern_id: "A.6.M"
pattern_title: "Module Relation Repair"
section_id: "A.6.M:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.M/A.6.M__005_solution.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "A.6.M — Module Relation Repair"
  - "A.6.M:4 — Solution"
line_start: 14683
line_end: 14839
dependencies:
keywords:
  - "are used only for pattern users"
  - "claims"
  - "conformance items"
  - "evidence records"
  - "or assurance records. Modeled modules and interfaces are not written as agents with duties"
  - "or publication records"
  - "records"
---

### A.6.M:4 - Solution

A.6.M specializes `A.6.P` for module, component, interface, platform, and open-architecture wording when the recovered result is a module-interface relation, interface specification, platform grammar, substitutability relation, or open-architecture module-interface claim. Stratification or architecture-operation source labels covered by `C.30.STRAT` are governed by `C.30.STRAT` until that repair recovers a module-interface relation; A.6.M applies only to that recovered module-interface result. A.6.M does not mint root kinds from those source labels.

A module is a `U.Holon` viewed in a declared bounded context as a replaceable, reusable, or separately changed structural unit of a larger `U.Holon` under `VP.ModuleInterface`, with explicit boundary, interface specification, admissibility conditions, and admissible substitution or change policy.

For modular synthesis, A.6.M supplies only the module-interface slice. A synthesis move may align required functions or functional-service claims under `VP.Functional`, flow or transduction topology under `E.TGA`, control structure under `C.30.LCA`, procedures and work packages under `VP.Procedural`, role enactors under `VP.RoleEnactor`, and modules or interfaces under `VP.ModuleInterface`; A.6.M repairs the module-interface relation, while non-module candidate generation, evidence, assurance, decision, work, and characteristic claims are governed by the patterns named in `A.6.M:12` when those claims are being made.

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
  tgaFlowRefs?: FinSet(PathSliceId | TransferRef | CrossingRef),
  mechanismRefs?: FinSet(MechanismRef),
  dependencyRefs?: FinSet(QualifiedRelationRecordRef),
  substitutabilityPolicyRef?: EpistemeRef,
  variabilitySlotRefs?: FinSet(SlotRef),
  evidencePathRefs?: FinSet(EvidencePathRef),
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
  protocolOrSchemaRefs?: FinSet(EpistemeRef)
  admissibilityConditions:
  semanticConditions:
  versionOrChangePolicyRef?:
  conformanceExpectationRefs?:
  evidencePathRefs?:
  nonAdmissibleUse:
```

A signature declares vocabulary, laws, and applicability. A slot or endpoint record names positions and field structure. A protocol or schema constrains interaction. A mechanism reference can substantiate a realization relation. Evidence paths and conformance expectations can substantiate reliance only when an evidence path named by value or an assurance claim is being made. None of these, alone, is the module interface.

#### A.6.M:4.3 - Repair applications for overloaded words

| Source wording | Governing repair application |
| --- | --- |
| `component` | First recover an `A.14` relation such as `ComponentOf`, `ConstituentOf`, `PortionOf`, `MemberOf`, or `PhaseOf`. Apply A.6.M only when a module-interface relation is being claimed. |
| `module` | Recover `moduleIn(...)` or `ModuleRelationRepairNote` over `U.Holon` refs under `VP.ModuleInterface`. |
| `functional element` | Keep under `VP.Functional`, `A.6.F`, or `FunctionalStructureView@Context`; connect to module-interface structure only through correspondence or allocation. |
| `work package`, `delivery unit`, or `team boundary` | Keep work, method, work-plan, role-assignment, role, and enactor claims with `A.15`, `A.2`, `VP.Procedural`, or `VP.RoleEnactor` when the wording asserts those claim kinds. Relate them to module-interface structure only through declared correspondence, allocation, or boundary relation. |
| `deployment scope` or `placement` | Recover a deployment or placement structure under `C.30` or `C.30.ASV` when that deployment or placement structure is being claimed. Relate it to module-interface structure only through declared correspondence or boundary relation. |
| `interface` | Recover `InterfaceSpecificationRef`, not a wire, API label, port label, E.18 transduction relation, or function by itself. |
| `signature` | Keep as A.6.0 declaration. It is not an implemented interface, mechanism, gate, evidence row, or substitution policy. |
| `port` or `endpoint` | Recover `SlotSpec`, endpoint field, or interface-specification field when the claim is being made. It is not a module, graph edge, TGA crossing, or proof of integration. |
| `functional link` | Keep under `VP.Functional` or `FunctionalStructureView@Context`; relate to modules only through declared correspondence, allocation, or retargeting. |
| `E.18 transduction relation` or `path` | Keep under `E.18` and `C.30.TGA-FLOW-REL`; it may inform an architecture-flow description, but it is not an interface specification. |
| `platform` | Recover `PlatformGrammarRef`: extension rules, variability slots, interface specifications, substitution policy, and conformance expectations when platform extension, variation, substitution, or conformance use is being claimed. |
| stratification or architecture-operation source label | Apply `C.30.STRAT` first. Use A.6.M only when the recovered result is a module-interface relation, interface specification, platform grammar, substitution or change policy, or open-architecture module-interface claim. Otherwise apply `C.30.LCA`, `C.30.ASV`, `A.6.F`, `E.18`, `C.16.P`, `C.29`, `C.2.P`, or use ordinary source-label disposition when no FPF-governed claim remains. |
| `open architecture` | Recover `OpenArchitectureClaim@Context`: published interface specifications, substitution rules, change policy, data-rights or access constraints when those constraints are part of the open-architecture claim, and conformance expectations or evidence paths when reliance is being claimed. |

#### A.6.M:4.4 - First repair sequence

1. Name the phrase and the practical situation.
2. Select the whole holon and candidate module holon.
3. State whether the source phrase is module relation, component relation, function allocation, procedural or work-package relation, role or enactor relation, deployment or placement structure, interface specification, signature, port or endpoint, TGA flow crossing, mechanism realization, platform grammar, control relation, autonomy-like operation claim, `C.30.STRAT` source-label case, or open-architecture claim.
4. State the boundary and the declared interface specification or explicit interface-specification gap.
5. State the admissibility conditions and substitution or change policy, or mark them not established by the repair.
6. State the governing pattern for any non-module claim being made: `C.30`, `C.30.ASV`, `A.6.F`, `A.15`, `A.2`, `E.18`, `C.30.TGA-FLOW-REL`, `C.31`, `C.31.RSA`, `C.16`, `A.10`, `B.3`, `A.20`, `A.21`, `C.28`, `E.20`, `G.5`, or `C.11`.
7. Stop when the relation and next move are explicit.

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
  substitutionOrChangePolicyRef: missing
  claimBoundary: interface-spec repair; no evidence or gate claim yet
  notAModuleBecause: port labels alone do not establish implemented interface compatibility
  governedNonModuleClaimPatternRefs: A.6.5, A.6.B, then A.6.M only if a substitution claim remains
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
  substitutionOrChangePolicyRef:
  conformanceExpectationRefs:
  evidencePathRefs?:
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
  substitutionOrChangePolicyRef: missing
  claimBoundary: role, enactor, work, and procedural correspondence first; module-interface relation only after boundary and interface specification are declared
  notAModuleBecause: team communication boundary and delivery responsibility do not by themselves establish module interface, substitutability, or compatibility
  governedNonModuleClaimPatternRefs: A.15 and A.2 for team and work claims; C.29 if the team/module correspondence is claimed as homomorphism-like or almost-same structure; A.6.M only for the declared module-interface relation
  stopCondition: the correspondence is usable as an architecture diagnostic, not as proof
```

The third slice uses Conway-like mirroring as a diagnostic prompt. It does not make organization structure, communication relations, or delivery responsibility into module-interface structure by identity.

Proxy-cost replay: if a repair proposes more modules, more open interfaces, or more parallel paths, name what may get worse before claiming improvement. Synchronization work, communication overhead, conformance work, shared-resource pressure, hidden exception cost, or cross-boundary change cost can become the claim being made. A.6.M repairs only the module-interface relation; speedup, bottleneck, modularity, measurement, work, and quality tradeoffs are governed by `C.29`, `E.18`, `C.31`, `C.16`, `A.15`, or the related governing pattern named by value when that related claim is being made.

#### A.6.M:4.6 - Lowering and Reopen Conditions

Lower an A.6.M repair to reduced-use cue, quote-only wording, blocked use, or incomplete rewrite when the module-interface relation, interface specification, admissibility conditions, or substitution or change policy cannot be stated by value.

Reopen the repair when any of these change: the whole holon or candidate module holon, the boundary, the interface specification or explicit gap, the substitution or change policy, the platform grammar, the conformance expectation, the evidence path relied on, the source-label recovery from `C.30.STRAT`, the team-boundary or work correspondence, or the governing pattern for a related claim being made.

If the reopened material is no longer a module-interface relation, A.6.M keeps only the previous repair as source context and the claim being made is governed by the pattern named in `A.6.M:12`.

