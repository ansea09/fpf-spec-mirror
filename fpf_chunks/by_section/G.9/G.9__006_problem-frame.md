---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:2"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__006_problem-frame.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:2 — Problem frame"
line_start: 98136
line_end: 98148
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

### G.9:2 — Problem frame

Parity claims become non‑reproducible or non‑comparable when any of the following are implicit:

* evidence window / freshness regime,
* comparator semantics (including any normalization / comparability mapping),
* method‑family “measurement” edition pins (incl. DHC method/spec),
* cross‑Context reuse (Bridge refs, crossing pins, and CL penalty placement),
* dominance and `PortfolioMode` interpretation rules,
* gate outcomes (why a run abstained or degraded).

G.9’s role is to make these recoverable as **pinned and publishable** as a *method of obtaining outputs* (MOO) without introducing new governing spec refs.

