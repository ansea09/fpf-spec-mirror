---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:14"
section_title: "Three worked micro-examples — E.10 across domains (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__018_three-worked-micro-examples-e-10-across-domains-informative.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:14 — Three worked micro-examples — E.10 across domains (informative)"
line_start: 61306
line_end: 61331
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.SPR"
  - "A.2"
  - "A.6.P"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.P"
  - "E.10.ARCH"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.5"
  - "F.18"
  - "F.19"
  - "F.5"
  - "U.Types"
keywords:
---

### E.10:14 - Three worked micro-examples — E.10 across domains *(informative)*

#### E.10:14.1 - Healthcare (OR context)

**Messy:** “The surgical **process** is scheduled at 08:00; the SOP approves the incision and the **service** documents recovery.”
**E.10-clean rewrite:**
“**WorkPlan** OR‑Case‑221 starts 08:00 and will execute **MethodDescription** `Incision_v4`.
`SOP_OR_v4` is used as a specification-use episteme for the applicable requirement or gate relation; a **SpeechAct Work** by `QA_Officer#ApproverRole` authorises the run.
The hospital records a post-op monitoring service promise (access = ward protocol; acceptance = vitals envelope).”

#### E.10:14.2 - Manufacturing (assembly line)

**Messy:** “The welding **function** provides air‑tight seams; the **process** costs 3 min.”
**E.10-clean rewrite:**
“`Robot_SN789` has **Capability** ‘execute `Weld_MIG_v3` within envelope E at measures M’.
**Work** instances that satisfy the promise content ‘Provide seam S’ average 3 min; **acceptance** bounds are in `Seal_Acceptance.md`.
The **MethodDescription** is `Weld_MIG_v3`; the **Role** is `WelderRole`.”

#### E.10:14.3 - Cloud and SRE (production Context)

**Messy:** “The storage **service** wrote logs and the deployment **process** failed after 2 min.”
**E.10-clean rewrite:**
“`sCG‑Spec_ci_bot#DeployerRole:CD_v7` performed **Work** ‘Deploy r4711’ (failed at T+120 s).
The platform records an object-storage service promise (access = `S3_API_Spec_vX`; **acceptance** = durability and availability targets).
`U.RoleAssignment(holderRef=LogWriter, roleRef=TransformerRole@Context, boundedContextRef=LoggingContext)` records the work-facing assignment for the system that wrote the records; *the service promise did not act*.”

