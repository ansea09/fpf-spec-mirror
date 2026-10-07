---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__002_use-this-when.md"
commit_sha: "8685aeda98d24b7a7533364cb0df680eccfbfd4c"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:0 — Use this when"
line_start: 118520
line_end: 118539
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

### G.9:0 — Use this when

- rival method families, method sets, or adaptation paths must be compared under one declared baseline set and freshness window
- you need parity to publish one reproducible report rather than one opaque benchmark score
- downstream selection must recover comparator, normalization, bridge, and evidence pins without relying on one hidden scoring sheet

#### G.9:0.1 — What goes wrong if missed

- benchmark reports present numbers from different windows, baselines, or comparator editions as comparable
- reuse across distinct source-local meanings, a reference-plane crossing, or a normalization mapping stays hidden until a disagreement appears downstream
- parity flattens a partial order into one scalar winner and silently changes what the comparison means

#### G.9:0.2 — What this buys

- one exact `ParityPlanRef` that fixes the plan edition, baseline, freshness, comparator, and bridge discipline up front
- one `ParityReport` that cites that exact plan and echoes its active baseline binding, pins, outcomes, and evidence trace by value
- one harness that downstream selection can consume without inventing a `G.9`-local CSLC gate or a shadow governance card

Illumination, coverage, and regret remain telemetry by default. If they are promoted into dominance, that promotion must be one explicit policy-bound choice rather than one hidden scoring convenience.

