---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh and Decay Orchestrator"
section_id: "G.11:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__002_use-this-when.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "G.11 — Telemetry-Driven Refresh and Decay Orchestrator"
  - "G.11:0 — Use this when"
line_start: 100610
line_end: 100628
dependencies:
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

### G.11:0 - Use this when

Use this pattern when a shipped pack, evidence set, dashboard, selected set, archive, front, Q-front, term bridge, descriptor set, or parity result may be stale because telemetry, freshness, edition pins, policy pins, evidence, bridge calibration, or source currentness changed.

#### G.11:0.1 - What goes wrong if missed

The team either rebuilds everything after every small change or keeps using a shipped record whose source, descriptor, edition, policy, bridge, or archive currentness has silently drifted. Refresh then becomes an informal maintenance habit rather than a scoped, reviewable work plan and report.

#### G.11:0.2 - What this buys

The practitioner gets a small refresh kit: name the affected object, currentness object kind, source record, edition or lineage pins, affected scope, governing pattern, planned refresh action, and report. The refresh can stay local while still preserving comparability, selected-set meaning, archive and front meaning, and source-currentness evidence.

#### G.11:0.3 - First output
For loop, harness, workflow-store, or DPF seed artifacts, a refresh line names the currentness object directly: source pack, evaluator, benchmark, harness edition, workflow edition, pattern seed, PFAD and PFR dependency, selected set, archive, front, or publication carrier. `G.11` records currentness, source decay, edition change, telemetry, scoped refresh action, and report refs; it does not create a local "reopen and refresh" pair and does not decide whether the artifact improved.

Write one `RefreshCurrentnessLine@Context` or one `RefreshPlan@Context` with the affected scope and direct governing pattern named. If the meaning belongs to selected-set publication, archive or front stewardship, cultural evolution, term bridges, evidence, dashboard, or shipping, cite that governing pattern rather than defining the meaning inside the refresh record.

Framework edition pins, source packs, publication-carrier currentness, deprecation, supersession, and source-decay conditions are refresh and currentness claims governed here when currentness is the live question. Record the framework-specific trigger and cite `E.4`, `E.4.PFR`, `E.4.PFAD`, `G.2`, `E.11`, or `E.17` as the direct owner of the affected framework, source, decision, or publication meaning instead of creating a private refresh vocabulary in the framework pattern.

