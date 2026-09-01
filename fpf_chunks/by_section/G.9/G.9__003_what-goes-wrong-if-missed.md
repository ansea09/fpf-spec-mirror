---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:0.1"
section_title: "What goes wrong if missed"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__003_what-goes-wrong-if-missed.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:0.1 — What goes wrong if missed"
line_start: 105030
line_end: 105035
dependencies:
  - "A.19"
  - "A.2.6"
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
  - "U.ClaimScope"
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
- reuse across distinct source-local meanings, a reference-plane crossing, or a normalization mapping stays hidden until a disagreement appears downstream
- parity flattens a partial order into one scalar winner and silently changes what the comparison means

