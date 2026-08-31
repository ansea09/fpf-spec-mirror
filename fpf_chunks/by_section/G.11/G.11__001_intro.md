---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh and Decay Orchestrator"
section_id: "G.11:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__001_intro.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "G.11 — Telemetry-Driven Refresh and Decay Orchestrator"
  - "G.11:intro — Intro"
line_start: 105917
line_end: 105932
dependencies:
  - "A.6.RCD"
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

## G.11 - Telemetry-Driven Refresh and Decay Orchestrator

**Tag.** Architectural pattern (architectural; notation-independent)
> **Status:** Stable
**Normativity.** Normative (unless explicitly marked informative)

**Stage.** run-time and maintenance-time (selective re-computation, republication, and controlled deprecation)

**Primary outputs (kit publication units and records).** `RefreshQueue`, `RefreshPlan@Context` (a local application name for one exact `U.WorkPlan`, not a new kind), `RefreshReport@Context` (Work or Audit record), `DeprecationNotice@Context`, `EditionBumpLog@Context`.

**Primary hooks.** `G.Core` (RSCR trigger catalogue, alias docking, and Default Governing Definition Index), `G.6` (EvidenceGraph; `PathId` and `PathSliceId`), `G.7` (Bridge Sentinels; CL, Φ, and plane policy pins), `G.5` (set-returning selection and dispatch), `G.8` (SoS-LOGBundle telemetry hooks), `G.9` (parity reruns), `G.10` (shipping hooks and pack-level telemetry pins), `G.12` (dashboard telemetry pins), `B.3.4` (freshness and decay), `E.18` (GateCrossing and CrossingBundle visibility), `C.18` and `C.19` archive, front, and live-pool policy pins, `C.23` (SoS-LOG branches and maturity ladders), `C.28` (causal-use support results whose SoTA-sensitive fields can change downstream causal-use results).

**Non-duplication note.**
`G.11` cites `G.Core` for RSCR trigger-kind meaning, CN and CG admissibility, tri-state guards, penalties, set-return semantics, shipping or harvesting delegation, `RSCRTriggerKindId` values, and default governing definitions.
Refresh plans and reports cite those governed definitions; they do not create local trigger meanings or default definitions inside the refresh record.

