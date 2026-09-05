---
chunk_kind: "child"
pattern_id: "C.26.3"
pattern_title: "Viability-Envelope Boundary Regulation"
section_id: "C.26.3:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.3/C.26.3__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "C.26.3 — Viability-Envelope Boundary Regulation"
  - "C.26.3:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 55657
line_end: 55667
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
| One metric as viability | Availability, latency, or score stands for the whole envelope. | Add the exact object filling the local viability-bearer position and the pattern used to identify it, protected promise, other dimensions, and failure mode. |
| Fixed setpoint thinking | Stability means one variable must never move. | Ask whether allostasis preserves function by changing settings, environment, boundary, or regime. |
| Passive sensor assumption | A dashboard is treated as neutral even after it changes behavior. | Use `C.26.1` when the false passive reading changes the architecture decision; use evidence patterns for its support. |
| Candidate intervention without a recovered object, predicate, or applicable authority | The text recommends a change without recovering its proposal-side Method, description, setting proposal, WorkPlan, access or permission claim, or Bridge proposal or description; fails to identify separately any dated Work, actual transformation, obtaining relation occurrence, or resulting state on which it relies; or claims Work no system can perform in time. | Recover the proposal-side object first; identify every actuality separately under its subject pattern; state authority and latency only for the applicable Work, change, or relation. |
| Biological proof jump | Homeostasis or FEP language is used as proof for software or organizations. | Treat it as modeling discipline and apply existing FPF patterns to claims. |
| Markov-blanket collapse | A statistical separation, physical interface, interface module, functional element, component, boundary description, and agency threshold are all called the Markov blanket. | Split the source phrase through `A.6.RSIR`: use `C.29` or `C.26` for lens use; use `A.1` plus the direct relation pattern for holon delimitation or boundary crossing; use `A.6.P`, `A.6.0`, and `A.6.5` for relation, signature, or slot claims; use `A.6.M` for module-interface claims; use `A.6.F` for functional claims; use `A.14`, `C.13`, or `B.3.5` for component claims; use `C.2.1` for description content, `C.30.AD` for architecture descriptions, and `E.17` for reader-facing publication of an accepted account; use `A.13` for agency criteria, `C.16` for measurement construction, and `A.19` for a `CharacteristicSpace` or reusable `CharacteristicSpacePredicate` over it. |

