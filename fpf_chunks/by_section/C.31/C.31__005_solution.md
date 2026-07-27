---
chunk_kind: "child"
pattern_id: "C.31"
pattern_title: "Modularity and Reusable Structure Characteristics"
section_id: "C.31:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31/C.31__005_solution.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "C.31 — Modularity and Reusable Structure Characteristics"
  - "C.31:4 — Solution"
line_start: 62053
line_end: 62249
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.31"
  - "C.31.ASAP"
  - "C.31.RSA"
  - "C.32"
  - "C.32.P2S"
  - "G.5"
keywords:
  - "ModularityVectorLite"
  - "bespoke residue"
  - "cohesion"
  - "coupling"
  - "evidence reuse"
  - "interface variation"
  - "modularity characteristics"
  - "reusable-structure characteristics"
  - "substitutability"
---

### C.31:4 - Solution

C.31 governs modularity and reusable-structure characteristics as C.16-compatible characteristic heads, composite descriptions, lens-backed characteristic interpretations, temporal or scale-sensitive characteristic interpretations, causal-use-sensitive characteristic interpretations, or report-only proxies. It starts from action guidance and adds fields for beyond-local-repair use only when a use being made requires them.

#### C.31:4.1 - Ordinary output: `ModularityVectorLite`

`ModularityVectorLite` is the ordinary output. It names at most three characteristics under evaluation because the first task is to find the next repair, not to audit all possible modularity interpretations.

```text
ModularityVectorLite:
  describedHolonRef:
  boundedContextRef:
  architectureClaimRef?:
  structureKindRefs:
  threeLiveCharacteristicsAtMost:
    - characteristicRef:
      currentCue:
      repairDirection:
      claimUseClass:
      forbiddenOverread:
  observedProblem:
  relatedClaimGovernanceIfClaimed:
  stopCondition:
```

The vector is complete enough when it states what can be done next and what cannot be inferred. If a characteristic is used beyond local repair, use the appropriate card and governing pattern; architecture scale-preference claims are governed by `C.31.ASAP`.

#### C.31:4.1a - Filled `ModularityVectorLite`

```text
ModularityVectorLite:
  describedHolonRef: ProductPlatform@FieldPumpFamily
  boundedContextRef: FieldServiceAndProcurement@2026Q2
  architectureClaimRef?: ArchitectureOf@PumpControllerPlatform
  structureKindRefs: ModuleInterfaceStructure, EvidencePackageStructure
  threeLiveCharacteristicsAtMost:
    - characteristicRef: InterfaceStandardizationShare
      currentCue: controller ports are named by the same API family, but three field variants still require adapter-specific wiring.
      repairDirection: narrow the interface grammar and name the allowed variation before counting the interface as standardized.
      claimUseClass: local repair cue
      forbiddenOverread: the public API label is not substitutability or procurement suitability.
    - characteristicRef: SubstitutabilityWidth
      currentCue: two alternate controller boards pass the bench test, but only one has the required thermal envelope and connector constraints.
      repairDirection: state the substitution conditions and the exception before using the alternative count.
      claimUseClass: report-only proxy until C.16 or selection use is being made
      forbiddenOverread: the alternate-board count is not a selection result.
    - characteristicRef: EvidenceReuseShare
      currentCue: electrical-safety evidence is reused, while environmental evidence is recreated per enclosure variant.
      repairDirection: split reusable evidence package from variant-specific evidence and add source-return condition.
      claimUseClass: local repair cue with possible evidence-package use
      forbiddenOverread: reused evidence is not assurance sufficiency.
  observedProblem: the team says the platform is modular because interfaces are public and evidence is reusable, but field replacement and certification still create variant-specific work.
  relatedClaimGovernanceIfClaimed: A.6.M for the module-interface relation; C.31.RSA if report-only share becomes reusable-structure accounting; A.10 or B.3 only if evidence or assurance use is being made.
  stopCondition: stop at local repair until measurement basis, comparability basis, and any selection or assurance use are declared by their governing patterns.
```

Near miss: a high interface-standardization count alone is not a C.31 improvement. If field-service work, source-return events, or variant-specific evidence increase, the vector records that proxy divergence and returns to repair rather than treating the count as architecture quality.

#### C.31:4.2 - Characteristic classes

Every C.31 head is classified before use:

| Class | Use | Boundary |
| --- | --- | --- |
| `DirectCharacteristic` | A C.16-governed characteristic can be named with subject, scale, unit or unitless interpretation, declared measurement basis, comparability basis, and repair action. | It is not automatically a score or decision selector. |
| `CompositeCharacteristicDescription` | The head is a bundle or description with sub-slots, such as function-module alignment or flow-boundary alignment. | Do not pretend the bundle is one raw measure. |
| `LensBackedCharacteristic` | The head depends on a model description or mathematical lens, such as compression or RG or coarsening lens. | Apply C.29 for lens use that changes action. |
| `TemporalOrScaleCharacteristic` | The head depends on time window, repeated instance, scale variable, aggregation scope, or source-return condition. | Apply `C.31.ASAP` for architecture scale preference, `C.27` for temporal adequacy, and `C.18.1` or `C.19.1` when scale-law or general BLP preference claims are being made. |
| `CausalUseSensitiveCharacteristic` | The interpretation is used to claim effect or intervention success. | Apply C.28 before relying on the claim causally. |
| `ReportOnlyProxy` | The interpretation is only a local diagnostic or communication aid. | State forbidden overread and the governing pattern needed for any beyond-local-repair use. |

In C.31, `declared basis` and `comparability basis` name C.16-compatible measurement or comparison fields. They are not generic reason words and are not substitutes for evidence, assurance, cause, source, decision, or architecture-description relations.

#### C.31:4.3 - Measurement-head mapping

When a head becomes decision-facing or publication-facing, create `MeasurementHeadMapping` before relying on it:

```text
MeasurementHeadMapping:
  sourceHead:
  knownMeasureFamilyOrPractice:
  fpfCharacteristicKind:
  scaleType:
  unitPolicy:
  declaredBasisNeeded:
  requiredEvidence:
  evidenceRelationRefs?:
  evidenceProvenanceRelationRefs?:
  sourceRelationRefs?:
  evidenceClaimAbsentBecause?:
  commonFalseUse:
  nonAdmissibleUse:
  repairAction:
  governingPatternRef:
```

This mapping is not a measurement template by itself. It prepares a C.16-compatible characteristic card or a report-only boundary. When the head is decision-facing or publication-facing, the mapping names required evidence plus at least one evidence relation, evidence-provenance relation, or source relation. If no evidence claim is being made, `evidenceClaimAbsentBecause` states why the head remains local, report-only, or repair-only.

#### C.31:4.4 - C.31 characteristic card

Use the full card only when the use goes beyond local repair:

```text
ModularityCharacteristicCard:
  characteristicRef:
  subjectRef or relationSubjectTuple:
  characteristicClass:
  scaleRef:
  unitInterpretation:
  declaredBasisRef:
  comparabilityBasisRef:
  requiredEvidence:
  evidenceRelationRefs?:
  evidenceProvenanceRelationRefs?:
  sourceRelationRefs?:
  evidenceClaimAbsentBecause?:
  proxyRisk:
  auditQuestion:
  nonAdmissibleUse:
  repairAction:
  relatedClaimGovernanceRefs:
```

Each card states its own C.16 well-formedness fields: characteristic, scale, unit or unitless interpretation, declared measurement basis, comparability basis, evidence relation, evidence-provenance relation, source relation, or evidence-claim-absent reason, non-admissible use, and repair action. When source material is used as evidence, the source relation is named. A source checklist, source-discharge slice, dashboard label, or inherited score is not enough.

#### C.31:4.5 - Seed characteristic heads and repair actions

These heads are seeds, not an exhaustive taxonomy. Use only the heads that change the next action.

| Characteristic head | Intended characteristic interpretation | Typical scale or value form | Declared measurement or comparison basis | Defect signal | Repair direction | Escalation trigger |
| --- | --- | --- | --- | --- | --- | --- |
| `InternalCohesionDensity` | Density of typed relations inside a proposed module. | ratio or graph-derived value | typed dependency graph or DSM | proposed module has insufficient typed internal dependency basis | split the proposed module, move relations, or reclassify as component relation | comparison, clustering, or publication use |
| `ExternalCouplingDensity` | Cross-boundary dependencies per module or interface. | ratio or distribution | typed dependency graph, interface graph, integration defects | hidden external dependencies dominate module boundary | expose dependency, revise interface spec, split context, or accept bounded exception | integration risk, assurance, or release claim |
| `InterfaceAlphabetSize` | Count or entropy-like variety of interface types. | count or entropy-like value | interface registry | too many interface variants erase modular benefit | reduce variants, introduce interface grammar, split context, or document exception | platform grammar, candidate selection, or publication use |
| `InterfaceStandardizationShare` | Share of interfaces conforming to declared specifications. | ratio or percentage | conformance tests and specifications | standardization is low where reuse needs it | define or narrow standards, add conformance tests, or stop at local exception | cross-case comparison, certification, or procurement decision claim |
| `InterfacePublicness` | Openness, publication, and vendor-neutrality value. | ordinal or category | standards, API specs, licensing, access terms | open label lacks substitutability relation, substitution policy, conformance expectation, or interface specification | recover interface spec, substitution policy, and conformance expectation | open-architecture claim, procurement decision claim, or publication claim |
| `SubstitutabilityWidth` | Number or diversity of compatible alternatives for a slot or interface. | count or diversity value | approved implementations, vendors, tests | only one viable implementation exists | repair interface spec, loosen unnecessary coupling, or mark single-source exception | competition, platform, or decision claim |
| `ModuleTypeReuseRate` | Instances per module type or template. | ratio or count | product-line records, bills of material, template records | reuse is claimed only by repeated naming | define module type, allowed variation, and measurement basis | cross-case reuse or product-line publication |
| `TemplateCompressionGain` | Description saving from template plus parameters compared with instance-by-instance descriptions. | ratio or bits under declared method | corpus or model-description method | compression erases safety, law-domain, or source distinctions | add source-return condition, split template, or apply C.29 | lens-characteristic or effect claim, publication, or decision use |
| `FunctionModuleAlignmentCharacteristic` | Functional elements and module relations align without unmanaged many-to-many exceptions. | vector, ordinal, or bundle description | functional view and module relation records | allocation hides many-to-many exceptions | split function from module claim, revise allocation, or add correspondence | candidate decomposition or quality-composition claim |
| `FlowModuleBoundaryAlignmentCharacteristic` | Flow topology crosses declared interfaces rather than hidden channels. | vector, ordinal, or bundle description | transformation-flow structure refs and interface refs | flows bypass declared module boundaries | expose crossing, revise interface, or apply C.30.TFS-REL for the architecture-to-transformation-flow relation claim | publication or assurance claim about the architecture-to-transformation-flow relation |
| `ControlStructureSeparationCharacteristic` | Control responsibilities, rates, and boundaries are explicit enough for the architecture move. | ordinal or vector | LCA or control description and temporal adequacy basis | control relation is hidden inside module label | apply C.30.LCA, C.27, A.3.3, or B.3 when a control, temporal, dynamics, or assurance claim kind is being made | stability, assurance, or gate use |
| `HiddenCouplingDiscoveryRate` | Hidden dependencies discovered after integration or change. | rate | defect and change records | dependencies appear late | expose side channel, revise interface spec, add sentinel, or reopen boundary | integration risk, repeated release, or assurance claim |
| `CrossBoundaryChangeReach` | How many modules, views, or work items a local change touches. | distribution | change-impact records | local change travels farther than claimed | split relation, add interface grammar, revise allocation, or source return | release, decision, or comparison claim |
| `WorkRepeatabilityShare` | Delivery, operation, or test work under repeatable method descriptions. | ratio | work records and method descriptions | work repeats as bespoke effort | move repeated work into `MethodDescription` or accept exception | work planning, evidence reuse, or scale use |
| `EvidenceReuseShare` | Evidence package items reused across instances or contexts. | ratio | evidence graph and validity context | evidence is recreated or mis-scoped | move repeated evidence into reusable evidence or assurance package | certification, safety-case, or assurance claim |
| `RegulatoryBespokeResidue` | One-off regulatory or acceptance content not covered by reusable structures. | ratio or ordinal | safety, approval, or regulatory records | each instance needs new regulatory argument | isolate residue, add reusable evidence package, or keep bounded exception | safety case, approval, or publication claim |
| `LearningTransferCoefficient` | Improvement transfer from one instance or run to subsequent instances. | slope or elasticity | repeated work data and learning curve records | improvement claim hides time or causal assumptions | apply C.27 for temporal adequacy and C.28 for causal use | causal, benchmark, or scale-preference use |
| `BespokeResidueShare` | Share of structure not covered by reusable templates or rules. | report-only share unless C.16 measurement basis is declared | RSA description and exception register | residue is hidden under reuse score | use C.31.RSA and source-return condition | accounting, comparison, or decision claim |
| `RGFlowStability` | Stability of characteristic vector across declared coarse-graining scopes. | vector or ordinal | declared multi-scope architecture graphs | coarse-graining hides lower-scope hazards | apply C.29 for lens use and C.31.ASAP when an architecture scale-preference claim is being made | RG, scale, or lens transfer use |
| `ExceptionCurveSlope` | Change in one-off exceptions over a scale variable. | slope | exception records against scale variable | exceptions grow with scale | apply C.31.ASAP or accept bounded exception | scale preference, publication, or decision claim |

#### C.31:4.6 - Claim-scoped residual heads

C.31 uses residual heads only as qualitative repair cues. These heads do not create one complexity characteristic.

| Head | Meaning | Related claim governance | Risk | Repair direction |
| --- | --- | --- | --- | --- |
| ComplexityGrowthPressure | Pressure to add, split, mediate, or stabilize a declared aggregation scope, interface grammar, control relation, evidence scope, work-method scope, abstraction scope, or source-return condition. | C.30.ILC, C.31.ASAP when an architecture scale-preference claim is being made, G.5, C.11 | treating more apparatus as progress | name the pressure and the repair direction; use set-return or decision patterns when the corresponding claim is being made |
| `FrustrationResidual` | Persistent cross-scope residual after local repair. | `C.30.ILC`, C.29-local cross-scope lens claim | turning a lens-backed interpretation into proof | keep as residual cue or apply C.29 or C.30.ILC |
| `ConflictResidualSlope` | Residual grows or shrinks over declared scale variable, scale window, or coarse-graining scale. | `C.31.ASAP`, `C.29`, `C.27`, `C.18.1`, `C.19.1` | treating two points as universal law | declare window, lens-use boundary, and measurement basis or stop at report-only |
| `DeclaredScopeAdditionCost` | Added work, evidence, change-policy, latency, observability, accountability, or interface cost from a new declared aggregation or control scope. | `C.16`, `C.31`, `C.30.LCA` | ignoring the cost of added structure | identify cost bearer and apply the measurement pattern if used for comparison |
| `BespokeResidueGrowth` | One-off exceptions grow with deployment spread, regulation, or project repetition. | `C.31.RSA`, `C.31.ASAP` when an architecture scale-preference claim is being made | assuming all bespoke work is bad | split useful exception from repairable residue |
| `InterfaceAlphabetGrowth` | Interface variants grow faster than reuse, substitutability, or integration payoff. | `A.6.M`, `C.31` | premature standardization | add platform grammar, split context, or accept bounded variation |
| `SourceReturnCost` | Frequency or cost of returning from a compressed, indexed, coarse, extracted, or accounting view to source-side structure records. | `C.29`, source-return discipline, `A.10` | over-compression | add source-return condition or reduce compression |
| `ControlNestingDepthRisk` | Nested control relations create latency, accountability, observability, stability, or assurance cost. | `C.30.LCA`, `C.27`, `B.3`, `A.3.3` | LCA-as-proof | apply control, temporal, assurance, or dynamics governing patterns when the corresponding claim is being made |

#### C.31:4.7 - Proxy-risk discipline

Every decision-facing C.31 card includes `ProxyRisk` and `AuditQuestion`. If the proxy diverges from the value it was meant to represent, the card stops at report-only use or returns to repair.

| Head | Proxy risk | Audit question |
| --- | --- | --- |
| `ExternalCouplingDensity` | Teams hide dependencies instead of reducing them. | Did integration failures or source-return events fall? |
| `InterfaceStandardizationShare` | Premature standardization blocks useful variation. | Did exception slope or workarounds rise? |
| `InterfacePublicness` | Open label without substitutability. | Are alternative implementations actually viable under declared conditions? |
| `TemplateCompressionGain` | Compression erases safety, law-domain, or source distinctions. | Did source-return events or bounded exceptions rise? |
| `EvidenceReuseShare` | Reused evidence becomes stale or mis-scoped. | Does evidence remain valid in the new context? |
| `RGFlowStability` | Coarse-graining hides lower-scope hazards. | Are source-return conditions triggered? |

#### C.31:4.8 - Rejected shortcut

The expression `ModularityScore = average(all measures)` is not admissible as a C.31 result. A local score is admissible only when the scoring method, codomain, polarity, characteristic basis, comparability basis, and use boundary are disclosed through the governing scoring or comparator pattern. Without that, keep the result as report-only or return to `ModularityVectorLite`.

#### C.31:4.9 - Lowering and currentness conditions

Lower or reopen a `ModularityVectorLite`, `ModularityCharacteristicCard`, or report-only proxy when any of these conditions changes the characteristic use:

- proxy audit worsens, such as more integration failures, workarounds, source-return events, stale evidence reuse, or bounded exceptions;
- measurement basis, comparability basis, scoring method, codomain, polarity, unit policy, or declared characteristic basis changes;
- evidence relation, evidence-provenance relation, source relation, evidence-claim-absent reason, or source-return condition changes;
- described holon, bounded context, architecture claim, structure kind, characteristic head, or repair direction changes;
- a report-only proxy is used for comparison, selection, publication, assurance, benchmark, causal-use, cross-case reuse, decision, procurement, or architecture scale-preference;
- `C.31.RSA`, `C.31.ASAP`, `C.16`, `C.25`, `C.29`, `C.30.STRAT`, `A.6.M`, `C.30`, `C.30.ASV`, `A.10`, `B.3`, `A.20`, `A.21`, `G.5`, or `C.11` changes the boundary for the neighboring claim being made.

Admissible repair results are: keep the result report-only, split or rename the characteristic head, update basis or evidence fields, revise the repair direction, change `relatedClaimGovernanceIfClaimed`, lower a score to a local proxy, or stop C.31 use for the beyond-local-repair claim and use the governing pattern.

