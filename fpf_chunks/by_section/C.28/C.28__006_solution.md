---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
section_id: "C.28:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__006_solution.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Identification, and Realizability"
  - "C.28:4 — Solution"
line_start: 58492
line_end: 59017
dependencies:
  - "A.10"
  - "A.15"
  - "A.2.4"
  - "A.3.2"
  - "A.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.19"
  - "C.24"
  - "C.26"
  - "C.27"
  - "D.5"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "CausalUseSupportResult"
  - "Pearl Causal Hierarchy"
  - "Structural Causal Model"
  - "association"
  - "causal diagram"
  - "causal estimand"
  - "causal fairness"
  - "causal support components"
  - "causal-RL evaluation"
  - "causal-use question"
  - "causality ladder"
  - "counterfactual"
  - "counterfactual sampling realizability"
  - "identification"
  - "intervention"
  - "off-policy causal evaluation"
  - "target trial"
---

### C.28:4 - Solution

Use the smallest result that answers the current question:

1. triage the claim;
2. stabilize the question in a small card when it must be reused;
3. run the common threat screen;
4. add only the specialist result needed now; and
5. issue a small `CausalUseSupportResult` when another pattern must consume the conclusion.

#### C.28:4.0 - Public contract and support components

When a question or result must be referenced, recover its content and use the corresponding contract:

- `CausalUseQuestionRef` identifies the exact question content, normally a C.2.1 episteme.
- `CausalEstimandRef` identifies the mathematical target or the episteme that describes it under its direct pattern.
- `PotentialOutcomeContrastRef` identifies the exact contrast or its description.
- `CausalUseSupportResultRef` identifies one C.2.1 result episteme defined below.

Support is composable. A real result may use several components:

```text
CausalSupportComponentRefs:
  evidencePathRefs?
  empiricalDataRegimeRefs?
  identificationResultRef?
  estimateResultRef?
  counterfactualSamplingRealizabilityResultRef?
  simulationResultRef?
  targetTrialMappingResultRef?
  offPolicyCausalEvaluationResultRef?
  causalVariableRepresentationRecordRef?
  transportabilityResultRef?
```

These fields answer different questions. Do not compress them into one exclusive value. Each optional specialist ref identifies the exact result or record actually used. Keep a component's own assumptions, uncertainty or sensitivity, supported and unsupported uses, and reopen information with that component when its defining contract requires them; do not copy fields merely to complete a standard list. The common `CausalUseSupportResult` still states its own `supportedUse`, `unsupportedUse`, `limits`, optional evidence window, and `reopenCondition`. Naming a specialist subject in prose does not make its result available to a consumer.

| Component | Question it answers | Does not establish |
| --- | --- | --- |
| evidence path and data regime | What observations, assignments, or samples are available, and where did they come from? | identification or a valid estimate |
| identification result | Can the estimand be expressed or bounded from those data and assumptions? | a numerical estimate or direct sampling |
| estimate result | What value and uncertainty were obtained under an identification or design basis? | identification by the number alone |
| counterfactual-sampling realizability result | Can samples from the declared target distribution be obtained under the stated constraints, and how was that decided? | a WorkPlan, performed sampling, resulting data, or identification of every target |
| simulation result | What did the model produce under its assumptions and validation? | realized evidence or an intervention effect |
| target-trial mapping result | How does the declared trial protocol map to one observational data source, and which gaps, residual-confounding risks, and sensitivity checks remain? | identification, low risk of bias, or a valid estimate by reporting completeness alone |
| off-policy evaluation result | What does logged behaviour support about one evaluation policy under the stated history, confounding, overlap, endpoint, estimator, and uncertainty conditions? | authority to deploy or unqualified policy optimality |
| causal-variable representation record | Which learned, selected, or abstracted variables preserve the interventions, invariances, and queries needed for this use? | causal validity for every query, shift, or domain |
| transportability result | Which support transfers between exact endpoints, under which assumptions? | transfer by a shared label or population name |

`CausalEmpiricalDataRegime` is a local classification used only when it helps distinguish evidence:

```text
CausalEmpiricalDataRegime =
  observationalOrNaturalBehaviorData |
  randomizedInterventionData |
  governedInterventionData |
  realizedCounterfactualSamplingData
```

`realizedCounterfactualSamplingData` is used only when an A.10 evidence path cites dated sampling Work and the resulting sample or data. A realizability result or WorkPlan alone establishes no empirical regime. Model output is recorded separately through `simulationResultRef`, not as an empirical regime.

#### C.28:4.1 - Causality-Ladder Rung

```text
CausalityLadderRung =
  observationalAssociationRung |
  interventionalActionRung |
  counterfactualComparisonRung
```

- observational: passive observation, natural behaviour, or association;
- interventional: action setting, experiment, policy change, or action effect;
- counterfactual: counter-to-fact, potential-outcome, or unit-history-conditioned comparison.

Lower-rung data may contribute to a higher-rung result only through a replayable identification, bound, or other specialist result. The rung label itself supplies no support.

#### C.28:4.1a - Causal-Use Claim Kind

```text
CausalUseClaimKind =
  causalEffectClaim |
  counterfactualComparisonClaim |
  causalFairnessClaim |
  causalPolicyClaim |
  causalBenchmarkParityClaim |
  causalEvidenceSupportClaim |
  causalAssuranceSupportClaim
```

Choose the kind by the claim being supported, not by the tool or source. Simulation for a causal claim uses the appropriate claim kind plus `simulationResultRef`; it does not need a simulation-only claim kind.

#### C.28:4.2 - Question cards and support result

Use a local card when the question must survive beyond the current sentence:

```text
LocalCausalUseQuestionCard:
  causalUseQuestionRef: CausalUseQuestionRef
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind?
  comparatorOrCounterfactualRef?
  causalEstimandRef?
  supportedUse
  unsupportedUse
  nextCausalUseAction
```

Use a durable card only for a reusable or consequential claim:

```text
DurableCausalUseQuestionCard:
  causalUseQuestionRef: CausalUseQuestionRef
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind
  comparatorOrCounterfactualRef?
  causalEstimandRef: CausalEstimandRef
  potentialOutcomeContrastRef?: PotentialOutcomeContrastRef
  interventionOrAssignmentWindowRef?
  followUpWindowRef?
  outcomeMeasureRef?
  causalAssumptionRefs
  rivalCauseRefs?
  causalSupportComponentRefs
  commonThreatScreenRef?
  supportedUse
  unsupportedUse
  stopOrReopenCondition
```

When another pattern needs a stable conclusion, issue this small C.2.1 result episteme:

```text
CausalUseSupportResult:
  causalUseQuestionRef: CausalUseQuestionRef
  causalUseClaimKind: CausalUseClaimKind
  targetCausalityLadderRung: CausalityLadderRung
  causalEstimandRef?: CausalEstimandRef
  causalSupportComponentRefs: CausalSupportComponentRefs
  commonThreatScreenRef?
  verdict: supported | bounded | unsupported | undecided
  supportedUse
  unsupportedUse
  limits
  evidenceWindowRef?
  reopenCondition
```

Its identity and reference follow C.2.1. A receiving decision consumes it under :4.9.

#### C.28:4.3 - Common causal-validity screen

Run only the questions relevant to the current claim. A live threat either points to an existing specialist field/result or lowers the support result; it does not trigger a mandatory dossier.

```text
CommonCausalThreatScreen:
  causalUseQuestionRef
  interventionWellDefinedOrConsistency?: clear | liveThreat | notApplicable
  temporalOrdering?: clear | liveThreat | notApplicable
  exchangeabilityOrConfounding?: clear | liveThreat | notApplicable
  positivityOrOverlap?: clear | liveThreat | notApplicable
  interferenceOrSpillover?: clear | liveThreat | notApplicable
  selectionCensoringOrMissingness?: clear | liveThreat | notApplicable
  measurementErrorOrConstructShift?: clear | liveThreat | notApplicable
  transportToTarget?: clear | liveThreat | notApplicable
  routedThreatRefs?
  resultingSupportBoundary
```

**Ordinary effect case.** A randomized treatment study records `interventionWellDefinedOrConsistency=clear`, `temporalOrdering=clear`, `positivityOrOverlap=clear`, `interferenceOrSpillover=notApplicable`, `selectionCensoringOrMissingness=clear`, and `measurementErrorOrConstructShift=clear` for its declared target and window. The screen points to the trial and estimate results; it does not repeat them.

**Countercase.** An observational cohort has the right rung label and a plausible estimand, but records `exchangeabilityOrConfounding=liveThreat` and `positivityOrOverlap=liveThreat` because severity is unmeasured and one treatment region has no comparator. The claimed effect remains `unsupported` until a suitable design or new evidence closes those threats; a suitable bound can instead support a correspondingly bounded claim. “Observational data” was classified correctly; that label does not establish validity.

#### C.28:4.4 - Identification result


Identification answers whether the estimand can be expressed or bounded from the available data and assumptions. The bounds for nonidentified counterfactual queries in [Raghavan and Bareinboim, 2026, §5](https://arxiv.org/html/2602.23541v1) belong to this identification problem. The conclusion must be replayable:

```text
CausalIdentificationResult:
  causalUseQuestionRef: CausalUseQuestionRef
  causalEstimandRef: CausalEstimandRef
  availableDataRegimeRefs
  causalAssumptionRefs
  modelOrDiagramRefs?
  calculusOrDerivationMethodRef?
  status: identified | bounded | nonidentified | unclear
  identifyingExpressionOrDerivationRef?   # required when identified
  boundResultRef?                         # required when bounded
  obstructionOrFailureWitnessRef?         # required when nonidentified
  falsificationOrNegativeControlRef?
  sensitivityAnalysisRef?
  supportedUse
  unsupportedUse
```

An `identified` label without an identifying expression or derivation is incomplete. A `bounded` result cites the bound. A `nonidentified` result exposes the obstruction or failure witness. Identification is neither a numerical estimate nor direct physical sampling.

**Replayable identified case.** For `treatment_effect_in_population_P`, `AdjustmentSet_Z` is justified as blocking the relevant back-door paths. `backdoor_adjustment_derivation_7` states the identifying expression in ordinary terms: compare treated and untreated outcomes within each Z group, then average those differences using the target population's Z distribution. The result cites the data regime, assumptions, expression, and the confounding or overlap change that would reopen it.

**Replayable nonidentified case.** In a treatment cohort, unmeasured severity affects both treatment and outcome, and no valid adjustment set, instrument, proxy, or useful bound is available. `unmeasured_severity_obstruction_3` is the failure witness. The result is `nonidentified`; reporting an adjusted number does not change that status.

**Replayable sensor case: observation and intervention.** Let `H` denote binary high load and `S` a binary alarm. Stipulate `P(H=1)=0.5`, `P(S=1|H=1)=0.9` and `P(S=1|H=0)=0.1`. Bayes' rule gives `P(H=1|S=1)=0.9` and `P(H=1|S=0)=0.1`. These are observational questions about the stated joint distribution.

For the query `P(H=1|do(S=0))`, additionally specify a structural model: H is determined by an exogenous random input; S is a noisy measurement of H with separate independent noise; S has no influence on H. Replacing the S mechanism by the constant zero preserves the H mechanism and its input distribution, giving `P(H=1|do(S=0))=0.5`. This derivation is an identified model-based result under those assumptions. The [corrected Pearl, Glymour and Jewell primer, p.55](https://bayes.cs.ucla.edu/PRIMER/mueller-edits-questions-pearl-etal-2016-primer-errata-pages-august2019.pdf) explains the mechanism-replacement operation.

If the alarm controls cooling, specify the intervention time and the subsequent load mechanism before answering a later-load question. [F.0.2:5.5][fpf-f0-2-5-5-ref] uses this distinction when comparing source theories for an explanation.

#### C.28:4.5 - Counterfactual sampling realizability

Use this result to answer whether a declared target distribution can be sampled under current constraints. [Raghavan and Bareinboim, 2025, Definition 3.4 and Theorem 3.5](https://proceedings.iclr.cc/paper_files/paper/2025/file/e59c4efcaed615db8911fecb84c1d51b-Paper-Conference.pdf) give a construction-or-failure decision for their graph and available-action setting. The result is prospective: it does not say that sampling was planned, performed, or yielded data.

```text
CounterfactualSamplingRealizabilityResult:
  causalUseQuestionRef: CausalUseQuestionRef
  targetCounterfactualDistributionRef
  targetCausalityLadderRung: counterfactualComparisonRung
  modelOrDiagramRefs?
  sameUnitConflictCheck
  ancestorRegimeConflictCheck
  physicalConstraintRefs
  ethicalConstraintRefs
  operationalConstraintRefs
  unitHistoryAvailabilityRef?
  decisionMethodRef
  decisionDerivationRef?
  positiveSamplingConstructionRef?  # required when realizable

  obstructionOrFailureWitnessRef?   # required when nonrealizable
  status: realizable | nonrealizable | unclear
  supportedUse
  unsupportedUse
```

A `realizable` result cites the sampling construction that the decision Method accepts for the exact target and constraints. A `nonrealizable` result exposes the obstruction or failure witness. `unclear` names what remains unresolved. Bounds on a counterfactual probability belong to the identification result at :4.4; they constrain what can be inferred about that probability, while this result asks how draws from the target distribution can be obtained. “Realized counterfactual sampling” never means observing incompatible outcomes for one unit in one realized world.

If the team plans to draw samples, use a separate A.15.2 WorkPlan. If sampling occurs, recover every precise performer's A.13 core and independently admit the dated Work under A.15.1. Add F.6 only when the sampling claim also needs precise assignment-bound attribution. If the samples are used as evidence, cite the resulting data through an A.10 evidence path. Actual sampling support requires both the dated Work and resulting data or evidence ref; neither `realizable` nor a WorkPlan can stand in for them. Identification from those data, when claimed, is another `CausalIdentificationResult`.

#### C.28:4.6 - Applied profiles

**Target trial.** The [TARGET Statement, 2025](https://www.bmj.com/content/390/bmj-2025-087179) supplies reporting guidance for an observational study explicitly emulating a target trial. Use it for the protocol-to-data account below, with causal validity checked separately.

```text
TargetTrialProtocolRecord:
  causalUseQuestionRef: CausalUseQuestionRef
  targetPopulationRef
  eligibilityCriteriaRef
  treatmentStrategyRefs
  assignmentProcedureRef?
  timeZeroRef
  followUpWindowRef
  outcomeMeasureRef
  potentialOutcomeContrastRef?: PotentialOutcomeContrastRef
  causalEstimandRef: CausalEstimandRef
  analysisPlanRef
```

An observational emulation keeps the protocol and its mapping to available data as separate results:

```text
TargetTrialMappingResult:
  causalUseQuestionRef: CausalUseQuestionRef
  targetTrialProtocolRef
  observationalDataSourceRef
  eligibilityCriteriaMappingRef
  treatmentStrategyMappingRefs
  assignmentAndTimeZeroMappingRef
  followUpWindowMappingRef
  outcomeMeasureMappingRef
  identifyingAssumptionRefs
  protocolToDataGapAccountRef
  residualConfoundingAssessmentRef
  sensitivityMappingRefs
  supportedUse
  unsupportedUse
  reopenCondition
```

Every mapping field identifies the actual mapping. `protocolToDataGapAccountRef` points to one account that lists the observed gaps or explicitly states that none was found within the declared source and window. The residual-confounding and sensitivity fields remain present even when their bounded result is favourable. Reporting completeness is not a risk-of-bias, identification, or estimate verdict.

**Filled target-trial mapping.** `HypertensionEmulationMap-2025` maps `HypertensionTargetTrial-1` to `ClinicRecords-2022-2024`: age and diagnosis fields implement eligibility; prescription records distinguish the two treatment strategies; the prescription date supplies assignment and time zero; encounter records map the twelve-month follow-up; and the recorded systolic-pressure field maps the outcome. `GapRecord-17` states that adherence after prescription is not observed, `ResidualConfoundingAssessment-17` retains unmeasured severity as a live threat, and `SensitivityMap-17` points to the negative-control and quantitative-bias analyses. The result supports construction and review of this emulation. It does not by itself establish identification, low bias, or a transportable effect; new severity or adherence data reopens it.

**Estimation.**

```text
CausalEstimateResult:
  causalEstimandRef: CausalEstimandRef
  identificationResultRef?: CausalIdentificationResultRef
  designBasedIdentificationResultRef?
  dataRef
  estimatorMethodRef
  diagnosticRefs?
  uncertaintyResultRef
  sensitivityAnalysisRef?
  estimationConsistencyResultRef?  # when consistency is a live support condition
  methodSpecificDetailRefs?        # only for the selected estimator family
  supportedUse
  unsupportedUse
```

At least one identification or explicit design-based basis is required before the estimate supports a causal use. Orthogonal scores, nuisance models, and cross-fitting belong in `methodSpecificDetailRefs` only when a [DML Method](https://academic.oup.com/ectj/article/21/1/C1/5056401) is selected. `estimationConsistencyResultRef` points to the consistency result defined by the selected estimation Method or its direct evaluation pattern.

**Counterfactual fairness.** Before D.5 uses a counterfactual-fairness support result, its C.28 components cite the identification result and the extra assumptions needed to connect the available data to that counterfactual question. When the fairness conclusion depends on an estimate, they also cite the estimate and its `estimationConsistencyResultRef`. Without those conditions, return `bounded` or `unsupported`; more data, even an unlimited amount of the same data, does not repair missing counterfactual identification or an inconsistent estimator. Associative or interventional fairness claims use their own rung and do not inherit this stronger branch by label.

**Non-DML estimate.** A randomized trial cites `random_assignment_identification_4`, `trial_data_8`, `DifferenceInMeansMethod_2`, `standard_error_result_5`, and its attrition sensitivity check. It needs no orthogonal-score, nuisance-model, or cross-fitting fields. The estimate supports only the declared population, outcome, assignment, and follow-up window.

**Transport.** For the first-moment population-measure problem under covariate shift, use [Boughdiri, Berenfeld, Josse and Scornet, *A Unified Framework for the Transportability of Population-Level Causal Measures*, 2025, §§2–4](https://proceedings.neurips.cc/paper_files/paper/2025/hash/795679e4056817ee71d37680939e980f-Abstract-Conference.html) with its internal trial-validity, overlap and selected exchangeability conditions. Other endpoint changes need their own identifying result.

```text
CausalTransportabilityResult:
  causalUseQuestionRef: CausalUseQuestionRef
  sourcePopulationRef?
  targetPopulationRef?
  sourceDomainRef?
  targetDomainRef?
  sourceEnvironmentRef?
  targetEnvironmentRef?
  sourceDataGeneratingRegimeRef?
  targetDataGeneratingRegimeRef?
  selectionAssumptionRefs?
  domainShiftAssumptionRefs?
  sourceWindowRef?
  targetWindowRef?
  overlapEvidenceRef?
  transportComparatorOrFormulaRef
  semanticBridgeRef?          # only when interpretation differs
  supportedUse
  unsupportedUse
  unresolvedAssumptionRefs?
```

Identify every endpoint dimension that differs in the current claim. Population, domain, environment, data-generating regime, and semantic scheme answer different questions. A shared label proves nothing; a semantic Bridge is added only when its F.9 relation independently obtains.

**Off-policy evaluation.**

```text
OffPolicyCausalEvaluationResult:
  causalUseQuestionRef: CausalUseQuestionRef
  evaluationPolicyRef
  behaviorPolicyRef
  sequentialHorizonRef?
  unitHistoryConditioningRef?
  confoundingAssumptionRefs?
  overlapOrSupportCheckRef
  policyTransportabilityResultRef?
  estimatorRef?
  uncertaintyResultRef?
  supportedUse
  unsupportedUse
  reopenCondition
```

**Causal representation.** Use this record only when variables are learned, selected, or abstracted rather than supplied by the domain:

```text
CausalVariableRepresentationRecord:
  causalUseQuestionRef: CausalUseQuestionRef
  sourceRepresentationRef
  selectionOrAbstractionMethodRef
  representationAssumptionRefs
  interventionValidityResultRef
  invarianceResultRefs?
  abstractionFidelityResultRef?
  counterfactualQueryPreservationResultRef?
  uncertaintyResultRef?
  shiftLimitRefs?
  supportedUse
  unsupportedUse
  reopenCondition
```

The record states which interventions and queries the learned or abstracted variables preserve, not that they are causal variables for every query or domain.

**Filled representation case.** `WardStateRepresentation-4` derives three state variables from monitor traces through `WardStateAbstractionMethod-2`. Its intervention-validity result covers dosage interventions, its invariance result covers the two hospitals in the training and hold-out comparison, and its query-preservation result passes the declared one-step counterfactual query but fails the long-horizon query. The record therefore supports the one-step policy comparison only; a new hospital, sensor scheme, intervention family, or long-horizon claim reopens it.

#### C.28:4.7 - Graph and calculus names

Use specialist names only when the result depends on them. For a counterfactual graphical-model derivation, use the conditions and calculus in [Correa and Bareinboim, 2025](https://proceedings.mlr.press/v267/correa25a.html) and cite the actual derivation used:


```text
CausalGraphRepresentationKind =
  causalDirectedAcyclicGraphRepresentation |
  acyclicDirectedMixedGraphRepresentation |
  singleWorldInterventionGraphRepresentation |
  structuralCausalModelTwinNetworkRepresentation |
  ancestralMultiWorldNetworkRepresentation |
  counterfactualGraphicalModelRepresentation

GraphSeparationCriterionKind =
  dSeparationCriterion |
  mSeparationCriterion |
  singleWorldInterventionGraphSeparationCriterion |
  ancestralMultiWorldNetworkSeparationCriterion |
  counterfactualGraphSeparationCriterion

CausalInferenceCalculusKind =
  doCalculus |
  ctfCalculus |
  potentialOutcomeCalculus |
  gFormulaCalculus
```

These values classify the formal support form. Concrete refs point to the model, diagram, derivation, assumptions, or proof. A graph-class label is not a proof and does not replace the plain statement of what was identified or bounded.

#### C.28:4.8 - Causal evidence design and Work

Use `CausalUseEvidenceDesignRecord` when additional evidence could change the support boundary:

```text
CausalUseEvidenceDesignRecord:
  causalUseQuestionRef: CausalUseQuestionRef
  targetCausalityLadderRung
  causalEstimandRef?
  interventionOrProtocolRef?
  plannedDataRegimeRefs?
  identificationQuestionRef?
  estimationQuestionRef?
  samplingRealizabilityQuestionRef?
  transportQuestionRef?
  targetTrialMappingResultRef?
  offPolicyCausalEvaluationResultRef?
  causalVariableRepresentationRecordRef?
  causalEvidenceMethodDescriptionRefs?
  causalEvidenceWorkPlanRef?
  realizedCausalEvidenceWorkRefs?
  workAttributionResultRefs?
  evidencePathRefs?
  modelAssumptionRefs?
  simulationValidationRef?
  decisionThresholdAffected?: yes | no | unclear
  evidenceValueOrProbeWorthinessRef?
  costOrRiskRef?
  supportedUseIfSuccessful
  unsupportedUseWithoutFurtherEvidence
```

The three optional specialist refs are included only when an existing target-trial mapping, off-policy evaluation, or causal-variable representation result shows what additional evidence could change the support boundary. Before execution, cite a MethodDescription or WorkPlan only when used. After execution, cite every precise performer's A.13 core and the independent A.15.1 Work admission; cite F.6 only when precise assignment-bound attribution is also current. If performed counterfactual sampling is used as evidence, also cite the resulting sample or data through `evidencePathRefs`; Work without output data and data without its Work and provenance path each remain incomplete for that claim. Do not copy performer-kind, assignment, or occurrence mechanics into this record unless one of those facts changes causal validity, safety, authorization, or supported use.

Additional evidence is worth planning only when it can change a material causal statement or downstream decision enough to justify cost, risk, and delay, or when safety or release rules independently require it.

#### C.28:4.9 - Support is not authority

`CausalUseSupportResult.verdict` has four values:

- `supported`: the named causal statement or evidential reliance is supported under the stated limits;
- `bounded`: only the narrower statement or reliance is supported;
- `unsupported`: the claimed causal statement or reliance is not supported;
- `undecided`: the available work does not establish a causal conclusion.

When another pattern uses the result for a decision, it checks whether the named support and limits answer its question and applies its own remaining decision conditions. For `undecided`, it chooses whether to seek evidence, abstain or use an available non-causal result. “Report association only” limits the evidential claim; any decision to publish, choose or deploy remains with the receiving pattern.

#### C.28:4.10 - Causal action policy class

Use `CausalActionPolicyClass` only when the action-selection regime changes the causal question. Identify the decision variables, horizon and natural mechanism; say whether the question compares one specified rule or an admissible family. Keep that rule or family with the question. When both behavior and evaluation policies occur, identify which one the field summarizes.

The mechanism distinctions follow [Maiti and Bareinboim, *Sequential Causal Games*, Definitions 2.3, 2.5, 2.7–2.8](https://causalai.net/r145.pdf). Let `X°` be the natural action and `Z` the allowed pre-action information. Order actions causally; `Z` excludes descendants of the current or later action variables.

| Value | Operative distinction |
| --- | --- |
| `naturalBehaviorPolicy` | Leave the natural action mechanism in place. |
| `interventionalPolicy` | Replace it by a rule `X = g(Z)`, including a fixed action or declared randomized rule. The current natural proposal is not an additional input. |
| `counterfactualPolicy` | Permit a replacement `X = g(Z, X°)` after observing the natural proposal. This family includes the identity and natural-proposal-independent special cases. |
| `mixedPolicy` | Use a declared combination of natural and interventional choices, corresponding to the available-class union in Definition 2.8. State the component choices and their selection rule or distribution. |

For this interface, when a concrete rule is represented in the wider counterfactual family, record its simpler natural or interventional case when that reduction holds throughout the stated scope. Keep `mixedPolicy` when the specified combination matters. If selection itself requires the current natural proposal, expose that counterfactual dependence. For a family comparison, retain the declared available family and any restrictions. Thus the scalar is an informative summary of the supplied rule or family, not a disjoint ontology of policies.

**Authored three-rule replay.** For binary `X°`, compare:

| Rule | Outputs for `X° = 0, 1` | Concrete classification |
| --- | --- | --- |
| Follow the natural action | `0, 1` | `naturalBehaviorPolicy` |
| Replace it by zero | `0, 0` | `interventionalPolicy` |
| Replace it by `1 - X°` | `1, 0` | `counterfactualPolicy` |

The last evaluation needs the natural proposal and its relation to outcomes; a fixed-action evaluation does not answer it. A mixed example chooses with equal probability, using an independent coin, between following the natural mechanism and replacing its action by zero. Retain both component choices and their probabilities.

`unknown` records unresolved classification, not another member. Omit the field when it changes no support, comparison or receiving decision.

#### C.28:4.11 - Neighbor selection

| Current issue | Use | C.28 contribution |
| --- | --- | --- |
| measurement or metric | `C.16` | causal support only when the measure is used causally |
| temporal trend or rate | `C.27` | causal support only when time order is used as cause evidence |
| evidence path and provenance | `A.10` | support-result and component refs |
| assurance | `B.3` | one possible basis for a separate bounded assurance result |
| local choice | `C.11` | question, support result, and policy class when needed |
| live-pool policy | `C.19` | causal data or policy support when needed |
| call plan | `C.24` | causal action-use field when planned calls serve a causal claim |
| bias or fairness audit | `D.5` | causal question, rung, estimand, support result, and the additional counterfactual-identification and estimation-consistency conditions when that branch is current |
| method dispatch | `G.5` | causal method-use classification and support refs |
| benchmark parity | `G.9` | rung, estimand, support-component, transport, and support-result parity |

#### C.28:4.13 - Cheap downgrade library

| Case | Plain bounded result |
| --- | --- |
| association only | “The evidence supports an association report; it does not support an intervention-effect claim.” |
| temporal change only | “The change in time is recorded; a causal-effect claim remains unsupported.” |
| non-causal simulation | “The simulator produced these traces; no causal use is claimed.” |
| simulation used causally | “The validated model supports this bounded model-based comparison; it does not supply realized or interventional evidence.” |
| metric-only fairness | “The metric disparity is reported; causal fairness is not established.” |
| logged policy | “The evaluation supports only the named behaviour/evaluation-policy regime and overlap limits; unqualified optimality is unsupported.” |
| cross-rung benchmark | “The methods answer different causal questions; publish the bridge and its loss, report degraded parity, or abstain instead of naming one causal winner.” |

#### C.28:4.14 - Payoff check

Keep a causal-use record only when it changes the supported causal statement, blocks a concrete overclaim, changes evidence work, or supplies a real basis to a downstream decision. Remove fields that do none of those things. Prefer triage when it preserves the same boundary.

#### C.28:4.15 - Publication-unit boundary

When only wording inside one publication unit is unclear, use the publication and wording patterns. Open C.28 only when the wording is relied on causally.

#### C.28:4.16 - Causal-laundering cases

| Case | Result |
| --- | --- |
| “Users who received X improved, so X works.” | Observational rung; association supported; intervention effect unsupported unless identification/design results close the gap. |
| “We changed X once, so the policy works everywhere.” | Interventional result limited to its population/environment/window; transport requires exact endpoints and assumptions. |
| “The simulator shows what would have happened.” | With no causal reliance, exit to model reporting. With causal reliance, cite the simulation result, assumptions, validation, supported model use, and unsupported realized/interventional use. |
| “The trial was randomized, therefore the estimate is valid.” | Run the common threats: interference, attrition, measurement, adherence, and analysis can still lower the result. |
| “The observational estimand is identified.” | Cite the identifying expression/derivation for `identified`; a bound supports `bounded` wording, and a nonidentification witness supports `nonidentified` wording. The label alone is incomplete. |
| “The fairness metric improved, therefore the intervention is fair.” | Report metric change. A counterfactual-fairness claim additionally needs its causal estimand, counterfactual-identifiability assumptions, estimate-consistency basis when used, and bounded C.28 support before D.5 audits it. |
| “Logged replay says this policy is optimal.” | Cite behaviour/evaluation policies, overlap, confounding, transport, uncertainty, and bounded support; unqualified optimality is unsupported. |
| “Method A beats Method B causally.” | Use G.9; different rungs, estimands, support components, endpoints, or windows require a bridge with stated loss, degraded parity, or abstention. |

