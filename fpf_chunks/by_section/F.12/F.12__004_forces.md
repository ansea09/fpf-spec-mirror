---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__004_forces.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:3 — Forces"
line_start: 65634
line_end: 65643
dependencies:
  - "A.2.3"
  - "F.1"
  - "F.10"
  - "F.11"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.9"
  - "U.BoundedContext"
  - "U.PromiseContent"
keywords:
  - "Service Level Agreement (SLA)"
  - "Service Level Objective (SLO)"
  - "acceptance criteria"
  - "binding"
  - "observation"
---

### F.12:3 - Forces

| Force                                | Tension to resolve                                                                                        |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| **Promise vs. occurrence**           | A service **promise clause** (`U.PromiseContent`) is an external promise, yet acceptance must reference **Work** (run‑time). |
| **Locality vs. integration**         | Meanings are **context‑local**; still we must compare across **service situations**, plants, and monitors.                 |
| **Parsimony vs. realism**            | We want a small binding scheme, yet domains differ (percentiles, downtime minutes, control margins).      |
| **Evidence vs. privacy/feasibility** | Observations prove outcomes; sometimes only proxies exist.                                                |


