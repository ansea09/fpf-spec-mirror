---
chunk_kind: "child"
pattern_id: "C.26.3"
pattern_title: "Viability-Envelope Boundary Regulation"
section_id: "C.26.3:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.3/C.26.3__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "C.26.3 — Viability-Envelope Boundary Regulation"
  - "C.26.3:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 49743
line_end: 49753
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
| Markov-blanket collapse | A statistical separation, physical interface, interface module, functional element, component, boundary description, and agency threshold are all called the Markov blanket. | Split the source phrase through `A.6.RSIR`: use `C.29` or `C.26` for lens use; use `A.1` plus the direct relation owner for holon delimitation or boundary crossing; use `A.6.P`, `A.6.0`, and `A.6.5` for relation, signature, or slot claims; use `A.6.M` for module-interface claims; use `A.6.F` for functional claims; use `A.14`, `C.13`, or `B.3.5` for component claims; use `C.30.AD` or `E.17` for descriptions; use `A.13`, `A.19`, or `C.16` for agency-threshold claims. |

