---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh and Decay Orchestrator"
section_id: "G.11:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__002_use-this-when.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "G.11 — Telemetry-Driven Refresh and Decay Orchestrator"
  - "G.11:0 — Use this when"
line_start: 102901
line_end: 102919
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

### G.11:0 - Use this when

Use this pattern when a shipped pack, evidence set, dashboard, selected set, archive, front, Q-front, term bridge, descriptor set, parity result, or a use that relies on an `A.6.RCD` predicate definition or derived relation kind may be stale because telemetry, freshness, edition pins, policy pins, evidence, bridge calibration, source currentness, a relied-on base relation definition, the named substrate edition, or derivation applicability changed.

#### G.11:0.1 - What goes wrong if missed

The team either rebuilds everything after every small change or keeps using a shipped record whose source, descriptor, edition, policy, bridge, or archive currentness has silently drifted. Refresh then becomes an informal maintenance habit rather than a scoped, reviewable work plan and report.

#### G.11:0.2 - What this buys

The practitioner gets a small refresh kit: name the affected object, currentness object kind, source record, edition or lineage pins, affected scope, subject pattern, planned refresh action, and report. The refresh can stay local while still preserving comparability, selected-set meaning, archive and front meaning, and source-currentness evidence.

#### G.11:0.3 - First output
For loop, harness, workflow-store, or DPF seed artifacts, a refresh line names the currentness object directly: source pack, evaluator, benchmark, harness edition, workflow edition, pattern seed, PFAD and PFR dependency, selected set, archive, front, or publication carrier. `G.11` records currentness, source decay, edition change, telemetry, scoped refresh action, and report refs; it does not create a local "reopen and refresh" pair and does not decide whether the artifact improved.

Write one `RefreshCurrentnessLine@Context` or one `RefreshPlan@Context` with the affected scope and the applicable pattern named. If the current claim concerns selected-set result declaration, archive or front stewardship, cultural evolution, term bridges, evidence, a dashboard, or shipping, use the pattern that defines and tests that claim rather than defining it inside the refresh record. For publication, use `E.17` for a source-backed face and return to source and `E.24.PUB` for the occurrence, form, carrier, audience, bounded use, and availability.

When currentness is the live question, use G.11 to record framework edition pins, source packs, publication-carrier currentness, deprecation, supersession, and source-decay conditions. In that record, cite `E.4` for the affected framework, `E.4.PFR` for a framework relation, `E.4.PFAD` for the framework architecture decision, `G.2` for source use, and `E.11` for discovery. For publication, cite `E.17` for a source-backed face and return to source and `E.24.PUB` for the occurrence, form, carrier, audience, bounded use, and availability. Do not create private refresh vocabulary for these neighboring meanings.

