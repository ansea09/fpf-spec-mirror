---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Grounded Architecture and Selected-Structure Adequacy"
section_id: "C.30:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__005_solution.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "C.30 — Grounded Architecture and Selected-Structure Adequacy"
  - "C.30:4 — Solution"
line_start: 59589
line_end: 60083
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

C.30 starts from one architecture move over one exact `U.Holon`. Recover separately: any actual subject-relation occurrences; the exact A.22 structures selected from them; any obtaining `ArchitectureRelation`; the claim episteme that states an affirmative, negative, unresolved, candidate, or expected architecture claim; the concern and admissible-use frame; and the source, description, view, representation, or publication role of the inspected material. Use a conditional architecture-description bridge when durable, reusable, multi-view, regulated, comparison, or reliance-bearing description is being made. If `ArchitectureQuestionCard@Project` gives one usable next architecture candidate use, stop there.

In C.30, the EntityOfConcern is one exact described holon, one exact `ArchitectureRelation` occurrence, one exact selected structure, or another exact subject object selected by the current claim. A claim episteme, description, diagram, or publication is not a proxy EntityOfConcern for a world-side relation or structure. Description hygiene supports this boundary but is not the center of C.30.

Architecture-description material in C.30 is deliberately minimal. C.30 itself is not the full architecture-description mechanism. It gives a thin bridge from the exact holon, architecture relation, or selected structure to a separately constituted architecture-description episteme only when durable description use changes the architecture move. `C.30.AD` carries the full general architecture-description EntityOfConcern: multi-view description sets, viewpoint-based views, correspondences, source return, freshness, specification use, and publication boundary. `C.30.AD.BA` carries built-asset architecture-description, asset-information, digital-twin, and reference-designation specialization. Generic episteme, view, viewpoint, publication, form, representation, and carrier machinery remains with C.2.1, E.17.0, E.17.1, E.17.2, E.17, E.24.PUB, and C.29. C.30.ASV carries the selected-structure-to-view branch; C.30.TFS-REL, C.30.LCA, and other named subpatterns carry their direct structure relations and claims.

C.30 does not mint `U.Architecture` and does not redefine `U.Viewpoint`. It directly governs `ArchitectureRelation`, the architecture claim form, `ArchitectureQuestionCard@Project`, selected architecture-relevant structures, structure-kind recovery, architecture concern and admissible-use framing, source/description/view/publication-role recovery, first architecture-question assignment, characteristic-claim assignment, small boundary notes, and the thin description bridge. It does not make descriptions or views conform merely by form and does not govern all architecture structure-kind views. Generic guards about publication, deontic permission, promise, evidence sufficiency, assurance, decision, gate passage, work authorization, or release authorization stay in their direct patterns.

#### C.30:4.1 - Direct architecture relation and architecture claim

C.30 keeps one subject-side relation and one claim-bearing episteme distinct.

**Direct relation kind.** `ArchitectureRelation` is a C.30-governed direct dependent `U.Relation` between exactly two actual participants:

1. `architectureBearingHolonRef` — the exact `U.Holon` whose realized organization is at issue; and
2. `selectedArchitectureStructureRef` — one exact `U.Structure` selected under A.22 from declared constituents, obtaining subject-relation occurrences, applied constraints and invariants, and an admissible-use frame.

The relation is applicable only when the structure's exact constituents and selected subject-relation occurrences are recoverable for that holon or its admitted constituents and the structure is being used as architecture-relevant organization of that holon. Its obtaining predicate is satisfied only when the selected structure is actually constituted under A.22, every selected subject relation required by that structure obtains under its direct owner, and those constituents and relations organize the exact holon in the declared way. A planned, required, desired, expected, modeled, diagrammed, listed, or merely published structure does not satisfy this predicate.

Occurrence identity is the exact participant pair over one maximal continuous interval during which that predicate remains satisfied. A different holon, a differently identified A.22 structure, or cessation followed by later renewed obtaining yields another occurrence. A changed concern, claim scope, effective reference scheme, description, viewpoint, view, representation, publication, or carrier does not by itself reidentify or create the relation. Ordinary prose may state the readable relation and stop; use A.6.REL only when a later receiver must distinguish this occurrence from another one.

**Architecture claim episteme.** `ArchitectureClaim` is an ordinary C.2.1 `U.Episteme`, not the direct relation and not a new architecture kind:

```text
ArchitectureClaim ::= {
  claimEpistemeRef: U.EpistemeRef,
  entityOfConcernRef:
    describedHolonRef | architectureRelationRef | selectedStructureRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue,
  claimScope?: U.ClaimScope, byValue,
  content: {
    describedHolonRef: U.HolonRef,
    architectureRelationAssertion:
      obtains | doesNotObtain | unresolved | candidateOrExpectedOnly,
    architectureRelationRefs?: FinSet(U.RelationRef),
    selectedStructureRefs?: FinSet(U.StructureRef),
    candidateOrExpectedStructureRefs?: FinSet(U.StructureRef),
    structureKindRefs: FinSet(ArchitectureStructureKindRef),
    architectureConcernClaimRefs?: FinSet(U.EpistemeRef),
    architectureConcernCue?: Plain recognition wording,
    admissibleUse,
    nonAdmissibleUse
  },
  modelUseStructureRef?: U.StructureRef,
  empiricalGroundingRelationRef?: U.RelationRef
}
```

The C.2.1 identity basis is the exact content, one exact `entityOfConcernRef`, and effective `U.ReferenceScheme`. `claimScope` qualifies what the claim covers. `modelUseStructureRef` appears only when one independently selected bounded-model-use structure changes structure interpretation or selection for this receiving use. `empiricalGroundingRelationRef` names a separately obtaining grounding relation; neither grounding nor the optional model-use structure is an `ArchitectureRelation` participant.

For an affirmative actual claim, every `architectureRelationRef` resolves to an obtaining occurrence governed by the direct settlement above and every `selectedStructureRef` is the exact structure participant of one of those occurrences. A negative, unresolved, candidate, required, desired, or expected claim can remain truthful claim content without an obtaining occurrence; it uses no invented positive reference. A description, diagram, graph, file, list, architecture decision, authoring act, or publication may state or carry the claim, but creates neither its truth nor the subject-side relation or structure.

Earlier consumers may still say “open the `ArchitectureOf@Context` form in the current C.30 edition.” In this edition that legacy retrieval instruction resolves to the `ArchitectureClaim` form plus the separate `ArchitectureRelation` settlement above. The suffix supplies no field, participant, scope, scheme, grounding, project identity, or relation fact, and new records use the current names.

**EntityOfConcern bridge.** C.30 may make the described holon, one exact `ArchitectureRelation` occurrence, or one exact selected structure the EntityOfConcern of a claim. A later architecture description independently chooses the exact holon, relation occurrence, or structure it describes under C.2.1; it does not use a claim record as a world-side proxy. Publication occurrences, forms, representations, and carriers remain separate.

#### C.30:4.1a - Holonic architecture modes

Recover which holonic architecture mode is current before applying MHT, structure, description, or mathematical-lens language:

| Mode | Current EntityOfConcern | Admissible C.30 use | Boundary |
| --- | --- | --- | --- |
| Direct holonic architecture mode | One exact `ArchitectureRelation` between a described holon and an actual selected structure, plus any C.2.1 claim about it. | Recover the actual subject relations, selected structure, architecture relation, structure kind, concern, admissible-use frame, and first move. | Do not apply MHT merely because the architecture has levels, scopes, parts, modules, or views. |
| Architecture-bound holon mode | An architecture residual raises a whole-reidentification question for a candidate result holon. | Use C.30 only for the actual-relation or modal-claim architecture residual; use `B.2` or `B.2.P` when whole reidentification is current. | `MHTTriggerProfile` is not a general architecture heuristic. |
| Non-holonic description, record, or mathematical mode | A description, view, diagram, dashboard, model, source relation, publication form, or mathematical-lens result is under repair. | Assign the claim to `C.30.AD`, `C.30.AD.BA`, `C.30.ASV`, `E.17`, `A.10`, `C.29`, or another direct governing pattern. | Do not treat the representation as the architecture or as MHT evidence by label. |

#### C.30:4.1b - Evolutionary-engineering architecture candidate bridge

Use this bridge when an open-ended search, quality-diversity archive, current pool, front, or selected set contains possible architecture moves. The archive or front is not yet an actual architecture relation. It becomes C.30 material only when the current claim names the described holon, the existing or candidate structure and structure kind, the affected architecture characteristic, and the next architecture move.

```text
ArchitectureCandidateMove:
  candidateMoveClaimEpistemeRef: U.EpistemeRef
  architectureClaimRef?: ArchitectureClaimRef
  describedHolonRef:
  currentArchitectureRelationRefs?: FinSet(U.RelationRef)
  currentSelectedStructureRefs?: FinSet(U.StructureRef)
  candidateStructureRefs: FinSet(U.StructureRef)
  candidateStructureKindRefs:
  affectedArchitectureCharacteristicRef:
  candidateMoveClaim:
  candidateSetOrArchiveRef:
  selectedSetPublicationRef?:
  localChoiceRef?:
  patternUseRecommendationRef?:
  workPlanRef?:
  workEntryReadinessRef?:
  gateDecisionRef?:
  performedWorkRef?:
  stopCondition:
```

`ArchitectureCandidateMove` is a thin claim note about a possible structural change. It records why a generated, retained, front-member, or selected-set variant can be considered as architecture material; it is not an obtaining `ArchitectureRelation`, work plan, local choice result, selected-set publication, decision, performed Work, or new kind. Candidate structure content remains modal until the exact structure is constituted and the direct architecture predicate obtains.

If the current work is archive generation, front maintenance, current-pool treatment, selected-set publication, or local choice, use `C.18`, `C.19`, `G.5`, or `C.11` before C.30 relies on it. If the selected architecture move is a recommended FPF pattern use, cite `E.11.PUR`. If it is ready to enter planning, work-entry readiness, gate decision, or performed work, use `A.15.2`, `A.15.5`, `A.21`, or `A.15.1` respectively. C.30 keeps only the architecture claim: which exact holon and current relation are at issue, which candidate structure matters, which characteristic may change, and which next use is admissible.

Architecture-move wording creates no root `U.Move`, structure, relation, WorkPlan, readiness relation, gate decision, performed work, decision, or source-use claim by itself. When source wording uses “move” outside this architecture-candidate use, restore the concern through `E.10.MOVE` and name the direct governing pattern.

When the useful next work is synthesizing candidate architecture variants rather than judging or repairing one grounded actual relation, stop the C.30 question card after the described holon, current/candidate structure distinction, structure kind, concern, admissible-use frame, and admissible next use are named. Apply `C.32` only to build the candidate architecture palette. If the next claim is comparison, selector-policy use, selected-set publication, final local choice, project architecture decision, evidence, assurance, gate, release, or performed work, send the palette or candidate reference to `A.19.CPM`, `A.19.SelectorMechanism`, `G.5`, `C.11`, `C.32.PAD`, `A.10`, `B.3`, `A.20`, `A.21`, or `A.15` when that claim is current.

#### C.30:4.2 - Conditional architecture-description bridge

C.30 does not define a second local `ArchitectureDescription` record shape. The canonical C.2.1 episteme and its architecture-use specialization are governed by `C.30.AD:4.1`. C.30 admits only a thin bridge when durable description use changes the first architecture move.

The minimum bridge recoverable in C.30 is:

```text
C30ArchitectureDescriptionBridge minimum:
  architectureDescriptionRef: exact U.EpistemeRef
  entityOfConcernRef: exactly one described holon,
    obtaining ArchitectureRelation occurrence, or selected U.Structure
  effectiveReferenceScheme: U.ReferenceScheme, byValue
  architectureClaimRefs?: bounded claim content or trace
  selectedStructureRefs or structureKindRefs:
  architectureStructuralViewRefs?: only for exact description epistemes
    with independently obtaining E.17.0 viewpoint conformance
  viewpointConformanceRelationRefs?:
  admissibleUse:
  nonAdmissibleUse:
  correspondenceClaimOrRelationRefs or sourceReturnCondition?:
    only when reuse, cross-view use, or source return is needed
  freshnessClaimRefs?: only when currentness bounds admissible use
```

This bridge does not mint another description definition, local view-membership relation, subject-side architecture relation, selected structure, or truth fact. It lets the C.30 reader say why an exact description episteme matters for the next architecture move, then applies `C.30.AD` whenever the description itself becomes the EntityOfConcern under repair or the full mechanism is needed: multi-view description-set use, exact viewpoint conformance, correspondence, source return, freshness, specification-use boundary, representation/publication boundary, or reusable architecture-description use.

An architecture-description freshness claim is canonical in `C.30.AD:4.4`. C.30 may point to it only to bound admissible use of the first architecture move; it is not empirical grounding, publication currentness, evidence sufficiency, or assurance.

#### C.30:4.3 - Publication-use boundary

This subsection is the C.30 publication-use boundary. It says what an architecture description or its publication does not carry by itself, while the subject Solution stays about architecture claim, described holon, selected structures, structural views, and the next architecture move. If a guard concerns deontic permission, promise, prescription, evidence sufficiency, assurance, decision, gate passage, work authorization, release authorization, source authority, or publication-use authority, keep it here, in `C.30.AD`, or in the description or publication pattern governing that claim rather than expanding C.30's thin bridge.

```text
ArchitectureDescriptionPublication@Project ::= {
  sourceEpistemeRef | sourceViewRef,
  publicationViewpointRef?,
  publicationScopeId,
  claimScope?,
  effectiveReferenceScheme?,
  modelUseStructureRef?,
  mvpkFaceRef,
  publicationFormRef,
  sourcePinSetRef,
  audience,
  admissiblePublicationUse,
  nonAdmissiblePublicationUse
}
```

`ArchitectureDescriptionPublication@Project` is subordinate to E.17 and MVPK machinery. It publishes one source episteme or episteme-lane view reference. `publicationViewpointRef?` names the publication-side viewpoint only when MVPK needs one; it is not an architecture viewpoint and not a TEVB viewpoint. `mvpkFaceRef` is a publication-lane face reference, not an alternative source episteme, source view, or source relation. Publication does not establish non-publication claims; apply `C.30:4.3` and the governing pattern when evidence, gate, work, assurance, decision, or release claims are current.

Model cards, system cards, and evaluation harness reports enter C.30 through the same publication boundary or source-relation boundary. They may describe a model, deployed AI system, architecture claim, evaluation harness, or policy, but the architecture move still needs the actual/candidate structure distinction, an obtaining `ArchitectureRelation` only when its predicate is satisfied, a bounded `ArchitectureClaim` when claim content is needed, and any proof, release, or gate claim assigned to its governing pattern.

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
  deploymentInterpretationOrUseMismatch?,
  evidenceOrAssuranceGoverningPatternRef?,
  nonAdmissibleUse:
    notArchitectureAdequacy | notSafetyProof |
    notReleaseAuthorityByPublicationAlone
}
```

If the card or harness is used beyond transparency, recover the architecture structure kind being used first and then apply `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `C.16`, `C.28`, or `C.11` for the non-architecture claim kind.

#### C.30:4.4 - Architecture name formation

The word `architecture` is shorthand only after the described holon, selected structures, structure kind, architecture concern and admissible-use frame, and source, description, view, or publication role are recoverable. Without those qualifiers, it is a recovery trigger, not a stable FPF term.

```text
ArchitectureNameFormationRule:

If a text says "<X> architecture", then the FPF-governed use is conforming only with:
  describedHolonRef,
  actual subject relation occurrences or an explicit candidate/expected stop,
  architectureRelationRefs only when those exact relations obtain,
  claimScope? when claim coverage changes use,
  effectiveReferenceScheme for any claim episteme,
  modelUseStructureRef? only when that structure changes interpretation or selection,
  structureKindRef = <X>StructureKind or a declared local classifier,
  actual selectedStructureRefs or separately named candidateOrExpectedStructureRefs,
  architectureStructuralViewRefs only when a conforming view episteme is being used,
  admissibleUse,
  nonAdmissibleUse.
If <X> is not a declared structure kind, the phrase is plain recognition wording only.
```

| Phrase | Required recovery |
| --- | --- |
| functional architecture | `structureKindRef = FunctionalStructure`; functions, effects, capabilities, and functional dependencies named as structure content; transformation-flow structures, paths, and flow valuations are assigned to `TransformationFlowStructure` or `C.30.TFS-REL`. |
| modular architecture | `structureKindRef = ModuleInterfaceStructure`; module claim content, selected dependency structure, interface specifications, substitutability rule, and change policy. Cite a direct module relation only after its direct owner admits it and its predicate obtains; current A.6.M `moduleIn(...)` syntax is claim content. |
| logical architecture | `structureKindRef = DeclaredLogicalStructure`; local definition says whether `logical` means information relation, functional relation, runtime relation, responsibility relation, allocation relation, or another relation class. |
| physical architecture | `structureKindRef` in `{MaterialSpatialStructure, PlacementDeploymentStructure}` or a locally declared physical structure kind. |
| control architecture | `structureKindRef = ControlStructure`; an LCA record may describe the control structure, but proof claims are assigned to dynamics, temporal, causal, evidence, safety, or assurance patterns as triggered. |
| information architecture | `structureKindRef = InformationDataStructure`; state bearer and residence, schema refs, semantic refs, persistence locus, provenance relation, custody relation, and source-return conditions. |
| security architecture | `structureKindRef = SecurityTrustBoundaryStructure`; recover protected asset or effect, trust boundary, adversarial path, authority or privilege relation, secure-default or hardening boundary, and evidence, assurance, or gate governing patterns when those claim kinds are being made. |

#### C.30:4.5 - Architecture characteristic assignment

C.30 recovers the exact bearer before any `quality`, `fitness`, `measure`, `metric`, `score`, `modularity`, or `ility` wording carries an architecture-adequacy claim. Those words are triggers, not stable architecture adequacy by themselves.

```text
ArchitectureCharacteristicAssignment:

A. SystemQualityAffectedByArchitecture
   Bearer: exact described U.Holon, named product holon, or named system holon
   Governing pattern: C.25 Q-Bundle or C.16
   Examples: maintainability, evolvability, resilience, availability, safety, observability

B. ArchitectureStructuralCharacteristic
   Bearer: one exact selected U.Structure, obtaining ArchitectureRelation,
           actual subject relation or constraint, or separately admitted
           module/interface relation
   Governing pattern: C.16, A.17-A.19, C.25, or the direct
                      characteristic-space/Q-bundle owner
   Examples: coupling, cohesion, interface alphabet, substitutability,
             hidden coupling, reusable-structure share

C. ArchitectureDescriptionOrViewAdequacy
   Bearer: one exact architecture-description episteme, one exact view episteme,
           one exact correspondence model, or one exact publication-use object
   Governing pattern: C.30.AD, C.30.ASV, E.17.0, E.17, C.16.Q, or C.16
   Examples: viewpoint coverage, correspondence adequacy,
             source-return adequacy, description modularity
```

An `ArchitectureClaim` may state a characteristic claim, but the claim episteme is not automatically the characteristic bearer when its content names the holon, direct architecture relation, or selected structure. Select the exact bearer under the characteristic's direct owner. Likewise, a diagram or publication cannot inherit the subject's quality by describing it.

C.30 keeps only a thin bridge from structural characteristics to Q-Bundle relevance. If the claim says architecture causes an outcome improvement, assign causal use to `C.28`. If a structural characteristic is used as a mechanism, constraint, predictor, proxy, evidence relation, or causal hypothesis for a Q-Bundle slot, start with `ArchitectureStructuralCharacteristicQBundleClaimLine` rather than a formula such as `low coupling = maintainability`.

`ArchitectureStructuralCharacteristicQBundleClaimLine` is claim content for first contact, not a `U.Relation` occurrence or reusable relation declaration:

```text
ArchitectureStructuralCharacteristicQBundleClaimLine ::= {
  architectureClaimRef?: ArchitectureClaimRef,
  entityOfConcernRef:
    architectureBearingHolonRef | architectureRelationRef |
    selectedStructureRef | directStructuralRelationRef |
    structuralCharacteristicRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue,
  claimScope?: U.ClaimScope, byValue,
  structuralCharacteristicCueOrRef,
  affectedQBundleSlotRef,
  relationClaimKind:
    structuralCharacteristicRelevantToQBundleSlot |
    structuralCharacteristicConstrainsQBundleSlot |
    structuralCharacteristicPredictsQBundleSlot |
    structuralCharacteristicProxiesQBundleSlot |
    structuralCharacteristicCausalHypothesisForQBundleSlot |
    structuralCharacteristicEvidenceRelationForQBundleSlot,
  relationGroundingKind:
    modelBased | empirical | causalModelBased | expertJudgement |
    sourceLineageOnly | SoTAActionLineage | reportOnly,
  directRelationDisposition:
    noDirectRelationClaimed | exactDirectOwnerAndOccurrenceRefs |
    directOwnerStillNeeded,
  directRelationOccurrenceRefs?: FinSet(U.RelationRef),
  evidenceOrCausalGoverningPatternRef?,
  nonAdmissibleUse
}
```

The line supports an inspectable next question without claiming measurement, modularity score, evidence sufficiency, assurance, gate passage, or causal proof. `exactDirectOwnerAndOccurrenceRefs` is available only when the direct characteristic, evidence, or causal pattern supplies its participant meanings, obtaining predicate, applicability, and occurrence identity and the referenced occurrences actually obtain. If no direct owner exists for a needed reusable relation, use A.6.RCD; neither a local token nor this line admits one.

Minimal structural-characteristic claim-line examples:

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

`ArchitectureCharacteristicQBundleClaim` is the triggered full claim episteme. Use it only when publication, comparison, causal use, evidence reliance, assurance, gate, decision, or reusable cross-case reliance needs a durable bounded claim and the thin line cannot keep the content inspectable.

```text
ArchitectureCharacteristicQBundleClaim ::= {
  claimEpistemeRef: U.EpistemeRef,
  entityOfConcernRef:
    architectureBearingHolonRef | architectureRelationRef |
    selectedStructureRef | directStructuralRelationRef |
    structuralCharacteristicRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue,
  claimScope?: U.ClaimScope, byValue,
  architectureClaimRef?: ArchitectureClaimRef,
  architectureStructuralViewRef?,
  architectureDescriptionRef?,
  structuralCHRRefs,
  affectedQBundleRefs,
  assertedParticipantRefs: {
    structuralCharacteristicRef,
    qBundleSlotRef
  },
  relationClaimPolarity:
    positive | negative | unresolved | candidateOnly,
  relationClaimKind:
    structuralCharacteristicRelevantToQBundleSlot |
    structuralCharacteristicConstrainsQBundleSlot |
    structuralCharacteristicPredictsQBundleSlot |
    structuralCharacteristicProxiesQBundleSlot |
    structuralCharacteristicCausalHypothesisForQBundleSlot |
    structuralCharacteristicEvidenceRelationForQBundleSlot,
  relationGroundingKind:
    modelBased | empirical | expertJudgement |
    sourceLineageOnly | SoTAActionLineage | causalModelBased | reportOnly,
  directRelationDisposition,
  directRelationOccurrenceRefs?: FinSet(U.RelationRef),
  scopeOrScaleWindow?,
  viewpointRef?,
  qualifiers?,
  witnessExpectations?,
  admissibleSemanticChangeClasses?,
  bridgeOrLossBoundary?,
  admissibleUse,
  nonAdmissibleUse,
  evidenceOrCausalGoverningPatternRef?
}
```

The full claim preserves the older branch's inspectable proposal detail: assertion polarity, the exact structural-characteristic and Q-Bundle-slot referents, scope or scale window, viewpoint when it changes interpretation, qualifiers, witness expectations, admissible semantic change classes, and bridge or loss boundary. These are claim-content fields. They neither declare a reusable relation kind nor make an occurrence obtain; a direct relation still needs its own owner, participants, obtaining predicate, applicability, and occurrence identity.

Reusable product-quality vocabularies may supply candidate characteristic names, but they do not become architecture theory. The claim content may connect exact bearers and Q-Bundle slots; only the direct owner makes a relation obtain. Measurement, modularity scoring, reusable-structure accounting, bespoke-residue accounting, evidence, assurance, gate, causal, and scale-audit claims stay with their governing patterns.

#### C.30:4.6 - Relation to structural views

`C.30.ASV` governs structural-view adequacy for an exact architecture-description episteme about one selected structure; E.17.0 alone admits that same episteme as `U.View` through independently obtaining conformance to an exact viewpoint. C.30 governs direct `ArchitectureRelation` occurrences and bounded `ArchitectureClaim` content and, only when durable description use is being made, how its thin `ArchitectureDescription` bridge cites exact structural views. Hidden/lost structure, correspondence, source or reliance relations, and source-return boundaries stay explicit when they affect action. `C.30.AD` governs the full description mechanism.

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

Use the thinnest claim or boundary form that preserves the next architecture move. Use a fuller governing claim or relation record only when the content or independently admitted relation being used cannot be inspected, compared, refreshed, or bounded without it. Typical thin forms are `ArchitectureMathLensUseBoundary` before C.29 Mini or Full, `AffectedArchitectureStructureNote` before an architecture decision record, and `ArchitectureStructuralCharacteristicQBundleClaimLine` before full measurement, causal, evidence, or reusable direct-relation records.

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
| Bare architecture as free-floating selected claim | Recover the actual subject-relation occurrences and exact A.22 structure, then either identify the obtaining `ArchitectureRelation` or keep candidate, expected, negative, or unresolved content in `ArchitectureClaim`. Also recover the exact described holon, structure kind, concern and admissible-use frame, effective reference scheme and ClaimScope when applicable, and the source, description, view, representation, or publication role of inspected material. |
| Architecture description as architecture | Keep `ArchitectureDescription` as a C.2.1 episteme about one exact holon, obtaining `ArchitectureRelation`, or selected structure; keep specification use, representation, and publication separate. |
| Diagram, model, table, dashboard, or generated relation graph as architecture | Treat it as publication form, description, view, source relation, or source-finding aid only when that relation is explicit. |
| Module diagram as all architecture | Use `C.30.ASV` to recover structure kind; module structure and interface relation are only one structure family. |
| Transformation-flow structure or graph description as architecture | Use E.18 for selected transformation-flow structure, path, and crossing records; use E.18.2 and C.29 for mathematical graph descriptions; use C.30.TFS-REL for the architecture-to-transformation-flow relation. |
| LCA diagram or control diagram as proof | Use `C.30.LCA` for control-structure view; assign dynamics, temporal, causal, evidence, gate, safety, and assurance claims to their governing patterns. |
| Mathematical lens as architecture ontology | Use `C.29`; cite `MathLensUseOutputRef` only through an `ArchitectureMathLensUseBoundary` or C.29 lens record and state stop condition. |
| ADR as architecture decision | Use the project-side architecture decision pattern when a decision claim is being made; ADR is a publication form, not the decision. |
| Quality, score, or measurement term as architecture adequacy | Recover the bearer through ArchitectureCharacteristicAssignment; assign the claim being made to C.25, C.16, A.17-A.19, the characteristic-space or Q-bundle pattern governing the characteristic claim, or C.30 grounded architecture, selected-structure, or conditional description-use scope. |
| Architecture record as evidence, assurance, gate, work, or release | Assign evidence, assurance, gate, work, or release claims to A.10, G.6, B.3, A.20, A.21, A.15, or the release locus named by value when a release claim is being made. |
| Architecture as agent, worker, controller, gate, or proof | Recover the mechanism, control relation, role and enactor relation, gate, work, evidence, or assurance record that carries enforce, decide, optimize, adapt, prove, or guarantee wording. Neither an `ArchitectureRelation`, its selected structure, nor `ArchitectureClaim` is an acting entity by that wording. |

**Currentness and smallest reopen.** When a decisive input changes, reopen only the C.30 object and use conclusion that depend on it. A changed holon or obtaining subject relation reopens the affected selected structure and, if asserted, the direct `ArchitectureRelation` predicate; a changed selected structure or predicate result reopens that relation occurrence and any affirmative `ArchitectureClaim` reference; a changed claim scheme or `ClaimScope` reopens only that claim; and a changed description, view, or source edition, admissible-use boundary, or direct governor reopens its exact reference and dependent `ArchitectureQuestionCard@Project` disposition. Admissible results are to update the affected reference or claim mode, narrow use, re-run the direct predicate, or reopen the card when its next architecture move is no longer supported; unrelated structures, descriptions, and claims stay closed.

#### C.30:4.10 - Worked slices

**"We have the architecture in this diagram."** The diagram is a representation or publication form. It creates neither architecture nor `U.View`; recover an exact `ArchitectureDescription` episteme and, when view use is claimed, its independently obtaining E.17.0 conformance relation.

```text
ArchitectureQuestionCard@Project:
  describedHolonRef: payment system
  claimScope: checkout-platform architecture use
  effectiveReferenceScheme: checkout-platform architecture terms
  architectureConcernCue: descriptionViewLoss or flowBottleneck
  sourcePhrase?: "architecture in this diagram"; unclear dependency between payment orchestration and fraud scoring
  questionDisposition: architectureClaimReady
  architectureRelationDisposition: actualRelationStillToRecover
  inspectedMaterialRole: diagram as publication face carrying possible architecture structural-view material
  selectedStructureKindRefs: FunctionalStructure, ModuleInterfaceStructure, TransformationFlowStructure
  firstArchitectureMove: recover the diagram as a publication face and create a minimal architecture structural-view note
  governingPatternApplicationRefs: C.30.ASV
  non-admissible overread: treating the diagram as architecture itself, evidence, assurance, gate passage, or decision
```

**"Low coupling gives maintainability."** C.30 does not allow that formula to carry the claim by itself. The ordinary repair starts with the thin claim line:

```text
ArchitectureStructuralCharacteristicQBundleClaimLine:
  architectureClaimRef: ArchitectureClaimRef
  entityOfConcernRef: selected module-interface structure or its exact structural-characteristic referent
  effectiveReferenceScheme: module-interface and maintainability terms used by this claim
  structuralCharacteristicCueOrRef: coupling under module claim, admitted direct module relation, or interface relation as actually grounded
  affectedQBundleSlotRef: maintainability Q-Bundle slot
  relationClaimKind: structuralCharacteristicRelevantToQBundleSlot
  relationGroundingKind: sourceLineageOnly | SoTAActionLineage | modelBased, as actually grounded
  directRelationDisposition: noDirectRelationClaimed | exactDirectOwnerAndOccurrenceRefs | directOwnerStillNeeded
  evidenceOrCausalGoverningPatternRef?: one selected governing pattern reference: C.28, B.3, A.10, or G.6 when evidence sufficiency, causal-use, assurance, or safety-case claim is being made
  nonAdmissibleUse: causal proof, assurance, or direct relation by slogan
```
Use `ArchitectureCharacteristicQBundleClaim` only when publication, comparison, causal use, evidence reliance, assurance, gate, decision, or reusable cross-case claim reliance needs the fuller bounded claim. If repeated use needs an independently admitted direct characteristic, evidence, or causal relation, its direct owner must first supply the participants, obtaining predicate, applicability, and occurrence identity; the useful move is not to accept the slogan as architecture truth.

**"The backup-pump architecture is safe because the loop is redundant."** C.30 starts with the plant holon, operating claim scope, effective reference scheme when local terms need it, and selected structures: control loop, material-flow structure, placement structure, module-interface relation, and maintenance-work relation. The redundancy phrase may motivate an architecture move, but safety proof, causal proof, evidence sufficiency, gate passage, and work authorization go to their governing patterns. The C.30 output is the selected structure and next architecture move, not a safety case by slogan.

**"We replaced the neural-network block, so the architecture improved."** Treat `block` first as a source label and apply `C.30.STRAT` unless the changed value is already recovered. The phrase is admissible architecture recognition only after the changed structure kind, transformation-flow relation, module or interface claim kind, preserved and lost structure, changed characteristic, source relation, and decision or evidence governing patterns are named. A block label, benchmark result, ablation, pruning mask, or distillation result is not an architecture decision, evidence sufficiency, gate passage, assurance, or architecture adequacy by itself.

