---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:0.2"
section_title: "What this buys"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__004_what-this-buys.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:0.2 — What this buys"
line_start: 102800
line_end: 102807
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

### G.9:0.2 — What this buys

- one `ParityPlan@Context` that fixes baseline, freshness, comparator, and bridge discipline up front
- one `ParityReport@Context` that echoes the active pins, outcomes, and evidence trace by value
- one harness that downstream selection can consume without inventing a `G.9`-local CSLC gate or a shadow governance card

Illumination, coverage, and regret remain telemetry by default. If they are promoted into dominance, that promotion must be one explicit policy-bound choice rather than one hidden scoring convenience.

