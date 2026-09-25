---
chunk_kind: "child"
pattern_id: "G.7"
pattern_title: "Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
section_id: "G.7:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.7/G.7__001_intro.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "G.7 — Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
  - "G.7:intro — Intro"
line_start: 114114
line_end: 114123
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

## G.7 - Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)

**Tag.** Architectural pattern
**Stage.** design‑time (calibration + publication) + run‑time (sentinel‑driven telemetry emission; orchestration governed by **G.11**)
**Start here.** Name the correspondence to be calibrated and the question of the receiving use, if one is already known. Recover its exact endpoints and governing relation, then state the evidence, preserved distinctions and losses. The first useful result is a bounded calibration statement; its suitability for a receiving use requires that use’s own rule, loss tolerance and reliance. Add the kit fields below when calibrated values or published, refreshable calibration records are needed. For a bounded reuse needing neither, follow the correspondence’s direct rule instead (F.9 for senses, C.3.3 for kinds, or the named plane rule).
**Primary output.** A calibration kit with a `BridgeCalibrationTable (BCT)`, `CalibrationLedger`, `RegressionSet` and `SentinelSet`. Each row cites the actual sense, kind or plane correspondence being calibrated. F.9 rows carry BridgeCards; public naming and real flow/gate crossings add their required UTS or bundle anchors. Sentinel triggers carry the affected references and live scope.
**Primary hooks.** `G.Core` (Part‑G invariants + RSCR trigger catalogue + Default Governing Definition Index), **G.2** (BridgeMatrix), **F.9** (BridgeCard + CL), **C.3.3** (KindBridge + CL^k when the kind channel is used), **F.3** (source-local sense clustering), **F.17** (SenseCell anchoring), **F.7** (source-local comparison display), **E.18/A.21** (GateCrossing + CrossingBundle checks), **G.6** (PathId/PathSliceId citation surface), **G.5** (downstream consumer for eligibility/selection), **G.11** (refresh orchestration consumer), **B.3** (assurance lanes + penalty policies), **C.21** (DHC accounts such as AlignmentDensity), **C.18 and C.19** (QD/OEE pins when relevant), **C.23** (SoS‑LOG clauses as explainability gates for cross‑Tradition choices), **G.4** (Acceptance hooks/thresholds when bridges are used as selector gates), **E.10** (LEX / strict distinction discipline).
**Working‑Model first.** Prefer a minimal, auditable calibration procedure and worked micro‑cases; escalate to heavier harnesses only where risk warrants (per **E.8**).
**Non‑duplication note.** Universal Part‑G invariants (no shadow specs; Bridge‑only crossings; penalty routing to `R_eff` only; P2W split; typed/id‑based RSCR causes; defaults with one governing definition; Δ‑discipline) are governed by `G.Core` and are *cited* via `CC‑GCORE‑*`. This pattern defines only the *bridge calibration kit* and its surfaces.

