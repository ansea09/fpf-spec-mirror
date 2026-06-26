---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__007_forces.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:3 — Forces"
line_start: 91053
line_end: 91062
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

### G.9:3 — Forces

* **Pluralism vs comparability.** Multiple Traditions must be comparable *without semantic collapse*.
* **Partial orders.** Many targets are only partially ordered; parity reporting must preserve CSLC-admissible outcome shape (often selected sets or archives rather than a single scalar).
* **Edition sensitivity.** Parity must be robust to silent drift in measurement/comparator definitions. When DHC/QD/OEE modes are used, the required definition pins are introduced only via the corresponding `Extensions` blocks (nil‑elision when unused).
* **Telemetry vs objectives.** IlluminationSummary and coverage/regret are telemetry: **report‑only by default**; dominance changes require explicit CAL policy ids (recorded in audit pins).
* **GateCrossing visibility.** Any crossings/gates used by parity must be visible and auditable via CrossingBundle + GateCrossing checks; failures block parity publication/consumption.
* **Cross‑Context reuse.** Any reuse across contexts or reference planes must carry explicit crossing pins, audit evidence relation, and R-channel penalty placement.
* **Refreshability.** Parity must emit RSCR‑relevant causes as canonical ids, with enough pins to re‑run.

