---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF (LEX‑BUNDLE)"
section_id: "E.10:14"
section_title: "Three worked micro‑examples — ULR across domains (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__018_three-worked-micro-examples-ulr-across-domains-informative.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF (LEX‑BUNDLE)"
  - "E.10:14 — Three worked micro‑examples — ULR across domains (informative)"
line_start: 60097
line_end: 60122
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.ECS"
  - "A.2"
  - "A.6.P"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.P"
  - "E.22"
  - "E.23"
  - "E.5"
  - "F.18"
  - "F.19"
  - "F.5"
  - "U.Types"
keywords:
---

### E.10:14 - Three worked micro‑examples — ULR across domains *(informative)*

#### E.10:14.1 - Healthcare (OR context)

**Messy:** “The surgical **process** is scheduled at 08:00; the SOP approves the incision and the **service** documents recovery.”
**ULR rewrite:**
“**WorkPlan** OR‑Case‑221 starts 08:00 and will execute **MethodDescription** `Incision_v4`.
`SOP_OR_v4` holds **RequirementRole**; a **SpeechAct Work** by `QA_Officer#ApproverRole` authorises the run.
The hospital offers **Service** ‘Post‑op monitoring’ (access = ward protocol; acceptance = vitals envelope).”

#### E.10:14.2 - Manufacturing (assembly line)

**Messy:** “The welding **function** provides air‑tight seams; the **process** costs 3 min.”
**ULR rewrite:**
“`Robot_SN789` has **Capability** ‘execute `Weld_MIG_v3` within envelope E at measures M’.
**Work** instances that **fulfil Service** ‘Provide seam S’ average 3 min; **acceptance** bounds are in `Seal_Acceptance.md`.
The **MethodDescription** is `Weld_MIG_v3`; the **Role** is `WelderRole`.”

#### E.10:14.3 - Cloud/SRE (production Context)

**Messy:** “The storage **service** wrote logs and the deployment **process** failed after 2 min.”
**ULR rewrite:**
“`sCG‑Spec_ci_bot#DeployerRole:CD_v7` performed **Work** ‘Deploy r4711’ (failed at T+120 s).
The platform offers **Service** ‘Object Storage’ (access = `S3_API_Spec_vX`; **acceptance** = durability/availability targets).
`LogWriter` is a **System** bearing `TransformerRole` that wrote the records; *the service did not act*.”

