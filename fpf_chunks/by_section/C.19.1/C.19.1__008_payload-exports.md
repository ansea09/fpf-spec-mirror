---
chunk_kind: "child"
pattern_id: "C.19.1"
pattern_title: "Bitter‑Lesson Preference (BLP)"
section_id: "C.19.1:6"
section_title: "Payload — exports"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.1/C.19.1__008_payload-exports.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "C.19.1 — Bitter‑Lesson Preference (BLP)"
  - "C.19.1:6 — Payload — exports"
line_start: 45891
line_end: 45898
dependencies:
  - "A.0"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.5"
  - "E.23"
  - "E.3"
  - "E.5"
  - "F.7"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "BLP‑waiver"
  - "Scale‑Audit"
  - "alpha and delta tolerances"
  - "general-solution preference"
  - "iso‑scale parity"
  - "scale‑amenability"
  - "slope vector"
---

### C.19.1:6 - Payload — exports

`BLP.Policy@Context` (UTS row; editioned):
`<PreferenceDefault, alpha and delta tolerances plus CI, Scale-Audit recipe (G.9 link; DoE), WaiverRegister{reason, responsibleRoleRef, expiry}, E-LOG lens policy-ids, ATC.PolicyRef? (agentic), G.11.TelemetryPins>`.

**UTS row template (conceptual; pencil‑ready).**
`BLP.Policy@Context := PreferenceDefault=(prefer-general or neutral), tolerances=(alpha=..., delta=..., CI=...), Scale-Audit=(parity=G.9; sweep=S={...}; DoE=factorial or LHD; kneeTest=policy-tau), WaiverRegister=[{reason=..., responsibleRoleRef=..., expiry=...}], E-LOG=(policyIds=...), ATC.PolicyRef=(...), TelemetryPins=(edition=..., seeds=..., comparatorSet=...)`.

