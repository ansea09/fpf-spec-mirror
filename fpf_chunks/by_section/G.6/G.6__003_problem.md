---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__003_problem.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:2 — Problem"
line_start: 96601
line_end: 96613
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

### G.6:2 - Problem

Large projects need to rely on evidence that is distributed across proofs, measurements, work traces, source publications, credentials, model cards, benchmarks, bridge records, and status sources. A compact evidence-use statement is often enough for a local claim, but it is not enough when downstream work must cite, replay, compare, refresh, or audit the whole provenance line.

The common failures are:

1. **Narrative provenance.** A report says "because the evidence carries the claim" but does not expose the graph path from claim to evidence relations, sources, checks, and work occurrences.
2. **Hidden crossing.** Evidence accepted in one bounded context, reference plane, edition, or status window is reused in another as if no bridge or currentness relation were needed.
3. **Role drift.** A proof, dataset, status cell, report, or benchmark result is treated as if it held an evidence role, instead of being a value in an evidence-use, status-use, source-use, or provenance relation.
4. **Path metaphor drift.** A graph path is read as an action route or workflow. The pattern then starts teaching work planning or performed work, rather than how a provenance graph is addressed.
5. **Ledger process drift.** A provenance ledger is confused with work-progress, review-comment, or process evidence. The pattern then records development status instead of citable evidence-provenance facts.
6. **Refresh fanout.** A source edit, edition change, decay event, bridge change, or policy change forces a broad "rerun everything" because the affected evidence-provenance paths were never addressable.

