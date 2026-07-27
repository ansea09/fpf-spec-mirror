---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Grounded Architecture and Selected-Structure Adequacy"
section_id: "C.30:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__005_solution.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "C.30 — Grounded Architecture and Selected-Structure Adequacy"
  - "C.30:4 — Solution"
line_start: 58911
line_end: 59331
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
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
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.MLAO"
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
  - "G.5"
  - "G.6"
keywords:
  - "ArchitectureOf@Context"
  - "architecture claim"
  - "architecture question card"
  - "architecture-description boundary"
  - "artifact-as-architecture guard"
  - "candidate architecture use"
  - "grounded architecture"
  - "selected structure"
---

### C.30:4 - Solution

C.30 starts from one architecture move over one described `U.Holon` in one `U.BoundedContext`: recover the `ArchitectureOf@Context` claim record when it is being claimed, selected `U.Structure` references, structure kind refs, the source, description, view, or publication role of the inspected material, and first admissible architecture move. Use a conditional architecture-description bridge when durable, reusable, multi-view, regulated, comparison, or reliance-bearing description is being made. If `ArchitectureQuestionCard@Project` gives one usable next architecture candidate use, stop there.

In C.30, the EntityOfConcern for this use is the architecture claim, one of its selected structures, or the relation record or claim record named by value for the architecture use being made. The description is not the architecture itself, and description hygiene is not the center of C.30.

Architecture-description material in C.30 is deliberately minimal. C.30 itself is not the full architecture-description mechanism. It binds `ArchitectureDescription@Context` to `ArchitectureOf@Context`, selected structures, structural views, correspondence, source return, and admissible use only when durable description use is being made. `C.30.AD` carries the full general architecture-description EntityOfConcern: multi-view description sets, viewpoint-based views, correspondences, source return, freshness, specification use, and publication boundary over `ArchitectureOf@Context`. `C.30.AD.BA` carries built-asset architecture-description, asset-information, digital-twin, and reference-designation specialization. Generic Description, view, viewpoint, publication-face, and publication-form machinery still remains in A.7, E.17.0, E.17.1, E.17.2, and E.17. C.30.ASV carries the selected-structure-kind-to-view relation; C.30.TFS-REL, C.30.LCA, and other named subpatterns carry named structure relations.

C.30 does not mint `U.Architecture` and does not redefine `U.Viewpoint`. It specializes A.22 structure records and `U.MultiViewDescribing` only for architecture descriptions whose DescriptionContext `EntityOfConcernRef` is the `ArchitectureOf@Context` claim record for a holon, while preserving the EntityOfConcern and Description-episteme and specification-use distinction between architecture and its descriptions. Use A.1 for `U.Holon`, A.22 for selected `U.Structure`, and E.24.PUB when the problem is a confusion among ontic, ontic-description episteme, and publication form.

C.30 governs grounded architecture adequacy for one `ArchitectureOf@Context` claim record over selected `U.Structure` references for one described holon in one bounded context. It governs `ArchitectureOf@Context`, `ArchitectureQuestionCard@Project`, selected architecture-relevant structures, architecture structure-kind recovery, source, description, view, or publication-role recovery, first architecture-question assignment, characteristic assignment, small boundary notes, and the thin `ArchitectureDescription@Context` bridge when durable description use is being made. It does not mint `U.Architecture` and does not govern all architecture structure-kind views; `C.30.ASV` governs architecture structural views, and `C.30.AD` governs the full architecture-description mechanism. Generic guards about publication, deontic permission, promise, evidence sufficiency, gate passage, work authorization, decision claim, or release authorization stay in the publication-use boundary or in governing patterns.

#### C.30:4.1 - Architecture claim record

```text
ArchitectureOf@Context ::= {
  describedHolonRef: U.HolonRef,
  boundedContextRef: U.BoundedContextRef,
  structureRefs: FinSet(U.StructureRef),
  structureKindRefs: FinSet(ArchitectureStructureKindRef),
  architectureConcernCue?,
  governingArchitectureConcernRefs?,
  architectureConcernNotes?,
  structuralRelationRecordRefs?,
  admissibleUse,
  nonAdmissibleUse
}
```

`ArchitectureOf@Context` is a project-side architecture claim record over selected structures. It is not the selected structure itself, not a Description episteme, not a view, not a diagram, not a publication face, not a decision, and not a new root `U.*` kind.

`ArchitectureOf@ContextRef` is admissible as a `DescriptionContext.EntityOfConcernRef` for architecture Description epistemes and views. The holon whose architecture is claimed remains `ArchitectureOf@Context.describedHolonRef`; it is not the DescriptionContext `EntityOfConcernRef` for those architecture descriptions unless a separate direct holon description is being made.

**EntityOfConcern bridge.** In C.30, the primary `EntityOfConcern` is the `ArchitectureOf@Context` claim record, one of its selected structures, or a related relation record or claim record selected by the use under repair. Selected architecture structure is dependent, non-agentive, and claim-bearing through episteme or view records, but it is not a second EntityOfConcern family beside `EntityOfConcern`. Publication faces, forms, units, and renderings publish descriptions or views; they do not become the architecture claim or the selected structure.

#### C.30:4.1a - Holonic architecture modes

Recover which holonic architecture mode is current before applying MHT, structure, description, or mathematical-lens language:

| Mode | Current EntityOfConcern | Admissible C.30 use | Boundary |
| --- | --- | --- | --- |
| Direct holonic architecture mode | `ArchitectureOf@Context` over selected structures of one described holon in one bounded context. | Name selected structures, structure kinds, architecture concern, and first architecture move. | Do not apply MHT merely because the architecture has levels, scopes, parts, modules, or views. |
| Architecture-bound holon mode | An architecture residual raises a whole-reidentification question for a candidate result holon. | Use C.30 only for the architecture residual and selected-structure claim; use `B.2` or `B.2.P` when whole reidentification is current. | `MHTTriggerProfile` is not a general architecture heuristic. |
| Non-holonic description, record, or mathematical mode | A description, view, diagram, dashboard, model, source relation, publication form, or mathematical-lens result is under repair. | Assign the claim to `C.30.AD`, `C.30.AD.BA`, `C.30.ASV`, `E.17`, `A.10`, `C.29`, or another direct governing pattern. | Do not treat the representation as the architecture or as MHT evidence by label. |

#### C.30:4.1b - Evolutionary-engineering architecture candidate bridge

Use this bridge when an open-ended search, quality-diversity archive, current pool, front, or selected set contains possible architecture moves. The archive or front is not yet an architecture claim. It becomes C.30 material only when the current claim names `ArchitectureOf@Context`, the selected structure or structure kind, the affected architecture characteristic, and the next architecture move.

```text
ArchitectureCandidateMove@Context:
  CandidateSetOrArchiveRef:
  ArchitectureOfRef:
  SelectedStructureOrStructureKindRef:
  AffectedArchitectureCharacteristicRef:
  CandidateMoveClaim:
  SelectedSetPublicationRef?:
  LocalChoiceRef?:
  PatternUseRecommendationRef?:
  WorkPlanRef?:
  WorkEntryReadinessRef?:
  GateDecisionRef?:
  PerformedWorkRef?:
  StopCondition:
```

`ArchitectureCandidateMove@Context` is a thin architecture-candidate use record over an `ArchitectureOf@Context` claim. It records why a generated, retained, front-member, or selected-set variant can be considered as architecture material; it is not a work plan, local choice result, selected-set publication, or new kind.

If the current work is archive generation, front maintenance, current-pool treatment, selected-set publication, or local choice, use `C.18`, `C.19`, `G.5`, or `C.11` before C.30 relies on it. If the selected architecture move is a recommended FPF pattern use, cite `E.11.PUR`. If it is ready to enter planning, work-entry readiness, gate decision, or performed work, use `A.15.2`, `A.15.5`, `A.21`, or `A.15.1` respectively. C.30 keeps only the architecture claim: which architecture of which entity in which context, which selected structure matters, which characteristic changes, and which architecture candidate use is admissible next.

In C.30, architecture-move wording is practitioner shorthand for an architecture-candidate use over an `ArchitectureOf@Context` claim. It does not create a root `U.Move`, WorkPlan, readiness relation, gate decision, performed work, decision, or source-use claim by itself. When source wording uses "move" outside this architecture-candidate use, restore the concern through `E.10.MOVE` and name the direct governing pattern.

When the useful next work is synthesizing candidate architecture variants rather than judging or repairing one grounded architecture claim, stop the C.30 question card after the described holon, bounded context, selected structure or structure kind, architecture concern, and admissible next use are named.
Apply `C.32` only to build the candidate architecture palette.
If the next claim is comparison, selector-policy use, selected-set publication, final local choice, project architecture decision, evidence, assurance, gate, release, or performed work, send the palette or candidate reference to `A.19.CPM`, `A.19.SelectorMechanism`, `G.5`, `C.11`, `C.32.PAD`, `A.10`, `B.3`, `A.20`, `A.21`, or `A.15` when that claim is current.

#### C.30:4.2 - Conditional architecture-description bridge



C.30 does not define a second local `ArchitectureDescription@Context` record shape. The canonical `ArchitectureDescription@Context` record is governed by `C.30.AD:4.1`. C.30 admits only a thin bridge to that record when durable architecture-description use changes the first architecture move.

The minimum bridge recoverable in C.30 is:

```text
C30ArchitectureDescriptionBridge minimum:
  architectureClaimRef: ArchitectureOf@ContextRef
  selectedStructureRefs or structureKindRefs:
  architectureStructuralViewRefs? only when a structural view is being used
  admissibleUse:
  nonAdmissibleUse:
  correspondenceRefs or sourceReturnCondition? when reuse, cross-view use, or source return is needed
  freshnessCueRefs? when currentness bounds the admissible use
```

This bridge does not mint another `ArchitectureDescription@Context` definition, does not add local fields to the canonical record, and does not collect non-architecture claim kinds as architecture-description ontology. It lets the C.30 reader say why a description matters for the next architecture move, then applies `C.30.AD` whenever the architecture description itself becomes the `EntityOfConcern` under repair or the full mechanism is needed: multi-view composition, correspondence, source return, freshness, specification-use boundary, publication-use boundary, or reusable architecture-description use.

An architecture-description freshness cue is also canonical in `C.30.AD:4.4`. C.30 may point to that cue only to bound the admissible use of the first architecture move; the cue is not evidence sufficiency and not assurance.

#### C.30:4.3 - Publication-use boundary

This subsection is the C.30 publication-use boundary. It says what an architecture description or its publication does not carry by itself, while the subject Solution stays about architecture claim, described holon, selected structures, structural views, and the next architecture move. If a guard concerns deontic permission, promise, prescription, evidence sufficiency, assurance, decision, gate passage, work authorization, release authorization, source authority, or publication-use authority, keep it here, in `C.30.AD`, or in the description or publication pattern governing that claim rather than expanding C.30's thin bridge.

```text
ArchitectureDescriptionPublication@Project ::= {
  sourceEpistemeRef | sourceViewRef,
  publicationViewpointRef?,
  publicationScopeId,
  boundedContextRef,
  mvpkFaceRef,
  publicationFormRef,
  sourcePinSetRef,
  audience,
  admissiblePublicationUse,
  nonAdmissiblePublicationUse
}
```

`ArchitectureDescriptionPublication@Project` is subordinate to E.17 and MVPK machinery. It publishes one source episteme or episteme-lane view reference. `publicationViewpointRef?` names the publication-side viewpoint only when MVPK needs one; it is not an architecture viewpoint and not a TEVB viewpoint. `mvpkFaceRef` is a publication-lane face reference, not an alternative source episteme, source view, or source relation. Publication does not establish non-publication claims; apply `C.30:4.3` and the governing pattern when evidence, gate, work, assurance, decision, or release claims are current.

Model cards, system cards, and evaluation harness reports enter C.30 through the same publication boundary or source-relation boundary. They may describe a model, deployed AI system, architecture claim, evaluation harness, or policy, but the architecture move still needs `ArchitectureOf@Context`, selected structures, and any proof, release, or gate claim assigned to its governing pattern.

```text
ModelCardOrSystemCardBoundaryNote@Project ::= {
  sourcePublicationRef,
  entityOfConcernRef,
  entityOfConcernKind:
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

If the card or harness is used beyond transparency, recover the architecture structure kind being used first and then apply `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `C.16`, `C.28`, or `C.11` for the non-architecture claim kind.

#### C.30:4.4 - Architecture name formation

The word `architecture` is shorthand only after the described holon, bounded context, selected structures, structure kind, and source, description, view, or publication role are recoverable. Without those qualifiers, it is a recovery trigger, not a stable FPF term.

```text
ArchitectureNameFormationRule:

If a text says "<X> architecture", then the FPF-governed use is conforming only with:
  describedHolonRef,
  boundedContextRef,
  structureKindRef = <X>StructureKind or declared local relation,
  structureRefs,
  ArchitectureStructuralViewRefs if this is a description or view claim,
  admissibleUse,
  nonAdmissibleUse.

If <X> is not a declared structure kind, the phrase is plain recognition wording only.
```

| Phrase | Required recovery |
| --- | --- |
| functional architecture | `structureKindRef = FunctionalStructure`; functions, effects, capabilities, and functional dependencies named as structure content; transformation-flow structures, paths, and flow valuations are assigned to `TransformationFlowStructure` or `C.30.TFS-REL`. |
| modular architecture | `structureKindRef = ModuleInterfaceStructure`; module relation records, interface specifications, substitutability rule, and change policy. Full module-and-interface repair applies the module-and-interface repair pattern when that claim kind is being made. |
| logical architecture | `structureKindRef = DeclaredLogicalStructure`; local definition says whether `logical` means information relation, functional relation, runtime relation, responsibility relation, allocation relation, or another relation class. |
| physical architecture | `structureKindRef` in `{MaterialSpatialStructure, PlacementDeploymentStructure}` or a locally declared physical structure kind. |
| control architecture | `structureKindRef = ControlStructure`; an LCA record may describe the control structure, but proof claims are assigned to dynamics, temporal, causal, evidence, safety, or assurance patterns as triggered. |
| information architecture | `structureKindRef = InformationDataStructure`; state bearer and residence, schema refs, semantic refs, persistence locus, provenance relation, custody relation, and source-return conditions. |
| security architecture | `structureKindRef = SecurityTrustBoundaryStructure`; recover protected asset or effect, trust boundary, adversarial path, authority or privilege relation, secure-default or hardening boundary, and evidence, assurance, or gate governing patterns when those claim kinds are being made. |

#### C.30:4.5 - Architecture characteristic assignment

C.30 uses three bearers before any `quality`, `fitness`, `measure`, `metric`, `score`, `modularity`, or `ility` wording carries an architecture-adequacy claim. Those words are triggers for bearer recovery, not stable architecture adequacy by themselves.

```text
ArchitectureCharacteristicAssignment:

A. SystemQualityAffectedByArchitecture
   Bearer: described U.Holon, named product holon, or named system holon
   Governing pattern: C.25 Q-Bundle or C.16
   Examples: maintainability, evolvability, resilience, availability, safety, observability

B. ArchitectureStructuralCharacteristic
   Bearer: `ArchitectureOf@Context` claim, architecture structural view, declared structural relation or constraint, module relation, or interface relation
      Governing pattern: selected from C.16, A.17-A.19, C.25, or the characteristic-space or Q-bundle pattern governing the characteristic claim
   Examples: coupling, cohesion, interface alphabet, substitutability, hidden coupling, reusable-structure share

C. ArchitectureAdequacyBearer
   Bearer: one selected architecture adequacy bearer: `ArchitectureOf@Context`, selected architecture-relevant structure, `ArchitectureDescription@Context` when durable description use is being made, architecture structural view, or correspondence model
   Governing pattern: selected from C.30 for grounded architecture and selected-structure adequacy, E.17 for publication-face and view discipline, C.16.Q for quality-term precision, or C.16 for measurement and characterization
   Examples: viewpoint coverage, correspondence adequacy, source-return adequacy, description modularity
```

C.30 keeps only a thin bridge from structural characteristics to Q-Bundle relevance. If the claim says architecture causes an outcome improvement, assign the causal-use claim to `C.28` before causal use. If a structural characteristic is used as a mechanism, constraint, predictor, proxy, evidence relation, or causal hypothesis for a Q-Bundle slot, start with `ArchitectureStructuralCharacteristicQBundleRelationLine` rather than a formula such as `low coupling = maintainability`; assign measurement, modularity scoring, reusable-structure accounting, bespoke-residue accounting, evidence, assurance, gate, causal, and scale-audit claims to their governing patterns.

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
    structuralCharacteristicEvidenceRelationForQBundleSlot(A.10-governed evidence relation only when evidence provenance is the claim being made),
  relationGroundingKind:
    modelBased | empirical | causalModelBased | expertJudgement |
    sourceLineageOnly | SoTAActionLineage | reportOnly,
  evidenceOrCausalGoverningPatternRef?,
  nonAdmissibleUse
}
```

Minimal structural-characteristic relation-line examples:

| Structure kind | Structural characteristic cue or relation | Affected Q-Bundle slot | Relation grounding note | Non-admissible use |
| --- | --- | --- | --- | --- |
| `ModuleInterfaceStructure` | Stable interface specification plus substitution policy. | Evolvability or replaceability. | Replacement without global retesting. | Open label as substitutability proof. |
| `PlacementDeploymentStructure` | Controller placed near plant or edge-node locality. | Latency, resilience, or jurisdictional compliance. | Reduced communication delay and bounded data custody. | Placement diagram as performance or regulatory acceptance proof. |
| `InformationDataStructure` | State bearer, residence, provenance, and custody boundary. | Observability, privacy, or auditability. | Recoverable state lineage and bounded custody. | Data schema as evidence sufficiency. |
| `MaterialSpatialStructure` | Physical separation, adjacency, or energy path. | Safety, maintainability, or energy efficiency. | Isolation, accessibility, or loss reduction. | Geometry as safety proof. |
| `ControlStructure` | Observer-controller-plant loop with rate envelope. | Stability, controllability, or safety. | Feedback and bounded actuation relation. | Control diagram as proof. |
| `TransformationFlowStructure` | Path crossing, bottleneck, buffer boundary, or waiting-line boundary. | Latency, throughput, or resilience. | Recoverable path, crossing, capacity, and valuation relation. | Flow diagram or mathematical graph description as performance or causal proof. |
| `SecurityTrustBoundaryStructure` | Trust boundary, privilege path, or untrusted-input crossing. | Security, abuse resistance, or privacy. | Reduced exposed authority and bounded trust crossing. | Risk color or compliance label as security proof. |
| `EvidenceAssuranceStructure` | Evidence package reused across variants. | Assurance maintainability or release readiness. | Explicit affected-structure and source-return boundary. | Evidence-structure view as assurance verdict. |
| `WorkMethodStructure` | Method description, work plan, or work enactment relation with explicit exception path. | Operability, auditability, or maintainability. | Bounded repeatability and recoverable exception handling. | Work-method diagram as work authorization or evidence sufficiency. |

`ArchitectureCharacteristicQBundleRelationRecord` is a triggered full-mode record, not the ordinary first-contact shape. Use the full record only when publication, comparison, causal use, evidence reliance, assurance, gate, decision, or reusable cross-case relation reliance is being claimed and the thin line cannot keep the relation inspectable, reusable, or bounded. This preserves the protection against causal or quality overread without turning C.30 into a measurement-first pattern.

Relation kinds in this record are C.30-local relation tokens. They must remain recoverable as A.6.P-style relation specifications: polarity, participant slots, qualifiers, witness expectations, admissible semantic change classes, and bridge or loss boundary where those boundary conditions are being claimed.
ISO/IEC 25010-like quality models may be used as quality vocabulary or comparison lineage for product qualities such as reliability, security, maintainability, usability, efficiency, compatibility, or portability. C.30 does not inherit them as architecture theory. Architecture relates to qualities through Q-Bundle slots, mechanism slots, relation class or admissible-use value, evidence or causal governing patterns, or report-only use.

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
    structuralCharacteristicEvidenceRelationForQBundleSlot(A.10-governed evidence relation only when evidence provenance is the claim being made),
  participantSlots:
    structuralCharacteristicRef,
    qBundleSlotRef,
    architectureClaimRef,
    scopeOrScaleWindow?,
    viewpointRef?,
  qualifiers?,
  witnessExpectations?,
  relationGroundingKind:
    modelBased | empirical | expertJudgement |
    sourceLineageOnly | SoTAActionLineage | causalModelBased | reportOnly,
  bridgeOrLossBoundary?,
  admissibleUse,
  nonAdmissibleUse,
  evidenceOrCausalGoverningPatternRef?
}
```

#### C.30:4.6 - Relation to structural views

`C.30.ASV` governs `ArchitectureStructuralView@Context`. C.30 governs the `ArchitectureOf@Context` claim and, only when durable description use is being made, how its thin `ArchitectureDescription@Context` bridge uses structural views, with hidden or lost structure, correspondence, source or reliance relation, and source-return boundaries recoverable when those boundaries affect action. `C.30.AD` governs the full architecture-description mechanism.

A diagram, model, table, selected transformation-flow diagram, mathematical graph description, LCA diagram, C.29 lens output, ADR, dashboard, generated explanation, or other publication face may carry an architecture description or an architecture structural view. It does not become the architecture, and it does not become a conforming view only because it looks like a view.

Use `AffectedArchitectureStructureNote` when the next architecture move needs to name affected structures or view losses without using an architecture decision, ADR, gate, evidence, assurance, or release record:

```text
AffectedArchitectureStructureNote:
  architectureClaimRef:
  affectedStructureKindRefs:
  affectedStructureRefs?:
  affectedArchitectureStructuralViewRefs?:
  acceptedOrSuspectedViewLoss?:
  sourceReturnCondition?:
  nextAdmissibleUse:
```

This note only names affected architecture structure for the next architecture use. Decision, ADR, gate-passage, evidence-sufficiency, and release-authorization claims apply the patterns governing those claims.

#### C.30:4.7 - Minimal boundary notes

Use these notes when a common architecture phrase is close to a governing pattern but the full governing-pattern application is not yet needed for an asserted claim.

Use the thinnest relation form that preserves the next architecture move. Use a fuller governing relation record only when the relation being used cannot be inspected, compared, refreshed, or bounded without it. Typical thin forms are `ArchitectureMathLensUseBoundary` before C.29 Mini or Full, `AffectedArchitectureStructureNote` before an architecture decision record, and `ArchitectureStructuralCharacteristicQBundleRelationLine` before full measurement records, causal records, or evidence records.

```text
InterfaceSignatureBoundaryNote ::= {
  phraseOrArtifactRef,
  apparentClaim:
    interface | signature | port | endpoint | connector | link |
    API | protocol | E.18 transformation-flow relation | E.18 transformation-flow path | mechanism reference,
  recoveredKind,
  governingPatternApplicationRefs,
  admissibleUse,
  nonAdmissibleUse
}

ModuleRelationBoundaryNote ::= {
  phraseOrArtifactRef,
  apparentClaim:
    module | component | package | platform | open architecture |
    recoveredModuleInterfaceSourceLabel |
    typed control-structure relation,
  moduleInterfaceRepairClaimCurrent?: yes | no,
  openOrPlatformClaimCurrent?: yes | no,
  selectedModuleInterfaceRelationRefs?,
  variationPointRef?,
  substitutabilityPolicyRef?,
  interfaceConformanceEvidencePatternRef?,
  changePolicyOrRelationRef?,
  consumerMigrationBoundary?,
  versionOrUpdateChannelRef?,
  secureDefaultOrHardeningBoundary?,
  governingPatternApplicationRefs,
  admissibleUse,
  nonAdmissibleUse
}
```

These notes are not substitutes for the module-and-interface repair pattern named by value, interface specifications, signature records, conformance evidence, or module-and-interface repair. An open or platform label is not substitutability proof, security proof, scale proof, assurance, or universal maturity evidence. A source label such as `layer`, `stack`, `block`, `expert`, `cache`, `router`, or `gate` enters this note only after `C.30.STRAT` recovers a module-interface or adjacent architecture-relevant item. It becomes architecture-relevant only through local structure, interface, variation, substitution, migration, update, and hardening boundaries. Relation-heavy wording inside these notes remains a Plain cue until a module relation reference named by value, interface relation ref, relation governing the asserted use record, or governing FPF pattern application is named. The note keeps first use honest until the non-architecture claim kind named by value is being made.

#### C.30:4.8 - Architecture mathematical-lens boundary

Architecture descriptions may use C.29 lenses, but the lens does not become architecture ontology.

```text
ArchitectureMathLensUseBoundary:
  noMLUNeeded?: yes | no
  lensOneLine?:
    lensRef,
    structureClaimRef,
    preservedStructure,
    lostStructure,
    lensRelationKind,
    stopCondition,
    governingPatternApplicationRefs?
```

Use the one-line boundary only when it is enough to keep the lens from being overread. Use a C.29 Mini or Full card when the lens choice, preserved structure, lost structure, relation class or admissible-use value, or stop condition changes the architecture move.

Lens use by architecture problem:

| Architecture problem | Candidate mathematical lens | Preserved structure | Typical loss or stop |
| --- | --- | --- | --- |
| Hidden dependency or modularity. | Typed graph, DSM, or hypergraph. | Dependency, coupling, or clustering. | Semantics, interface law, evidence, and work remain outside unless bridged. |
| Flow bottleneck. | Transformation-flow structure, network flow, or queueing. | Path, crossing, valuation, and capacity. | Purpose, proof, causality, and safety remain non-architecture claims. |
| Control-rate mismatch. | LCA, hybrid systems, assumption-guarantee relations, or control relations. | Feedback roles and scale or rate relations. | Stability proof and safety proof remain outside the lens. |
| Cross-scope residual. | Coarse-graining or renormalization-group-style lens. | Preserved and lost structure across scale. | Utility, causal-use claims, and selector authority remain outside unless separately grounded. |
| Extracted structure from traces. | Epiplexity or MDL-style bounded-observer lens. | Learnable structural regularity. | Task relevance, assurance, and causal proof remain non-architecture claims. |
| Physical separation or spatial arrangement. | Topology, geometry, or spatial graph lens. | Adjacency, containment, separation, reachability, energy-transfer relation, or material-transfer relation. | Safety proof, accessibility, regulatory acceptance, and causal-use claims remain outside unless separately grounded. |
| Composition relation. | Category, open-systems, or compositional lens. | Interface, composition, and coherence. | Domain semantics remain outside unless bridged. |

This table is not a C.29 replacement and does not make mathematics mandatory. It helps the practitioner see when a lens may add a useful architecture move; C.29 still carries lens-use result, preserved structure, lost structure, relation class or admissible-use value, and stop condition when those description or view uses are being made.

Epiplexity-like use remains a C.29 bounded-observer structural-information lens. It may help recover learnable structure from traces, but it is not an architecture quality, task relevance proof, causal proof, assurance, or selector authority.

#### C.30:4.9 - Boundary and repair table

| Tempting collapse | C.30 repair |
| --- | --- |
| Bare architecture as free-floating selected claim | Recover `ArchitectureOf@Context`, `describedHolonRef`, `boundedContextRef`, selected `structureRefs`, selected `structureKindRef`, source, description, view, or publication role for inspected material, `admissibleUse`, and `nonAdmissibleUse`. |
| Architecture description as architecture | Keep `ArchitectureDescription@Context` as Description episteme or specification-use case over `ArchitectureOf@Context`. |
| Diagram, model, table, dashboard, or generated relation graph as architecture | Treat it as publication form, description, view, source relation, or source-finding aid only when that relation is explicit. |
| Module diagram as all architecture | Use `C.30.ASV` to recover structure kind; module structure and interface relation are only one structure family. |
| Transformation-flow structure or graph description as architecture | Use E.18 for selected transformation-flow structure, path, and crossing records; use E.18.2 and C.29 for mathematical graph descriptions; use C.30.TFS-REL for the architecture-to-transformation-flow relation. |
| LCA diagram or control diagram as proof | Use `C.30.LCA` for control-structure view; assign dynamics, temporal, causal, evidence, gate, safety, and assurance claims to their governing patterns. |
| Mathematical lens as architecture ontology | Use `C.29`; cite `MathLensUseOutputRef` only through an `ArchitectureMathLensUseBoundary` or C.29 lens record and state stop condition. |
| ADR as architecture decision | Use the project-side architecture decision pattern when a decision claim is being made; ADR is a publication form, not the decision. |
| Quality, score, or measurement term as architecture adequacy | Recover the bearer through ArchitectureCharacteristicAssignment; assign the claim being made to C.25, C.16, A.17-A.19, the characteristic-space or Q-bundle pattern governing the characteristic claim, or C.30 grounded architecture, selected-structure, or conditional description-use scope. |
| Architecture record as evidence, assurance, gate, work, or release | Assign evidence, assurance, gate, work, or release claims to A.10, G.6, B.3, A.20, A.21, A.15, or the release locus named by value when a release claim is being made. |
| Architecture as agent, worker, controller, gate, or proof | Recover the mechanism, control relation, role and enactor relation, gate, work, evidence, or assurance record that carries enforce, decide, optimize, adapt, prove, or guarantee wording; keep `ArchitectureOf@Context` as a selected-structure claim, not an acting entity. |

#### C.30:4.10 - Worked slices

**"We have the architecture in this diagram."** The diagram is a publication face unless it explicitly publishes an `ArchitectureDescription@Context` or `ArchitectureStructuralView@Context`.

```text
ArchitectureQuestionCard@Project:
  describedHolonRef: payment system
  boundedContextRef: checkout platform context
  architectureConcernCue: descriptionViewLoss or flowBottleneck
  sourcePhrase?: "architecture in this diagram"; unclear dependency between payment orchestration and fraud scoring
  questionDisposition: architectureClaimReady
  inspectedMaterialRole: diagram as publication face carrying possible architecture structural-view material
  selectedStructureKindRefs: FunctionalStructure, ModuleInterfaceStructure, TransformationFlowStructure
  firstArchitectureMove: recover the diagram as a publication face and create a minimal architecture structural-view note
  governingPatternApplicationRefs: C.30.ASV
  non-admissible overread: treating the diagram as architecture itself, evidence, assurance, gate passage, or decision
```

**"Low coupling gives maintainability."** C.30 does not allow that formula to carry the claim by itself. The ordinary repair starts with the thin relation line:

```text
ArchitectureStructuralCharacteristicQBundleRelationLine:
  architectureClaimRef: ArchitectureOf@ContextRef
  structuralCharacteristicCueOrRef: coupling under module relation or interface relation
  affectedQBundleSlotRef: maintainability Q-Bundle slot
  qBundleRelationKind: structuralCharacteristicRelevantToQBundleSlot
  relationGroundingKind: sourceLineageOnly | SoTAActionLineage | modelBased, as actually grounded
  evidenceOrCausalGoverningPatternRef?: one selected governing pattern reference: C.28, B.3, A.10, or G.6 when evidence sufficiency, causal-use, assurance, or safety-case claim is being made
  nonAdmissibleUse: causal proof or assurance by slogan
```

Use `ArchitectureCharacteristicQBundleRelationRecord` only when publication, comparison, causal use, evidence reliance, assurance, gate, decision, or reusable cross-case relation reliance needs the fuller record. The useful move is to decide whether a structural characteristic has a bounded relation to a maintainability slot, not to accept the slogan as architecture truth.

**"The backup-pump architecture is safe because the loop is redundant."** C.30 starts with the plant holon, bounded operating context, and selected structures: control loop, material-flow structure, placement structure, module-interface relation, and maintenance-work relation. The redundancy phrase may motivate an architecture move, but safety proof, causal proof, evidence sufficiency, gate passage, and work authorization go to their governing patterns. The C.30 output is the selected structure and next architecture move, not a safety case by slogan.

**"We replaced the neural-network block, so the architecture improved."** Treat `block` first as a source label and apply `C.30.STRAT` unless the changed value is already recovered. The phrase is admissible architecture recognition only after the changed structure kind, transformation-flow relation, module or interface claim kind, preserved and lost structure, changed characteristic, source relation, and decision or evidence governing patterns are named. A block label, benchmark result, ablation, pruning mask, or distillation result is not an architecture decision, evidence sufficiency, gate passage, assurance, or architecture adequacy by itself.

