---
chunk_kind: "child"
pattern_id: "C.27.TA"
pattern_title: "Temporal Aspect: Time Windows, Rhythm, Cadence, and Currentness"
section_id: "C.27.TA:8"
section_title: "Common Anti-Patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/C.27.TA/C.27.TA__010_common-anti-patterns.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "C.27.TA — Temporal Aspect: Time Windows, Rhythm, Cadence, and Currentness"
  - "C.27.TA:8 — Common Anti-Patterns"
line_start: 49988
line_end: 49997
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.3.4"
  - "A.6.5"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.18"
  - "E.24"
  - "G.11"
  - "G.9"
keywords:
  - "cadence"
  - "currentness"
  - "freshness"
  - "recovery timing"
  - "rhythm"
  - "temporal aspect"
  - "time window"
  - "validity window"
---

### C.27.TA:8 - Common Anti-Patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Cadence without bearer | "Weekly cadence" appears without saying what has the cadence. | Name bearer, timing reference, interval, and governing use relation. |
| Freshness without window | A source is called current without reference time or validity window. | Write currentness/freshness with reference time, validity window, and refresh condition. |
| Recovery without disturbance | A claim says "recovery improved" without starting condition or interval. | Name disturbance, bearer, recovery window, and governing use. |
| Rhythm as value | A rhythm is treated as good by default. | Keep value, assurance, quality, or proxy claims with their governing patterns. |
| Timing as transformation | A time window is treated as if it specified the change. | Use `A.3.4` for the transformation relation and C.27.TA for the temporal aspect. |

