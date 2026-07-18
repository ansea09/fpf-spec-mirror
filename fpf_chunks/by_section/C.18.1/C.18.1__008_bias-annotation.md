---
chunk_kind: "child"
pattern_id: "C.18.1"
pattern_title: "Scaling‑Law Lens Binding (SLL)"
section_id: "C.18.1:7"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18.1/C.18.1__008_bias-annotation.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "C.18.1 — Scaling‑Law Lens Binding (SLL)"
  - "C.18.1:7 — Bias-Annotation"
line_start: 46853
line_end: 46860
dependencies:
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.5"
  - "G.10"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "DoE (design‑of‑experiments)"
  - "Scale Variables (S)"
  - "ScaleWindow"
  - "UNM/NormalizationMethod‑based mapping"
  - "compute‑elasticity"
  - "data‑elasticity"
  - "diminishing returns"
  - "exponent class"
  - "iso‑scale parity"
  - "knee"
  - "knee detection"
  - "resolution‑elasticity"
  - "scale variables (S)"
  - "scale‑probe"
  - "scaling law"
  - "segmented regression"
---

### C.18.1:7 - Bias-Annotation

| Bias | Symptom | Correction |
| --- | --- | --- |
| Bigger-is-better bias | More compute, data, capacity, or freedom of action is treated as automatic improvement. | Declare `S`, ScaleWindow, and elasticity class before using the scale claim. |
| Telemetry-as-objective bias | Coverage or illumination is promoted into dominance by default. | Keep telemetry report-only unless the selector policy explicitly admits it. |
| Knee-by-story bias | A plateau or knee is asserted from one anecdote or one late observation. | Require scale-probe points, replicates or uncertainty, and a cited threshold policy. |

