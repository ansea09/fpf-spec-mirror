---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Architecture Description Adequacy (ADA)"
section_id: "C.30:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__005_solution.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "C.30 — Architecture Description Adequacy (ADA)"
  - "C.30:4 — Solution"
line_start: 51123
line_end: 51515
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
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
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
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
  - "ArchitectureOf@Context"
  - "architecture claim"
  - "architecture description"
  - "architecture question card"
  - "artifact-as-architecture guard"
  - "selected structure"
---

### C.30:4 - Solution

Introduce architecture-description adequacy as governance for describing an `ArchitectureOf@Context` claim record that selects intensional structure for one holon in one bounded context. The description is governed; it is not the architecture itself.

C.30 does not mint `U.Architecture` and does not redefine `U.Viewpoint`. It specializes A.22 structure records and `U.MultiViewDescribing` for architecture descriptions whose described entity is the `ArchitectureOf@Context` claim record for a holon, while preserving the I/D/S distinction between architecture and its descriptions.

C.30 governs architecture-description adequacy for one `ArchitectureOf@Context` claim record over selected `candidate:U.Structure` references for one described holon in one bounded context. It governs `ArchitectureOf@Context`, `ArchitectureQuestionCard@Project`, `ArchitectureDescription@Context`, architecture-description publication boundaries, architecture name formation, characteristic assignment, first architecture-question assignment, and small boundary notes. It does not mint `U.Architecture` and does not govern all architecture structure-kind views; `C.30.ASV` governs architecture structural views.

#### C.30:4.1 - Architecture claim record

```text
ArchitectureOf@Context ::= {
  describedHolonRef: U.HolonRef,
  boundedContextRef: U.BoundedContextRef,
  structureRefs: FinSet(candidate:U.StructureRef),
  structureKindRefs: FinSet(ArchitectureStructureKindRef),
  liveArchitectureConcernCue?,
  governingArchitectureConcernRefs?,
  architectureConcernNotes?,
  structuralRelationRecordRefs?,
  admissibleUse,
  nonAdmissibleUse
}
```

`ArchitectureOf@Context` is a project-side architecture claim record over selected structures. It is not the selected structure itself, not a D/S description, not a view, not a diagram, not a publication face, not a decision, and not a new root `U.*` kind.

`ArchitectureOf@ContextRef` is admissible as a `DescriptionContext.DescribedEntityRef` for architecture D/S descriptions and views. The holon whose architecture is claimed remains `ArchitectureOf@Context.describedHolonRef`; it is not the D/S `DescribedEntityRef` for those architecture descriptions unless a separate direct holon description is opened.

#### C.30:4.2 - Architecture description record

`ArchitectureDescription@Context` is a governed multi-view D/S description record set over one `ArchitectureOf@Context` claim record and selected `StructuralDescription@Context` or `StructuralView@Context` records. It is used for engineering reasoning about the described holon's design, operation, evolution, interfaces, work, evidence, adequacy, and scale behavior through typed relations to exact non-architecture records; it does not collect those non-architecture claim kinds as architecture-description ontology.

```text
ArchitectureDescription@Context ::= {
  architectureDescriptionId: ArchitectureDescriptionId,
  architectureClaimRef: ArchitectureOf@ContextRef,
  descriptionContext: DescriptionContext(
    DescribedEntityRef = architectureClaimRef,
    BoundedContextRef = ArchitectureOf@Context.boundedContextRef,
    ViewpointRef = viewpointRef
  ),
  selectedStructureRefs: FinSet(candidate:U.StructureRef),
  structureKindRefs: FinSet(ArchitectureStructureKindRef),
  architectureStructuralViewRefs: FinSet(ArchitectureStructuralViewRef),
  structuralAspectDescriptionRefs: FinSet(StructuralAspectDescriptionRef),
  correspondenceModelRefs: FinSet(CorrespondenceModelRef),
  structuralRelationRecordRefs: FinSet(QualifiedRelationRecordRef),
  descriptionRelianceRelationRefs?: FinSet(
    CharacteristicRelationRef | EvidencePathRef | AssuranceCaseRef |
    TGASourceRelationRef | MLALensBoundaryRef | SourceReturnRef
  ),
  freshnessCueRefs?: FinSet(ArchitectureDescriptionFreshnessCueRef),
  sourceReturnCondition?,
  admissibleUse,
  nonAdmissibleUse
}
```

`ArchitectureDescription@Context` is not the holon itself, not the selected structure, not identical to the `ArchitectureOf@Context` claim record, and not the publication face, carrier, or rendering. It is a D/S episteme record whose `DescriptionContext.DescribedEntityRef` points to the `ArchitectureOf@Context` claim record.

Use an `ArchitectureDescriptionFreshnessCue` when the admissible use of an architecture description depends on source edition or structure edition:

```text
ArchitectureDescriptionFreshnessCue:
  sourceEditionRefs:
  structureEditionRefs?:
  knownRefreshTrigger:
    sourceChange | deploymentChange | interfaceChange | controlRateChange |
    modelEditionChange | evidenceDecay | toolApiChange |
    legalRegulatoryChange | incidentFinding | unknown
  admissibleUseUntil:
  sourceReturnCondition:
```

The freshness cue is not evidence sufficiency and not assurance. It only bounds the architecture description's admissible use.

#### C.30:4.3 - Publication boundary

```text
ArchitectureDescriptionPublication@Project ::= {
  sourceEpistemeRef | sourceViewRef,
  publicationVPId,
  publicationScopeId,
  boundedContextRef,
  mvpkFaceRef,
  carrierRef,
  sourcePinSetRef,
  audience,
  admissiblePublicationUse,
  nonAdmissiblePublicationUse
}
```

`ArchitectureDescriptionPublication@Project` is E.17/MVPK-subordinate. It publishes one source episteme or episteme-lane view reference. `mvpkFaceRef` is a publication-lane face reference, not an alternative source object. Publication does not add architecture claims, evidence sufficiency, gate status, work authority, assurance, decision authority, or release permission.

Model cards, system cards, and evaluation harness reports enter C.30 through the same publication/source-relation boundary. They may describe a model, deployed AI system, architecture claim, evaluation harness, or policy, but they do not by themselves establish architecture adequacy, safety proof, release authority, or gate passage.

```text
ModelCardOrSystemCardBoundaryNote@Project ::= {
  sourcePublicationRef,
  describedEntityRef,
  describedEntityKind:
    model | deployedAISystem | architectureClaim |
    evaluationHarness | policy | otherDeclared,
  architectureStructureKindRefs?,
  intendedUseScope,
  evaluationScopeAndKnownLoss?,
  deploymentContextMismatch?,
  evidenceOrAssuranceGoverningPatternRef?,
  nonAdmissibleUse:
    notArchitectureAdequacy | notSafetyProof |
    notReleaseAuthorityByPublicationAlone
}
```

If the card or harness is used beyond transparency, recover the live architecture structure kind first and then apply `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `C.16`, `C.28`, or `C.11` for the non-architecture claim kind.

#### C.30:4.4 - Architecture name formation

The word `architecture` is shorthand only after the described holon, bounded context, selected structures, structure kind, and artifact role are recoverable. Without those qualifiers, it is a recovery trigger, not a stable FPF term.

```text
ArchitectureNameFormationRule:

If a text says "<X> architecture", then the load-bearing use is conforming only with:
  describedHolonRef,
  boundedContextRef,
  structureKindRef = <X>StructureKind or declared local relation,
  structureRefs,
  ArchitectureStructuralViewRefs if this is a description/view claim,
  admissibleUse,
  nonAdmissibleUse.

If <X> is not a declared structure kind, the phrase is plain recognition wording only.
```

| Phrase | Required recovery |
| --- | --- |
| functional architecture | `structureKindRef = FunctionalStructure`; functions, effects, capabilities, and functional dependencies named as structure content; transductions and flow paths are assigned to `FlowTransductionStructure` or `C.30.TGA-FLOW-REL`. |
| modular architecture | `structureKindRef = ModuleInterfaceStructure`; module relation records, interface specifications, substitutability rule, and change policy. Full module/interface repair applies the exact module/interface repair pattern when that claim kind is live. |
| logical architecture | `structureKindRef = DeclaredLogicalStructure`; local definition says whether `logical` means information, functional, runtime, responsibility/allocation, or another relation class. |
| physical architecture | `structureKindRef` in `{MaterialSpatialStructure, PlacementDeploymentStructure}` or a locally declared physical structure kind. |
| control architecture | `structureKindRef = ControlStructure`; an LCA record may describe the control structure, but proof claims are assigned to dynamics, temporal, causal, evidence, safety, or assurance patterns as triggered. |
| information architecture | `structureKindRef = InformationDataStructure`; state bearer and residence, schema refs, semantic refs, persistence locus, provenance relation, custody relation, and source-return conditions. |
| security architecture | `structureKindRef = SecurityTrustBoundaryStructure`; recover protected asset or effect, trust boundary, adversarial path, authority or privilege relation, secure-default or hardening boundary, and evidence, assurance, or gate governing patterns when those claim kinds are live. |


#### C.30:4.5 - Architecture characteristic assignment

C.30 uses three bearers before any `quality`, `fitness`, `measure`, `metric`, `score`, `modularity`, or `ility` wording carries architecture-adequacy force. Those words are triggers for bearer recovery, not stable architecture adequacy by themselves.

```text
ArchitectureCharacteristicAssignment:

A. SystemQualityAffectedByArchitecture
   Bearer: described U.Holon or named product/system entity
   Governing pattern: C.25 Q-Bundle or C.16
   Examples: maintainability, evolvability, resilience, availability, safety, observability

B. ArchitectureStructuralCharacteristic
   Bearer: `ArchitectureOf@Context` claim, architecture structural view, declared structural relation or constraint, module/interface relation
      Governing pattern: C.16 / A.17-A.19 / admitted architecture-characterization receiving pattern
   Examples: coupling, cohesion, interface alphabet, substitutability, hidden coupling, reusable-structure share

C. ArchitectureDescriptionAdequacy
   Bearer: ArchitectureDescription@Context / architecture structural view / correspondence model
   Governing pattern: C.30 / E.17 / A.6.Q / C.16
   Examples: viewpoint coverage, correspondence adequacy, source-return adequacy, description modularity
```

C.30 keeps only a thin bridge from structural characteristics to Q-Bundle relevance. If the claim says architecture causes an outcome improvement, assign causal-use governance to `C.28` before causal use. If a structural characteristic is used as a mechanism, constraint, predictor, proxy, evidence relation, or causal hypothesis for a Q-Bundle slot, start with `ArchitectureStructuralCharacteristicQBundleRelationLine` rather than a formula such as `low coupling = maintainability`; send measurement, modularity scoring, reusable-structure share or accounting, bespoke-residue accounting, evidence sufficiency, assurance, gate, causal proof, and scale audit to their exact governing patterns.

`ArchitectureStructuralCharacteristicQBundleRelationLine` is the only ordinary first-contact relation shape C.30 introduces for this case. Do not add a second generic characteristic relation record in C.30. Use the line when the useful move is to show why one structural characteristic may matter without opening the full relation record. Do not use this line as a measurement record, modularity score, evidence sufficiency statement, assurance verdict, or causal proof:

```text
ArchitectureStructuralCharacteristicQBundleRelationLine ::= {
  architectureClaimRef: ArchitectureOf@ContextRef,
  architectureStructuralViewRef?: ArchitectureStructuralView@ContextRef,
  structuralCharacteristicCueOrRef,
  affectedQBundleSlotRef,
  qBundleRelationKind:
    structuralCharacteristicRelevantToQBundleSlot |
    structuralCharacteristicConstrainsQBundleSlot |
    structuralCharacteristicPredictsQBundleSlot |
    structuralCharacteristicProxiesQBundleSlot |
    structuralCharacteristicCausalHypothesisForQBundleSlot |
    structuralCharacteristicEvidencePathForQBundleSlot,
  relationBasisKind:
    modelBased | empirical | causalModelBased | expertJudgement |
    sourceLineageOnly | SoTAActionLineage | reportOnly,
  evidenceOrCausalGoverningPatternRefIfLive?,
  nonAdmissibleUse
}
```

Minimal structural-characteristic relation-line examples:

| Structure kind | Structural characteristic cue or relation | Affected Q-Bundle slot | Relation-basis note | Non-admissible use |
| --- | --- | --- | --- | --- |
| `ModuleInterfaceStructure` | Stable interface specification plus substitution policy. | Evolvability or replaceability. | Replacement without global retesting. | Open label as substitutability proof. |
| `PlacementDeploymentStructure` | Controller placed near plant or edge-node locality. | Latency, resilience, or jurisdictional compliance. | Reduced communication delay and bounded data custody. | Placement diagram as performance or legal proof. |
| `InformationDataStructure` | State bearer, residence, provenance, and custody boundary. | Observability, privacy, or auditability. | Recoverable state lineage and bounded custody. | Data schema as evidence sufficiency. |
| `MaterialSpatialStructure` | Physical separation, adjacency, or energy path. | Safety, maintainability, or energy efficiency. | Isolation, accessibility, or loss reduction. | Geometry as safety proof. |
| `ControlStructure` | Observer-controller-plant loop with rate envelope. | Stability, controllability, or safety. | Feedback and bounded actuation relation. | Control diagram as proof. |
| `FlowTransductionStructure` | Path crossing, bottleneck, or buffer/waiting-line boundary. | Latency, throughput, or resilience. | Recoverable path, crossing, capacity, and valuation relation. | Flow graph as performance or causal proof. |
| `SecurityTrustBoundaryStructure` | Trust boundary, privilege path, or untrusted-input crossing. | Security, abuse resistance, or privacy. | Reduced exposed authority and bounded trust crossing. | Risk color or compliance label as security proof. |
| `EvidenceAssuranceStructure` | Evidence package reused across variants. | Assurance maintainability or release readiness. | Explicit affected-structure and source-return boundary. | Evidence-structure view as assurance verdict. |
| `WorkMethodStructure` | Method description, work plan, or work enactment relation with explicit exception path. | Operability, auditability, or maintainability. | Bounded repeatability and recoverable exception handling. | Work-method diagram as work authority or evidence sufficiency. |

`ArchitectureCharacteristicQBundleRelationRecord` is a triggered/full-mode record, not the ordinary first-contact shape. Open the full record only when publication, comparison, causal use, evidence reliance, assurance, gate, decision, or reusable cross-case relation reliance is live and the thin line cannot keep the relation inspectable, reusable, or bounded. This preserves the protection against causal or quality overread without turning C.30 into a measurement-first pattern.

Relation kinds in this record are C.30-local relation tokens. They must remain recoverable as A.6.P-style relation specifications: polarity, participant slots, qualifiers, witness expectations, admissible semantic change classes, and bridge or loss boundary where those are live.
ISO/IEC 25010-like quality models may be used as quality vocabulary or comparison lineage for product qualities such as reliability, security, maintainability, usability, efficiency, compatibility, or portability. C.30 does not inherit them as architecture theory. Architecture relates to qualities through Q-Bundle slots, mechanism slots, relation posture, evidence or causal governing patterns, or report-only posture.

```text
ArchitectureCharacteristicQBundleRelationRecord ::= {
  architectureClaimRef: ArchitectureOf@Context,
  architectureStructuralViewRef?,
  architectureDescriptionRef?,
  structuralCHRRefs,
  affectedQBundleRefs,
  relationKind:
    structuralCharacteristicRelevantToQBundleSlot |
    structuralCharacteristicConstrainsQBundleSlot |
    structuralCharacteristicPredictsQBundleSlot |
    structuralCharacteristicProxiesQBundleSlot |
    structuralCharacteristicCausalHypothesisForQBundleSlot |
    structuralCharacteristicEvidencePathForQBundleSlot,
  participantSlots:
    structuralCharacteristicRef,
    qBundleSlotRef,
    architectureClaimRef,
    scopeOrScaleWindow?,
    viewpointRef?,
  qualifiers?,
  witnessExpectations?,
  relationBasisKind:
    modelBased | empirical | expertJudgement |
    sourceLineageOnly | SoTAActionLineage | causalModelBased | reportOnly,
  bridgeOrLossBoundary?,
  admissibleUse,
  nonAdmissibleUse,
  evidenceOrCausalGoverningPatternRefIfLive?
}
```
#### C.30:4.6 - Relation to structural views

`C.30.ASV` governs `ArchitectureStructuralView@Context`. C.30 only governs the architecture-description relation to the structural views it uses, with hidden/lost structure, correspondence, source or reliance relation, and source-return boundaries recoverable when those boundaries affect action.

A diagram, model, table, TGA graph, LCA diagram, C.29 lens output, ADR, dashboard, generated explanation, or other publication face may carry an architecture description or an architecture structural view. It does not become the architecture, and it does not become a conforming view only because it looks like a view.

Use `AffectedArchitectureStructureNote` when the next architecture move needs to name affected structures or view losses without opening an architecture decision, ADR, gate, evidence, assurance, or release record:

```text
AffectedArchitectureStructureNote:
  architectureClaimRef:
  affectedStructureKindRefs:
  affectedStructureRefs?:
  affectedArchitectureStructuralViewRefs?:
  acceptedOrSuspectedViewLoss?:
  sourceReturnCondition?:
  nextAdmissibleMove:
```

This note only names affected architecture structure for the next move. It is not an architecture decision, not an ADR, not gate passage, not evidence sufficiency, and not release authority.

#### C.30:4.7 - Minimal boundary notes

Use these notes when a common architecture phrase is close to a exact governing pattern but the full governing pattern is not yet live.

Use the thinnest relation form that preserves the next architecture move. Open fuller exact governing relation records only when the current relation cannot be inspected, used, compared, refreshed, or bounded without it. Typical thin forms are `ArchitectureMLABoundary` before C.29 Mini or Full, `AffectedArchitectureStructureNote` before an architecture decision record, and `ArchitectureStructuralCharacteristicQBundleRelationLine` before full measurement or causal/evidence records.

```text
InterfaceSignatureBoundaryNote ::= {
  phraseOrArtifactRef,
  apparentClaim:
    interface | signature | port | endpoint | connector | link |
    API | protocol | TGA transfer | TGA path | mechanism reference,
  recoveredKind,
  governingPatternApplicationRefs,
  admissibleUse,
  nonAdmissibleUse
}

ModuleRelationBoundaryNote ::= {
  phraseOrArtifactRef,
  apparentClaim:
    module | component | package | platform | stack | open architecture |
    typed control-structure relation,
  moduleInterfaceRepairClaimLive?: yes | no,
  openOrPlatformClaimLive?: yes | no,
  exactModuleInterfaceRelationRefs?,
  variationPointRef?,
  substitutabilityPolicyRef?,
  interfaceConformanceEvidencePatternRef?,
  changePathRef?,
  consumerMigrationBoundary?,
  versionOrUpdateChannelRef?,
  secureDefaultOrHardeningBoundary?,
  governingPatternApplicationRefs,
  admissibleUse,
  nonAdmissibleUse
}
```

These notes are not substitutes for the exact module/interface repair pattern, interface specifications, signature records, conformance evidence, or module/interface repair. An open or platform label is not substitutability proof, security proof, scale proof, assurance, or universal maturity evidence. It becomes architecture-relevant only through local structure, interface, variation, substitution, migration, update, and hardening boundaries. Relation-heavy wording inside these notes remains a Plain cue until an exact module/interface relation ref, exact governing relation record, or governing FPF pattern carrier is named. The note keeps first use honest until the exact non-architecture claim kind opens.

#### C.30:4.8 - Architecture mathematical-lens boundary

Architecture descriptions may use C.29 lenses, but the lens does not become architecture ontology.

```text
ArchitectureMLABoundary:
  noMLANeeded?: yes | no
  lensOneLine?:
    lensRef,
    structureClaimRef,
    preservedStructure,
    lostStructure,
    lensRelationBasisKind,
    stopCondition,
    governingPatternApplicationRefs?
```

Use the one-line boundary only when it is enough to keep the lens from being overread. Open C.29 Mini or Full cards when the lens choice, preserved/lost structure, relation posture, or stop condition changes the architecture move.

Lens use by architecture problem:

| Architecture problem | Candidate mathematical lens | Preserved structure | Typical loss or stop |
| --- | --- | --- | --- |
| Hidden dependency or modularity. | Typed graph, DSM, or hypergraph. | Dependency, coupling, or clustering. | Semantics, interface law, evidence, and work remain outside unless bridged. |
| Flow bottleneck. | TGA, network flow, or queueing. | Path, crossing, valuation, and capacity. | Purpose, proof, causality, and safety remain non-architecture claims. |
| Control-rate mismatch. | LCA, hybrid systems, assumption-guarantee relations, or control relations. | Feedback roles and scale or rate relations. | Stability proof and safety proof remain outside the lens. |
| Cross-scope residual. | Coarse-graining or renormalization-group-style lens. | Preserved and lost structure across scale. | Utility, causal-use claims, and selector authority remain outside unless separately grounded. |
| Extracted structure from traces. | Epiplexity or MDL-style bounded-observer lens. | Learnable structural regularity. | Task relevance, assurance, and causal proof remain non-architecture claims. |
| Physical separation or spatial arrangement. | Topology, geometry, or spatial graph lens. | Adjacency, containment, separation, reachability, or energy/material path. | Safety proof, accessibility, legal acceptance, and causal-use claims remain outside unless separately grounded. |
| Composition relation. | Category, open-systems, or compositional lens. | Interface, composition, and coherence. | Domain semantics remain outside unless bridged. |

This table is not a C.29 replacement and does not make mathematics mandatory. It helps the practitioner see when a lens may add a useful architecture move; C.29 still carries lens adequacy, preserved/lost structure, relation posture, and stop condition when those are live.

Epiplexity-like use remains a C.29 bounded-observer structural-information lens. It may help recover learnable structure from traces, but it is not an architecture quality, task relevance proof, causal proof, assurance, or selector authority.

#### C.30:4.9 - Boundary and repair table

| Tempting collapse | C.30 repair |
| --- | --- |
| Bare architecture as governed object | Recover `describedHolonRef`, `boundedContextRef`, selected `structureRefs`, active `structureKindRef`, artifact role, `admissibleUse`, and `nonAdmissibleUse`. |
| Architecture description as architecture | Keep `ArchitectureDescription@Context` as D/S episteme over `ArchitectureOf@Context`. |
| Diagram, model, table, dashboard, or generated relation graph as architecture | Treat it as carrier, publication, description, view, source relation, or source-finding aid only when that relation is explicit. |
| Module diagram as all architecture | Use `C.30.ASV` to recover structure kind; module/interface is only one structure kind. |
| TGA graph as architecture | Use `E.18` for graph/path/crossing and `C.30.TGA-FLOW-REL` for architecture-flow description. |
| LCA/control diagram as proof | Use `C.30.LCA` for control-structure view; assign dynamics, temporal, causal, evidence, gate, safety, and assurance claims to their governing patterns. |
| Mathematical lens as architecture ontology | Use `C.29`; cite `MLAOutputRef` only through an `ArchitectureMLABoundary` or C.29 lens record and state stop condition. |
| ADR as architecture decision | Use the exact project-side architecture decision pattern when a decision claim is live; ADR is a publication form, not the decision. |
| Quality, score, or measurement term as architecture adequacy | Recover the bearer through `ArchitectureCharacteristicAssignment`; assign the live claim to `C.25`, `C.16`, an admitted architecture-characterization receiving pattern, or C.30 description adequacy. |
| Architecture record as evidence, assurance, gate, work, or release | Assign evidence, assurance, gate, work, or release claims to `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, or release loci as live. |
| Architecture as agent, worker, controller, gate, or proof | Recover the mechanism, control relation, role/enactor, gate, work, evidence, or assurance carrier that actually bears enforce, decide, optimize, adapt, prove, or guarantee wording; keep `ArchitectureOf@Context` as a selected-structure claim, not an acting entity. |

#### C.30:4.10 - Worked slices

**"We have the architecture in this diagram."** The diagram is a carrier or publication face unless it explicitly carries an `ArchitectureDescription@Context` or `ArchitectureStructuralView@Context`.

```text
ArchitectureQuestionCard@Project:
describedHolonRef: payment system
boundedContextRef: checkout platform context
liveArchitectureConcernCue: unclear dependency between payment orchestration and fraud scoring
plainPromptLabel: "architecture in this diagram"
activeStructureKindRefs: FunctionalStructure, ModuleInterfaceStructure, FlowTransductionStructure
currentCollapseCue: diagram is being treated as architecture itself
firstArchitectureMove: downgrade the diagram to a publication face and create a minimal architecture structural-view note
ordinaryNotThisPatternBoundary: no evidence, assurance, gate, or decision claim yet
governingPatternApplicationRefs: C.30.ASV
```

**"Low coupling gives maintainability."** C.30 does not allow that formula to carry the claim by itself. The ordinary repair starts with the thin relation line:

```text
ArchitectureStructuralCharacteristicQBundleRelationLine:
  architectureClaimRef: ArchitectureOf@ContextRef
  structuralCharacteristicCueOrRef: coupling under module/interface relation
  affectedQBundleSlotRef: maintainability Q-Bundle slot
  qBundleRelationKind: structuralCharacteristicRelevantToQBundleSlot
  relationBasisKind: sourceLineageOnly | SoTAActionLineage | modelBased, as actually grounded
  evidenceOrCausalGoverningPatternRefIfLive?: C.28 / B.3 / A.10 / G.6 when the stronger claim is live
  nonAdmissibleUse: causal proof or assurance by slogan
```

Open `ArchitectureCharacteristicQBundleRelationRecord` only when publication, comparison, causal use, evidence reliance, assurance, gate, decision, or reusable cross-case relation reliance needs the fuller record. The useful move is to decide whether a structural characteristic has a bounded relation to a maintainability slot, not to accept the slogan as architecture truth.

**"We replaced the neural-network block, so the architecture improved."** The phrase is admissible architecture recognition only after the changed structure kind, flow or transduction relation, module or interface claim kind, preserved and lost structure, changed characteristic, source-relation object, and decision or evidence governing patterns are named. A block label, benchmark result, ablation, pruning mask, or distillation result is not an architecture decision, evidence sufficiency, gate passage, assurance, or architecture adequacy by itself.

