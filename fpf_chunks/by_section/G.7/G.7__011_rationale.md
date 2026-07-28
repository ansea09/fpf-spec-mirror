---
chunk_kind: "child"
pattern_id: "G.7"
pattern_title: "Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
section_id: "G.7:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/G.7/G.7__011_rationale.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "G.7 — Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
  - "G.7:10 — Rationale"
line_start: 98380
line_end: 98385
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

### G.7:10 - Rationale

* **Why a kit (not a new governance card or legality gate)?** Bridge calibration must support many downstream consumers without becoming a competing legality gate; governing-spec semantics remain governed by `CG‑Spec`/`CN‑Spec`.
* **Why BCT + RegressionSet + SentinelSet?** Because calibration without regression tests drifts silently, and regression without sentinels is operationally unusable (refresh becomes global).
* **Why row scopes?** Because “comparable” is not one thing; scope must be explicit to avoid accidental substitution.

