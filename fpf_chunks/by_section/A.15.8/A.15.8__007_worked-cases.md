---
chunk_kind: "child"
pattern_id: "A.15.8"
pattern_title: "Work-Performance Configuration and Recovery Testing"
section_id: "A.15.8:6"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.8/A.15.8__007_worked-cases.md"
commit_sha: "4260875dd8bc4595bbca3b6dbfa61e6f35afa013"
heading_path:
  - "A.15.8 — Work-Performance Configuration and Recovery Testing"
  - "A.15.8:6 — Worked cases"
line_start: 31845
line_end: 31876
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.15.2"
  - "A.15.4"
  - "A.15.5"
  - "A.15.7"
  - "A.15.8"
  - "A.2.1"
  - "A.2.2"
  - "A.2.4"
  - "A.22"
  - "A.6.RCD"
  - "A.6.REL"
  - "C.11"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.27.TA"
  - "C.30"
  - "E.23.CAE"
  - "E.23.CDI"
  - "F.6"
keywords:
---

### A.15.8:6 - Worked cases

#### A.15.8:6.1 - Literature qualification across a researcher, services, and files

**Situation.** In this constructed case, `LiteratureQualificationWork-2026-08-27-AM` runs from 09:00 to 11:00 UTC on 27 August 2026 within the admitted containing System `ResearchService-3`, enacting the admitted `LiteratureQualificationMethod-2`. The independently identified performer System `Researcher-17` satisfies the local `LiteratureQualifierRole` criterion by controlling source selection and claim qualification. The directly declared `ResearchAssignment` species assigns `LiteratureQualifierRole` to a System when its question designation and authorized source access obtain. Those stipulated facts establish `RA-Researcher17-Question6` throughout this interval and complete the A.13 core. This constructed case stipulates the full A.15.1:4.1 admission basis, including that core, the independent performance history, A.1:4.2 construction, and a declared containing-System relation covering the complete occurrence. Because this account also compares accountability, F.6 then checks attribution through that same assignment. A search service, language-model service, repository, pinned papers, claim sheet, and unresolved-question note support the Work; none becomes a performer or constituent of a new whole merely by appearing in the configuration. A reviewer may continue later.

**Probe.** The fresh-session and reviewer-handoff probe removes the original model session and asks the reviewer to recover the bounded question, exact source editions, accepted and rejected claim reasons, open uncertainty, and next probe.

**Observation and result.** The reviewer can recover the papers but cannot distinguish why one claim was rejected because the claim sheet lacks a decision reason and one citation lacks an edition pin. The result focuses on the exact Work occurrence, identifies the missing source and record relations, and returns two repairs to their representation and source owners. Do not rely on the unrecovered qualification; retain independently supported claims.

**What changed.** Recover the missing source edition and decision reason for that qualification, or retain the bounded stop.

#### A.15.8:6.2 - Non-human distributed computation after worker loss

**Situation.** In this constructed case, `SettlementComputationWork-2026-08-27-Run42` runs from 08:00 to 12:00 UTC on 27 August 2026 within the admitted containing System `SettlementService-2`, enacting `SettlementMethod-5`. Its independently identified performer Systems `Worker-1` and `Worker-2` satisfy the local `SettlementExecutorRole` criterion through observed message processing and settlement-effect control. The directly declared `SettlementExecutionAssignment` species assigns that kind when registration for Run42 and connection to its queue obtain. Those stipulated facts establish `RA-Worker1-Run42` and `RA-Worker2-Run42` throughout the Work window. The full A.15.1:4.1 admission basis is stipulated, including A.1:4.2 construction and a declared containing-System relation covering the complete occurrence. The performance history establishes the Method enactment. No assignment-bound attribution is required for these workers. They exchange messages and use an object store, configuration values, intermediate results, completed-effect records, and provenance records. Another worker must continue without duplicating an irreversible settlement effect.

**Probe.** The independently identified `RecoveryTestController-Run42 : U.System` satisfies the local `RecoveryProbeControllerRole` criterion by controlling worker removal and observing recovery. `WorkerLossRecoveryProbeWork-Run42-P1 : U.Work` runs from 09:15 to 09:20 UTC on the same date within `SettlementService-2`. The full A.15.1:4.1 admission basis is stipulated, including A.1:4.2 construction and a declared containing-System relation covering the complete occurrence. Its history establishes that it enacts the admitted `WorkerLossRecoveryTestMethod-1`. The directly declared `RecoveryControllerAssignment` species assigns `RecoveryProbeControllerRole` when probe designation and connection to the control interface obtain. Those stipulated facts establish `RA-Controller42-P1` for that interval and complete the A.13 core. The comparison also uses which assignment covered the probe, so F.6 checks attribution through this same assignment. The probe removes one worker after a message has been emitted but before its local completion record is available, then attempts recovery from the selected state mechanism.

**Observation and result.** Process state is recoverable, but channel state and the completed-effect provenance relation are not mutually consistent. The branch-specific account names those state bearers and update/use relations and returns the missing idempotency or provenance condition. A Chandy-Lamport snapshot, event sourcing, transaction protocol, or another computing Method may be selected as the reusable way for the repair. If the receiving account needs a distinct repair Work, admit its performer and occurrence through A.13 and A.15.1 and ground its Method enactment. An ordinary repair need not acquire a separate occurrence identity.

**What changed.** Add or repair the exact checkpoint, provenance, or idempotency condition.

#### A.15.8:6.3 - Equipped performer in a present WorkPlan

**Situation.** `ConcertPerformancePlan-2026-09-12` is one exact present `U.WorkPlan`. Its declaration-local content names a musician and a robotic prosthesis controller as intended performers for a proposed performance after device replacement. It also names an instrument, cue source, power support, control link, and allowed latency. None of this content is a future Work occurrence or obtaining assignment.

**Probe.** The current plan proposes a rehearsal under changed latency and a degraded visual-cue condition. Its material, timing, control, threshold, and stop rules are taken from the applicable music-performance, robotics, human-factors, and safety Methods. If the account identifies a dated rehearsal Work, first recover each actual performer through A.13 and admit that Work independently under `A.15.1`.

**Observation and result.** Current evidence leaves recovery after cue loss within the required timing window unresolved. The WorkPlan-focused account names the intended performers, support and control relations, return condition, uncertainty, and the planned probe. Obtain the needed recovery evidence through the planned rehearsal or another sufficient source, or stop the dependent use. Change the cue/control relation or narrow the proposed use when the result requires it. Capability claims for the musician, device, or any independently admitted whole stay separate.

**What changed.** Resolve the recovery question before relying on a dependent entry-readiness claim. Make any needed configuration repair under the applicable domain conditions.

