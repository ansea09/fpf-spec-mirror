---
chunk_kind: "child"
pattern_id: "A.19.UNM"
pattern_title: "Normalize Coordinate Values under Declared Invariants"
section_id: "A.19.UNM:6"
section_title: "Bias‑Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.UNM/A.19.UNM__008_bias-annotation.md"
commit_sha: "5e9f4d868afa1f9db90d4c7ff6840bd55f3b8d18"
heading_path:
  - "A.19.UNM — Normalize Coordinate Values under Declared Invariants"
  - "A.19.UNM:6 — Bias‑Annotation"
line_start: 39310
line_end: 39319
dependencies:
keywords:
  - "CV→NCV"
  - "NormalizationFixSpec"
  - "NormalizationInvariant[*]"
  - "NormalizationMethodId"
  - "NormalizationMethodInstanceId"
  - "fail-closed tri-state guard (pass\\"
  - "normalization"
  - "validity window (no implicit “latest”)"
  - "≡_UNM"
---

### A.19.UNM:6 - Bias‑Annotation

Common cognitive traps around normalization:
- **Normalization-as-truth bias:** treating an NCV as a justified answer before checking its input basis, transformation and receiving-use conditions.
- **Hidden-steps bias:** assuming normalization “happened somewhere” and skipping routing/pins.
- **Unit-blindness:** treating numeric sameness as semantic sameness.
- **Proxy legitimacy:** assuming a popular method is legitimate without evidence pins or validity region.

Mitigation: enforce `NormalizationMethodInstance` + validity window + evidence pins; and distinguish the directed output, optional classes and any separately justified operation or query on them.

