---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:6"
section_title: "Archetypal grounding (parallel domains)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__007_archetypal-grounding-parallel-domains.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:6 — Archetypal grounding (parallel domains)"
line_start: 24437
line_end: 24513
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
  - "U.Work admitted kind"
  - "actual binding"
  - "affected referent"
  - "enactsMethod"
  - "episode"
  - "no automatic transformation"
  - "occurrence assertion and record separation"
  - "overlap"
  - "performed resource-use fact"
  - "performedBy"
  - "retry"
  - "work continuity"
  - "work part"
  - "world-side dated occurrence"
---

### A.15.1:6 - Archetypal grounding (parallel domains)

Each case below is presented as readable content of a separate assertion or description episteme. Arrow notation abbreviates independently obtaining world-side relations involving the named Work individual; `methodDescriptionRef` and continuity-policy references cite separate epistemes. The bullet layout declares no slots or fields on the Work individual.

#### A.15.1:6.1 - Surgical case (overlap and episodes)

* **Top work occurrence:** `Appendectomy_Case_2025-08-10T0905_1142`.
* **Actual method and containing system:** `enactsMethod -> Appendectomy@Hospital-2025`; `executedWithin -> SurgicalService_A`.
* **Affected referent and performed resources:** an exact affected-referent relation connects the occurrence to `Patient_8472`; separately obtaining resource-use relations connect it to actual use of operating theatre `OR_7`, consumables pack `AppendectomyKit_8472`, and assigned staff time during the occurrence. No result, change, delivery, or acceptance follows from those relations.
* **`methodDescriptionRef`:** `Appendectomy_v5`.
* **Performer:** `U.RoleAssignment` with holder system `OR_Team_A`, role value `SurgicalTeamRole`, role-taxonomy episteme `HospitalRoles-2025`, and effective reference scheme `Hospital-Operating-Scheme-2025`; the assignment occurrence covers the surgery interval.
* **Operational parts:** `Incision` (09:15–09:22), `Exploration` (overlaps with monitoring), `Closure` (11:10–11:35).
* **Episode:** brief power dip 10:02-10:07 -> **resumptionOf** same occurrence (per hospital policy).
* **B.1.4 temporal roll-up:** a recovered temporal aggregation uses union for OR utilization and hull for patient lead time under separately declared policies.
* **B.1.6 resource roll-up:** a recovered `WorkResourceAggregation@Context` totals consumables and staff time once under its typed resource basis and overlap policy; every contributing resource-use relation continues to obtain independently with the exact Work occurrence as a participant.

#### A.15.1:6.2 - ETL pipeline (parallelism and retries)

* **Top work occurrence:** `ETL_Nightly_2025-08-11T01:00-01:47`.
* **Actual method and containing system:** `enactsMethod -> Nightly_ETL_Load@DataOps-2025`; `executedWithin -> DataPlatform_Prod`.
* **Affected referent, actual participation, and performed resources:** `WarehouseOrders_2025-08-11` is the affected dataset. The obtaining source-dataset participation of `RawOrders_2025-08-11` and destination-dataset participation of `WarehouseOrders_2025-08-11`, under their exact project data-use relations, are the actual-use facts on which this case relies. Actual cluster machine-time on `ETL_Cluster_3` and storage use on `WarehouseStore_1` are performed resource-use facts. None supplies a generic input/output binding or an automatic dataset-transformation claim.
* **`methodDescriptionRef`:** `ETL_v12.bpmn`.
* **Performer:** `U.RoleAssignment` with holder system `ETL_Runtime`, role value `TransformerRole`, role-taxonomy episteme `DataOpsRoles-2025`, and effective reference scheme `DataOps-Execution-Scheme-2025`; the assignment occurrence covers the ETL interval.
* **Parallel parts:** `Extract_A` ‖ `Extract_B`; `Transform` starts when either completes (overlap).
* **Retry:** `WarehouseWrite` failed at 01:36; retried with batch size ↓ — **new Work** linked via `retryOf`.
* **B.1.4 temporal roll-up:** a recovered temporal aggregation uses hull for SLA and union for cluster utilization under separately declared policies.
* **B.1.6 resource roll-up:** a recovered resource aggregation sums compute minutes under its declared overlap policy; source-dataset participation, destination-dataset participation, storage use, returned values, and downstream result claims stay under their exact direct relations rather than one input-output family.

#### A.15.1:6.3 - Thermodynamic cycle (work through a state-plane trace)

* **Run:** `Carnot_Cycle_Run_2025-08-09T1300_1306`.
* **Actual method and containing system:** `enactsMethod -> Carnot_Cycle_Operation@ThermoLab`; `executedWithin -> LabRig_7`.
* **Affected referent and performed resources:** `WorkingFluidCharge_7`; actual electrical-energy use attributed to the run through `HeaterBank_7` and `Chiller_7` during 13:00-13:06. Any thermodynamic energy-exchange or transformation claim remains separately governed.
* **`methodDescriptionRef`:** `Carnot_Cycle_Spec` with Dynamics model.
* **Performer:** `U.RoleAssignment` with holder system `LabRig_7`, role value `TransformerRole`, role-taxonomy episteme `ThermoLabRoles-v2`, and effective reference scheme `ThermoLab-Experiment-Scheme`; the assignment occurrence covers the laboratory-work interval.
* **Work identity:** a separate identity assertion under exact `workContinuityPolicyRef` designates the occurrence and cites the independently obtaining performer-assignment, enacted-method, temporal, containing-system, affected-referent, binding, and performed resource-use relations needed by that policy. The thermodynamic state-plane trace separately describes or evidences actual change; it is not a work-identity field, work-control relation, or ordered instruction sequence.
* **Part B roll-ups:** B.1.4 may use the exact run interval in a temporal aggregation; B.1.6 may aggregate the performed energy-use facts under a typed resource basis and selected overlap policy. Any thermodynamic energy-exchange or transformation claim keeps its direct governor; no "steps" are required.

#### A.15.1:6.4 - Claim handling (episodes versus monitoring slices)

* **Top work occurrence:** `ClaimHandling_Case_8142_2026-06-03`.
* **Actual method and containing system:** `enactsMethod -> ClaimHandling@InsuranceOps-2026`; `executedWithin -> ClaimsOperations_A`.
* **Affected referent and performed resources:** `Claim_8142`; actual handler time during 09:00-09:42 and 10:11-10:38, plus actual case-system time on `ClaimsPlatform_A` during those episodes. The callback and monitoring records remain neighboring evidence or telemetry, not occurrence constituents.
* **`methodDescriptionRef`:** `Claims_Method_v7`.
* **Performer:** `U.RoleAssignment` with holder system `ClaimsTeam_A`, role value `ClaimsHandlerRole`, role-taxonomy episteme `InsuranceOpsRoles-2026`, and effective reference scheme `Claims-Handling-Scheme-2026`; the assignment occurrence covers the claims-work interval.
* **Episode policy:** a customer callback interruption under one hour keeps the same parent work identity and creates two `EpisodeOf_work` fragments: `InitialReview_09:00-09:42` and `ResumedResolution_10:11-10:38`.
* **Temporal monitoring slice:** `MonitoringSlice_09:15-09:20` is `TemporalPartOf_work` for queue-latency evidence. It is not a new work occurrence and not an episode unless downstream reliance needs a named part with its own evidence, KPI, acceptance, repair, or aggregation role.
* **Method relation:** both episodes enact the same claim-handling method. The five-minute slice does not prove a submethod.

#### A.15.1:6.5 - Internal-combustion engine (cycle parts without human-only boundary language)

* **Top work occurrence:** `EngineRun_Cell7_2026-06-03T1300_1330`.
* **Actual method and containing system:** `enactsMethod -> FourStrokeEngineOperation@TestBench-2026`; `executedWithin -> Engine_Cell7`.
* **Affected referent and performed resources:** `EngineUnderTest_7`; actual fuel use from `FuelBatch_F7` and ignition-electrical-energy use during 13:00-13:30. Any thermodynamic change, result, or evidence claim remains separately governed.
* **`methodDescriptionRef`:** `FourStrokeOperationSpec_v4`.
* **Performer:** `U.RoleAssignment` with holder system `Engine_Cell7`, role value `EngineOperationRole`, role-taxonomy episteme `EngineCellRoles-2026`, and effective reference scheme `TestBench-Operating-Scheme-2026`; the assignment occurrence covers the engine-run interval.
* **Episodes:** start, stop, mode-change, fuel/ignition policy, or diagnosis policy may bound `EpisodeOf_work` fragments. The definition uses boundary events and policy, not a human-attention metaphor.
* **Temporal parts:** crank-angle intervals or one-second telemetry windows are `TemporalPartOf_work` unless an exact receiving use requires a named work part for resource, evidence, KPI, acceptance, repair, or aggregation.
* **Method factors:** intake, compression, combustion-expansion, and exhaust are method factors only if recovered as `U.Method` submethods with method-level preconditions, effects, interfaces, and whole-method relation. Actual strokes are work parts or temporal parts of engine work, not submethods by label.

#### A.15.1:6.6 - Detector radio receiver (component behavior, method factor, work part)

* **Top work occurrence:** `ReceiverReception_Rx42_2026-06-03T2115_2120`.
* **Actual method and containing system:** `enactsMethod -> EnvelopeDetection@RadioLab-2026`; `executedWithin -> Receiver_Rx42`.
* **Affected referent and performed resources:** `RF_TestSignal_42_2115`; actual receiver-channel time on `Rx42_Channel_1` and electrical-energy use during 21:15-21:20. Waveform and telemetry traces remain separately governed representations or evidence.
* **`methodDescriptionRef`:** `EnvelopeDetectionMethod_v2`.
* **Performer:** `U.RoleAssignment` with holder system `Receiver_Rx42`, role value `DetectorReceiverRole`, role-taxonomy episteme `RadioLabRoles-2026`, and effective reference scheme `RadioLab-Reception-Scheme-2026`; the assignment occurrence covers the reception interval.
* **Episodes:** a continuous reception interval between retune, on/off, interruption, or declared diagnostic mode events is `EpisodeOf_work` only under the receiver's episode policy.
* **Temporal parts:** a one-second reception slice is `TemporalPartOf_work` for signal-quality evidence or telemetry aggregation. It is not a new occurrence merely because it appears in a trace.
* **Method and mechanism split:** tuning, rectification, smoothing, and acoustic output may be recovered as method factors, system-component behaviors, mechanism material, evidence traces, or operational work parts depending on the current claim. A detector component or waveform segment does not become a submethod or a work part by label.

#### A.15.1:6.7 - Classification work without result collapse

`Pump37_RecognitionWork_2026-07-20T1015_1022` is one Work individual admitted under `U.Work`, with temporal extent 10:15-10:22. Exact `performedBy(Pump37_RecognitionWork_2026-07-20T1015_1022, Pump37_EvaluatorAssignment_2026-07-20)` obtains. That `U.RoleAssignment` has holder system `RecognitionEvaluator_A`, role value `HolonRecognitionEvaluatorRole`, role-taxonomy episteme `FPFRoles-2026`, effective reference scheme `FPF-Recognition-Scheme-2026`, and an assignment extent covering the work. Exact `enactsMethod(Pump37_RecognitionWork_2026-07-20T1015_1022, HolonRecognitionEvaluation@FPF)` and `executedWithin(Pump37_RecognitionWork_2026-07-20T1015_1022, FPF_Recognition_Service_A)` obtain, and the governed affected-referent fact concerns `Pump_37`. A separate assertion about the Work occurrence cites exact A.6.1 application `Pump37_RecognitionApplication_2026-07-20T1017`, whose `candidateArgument` binding designates `Pump_37` and whose `judgmentResult` binding returns `unknown`. Separately obtaining resource-use relations ground seven minutes of evaluator time and the application compute time on `RecognitionRunner_A`.

The returned `unknown` value remains the A.6.1 result binding. Candidate-side criterion satisfaction remains under A.1; evidence and assurance remain neighboring relations; and any materialized classification assertion or evaluation-result episteme remains under C.2.1. None is the Work occurrence or an intrinsic Work result field.

