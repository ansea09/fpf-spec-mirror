---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__005_forces.md"
commit_sha: "ea8c54542bf017f36659167f36e816fad4de88cb"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:3 — Forces"
line_start: 130172
line_end: 130181
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

* **Pluralism vs comparability.** Support justified comparisons across Traditions while preserving their differences in meaning and admissibility.
* **Partial orders.** Many targets are only partially ordered; parity reporting must preserve CSLC-admissible outcome shape (often declared set results rather than a single scalar; an archive may supply the compared candidates).
* **Edition sensitivity.** Parity must be robust to silent drift in measurement and comparator definitions. When DHC, QD, or OEE modes are used, the required definition pins are introduced only through the corresponding `Extensions` blocks; omit them when unused.
* **Telemetry versus objectives.** `IlluminationSummary`, coverage, and regret are report-only telemetry by default. A dominance change needs an explicit CAL policy id recorded in the audit pins.
* **Crossing visibility.** An actual E.18 flow crossing or A.21 gate used by parity retains its required `CrossingBundle`, pins and checks. Failure blocks the dependent publication or use.
* **Cross-sense and reference-plane reuse.** When expressions have distinct F.17 source-local meanings, recover both cells and establish the required F.9 relation; a ReferencePlane crossing follows its own declared crossing basis. Each actual correspondence retains its required pins and evidence; any justified numerical loss follows its receiving model and R-channel placement.
* **Refreshability.** Parity must emit RSCR-relevant causes as canonical ids, with enough pins to identify the affected use and plan any needed rerun.

