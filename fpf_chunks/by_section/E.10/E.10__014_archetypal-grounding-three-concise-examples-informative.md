---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:12"
section_title: "Archetypal grounding: three concise examples (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__014_archetypal-grounding-three-concise-examples-informative.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:12 — Archetypal grounding: three concise examples (informative)"
line_start: 75932
line_end: 75959
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

#### E.10:12.1 - Healthcare

**Messy:** “The surgical **process** is scheduled at 08:00; the SOP approves the incision and the **service** documents recovery.”

**Repair:** “Schedule `Incision_221` in `OR_Case_221_WorkPlan` for 08:00, using `IncisionMethod`. `SOP_OR_v4` states the incision-readiness constraint. `QAApprovalSystem` performs the approval; record its speech-act content and the resulting `GateDecision` separately. `PostOpMonitoringPromiseContent` states the promised monitoring and acceptance envelope.”

Use the plan as `U.WorkPlan` only when A.15.2 admits it. If precise approval Work or assignment-bound attribution matters, apply A.13 and A.15.1 first and F.6 only for that attribution. Use `WardProtocol` as `U.MethodDescription` only when A.3.2 admits it as a claim-bearing episteme about `WardAccessMethod`.

#### E.10:12.2 - Manufacturing

**Messy:** “The welding **function** provides air-tight seams; the **process** costs 3 min.”

**Repair:** “`Robot_SN789` can execute `Weld_MIG_v3` within envelope E. The run `WeldWork-SN789-4711` lasts three minutes; measurement-result epistemes provide the evidence used to accept the seam.”

Admit the run through A.13 and A.15.1. Apply F.6 only if precise assignment-bound attribution is part of the claim. If the Work first constitutes a distinct seam, use `A.15.PROD` for its inception boundary. If `WeldingCellContext` changes interpretation, name the source, scheme, scope, or working situation it denotes.

#### E.10:12.3 - Cloud and SRE

**Messy:** “The storage **service** wrote logs and the deployment **process** failed after 2 min.”

**Repair:** “`sCGSpecCIBot` performed `DeployWork-r4711`, which failed after 120 seconds. `LogWriterSystem` performed `LogWritingWork-r4711`. `ObjectStoragePromiseContent` states the durability and availability targets; `S3_API_Spec_vX` describes the access method.”

Admit each Work occurrence through A.13 and A.15.1; add F.6 only for a current assignment-bound attribution. Treat `sCG-Spec_ci_bot#DeployerRole:CD_v7` as a source expression and recover `CD_v7` separately. Use `DeployerSystemRole` or `TransformerSystemRole` only when the classification changes the claim.

