---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Evaluate Promise Fulfilment from Work Evidence (Service Acceptance)"
section_id: "F.12:1"
section_title: "Intent & applicability"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__002_intent-applicability.md"
commit_sha: "e307edbd91c04c1d85661bd309b9944fac251937"
heading_path:
  - "F.12 — Evaluate Promise Fulfilment from Work Evidence (Service Acceptance)"
  - "F.12:1 — Intent & applicability"
line_start: 122528
line_end: 122535
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.3"
  - "A.3.2"
  - "A.6.1"
  - "A.6.RCD"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.2"
  - "E.13"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.11"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.9"
  - "U.PromiseContent"
keywords:
  - "EvidenceStatus"
  - "PromiseContent"
  - "RequirementStatus"
  - "declared result scale"
  - "delivery Work"
  - "evaluation Work"
  - "indicator recovery"
  - "measured value"
  - "observation"
  - "operation result binding"
---

### F.12:1 - Intent & applicability

**Intent.** Relate an exact promise-content claim to the delivery Work and outcome being judged, the observations and measured values used as evidence, the relevant window and population, and application of the declared acceptance rule to those inputs. Return a result on its declared scale. Recover a separate dated evaluation Work when the claim or receiving use consumes that performance history. Map the result to F.10 status when needed, and identify a durable verdict episteme when another use needs that assertion. Keep these objects and relations distinct so a reader can see what would change the result.

**Use this when.** An SLO, SLA clause, safety margin, response-time target, quality gate, or other promise must be judged from actual occurrences.

**Do not use this when.** The question is only what the promise says, how the Method is described, or how a measurement is made. Use the direct A.2.3, A.3, A.15, or C.16 pattern. F.12 does not turn a lexical cell or comparison row into a verdict subject.

