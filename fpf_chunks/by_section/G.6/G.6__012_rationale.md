---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph & Provenance Ledger"
section_id: "G.6:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__012_rationale.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "G.6 — Evidence Graph & Provenance Ledger"
  - "G.6:10 — Rationale"
line_start: 71055
line_end: 71065
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

### G.6:10 - Rationale

G.6 concretizes the “because‑graph” implicit in A.10 into a typed, lane‑aware DAG with stable path addresses. It relies on canonical governing definitions for semantics:

* A.10 for anchoring discipline and carrier reality,
* B.3 for the assurance skeleton,
* G.4 for proof/evidence profile semantics,
* `G.Core` for universal crossing, penalty, Default Governing Definition Index, and typed RSCR cause discipline.

This preserves conceptual modularity: G.6 standardizes *addressable provenance*, not a competing legality or selection mechanism.

