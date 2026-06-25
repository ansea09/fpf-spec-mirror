---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__004_forces.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:3 — Forces"
line_start: 88212
line_end: 88222
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

### G.6:3 - Forces

| Force | Tension this pattern resolves |
| --- | --- |
| Citable provenance versus local evidence use | `A.10` and `A.2.4` can state evidence use; G.6 adds stable path identity only when downstream citation or refresh needs it. |
| Graph path and work claims stay distinct | A graph path is a declarative relation in an evidence-provenance DAG; actual work and transformation-flow claims stay with `A.15.1` and `E.18`. |
| Detail versus affordability | A path needs enough nodes, edges, windows, and constraints to replay reliance, but not every neighboring pattern boundary repeated in prose. |
| Typed downstream use versus one citation | The downstream citation may be one `PathId`, while verification, validation, lineage, assurance, status, causal-use, and source-currentness relations remain typed. |
| Bridge visibility versus reuse convenience | Cross-context or cross-plane reuse needs explicit bridge/currentness refs; label equality is not enough. |
| Refresh locality versus stale evidence | Path-level addresses let one changed source, bridge, edition, or policy reopen only the affected evidence-provenance paths. |

