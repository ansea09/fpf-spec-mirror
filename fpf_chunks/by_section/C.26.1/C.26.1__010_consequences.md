---
chunk_kind: "child"
pattern_id: "C.26.1"
pattern_title: "Probe-Coupled Boundary Interaction"
section_id: "C.26.1:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.1/C.26.1__010_consequences.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "C.26.1 — Probe-Coupled Boundary Interaction"
  - "C.26.1:9 — Consequences"
line_start: 53793
line_end: 53798
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.6"
  - "A.6.8"
  - "A.6.B"
  - "A.6.P"
  - "B.3"
  - "C.16"
  - "C.25"
  - "C.26"
  - "C.26.2"
  - "C.26.3"
  - "F.9"
keywords:
  - "API read"
  - "bridge result"
  - "dashboard as instrument"
  - "evidence window"
  - "export loss"
  - "passive read"
  - "probe-coupled boundary"
  - "survey"
  - "workshop as state-changing interaction"
---

### C.26.1:9 - Consequences

This pattern makes boundary decisions more honest. It turns "the workshop showed the split" into "the workshop both showed and changed the split-relevant state." It turns "the dashboard says ready" into "the dashboard is probe-coupled evidence with a limited decision use."

The cost is that some familiar artifacts lose false authority. Dashboards, workshops, surveys, API reads, and messages remain useful, but they no longer get to pretend they are always neutral windows.

