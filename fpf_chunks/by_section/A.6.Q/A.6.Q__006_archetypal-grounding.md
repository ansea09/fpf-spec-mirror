---
chunk_kind: "child"
pattern_id: "A.6.Q"
pattern_title: "U.QualityTermPrecisionRestoration — Quality Term Precision Restoration (Q-TERM)"
section_id: "A.6.Q:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.Q/A.6.Q__006_archetypal-grounding.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.6.Q — U.QualityTermPrecisionRestoration — Quality Term Precision Restoration (Q-TERM)"
  - "A.6.Q:5 — Archetypal Grounding"
line_start: 13233
line_end: 13335
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.17"
  - "A.18"
  - "A.2.6"
  - "A.6.A"
  - "A.6.B"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "C.25"
  - "E.17.0"
  - "E.17.2"
  - "F.9"
  - "F.9.1"
keywords:
  - "bridge reading"
  - "endpoint classification"
  - "evaluative ascription"
  - "language-state seam"
  - "quality senses"
  - "quality-term precision restoration"
---

### A.6.Q:5 - Archetypal Grounding

#### A.6.Q:5.1 - Tell

If a draft says *quality*, the author has not yet named the evaluative family.
A conforming rewrite publishes either one explicit endpoint-pattern-governed evaluative form or one explicit `evaluativeAscription(...)` transitional record with one `QualitySense`, one bearer tuple, one evaluation frame, one evaluator/viewpoint, one admissible normal form, explicit scope/time/bridge qualifiers when they matter, and declared target endpoint governing pattern or publication with named authority-reference relation.
#### A.6.Q:5.2 - Show (System lane)

**Draft:** “The model quality improved.”

**Repair A — latent representation line**
`evaluativeAscription(
  bearer = Model_v5,
  qualitySense = QS.LatentFit,
  evaluationFrame = ProbePack_PP2,
  evaluator = RepLearningReviewBoard,
  normalForm = SignalPack,
  Γ_time = Window_W5,
  witnesses = {ProbeSeparationRun_22, AliasRiskCard_9}
)`

**Repair B — closed-loop control line**
`evaluativeAscription(
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

#### A.6.Q:5.3 - Show (Episteme lane)

**Draft:** “Quality matters before definition.”

**Repair A — preconceptual / phenomenological line**
`evaluativeAscription(
  bearer = ProblemFramingEpisode_PF3,
  qualitySense = QS.PreconceptualFit,
  evaluationFrame = ExemplarPack_EP3,
  evaluator = ReviewerGroup_A,
  normalForm = SignalPack,
  representationSubstrate = embodied-kinesthetic,
  witnesses = {EpisodeNotes_3}
)`

**Repair B — explanatory line**
`evaluativeAscription(
  bearer = Explanation_N5,
  qualitySense = QS.ExplanatoryMerit,
  evaluationFrame = CriticismBundle_CB4,
  evaluator = TheoryReviewPanel,
  referencePlane = epistemic,
  normalForm = Bundle,
  witnesses = {CritiqueSheet_14, CounterexampleSet_2}
)`

#### A.6.Q:5.3a - Show (Architecture description lane)

**Draft:** “The architecture quality improved.”

**Repair A — quality of the described system**
`evaluativeAscription(
  bearer = PaymentPlatform_v4,
  qualitySense = QS.EngineeringQualityFamily,
  evaluationFrame = Q_Bundle_AvailabilitySecurityEvolvability_3,
  evaluator = ArchitectureReviewBoard,
  viewpoint = TEVB_ArchitectureViewpointSet,
  referencePlane = world/external,
  normalForm = Bundle,
  witnesses = {AvailabilityReport_8, CouplingCheck_3, EvolvabilityNote_2}
)`

**Repair B — quality of the architecture description**
`evaluativeAscription(
  bearer = ArchitectureDescription_AD12,
  qualitySense = QS.ArchitecturalDescriptionFitness,
  evaluationFrame = ViewpointBundle_TEVB × DecisionQuestionSet_DQ7,
  evaluator = ArchitectureReviewBoard,
  viewpoint = TEVB_ArchitectureViewpointSet,
  referencePlane = epistemic,
  normalForm = Bundle,
  witnesses = {CoverageMatrix_4, CorrespondenceCheck_7, ViewConsistencyNote_2}
)`

#### A.6.Q:5.4 - Show (QD / selector lane)

**Draft:** “Quality in our QD loop.”

**Repair**
`evaluativeAscription(
  bearer = Candidate_7,
  qualitySense = QS.UseValue,
  evaluationFrame = CG_Frame_9,
  evaluator = SelectorPolicy_P4,
  normalForm = Objective,
  Γ_time = SelectionWindow_SW,
  witnesses = {ObjectiveCard_9, AcceptanceSpec_4}
)`

