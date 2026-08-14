---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:12"
section_title: "Archetypal Grounding - three worked micro-examples - E.10 across domains (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__014_archetypal-grounding-three-worked-micro-examples-e-10-across-domains-informative.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:12 — Archetypal Grounding - three worked micro-examples - E.10 across domains (informative)"
line_start: 75846
line_end: 75871
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

### E.10:12 - Archetypal Grounding - three worked micro-examples - E.10 across domains *(informative)*

#### E.10:12.1 - Healthcare (OR context)

**Messy:** “The surgical **process** is scheduled at 08:00; the SOP approves the incision and the **service** documents recovery.”
**E.10-clean rewrite:**
"`OR_Case_221_WorkPlan` is used as `U.WorkPlan` only after A.15.2 membership is established: its already identified present EntityOfConcern is `Patient_221`, its horizon is the bounded surgical-planning interval, and `Incision_221`, a `PlanItem` substantively coordinates the intended surgeon classification and assignment conditions, operating-room resource reservation, planned start of 08:00, `IncisionMethod`, the `U.Method`, and the incision-readiness target. It cites `IncisionMethodDescription`, a separately identified claim-bearing episteme. That episteme is `U.MethodDescription` only because the method is its exact EntityOfConcern and its claims substantively describe how the method is carried out. Any edition identity needed by the plan is selected through a separate `U.EpistemeRef` whose subject pattern supplies its rule; carrier version remains separate.
`SOP_OR_v4` is used as a specification-use episteme for the incision-readiness constraint; it does not approve the incision. Source title `QA_Officer` does not identify the performer. For `ApprovalSpeechActWork-221`, apply A.15.1 and F.6 to identify `QAApprovalSystem` as performer and the assignment under which it acted. Add `ApproverSystemRole` only when that classification matters. Approval speech-act content and the resulting `GateDecision` remain separate, and that decision admits the planned run.
`PostOpMonitoringPromiseContent` states the promised monitoring and its vitals acceptance envelope. `WardAccessMethod : U.Method` names the exact access method; `WardProtocol` is `U.MethodDescription` only if it is a separately identified claim-bearing episteme about that method and passes A.3.2, while its publication form and carrier remain separate."

#### E.10:12.2 - Manufacturing (assembly line)

**Messy:** “The welding **function** provides air‑tight seams; the **process** costs 3 min.”
**E.10-clean rewrite:**
“`Robot_SN789` has **Capability** ‘execute `Weld_MIG_v3` within envelope E at measures M’.
For one run, `Robot_SN789` is admitted as a system and performs `WeldWork-SN789-4711`; A.15.1 and F.6 identify its time, Method, containing System, and assignment. Add `WelderSystemRole` only when that classification matters. Each bounded change of the workpiece joint is identified under A.3.4 before stating a work-to-change fact. If the Work first constitutes a distinct seam entity, `A.15.PROD` supplies its identity specification and inception boundary. Measurement-result epistemes remain separate evidence for acceptance and duration claims.
Recover source `WeldingCellContext` separately. Any assignment interval is described outside the four participant designations.”

#### E.10:12.3 - Cloud and SRE (production Context)

**Messy:** “The storage **service** wrote logs and the deployment **process** failed after 2 min.”
**E.10-clean rewrite:**
“Source string `sCG‑Spec_ci_bot#DeployerRole:CD_v7` is a quoted recovery cue, not a performer or assignment. `sCGSpecCIBot` performs `DeployWork-r4711`; A.15.1 and F.6 identify its time, Method, containing System, and assignment. Use `DeployerSystemRole` only when that classification matters. The Work failed at T+120 s. Recover source `CD_v7` separately.
`ObjectStoragePromiseContent` states durability and availability targets; `S3_API_Spec_vX` describes the access method.
`LogWriterSystem` performs `LogWritingWork-r4711`; A.15.1 and F.6 identify its time, Method, containing System, and assignment. Use `TransformerSystemRole` only when that classification matters. The service promise remains separate and does not act.”

