---
chunk_kind: "child"
pattern_id: "C.26.3"
pattern_title: "Viability-Envelope Boundary Regulation"
section_id: "C.26.3:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.3/C.26.3__003_problem.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "C.26.3 — Viability-Envelope Boundary Regulation"
  - "C.26.3:2 — Problem"
line_start: 53971
line_end: 53978
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.3"
  - "A.6"
  - "B.3"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "U.Dynamics"
keywords:
  - "allostasis"
  - "boundary regulation"
  - "failure mode"
  - "homeostasis"
  - "metric-induced distortion"
  - "quality bundle"
  - "sensor/probe/actuator split"
  - "service viability"
  - "viability envelope"
---

### C.26.3:2 - Problem

Teams often collapse viability into one dashboard value or fixed target. They optimize latency and damage operator load. They improve availability and increase compliance exposure. They preserve one metric while exhausting the team, hiding risk, or making recovery slower.

A second failure is passive sensing. A metric, probe, dashboard, alert, or health check is treated as a neutral window into viability, even when it changes behavior, hides unmeasured dimensions, or becomes an actuator through Goodhart effects.

A third failure is static stability. Teams say "keep the system stable" as if stability always means holding one internal variable fixed. In real architecture work, preserving viability may require changing environment, access, staffing, caching, throttling, routing, protocol, context split, or measurement design.

