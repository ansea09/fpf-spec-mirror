---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:9"
section_title: "Cited Records (what this pattern publishes)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__013_cited-records-what-this-pattern-publishes.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:9 — Cited Records (what this pattern publishes)"
line_start: 81058
line_end: 81066
dependencies:
  - "A.19"
  - "A.21"
  - "C.18"
  - "C.19"
  - "C.21"
  - "C.22.1"
  - "C.23"
  - "C.27"
  - "C.28"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.5.2"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "adaptation parity"
  - "benchmark plan"
  - "comparator pins"
  - "freshness windows"
  - "parity harness"
  - "selected-set outcomes"
---

### G.9:9 — Cited Records (what this pattern publishes)

**Exports (UTS‑publishable, edition‑pinned):**

* `ParityPlan@Context` (WorkPlanning plan item)
* `ParityReport@Context` (UTS publication record; work-result or audit-facing publication record only when the neighboring source relation is live)
* DRR+SCR refs (by id) and (when applicable) `PortfolioPackRef?`/selector output refs (by id), for downstream consumption.
* Telemetry pins/events (by id), for refresh wiring (`G.11`) and RSCR harnesses (`F.15`).

