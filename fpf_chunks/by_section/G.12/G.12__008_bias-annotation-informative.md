---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
section_id: "G.12:7"
section_title: "Bias‑Annotation (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__008_bias-annotation-informative.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "G.12 — DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
  - "G.12:7 — Bias‑Annotation (informative)"
line_start: 81922
line_end: 81928
dependencies:
  - "A.19"
  - "C.18"
  - "C.19"
  - "C.21"
  - "E.10"
  - "E.5.2"
  - "F.17"
  - "F.18"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.Core"
keywords:
  - "DHC"
  - "PathId/PathSliceId"
  - "RSCR/refresh wiring"
  - "UTS twins"
  - "admissible telemetry"
  - "dashboard"
  - "discipline health"
  - "edition pins"
  - "time-series"
  - "view-only slices"
---

### G.12:7 — Bias‑Annotation (informative)

* **Didactic:** dashboard publication units publish pins and paths first; views second.
* **Architectural:** no “dashboard‑local governing spec refs”; invariant citation is via `G.Core`.
* **Pragmatic:** slice‑scoped refresh is enabled by canonical trigger ids + payload pins.
* **Epistemic:** compare‑only ordinals and explicit provenance prevent “trend‑as‑drift”.

