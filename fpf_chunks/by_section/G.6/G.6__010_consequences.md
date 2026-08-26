---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__010_consequences.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:9 — Consequences"
line_start: 101439
line_end: 101453
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.1"
  - "A.2.4"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.18"
  - "E.18.2"
  - "F.10"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.9"
keywords:
  - "EvidenceGraph"
  - "NotCarried"
  - "PathCitationRecord"
  - "PathId"
  - "PathSliceId"
  - "actual-use relation"
  - "direct governors"
  - "downstream work"
  - "exact direct relations"
  - "exact represented objects"
  - "local refresh"
  - "obtaining claims"
  - "provenance ledger"
  - "representation correspondence"
  - "source/currentness"
  - "unresolved gaps"
---

### G.6:9 - Consequences

Benefits:

* downstream records cite evidence-provenance paths without copying evidence tables;
* source, bridge, policy, edition, and time changes reopen the smallest path slice;
* evidence, assurance, causal use, status, gate, work, and publication claims stay in their subject patterns;
* provenance becomes replayable and privacy-minimizable through scoped refs.

Costs:

* path identity, node typing, and source-currentness refs add overhead;
* graph paths can look like routes unless declarative representation discipline is kept visible;
* users must resist treating one complete path as a complete downstream decision.

