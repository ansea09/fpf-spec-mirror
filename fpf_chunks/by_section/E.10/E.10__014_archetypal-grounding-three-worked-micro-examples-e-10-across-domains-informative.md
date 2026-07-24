---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:12"
section_title: "Archetypal Grounding - three worked micro-examples - E.10 across domains (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__014_archetypal-grounding-three-worked-micro-examples-e-10-across-domains-informative.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:12 — Archetypal Grounding - three worked micro-examples - E.10 across domains (informative)"
line_start: 73502
line_end: 73527
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.PROD"
  - "A.19.SPR"
  - "A.2"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6.0"
  - "A.6.5"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
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
“**WorkPlan** OR‑Case‑221 states a planned start of 08:00 and selects the method described by **MethodDescription** `Incision_v4`.
`SOP_OR_v4` is used as a specification-use episteme for the incision-readiness constraint; it does not approve the incision. `QA_Officer`, assigned `ApproverRole`, performs approval **SpeechAct Work**, and the resulting **GateDecision** admits the planned run.
`PostOpMonitoringPromiseContent` states the promised monitoring and its vitals acceptance envelope; `WardProtocol` describes the access method.”

#### E.10:12.2 - Manufacturing (assembly line)

**Messy:** “The welding **function** provides air‑tight seams; the **process** costs 3 min.”
**E.10-clean rewrite:**
“`Robot_SN789` has **Capability** ‘execute `Weld_MIG_v3` within envelope E at measures M’.
Each exact **Work** occurrence enacts that method and has the workpiece joint as its affected referent. Each actual bounded change of that joint must first be identified independently under `A.3.4` at the resolution and boundary required by the receiving use. Exact direct work-to-change facts may then relate the **Work** to those already identified transformations; neither the **Work**, method enactment, nor that relation supplies transformation identity, and none by itself establishes a new seam entity. If the receiving use claims that one distinct seam entity was first constituted, `A.15.PROD` must recover its exact identity-specification basis and inception boundary. Separate measurement-result epistemes record seam-characteristic and duration values: the acceptance evaluation compares the seam values with the bounds published in `Seal_Acceptance.md`, while duration measurements are used under their direct evidence relation for the three-minute-average claim.
`U.RoleAssignment(holderRef=Robot_SN789, roleRef=WelderRole, boundedContextRef=WeldingCellContext)` assigns the robot to the work-facing role.”

#### E.10:12.3 - Cloud and SRE (production Context)

**Messy:** “The storage **service** wrote logs and the deployment **process** failed after 2 min.”
**E.10-clean rewrite:**
“`sCG‑Spec_ci_bot#DeployerRole:CD_v7` performed **Work** ‘Deploy r4711’ (failed at T+120 s).
`ObjectStoragePromiseContent` states durability and availability targets; `S3_API_Spec_vX` describes the access method.
`U.RoleAssignment(holderRef=LogWriter, roleRef=TransformerRole@Context, boundedContextRef=LoggingContext)` assigns the log-writing system to the work-facing role; that system performed the log-writing Work, while the service promise did not act.”

