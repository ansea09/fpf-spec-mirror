---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Normalize Coordinate Values under Declared Invariants (UNM)"
section_id: "A.19.UNM:6"
section_title: "Bias‑Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__008_bias-annotation.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.19.UNM — Normalize Coordinate Values under Declared Invariants (UNM)"
  - "A.19.UNM:6 — Bias‑Annotation"
line_start: 34991
line_end: 35000
dependencies:
keywords:
  - "CV→NCV"
  - "NormalizationFixSpec"
  - "NormalizationInvariant[*]"
  - "NormalizationMethodId"
  - "NormalizationMethodInstanceId"
  - "fail-closed tri-state guard (pass"
  - "normalization"
  - "validity window (no implicit “latest”)"
  - "≡_UNM"
---

### A.19.UNM:6 - Bias‑Annotation

Common cognitive traps around normalization:
- **Normalization-as-truth bias:** treating NCVs as “objective” instead of “objective under declared invariants and validity window”.
- **Hidden-steps bias:** assuming normalization “happened somewhere” and skipping explicit routing/pins.
- **Unit-blindness:** treating numeric sameness as semantic sameness.
- **Proxy legitimacy:** assuming a popular method is legitimate without evidence pins or validity region.

Mitigation: enforce explicit `NormalizationMethodInstance` + validity window + evidence pins; and distinguish the directed output, optional classes and any separately justified operation or query on them.

