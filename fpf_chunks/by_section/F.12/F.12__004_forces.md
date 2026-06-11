---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__004_forces.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:3 — Forces"
line_start: 73272
line_end: 73280
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

