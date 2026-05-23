---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph & Provenance Ledger"
section_id: "G.6:11"
section_title: "SoTA‑Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__013_sota-echoing.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "G.6 — Evidence Graph & Provenance Ledger"
  - "G.6:11 — SoTA‑Echoing"
line_start: 72029
line_end: 72037
dependencies:
  - "A.10"
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.18"
  - "E.5"
  - "E.5.2"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
  - "G.Core.TriggerAliasMap.G6"
keywords:
  - "CrossingBundle"
  - "EvidenceGraph"
  - "GateCrossing"
  - "PathId"
  - "PathSliceId"
  - "SCR/RSCR"
  - "TriggerAliasMap"
  - "UTS PathCard"
  - "lane tags (TA/VA/LA)"
  - "provenance"
  - "Γ-fold pinning"
---

### G.6:11 - SoTA‑Echoing

This pattern aligns with post‑2015 best practice in reproducibility and evaluation governance by:

* treating **provenance and versioning/pinning** as first‑class audit surfaces (rather than informal “methods” prose),
* enabling **selective re‑evaluation** (path‑scoped refresh) rather than global reruns whenever one policy/edition changes,
* separating **design‑time specifications** from **run‑time traces/telemetry**, matching modern reproducibility and “lineage” practice in complex ML/scientific pipelines,
* keeping **method‑family specifics** (e.g., archive/illumination/QD pins or open‑ended telemetry pins) modular via extension wiring instead of embedding them into the universal provenance core.

