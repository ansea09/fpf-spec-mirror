---
chunk_kind: "child"
pattern_id: "C.16.Q"
pattern_title: "Quality-Term Precision Restoration"
section_id: "C.16.Q:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.Q/C.16.Q__007_archetypal-grounding.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "C.16.Q — Quality-Term Precision Restoration"
  - "C.16.Q:5 — Archetypal Grounding"
line_start: 47982
line_end: 48085
dependencies:
  - "A.10"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.17"
  - "A.18"
  - "A.19"
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
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "E.17.2"
  - "E.21"
  - "E.8"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
---

### C.16.Q:5 - Archetypal Grounding

#### C.16.Q:5.1 - Tell

If a draft says *quality*, the draft has not yet named the evaluative family.
A conforming rewrite publishes either one explicit endpoint-pattern-governed evaluative form or one explicit `qualityTermAscription(...)` transitional record with one `QualitySense`, one bearer tuple, one evaluation frame, one evaluator and viewpoint, one admissible normal form, explicit scope, time, and bridge qualifiers when they matter, and declared endpoint-governing pattern or explicit endpoint source relation.

#### C.16.Q:5.2 - Show (System lane)

**Draft:** “The model quality improved.”

**Repair A — latent representation line**
`qualityTermAscription(
  bearer = Model_v5,
  qualitySense = QS.LatentFit,
  evaluationFrame = ProbePack_PP2,
  evaluator = RepLearningReviewBoard,
  normalForm = SignalPack,
  Γ_time = Window_W5,
  witnesses = {ProbeSeparationRun_22, AliasRiskCard_9}
)`

**Repair B — closed-loop control line**
`qualityTermAscription(
  bearer = PolicyModelPair_PM5,
  qualitySense = QS.ControlAdequacy,
  evaluationFrame = Horizon_H × EnvClass_E,
  evaluator = ControlReviewBoard,
  viewpoint = ControlView_VP,
  normalForm = Bundle,
  scope = U.WorkScope(ControlDeploymentScope_7),
  Γ_time = RunWindow_RW,
  witnesses = {ClosedLoopTraceSet_41}
)`

#### C.16.Q:5.3 - Show (Episteme lane)

**Draft:** “Quality matters before definition.”

**Repair A — preconceptual or phenomenological line**
`qualityTermAscription(
  bearer = ProblemFramingEpisode_PF3,
  qualitySense = QS.PreconceptualFit,
  evaluationFrame = ExemplarPack_EP3,
  evaluator = ReviewerGroup_A,
  normalForm = SignalPack,
  representationSubstrate = embodied-kinesthetic,
  witnesses = {EpisodeNotes_3}
)`

**Repair B — explanatory line**
`qualityTermAscription(
  bearer = Explanation_N5,
  qualitySense = QS.ExplanatoryMerit,
  evaluationFrame = CriticismBundle_CB4,
  evaluator = TheoryReviewPanel,
  referencePlane = episteme,
  normalForm = Bundle,
  witnesses = {CritiqueSheet_14, CounterexampleSet_2}
)`

#### C.16.Q:5.3a - Show (Architecture description lane)

**Draft:** “The architecture quality improved.”

**Repair A — quality of the system-side bearer**
`qualityTermAscription(
  bearer = PaymentPlatform_v4,
  qualitySense = QS.EngineeringQualityFamily,
  evaluationFrame = Q_Bundle_AvailabilitySecurityEvolvability_3,
  evaluator = ArchitectureReviewBoard,
  viewpoint = TEVB_ArchitectureViewpointSet,
  referencePlane = world,
  normalForm = Bundle,
  witnesses = {AvailabilityReport_8, CouplingCheck_3, EvolvabilityNote_2}
)`

**Repair B — quality of the architecture description**
`qualityTermAscription(
  bearer = ArchitectureDescription_AD12,
  qualitySense = QS.ArchitecturalDescriptionFitness,
  evaluationFrame = ViewpointBundle_TEVB × DecisionQuestionSet_DQ7,
  evaluator = ArchitectureReviewBoard,
  viewpoint = TEVB_ArchitectureViewpointSet,
  referencePlane = episteme,
  normalForm = Bundle,
  witnesses = {CoverageMatrix_4, CorrespondenceCheck_7, ViewConsistencyNote_2}
)`

#### C.16.Q:5.4 - Show (QD or selector lane)

**Draft:** “Quality in our QD loop.”

**Repair**
`qualityTermAscription(
  bearer = Candidate_7,
  qualitySense = QS.UseValue,
  evaluationFrame = CG_Frame_9,
  evaluator = SelectorPolicy_P4,
  normalForm = Objective,
  Γ_time = SelectionWindow_SW,
  witnesses = {ObjectiveCard_9, AcceptanceSpec_4}
)`

