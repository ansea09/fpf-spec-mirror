---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:11"
section_title: "Working reading checks"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__015_working-reading-checks.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:11 — Working reading checks"
line_start: 81882
line_end: 81887
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

### G.9:11 — Working reading checks

- If two baselines are being compared under different freshness windows, comparator editions, or silent normalization rules, this pattern has not yet been satisfied.
- If parity cannot tell the reader what was held constant, what remained telemetry, and what crossings or penalties were active, the report is not yet usable.
- If a scalar winner is being claimed where only a selected set or partial order is CSLC-admissible, parity is overclaiming and should publish the CSLC-admissible outcome shape instead.

