---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh & Decay Orchestrator"
section_id: "G.11:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__001_intro.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "G.11 — Telemetry-Driven Refresh & Decay Orchestrator"
  - "G.11:intro — Intro"
line_start: 83760
line_end: 83775
dependencies:
  - "B.3.4"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.28"
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

## G.11 - Telemetry-Driven Refresh & Decay Orchestrator

**Tag.** Architectural pattern (architectural; notation-independent)
**Status.** Stable
**Normativity.** Normative (unless explicitly marked informative)

**Stage.** run-time + maintenance-time (selective re-computation, republication, and controlled deprecation)

**Primary outputs (kit publication units and records).** `RefreshQueue`, `RefreshPlan@Context` (WorkPlanning plan item), `RefreshReport@Context` (Work or Audit record), `DeprecationNotice@Context`, `EditionBumpLog@Context`.

**Primary hooks.** `G.Core` (RSCR trigger catalogue + alias docking + Default Governing Definition Index), `G.6` (EvidenceGraph; `PathId`/`PathSliceId`), `G.7` (Bridge Sentinels; CL/Φ/plane policy pins), `G.5` (set-returning selection/dispatch), `G.8` (SoS-LOGBundle telemetry hooks), `G.9` (parity reruns), `G.10` (shipping hooks and pack-level telemetry pins), `G.12` (dashboard telemetry pins), `B.3.4` (freshness/decay), `E.18` (GateCrossing/CrossingBundle visibility), optional `C.18 and C.19` (QD/E–E policy pins), `C.23` (SoS-LOG branches / maturity ladders), `C.28` (causal-use support records whose SoTA-sensitive fields can change downstream causal-use results).

**Non-duplication note (Phase-2).**
This pattern **does not** (i) define the meaning of RSCR trigger kinds, (ii) introduce “shadow specs” for CN/CG legality, (iii) redefine tri-state guards / penalties / set-return semantics, (iv) re-govern shipping or harvesting, or (v) mint new `RSCRTriggerKindId` / default governing definitions (design-time changes live in `G.Core` and are recorded via DRR, `E.9`).
All such universal norms are **cited via `G.Core`** and enforced through **delegation** in this pattern’s conformance checklist.

