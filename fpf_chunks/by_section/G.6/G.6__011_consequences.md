---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph & Provenance Ledger"
section_id: "G.6:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__011_consequences.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "G.6 — Evidence Graph & Provenance Ledger"
  - "G.6:9 — Consequences"
line_start: 78875
line_end: 78879
dependencies:
  - "A.10"
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.18"
  - "E.5"
  - "E.5.2"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
  - "G.Core.TriggerAliasMap.G6"
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

### G.6:9 - Consequences

**Benefits.** Path‑addressable provenance; crossing/plane effects are auditable by pins rather than folklore; selectors and auditors read the same path-addressable evidence graph; refresh becomes localized (path‑scoped) rather than global “rerun everything”.
**Trade‑offs.** Authors must declare (or pin) time/plane/scope and keep pins explicit; mitigated by reusing CAL EvidenceProfiles and by modularizing method‑specific telemetry as Extensions.

