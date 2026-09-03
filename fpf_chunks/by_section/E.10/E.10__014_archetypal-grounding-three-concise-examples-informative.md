---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:12"
section_title: "Archetypal grounding: three concise examples (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__014_archetypal-grounding-three-concise-examples-informative.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:12 — Archetypal grounding: three concise examples (informative)"
line_start: 76269
line_end: 76304
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.2"
  - "A.15.PROD"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.3.2"
  - "A.6.0"
  - "A.6.5"
  - "A.6.6"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.10.DEV"
  - "E.10.LRN"
  - "E.10.MOVE"
  - "E.10.ROLE"
  - "E.17"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.5"
  - "F.17"
  - "F.18"
  - "F.19"
  - "F.5"
  - "F.6"
  - "F.9"
  - "U.SystemRoleAssignment"
keywords:
---

### E.10:12 - Archetypal grounding: three concise examples *(informative)*

These examples show the repaired claim first. Open the exact Work, attribution, publication, or naming apparatus only where the receiving use needs it.

#### E.10:12.1 - Healthcare (operating-room planning and work)

**Messy:** “The surgical **process** is scheduled at 08:00; the SOP approves the incision and the **service** documents recovery.”

**Repair, taking `service` here to mean the ward team:** “Schedule `Incision_221` in `OR_Case_221_WorkPlan` for 08:00, using `IncisionMethod`. `SOP_OR_v4` states the incision-readiness constraint. `QAApprovalSystem` performs the approval; record its speech-act content and the resulting `GateDecision` separately; that decision admits the planned run. The ward team records `Patient_221`'s recovery in `RecoveryRecord_221`.”

**Formal plan membership.** `OR_Case_221_WorkPlan` is used as `U.WorkPlan` only after A.15.2 membership is established: its already identified present EntityOfConcern is `Patient_221`, its horizon is the bounded surgical-planning interval, and `Incision_221`, a `PlanItem` substantively coordinates the intended surgeon classification and assignment conditions, operating-room resource reservation, planned start of 08:00, `IncisionMethod`, the `U.Method`, and the incision-readiness target. It cites `IncisionMethodDescription`, a separately identified claim-bearing episteme. That episteme is `U.MethodDescription` only because the method is its exact EntityOfConcern and its claims substantively describe how the method is carried out. Any edition identity needed by the plan is selected through a separate `U.EpistemeRef` whose subject pattern supplies its rule; carrier version remains separate.

**Actual approval Work.** For `ApprovalSpeechActWork-221`, recover `QAApprovalSystem` as exact actual performer through A.13 and let A.15.1 independently admit the dated Work. Add F.6 only when this account or its receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; F.6 identifies neither assignment nor performer, and missing or failed F.6 leaves the Work intact. Add `ApproverSystemRole` only when that classification matters.

**Separate source claims.** If the source also specifies a monitoring promise or an access method, recover those additional claims separately: `PostOpMonitoringPromiseContent` states the promised monitoring and its vitals acceptance envelope. `WardAccessMethod : U.Method` names the exact access method; `WardProtocol` is `U.MethodDescription` only if it is a separately identified claim-bearing episteme about that method and passes A.3.2, while its publication form and carrier remain separate. These are additional claims, not replacements for recording recovery.

#### E.10:12.2 - Manufacturing (assembly line)

**Messy:** “The welding **function** provides air-tight seams; the **process** costs 3 min.”

**Repair:** “`Robot_SN789` can execute `Weld_MIG_v3` within envelope E at measures M. The run `WeldWork-SN789-4711` lasts three minutes and changes the workpiece joint. Use the recorded measurements to check the duration and the seam's air-tightness acceptance criterion.”

For one run, recover `Robot_SN789` as exact actual performer through A.13 and let A.15.1 independently admit `WeldWork-SN789-4711` from its performer, time, Method, and containing-System facts. Add F.6 only when this account or its receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; F.6 identifies neither assignment nor performer, and missing or failed F.6 leaves the Work intact. Add `WelderSystemRole` only when that classification matters. Each bounded change of the workpiece joint is identified under A.3.4 before stating a work-to-change fact. If the Work first constitutes a distinct seam entity, `A.15.PROD` supplies its identity specification and inception boundary. Measurement-result epistemes remain separate evidence for acceptance and duration claims.

Treat source string `WeldingCellContext` as a quoted recovery cue. If it changes the claim, recover the exact source edition, plant practice, effective scheme, scope, or working situation that it denotes. Any assignment interval is described outside the four participant designations.

#### E.10:12.3 - Cloud and SRE

**Messy:** “The storage **service** wrote logs and the deployment **process** failed after 2 min.”

**Repair:** “`sCGSpecCIBot` performed `DeployWork-r4711`, which failed after 120 seconds. `LogWriterSystem` performed `LogWritingWork-r4711`.”

Admit each Work occurrence through A.13 and A.15.1; add F.6 only for a current assignment-bound attribution. Treat `sCG-Spec_ci_bot#DeployerRole:CD_v7` as a source expression and recover `CD_v7` separately. Use `DeployerSystemRole` or `TransformerSystemRole` only when the classification changes the claim.

**Separate source claims.** If the source also specifies durability and availability targets as a storage promise, recover them in `ObjectStoragePromiseContent`. If it supplies an access-method description, identify that separate episteme as `S3_API_Spec_vX` and preserve the method it describes.

