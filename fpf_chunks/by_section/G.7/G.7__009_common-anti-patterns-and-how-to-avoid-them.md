---
chunk_kind: "child"
pattern_id: "G.7"
pattern_title: "Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
section_id: "G.7:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/G.7/G.7__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "G.7 — Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
  - "G.7:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 114467
line_end: 114481
dependencies:
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.21"
  - "C.23"
  - "C.3.3"
  - "E.10"
  - "E.18"
  - "F.17"
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

### G.7:8 - Common Anti-Patterns and How to Avoid Them

* **Bridge‑by‑prose (“they have the same sense”).**
  **Avoid:** publish BCT rows + BridgeCards + UTS rows; require SenseCell anchoring and row scopes.
* **Scope or sense relation used as a kind bridge.**
  **Avoid:** state the channel in `RowScopeId` and use its direct governor. A C.3.3 correspondence needs its kind endpoints and separate receiving classification; cite CL^k and any loss policy only when that calibration or reliance account uses them.
* **Plane blindness (“concept = world”).**
  **Avoid:** record plane pins and policy id pins; keep plane effects auditable and separable from CL/CL^k semantics.
* **CL smoothing / averaging.**
  **Avoid:** establish the common scale and calibration question before taking a minimum; retain actual counterexamples and losses, and keep the receiving decision separate.
* **Pack‑wide refresh on a local bridge edit.**
  **Avoid:** register sentinels scoped to `PathSliceId` and emit typed RSCR triggers with minimal payload pins.
* **QD metric drift by unpinned artefacts.**
  **Avoid:** enable `G.7:Ext.QDParityPins` only when needed and require edition/policy pins when enabled.

