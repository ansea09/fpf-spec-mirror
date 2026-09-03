---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:6"
section_title: "Archetypal grounding (parallel domains)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__007_archetypal-grounding-parallel-domains.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:6 — Archetypal grounding (parallel domains)"
line_start: 25217
line_end: 25310
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.27.TA"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ROLE"
  - "E.17"
  - "F.6"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.WorkPlan"
keywords:
  - "A.13-qualified actual performer U.System"
  - "F.6 only after admission for precise assignment-bound attribution"
  - "conditional agency profile"
  - "containing System"
  - "enacted Method"
  - "exact performance history"
  - "independent U.Work admission"
  - "optional direct bindings and resource use"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:6 - Archetypal grounding (parallel domains)

#### A.15.1:6.0 - Change without Work and self-directed Work

- **Change without Work:** `LunarTideRise-2026-07-27` may be identified under A.3.4 as a Transformation of the exact water body over the stated interval. The fixture supplies no actual performer `U.System` with an A.13 agency basis for a tidal action, no Method that such a performer followed, and no containing-System relation for a performed occurrence, so A.15.1 does not admit Work. A causal explanation, assignment-like label, or hypothetical F.6 link supplies none of those missing admission facts.
- **Self-directed Work:** in the rehabilitation case, the current model admits `MotorControlRightArmSystem-7 : U.System` and `Person-7 : U.System`; A.14 `ComponentOf(MotorControlRightArmSystem-7, Person-7)` and `ComponentOf(LeftArm-7, Person-7)` obtain, so the mover and the affected limb are distinct parts of one person. `SelfCarePerformerSystemRole` is a declared local agential kind for the stated stretch action; the case gives its target-relative membership criterion, classifies `MotorControlRightArmSystem-7` under it, makes `SelfCarePerformerAssignment-7` obtain for the scope and window, and cites evidence that the System satisfies that local criterion; this case makes no Grade or autonomy-profile claim. `MotorControlRightArmSystem-7` then performs `LeftArmStretchWork-7` from `2026-07-27T07:30:00+03:00` to `2026-07-27T07:35:00+03:00` under that assignment; F.6 `performedUnderAssignment` obtains and the Work enacts `AssistedLeftArmStretchMethod-E1`. Clinic relation specification `ClinicRehabRelations@Clinic-E1` declares `RehabWorkOccursWithinPersonBoundary@Clinic-E1(work, system)` for the stated person delimitation and five-minute window, and the case facts make it obtain for that Work and `Person-7`. The same specification declares `RehabWorkStretchesLimb@Clinic-E1(work, limb, interval)`, which obtains for that Work, `LeftArm-7`, and the five-minute interval. Separately, A.6.1 application `AssistedStretchApplication-7` binds its declared `AffectedLimbArgument` to `LeftArm-7`. The first Work-to-limb fact and the operation binding remain different; neither is a primitive self-relation, and this case-specific decomposition is not a required anatomy for every self-directed action.

These branches test admitted facts, not human resemblance. A non-human or molecular-scale System can perform Work when its A.1 admission, A.13 local kind and criterion, classification, obtaining assignment for the scope, working situation, and window, evidence adequate for those core claims, exact performance history, actual enacted Method, extent, and at least one obtaining local Work-to-System containment relation ground A.15.1 admission; unfamiliar agency is not a reason to reject it. If a receiving use also claims the exact assignment under which that Work was performed, check F.6 separately after admission. Add an A.13 characteristic profile only for a Grade, autonomy or profile claim, a criterion-dependent characteristic, or a named assurance use.

Each case below is presented as readable content of a separate assertion or description episteme. Arrow notation abbreviates independently obtaining world-side relations involving the named Work individual; `methodDescriptionRef` and continuity-policy references cite separate epistemes. The bullet layout declares no slots or fields on the Work individual.

#### A.15.1:6.1 - Surgical case (overlap and episodes)

* **Top work occurrence:** `Appendectomy_Case_2025-08-10T0905_1142`.
* **Actual method and containing-system relation:** `enactsMethod -> Appendectomy@Hospital-2025`; `SurgicalWorkOccursWithinServiceBoundary@Hospital-8472(Appendectomy_Case_2025-08-10T0905_1142, SurgicalService_A)` obtains under the service delimitation declared in `SurgicalServiceWorkBoundaryRelations@Hospital-8472`.
* **Patient and administered dose:** project relation specification `MED-ADM-2026`, owned by `ClinicalAdministrationRelations@Hospital-8472`, declares `ClinicalWorkAdministersDoseToPatient(dose, patient, clinicalWork, interval)`. The stipulated administration facts make it obtain for `MedicineDose_8472`, `Patient_8472`, `Appendectomy_Case_2025-08-10T0905_1142`, and the surgery interval. This relation establishes only that administration claim. The case names no admitted predicates for theatre, consumables, or staff-time resource use, so those optional claims return `missing-governor[SURGERY-RESOURCE-USE]` and do not enter Work identity.
* **`methodDescriptionRef`:** `Appendectomy_v5`.
* **A.13 Agent basis, performer System, and assignment:** `SurgicalTeamSystemRole` is a declared local agential kind for coordinated operative action; its criterion requires goal-directed, condition-sensitive regulation of the stated surgical action, the fixture classifies `OR_Team_A : U.System` under it, and cited evidence supports that local criterion and classification for the surgery scope and window; no Grade or autonomy-profile claim is used. `SurgicalTeamAssignment` is the directly declared assignment species whose signature gives the holder and assigned-kind participant meanings. `OR_Team_A_SurgicalTeamAssignment_2025-08-10` is the obtaining occurrence: its holder is `OR_Team_A`, its assigned kind is `SurgicalTeamSystemRole`, and its extent covers the surgery. F.6 states that `OR_Team_A` performed this Work under that occurrence. The team System acts; the kind, species, and occurrence do not.
* **Operational parts:** `Incision` (09:15–09:22), `Exploration` (overlaps with monitoring), `Closure` (11:10–11:35).
* **Episode:** a brief power dip occurs from 10:02 to 10:07. The named surgery-continuity use applies `HospitalWorkContinuityPolicy_2025`, a C.2.1 policy episteme interpreted under `Hospital-Operating-Scheme-2025`; its stated pause-and-resumption criterion keeps both event-bounded fragments under the same parent Work. The power dip alone would not decide that grouping.
* **B.1.4 temporal roll-up:** `SurgeryORUtilizationAggregation-8472` uses union under `ORUtilizationUnionPolicy-2025`; `SurgeryPatientLeadTimeAggregation-8472` uses hull under `PatientLeadTimeHullPolicy-2025`. Both consume the named surgery and part intervals; neither supplies a resource-use or acceptance relation.
* **B.1.6 resource roll-up:** no positive aggregate is asserted in this fixture because the direct theatre-, consumables-, and staff-time resource-use predicates are absent. Preserve the Work and the administration relation and return `missing-governor[SURGERY-RESOURCE-USE]`; open B.1.6 only after the project declares those predicates and supplies their actual participants and facts.

#### A.15.1:6.2 - ETL pipeline (parallelism and retries)

* **Top work occurrence:** `ETL_Nightly_2025-08-11T01:00-01:47`.
* **Actual method and containing-system relation:** `enactsMethod -> Nightly_ETL_Load@DataOps-2025`; `ETLWorkOccursWithinPlatformBoundary@WarehousePlatform(ETL_Nightly_2025-08-11T01:00-01:47, DataPlatform_Prod)` obtains under the platform delimitation declared in `ETLWorkBoundaryRelations@WarehousePlatform`.
* **Dataset participation; resource stop:** relation specification `ETL-DATA-REL-2025`, owned by `ETLDataUseRelations@WarehousePlatform`, declares `SourceDatasetParticipatesInETLWork(dataset, work, extent)` and `DestinationDatasetParticipatesInETLWork(dataset, work, extent)`. The stipulated job facts make the first obtain for `RawOrders_2025-08-11`, `ETL_Nightly_2025-08-11T01:00-01:47`, and its extent, and the second for `WarehouseOrders_2025-08-11` with the same Work and extent. Neither predicate means later analytics use or dataset transformation. The case names no direct cluster-time or storage-use predicate, so those optional claims return `missing-governor[ETL-RESOURCE-USE]`.
* **Actual change, no connection yet:** A.3.4 identifies `WarehouseOrders_LoadTransformation_2025-08-11` as the bounded change of the exact dated warehouse partition across 01:00–01:47 under the declared source-snapshot and partition-write conditions. Before that boundary the partition lacks `AcceptedOrdersRowSet_2025-08-11`; after it, the project data-state relation to that row set obtains. This fixture declares neither a direct W-to-T predicate nor a complete A.6.RCD disposition-2 claim with a constructor, governed base predicates, participants, and case facts, so it returns `missing-governor[ETL-WORK-TO-CHANGE]`. Keep the Work, transformation, and dataset-participation facts; shared time, destination label, and post-state do not connect W to T.
* **A.13 Agent basis, performer System, and assignment:** `ETL_Runtime` is independently admitted as the exact running System. `BatchExecutionControllerSystemRole` is a declared local agential kind whose membership criterion requires condition-sensitive regulation of the stated batch action against the batch completion and failure policy. The runtime's scheduler, authoritative state, policy branches, retry/redirect behavior, and stop conditions support its classification under that local criterion at this grain; no Grade or autonomy-profile claim is used. `TransformerRuntimeAssignment` is the direct assignment species; `ETL_Runtime_TransformerAssignment_2025-08-11` is the obtaining occurrence with holder `ETL_Runtime`, assigned-kind value `BatchExecutionControllerSystemRole`, and an extent covering the ETL interval. Actual trace facts then support the dated ETL action and Method enactment; F.6 relates that Work to the same assignment. Code, a model artifact, the assignment alone, or a successful output does not supply agency or Work.
* **Parallel parts:** `Extract_A` ‖ `Extract_B`; `Transform` starts when either completes (overlap).
* **Retry:** `WarehouseWriteAttempt-1` ended at 01:36 without satisfying `WarehousePartitionWriteComplete@ETL-2025`; `WarehouseWriteAttempt-2` then entered to satisfy that same condition for the same dated partition and source snapshot with a smaller batch. Local declaration `ETLRetryRelations@WarehousePlatform` defines `RetriesWarehousePartitionWrite(later, earlier)` over `<U.Work, U.Work>` by exactly those facts and permits one immediate failed predecessor. The relation obtains for the two named attempts; a generic `retryOf` token is not used.
* **B.1.4 temporal roll-up:** `ETLSLACoverageAggregation-2025` uses hull under `ETLSLAHullPolicy-2025`; `ETLClusterUtilizationAggregation-2025` uses union under `ETLClusterUnionPolicy-2025`. They consume the named Work-part intervals and do not establish dataset participation, resource use, or change.
* **B.1.6 resource roll-up:** no compute or storage aggregate is asserted until the ETL project declares cluster-time and storage-use predicates and supplies the exact Work, resource, value, unit, and extent participants. Until then return `missing-governor[ETL-RESOURCE-USE]`; the two dataset-participation relations remain valid.

#### A.15.1:6.3 - Thermodynamic cycle without a whole-rig performer shortcut

`Carnot_Cycle_Run_2025-08-09T1300_1306` is a candidate Work designator, and `Carnot_Cycle_Operation@ThermoLab` is the proposed enacted Method. A state-plane trace can support thermodynamic state and Transformation claims, while a declared `ThermoWorkOccursWithinRigBoundary@ThermoLab` relation can locate an independently admitted Work occurrence inside `LabRig_7`.

The current fixture admits `LabRig_7` as a System and supports its containment and thermodynamic participation, but it does not independently declare a local agential kind for the rig whole, classify the rig under it, establish an obtaining assignment, or supply evidence that the rig whole satisfies such a criterion for the proposed cycle action. Do not invent whole-rig initiation, redirection, or stop facts. Recover the exact human operator, controller runtime, or coordinated team, its A.13 core, and the independently grounded occurrence, Method, extent, and containment facts before admitting the candidate as performed Work. Only after admission may a precise assignment-bound claim add F.6.

Until then, retain the supported System functioning, thermodynamic change, Method proposal, state-plane representation, and evidence claims. Lower only the unsupported Agent, performer, `U.Work`, and F.6 claims. A containing System, controlled apparatus, MethodDescription, or trace does not perform by being the locus or evidence of the cycle.

#### A.15.1:6.4 - Claim handling (episodes versus monitoring slices)

* **Top work occurrence:** `ClaimHandling_Case_8142_2026-06-03`.
* **Actual method and containing-system relation:** `enactsMethod -> ClaimHandling@InsuranceOps-2026`; `ClaimWorkOccursWithinOperationsBoundary@InsuranceOps(ClaimHandling_Case_8142_2026-06-03, ClaimsOperations_A)` obtains under the operations delimitation declared in `ClaimsWorkBoundaryRelations@InsuranceOps-2026`.
* **Claim and resource stop:** this fixture names `Claim_8142`, handler-time intervals, and `ClaimsPlatform_A`, but supplies no admitted Work-to-claim, handler-time-use, or case-system-time-use predicate. Keep the grounded claim-handling Work and return `missing-governor[CLAIM-REFERENT-AND-RESOURCE-USE]` for those optional relations. Callback and monitoring records remain neighboring evidence or telemetry, not occurrence constituents.
* **`methodDescriptionRef`:** `Claims_Method_v7`.
* **A.13 Agent basis, performer System, and assignment:** `ClaimsHandlerSystemRole` is a declared local agential kind for claim-resolution action; its criterion requires goal-directed, condition-sensitive regulation of the stated handling action, the fixture classifies `ClaimsTeam_A : U.System` under it, and cited evidence supports that local criterion and classification for the claim scope and window; no Grade or autonomy-profile claim is used. `ClaimsHandlerAssignment` is the directly declared assignment species whose signature gives the holder and assigned-kind participant meanings. `ClaimsTeam_A_HandlerAssignment_2026-06-03` is the obtaining occurrence: its holder is `ClaimsTeam_A`, its assigned kind is `ClaimsHandlerSystemRole`, and its extent covers the claims Work. F.6 states that `ClaimsTeam_A` performed this Work under that occurrence. The team System acts; the kind, species, and occurrence do not.
* **Episode policy:** `InitialReviewEpisodeWork-8142` and `ResumedResolutionEpisodeWork-8142` are first independently admitted as Work individuals with their own A.13-qualified actual performers, performance histories, enacted Methods, extents, and containing-System relations. Any precise assignment-bound attribution for either episode is checked separately through F.6 after admission. The named claims-handling continuity use then applies `ClaimsWorkContinuityPolicy_v7`, a C.2.1 policy episteme interpreted under `Claims-Handling-Scheme-2026`. Its stated under-one-hour callback criterion supports assertion `ClaimsSegmentation-v7-8142` that the two named Work individuals stand in `EpisodeOf_work` relations to `ClaimHandling_Case_8142_2026-06-03`. The policy supports the ambiguous grouping; it does not create either episode Work or relation.
* **Nearest non-continuing replacement:** competing episteme `ClaimsWorkContinuityPolicy_15min-Alt`, interpreted under the same reference scheme, states a fifteen-minute callback threshold. Applied to the same 29-minute gap, it supports assertion `ClaimsSegmentation-15min-8142` that the resumed performance is a later Work occurrence rather than an episode under the first parent. No `EpistemeEditionRelation` between the exact v7 and 15-minute policy epistemes is established, so the second is a non-continuing replacement, not an edition. Either assertion may govern its named receiving use; switching the selected policy changes the use-local segmentation judgment, not either interval's actual history. Only if C.2.1's historical-continuation predicate is separately satisfied may the later policy be called an edition.
* **Temporal monitoring slice:** `MonitoringSlice_09:15-09:20` is a C.27.TA temporal aspect used for queue-latency evidence. It is not a `TemporalPartOf_work` participant or an episode. If a later use needs an independently admitted Work sub-occurrence with its own performed content and exact extent, identify that Work first and test the applicable §4.1a part predicate.
* **Method relation:** under `ClaimsSegmentation-v7-8142`, both episodes enact the same claim-handling method; under `ClaimsSegmentation-15min-8142`, each of the two Work occurrences enacts that method. The segmentation choice changes neither enactment fact. The five-minute slice does not prove a submethod.

#### A.15.1:6.5 - Internal-combustion engine without cell-whole performerhood

`EngineRun_Cell7_2026-06-03T1300_1330` is a candidate Work designator and `FourStrokeEngineOperation@TestBench-2026` is the proposed Method. `Engine_Cell7` may be an admitted containing System, and `EngineUnderTest_7` may exhibit functioning, behaviour, causal participation, state change, and resource use under separately governed claims.

Those facts do not classify the cell whole or engine-under-test under a local agential kind. This fixture supplies no independent A.13 local-kind criterion, cell-whole classification, obtaining agential assignment, or evidence that the cell whole satisfies such a criterion. Recover the exact operator, controller runtime, or coordinated team, its A.13 core, and the independently grounded test action, Method, extent, and containment facts before admitting performed test Work. Only afterward may a precise assignment-bound attribution add F.6. If the admission basis is absent, keep the engine-cycle, telemetry, Method-factor, Transformation, and resource claims and leave the performer and Work unresolved.

Crank-angle intervals and one-second telemetry windows remain C.27.TA temporal aspects unless a receiving use first identifies an independently admitted performed Work sub-occurrence and the `TemporalPartOf_work` predicate passes. Intake, compression, combustion-expansion, and exhaust are Method factors only when A.3.1/B.1.5 establish their Method identities and whole-Method relation; physical strokes and traces do not become submethods or Work parts by label.

#### A.15.1:6.6 - Detector receiver: narrow control agency versus broad reception Work

`Receiver_Rx42` is an admitted System whose components can function and interact with `RF_TestSignal_42_2115`. A named automatic-gain-control loop may support a narrow A.13 claim only if a local `GainRegulationControllerSystemRole` has an independent target-relative membership criterion, the exact controller System satisfies it, an assignment obtains for the relevant window, and evidence shows that the System satisfies that criterion; add a characteristic profile only if the receiving use consumes one. That narrow claim does not make the receiver whole an Agent for envelope detection, diagnosis, or a broader reception service.

Admit `ReceiverReception_Rx42_2026-06-03T2115_2120` as Work only after the exact performer System, its complete A.13 basis, actual performance history, `enactsMethod` fact for `EnvelopeDetection@RadioLab-2026`, temporal extent, and containing-System relation independently pass A.15.1. Only after that admission may a precise assignment-bound claim add F.6. Otherwise retain receiver functioning, component behavior, waveform interaction, retuning trace, and Method proposal without a Work assertion.

A one-second reception slice remains a C.27.TA temporal aspect unless an independently admitted performed Work sub-occurrence and the direct part predicate are established. Tuning, rectification, smoothing, and acoustic output may be Method factors, component behaviors, mechanism material, evidence traces, or operational Work parts only under the pattern that defines the claimed relation; an AGC loop or detector component does not settle those identities.

#### A.15.1:6.7 - Classification work without result collapse

`Pump37_RecognitionWork_2026-07-20T1015_1022` is one Work individual admitted under `U.Work`, with temporal extent 10:15–10:22. `RecognitionEvaluatorAssignment` is a directly declared species whose signature uses the local `RecognitionEvaluatorSystemRole` domain. The fixture declares `RecognitionEvaluatorSystemRole` as a local agential kind, gives its evaluation-action membership criterion, classifies `RecognitionEvaluator_A` under it, and cites evidence that the System satisfies that local criterion for the scope and window; no Grade or autonomy-profile claim is used. `Pump37_EvaluatorAssignment_2026-07-20` is its obtaining occurrence, with `RecognitionEvaluator_A` as holder and an extent covering the Work. Exact F.6 `performedUnderAssignment` and `enactsMethod(Pump37_RecognitionWork_2026-07-20T1015_1022, HolonRecognitionEvaluation@FPF)` obtain. `FPFRecognitionWorkBoundaryRelations` declares `RecognitionWorkOccursWithinServiceBoundary(work, system)`; under its stated service delimitation and 10:15–10:22 window, the relation obtains for this Work and `FPF_Recognition_Service_A`. A.6.1 application `Pump37_RecognitionApplication_2026-07-20T1017` has obtaining `candidateArgument -> Pump_37` and `judgmentResult -> unknown` bindings, so candidate participation and returned value need no generic affected-referent or Work-result relation. This fixture supplies no admitted evaluator-time or runner-compute resource-use predicate; return `missing-governor[PUMP37-RESOURCE-USE]` for those optional claims without lowering the Work or application bindings.

The returned `unknown` value remains the A.6.1 result binding. No `U.Transformation` of `Pump_37` or of a classification record is asserted. This evaluation Work remains admitted from the stated performer's A.13 basis, independently grounded performance history, enacted Method, extent, and the obtaining service-boundary relation just stated; its covering assignment and F.6 attribution remain separate obtaining facts. The application binding is another separate fact, and the absent optional resource-use predicates do not lower the Work. No pre-state, post-state, or delta is needed. Candidate-side criterion satisfaction remains under A.1; evidence and assurance remain neighboring relations; and any materialized classification assertion or evaluation-result episteme remains under C.2.1.

#### A.15.1:6.7.1 - Filled result route: build, verify, transfer, accept

`BuildRunnerAssignment` is a directly declared species whose signature uses the local `BuildRunnerSystemRole` domain. The fixture declares `BuildRunnerSystemRole` as a local agential kind, gives its build-action membership criterion, classifies `BuildRunner_A : U.System` under it, and cites evidence that the System satisfies that local criterion for the scope and window; no Grade or autonomy-profile claim is used. `BuildRunnerAssignment_2026-07-21` is its obtaining occurrence, with that System as holder and an extent covering 09:00–09:12. The exact action history, Method, extent, and `BuildWorkOccursWithinServiceBoundary` fact first admit `ReleaseBinary12_BuildWork_2026-07-21T0900_0912 : U.Work`. F.6 then separately states that `BuildRunner_A` performed that Work under the same assignment. Those facts establish distinct Work and attribution results. The rows below add only the result and consequence claims that are current in this case. Every additional verification, evaluation, or acceptance Work named in a row needs its own A.15.1 admission basis; any precise assignment-bound attribution for it needs its own later F.6 check. It does not inherit `BuildRunner_A` or the build assignment.

| Current case claim | Exact object or relation | Kept separate from |
| --- | --- | --- |
| build application returned the binary | A.6.1 application `BuildApplication_12` of declared operation `storeWrite@BuildOps-v12`, with argument binding `storeTarget -> ArtifactStorePartition_12` and result binding `builtBinary -> ReleaseBinary_12` | entity inception, production completion, delivery, acceptance |
| subject practice also needs a direct result relation | case-local occurrence `BuildRunReturnedBinary_12` under already declared predicate `BuildRunReturnedBinary@BuildOps-v12`, relating the build Work to `ReleaseBinary_12`; if that declaration were absent, this row would be omitted and the A.6.1 binding retained | a universal `WorkResultRelation` |
| the artifact-store partition changed | A.3.4 identifies `ArtifactStorePopulationTransformation_12`. BuildOps relation specification `BuildOpsWorkChangeRelations-v12` declares the direct predicate `BuildWorkPopulatedStore@BuildOps-v12(work, transformation)` with participant order `<work, transformation>`. Its test requires the named Work to be the performed process that, through exact `storeWrite@BuildOps-v12` application `BuildApplication_12` and its `storeTarget -> ArtifactStorePartition_12` binding, brings about the independently identified population transformation of that same partition. The stipulated Work, application, target binding, and transformation facts make the predicate obtain for `ReleaseBinary12_BuildWork_2026-07-21T0900_0912` and `ArtifactStorePopulationTransformation_12`; C.2.1 assertion `BuildWorkPopulatedStore-12` states that positive claim | the application remains an independently identified occurrence used by the predicate test; shared time, artifact label, or returned binary cannot establish the direct W-to-T claim |
| this was production, the binary first existed, and production completed | three separate A.15.PROD local claims: whole-production-work participation for the build Work; inception of `ReleaseBinary_12` at 09:11 under `ReleaseBinaryIdentitySpec_v12`; completion at 09:12 under `BuildCompletionCriterion_v12` | one omnibus production/result record |
| verification returned `pass` | separate `ReleaseBinary12_VerificationWork_2026-07-21T0913_0918 : U.Work`, A.6.1 application `VerifyApplication_12`, result binding `verdict -> pass`, and C.2.1 episteme `BinaryVerificationResult_12` when the durable verdict claim is needed | acceptance and the build Work's result binding |
| checksums and test logs support that verdict claim | A.10 evidence-provenance relation `BinaryVerificationEvidenceUse_12`, bounded to the verification claim and staging decision | truth by carrier presence or acceptance |
| the binary moved to staging | relation occurrence `ArtifactTransferToStaging_12` under declared predicate `ArtifactTransferredToStaging@BuildOps-v12`, with participants `ReleaseBinary_12` and `StagingSystem_A`, establishes this transfer | production, verification, acceptance |
| staging accepted the binary | `StagingAcceptanceWork_12`, `StagingAcceptanceCriterion_v12`, and its returned verdict remain available, but this fixture declares no acceptance predicate relating that verdict to `ReleaseBinary_12`; return `missing-governor[STAGING-ACCEPTANCE]` and do not assert acceptance | transfer, evidence, or a bare `pass` value cannot fill the missing relation |

The readable report is therefore: the build Work occurred; a different entity was returned and produced; `BuildWorkPopulatedStore-12` states the positive local W-to-T claim; separate verification Work returned a verdict supported by evidence; and `ArtifactTransferToStaging_12` transferred the entity. Acceptance remains at `missing-governor[STAGING-ACCEPTANCE]`. Removing any non-current row does not alter the identity of the build Work.

