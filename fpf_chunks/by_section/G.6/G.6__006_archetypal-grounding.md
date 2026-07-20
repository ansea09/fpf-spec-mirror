---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__006_archetypal-grounding.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:5 — Archetypal Grounding"
line_start: 96003
line_end: 96020
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.21"
  - "A.6.5"
  - "A.6.RSIR"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.17.EFP"
  - "E.18"
  - "E.18.2"
  - "E.24"
  - "E.5.2"
  - "F.10"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "CrossingBundle"
  - "EvidenceGraph"
  - "GateCrossing"
  - "PathId"
  - "PathSliceId"
  - "SCR/RSCR"
  - "TriggerAliasMap"
  - "UTS PathCard"
  - "lane tags (TA/VA/LA)"
  - "provenance"
  - "Γ-fold pinning"
---

### G.6:5 - Archetypal Grounding

#### G.6:5.1 - Brake Envelope Claim

A braking-system claim says the vehicle stops within a declared distance under declared conditions. `A.10` identifies telemetry files, calibration certificates, test runs, and external lab work. `G.6` mints a `PathId` that cites the graph path from the claim to proof checks, instrumented tests, calibration records, work occurrences, and time windows. `NotCarried` names stronger downstream uses; `B.3` and gate patterns govern assurance and release uses.

#### G.6:5.2 - Benchmark Parity Claim

A model-family report says a method reaches parity on a benchmark. `G.6` cites the path through dataset version, evaluation protocol, result record, source publication, method description, and replication work. If the dataset edition, metric policy, or source-currentness relation changes, the affected `PathSliceId` reopens without rerunning unrelated evidence-provenance paths.

#### G.6:5.3 - Dashboard Status Cue

A dashboard cell shows `Ready`. `F.10` governs status-family mapping and status-use. `A.10` governs the evidence relation to the governing register or source. `G.6` is used only when a downstream release package, selector, assurance record, or audit needs a stable evidence-provenance path from the visible cue to source, status-use relation, query time, window, issuer, and currentness policy.

#### G.6:5.4 - Causal Policy Result

A policy report says an intervention caused improvement. `C.28` governs causal-use support basis, identification, and realizability. `A.10` records evidence relation. `G.6` only gives a citable evidence-provenance path from the policy claim to the causal-use refs, data sources, assumptions, work occurrences, time window, and bridge refs needed for later audit.

