---
chunk_kind: "child"
pattern_id: "C.27.TA"
pattern_title: "Temporal Aspect: Time Windows, Rhythm, Cadence, and Currentness"
section_id: "C.27.TA:8"
section_title: "Common Anti-Patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/C.27.TA/C.27.TA__010_common-anti-patterns.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "C.27.TA — Temporal Aspect: Time Windows, Rhythm, Cadence, and Currentness"
  - "C.27.TA:8 — Common Anti-Patterns"
line_start: 56437
line_end: 56446
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
| Cadence without bearer | "Weekly cadence" appears without saying what has the cadence. | Name the exact EntityOfConcern, cadence predicate, temporal reference, and interval; add other fields only when the receiving use needs them. |
| Freshness without window | A source is called current without reference time or validity window. | Name the exact source, current or fresh predicate, reference time or edition, and validity window; add a refresh condition only when the next use depends on it. |
| Recovery without an adequate temporal claim | A claim says "recovery improved" without an exact bearer, temporal reference, or interval. | State the four-part minimum; add a disturbance, measure, rule citation, or relation only when the receiving use depends on it. |
| Rhythm as value | A rhythm is treated as good by default. | Use the direct value, assurance, quality, or proxy pattern for those separate claims. |
| Timing as transformation | A time window is treated as if it specified the change. | Use `A.3.4` for the transformation relation and C.27.TA for the temporal aspect. |

