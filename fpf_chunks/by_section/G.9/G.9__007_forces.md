---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__007_forces.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:3 — Forces"
line_start: 103217
line_end: 103226
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

### G.9:3 — Forces

* **Pluralism vs comparability.** Multiple Traditions must be comparable *without semantic collapse*.
* **Partial orders.** Many targets are only partially ordered; parity reporting must preserve CSLC-admissible outcome shape (often selected sets or archives rather than a single scalar).
* **Edition sensitivity.** Parity must be robust to silent drift in measurement and comparator definitions. When DHC, QD, or OEE modes are used, the required definition pins are introduced only through the corresponding `Extensions` blocks; omit them when unused.
* **Telemetry versus objectives.** `IlluminationSummary`, coverage, and regret are report-only telemetry by default. A dominance change needs an explicit CAL policy id recorded in the audit pins.
* **Crossing visibility.** Every crossing used by parity must be visible and auditable through its `CrossingBundle` and `GateCrossing` checks; failure blocks publication or use of the parity result.
* **Cross-sense and reference-plane reuse.** When expressions have distinct F.17 source-local meanings, recover both cells and establish the required F.9 relation; a ReferencePlane crossing follows its own declared crossing basis. Each actual crossing carries explicit pins, its audit evidence relation, and R-channel penalty placement.
* **Refreshability.** Parity must emit RSCR‑relevant causes as canonical ids, with enough pins to re‑run.

