---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:9"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__011_bias-annotation.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:9 — Bias-Annotation"
line_start: 47409
line_end: 47418
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "C.11"
  - "C.16.P"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "G.11"
  - "G.4"
  - "G.6"
keywords:
  - "C.2.1 result episteme"
  - "Characteristic"
  - "Level/Coordinate"
  - "Scale"
  - "Unit"
  - "actual bindings"
  - "bounded later use"
  - "calibration"
  - "comparability"
  - "dated measurement work"
  - "input/output quantities"
  - "measurand"
  - "measurement result"
  - "measurement subject"
  - "method"
  - "model"
  - "polarity"
  - "provenance"
  - "uncertainty"
---

### C.16:9 - Bias-Annotation

| Bias | Symptom | Correction |
| --- | --- | --- |
| Number-as-fact | A displayed value lacks measurand, Characteristic, Scale, model, calibration, uncertainty, or time stance. | Rebuild the complete C.16 chain. |
| Instrument realism | Raw output or indication is asserted as the actual subject state. | Separate output, indication, attributed result, and subject state. |
| Uncertainty laundering | A point estimate is carried forward while model and calibration uncertainty disappear. | Recover input uncertainties, correlations, propagation, and interpretation. |
| Dashboard authority | A tile or score is reused as diagnosis, assurance, acceptance, or decision authority. | Route the later use to the exact patterns for its Work, result, provenance, currentness, and reliance claims. |
| Common-scale pressure | Distinct scales are normalized merely because comparison is desired. | Require an exact transformation and receiving comparison pattern; otherwise preserve incomparability. |

