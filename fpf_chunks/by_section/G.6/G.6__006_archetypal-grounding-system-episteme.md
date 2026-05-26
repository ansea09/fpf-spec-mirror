---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph & Provenance Ledger"
section_id: "G.6:5"
section_title: "Archetypal Grounding (System / Episteme)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__006_archetypal-grounding-system-episteme.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "G.6 — Evidence Graph & Provenance Ledger"
  - "G.6:5 — Archetypal Grounding (System / Episteme)"
line_start: 75546
line_end: 75553
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

### G.6:5 - Archetypal Grounding (System / Episteme)

**System (Γ_sys):** *Autonomous brake envelope claim.*
Claim: “Stop within 50 m from 100 km/h.” EvidenceGraph nodes include proof carriers (TA/VA), instrumented track tests (LA/VA), calibration carriers, and an external test lab as an external evidencing role (no self‑evidence). A `PathId` provides a stable justification address; empirical legs are bound to explicit windows; crossings (if any) are explicit and pinned.

**Episteme (Γ_epist):** *Benchmark parity/replication lineage (post‑2015 practice).*
Claim: “Method family M attains parity on ImageNet‑style tasks under a declared evaluation protocol.” EvidenceGraph nodes include replication carriers (LA), legality/metric‑soundness carriers (VA), and tool‑qualification carriers (TA). The cited `PathId` binds the `ReferencePlane`, the scope slice, and the pinned evaluation/legal surfaces (by edition/policy ids rather than prose). When refresh triggers occur (edition pin change, evidence surface edit, decay events), downstream artefacts can re‑cite or re‑compute using the same `PathSliceId` addressing discipline.

