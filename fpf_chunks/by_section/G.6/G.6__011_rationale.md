---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__011_rationale.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:10 — Rationale"
line_start: 90968
line_end: 90975
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

### G.6:10 - Rationale

`A.10` already gives the evidence-provenance graph relation for claims. `G.6` adds the Part-G need that local A.10 records do not fully satisfy: stable citation and path-local refresh for selectors, benchmarks, maturity transitions, assurance records, and release packages.

The pattern uses a graph mathematical lens because the useful mathematical object is a path through typed nodes and edges. It does not use graph language to claim that work "flows" through the path. When actual transformation structure matters, `E.18` governs it. When actual work matters, `A.15.1` governs it.

The pattern uses ledger language only for a provenance record. It does not invite process logs into pattern prose.

