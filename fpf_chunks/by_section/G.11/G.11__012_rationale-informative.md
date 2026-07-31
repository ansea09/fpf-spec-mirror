---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh and Decay Orchestrator"
section_id: "G.11:10"
section_title: "Rationale (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__012_rationale-informative.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "G.11 — Telemetry-Driven Refresh and Decay Orchestrator"
  - "G.11:10 — Rationale (informative)"
line_start: 101113
line_end: 101120
dependencies:
  - "B.3.4"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.28"
  - "C.32.P2S"
  - "E.18"
  - "F.15"
  - "G.10"
  - "G.12"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
  - "G.Core.TriggerAliasMap.G11"
keywords:
  - "Bridge Sentinels"
  - "PathSlice"
  - "RSCR"
  - "decay"
  - "deprecation"
  - "edition bumps"
  - "edition-aware"
  - "epistemic debt"
  - "re-shipping"
  - "refresh"
  - "telemetry"
---

### G.11:10 - Rationale (informative)

`G.11` is intentionally a **thin orchestration governing definition**:

* The refresh loop is powerful enough to coordinate reruns and republishing, but **too thin to become a second spec**. That is why trigger semantics, invariants, and defaults are delegated to `G.Core`.
* The kit is split across the **P2W planning-to-work boundary** so that WorkPlanning plan items remain planning references and executed work remains auditably executed work.
* Alias stability is maintained by allowing trigger aliases (`T0…T7`) while prohibiting them from becoming semantic authorities.

