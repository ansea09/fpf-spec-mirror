---
chunk_kind: "child"
pattern_id: "C.18.1"
pattern_title: "Scaling‑Law Lens Binding (SLL)"
section_id: "C.18.1:6"
section_title: "Conformance Checklist (CC-SLL)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18.1/C.18.1__009_conformance-checklist-cc-sll.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "C.18.1 — Scaling‑Law Lens Binding (SLL)"
  - "C.18.1:6 — Conformance Checklist (CC-SLL)"
line_start: 64255
line_end: 64262
dependencies:
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "G.10"
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
  - "elasticity class"
  - "iso‑scale parity"
  - "knee"
  - "knee detection"
  - "probe uncertainty"
  - "resolution‑elasticity"
  - "scale variables (S)"
  - "scale‑probe"
  - "scaling law"
  - "segmented regression"
---

### C.18.1:6 - Conformance Checklist (CC-SLL)

1. `S` declared **or** `S = N/A` with rationale.
2. For an empirical scale comparison, give the probe settings, response, task family, invariants and applicable uncertainty. Name the supported class or the remaining uncertainty. With observations at only one setting, report what is established there and leave the scale comparison open.
3. A matched-scale claim has established iso-scale parity, with the editions, seeds when used, and comparator recoverable. If the resource regimes cannot be matched, report the individual results or a narrower comparison whose grounds hold. Any numerical assurance penalty has a basis in the receiving B.3 model.
4. An illumination tie-break cites the policy admitting it and its **lens id** in **E/E-LOG** provenance. When that policy depends on **χ**, include the supported class or leave the dependent preference open.
5. Knee claims cite the **policy threshold**, slope-comparison method and applicable uncertainty or error basis; include the statistical significance level and any CI level when those are used.

