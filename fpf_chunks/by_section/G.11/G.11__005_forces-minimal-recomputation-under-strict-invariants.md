---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh and Decay Orchestrator"
section_id: "G.11:3"
section_title: "Forces — Minimal recomputation under strict invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__005_forces-minimal-recomputation-under-strict-invariants.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "G.11 — Telemetry-Driven Refresh and Decay Orchestrator"
  - "G.11:3 — Forces — Minimal recomputation under strict invariants"
line_start: 92828
line_end: 92835
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

### G.11:3 - Forces — Minimal recomputation under strict invariants

* **Minimal scope vs. completeness.** Refresh must be *as local as possible* (slice-scoped), but still include a defensible dependency closure over evidence and crossings.
* **Operational urgency vs. auditability.** Refresh is triggered by run-time telemetry and decay, yet must remain auditable as Work (pins, refs, paths), not as opaque “decisions.”
* **Alias stability vs. semantic unification.** Existing trigger labels must remain usable, but their meaning must be one governing definition and id-based.
* **Modularity vs. orchestration power.** `G.11` must coordinate harvesting, parity, and shipping without re-implementing them or importing discipline-specific method semantics into core.
* **Policy-bound behavior vs. “smart defaults.”** Ordering of refresh, priority heuristics, and budget handling are valuable—but must live as policy-bound extensions, not as hidden universal rules.

