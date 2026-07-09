---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:6"
section_title: "Archetypal grounding (parallel domains)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__007_archetypal-grounding-parallel-domains.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:6 — Archetypal grounding (parallel domains)"
line_start: 22055
line_end: 22111
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
  - "B.3"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "EpisodeOf_work"
  - "TemporalPartOf_work"
  - "actuals"
  - "concurrent work part"
  - "operational work part"
  - "performed enactment"
  - "trace"
  - "work occurrence"
---

### A.15.1:6 - Archetypal grounding (parallel domains)

#### A.15.1:6.1 - Surgical case (overlap and episodes)

* **Top work occurrence:** `Appendectomy_Case_2025-08-10T0905_1142`.
* **`methodDescriptionRef`:** `Appendectomy_v5`.
* **Performer:** `U.RoleAssignment` with holder slot `OR_Team_A`, role value `SurgicalTeamRole`, bounded-context slot `Hospital_2025`, and current-window slot covering the surgery interval.
* **Operational parts:** `Incision` (09:15–09:22), `Exploration` (overlaps with monitoring), `Closure` (11:10–11:35).
* **Episode:** brief power dip 10:02-10:07 -> **resumptionOf** same occurrence (per hospital policy).
* **Γ\_time:** union for OR utilization; hull for patient lead time.
* **Gamma_work:** totals consumables and staff time once (no double-count for overlapping work-part occurrences).

#### A.15.1:6.2 - ETL pipeline (parallelism and retries)

* **Top work occurrence:** `ETL_Nightly_2025-08-11T01:00-01:47`.
* **`methodDescriptionRef`:** `ETL_v12.bpmn`.
* **Performer:** `U.RoleAssignment` with holder slot `ETL_Runtime`, role value `TransformerRole`, bounded-context slot `DataOps_2025`, and current-window slot covering the ETL occurrence.
* **Parallel parts:** `Extract_A` ‖ `Extract_B`; `Transform` starts when either completes (overlap).
* **Retry:** `WarehouseWrite` failed at 01:36; retried with batch size ↓ — **new Work** linked via `retryOf`.
* **Γ\_time:** hull for SLA, union for cluster utilization.
* **Γ\_work:** sum compute minutes; attribute storage input and output once at the parent.

#### A.15.1:6.3 - Thermodynamic cycle (work through a state-plane trace)

* **Run:** `Carnot_Cycle_Run_2025-08-09T1300_1306`.
* **`methodDescriptionRef`:** `Carnot_Cycle_Spec` with Dynamics model.
* **Performer:** `U.RoleAssignment` with holder slot `LabRig_7`, role value `TransformerRole`, bounded-context slot `ThermoLab`, and current-window slot covering the lab occurrence.
* **Work identity:** the occurrence is identified by the occurrence interval plus occurrence references; the thermodynamic state-plane trace is a dynamics or geometry relation used to describe the change, not a work-control relation or ordered instruction sequence.
* **Γ\_time:** straightforward interval; **Γ\_work:** integrates energy exchange; no “steps” required.

#### A.15.1:6.4 - Claim handling (episodes versus monitoring slices)

* **Top work occurrence:** `ClaimHandling_Case_8142_2026-06-03`.
* **`methodDescriptionRef`:** `Claims_Method_v7`.
* **Performer:** `U.RoleAssignment` with holder slot `ClaimsTeam_A`, role value `ClaimsHandlerRole`, bounded-context slot `InsuranceOps_2026`, and current-window slot covering the work occurrence.
* **Episode policy:** a customer callback interruption under one hour keeps the same parent work identity and creates two `EpisodeOf_work` fragments: `InitialReview_09:00-09:42` and `ResumedResolution_10:11-10:38`.
* **Temporal monitoring slice:** `MonitoringSlice_09:15-09:20` is `TemporalPartOf_work` for queue-latency evidence. It is not a new work occurrence and not an episode unless downstream reliance needs a named part with its own evidence, KPI, acceptance, repair, or aggregation role.
* **Method relation:** both episodes enact the same claim-handling method. The five-minute slice does not prove a submethod.

#### A.15.1:6.5 - Internal-combustion engine (cycle parts without human-only boundary language)

* **Top work occurrence:** `EngineRun_Cell7_2026-06-03T1300_1330`.
* **`methodDescriptionRef`:** `FourStrokeOperationSpec_v4`.
* **Performer:** `U.RoleAssignment` with holder slot `Engine_Cell7`, role value `EngineOperationRole`, bounded-context slot `TestBench_2026`, and current-window slot covering the run.
* **Episodes:** start, stop, mode-change, fuel/ignition policy, or diagnosis policy may bound `EpisodeOf_work` fragments. The definition uses boundary events and policy, not a human-attention metaphor.
* **Temporal parts:** crank-angle intervals or one-second telemetry windows are `TemporalPartOf_work` unless the context declares a named work part for resource, evidence, KPI, acceptance, repair, or aggregation use.
* **Method factors:** intake, compression, combustion-expansion, and exhaust are method factors only if recovered as `U.Method` submethods with method-level preconditions, effects, interfaces, and whole-method relation. Actual strokes are work parts or temporal parts of engine work, not submethods by label.

#### A.15.1:6.6 - Detector radio receiver (component behavior, method factor, work part)

* **Top work occurrence:** `ReceiverReception_Rx42_2026-06-03T2115_2120`.
* **`methodDescriptionRef`:** `EnvelopeDetectionMethod_v2`.
* **Performer:** `U.RoleAssignment` with holder slot `Receiver_Rx42`, role value `DetectorReceiverRole`, bounded-context slot `RadioLab_2026`, and current-window slot covering the reception occurrence.
* **Episodes:** a continuous reception interval between retune, on/off, interruption, or declared diagnostic mode events is `EpisodeOf_work` only under the receiver's episode policy.
* **Temporal parts:** a one-second reception slice is `TemporalPartOf_work` for signal-quality evidence or telemetry aggregation. It is not a new occurrence merely because it appears in a trace.
* **Method and mechanism split:** tuning, rectification, smoothing, and acoustic output may be recovered as method factors, system-component behaviors, mechanism material, evidence traces, or operational work parts depending on the current claim. A detector component or waveform segment does not become a submethod or a work part by label.

