---
chunk_kind: "child"
pattern_id: "C.28"
pattern_title: "CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
section_id: "C.28:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28/C.28__006_solution.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "C.28 — CausalUse-CAL: Causal-Use Questions, Causality-Ladder Rungs, Identification and Realizability"
  - "C.28:4 — Solution"
line_start: 52197
line_end: 52753
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
  - "Pearl Causal Hierarchy"
  - "Structural Causal Model"
  - "association"
  - "causal diagram"
  - "causal estimand"
  - "causal evidence support basis"
  - "causal fairness"
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

Use a three-level causal-use escalation:

1. Start with `CausalUseTriageRecord`.
2. Escalate to `LocalCausalUseQuestionCard` or `DurableCausalUseQuestionCard` only when the claimed use needs a reusable causal-use record.
3. Add profiles or specialized records only when the claim triggers that exact need: identification, realizability, evidence design, fairness, policy evaluation, transportability, estimation validity, causal-variable representation, or parity.

The default move is cheap. The heavy move is triggered.

| Record or profile kind | Ordinary size | Trigger |
| --- | --- | --- |
| `CausalUseTriageRecord` | one short record; usually `5-8` lines covering activation, rung, comparator or counterfactual, causal support-basis triage value, supported use and unsupported use pair, and next supported use | any live causal wording or suspected causal laundering |
| `LocalCausalUseQuestionCard` | one small card; usually one causal-use question, one rung, optional comparator or estimand, one support basis, one supported use and unsupported use pair, and one next supported use | the team needs a reusable local record but not a publication, release, fairness, benchmark, or assurance object |
| `DurableCausalUseQuestionCard` | one durable card with causal-use kind, estimand, timing and outcome when needed, assumptions, rival causes, support basis, supported use and unsupported use pair, next supported use, and stop-or-reopen condition | the claim is decision-bearing, publication-bearing, fairness-bearing, benchmark-bearing, assurance-bearing, or reusable |
| heavy profile or specialized record | only the fields needed for the named triggered question or work item; absent fields remain absent rather than becoming implied dossier requirements | identification, realizability, target-trial emulation, parameter estimation, transportability, off-policy evaluation, causal representation, evidence design, fairness audit, or causal parity is materially needed |

#### C.28:4.0 - Causal-use governance and consumer carry-through boundary

`C.28` governs causal-use objects, `CausalEvidenceSupportBasis` values, causal-use support and unsupported-use statements, identification and realizability profiles, and causal-use verdicts.

Neighbor patterns keep their local authority and consume only the causal-use pieces they need: measurement, evidence path, assurance, fairness, decision, exploration, call-planning, dispatch, parity, and refresh records do not become causal-use governing patterns by carrying `C.28` fields.

| Object or decision | `C.28` governs | Neighbor may carry | Neighbor must not do |
| --- | --- | --- | --- |
| Causal-use kind and rung | `CausalUseClaimKind`, `CausalityLadderRung`, causal-use question, comparator or counterfactual, estimand, supported use, unsupported use | `causalUseSpec?`, `causalActionUseSpec?`, method dispatch spec, parity record, fairness audit card | Infer causal-use kind from local vocabulary alone or publish a higher `CausalityLadderRung` without C.28 support |
| Causal evidence support basis | `CausalEvidenceSupportBasis` and its five values | Evidence path refs in `A.10`, A.2.4 evidence-use relation slots for episteme-as-evidence use, consumer fields in `B.3`, `C.19`, `D.5`, `G.5`, and `G.9` | Mint another support-basis value set, add assumption-only values or no-support values, or let simulation-only output become realized evidence by name |
| Identification and realizability | `CausalIdentificationProfile`, `CounterfactualSamplingRealizabilityProfile`, their verdicts, and supported use and unsupported use | Evidence, assurance, decision, exploration, call-planning, fairness, dispatch, and parity refs to those profiles | Treat identification as direct sampling, or treat direct-sampling infeasibility as absence of all possible causal support |
| Graph and calculus naming | `CausalGraphRepresentationKind`, `GraphSeparationCriterionKind`, `CausalInferenceCalculusKind`, `StructuralCausalModel`, `CausalDiagramRef` | Named graph refs and calculus refs when the neighbor records the causal-use support basis and cited formalism | Use generic graph prose where the causal-use claim depends on a graph formalism or calculus |
| Assurance consequence | `CausalUseSupportVerdict` as causal-use action grammar | `B.3` degrade, block, or abstain consequences for `F-G-R/CL` assurance | Let assurance prose certify causal identification, realizability, or fairness |
| Fairness, policy, and parity specialization | Causal-use question, rung, estimand, support basis, and support verdict for fairness, policy, and causal method comparison | `D.5` ethical audit card or fairness audit card, `C.11` choice result, `C.19` pool policy, `C.24` call plan, `G.5` method dispatch spec, `G.9` parity report with local refs to consumed `C.28` support | Collapse metric disparity, policy replay, method dispatch, or benchmark score into a causal-use verdict |

A neighbor may quote the `C.28` values it consumes for by-value readability. Quoting the values does not transfer governing authority. A neighbor pattern governs only its local record and must cite `C.28` when the causal-use question or causal-support basis is live.

Compact crosswalk:

| Field or decision slot | Question answered | Typical values | Do not confuse with |
| --- | --- | --- | --- |
| `CausalityLadderRung` | What kind of causal question or use is being claimed? | observational association, interventional action, counterfactual comparison | the evidence source or the method family |
| `CausalEvidenceSupportBasis` | What support-basis value is being used for that causal use? | observational association, interventional action, realized counterfactual sample, identified counterfactual estimate, simulation-only output | the rung itself, a raw evidence-source label, a local evidence-use label, or a no-support verdict |
| `supportedUse` and `unsupportedUse` | What may the reader do next, and what must they not do? | `CausalUseSupportStatement`, `CausalUseUnsupportedStatement` | a confidence score, a graph name, a method name, or a neighboring governing pattern |

Rung-support-use examples:

| Rung | Support basis | Supported use | Unsupported use |
| --- | --- | --- | --- |
| `observationalAssociationRung` | `observationalAssociationSupportBasis` | association report, descriptive risk comparison, probe selection | intervention-effect claim, causal fairness certification, policy optimality |
| `interventionalActionRung` | `interventionalActionSupportBasis` | declared action-effect use inside assignment, follow-up, and outcome limits | counterfactual sample claim, cross-population policy claim without transportability |
| `counterfactualComparisonRung` | `identifiedCounterfactualEstimateSupportBasis` | identified or bounded counterfactual estimate under assumptions and profile refs | realized sample wording or assumption-free counterfactual certainty |
| `counterfactualComparisonRung` | `simulationOnlyCounterfactualOutputBasis` | bounded model-supported simulation use | realized counterfactual sample evidence, intervention-effect evidence |

#### C.28:4.1 - Causality-Ladder Rung

`CausalityLadderRung` is a controlled value set:

```text
CausalityLadderRung =
  observationalAssociationRung |
  interventionalActionRung |
  counterfactualComparisonRung
```

- `observationalAssociationRung` means passive observation, natural behavior, association, or seeing-only case.
- `interventionalActionRung` means `do(x)`, intervention, action setting, experiment, policy change, or action-effect case.
- `counterfactualComparisonRung` means counter-to-fact comparison, unit-history-conditioned comparison, potential-outcome contrast, or counterfactual-imagination case.

A higher causal-use rung is not supported by lower-rung data unless a `CausalIdentificationProfile`, `CounterfactualSamplingRealizabilityProfile`, or bounded-use statement says exactly what is supported and what is not.

#### C.28:4.1a - Causal-Use Claim Kind

`CausalUseClaimKind` is the controlled value set for the local causal-use claim being made:

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

- `causalEffectClaim` means a result is used as an effect, improvement, harm, intervention claim, or outcome claim.
- `counterfactualComparisonClaim` means a counter-to-fact, potential-outcome, or unit-history-conditioned comparison is being used.
- `causalFairnessClaim` means fairness is claimed through a causal path, intervention, counterfactual, or causal estimand rather than only a metric.
- `causalPolicyClaim` means a policy, action rule, exploration rule, or agentic strategy is claimed as causally preferable.
- `causalBenchmarkParityClaim` means causal methods are compared for parity, superiority, or benchmark consumption.
- `causalEvidenceSupportClaim` means an evidence path is being used as causal-use support.
- `causalAssuranceSupportClaim` means an assurance tuple or support verdict is being used for a causal-use claim.

Simulation-only causal use stays inside the existing claim-kind set. `simulationOnlyCounterfactualOutputBasis` is a support-basis value, with bounded use written through supported-use and unsupported-use statements; it is not a new `CausalUseClaimKind`. Use the relevant claim kind, usually `counterfactualComparisonClaim`, `causalPolicyClaim`, `causalBenchmarkParityClaim`, or `causalEvidenceSupportClaim`, and set `CausalEvidenceSupportBasis = simulationOnlyCounterfactualOutputBasis` with bounded model-supported use and unsupported use. Bounded model-supported simulation use does not become realized counterfactual sample evidence or intervention-effect evidence. Do not mint a separate simulation-only claim kind merely to avoid naming the support basis value.

Encoding rule: choose the causal-use claim kind by the question being answered, then choose `simulationOnlyCounterfactualOutputBasis` as the support basis and write `CausalUseSupportStatement` and `CausalUseUnsupportedStatement` for the bounded simulation use.

#### C.28:4.2 - Causal-Use Cards

Use a local card when the claim needs a small working record:

```text
LocalCausalUseQuestionCard:
  causalUseQuestionRef: U.CausalUseQuestion
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind?: CausalUseClaimKind
  comparatorOrCounterfactualRef?
  estimandRef?
  causalEvidenceSupportBasis: CausalEvidenceSupportBasis
  supportedUse: CausalUseSupportStatement
  unsupportedUse: CausalUseUnsupportedStatement
  nextCausalUseAction: CausalUseNextAction
```

Use a durable card when the claim is decision-bearing, publication-bearing, fairness-bearing, benchmark-bearing, assurance-bearing, or reusable:

```text
DurableCausalUseQuestionCard:
  causalUseQuestionRef: U.CausalUseQuestion
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind: CausalUseClaimKind
  causalInterventionSpecRef?
  comparatorOrCounterfactualRef?
  estimandRef: U.CausalEstimand
  potentialOutcomeContrastRef?
  targetTrialProtocolRef?
  assignmentOrInterventionWindowRef?
  causalFollowUpWindowRef?
  outcomeMeasureRef?
  causalAssumptionSetRef
  rivalCauseSetRef?
  causalEvidenceSupportBasis: CausalEvidenceSupportBasis
  causalIdentificationProfileRef?
  counterfactualSamplingRealizabilityProfileRef?
  causalParameterEstimationProfileRef?
  causalTransportabilityProfileRef?
  causalVariableRepresentationRef?
  falsificationOrNegativeControlRef?
  sensitivityAnalysisRef?
  rivalCauseStressTestRef?
  supportedUse: CausalUseSupportStatement
  unsupportedUse: CausalUseUnsupportedStatement
  nextCausalUseAction: CausalUseNextAction
  stopOrReopenCondition
```

The durable card is not the default. It is the record used when a causal note without the required `C.28` support basis would be unsafe.

#### C.28:4.3 - Causal Evidence Support Basis

`CausalEvidenceSupportBasis` is a controlled value set:

```text
CausalEvidenceSupportBasis =
  observationalAssociationSupportBasis |
  interventionalActionSupportBasis |
  realizedCounterfactualSampleSupportBasis |
  identifiedCounterfactualEstimateSupportBasis |
  simulationOnlyCounterfactualOutputBasis
```

This is the `C.28`-governed value set for causal evidence support basis. `causalAssumptionOnlySupport` and `noCausalEvidenceSupport` are not values of `CausalEvidenceSupportBasis`: assumption-only support condition belongs in `causalAssumptionSetRef` plus supported use and unsupported use; no-support basis value belongs in `CausalUseSupportVerdict`, `unsupportedUse`, or `abstain`.

Simulation-only output never becomes realized counterfactual-rung evidence by name alone. It may support model-based use only when assumptions, validation, and supported use and unsupported use are declared.

`CausalEvidenceSupportBasis` names a support-basis value. It is distinct from an evidence source, an `A.2.4` evidence-use relation, and an `A.10` evidence-provenance path. Some support bases are direct empirical support-basis classes, such as observational or interventional support. Other support bases are inferential support-basis classes, such as identified counterfactual estimate support. Do not read this value set as only a raw evidence-source kind.

`realizedCounterfactualSampleSupportBasis` does not mean observing two incompatible outcomes for the same unit in one realized world. It means physically obtaining samples from the declared target counterfactual distribution under the profile's physical, ethical, operational, unit-history, and graph constraints.

#### C.28:4.4 - Identification Profile

`CausalIdentificationProfile` answers whether a causal or counterfactual estimand can be expressed from available data plus assumptions, graph representation, and inferential calculus.

```text
CausalIdentificationProfile:
  causalUseQuestionRef: U.CausalUseQuestion
  estimandRef: U.CausalEstimand
  targetCausalityLadderRung: CausalityLadderRung
  sourceCausalEvidenceSupportBasis?: CausalEvidenceSupportBasis
  structuralCausalModelRef?: StructuralCausalModelRef
  causalDiagramRef?: CausalDiagramRef
  causalGraphRepresentationKind?: CausalGraphRepresentationKind
  graphSeparationCriterionKind?: GraphSeparationCriterionKind
  causalInferenceCalculusKind?: CausalInferenceCalculusKind
  causalAssumptionSetRef
  availableDataRegimeSetRef: AvailableCausalDataRegimeSetRef
  realizedCounterfactualDataRefs?: RealizedCounterfactualDataRefSet
  counterfactualDataIdentificationMethodRef?: CounterfactualDataIdentificationMethodRef
  counterfactualDataBoundRef?: CounterfactualDataBoundRef
  causalBoundOrPartialIdentificationRef?
  falsificationOrNegativeControlRef?
  sensitivityAnalysisRef?
  rivalCauseStressTestRef?
  verdict: identified | nonidentified | bounded | unknown
  supportedUse
  unsupportedUse
```

Identification is inferential support. It is not direct physical sampling.

Realized counterfactual data may change an identification derivation, tighten a bound, or change which assumptions are still needed. When it does, the profile names the data refs, identification method, and bound ref that changed the result. It does not erase the distinction between identification and direct sampling; the profile must still state what is identified, bounded, unknown, or not identified.

#### C.28:4.5 - Counterfactual Sampling Realizability Profile

`CounterfactualSamplingRealizabilityProfile` answers whether samples from a counterfactual-comparison target distribution can be physically obtained through admissible actions under physical, ethical, operational, unit-history, and graph constraints.

```text
CounterfactualSamplingRealizabilityProfile:
  causalUseQuestionRef: U.CausalUseQuestion
  targetCounterfactualDistributionRef
  targetCausalityLadderRung: counterfactualComparisonRung
  structuralCausalModelRef?: StructuralCausalModelRef
  causalDiagramRef?: CausalDiagramRef
  causalGraphRepresentationKind?: CausalGraphRepresentationKind
  graphSeparationCriterionKind?: GraphSeparationCriterionKind
  causalInferenceCalculusKind?: CausalInferenceCalculusKind
  graphChildInterventionConstraintRef?
  sameUnitConflictCheck
  ancestorRegimeConflictCheck
  physicalConstraintSetRef
  ethicalConstraintSetRef
  operationalConstraintSetRef
  unitHistoryAvailabilityRef?
  counterfactualSamplingActionSetRef
  counterfactualRandomizationCapabilityRef?
  counterfactualSamplingWorkPlanRef?
  verdict: realizable | nonrealizable | bounded | unknown
  supportedUse
  unsupportedUse
```

Realizability is operational. It asks what work can be done, by which system, with which action primitives, under which constraints.

#### C.28:4.6 - Applied Causal-Inference Profiles

Target-trial and potential-outcomes claims use `TargetTrialProtocolRecord` and `U.PotentialOutcomeContrast` when the causal-use claim is an applied intervention-effect claim.

```text
TargetTrialProtocolRecord:
  causalUseQuestionRef: U.CausalUseQuestion
  targetPopulationRef?
  eligibilityCriteriaRef?
  treatmentStrategySetRef
  treatmentAssignmentProcedureRef?
  timeZeroAlignmentRef?
  causalFollowUpWindowRef
  outcomeMeasureRef
  potentialOutcomeContrastRef?
  estimandRef: U.CausalEstimand
  causalAnalysisPlanRef?
```

Target-trial emulation from observational data adds a mapping and reporting record. `TargetTrialEmulationMappingRecord` records the fit between the protocol and the observed data; `TargetTrialProtocolRecord` alone does not state emulation adequacy.

```text
TargetTrialEmulationMappingRecord:
  targetTrialProtocolRef: TargetTrialProtocolRecord
  observationalDataSourceRef: ObservationalDataSourceRef
  eligibilityMappingRef: TargetTrialEligibilityMappingRef
  treatmentStrategyMappingRef: TargetTrialTreatmentStrategyMappingRef
  assignmentOrTimeZeroMappingRef: TargetTrialAssignmentOrTimeZeroMappingRef
  followUpMappingRef: TargetTrialFollowUpMappingRef
  outcomeMappingRef: TargetTrialOutcomeMappingRef
  emulationGapRef?: TargetTrialEmulationGapRef
  residualConfoundingAssessmentRef?: ResidualConfoundingAssessmentRef
  sensitivityOrAdditionalAnalysisRef?: TargetTrialSensitivityOrAdditionalAnalysisRef
  supportedEmulationUse: CausalUseSupportStatement
  unsupportedEmulationUse: CausalUseUnsupportedStatement
```

Numerical causal estimates use `CausalParameterEstimationProfile` when estimation validity is live:

```text
CausalParameterEstimationProfile:
  estimandRef: U.CausalEstimand
  causalIdentificationProfileRef?
  estimatorRef
  nuisanceModelSetRef?
  orthogonalScoreRef?
  crossFittingPlanRef?
  positivityOrOverlapCheckRef?
  sensitivityAnalysisRef?
  uncertaintyIntervalRef?
  supportedEstimateUse
  unsupportedEstimateUse
```

Transported support uses `CausalTransportabilityProfile`:

```text
CausalTransportabilityProfile:
  causalUseQuestionRef: U.CausalUseQuestion
  sourcePopulationRef
  targetPopulationRef
  sourceContextRef?
  targetContextRef?
  selectionDiagramRef?
  domainShiftAssumptionSetRef?
  transportFormulaOrBridgeRef?
  supportedTransportUse
  unsupportedTransportUse
```

Off-policy causal evaluation uses `OffPolicyCausalEvaluationProfile` when a policy is evaluated from data generated by another behavior or logging policy:

```text
OffPolicyCausalEvaluationProfile:
  evaluationPolicyRef
  behaviorPolicyRef
  causalUseQuestionRef: U.CausalUseQuestion
  sequentialHorizonRef?: SequentialPolicyHorizonRef
  adaptivePolicyClassRef?: AdaptivePolicyClassRef
  unitHistoryConditioningRef?: UnitHistoryConditioningRef
  confoundingAssumptionSetRef?
  supportOrOverlapCheckRef?
  policyTransportabilityRef?: CausalPolicyTransportabilityRef
  offPolicyEstimatorRef?
  uncertaintyIntervalRef?
  supportedPolicyUse
  unsupportedPolicyUse
```

Causal representation learning uses `CausalVariableRepresentationRecord` when abstract causal variables are learned, selected, abstracted, or represented from fine-grained observations rather than given by the domain:

```text
CausalVariableRepresentationRecord:
  causalUseQuestionRef?: U.CausalUseQuestion
  structuralCausalModelRef?: StructuralCausalModelRef
  causalVariableSetRef
  representationSourceRef
  abstractionOrSelectionMethodRef?
  interventionValidityRef?: CausalRepresentationInterventionValidityRef
  mechanismInvarianceRef?: CausalRepresentationMechanismInvarianceRef
  abstractionFidelityRef?: CausalRepresentationAbstractionFidelityRef
  counterfactualQueryPreservationRef?: CausalRepresentationCounterfactualQueryPreservationRef
  representationShiftRef?: CausalRepresentationShiftOrOODRef
  validationRef?
  supportedCausalVariableUse
  unsupportedCausalVariableUse
```

#### C.28:4.7 - Causal Graph Representation Names

Use names that causal inference specialists can recognize:

```text
CausalGraphRepresentationKind =
  causalDirectedAcyclicGraphRepresentation |
  acyclicDirectedMixedGraphRepresentation |
  singleWorldInterventionGraphRepresentation |
  structuralCausalModelTwinNetworkRepresentation |
  ancestralMultiWorldNetworkRepresentation |
  counterfactualGraphicalModelRepresentation
```

When graph separation or graphical calculus is part of the causal-use support, use controlled values rather than open prose:

```text
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

`CausalGraphRepresentationKind`, `GraphSeparationCriterionKind`, and `CausalInferenceCalculusKind` are formal-support classification values, not minted model objects. They classify the formal support form being used for causal support. Concrete `...Ref` fields point to actual models, diagrams, proof objects, assumptions, or epistemes and must be present when the causal-use claim depends on that formal support form. For example, `StructuralCausalModelRef` cites a concrete SCM object, while `structuralCausalModelTwinNetworkRepresentation` classifies a representation form.

`StructuralCausalModel` is the causal model kind with endogenous variables, exogenous variables, structural assignments, and intervention semantics. `structuralCausalModelTwinNetworkRepresentation` means the SCM twin-network representation used in counterfactual reasoning with shared exogenous variables. It is not a deep-learning twin network.

Acronyms such as SCM, DAG, ADMG, SWIG, and AMWN may appear as source labels, plain labels, and bridge notes. FPF Tech values expand the source name when expansion reduces alias risk.

#### C.28:4.8 - Causal Use Evidence Design

Use `CausalUseEvidenceDesignRecord` when the causal-use claim needs evidence planning, evidence graph support, experiment or quasi-experiment design, counterfactual randomization, mixed-design accountability, or simulation validation.

```text
CausalUseEvidenceDesignRecord:
  causalUseQuestionRef: U.CausalUseQuestion
  targetCausalityLadderRung: CausalityLadderRung
  estimandRef?
  causalInterventionSpecRef?
  targetTrialProtocolRef?
  potentialOutcomeContrastRef?
  causalIdentificationProfileRef?
  causalParameterEstimationProfileRef?
  counterfactualSamplingRealizabilityProfileRef?
  causalTransportabilityProfileRef?
  causalVariableRepresentationRef?
  causalEvidenceSupportBasis: CausalEvidenceSupportBasis
  causalEvidenceWorkRefs?
  causalEvidenceUseRelationRefs?
  causalEvidenceWorkRoleAssignmentRefs?
  causalEvidenceMethodRef?
  causalEvidenceWorkPlanRef?
  structuralCausalModelRef?
  causalDiagramRef?
  causalGraphRepresentationKind?: CausalGraphRepresentationKind
  graphSeparationCriterionKind?: GraphSeparationCriterionKind
  causalInferenceCalculusKind?: CausalInferenceCalculusKind
  counterfactualGraphicalModelClassRef?
  causalAssumptionSetRef
  counterfactualModelAssumptionSetRef?
  simulationValidationRef?
  falsificationOrNegativeControlRef?
  sensitivityAnalysisRef?
  rivalCauseStressTestRef?
  decisionThresholdAffected?: yes | no | unclear
  causalEvidenceDecisionImpactRef?: CausalEvidenceDecisionImpactRef
  evidenceValueOrProbeWorthinessRef?: EvidenceValueOrProbeWorthinessRef
  causalEvidenceCostRiskRef?: CausalEvidenceCostRiskRef
  supportedUse
  unsupportedUse
```

This record does not replace `A.10` or `B.3`. It gives them causal-use structure.

Higher-requirement causal evidence is worth planning only when it can change a choice, deployment decision, fairness consequence, assurance consequence, or benchmark conclusion enough to justify its cost, risk, and delay. If additional support would not change the next action, keep the narrower supported use explicit and stop.

#### C.28:4.9 - Verdicts

`CausalUseSupportVerdict` is the action grammar:

- `supported` means proceed only under the named supported use.
- `bounded` means proceed only inside the named limit and record `causalBoundedUseReason`.
- `unsupported` means downgrade the claim or remove causal use.
- `abstain` means no causal-use conclusion and records `causalAbstainReason`.

No verdict is allowed to silently widen the claim beyond its evidence support basis.

#### C.28:4.10 - Causal Action Policy Class

Use `CausalActionPolicyClass` when a decision, exploration policy, call plan, or agentic strategy depends on causal rung:

```text
CausalActionPolicyClass =
  naturalBehaviorPolicy |
  interventionalPolicy |
  counterfactualPolicy
```

- `naturalBehaviorPolicy` follows observed or natural behavior.
- `interventionalPolicy` chooses an action or `do(x)`.
- `counterfactualPolicy` acts conditioned on natural action, unit history, or counterfactual response.

This distinction matters for `C.11`, `C.19`, and `C.24`; it does not make those patterns the authority for causal evidence, identification, or realizability.

`CausalActionPolicyClass` is a classification value for policy-use class: natural behavior, interventional action, counterfactual policy, mixed policy, or unknown policy. It is not the policy object, not `U.Policy`, not `C.19` pool policy, and not the executable policy used by an agent.

#### C.28:4.10a - Local `U.*` alignment

`U.CausalUseQuestion` names the question whose answer would make a causal use admissible: association use, intervention-effect use, counterfactual-comparison use, causal fairness use, causal policy use, causal evidence support use, causal assurance use, or causal parity use. It governs the question-to-use relation, not the evidence path, estimator, policy object, graph object, or local neighbor pattern.

`U.CausalEstimand` names the target quantity, contrast, distribution, or functional answer shape for a `U.CausalUseQuestion`. It binds the question to what would have to be estimated, identified, sampled, bounded, or emulated. It is not the estimator, not the observed metric, not the graph, not the policy object, and not the support verdict.

The card and profile family relates to those heads this way: triage decides whether a `U.CausalUseQuestion` is live; local cards and durable cards stabilize the question, `U.CausalEstimand`, and supported use and unsupported use boundary; profiles and specialized records state what support basis, formal support form, operational work, assumptions, and admissible use the question-estimand pair can carry.

Local name cards:

| Name | Kind | Plain sense | Must not mean |
| --- | --- | --- | --- |
| `U.CausalUseQuestion` | question object for causal-use admissibility | the question-to-use object stabilized by triage, local cards, or durable cards before a claim is used causally | a whole research project, evidence path, graph, estimator, policy object, or neighboring-pattern application |
| `U.CausalEstimand` | target causal quantity, contrast, distribution, or functional | the answer-shape object linked to a `U.CausalUseQuestion` before estimation, identification, sampling, bounding, or emulation is judged | estimator, metric reading, support verdict, policy object, or causal graph |

Lexical tripwires:

| Phrase | Use instead when the causal-use claim depends on it |
| --- | --- |
| "causal evidence" | name `CausalEvidenceSupportBasis`, `A.10` evidence path refs, `CausalUseSupportRecordRef`, `CausalUseSupportStatement`, and `CausalUseUnsupportedStatement` |
| "counterfactual data" | distinguish realized counterfactual data refs, `realizedCounterfactualSampleSupportBasis`, `identifiedCounterfactualEstimateSupportBasis`, and `simulationOnlyCounterfactualOutputBasis` |
| "policy optimality" | name `causalPolicyClaim`, `CausalActionPolicyClass`, `OffPolicyCausalEvaluationProfile`, `CausalUseSupportStatement`, and unsupported unqualified optimality |
| "fairness evidence" | distinguish metric fairness or evaluation fairness from `causalFairnessClaim` with rung, estimand, support basis, support record and verdict, and supported fairness use and unsupported fairness use |
| "method improves" | name whether the claim is association, intervention effect, counterfactual comparison, or parity result, then name rung, support basis, and supported use and unsupported use |
| "what would have happened" | name counterfactual comparison support, realized counterfactual sample support, identified estimate support, or simulation-only bounded model use |

#### C.28:4.11 - Neighbor Governing-Pattern Selection Table

| If the issue under repair is... | Use... | `C.28` role |
| --- | --- | --- |
| measured value, score, scale, indicator, or metric definition | `C.16` | Only active when the measure is used causally. |
| temporal trend, rate, acceleration, inertia, or rhythm wording | `C.27` | Active when temporal wording is used as causal effect or intervention evidence. |
| evidence graph reference or provenance | `A.10` | Carries evidence path or provenance path and C.28 support-basis refs, not causal-use support authority. |
| assurance level, degrade, abstain, or trust or assurance result | `B.3` | Consumes C.28 support verdicts and applies assurance consequences. |
| local decision among options | `C.11` | Provides causal action-policy hooks when value, regret, or optimality depends on causal rung. |
| exploration and exploitation over live pools | `C.19` | Provides causal data-collection or causal policy-learning hooks when live. |
| tool, call, or enactment plan | `C.24` | Provides optional causal action use spec when the call selects observation, intervention, counterfactual-rung evidence collection, or counterfactual policy conditioning. |
| bias and fairness audit | `D.5` | Provides causal fairness rung and supported fairness use. |
| method dispatch or selector-facing registry | `G.5` | Provides causal method-class declarations or causal policy-class declarations when causal methods are compared. |
| benchmark or method parity | `G.9` | Provides causal method rung parity. |
| quantum-like modeling cue | `C.26` | Receives only the residual QL cue after causal-use explanation has been tried. |

#### C.28:4.12 - Non-Goals

`C.28` does not:

- define physical causation or decide what causation is in the modeled world;
- choose one causal school, such as SCM and PCH, potential outcomes, target-trial emulation, transportability, causal ML, causal RL, or causal fairness, for all FPF use;
- certify a DAG, SCM, SWIG, AMWN, or other graph as true or sufficient causal support by naming it;
- replace local domain science, domain intervention definitions, outcome definitions, or substantive rival-cause knowledge;
- replace `C.16` measurement and metrics characterization, including metric construction, calibration, and non-causal score interpretation;
- replace `A.10` evidence graph referring, provenance paths, A.2.4 evidence-use relations, source-use relations, publication-use relations, or evidence graph path discipline;
- replace `B.3` trust and assurance calculus, assurance tuples, `F-G-R/CL` consequences, or assurance publication use;
- replace `D.5` bias audit and ethical assurance, causal-fairness audit responsibility, human-impact review, or group-impact review;

- replace `G.9` parity benchmark harness, causal-rung parity screen, or benchmark report structure;
- replace `C.11` choice, `C.19` exploration and exploitation policy, or `C.24` call-planning patterns; it only supplies causal-use support boundaries consumed by those patterns.

#### C.28:4.13 - Cheap Downgrade Library

Use a downgrade sentence when a narrower admissible use is enough:

Each sentence below is an admissible `cheapStop` wording. It closes the causal-use question for the named insufficient-support case unless the author keeps a publish, choose, deploy, assure, audit, benchmark, or support-treatment use that commits the text beyond the `cheapStop` boundary alive.

| Case | Admissible downgrade wording |
| --- | --- |
| association-only case | "Observed association only; supported use = association report; unsupported use = intervention-effect claim." |
| temporal-change-only case | "Temporal change or trend is recorded; supported use = temporal or rate description; unsupported use = causal-effect claim until a causal-use support basis is named." |
| simulation-only case | "Simulation-only counterfactual output; supported use = bounded model-supported exploration or explanation; unsupported use = realized counterfactual sample evidence or intervention-effect claim." |
| metric-only fairness case | "Metric disparity or metric improvement is recorded; supported use = metric-level fairness or disparity report; unsupported use = causal fairness claim without a causal rung, estimand, support basis, and supported fairness use." |
| logged-policy bounded case | "Logged-policy evidence supports only the declared behavior-policy and evaluation-policy regime; supported use = bounded off-policy evaluation under named overlap and transportability limits; unsupported use = unqualified optimal-policy claim." |
| cross-rung benchmark case | "Methods answer different causal rungs or support bases; supported use = publish bridge and loss, degraded parity, or abstain; unsupported use = one scalar causal winner." |

#### C.28:4.14 - Causal-use payoff check

The causal-use payoff check keeps a causal-use record only when it changes the admissible next action or blocks a concrete overclaim. Keep the causal-use record only when at least one answer is "yes":

| Question | If no |
| --- | --- |
| Did the record change the next action? | Remove fields until only the action-changing line remains. |
| Did it block a concrete causal overclaim by naming the causal use governed by `C.28` as unsupported? | Use association, trend, simulation-only, or metric-only wording and stop. |
| Did it support one concrete decision, evidence-work, fairness, assurance, benchmark-parity, or deployment action by changing `supportedUse` or `unsupportedUse`? | Keep the neighboring pattern and do not open a durable causal-use object. |
| Was there a cheaper `nextCausalUseAction.cheapStop` that preserved the same admissible use boundary? | Use the cheaper stop. |
| Is the problem only the word "causal" or "counterfactual", rather than an admissible causal use? | Repair wording locally or apply the neighboring language or authoring pattern. |

#### C.28:4.15 - PublicationUnit Stability Relation

When the live problem is only local wording pressure inside one `PublicationUnit`, local lexical-head repair under `E.17.AUD.LHR`, whole-unit primary entity-of-concern stabilization under `E.17.AUD.OOTD`, relational precision restoration, explanation faithfulness, or conservative retextualization, apply the governing publication-side FPF pattern rather than `C.28`. `C.28` opens at `CausalUseActivation`, when the wording makes publication, choice, deployment, assurance, audit, fairness, policy, or benchmark use depend on causal support.

#### C.28:4.16 - Causal-Laundering Golden Cases

| Case | Expected `C.28` output |
| --- | --- |
| Association laundering: "users who received X improved, so X works." | rung = `observationalAssociationRung`; support basis = `observationalAssociationSupportBasis`; supported use = association report; unsupported use = intervention-effect claim. |
| Intervention overclaim: "we changed X once, so the policy will work everywhere." | rung = `interventionalActionRung`; support basis = `interventionalActionSupportBasis` inside assignment, context, follow-up, and transportability limits; unsupported use = cross-population or unbounded policy claim. |
| Simulation laundering: "the simulator shows what would have happened." | claim kind = relevant existing `CausalUseClaimKind`; support basis = `simulationOnlyCounterfactualOutputBasis`; supported use = bounded model-supported use; unsupported use = realized counterfactual sample or intervention-effect evidence. |
| Metric-only fairness laundering: "fairness improved because the metric improved." | supported use = metric-level fairness report or disparity report; unsupported use = causal fairness claim unless `causalFairnessClaim`, rung, estimand, support basis, and supported fairness use are declared. |
| Policy replay overclaim: "logged replay says this policy is optimal." | claim kind = `causalPolicyClaim`; support basis = off-policy causal evaluation with behavior-policy refs and evaluation-policy refs and overlap checks and support checks; supported use = bounded policy evaluation; unsupported use = unqualified optimality. |
| Cross-rung benchmark: "method A beats method B as a causal method." | claim kind = `causalBenchmarkParityClaim`; use `G.9` `CausalRungParityScreen`; supported use = within-rung parity or declared bridge and loss; unsupported use = one scalar causal winner when rungs and support bases differ. |
| Temporal-cause wording: "after launch, recovery got faster, so launch caused resilience." | supported use = `C.27` temporal adequacy or rate adequacy; unsupported use = causal-effect claim until `C.28` names intervention timing, outcome window, assumptions, rival causes, and support basis. |
| QL escape: "ordinary probability is hard here, so the effect is quantum-like." | supported use = causal-use triage and ordinary-neighbor explanation first; unsupported use = bypassing `C.28` with quantum-like vocabulary; `C.26` is retained only for residual quantum-like probe, frame, order, export, or coarsening issue. |
| Target-trial name-drop: "we emulate a trial, so the effect is identified." | supported use = target-trial claim only with protocol plus emulation mapping, data source, assignment and time-zero, follow-up and outcome mapping, residual confounding, and sensitivity analysis and additional analysis; unsupported use = identification claim by target-trial label alone. |
| Realized-counterfactual-data claim: "we observed both outcomes for the same unit." | supported use = samples from the declared target counterfactual distribution under the realizability profile's constraints; unsupported use = same-world incompatible-outcome wording for one unit. |

