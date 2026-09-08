---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh and Decay Orchestrator"
section_id: "G.11:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__002_use-this-when.md"
commit_sha: "2154d21570c891bd5ed30fd6e6136f17f1942cae"
heading_path:
  - "G.11 — Telemetry-Driven Refresh and Decay Orchestrator"
  - "G.11:0 — Use this when"
line_start: 106871
line_end: 106892
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
  - "deprecation"
  - "edition-aware"
  - "epistemic debt"
  - "re-shipping"
  - "refresh"
  - "telemetry"
  - "use-qualified currentness"
---

### G.11:0 - Use this when

Use this pattern when a shipped pack, evidence set, dashboard, selected set, archive, front, Q-front, term bridge, descriptor set, parity result, or a use that relies on an `A.6.RCD` predicate definition or derived relation kind may be stale because telemetry, freshness, edition pins, policy pins, evidence, bridge calibration, source currentness, a relied-on base relation definition, the named substrate edition, or derivation applicability changed.

#### G.11:0.1 - What goes wrong if missed

The team either rebuilds everything after every small change or keeps using a shipped record whose source, descriptor, edition, policy, bridge, or archive currentness has silently drifted. Refresh then becomes an informal maintenance habit rather than a scoped, reviewable work plan and report.

#### G.11:0.2 - What this buys

The practitioner first decides what the available support permits for the receiving use. When a changed premise requires upkeep, the refresh kit names the affected object and scope, the source and policy basis, and the justified action. Planning and reporting remain separate, and refresh can stay local while preserving comparability and subject-specific result meanings.

When a later or replacement source may change a claim and the actual receiving uses must first be found and revalidated, use `A.10.1` for the bounded search frame, discovery coverage and gaps, exact-use test, action-changing reach, application of the direct subject guidance, and the independently obtained subject result. `G.11` continues to govern source currentness, decay, refresh planning, and refresh reporting. A practitioner or admitted System may use a separately established currentness result or independently obtained subject result to plan later refresh without changing either result or the governing patterns.

#### G.11:0.3 - First output

For loop, harness, workflow-store, or DPF seed artifacts, a refresh line names the currentness object directly: source pack, evaluator, benchmark, harness edition, workflow edition, pattern seed, PFAD and PFR dependency, selected set, archive, front, or publication carrier. `G.11` records currentness, source decay, edition change, telemetry, scoped refresh action, and report refs; it does not decide whether the artifact improved.

First establish whether the current conditions and available basis already support the receiving use. If they do, retain that result without a new currentness line, WorkPlan, waiver or skip-refresh certificate. When a later recipient needs a changed limit or retained reason, keep the minimum useful content with the existing result or publication; a `RefreshCurrentnessLine@Context` can express it when a structured line is useful. Produce a `RefreshPlan@Context` only for selected planned refresh. For an underlying claim about a selected set, archive, culture, bridge, evidence, dashboard or shipping, obtain that subject pattern's result; currentness does not establish its adequacy.

When currentness is the live question, use G.11 to record framework edition pins, source packs, publication-carrier currentness, deprecation, supersession, and source-decay conditions. In that record, cite `E.4` for the affected framework, `E.4.PFR` for a framework relation, `E.4.PFAD` for the framework architecture decision, `G.2` for source use, and `E.11` for discovery. For publication, cite `E.17` for a source-backed face and return to source and `E.24.PUB` for the occurrence, form, carrier, audience, bounded use, and availability. Do not create private refresh vocabulary for these neighboring meanings.

