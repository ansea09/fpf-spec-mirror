---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Decide Whether and How to Refresh SoTA Packs and Related Results (Telemetry and Decay)"
section_id: "G.11:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__002_use-this-when.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "G.11 — Decide Whether and How to Refresh SoTA Packs and Related Results (Telemetry and Decay)"
  - "G.11:0 — Use this when"
line_start: 131182
line_end: 131203
dependencies:
  - "A.10.1"
  - "A.6.RCD"
  - "B.3.4"
  - "C.11.DUA"
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
  - "deprecation"
  - "edition-aware"
  - "epistemic debt"
  - "re-shipping"
  - "refresh"
  - "telemetry"
  - "use-qualified currentness"
---

### G.11:0 - Use this when

Use this pattern when a changed premise or condition may alter whether a shipped pack or related result supports its receiving use. The change can concern evidence, source currentness, telemetry, an edition or policy, bridge calibration, a relied-on base relation definition, the named substrate edition or derivation applicability. The affected result can be an evidence set, dashboard, selected set, archive, front, Q-front, term bridge, descriptor set, parity result or use of an `A.6.RCD` definition.

#### G.11:0.1 - What goes wrong if missed

A team may rerun unrelated work, continue using an unsupported result or publish a currentness report without repairing the affected use. First determine what the changed basis permits; select and perform upkeep only where it is needed.

#### G.11:0.2 - What this buys

The practitioner first decides what the available support permits for the receiving use. A shared premise can reopen several dependent results while leaving independent results usable. When upkeep is justified, the refresh plan names that scope, its source and policy basis, and the selected actions. The resulting report records what was actually performed.

When a later or replacement source may change a claim and the actual receiving uses must first be found and revalidated, use `A.10.1` for the bounded search frame, discovery coverage and gaps, exact-use test, action-changing reach, application of the direct subject guidance, and the independently obtained subject result. `G.11` continues to govern source currentness, decay, refresh planning, and refresh reporting. Use a separately established currentness result or independently obtained subject result to plan later refresh under its governing pattern.

#### G.11:0.3 - First output

When a structured currentness line is useful for a loop, harness, workflow-store or DPF seed artifact, name its currentness object: for example, the source pack, evaluator, benchmark, harness or workflow edition, pattern seed, PFAD/PFR dependency, selected set, archive, front or publication carrier. The line can state currentness, source decay, edition change, telemetry and scoped refresh refs. Its subject pattern determines whether the artifact improved.

First establish whether the current conditions and available basis already support the receiving use. If they do, retain that result without a new currentness line, WorkPlan, waiver or skip-refresh certificate. When a later recipient needs a changed limit or retained reason, keep the minimum useful content with the existing result or publication; a `RefreshCurrentnessLine@Context` can express it when a structured line is useful. Produce a `RefreshPlan@Context` only for selected planned refresh. For an underlying claim about a selected set, archive, culture, bridge, evidence, dashboard or shipping, obtain that subject pattern's result; currentness does not establish its adequacy.

When a currentness record is needed, include the applicable framework edition pins, source packs, publication-carrier currentness, deprecation, supersession and source-decay conditions. In that record, cite `E.4` for the affected framework, `E.4.PFR` for a framework relation, `E.4.PFAD` for the framework architecture decision, the exact source contribution and bounded use, including the `G.2` pack when that route was used, and `E.11` for discovery. For publication, cite `E.17` for a source-backed face and return to source and `E.24.PUB` for the occurrence, form, carrier, audience, bounded use, and availability.

