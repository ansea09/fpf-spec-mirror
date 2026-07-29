---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:0.1"
section_title: "What goes wrong if missed"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__003_what-goes-wrong-if-missed.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:0.1 — What goes wrong if missed"
line_start: 100003
line_end: 100008
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

### G.9:0.1 — What goes wrong if missed

- benchmark numbers mix different windows, baselines, or comparator editions and still pretend to be comparable
- cross-context reuse or normalization mapping stays hidden until a disagreement appears downstream
- parity flattens a partial order into one scalar winner and silently changes what the comparison means

