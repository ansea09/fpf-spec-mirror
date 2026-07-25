---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:6"
section_title: "Archetypal grounding (parallel domains)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__007_archetypal-grounding-parallel-domains.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:6 — Archetypal grounding (parallel domains)"
line_start: 24433
line_end: 24526
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
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actual performer U.System"
  - "admitted U.Work kind"
  - "containing system"
  - "covering U.RoleAssignment"
  - "enacted method"
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
* **Affected referent and performed resources:** an exact affected-referent relation connects the occurrence to `Patient_8472`; separately obtaining resource-use relations connect it to actual use of operating theatre `OR_7`, consumables pack `AppendectomyKit_8472`, and assigned staff time during the occurrence. No result, change, delivery, or acceptance follows from those relations.
* **`methodDescriptionRef`:** `Appendectomy_v5`.
* **Performer system and assignment:** admitted system `OR_Team_A` performs this occurrence under exact `OR_Team_A_SurgicalTeamAssignment_2025-08-10 : U.RoleAssignment`, whose role value is `SurgicalTeamRole`, role-taxonomy episteme is `HospitalRoles-2025`, effective reference scheme is `Hospital-Operating-Scheme-2025`, and obtaining extent covers the surgery interval. The team system acts; the assignment does not.
* **Operational parts:** `Incision` (09:15–09:22), `Exploration` (overlaps with monitoring), `Closure` (11:10–11:35).
* **Episode:** a brief power dip occurs from 10:02 to 10:07. The named surgery-continuity use applies `HospitalWorkContinuityPolicy_2025`, a C.2.1 policy episteme interpreted under `Hospital-Operating-Scheme-2025`; its stated pause-and-resumption criterion keeps both event-bounded fragments under the same parent Work. The power dip alone would not decide that grouping.
* **B.1.4 temporal roll-up:** a recovered temporal aggregation uses union for OR utilization and hull for patient lead time under separately declared policies.
* **B.1.6 resource roll-up:** a recovered `WorkResourceAggregation@Context` totals consumables and staff time once under its typed resource basis and overlap policy; every contributing resource-use relation continues to obtain independently with the exact Work occurrence as a participant.

#### A.15.1:6.2 - ETL pipeline (parallelism and retries)

* **Top work occurrence:** `ETL_Nightly_2025-08-11T01:00-01:47`.
* **Actual method and containing system:** `enactsMethod -> Nightly_ETL_Load@DataOps-2025`; `executedWithin -> DataPlatform_Prod`.
* **Affected referent, actual participation, and performed resources:** `WarehouseOrders_2025-08-11` is the affected dataset under the exact project data relation used by this case. The obtaining source-dataset participation of `RawOrders_2025-08-11` and destination-dataset participation of `WarehouseOrders_2025-08-11`, under their exact project data-use relations, are the actual-use facts on which this case relies. Actual cluster machine-time on `ETL_Cluster_3` and storage use on `WarehouseStore_1` are performed resource-use facts. None supplies a generic input/output binding or an automatic dataset-transformation claim.
* **Actual change, separately established:** A.3.4 identifies `WarehouseOrders_LoadTransformation_2025-08-11` as the bounded change of the exact dated warehouse partition across 01:00–01:47 under the declared source-snapshot and partition-write conditions. Before that boundary the partition lacks exact row set `AcceptedOrdersRowSet_2025-08-11`; after it, the project data-state relation to that row set obtains. A separate subject-governed work-to-change claim connects the transformation to `ETL_Nightly_2025-08-11T01:00-01:47`; temporal overlap, the destination designation, or the post-state alone would not. The transformation and connecting claim are not fields of the Work occurrence.
* **Performer system and assignment:** admitted system `ETL_Runtime` performs this occurrence under exact `ETL_Runtime_TransformerAssignment_2025-08-11 : U.RoleAssignment`, whose role value is `TransformerRole`, role-taxonomy episteme is `DataOpsRoles-2025`, effective reference scheme is `DataOps-Execution-Scheme-2025`, and obtaining extent covers the ETL interval. The runtime system acts; the assignment does not.
* **Parallel parts:** `Extract_A` ‖ `Extract_B`; `Transform` starts when either completes (overlap).
* **Retry:** `WarehouseWrite` failed at 01:36; retried with batch size ↓ — **new Work** linked via `retryOf`.
* **B.1.4 temporal roll-up:** a recovered temporal aggregation uses hull for SLA and union for cluster utilization under separately declared policies.
* **B.1.6 resource roll-up:** a recovered resource aggregation sums compute minutes under its declared overlap policy; source-dataset participation, destination-dataset participation, storage use, returned values, and downstream result claims stay under their exact direct relations rather than one input-output family.

#### A.15.1:6.3 - Thermodynamic cycle (work through a state-plane trace)

* **Run:** `Carnot_Cycle_Run_2025-08-09T1300_1306`.
* **Actual method and containing system:** `enactsMethod -> Carnot_Cycle_Operation@ThermoLab`; `executedWithin -> LabRig_7`.
* **Affected referent and performed resources:** `WorkingFluidCharge_7`; actual electrical-energy use attributed to the run through `HeaterBank_7` and `Chiller_7` during 13:00-13:06. Any thermodynamic energy-exchange or transformation claim remains separately governed.
* **`methodDescriptionRef`:** `Carnot_Cycle_Spec` with Dynamics model.
* **Performer system and assignment:** admitted system `LabRig_7` performs this occurrence under exact `LabRig_7_TransformerAssignment_2025-08-09 : U.RoleAssignment`, whose role value is `TransformerRole`, role-taxonomy episteme is `ThermoLabRoles-v2`, effective reference scheme is `ThermoLab-Experiment-Scheme`, and obtaining extent covers the laboratory-work interval. The rig system acts; the assignment does not.
* **Work identity:** this uninterrupted six-minute run is identified from its actual entry, extent, performer system, covering assignment and F.6 attribution when explicit, enacted method, and containing system, together with the actually obtaining work-to-referent, binding, and performed resource-use relations used in this case. No continuity-policy reference is needed because no interruption or competing segmentation is current. The thermodynamic state-plane trace separately describes or evidences actual change; it is not a work-identity field, work-control relation, or ordered instruction sequence.
* **Part B roll-ups:** B.1.4 may use the exact run interval in a temporal aggregation; B.1.6 may aggregate the performed energy-use facts under a typed resource basis and selected overlap policy. Any thermodynamic energy-exchange or transformation claim keeps its direct governor; no "steps" are required.

#### A.15.1:6.4 - Claim handling (episodes versus monitoring slices)

* **Top work occurrence:** `ClaimHandling_Case_8142_2026-06-03`.
* **Actual method and containing system:** `enactsMethod -> ClaimHandling@InsuranceOps-2026`; `executedWithin -> ClaimsOperations_A`.
* **Affected referent and performed resources:** `Claim_8142`; actual handler time during 09:00-09:42 and 10:11-10:38, plus actual case-system time on `ClaimsPlatform_A` during those episodes. The callback and monitoring records remain neighboring evidence or telemetry, not occurrence constituents.
* **`methodDescriptionRef`:** `Claims_Method_v7`.
* **Performer system and assignment:** admitted system `ClaimsTeam_A` performs this occurrence under exact `ClaimsTeam_A_HandlerAssignment_2026-06-03 : U.RoleAssignment`, whose role value is `ClaimsHandlerRole`, role-taxonomy episteme is `InsuranceOpsRoles-2026`, effective reference scheme is `Claims-Handling-Scheme-2026`, and obtaining extent covers the claims-work interval. The team system acts; the assignment does not.
* **Episode policy:** the named claims-handling continuity use applies `ClaimsWorkContinuityPolicy_v7`, a C.2.1 policy episteme interpreted under `Claims-Handling-Scheme-2026`. Its stated under-one-hour callback criterion classifies `InitialReview_09:00-09:42` and `ResumedResolution_10:11-10:38` as two `EpisodeOf_work` fragments under the same parent. A later edition may revise that segmentation assertion without changing either interval's actual history.
* **Temporal monitoring slice:** `MonitoringSlice_09:15-09:20` is `TemporalPartOf_work` for queue-latency evidence. It is not a new work occurrence and not an episode unless downstream reliance needs a named part with its own evidence, KPI, acceptance, repair, or aggregation role.
* **Method relation:** both episodes enact the same claim-handling method. The five-minute slice does not prove a submethod.

#### A.15.1:6.5 - Internal-combustion engine (cycle parts without human-only boundary language)

* **Top work occurrence:** `EngineRun_Cell7_2026-06-03T1300_1330`.
* **Actual method and containing system:** `enactsMethod -> FourStrokeEngineOperation@TestBench-2026`; `executedWithin -> Engine_Cell7`.
* **Affected referent and performed resources:** `EngineUnderTest_7`; actual fuel use from `FuelBatch_F7` and ignition-electrical-energy use during 13:00-13:30. Any thermodynamic change, result, or evidence claim remains separately governed.
* **`methodDescriptionRef`:** `FourStrokeOperationSpec_v4`.
* **Performer system and assignment:** admitted system `Engine_Cell7` performs this occurrence under exact `Engine_Cell7_OperationAssignment_2026-06-03 : U.RoleAssignment`, whose role value is `EngineOperationRole`, role-taxonomy episteme is `EngineCellRoles-2026`, effective reference scheme is `TestBench-Operating-Scheme-2026`, and obtaining extent covers the engine-run interval. The engine-cell system acts; the assignment does not.
* **Episodes:** when diagnosis or utilization needs event-bounded fragments, `EngineRunEpisodePolicy_2026`, a C.2.1 policy episteme under `TestBench-Operating-Scheme-2026`, states which start, stop, mode-change, fuel, ignition, or diagnostic events bound an `EpisodeOf_work`. Without that named use and branch criterion, the events remain direct history and do not mint episode objects.
* **Temporal parts:** crank-angle intervals or one-second telemetry windows are `TemporalPartOf_work` unless an exact receiving use requires a named work part for resource, evidence, KPI, acceptance, repair, or aggregation.
* **Method factors:** intake, compression, combustion-expansion, and exhaust are method factors only if recovered as `U.Method` submethods with method-level preconditions, effects, interfaces, and whole-method relation. Actual strokes are work parts or temporal parts of engine work, not submethods by label.

#### A.15.1:6.6 - Detector radio receiver (component behavior, method factor, work part)

* **Top work occurrence:** `ReceiverReception_Rx42_2026-06-03T2115_2120`.
* **Actual method and containing system:** `enactsMethod -> EnvelopeDetection@RadioLab-2026`; `executedWithin -> Receiver_Rx42`.
* **Affected referent and performed resources:** `RF_TestSignal_42_2115`; actual receiver-channel time on `Rx42_Channel_1` and electrical-energy use during 21:15-21:20. Waveform and telemetry traces remain separately governed representations or evidence.
* **`methodDescriptionRef`:** `EnvelopeDetectionMethod_v2`.
* **Performer system and assignment:** admitted system `Receiver_Rx42` performs this occurrence under exact `Receiver_Rx42_DetectorAssignment_2026-06-03 : U.RoleAssignment`, whose role value is `DetectorReceiverRole`, role-taxonomy episteme is `RadioLabRoles-2026`, effective reference scheme is `RadioLab-Reception-Scheme-2026`, and obtaining extent covers the reception interval. The receiver system acts; the assignment does not.
* **Episodes:** when signal-quality or diagnostic use needs event-bounded fragments, `ReceiverReceptionEpisodePolicy_2026`, a C.2.1 policy episteme under `RadioLab-Reception-Scheme-2026`, states whether retune, on/off, interruption, or diagnostic-mode events bound an `EpisodeOf_work`. A trace timestamp or retune label without that current branch criterion remains history, not an episode relation.
* **Temporal parts:** a one-second reception slice is `TemporalPartOf_work` for signal-quality evidence or telemetry aggregation. It is not a new occurrence merely because it appears in a trace.
* **Method and mechanism split:** tuning, rectification, smoothing, and acoustic output may be recovered as method factors, system-component behaviors, mechanism material, evidence traces, or operational work parts depending on the current claim. A detector component or waveform segment does not become a submethod or a work part by label.

#### A.15.1:6.7 - Classification work without result collapse

`Pump37_RecognitionWork_2026-07-20T1015_1022` is one Work individual admitted under `U.Work`, with temporal extent 10:15-10:22. Admitted system `RecognitionEvaluator_A` is the actual performer and performs this work under exact `Pump37_EvaluatorAssignment_2026-07-20 : U.RoleAssignment`. For explicit F.6 attribution, `performedUnderAssignment(Pump37_RecognitionWork_2026-07-20T1015_1022, Pump37_EvaluatorAssignment_2026-07-20)` obtains; its assignment endpoint is the ground under which `RecognitionEvaluator_A` performs and is not the actor. The assignment's role value is `HolonRecognitionEvaluatorRole`, role-taxonomy episteme is `FPFRoles-2026`, effective reference scheme is `FPF-Recognition-Scheme-2026`, and obtaining extent covers the work. Exact `enactsMethod(Pump37_RecognitionWork_2026-07-20T1015_1022, HolonRecognitionEvaluation@FPF)` and `executedWithin(Pump37_RecognitionWork_2026-07-20T1015_1022, FPF_Recognition_Service_A)` obtain, and the governed affected-referent fact concerns `Pump_37`. A separate assertion about the Work occurrence cites exact A.6.1 application `Pump37_RecognitionApplication_2026-07-20T1017`, whose `candidateArgument` binding designates `Pump_37` and whose `judgmentResult` binding returns `unknown`. Separately obtaining resource-use relations ground seven minutes of evaluator time and the application compute time on `RecognitionRunner_A`.

The returned `unknown` value remains the A.6.1 result binding. No `U.Transformation` of `Pump_37` or of a classification record is asserted: this evaluation Work remains admitted from its performer system, covering assignment, enacted method, extent, containing system, application binding, and resource-use facts without a pre-state, post-state, or delta. Candidate-side criterion satisfaction remains under A.1; evidence and assurance remain neighboring relations; and any materialized classification assertion or evaluation-result episteme remains under C.2.1. None is the Work occurrence or an intrinsic Work result field.

#### A.15.1:6.7.1 - Filled result route: build, verify, transfer, accept

`ReleaseBinary12_BuildWork_2026-07-21T0900_0912 : U.Work` is performed by `BuildRunner_A : U.System` under `BuildRunnerAssignment_2026-07-21 : U.RoleAssignment`, enacts `ReproducibleBuild@BuildOps-v12`, runs from 09:00 to 09:12, and is executed within `BuildService_A`. Those facts establish the Work occurrence. The rows below add only the result and consequence claims that are current in this case.

| Current case claim | Exact object or relation | Kept separate from |
| --- | --- | --- |
| build application returned the binary | A.6.1 application `BuildApplication_12`, with result binding `builtBinary -> ReleaseBinary_12` | entity inception, production completion, delivery, acceptance |
| subject practice also needs a direct result relation | case-local occurrence `BuildRunReturnedBinary_12` under already declared predicate `BuildRunReturnedBinary@BuildOps-v12`, relating the build Work to `ReleaseBinary_12`; if that declaration were absent, this row would be omitted and the A.6.1 binding retained | a universal `WorkResultRelation` |
| the artifact-store partition changed | `ArtifactStorePopulationTransformation_12 : U.Transformation` under A.3.4, plus the exact BuildOps work-to-change claim relating it to the build Work | the Work occurrence and the returned binary |
| this was production, the binary first existed, and production completed | three separate A.15.PROD local claims: whole-production-work participation for the build Work; inception of `ReleaseBinary_12` at 09:11 under `ReleaseBinaryIdentitySpec_v12`; completion at 09:12 under `BuildCompletionCriterion_v12` | one omnibus production/result record |
| verification returned `pass` | separate `ReleaseBinary12_VerificationWork_2026-07-21T0913_0918 : U.Work`, A.6.1 application `VerifyApplication_12`, result binding `verdict -> pass`, and C.2.1 episteme `BinaryVerificationResult_12` when the durable verdict claim is needed | acceptance and the build Work's result binding |
| checksums and test logs support that verdict claim | A.10 evidence-provenance relation `BinaryVerificationEvidenceUse_12`, bounded to the verification claim and staging decision | truth by carrier presence or acceptance |
| the binary moved to staging | subject-owned transfer occurrence `ArtifactTransferToStaging_12` under `ArtifactTransferredToStaging@BuildOps-v12`, with exact binary and staging-system participants | production, verification, acceptance |
| staging accepted the binary | acceptance work `StagingAcceptanceWork_12` applies `StagingAcceptanceCriterion_v12`; exact subject-owned acceptance relation `StagingAcceptance_12` relates its verdict to `ReleaseBinary_12` | transfer, evidence, or a bare `pass` value |

The readable report is therefore: the build Work occurred; a different entity was returned and produced; an exact store transformation occurred; separate verification Work returned a verdict supported by evidence; a transfer moved the entity; and a later acceptance relation admitted it. Removing any non-current row does not alter the identity of the build Work.

