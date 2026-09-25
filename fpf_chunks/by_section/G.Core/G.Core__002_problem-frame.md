---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Discipline SoTA Kit Invariants, Defaults and Refresh Triggers (Part G)"
section_id: "G.Core:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__002_problem-frame.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "G.Core — Discipline SoTA Kit Invariants, Defaults and Refresh Triggers (Part G)"
  - "G.Core:1 — Problem frame"
line_start: 110347
line_end: 110357
dependencies:
  - "A.15.3"
  - "A.19"
  - "A.19.CHR"
  - "A.6.7"
  - "E.10"
  - "E.19"
  - "E.8"
  - "G.0"
  - "G.13"
  - "G.Core"
keywords:
  - "Default Governing Definition Index"
  - "ID continuity"
  - "Part‑G invariants"
  - "RSCR trigger kinds"
  - "core linkage"
  - "delegation-first core"
---

### G.Core:1 - Problem frame

Part G contains patterns for CG‑frame characterization and its downstream artefacts (cards, evidence graphs, bridge surfaces, refresh/shipping orchestration, parity harnesses, dashboards, interop surfaces). In the current spec, several invariants are already present as **suite obligations/protocol norms** and are **reused across Part G**.

*Part‑G‑wide* invariants are governed by `G.Core` so every `G.x` can:

* cite the core invariants rather than restating them, and
* isolate pattern-scoped specifics as `Extensions` without turning each `G.x` into a mixed bag of universal rules, kit surfaces, and method/generator descriptions.

This pattern (`G.Core`) therefore acts as the **deduplication hub** for FPF Part G.

