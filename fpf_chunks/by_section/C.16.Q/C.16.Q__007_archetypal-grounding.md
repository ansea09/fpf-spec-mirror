---
chunk_kind: "child"
pattern_id: "C.16.Q"
pattern_title: "Quality-Term Precision Restoration"
section_id: "C.16.Q:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.Q/C.16.Q__007_archetypal-grounding.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "C.16.Q — Quality-Term Precision Restoration"
  - "C.16.Q:5 — Archetypal Grounding"
line_start: 49088
line_end: 49251
dependencies:
  - "A.10"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "A.6.A"
  - "A.6.B"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16"
  - "C.16.P"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "C.25"
  - "C.30.AD"
  - "C.30.ASV"
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "E.17.2"
  - "E.21"
  - "E.8"
  - "F.18"
  - "F.9"
  - "F.9.1"
  - "U.ClaimScope"
  - "U.ContextSlice"
  - "U.ViewpointRef"
keywords:
---

### C.16.Q:5 - Archetypal Grounding

#### C.16.Q:5.1 - Tell

If a draft uses *quality* for an FPF-governed claim without a recoverable sense, make that sense explicit.
A conforming rewrite publishes either the evaluative form for one known endpoint or one explicit `qualityTermAscription(...)` transitional record with bearer, one `QualitySense`, effective ReferenceScheme, separate probe/model and comparison frames, evaluator and `U.ViewpointRef`, ClaimScope, admissible normal form, `endpointPatternLocator` or endpoint source relation, and explicit boundaries among result claim, witnesses, evidence use, empirical grounding, Bridge, bounded-use claim, optional Card, and optional stance note.

#### C.16.Q:5.2 - Show (Latent fit and control adequacy)

The identifiers below denote distinct objects. Each `comparisonFrameRef` resolves its exact A.19.CPM configuration; each non-`none` `viewpointRef` resolves one E.17.0 viewpoint episteme. A named result claim is not assessment work, witness refs do not establish an A.10 evidence-provenance path, and neither witnesses nor a result label establish the grounding relation cited beside them. In the model and architecture improvement examples, the cited result claim asserts the improvement under its named comparison frame; the ascription record refers to that claim.

**Draft:** “The model quality improved.”

**Repair A — latent representation line**
`qualityTermAscription(
  bearerTuple = {Model_v5},
  qualitySense = QS.LatentFit,
  effectiveReferenceScheme = RepLearningScheme_5,
  probeOrModelFrameRef = ProbePack_PP2,
  comparisonFrameRef = LatentFitComparison_CF2,
  evaluatorRef = RepLearningReviewBoard,
  viewpointRef = none,
  normalForm = SignalPack,
  claimScope = U.ClaimScope({RepresentationLearningSlice_RL5}),
  Γ_time = Window_W5,
  qualityResultClaimRef = LatentFitResultClaim_22,
  witnessRefs = {ProbeSeparationRun_22, AliasRiskCard_9},
  evidenceProvenancePathRefs = {LatentFitEvidencePath_22},
  empiricalGroundingRelationRef = EGR_LatentFitResult_22,
  endpointPatternLocator = C.16
)`

Here `EGR_LatentFitResult_22` denotes a separately established relation between the exact result episteme and exact grounding holon under the governed probe or measurement relations. The run and card alone would not establish it.

**Repair B — closed-loop control line**
`qualityTermAscription(
  bearerTuple = {PolicyModelPair_PM5},
  qualitySense = QS.ControlAdequacy,
  effectiveReferenceScheme = ClosedLoopControlScheme_5,
  probeOrModelFrameRef = Horizon_H × EnvClass_E,
  comparisonFrameRef = ControlBaselineComparison_CF5,
  evaluatorRef = ControlReviewBoard,
  viewpointRef = ControlViewpointRef_7,
  normalForm = Bundle,
  claimScope = U.ClaimScope({ControlDeploymentSlice_7}),
  Γ_time = RunWindow_RW,
  qualityResultClaimRef = ControlAdequacyResultClaim_41,
  witnessRefs = {ClosedLoopTraceSet_41},
  evidenceProvenancePathRefs = {ControlEvidencePath_41},
  empiricalGroundingRelationRef = EGR_ControlAdequacyResult_41,
  endpointPatternLocator = C.25
)`

#### C.16.Q:5.3 - Show (Preconceptual fit and explanatory merit)

**Draft:** “Quality matters before definition.”

**Repair A — preconceptual or phenomenological line**
`qualityTermAscription(
  bearerTuple = {ProblemFramingEpisode_PF3},
  qualitySense = QS.PreconceptualFit,
  effectiveReferenceScheme = FeltFitArticulationScheme_3,
  probeOrModelFrameRef = ExemplarPack_EP3,
  comparisonFrameRef = ExemplarContrastFrame_ECF3,
  evaluatorRef = ReviewerGroup_A,
  viewpointRef = none,
  normalForm = SignalPack,
  claimScope = U.ClaimScope({ProblemFramingSlice_PF3}),
  representationSubstrate = embodied-kinesthetic,
  qualityResultClaimRef = PreconceptualFitClaim_PF3,
  witnessRefs = {EpisodeNotes_3},
  evidenceProvenancePathRefs = none,
  empiricalGroundingRelationRef = none,
  endpointPatternLocator = A.16.1
)`

The explicit `none` values matter: episode notes are witnesses to articulation, not automatic provenance or empirical grounding.

**Repair B — explanatory line**
`qualityTermAscription(
  bearerTuple = {Explanation_N5},
  qualitySense = QS.ExplanatoryMerit,
  effectiveReferenceScheme = ExplanationCriticismScheme_5,
  probeOrModelFrameRef = CriticismBundle_CB4,
  comparisonFrameRef = RivalExplanationComparison_CF4,
  evaluatorRef = TheoryReviewPanel,
  viewpointRef = none,
  referencePlane = episteme,
  normalForm = Bundle,
  claimScope = U.ClaimScope({ExplanationReviewSlice_N5}),
  qualityResultClaimRef = ExplanatoryMeritResultClaim_14,
  witnessRefs = {CritiqueSheet_14, CounterexampleSet_2},
  evidenceProvenancePathRefs = {ExplanationEvidencePath_14},
  empiricalGroundingRelationRef = none,
  endpointPatternLocator = C.25
)`

#### C.16.Q:5.3a - Show (System quality and architecture-description fitness)

**Draft:** “The architecture quality improved.”

**Repair A — quality of the system-side bearer**
`qualityTermAscription(
  bearerTuple = {PaymentPlatform_v4},
  qualitySense = QS.EngineeringQualityFamily,
  effectiveReferenceScheme = PlatformEngineeringQualityScheme_4,
  probeOrModelFrameRef = Q_Bundle_AvailabilitySecurityEvolvability_3,
  comparisonFrameRef = PlatformVersionComparison_CF4,
  evaluatorRef = ArchitectureReviewBoard,
  viewpointRef = ProjectSystemEngineeringQualityViewpointRef_4,
  referencePlane = world,
  normalForm = Bundle,
  claimScope = U.ClaimScope({PaymentPlatformEngineeringSlice_4}),
  qualityResultClaimRef = PlatformQualityResultClaim_8,
  witnessRefs = {AvailabilityReport_8, CouplingCheck_3, EvolvabilityNote_2},
  evidenceProvenancePathRefs = {PlatformQualityEvidencePath_8},
  empiricalGroundingRelationRef = EGR_PlatformQualityResult_8,
  endpointPatternLocator = C.25
)`

**Repair B — quality of the architecture description**
`qualityTermAscription(
  bearerTuple = {ArchitectureDescription_AD12},
  qualitySense = QS.ArchitecturalDescriptionFitness,
  effectiveReferenceScheme = ArchitectureDescriptionFitnessScheme_12,
  probeOrModelFrameRef = ArchitectureDescriptionProbeFrame_AD12,
  comparisonFrameRef = DescriptionEditionComparison_CF12,
  evaluatorRef = ArchitectureReviewBoard,
  viewpointRef = ProjectArchitectureDescriptionFitnessViewpointRef_12,
  referencePlane = episteme,
  normalForm = Bundle,
  claimScope = U.ClaimScope({ArchitectureDescriptionReviewSlice_AD12}),
  qualityResultClaimRef = DescriptionFitnessResultClaim_7,
  witnessRefs = {CoverageMatrix_4, CorrespondenceCheck_7, ViewConsistencyNote_2},
  evidenceProvenancePathRefs = {DescriptionFitnessEvidencePath_7},
  empiricalGroundingRelationRef = none,
  endpointPatternLocator = C.25
)`

`ArchitectureDescriptionProbeFrame_AD12` is one project-local probe frame: it may cite `DecisionQuestionSet_DQ7`, an architecture-description result under `C.30.AD`, structural-view adequacy under `C.30.ASV`, and the retained `U.ViewpointRef` members resolved from a constituted E.17.1 catalogue. It is neither a viewpoint-family value nor a substitute for the selected viewpoint. `C.25` supplies the Bundle endpoint; the architecture-description and viewpoint patterns supply their own checks. The shared evaluator does not collapse the two repairs: their bearers, schemes, probe/model frames, scopes, viewpoint references, result claims, and evidence paths differ.

#### C.16.Q:5.4 - Show (QD or selector lane)

**Draft:** “Quality in our QD loop.”

**Repair**
`qualityTermAscription(
  bearerTuple = {Candidate_7},
  qualitySense = QS.UseValue,
  effectiveReferenceScheme = QDUseValueScheme_9,
  probeOrModelFrameRef = CG_Frame_9,
  comparisonFrameRef = ArchiveComparatorFrame_9,
  evaluatorRef = SelectorPolicy_P4,
  viewpointRef = none,
  normalForm = Objective,
  claimScope = U.ClaimScope({QDSelectionSlice_9}),
  Γ_time = SelectionWindow_SW,
  qualityResultClaimRef = UseValueResultClaim_9,
  witnessRefs = {ObjectiveCard_9, AcceptanceSpec_4},
  evidenceProvenancePathRefs = {QDSelectionEvidencePath_9},
  empiricalGroundingRelationRef = none,
  endpointPatternLocator = C.17
)`

