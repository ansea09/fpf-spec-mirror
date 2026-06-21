---
chunk_kind: "child"
pattern_id: "C.18.1"
pattern_title: "Scaling‑Law Lens Binding (SLL)"
section_id: "C.18.1:12.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18.1/C.18.1__014_sota-echoing.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "C.18.1 — Scaling‑Law Lens Binding (SLL)"
  - "C.18.1:12.1 — SoTA-Echoing"
line_start: 44944
line_end: 44949
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

### C.18.1:12.1 - SoTA-Echoing

Current scaling-law practice in machine learning, quality-diversity, optimization, planning, and resource-aware experimentation treats scale behavior as windowed and regime-dependent rather than as one universal “scales well” label. C.18.1 adapts that line into FPF by requiring scale variables, windows, probe points, uncertainty, and elasticity classes before scale claims are reused.

The pattern also keeps SoTA scaling practice from overriding FPF ontology. Scaling-law fits, knee detectors, segmented regressions, and experimental-design methods are mathematical or methodological support for the scale claim; they do not replace `C.16` measurement construction, `G.9` parity, selector policy, or `C.29` mathematical-lens admissibility.

