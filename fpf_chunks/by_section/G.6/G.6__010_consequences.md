---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__010_consequences.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:9 — Consequences"
line_start: 94233
line_end: 94247
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

### G.6:9 - Consequences

Benefits:

* downstream records cite evidence-provenance paths without copying evidence tables;
* source, bridge, policy, edition, and time changes reopen the smallest path slice;
* evidence, assurance, causal use, status, gate, work, and publication claims stay in their governing patterns;
* provenance becomes replayable and privacy-minimizable through scoped refs.

Costs:

* path identity, node typing, and source-currentness refs add overhead;
* graph paths can look like routes unless declarative representation discipline is kept visible;
* users must resist treating one complete path as a complete downstream decision.

