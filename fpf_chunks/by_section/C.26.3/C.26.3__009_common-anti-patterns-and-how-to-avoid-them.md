---
chunk_kind: "child"
pattern_id: "C.26.3"
pattern_title: "Viability-Envelope Boundary Regulation"
section_id: "C.26.3:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.3/C.26.3__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.26.3 — Viability-Envelope Boundary Regulation"
  - "C.26.3:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 69935
line_end: 69963
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
| One metric as viability | Availability, latency, or score stands for the whole envelope. | Add the viability bearer and the pattern used to identify it, protected promise, other dimensions, and failure mode. |
| Fixed setpoint thinking | Stability means one variable must never move. | Ask whether allostasis preserves function by changing settings, environment, boundary, or regime. |
| Passive sensor assumption | A dashboard is treated as neutral even after it changes behavior. | Use `C.26.1` when the false passive reading changes the architecture decision; use evidence patterns for its support. |
| Candidate intervention without a recovered object, predicate, or applicable authority | The text recommends a change without recovering its proposal-side Method, description, setting proposal, WorkPlan, access or permission claim, or Bridge proposal or description; fails to identify separately any dated Work, actual transformation, obtaining relation occurrence, or resulting state on which it relies; or claims Work no system can perform in time. | Recover the proposal-side object first; identify every actuality separately under its subject pattern; state authority and latency only for the applicable Work, change, or relation. |
| Biological proof jump | Homeostasis or FEP language is used as proof for software or organizations. | Treat it as modeling discipline and apply existing FPF patterns to claims. |
| Markov-blanket collapse | A statistical separation, physical interface, interface module, functional element, component, boundary description, and agency threshold are all called the Markov blanket. | Split the source phrase through `A.6.RSIR` using the routes below. |

**Markov-blanket routes:**

| Pattern | Claim or use |
| --- | --- |
| `C.29` or `C.26` | Lens use. |
| `A.1` plus the direct relation pattern | Holon delimitation or boundary crossing. |
| `A.6.P`, `A.6.0`, and `A.6.5` | Relation, signature, or slot claims. |
| `A.6.M` | Module-interface claims. |
| `A.6.F` | Functional claims. |
| `A.14`, `C.13`, or `B.3.5` | Component claims. |
| `C.2.1` | Description content. |
| `C.30.AD` | Architecture descriptions. |
| `E.24.PUB` | A publication occurrence or form. |
| `E.17` | Multi-view publication when it is current. |
| `A.13` | Agency criteria. |
| `C.16` | Measurement construction. |
| `A.19` | A `CharacteristicSpace` or reusable `CharacteristicSpacePredicate` over it. |

