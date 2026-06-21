---
chunk_kind: "child"
pattern_id: "G.7"
pattern_title: "Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
section_id: "G.7:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/G.7/G.7__004_forces.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "G.7 — Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
  - "G.7:3 — Forces"
line_start: 84487
line_end: 84496
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

### G.7:3 - Forces

| Force                                    | Tension                                                                                                                                                                   |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Comparability vs local authority**     | Enable comparisons across Traditions ↔ avoid overriding Context‑local meaning.                                                                                            |
| **Auditability vs authoring throughput** | Require explicit artefacts, losses, and pins ↔ keep the calibration procedure light enough to be used.                                                                    |
| **Targeted refresh vs safety**           | Emit path‑local RSCR triggers ↔ ensure triggers are typed and carry enough payload pins for audit and rerun planning.                                                     |
| **Plane awareness vs “one story”**       | Explicitly surface `ReferencePlane` and plane penalties ↔ avoid turning plane discussion into a second semantics of “sameness”.                                           |
| **QD comparability vs metric drift**     | Enable cross‑context reporting of archive/illumination telemetry ↔ enforce edition‑aware pins for descriptor/distance/policies only when those modes are actually in use. |

