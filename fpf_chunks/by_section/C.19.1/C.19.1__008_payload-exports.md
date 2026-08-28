---
chunk_kind: "child"
pattern_id: "C.19.1"
pattern_title: "Bitter‑Lesson Preference (BLP)"
section_id: "C.19.1:6"
section_title: "Payload - exports"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.1/C.19.1__008_payload-exports.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "C.19.1 — Bitter‑Lesson Preference (BLP)"
  - "C.19.1:6 — Payload - exports"
line_start: 49988
line_end: 49995
dependencies:
  - "A.0"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "B.1.6"
  - "B.3"
  - "C.16"
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

### C.19.1:6 - Payload - exports

`BLP.Policy@Context` is an editioned local policy row, not a universal kind. It records:

`<scopeBranch={empirical-computational | declared-local-analogy}, PreferenceDefault={neutral | declared-prefer-general}, alpha?, delta?, scaleProbeResult?, proportionateComparisonMethod?, fullScaleAuditRef?, WaiverRegister?, E-LOG policyIds?, G.11 telemetryPins?>`.

The row omits fields that are not current. `PreferenceDefault=declared-prefer-general` identifies a local tie-break policy, not an empirical conclusion. A full audit reference appears only after the risk-selected audit exists.

