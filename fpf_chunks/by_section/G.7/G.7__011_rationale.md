---
chunk_kind: "child"
pattern_id: "G.7"
pattern_title: "Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
section_id: "G.7:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/G.7/G.7__011_rationale.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "G.7 — Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
  - "G.7:10 — Rationale"
line_start: 138674
line_end: 138679
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

### G.7:10 - Rationale

* **Why publish a kit?** Several consumers can use the same calibration. They use `CN‑Spec` for the governing comparison rules and `CG‑Spec` for the legality gate. The kit supplies calibration without creating a second governance card or gate.
* **Why BCT + RegressionSet + SentinelSet?** Regression tests make calibration drift detectable; sentinels identify the downstream scopes to refresh.
* **Why declare the row scope?** Two constructs may be comparable for one question and fail another. The scope identifies the correspondence or difference the row calibrates, so a reader can check the intended use.

