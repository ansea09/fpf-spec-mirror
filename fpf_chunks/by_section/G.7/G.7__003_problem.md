---
chunk_kind: "child"
pattern_id: "G.7"
pattern_title: "Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
section_id: "G.7:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/G.7/G.7__003_problem.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "G.7 — Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
  - "G.7:2 — Problem"
line_start: 128646
line_end: 128653
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

### G.7:2 - Problem

1. Cross-Tradition comparison through informal “synonymy” or an unspecified mapping can hide meaning drift and the relation actually needed.
2. An unexamined plane mismatch (world ↔ concept ↔ episteme, or another `ReferencePlane` shift) can support an unwarranted downstream confidence claim.
3. Calibration changes (CL/CL^k/plane or their policy pins) require rechecks of the uses that depend on them. Unrelated pack contents retain their existing basis.
4. If bridges are involved in QD/illumination or other edition‑sensitive telemetry, **edition pins** must be tracked (otherwise comparisons become irreproducible after a map/distance/policy update).
5. Averaging ordinal row values is inadmissible; even a lawful summary can hide a loss needed by a receiving task. Preserve the cell evidence and use only a summary justified for the stated calibration question.

