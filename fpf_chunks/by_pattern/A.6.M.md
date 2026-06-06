---
chunk_kind: "parent"
pattern_id: "A.6.M"
pattern_title: "Module Relation Repair"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/A.6.M.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "A.6.M — Module Relation Repair"
line_start: 13746
line_end: 14066
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
  - "C.30.TGA-FLOW-REL"
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

## A.6.M - Module Relation Repair

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### A.6.M:1 - Problem frame

Use this pattern when an architecture or engineering text says "module", "component", "interface", "port", "platform", or "open architecture", and the phrase is doing more than ordinary orientation. If a source label such as "layer" or "stack" is doing the work, apply `C.30.STRAT` first; A.6.M receives the case only when the recovered result is a module-interface relation. Open A.6.M when the live question is whether one holon is being treated as a replaceable, reusable, or separately changed structural unit of a larger holon under a declared module-interface viewpoint.

The first useful move is `ModuleRelationRepairNote`:

```text
ModuleRelationRepairNote:
  wholeHolonRef:
  candidateModuleHolonRef:
  boundedContextRef:
  moduleInterfaceViewpointRef: VP.ModuleInterface
  boundaryRef:
  interfaceSpecificationRef or interfaceSpecificationGap:
  admissibilityConditions:
  substitutionOrChangePolicyRef:
  liveClaimBoundary:
  notAModuleBecause:
  nextGoverningPatternRef:
  stopCondition:
```

Ordinary use stops when the whole, candidate module, boundary, interface specification, admissibility conditions, substitution or change policy, blocked false interpretation, and neighboring work, procedural, role, or enactor exit are clear enough to choose the next architecture move. Open the fuller `moduleIn(...)` relation record only when substitutability, conformance, publication, evidence, assurance, change policy, repeated reuse, or cross-team coordination is live.

What goes wrong if A.6.M is missed: a functional link becomes a module interface; a signature becomes an implemented interface; a port label becomes proof of integration; "open" becomes a decoration; a platform label hides the actual extension rules; a source word such as "layer" or "stack" bypasses `C.30.STRAT` and mints a false local kind; autonomy-like wording is confused with separate module change policy; and a module diagram starts carrying claims that belong elsewhere.

What A.6.M buys in practice: the practitioner can repair one module or interface phrase into a module-relation record, see which exact FPF governing pattern carries any remaining non-module claim, and stop before opening full measurement, evidence, or mechanism-suite records.

Not this pattern when the live question is the general architecture claim, selected architecture structure kind, structural view, stratification wording or source-label recovery, function wording, procedural or work-package wording, role or enactor wording, autonomous operation, independent acting, unsupervised decision or action, measurement, modularity characterization, or reusable-structure residue. Use `C.30`, `C.30.ASV`, `C.30.STRAT`, `A.6.F`, `A.15`, `A.2`, `E.16`, `C.31`, `C.16`, or `C.31.RSA` as appropriate. For any other live claim, apply the exact FPF governing pattern and keep A.6.M only for the module-relation and interface-specification portion.

**E.10.ARCH relation.** A.6.M is the receiving precision-restoration pattern for module-interface relation wording, interface-specification wording, platform-grammar wording, substitutability wording, and open-architecture module-interface claims. `E.10`, `E.10.ARCH`, or `C.30.STRAT` sends wording here only after the recovered result is a module-interface relation, interface specification, platform grammar, substitution or change policy, or open-architecture module-interface claim. If the source wording is still a structure-source label such as `block`, `layer`, `stack`, `expert`, `router`, or `cache`, apply `C.30.STRAT` first. If the live claim is functional architecture, TGA flow, component relation, work, role or enactor relation, autonomy, characteristic, evidence, assurance, gate, decision, or mathematical correspondence, use the exact receiving pattern and keep A.6.M only for the module-interface slice when that slice remains live.

### A.6.M:2 - Problem

Engineering teams use module language for several different things:

- a component in a part-whole decomposition;
- a replaceable unit under a declared interface;
- a functional element;
- a software package, neural-network block, hardware board, chiplet, subsystem, service, team boundary, or delivery unit;
- a published API, protocol, signature, port, connector, or endpoint;
- a platform extension point;
- a control relation, deployment scope, or source label such as layer or stack that still needs `C.30.STRAT` recovery;
- an open-architecture claim.

These are useful ordinary words, but they cannot carry the same FPF claim. A module claim is not created by a label. A conforming module-interface claim states how a candidate `U.Holon` relates to a larger `U.Holon` under `VP.ModuleInterface`: boundary, interface specification, admissibility conditions, substitution or change policy, and any live evidence, conformance, or admissible-use expectation.

The practical question is: does this phrase name a module relation, a component relation, a functional allocation, a procedural or work-package relation, a role or enactor relation, a deployment or placement structure, an interface specification, a signature declaration, a port or endpoint slot, a TGA flow crossing, a mechanism realization, a platform grammar, a control relation, an autonomy-like operation claim, a source label that must first go to `C.30.STRAT`, or only plain source wording?

### A.6.M:3 - Forces

| Force | Tension |
| --- | --- |
| Engineering convenience vs relation precision | Practitioners need short words such as module and interface, but claim-bearing use must recover relation kind, slots, boundary, and admissible use. |
| Module role vs root kind | A module is often a holon in a module-interface role; minting `U.Module` would hide context, viewpoint, and relation conditions. |
| Interface label vs interface specification | An API name, port label, connector label, or signature may substantiate an interface claim, but it is not by itself substitutability or conformance. |
| Function-flow-module proximity vs false identity | Functions, E.18 flow relations, control relations, mechanisms, and module interfaces often meet at the same artifact, but each has a different governing pattern. |
| Open architecture payoff vs open label overread | MOSA and open-system practice make open interfaces useful only with standards, conformance expectations, replacement or change policy, and data or access constraints where live. |
| Team boundary vs module boundary | Conway's law and mirroring practice make team communication boundaries and delivery-responsibility scopes architecture-relevant, but they do not turn a team boundary, delivery unit, or role/enactor arrangement into a module interface by identity. |
| Parallel decomposition vs serial bottleneck | Amdahl-style reasoning makes serial work, synchronization, communication overhead, and shared resource limits visible; more modules, teams, or parallel paths do not automatically improve throughput or evolvability. |
| Cheap repair vs full evidence pack | Most cases need a relation repair note, not a full conformance, evidence, assurance, gate, or mechanism-suite record. |

### A.6.M:4 - Solution

A.6.M specializes `A.6.P` for module, component, interface, platform, and open-architecture wording when the recovered result is a module-interface relation, interface specification, platform grammar, substitutability relation, or open-architecture module-interface claim. Source labels such as `layer` and `stack` go through `C.30.STRAT` first and return here only when that repair recovers a module-interface relation. A.6.M does not mint `U.Module`, `U.Interface`, `U.Platform`, `U.Layer`, or `U.Stack`.

A module is a `U.Holon` viewed in a declared bounded context as a replaceable, reusable, or separately changed structural unit of a larger `U.Holon` under `VP.ModuleInterface`, with explicit boundary, interface specification, admissibility conditions, and admissible substitution or change policy.

For modular synthesis, A.6.M supplies only the module-interface slice. A synthesis move may align required functions or functional-service claims under `VP.Functional`, flow or transduction topology under `E.TGA`, control structure under `C.30.LCA`, procedures and work packages under `VP.Procedural`, role enactors under `VP.RoleEnactor`, and modules or interfaces under `VP.ModuleInterface`; A.6.M repairs the module-interface relation and then exits to the neighboring pattern that carries candidate generation, evidence, assurance, decision, work, or characteristic selection.

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

Well-formedness: the relation names both holons, one bounded context, one module-interface viewpoint, one boundary, and an interface specification or explicit interface-specification gap. Optional evidence, mechanism, and policy fields activate only when their exact claim is live.

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

A signature declares vocabulary, laws, and applicability. A slot or endpoint record names positions and field structure. A protocol or schema constrains interaction. A mechanism reference can substantiate a realization relation. Evidence paths and conformance expectations can substantiate reliance only when their exact evidence or assurance claim is live. None of these, alone, is the module interface.

#### A.6.M:4.3 - Repair applications for overloaded words

| Source wording | Governing repair application |
| --- | --- |
| `component` | First recover an `A.14` relation such as `ComponentOf`, `ConstituentOf`, `PortionOf`, `MemberOf`, or `PhaseOf`. Apply A.6.M only when a module-interface role is live. |
| `module` | Recover `moduleIn(...)` or `ModuleRelationRepairNote` over `U.Holon` refs under `VP.ModuleInterface`. |
| `functional element` | Keep under `VP.Functional`, `A.6.F`, or `FunctionalStructureView@Context`; connect to module-interface structure only through correspondence or allocation. |
| `work package`, `delivery unit`, or `team boundary` | Keep work, method, work-plan, role-assignment, role claims, and enactor claims with `A.15`, `A.2`, `VP.Procedural`, or `VP.RoleEnactor` as live. Relate them to module-interface structure only through declared correspondence, allocation, or boundary relation. |
| `deployment scope` or `placement` | Recover a deployment or placement structure under `C.30` or `C.30.ASV` when the structure is live. Relate it to module-interface structure only through declared correspondence or boundary relation. |
| `interface` | Recover `InterfaceSpecificationRef`, not a wire, API label, port label, E.18 transduction relation, or function by itself. |
| `signature` | Keep as A.6.0 declaration. It is not an implemented interface, mechanism, gate, evidence row, or substitution policy. |
| `port` or `endpoint` | Recover `SlotSpec`, endpoint field, or interface-specification field when the claim is live. It is not a module, graph edge, TGA crossing, or proof of integration. |
| `functional link` | Keep under `VP.Functional` or `FunctionalStructureView@Context`; relate to modules only through declared correspondence, allocation, or retargeting. |
| `E.18 transduction relation` or `path` | Keep under `E.18` and `C.30.TGA-FLOW-REL`; it may inform an architecture-flow description, but it is not an interface specification. |
| `platform` | Recover `PlatformGrammarRef`: extension rules, variability slots, interface specifications, substitution policy, and conformance expectations where live. |
| `layer` or `stack` source label | Apply `C.30.STRAT` first. Return to A.6.M only when the recovered result is a module-interface relation, interface specification, platform grammar, substitution or change policy, or open-architecture module-interface claim. Otherwise use `C.30.LCA`, `C.30.ASV`, `A.6.F`, `E.18`, `C.16.P`, `C.29`, `C.2.P`, or ordinary source-label disposition as live. |
| `open architecture` | Recover `OpenArchitectureClaim@Context`: published interface specifications, substitution rules, change policy, data-rights or access constraints where live, and conformance expectations or evidence paths where relied on. |

#### A.6.M:4.4 - First repair sequence

1. Name the phrase and the practical situation.
2. Select the whole holon and candidate module holon.
3. State whether the source phrase is module relation, component relation, function allocation, procedural or work-package relation, role or enactor relation, deployment or placement structure, interface specification, signature, port or endpoint, TGA flow crossing, mechanism realization, platform grammar, control relation, autonomy-like operation claim, `C.30.STRAT` source-label case, or open-architecture claim.
4. State the boundary and the current interface specification or gap.
5. State the admissibility conditions and substitution or change policy, or mark them not established by the repair.
6. State the next governing pattern for any live non-module claim: `C.30`, `C.30.ASV`, `A.6.F`, `A.15`, `A.2`, `E.18`, `C.30.TGA-FLOW-REL`, `C.31`, `C.31.RSA`, `C.16`, `A.10`, `B.3`, `A.20`, `A.21`, `C.28`, `E.20`, `G.5`, or `C.11`.
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
  liveClaimBoundary: interface-spec repair; no evidence or gate claim yet
  notAModuleBecause: port labels alone do not establish implemented interface compatibility
  nextGoverningPatternRef: A.6.5, A.6.B, then A.6.M if substitution remains live
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

The first slice repairs the claim without opening measurement. The second slice applies MOSA-like conformance expectations and substitution policy only where those claims are live.

Supplier-diversity, procurement suitability, use-context compatibility, business constraint, policy authorization, and provider-selection claims are not module-interface fields. If they are live, A.6.M names the module-interface slice and exits: supplier-set or provider-choice use goes to `G.5` or `C.11`; procurement work, procedural, role, or enactor claims go to `A.15`, `A.2`, `VP.Procedural`, or `VP.RoleEnactor`; evidence, assurance, gate, release, and mechanism claims go to `A.10`, `B.3`, `A.20`, `A.21`, or `E.20` as live.

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
  liveClaimBoundary: role, enactor, work, and procedural correspondence first; module-interface relation only after boundary and interface specification are declared
  notAModuleBecause: team communication boundary and delivery responsibility do not by themselves establish module interface, substitutability, or compatibility
  nextGoverningPatternRef: A.15 and A.2 for team and work claims; C.29 if homomorphism-like correspondence carries the live mathematical-lens claim; A.6.M only for the declared module-interface relation
  stopCondition: the correspondence is usable as an architecture diagnostic, not as proof
```

The third slice uses Conway-like mirroring as a diagnostic prompt. It does not make organization structure, communication relations, or delivery responsibility into module-interface structure by identity.

### A.6.M:5 - Archetypal Grounding

**Tell.** A module is not a little box. It is a holon related to a larger holon under a declared boundary, interface specification, admissibility conditions, and substitution or change policy.

**Show.** A software package, neural-network block, chiplet, power converter, document template, or organizational unit can become module-like in a project only when the relation record says what whole it belongs to, what boundary it offers, what interface specification governs use, and what substitution or change policy makes replacement admissible.

**Show.** A port label, API endpoint or route label, flow edge, or function name may be a useful clue. It can substantiate a module-interface claim only after the relevant signature, slot, protocol, semantic condition, correspondence, mechanism, and exact evidence, conformance, source relation, or reliance relation are declared.

Holon and episteme: the candidate module and whole are described holons under a module relation; they may be systems, epistemes, methods, organizations, publication families, or other structured holons. The module relation, interface specification, platform grammar, and open-architecture claim are Description epistemes, specification-use descriptions, or relation records about those holons. `Layer` and `stack` remain source labels unless `C.30.STRAT` recovers a module-interface relation that A.6.M can receive.

### A.6.M:6 - Bias-Annotation

| Bias risk | A.6.M repair |
| --- | --- |
| Box bias | Do not treat a diagram box as a module. Recover holon, whole, boundary, and interface specification. |
| Open-label bias | Do not treat "open" as substitutability. Recover standards, conformance expectations, data or access constraints, and change policy where live. |
| Component bias | Do not treat every part as a module. Apply A.14 to component wording unless module-interface role is live. |
| Interface-label bias | Do not treat API, port, endpoint, or signature labels as implemented compatibility. Recover `InterfaceSpecificationRef`. |
| Team-boundary bias | Do not treat Conway-like mirroring, team responsibility, team communication boundary, or delivery-unit labels as module boundaries. Recover role, enactor, work, and procedural relations first; add module-interface correspondence only when the boundary and interface specification are declared. |
| Parallelism bias | Do not treat decomposition into more modules, teams, services, or paths as performance or evolvability improvement. Recover serial work, synchronization, communication overhead, shared resources, and bottleneck claims through TGA, C.29, C.31, or neighboring characteristic patterns when live. |
| Platform bias | Do not treat a platform name as architecture quality. Recover platform grammar and the exact claim it can substantiate. |

### A.6.M:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| `CC-A6M-1` | The text names the whole holon, candidate module holon, bounded context, and module-interface viewpoint, or explicitly stops at ordinary non-claim-bearing wording. |
| `CC-A6M-2` | The repair states whether the phrase is a module relation, component relation, function allocation, procedural or work-package relation, role or enactor relation, deployment or placement structure, interface specification, signature, port or endpoint, TGA flow crossing, mechanism realization, platform grammar, control relation, autonomy-like operation claim, `C.30.STRAT` source-label case, or open-architecture claim. |
| `CC-A6M-3` | No new root kind is minted for module, interface, platform, or open architecture; layer and stack labels route through `C.30.STRAT` unless a module-interface relation has already been recovered. |
| `CC-A6M-4` | `InterfaceSpecificationRef` is recoverable when interface compatibility, substitutability, or conformance is live. |
| `CC-A6M-5` | Substitution or change policy is declared when replaceability, alternate supplier, upgrade, or platform extension is live. Substitutability not established by the repair is marked as not established, not implied by wording. |
| `CC-A6M-6` | Function, TGA flow, control, work, evidence, assurance, gate, decision, causal, and mechanism claims use their exact governing patterns. |
| `CC-A6M-7` | A failed check gives a repair move or exact governing pattern application, not only a rejection. |
| `CC-A6M-8` | A current `G.2` source row for MOSA, open systems, platform practice, Conway correspondence, team-boundary correspondence, or Amdahl-style decomposition limits appears before that source carries live practitioner guidance. |
| `CC-A6M-9` | RFC keywords are used only for pattern users, records, claims, conformance items, or publication records, evidence records, or assurance records. Modeled modules and interfaces are not written as agents with duties. |

### A.6.M:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| `BoxIsModule` | A diagram box is treated as a module. | Recover `moduleIn(...)` fields or downgrade the box to a publication face or structural view element. |
| `SignatureAsInterface` | A signature declaration is treated as implemented compatibility. | Keep signature under A.6.0 and add interface-specification fields only when live. |
| `PortAsProof` | Matching port or endpoint names are treated as integration proof. | Recover slot specs, protocol or schema, semantic conditions, and exact evidence, conformance, source relation, or reliance relation. |
| `FunctionalLinkAsInterface` | A functional relation is treated as module boundary. | Keep `VP.Functional` and add correspondence or allocation only when live. |
| `OpenByPublicationOnly` | Published interface text is treated as open architecture. | Add substitution policy, conformance expectations, change policy, source or evidence relation, and data or access constraints where live; route supplier-set, procurement, evidence, assurance, gate, work, role, enactor, mechanism, and decision claims to their exact neighboring patterns. |
| `TeamBoundaryAsModule` | A team boundary, team responsibility label, communication boundary, or delivery unit is treated as a module interface. | Recover `A.15`, `A.2`, `VP.Procedural`, or `VP.RoleEnactor`; add A.6.M only for the declared module-interface relation; use `C.29` when a homomorphism-like correspondence claim is live. |
| `MoreModulesMeansBetter` | More modules, teams, services, threads, or parallel paths are treated as automatic improvement. | Recover serial work, synchronization, communication overhead, shared resources, and bottleneck claims; route mathematical speedup or homomorphism claims through `C.29` and route characteristic tradeoffs through `C.31` and `C.16`. |
| `PlatformAsKind` | A platform label becomes a root kind or quality claim. | Use `PlatformGrammarRef` and apply exact governing patterns for quality, measurement, and decision claims. |
| `StackAsArchitecture` | A stack diagram is treated as the architecture itself or as a module-interface relation by label. | Apply `C.30.STRAT` first; then use `C.30` or `C.30.ASV` for architecture or structural-view use, `A.6.M` only for a recovered module-interface relation, or ordinary source-label disposition. |

### A.6.M:9 - Consequences

Benefits:

- Module and interface talk becomes usable without minting false root kinds.
- Practitioners get a cheap relation repair before measurement or evidence work.
- MOSA and open-system claims become precise enough to make real substitution and change reasoning admissible.
- Functional, flow, control, mechanism, work, evidence, assurance, gate, decision, and causal claims stay with their exact governing patterns.

Costs:

- Ordinary architecture prose loses the convenience of treating boxes, ports, interfaces, and modules as one kind.
- Interface claims sometimes require additional records before substitutability can be relied on.
- "Open architecture" becomes harder to claim because interface publication alone is not enough.

### A.6.M:10 - Rationale

The central decision is to treat module as a context-sensitive and viewpoint-sensitive relation role of U.Holon, not as a new root kind. This keeps FPF compatible with many engineering contexts where the same system, episteme, method, organization, publication family, or other structured holon can be a component under one declared relation, a module under another, a functional element under another, and an evidence, assurance, source, or publication artifact under another.

A.6.M follows `A.6.P`: overloaded relation language is repaired by reconstructing kind, slots, qualifiers, admissible use, and witnesses. It also follows the current architecture relation discipline: boundary notes catch the first confusion, while A.6.M supplies the full repair body for module relation, interface specification, substitutability, change policy, and open-architecture conformance and admissible-use claims.

The pattern deliberately keeps measurement out of the first move. A module relation can be repaired before anyone knows whether external coupling density, interface standardization share, evidence reuse, or reusable-structure accounting will be needed. When those claims become live, A.6.M applies `C.31`, `C.31.RSA`, and `C.16`.

### A.6.M:11 - SoTA-Echoing

| Source or practice | Currentness or lineage use | Adopt | Adapt for FPF | Reject or boundary | Practitioner implication |
| --- | --- | --- | --- | --- | --- |
| DoD OUSD(R&E) MOSA guidance and implementation guidebook (`https://www.cto.mil/sea/mosa/`; `https://www.cto.mil/wp-content/uploads/2025/03/MOSA-Implementation-Guidebook-27Feb2025-Cleared.pdf`) | Current official acquisition and engineering practice family for open modular systems; used as current practice guidance, not as a complete FPF ontology. | Modular design, interface standards, conformance verification, replacement or change policy, and competitive reuse are real conformance and substitution expectations. | Recover them as `InterfaceSpecificationRef`, `PlatformGrammarRef`, `substitutionOrChangePolicyRef`, conformance expectation, source relation, and evidence path only where live; route supplier-set, procurement, policy authorization, evidence, assurance, gate, decision, work, role, enactor, and mechanism claims to their exact neighboring patterns. | Do not treat `open`, interface publication, or modular-looking structure as substitutability, assurance, procurement suitability, supplier-set selection, policy authorization, quality proof, or decision authority. | A practitioner asking whether something is open first repairs the relation and the interface specification; selection, procurement, evidence, assurance, gate, work, and decision claims open only when that use is live. |
| Conway's law, the mirroring hypothesis, and Team Topologies and inverse Conway practice (`https://www.melconway.com/Home/Committees_Paper.html`; `https://doi.org/10.1016/j.respol.2012.04.011`; `https://itrevolution.com/wp-content/uploads/2022/06/TTOP_excerpt.pdf`) | Mature socio-technical law and empirical lineage plus current organization-design practice family; used as diagnostic pressure, not as a proof rule. | Team communication structure, team-boundary placement, and delivery responsibility can create real pressure on module and interface boundaries and useful correspondence clues. | Recover team and work material through `A.15`, `A.2`, `VP.RoleEnactor`, or `VP.Procedural` first; connect it to `ModuleInterfaceStructure` only through declared correspondence, allocation, boundary relation, and preserved and lost structure note. Use `C.29` when the correspondence is claimed as homomorphism-like or almost-same structure. | Do not treat Conway's law, an org chart, team responsibility label, or a delivery unit as proof of module interface, substitutability, modularity quality, evidence, gate passage, or architecture decision. | A practitioner may use team-boundary mismatch as a diagnostic prompt: repair the role, work, and module relation, then decide whether the module boundary, team boundary, communication relation, or architecture move changes. |
| Amdahl's law and communication and synchronization extensions (`https://www.cs.cmu.edu/~18742/papers/Amdahl1967.pdf`; `https://arxiv.org/abs/1306.3302`; `https://arxiv.org/abs/2603.20654`) | Mature mathematical law plus current extension sources for communication, synchronization, and scalable-workload-fraction limits. | Serial work, synchronization, communication overhead, shared resources, and changing scalable workload fractions can limit the payoff of decomposition, parallelization, or specialization. | Use `C.29` for mathematical speedup or value-scalable-fraction reasoning, `E.18` and TGA for flow and crossing structure, and `C.31` and `C.16` for modularity and characteristic tradeoffs. | Do not treat module count, team count, service count, parallel-path count, or accelerator count as improvement, scalability, throughput, or evolvability by itself. | A practitioner considering a module split names the serial part, shared bottleneck, synchronization or communication overhead, and characteristic tradeoff before claiming improvement. |
| SEI Views and Beyond, ISO/IEC/IEEE 42010:2022, and multi-view architecture practice | Mature architecture-description lineage plus current international view-description discipline; not used as a current module-quality source. | Module and component-and-connector views are distinct architecture descriptions. | Use `ModuleInterfaceStructure` and `RuntimeInteractionStructure` as structure-kind signals under `C.30.ASV`. | Do not reduce architecture to a module diagram. | Module repair stays one architecture-structure concern, not the whole architecture ontology. |
| Platform and product-line engineering practice (`https://tag-app-delivery.cncf.io/fr/whitepapers/platform-eng-maturity-model/`; `https://www.sei.cmu.edu/library/variability-in-software-product-lines/`; `https://arxiv.org/abs/2605.21353`) | Mature product-line variability lineage plus current platform-engineering maturity-model and current SPLE-review cues; used for variability-slot and extension-rule discipline, not as one FPF platform kind. | Variation slots and extension rules matter for reuse and substitution. | Use `PlatformGrammarRef`, `variabilitySlotRefs`, and change policy instead of a platform root kind. | Do not treat platform name as architecture quality, architecture scale-preference evidence, procurement suitability, supplier-set selection, or decision authority. | The next move is to identify extension rules and substitution conditions; quality, architecture scale preference, procurement, supplier-set, and decision claims exit to the exact neighboring patterns. |
| Architecture-operation language, with neural-network and software-system intakes as source examples | Current practitioner-language source examples accepted by the architecture workstream; used as recognition material, not as a standard or current-best-known authority. | Source labels such as block, layer, expert, router, cache, and state are useful recognition prompts. | Keep them as `C.30.STRAT` source labels until the receiving FPF kind, relation, claim-use, or source-use disposition is recovered; return to A.6.M only for module-interface relation, interface specification, platform grammar, substitutability, or open-architecture module-interface claims. | Do not import source-context labels as module kinds or evidence of adequacy. | The same repair works for neural-network block replacement, hardware module substitution, organizational module repair, and episteme-module repair without making any source context the ontology. |

Older or local sources may serve as lineage or worked examples only when the row says so. They do not stand in for current competitive source, and they do not make a module, interface, platform, or open-architecture claim admissible for comparison, assurance, gate, selection, or decision use without the exact neighboring pattern that governs that use.

### A.6.M:12 - Relations

| Pattern | Relation |
| --- | --- |
| `A.6.P` | A.6.M is an RPR specialization for module-relation and interface-specification language. |
| `C.30.STRAT` | Recovers layer, stack, block, expert, cache, router, gate, and similar source labels before A.6.M receives only recovered module-interface relation cases. |
| `E.16` | Carries autonomy-budget, autonomous operation, independent acting, unsupervised decision or action, and freedom-of-action claims when those are live; A.6.M keeps only the module-interface relation, boundary, interface specification, and substitution or change-policy slice. |
| `A.14` | Component and part-whole wording uses A.14 first unless module-interface role is live. |
| `A.6.0` and `A.6.5` | Signatures, slots, ports, endpoints, and field structure remain governed by signature and slot discipline. |
| `A.6.B`, `A.6.C`, and `A.6.8` | Boundary, interface-specification, API, protocol, service, promise, and duty wording uses A.6.M when live. |
| `C.30` and `C.30.ASV` | Architecture claims and module-interface structural views stay architecture-governed. |
| `A.6.F` | Function and functional wording stays distinct from module allocation. |
| `A.15` and `A.2` | Method, work-plan, performed-work, role-assignment, role claims, and enactor claims stay outside A.6.M; team-boundary or delivery-unit wording routes here unless a module-interface relation is live. |
| `E.18` and `C.30.TGA-FLOW-REL` | E.18 transduction relations, path slices, crossings, and flow valuations are not interface specifications. |
| `C.31` | Modularity and reusable-structure characteristics open after relation repair when characteristic or measurement use is live. |
| `C.31.RSA` | Reusable-structure accounting opens when reusable loci, bespoke residue, or report-only shares are live. |
| `C.16` | Measurement, score, scale, unit, comparability, and evidence-stub legality remain C.16-governed. |
| `A.10`, `B.3`, `A.20`, `A.21`, `C.28`, `E.20`, `G.5`, `C.11` | Evidence, assurance, gates, causal use, mechanism suites, set-return selection, and local decisions use their exact governing patterns; they are not A.6.M claims. |
### A.6.M:End

