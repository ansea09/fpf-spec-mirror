---
chunk_kind: "child"
pattern_id: "G.7"
pattern_title: "Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
section_id: "G.7:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/G.7/G.7__013_relations.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "G.7 — Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
  - "G.7:12 — Relations"
line_start: 97625
line_end: 97632
dependencies:
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.21"
  - "C.23"
  - "E.10"
  - "E.18"
  - "F.3"
  - "F.7"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.12"
  - "G.2"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.9"
  - "G.Core"
keywords:
  - "BridgeCalibrationTable (BCT)"
  - "BridgeCard"
  - "BridgeSentinel"
  - "Congruence Level (CL/CL^k/CL^plane)"
  - "GateCrossing"
  - "PathSliceId"
  - "RSCRTriggerKindId"
  - "ReferencePlane"
  - "RegressionSet"
  - "SentinelSet"
  - "UTS"
  - "bridge calibration"
  - "loss notes"
  - "waivers"
  - "Φ(CL)/Ψ(CL^k)/Φ_plane policy pins"
---

### G.7:12 - Relations

**Builds on:** `G.Core`, `G.2`, `F.3`, `F.7`, `F.9`, `B.3`, `E.10`, `E.18`, `A.21`, `G.6`, `C.21`.
**Optionally uses via Extensions:** **G.4** (Acceptance hooks), **C.23** (SoS‑LOG clauses), **C.18 and C.19** (QD/OEE pins).
**Used by / prerequisite for:** **G.5** (cross‑Tradition eligibility/selection), **G.11** (refresh orchestration), **G.9** (parity across Traditions where bridges are required), **G.10** (shipping surfaces that must cite bridge calibration ids), **G.12** (DHC dashboards when bridge counts/units are surfaced).
**Publishes to:** **UTS** (bridge and crossing rows; twin labels as applicable) and emits RSCR‑ready telemetry/trigger payloads for **G.11**.
**Constrains:** Any downstream consumer that claims cross‑Context/Tradition reuse must use the calibrated bridge artefacts/pins surfaced by this kit (governed by G.Core crossing invariants apply).

