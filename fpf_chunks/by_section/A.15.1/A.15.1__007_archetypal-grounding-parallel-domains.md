---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:6"
section_title: "Archetypal grounding (parallel domains)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__007_archetypal-grounding-parallel-domains.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:6 — Archetypal grounding (parallel domains)"
line_start: 24531
line_end: 24625
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
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
  - "E.10.ARCH"
  - "E.17"
  - "F.6"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.System"
  - "U.SystemRoleAssignment"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actual performer U.System"
  - "admitted U.Work kind"
  - "containing System"
  - "covering U.SystemRoleAssignment"
  - "enacted Method"
  - "optional direct bindings and resource use"
  - "performedUnderAssignment"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:6 - Archetypal grounding (parallel domains)

Each case below is presented as readable content of a separate assertion or description episteme. Arrow notation abbreviates independently obtaining world-side relations involving the named Work individual; `methodDescriptionRef` and continuity-policy references cite separate epistemes. The bullet layout declares no slots or fields on the Work individual.

#### A.15.1:6.1 - Surgical case (overlap and episodes)

* **Top work occurrence:** `Appendectomy_Case_2025-08-10T0905_1142`.
* **Actual method and containing system:** `enactsMethod -> Appendectomy@Hospital-2025`; `executedWithin -> SurgicalService_A`.
* **Patient and administered dose:** project relation specification `MED-ADM-2026`, owned by `ClinicalAdministrationRelations@Hospital-8472`, declares `ClinicalWorkAdministersDoseToPatient(dose, patient, clinicalWork, interval)`. The stipulated administration facts make it obtain for `MedicineDose_8472`, `Patient_8472`, `Appendectomy_Case_2025-08-10T0905_1142`, and the surgery interval. This relation establishes only that administration claim. The case names no admitted predicates for theatre, consumables, or staff-time resource use, so those optional claims return `missing-governor[SURGERY-RESOURCE-USE]` and do not enter Work identity.
* **`methodDescriptionRef`:** `Appendectomy_v5`.
* **Performer System and assignment:** `SurgicalTeamAssignment` is the directly declared assignment species; its signature gives the holder and assigned-kind participant meanings and uses the local `SurgicalTeamSystemRole` domain. `OR_Team_A_SurgicalTeamAssignment_2025-08-10` is the obtaining occurrence: its holder value is `OR_Team_A`, its assigned-kind value is `SurgicalTeamSystemRole`, and its extent covers the surgery. F.6 states that `OR_Team_A` performed this Work under that occurrence. The team System acts; the species and occurrence do not.
* **Operational parts:** `Incision` (09:15–09:22), `Exploration` (overlaps with monitoring), `Closure` (11:10–11:35).
* **Episode:** a brief power dip occurs from 10:02 to 10:07. The named surgery-continuity use applies `HospitalWorkContinuityPolicy_2025`, a C.2.1 policy episteme interpreted under `Hospital-Operating-Scheme-2025`; its stated pause-and-resumption criterion keeps both event-bounded fragments under the same parent Work. The power dip alone would not decide that grouping.
* **B.1.4 temporal roll-up:** `SurgeryORUtilizationAggregation-8472` uses union under `ORUtilizationUnionPolicy-2025`; `SurgeryPatientLeadTimeAggregation-8472` uses hull under `PatientLeadTimeHullPolicy-2025`. Both consume the named surgery and part intervals; neither supplies a resource-use or acceptance relation.
* **B.1.6 resource roll-up:** no positive aggregate is asserted in this fixture because the direct theatre-, consumables-, and staff-time resource-use predicates are absent. Preserve the Work and the administration relation and return `missing-governor[SURGERY-RESOURCE-USE]`; open B.1.6 only after the project declares those predicates and supplies their actual participants and facts.

#### A.15.1:6.2 - ETL pipeline (parallelism and retries)

* **Top work occurrence:** `ETL_Nightly_2025-08-11T01:00-01:47`.
* **Actual method and containing system:** `enactsMethod -> Nightly_ETL_Load@DataOps-2025`; `executedWithin -> DataPlatform_Prod`.
* **Dataset participation; resource stop:** relation specification `ETL-DATA-REL-2025`, owned by `ETLDataUseRelations@WarehousePlatform`, declares `SourceDatasetParticipatesInETLWork(dataset, work, extent)` and `DestinationDatasetParticipatesInETLWork(dataset, work, extent)`. The stipulated job facts make the first obtain for `RawOrders_2025-08-11`, `ETL_Nightly_2025-08-11T01:00-01:47`, and its extent, and the second for `WarehouseOrders_2025-08-11` with the same Work and extent. Neither predicate means later analytics use or dataset transformation. The case names no direct cluster-time or storage-use predicate, so those optional claims return `missing-governor[ETL-RESOURCE-USE]`.
* **Actual change, no connection yet:** A.3.4 identifies `WarehouseOrders_LoadTransformation_2025-08-11` as the bounded change of the exact dated warehouse partition across 01:00–01:47 under the declared source-snapshot and partition-write conditions. Before that boundary the partition lacks `AcceptedOrdersRowSet_2025-08-11`; after it, the project data-state relation to that row set obtains. This fixture declares neither a direct W-to-T predicate nor a complete A.6.RCD disposition-2 claim with a constructor, governed base predicates, participants, and case facts, so it returns `missing-governor[ETL-WORK-TO-CHANGE]`. Keep the Work, transformation, and dataset-participation facts; shared time, destination label, and post-state do not connect W to T.
* **Performer System and assignment:** `TransformerRuntimeAssignment` is the directly declared assignment species; its signature gives the holder and assigned-kind participant meanings and uses the local `TransformerSystemRole` domain. `ETL_Runtime_TransformerAssignment_2025-08-11` is the obtaining occurrence: its holder value is `ETL_Runtime`, its assigned-kind value is `TransformerSystemRole`, and its extent covers the ETL interval. F.6 states that `ETL_Runtime` performed this Work under that occurrence. The runtime System acts; the species and occurrence do not.
* **Parallel parts:** `Extract_A` ‖ `Extract_B`; `Transform` starts when either completes (overlap).
* **Retry:** `WarehouseWrite` failed at 01:36; retried with batch size ↓ — **new Work** linked via `retryOf`.
* **B.1.4 temporal roll-up:** `ETLSLACoverageAggregation-2025` uses hull under `ETLSLAHullPolicy-2025`; `ETLClusterUtilizationAggregation-2025` uses union under `ETLClusterUnionPolicy-2025`. They consume the named Work-part intervals and do not establish dataset participation, resource use, or change.
* **B.1.6 resource roll-up:** no compute or storage aggregate is asserted until the ETL project declares cluster-time and storage-use predicates and supplies the exact Work, resource, value, unit, and extent participants. Until then return `missing-governor[ETL-RESOURCE-USE]`; the two dataset-participation relations remain valid.

#### A.15.1:6.3 - Thermodynamic cycle (work through a state-plane trace)

* **Run:** `Carnot_Cycle_Run_2025-08-09T1300_1306`.
* **Actual method and containing system:** `enactsMethod -> Carnot_Cycle_Operation@ThermoLab`; `executedWithin -> LabRig_7`.
* **Referent and energy-use stop:** this fixture supplies no admitted predicate relating the run to `WorkingFluidCharge_7` and no direct predicate for electrical-energy use through `HeaterBank_7` or `Chiller_7`. Keep the grounded Work occurrence and return `missing-governor[THERMO-REFERENT-AND-ENERGY-USE]` for those optional claims. A state-plane trace, shared interval, or equipment label cannot fill the missing predicates.
* **`methodDescriptionRef`:** `Carnot_Cycle_Spec` with Dynamics model.
* **Performer System and assignment:** `ThermoRigTransformerAssignment` is the directly declared assignment species; its signature gives the holder and assigned-kind participant meanings and uses the local `TransformerSystemRole` domain. `LabRig_7_TransformerAssignment_2025-08-09` is the obtaining occurrence: its holder value is `LabRig_7`, its assigned-kind value is `TransformerSystemRole`, and its extent covers the laboratory Work. F.6 states that `LabRig_7` performed this Work under that occurrence. The rig System acts; the species and occurrence do not.
* **Work identity:** this uninterrupted six-minute run is identified from its actual entry, extent, performer System, enacted Method, containing System, and the covering assignment occurrence and F.6 attribution just stated. Those world-side facts obtain whether a short report displays their identifiers. No continuity-policy reference is needed because no interruption or competing segmentation is current. The optional referent and energy-use claims remain at `missing-governor[THERMO-REFERENT-AND-ENERGY-USE]`. The thermodynamic state-plane trace separately describes or evidences actual change; it is not a Work field, control relation, or instruction sequence.
* **Part B roll-ups:** no B.1.4 temporal aggregate is asserted in this fixture. A later roll-up must name this Work ref, the aggregation concern, window, coverage and non-overlap conditions, and the exact policy selecting union, hull, or another admitted result; the run interval alone is insufficient. B.1.6 cannot aggregate energy use until the missing direct energy-use predicate and participants are supplied. Any thermodynamic transformation remains independently grounded under A.3.4 and needs its own named W-to-T route before connection to this Work.

#### A.15.1:6.4 - Claim handling (episodes versus monitoring slices)

* **Top work occurrence:** `ClaimHandling_Case_8142_2026-06-03`.
* **Actual method and containing system:** `enactsMethod -> ClaimHandling@InsuranceOps-2026`; `executedWithin -> ClaimsOperations_A`.
* **Claim and resource stop:** this fixture names `Claim_8142`, handler-time intervals, and `ClaimsPlatform_A`, but supplies no admitted Work-to-claim, handler-time-use, or case-system-time-use predicate. Keep the grounded claim-handling Work and return `missing-governor[CLAIM-REFERENT-AND-RESOURCE-USE]` for those optional relations. Callback and monitoring records remain neighboring evidence or telemetry, not occurrence constituents.
* **`methodDescriptionRef`:** `Claims_Method_v7`.
* **Performer System and assignment:** `ClaimsHandlerAssignment` is the directly declared assignment species; its signature gives the holder and assigned-kind participant meanings and uses the local `ClaimsHandlerSystemRole` domain. `ClaimsTeam_A_HandlerAssignment_2026-06-03` is the obtaining occurrence: its holder value is `ClaimsTeam_A`, its assigned-kind value is `ClaimsHandlerSystemRole`, and its extent covers the claims Work. F.6 states that `ClaimsTeam_A` performed this Work under that occurrence. The team System acts; the species and occurrence do not.
* **Episode policy:** the named claims-handling continuity use applies `ClaimsWorkContinuityPolicy_v7`, a C.2.1 policy episteme interpreted under `Claims-Handling-Scheme-2026`. Its stated under-one-hour callback criterion supports assertion `ClaimsSegmentation-v7-8142`: `InitialReview_09:00-09:42` and `ResumedResolution_10:11-10:38` are two `EpisodeOf_work` fragments under the same parent.
* **Nearest non-continuing replacement:** competing episteme `ClaimsWorkContinuityPolicy_15min-Alt`, interpreted under the same reference scheme, states a fifteen-minute callback threshold. Applied to the same 29-minute gap, it supports assertion `ClaimsSegmentation-15min-8142` that the resumed performance is a later Work occurrence rather than an episode under the first parent. No `EpistemeEditionRelation` between the exact v7 and 15-minute policy epistemes is established, so the second is a non-continuing replacement, not an edition. Either assertion may govern its named receiving use; switching the selected policy changes the use-local segmentation judgment, not either interval's actual history. Only if C.2.1's historical-continuation predicate is separately satisfied may the later policy be called an edition.
* **Temporal monitoring slice:** `MonitoringSlice_09:15-09:20` is `TemporalPartOf_work` for queue-latency evidence. It is not a new Work occurrence and not an episode unless downstream reliance needs a named part with its own evidence, KPI, acceptance, repair, or separately consumed place in an aggregation.
* **Method relation:** under `ClaimsSegmentation-v7-8142`, both episodes enact the same claim-handling method; under `ClaimsSegmentation-15min-8142`, each of the two Work occurrences enacts that method. The segmentation choice changes neither enactment fact. The five-minute slice does not prove a submethod.

#### A.15.1:6.5 - Internal-combustion engine (cycle parts without human-only boundary language)

* **Top work occurrence:** `EngineRun_Cell7_2026-06-03T1300_1330`.
* **Actual method and containing system:** `enactsMethod -> FourStrokeEngineOperation@TestBench-2026`; `executedWithin -> Engine_Cell7`.
* **Engine and resource stop:** this fixture supplies no admitted Work-to-engine, fuel-use, or ignition-energy-use predicate for `EngineUnderTest_7`, `FuelBatch_F7`, and the 13:00–13:30 run. Keep the grounded engine-cell Work and return `missing-governor[ENGINE-REFERENT-AND-RESOURCE-USE]`; a test-bench label or shared interval establishes none of those optional relations.
* **`methodDescriptionRef`:** `FourStrokeOperationSpec_v4`.
* **Performer System and assignment:** `EngineCellOperationAssignment` is the directly declared assignment species; its signature gives the holder and assigned-kind participant meanings and uses the local `EngineOperationSystemRole` domain. `Engine_Cell7_OperationAssignment_2026-06-03` is the obtaining occurrence: its holder value is `Engine_Cell7`, its assigned-kind value is `EngineOperationSystemRole`, and its extent covers the engine run. F.6 states that `Engine_Cell7` performed this Work under that occurrence. The engine-cell System acts; the species and occurrence do not.
* **Episodes:** when diagnosis or utilization needs event-bounded fragments, `EngineRunEpisodePolicy_2026`, a C.2.1 policy episteme under `TestBench-Operating-Scheme-2026`, states which start, stop, mode-change, fuel, ignition, or diagnostic events bound an `EpisodeOf_work`. Without that named use and branch criterion, the events remain direct history and do not mint episode objects.
* **Temporal parts:** crank-angle intervals or one-second telemetry windows are `TemporalPartOf_work` unless an exact receiving use requires a named work part for resource, evidence, KPI, acceptance, repair, or aggregation.
* **Method factors:** intake, compression, combustion-expansion, and exhaust are method factors only if recovered as `U.Method` submethods with method-level preconditions, effects, interfaces, and whole-method relation. Actual strokes are work parts or temporal parts of engine work, not submethods by label.

#### A.15.1:6.6 - Detector radio receiver (component behavior, method factor, work part)

* **Top work occurrence:** `ReceiverReception_Rx42_2026-06-03T2115_2120`.
* **Actual method and containing system:** `enactsMethod -> EnvelopeDetection@RadioLab-2026`; `executedWithin -> Receiver_Rx42`.
* **Signal and resource stop:** this fixture supplies no admitted Work-to-signal, receiver-channel-time-use, or electrical-energy-use predicate for `RF_TestSignal_42_2115`, `Rx42_Channel_1`, and the 21:15–21:20 reception. Keep the grounded receiver Work and return `missing-governor[RECEIVER-REFERENT-AND-RESOURCE-USE]`; waveform and telemetry traces remain representations or evidence.
* **`methodDescriptionRef`:** `EnvelopeDetectionMethod_v2`.
* **Performer System and assignment:** `DetectorReceiverAssignment` is the directly declared assignment species; its signature gives the holder and assigned-kind participant meanings and uses the local `DetectorReceiverSystemRole` domain. `Receiver_Rx42_DetectorAssignment_2026-06-03` is the obtaining occurrence: its holder value is `Receiver_Rx42`, its assigned-kind value is `DetectorReceiverSystemRole`, and its extent covers the reception. F.6 states that `Receiver_Rx42` performed this Work under that occurrence. The receiver System acts; the species and occurrence do not.
* **Episodes:** when signal-quality or diagnostic use needs event-bounded fragments, `ReceiverReceptionEpisodePolicy_2026`, a C.2.1 policy episteme under `RadioLab-Reception-Scheme-2026`, states whether retune, on/off, interruption, or diagnostic-mode events bound an `EpisodeOf_work`. A trace timestamp or retune label without that current branch criterion remains history, not an episode relation.
* **Temporal parts:** a one-second reception slice is `TemporalPartOf_work` for signal-quality evidence or telemetry aggregation. It is not a new occurrence merely because it appears in a trace.
* **Method and mechanism split:** tuning, rectification, smoothing, and acoustic output may be recovered as method factors, system-component behaviors, mechanism material, evidence traces, or operational work parts depending on the current claim. A detector component or waveform segment does not become a submethod or a work part by label.

#### A.15.1:6.7 - Classification work without result collapse

`Pump37_RecognitionWork_2026-07-20T1015_1022` is one Work individual admitted under `U.Work`, with temporal extent 10:15–10:22. `RecognitionEvaluatorAssignment` is a directly declared species whose signature uses the local `RecognitionEvaluatorSystemRole` domain. `Pump37_EvaluatorAssignment_2026-07-20` is its obtaining occurrence, with `RecognitionEvaluator_A` as holder and an extent covering the Work. Exact F.6 `performedUnderAssignment`, `enactsMethod(Pump37_RecognitionWork_2026-07-20T1015_1022, HolonRecognitionEvaluation@FPF)`, and `executedWithin(Pump37_RecognitionWork_2026-07-20T1015_1022, FPF_Recognition_Service_A)` obtain. A.6.1 application `Pump37_RecognitionApplication_2026-07-20T1017` has obtaining `candidateArgument -> Pump_37` and `judgmentResult -> unknown` bindings, so candidate participation and returned value need no generic affected-referent or Work-result relation. This fixture supplies no admitted evaluator-time or runner-compute resource-use predicate; return `missing-governor[PUMP37-RESOURCE-USE]` for those optional claims without lowering the Work or application bindings.

The returned `unknown` value remains the A.6.1 result binding. No `U.Transformation` of `Pump_37` or of a classification record is asserted. This evaluation Work remains admitted from its performer system, covering assignment, enacted method, extent, and containing system; the application binding is a separate obtaining fact, and the absent optional resource-use predicates do not lower the Work. No pre-state, post-state, or delta is needed. Candidate-side criterion satisfaction remains under A.1; evidence and assurance remain neighboring relations; and any materialized classification assertion or evaluation-result episteme remains under C.2.1. None is the Work occurrence or an intrinsic Work result field.

#### A.15.1:6.7.1 - Filled result route: build, verify, transfer, accept

`BuildRunnerAssignment` is a directly declared species whose signature uses the local `BuildRunnerSystemRole` domain. `BuildRunnerAssignment_2026-07-21` is its obtaining occurrence, with `BuildRunner_A : U.System` as holder and an extent covering 09:00–09:12. F.6 states that `BuildRunner_A` performed `ReleaseBinary12_BuildWork_2026-07-21T0900_0912 : U.Work` under that occurrence. The Work enacts `ReproducibleBuild@BuildOps-v12` and is executed within `BuildService_A`. Those facts establish the Work occurrence. The rows below add only the result and consequence claims that are current in this case.

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

