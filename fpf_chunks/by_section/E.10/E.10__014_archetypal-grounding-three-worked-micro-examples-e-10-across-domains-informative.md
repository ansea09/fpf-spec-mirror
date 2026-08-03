---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:12"
section_title: "Archetypal Grounding - three worked micro-examples - E.10 across domains (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__014_archetypal-grounding-three-worked-micro-examples-e-10-across-domains-informative.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:12 — Archetypal Grounding - three worked micro-examples - E.10 across domains (informative)"
line_start: 75233
line_end: 75258
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.2"
  - "A.15.PROD"
  - "A.19.SPR"
  - "A.2"
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
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.17"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.5"
  - "F.18"
  - "F.19"
  - "F.5"
keywords:
---

### E.10:12 - Archetypal Grounding - three worked micro-examples - E.10 across domains *(informative)*

#### E.10:12.1 - Healthcare (OR context)

**Messy:** “The surgical **process** is scheduled at 08:00; the SOP approves the incision and the **service** documents recovery.”
**E.10-clean rewrite:**
"`OR_Case_221_WorkPlan` is used as `U.WorkPlan` only after A.15.2 membership is established: its already identified present EntityOfConcern is `Patient_221`, its horizon is the bounded surgical-planning interval, and `Incision_221 : PlanItem` substantively coordinates the intended surgeon-role condition, operating-room resource reservation, planned start of 08:00, `IncisionMethod : U.Method`, and the incision-readiness target. It cites `IncisionMethodDescription`, a separately identified claim-bearing episteme. That episteme is `U.MethodDescription` only because the method is its exact EntityOfConcern and its claims substantively describe how the method is carried out. Any exact edition needed by the plan is selected through a separate governed `U.EpistemeRef`; carrier version remains separate.
`SOP_OR_v4` is used as a specification-use episteme for the incision-readiness constraint; it does not approve the incision. Source title `QA_Officer` does not identify the performer. `ORApprovalAssignment_221 : U.RoleAssignment` obtains with `QAApprovalSystem : U.System` as holder, `ApproverRole`, `ORRoles-v4`, and `OR-RoleScheme-v4`; `ApprovalSpeechActWork_221 : U.Work` is one exact dated occurrence, and `QAApprovalSystem performed ApprovalSpeechActWork_221 under ORApprovalAssignment_221` through F.6. The approval speech-act content and resulting `GateDecision` are separately governed, and that decision admits the planned run.
`PostOpMonitoringPromiseContent` states the promised monitoring and its vitals acceptance envelope. `WardAccessMethod : U.Method` names the exact access method; `WardProtocol` is `U.MethodDescription` only if it is a separately identified claim-bearing episteme about that method and passes A.3.2, while its publication form and carrier remain separate."

#### E.10:12.2 - Manufacturing (assembly line)

**Messy:** “The welding **function** provides air‑tight seams; the **process** costs 3 min.”
**E.10-clean rewrite:**
“`Robot_SN789` has **Capability** ‘execute `Weld_MIG_v3` within envelope E at measures M’.
For one run, `WeldAssignment_SN789_4711 : U.RoleAssignment` obtains with `Robot_SN789 : U.System` as holder, `WelderRole`, `WeldingRoles-v3`, and `WeldingCell-Scheme-A`; `WeldWork_SN789_4711 : U.Work` is one exact dated occurrence, and `Robot_SN789 performed WeldWork_SN789_4711 under WeldAssignment_SN789_4711` through F.6. For any later run, identify its exact Work occurrence and the exact assignment obtaining over that occurrence before making the same attribution. Each such **Work** occurrence enacts `Weld_MIG_v3` and has the workpiece joint as its affected referent. Each actual bounded change of that joint must first be identified independently under `A.3.4` at the resolution and boundary required by the receiving use. Exact direct work-to-change facts may then relate the **Work** to those already identified transformations; neither the **Work**, method enactment, nor that relation supplies transformation identity, and none by itself establishes a new seam entity. If the receiving use claims that one distinct seam entity was first constituted, `A.15.PROD` must recover its exact identity-specification basis and inception boundary. Separate measurement-result epistemes record seam-characteristic and duration values: the acceptance evaluation compares the seam values with the bounds published in `Seal_Acceptance.md`, while duration measurements are used under their direct evidence relation for the three-minute-average claim.
Recover source `WeldingCellContext` separately. Any assignment interval is described outside the four participant designations.”

#### E.10:12.3 - Cloud and SRE (production Context)

**Messy:** “The storage **service** wrote logs and the deployment **process** failed after 2 min.”
**E.10-clean rewrite:**
“Source string `sCG‑Spec_ci_bot#DeployerRole:CD_v7` is a recovery cue, not a performer or assignment. `DeployAssignment_r4711 : U.RoleAssignment` obtains with `sCGSpecCIBot : U.System` as holder, `DeployerRole`, `CDRoles-v7`, and `CD-Scheme-v7`; `DeployWork_r4711 : U.Work` is one exact dated occurrence, and `sCGSpecCIBot performed DeployWork_r4711 under DeployAssignment_r4711` through F.6. That Work failed at T+120 s. Recover source `CD_v7` separately.
`ObjectStoragePromiseContent` states durability and availability targets; `S3_API_Spec_vX` describes the access method.
`LogWriterAssignment_r4711 : U.RoleAssignment` obtains with `LogWriterSystem : U.System` as holder, `TransformerRole`, `LoggingRoles-v2`, and `Logging-Scheme-A`; recover source `LoggingContext` separately. `LogWritingWork_r4711 : U.Work` is one exact dated occurrence, and `LogWriterSystem performed LogWritingWork_r4711 under LogWriterAssignment_r4711` through F.6, while the service promise did not act.”

