---
chunk_kind: "child"
pattern_id: "C.26.3"
pattern_title: "Viability-Envelope Boundary Regulation"
section_id: "C.26.3:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.3/C.26.3__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "C.26.3 — Viability-Envelope Boundary Regulation"
  - "C.26.3:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 45010
line_end: 45020
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

### C.26.3:8 - Common Anti-Patterns and How to Avoid Them


| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| One metric as viability | Availability, latency, or score stands for the whole envelope. | Add the bearer, protected promise, other dimensions, and failure mode. |
| Fixed setpoint thinking | Stability means one variable must never move. | Ask whether allostasis preserves function by changing settings, environment, boundary, or regime. |
| Passive sensor assumption | A dashboard is treated as neutral even after it changes behavior. | Use `C.26.1` and evidence patterns. |
| Actuator without authority | The text recommends a change no one can enact in time. | State actuator authority and latency. |
| Biological proof jump | Homeostasis or FEP language is used as proof for software or organizations. | Treat it as modeling discipline and apply existing FPF patterns to claims. |

