---
chunk_kind: "child"
pattern_id: "C.19.1"
pattern_title: "Bitter‑Lesson Preference (BLP)"
section_id: "C.19.1:6"
section_title: "Payload — exports"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.1/C.19.1__007_payload-exports.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "C.19.1 — Bitter‑Lesson Preference (BLP)"
  - "C.19.1:6 — Payload — exports"
line_start: 40991
line_end: 40998
dependencies:
  - "A.0"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.5"
  - "E.3"
  - "E.5"
  - "F.7"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "BLP-waiver"
  - "BLP‑waiver"
  - "Bitter Lesson"
  - "Scale‑Audit"
  - "general‑method preference"
  - "iso‑scale parity"
  - "scale-audit"
  - "scale‑amenability"
  - "slope vector"
  - "task-family specialization"
  - "α/δ tolerances"
---

### C.19.1:6 - Payload — exports

`BLP.Policy@Context` (UTS row; editioned):
`⟨PreferenceDefault, α/δ tolerances + CI, Scale‑Audit recipe (G.9 link; DoE), WaiverRegister{reason, responsibleRoleRef, expiry}, E/E‑LOG lens policy‑ids, ATC.PolicyRef? (agentic), G.11.TelemetryPins⟩`.

**UTS row template (conceptual; pencil‑ready).**
`BLP.Policy@Context := PreferenceDefault=(prefer‑general|neutral), α/δ=(α=…, δ=…, CI=…), Scale‑Audit=(parity=G.9; sweep=S={…}; DoE=factorial|LHD; kneeTest=policy‑τ), WaiverRegister=[{reason=…, responsibleRoleRef=…, expiry=…}], E/E‑LOG=(policyIds=…), ATC.PolicyRef=(…), TelemetryPins=(edition=…, seeds=…, comparatorSet=…)`.

