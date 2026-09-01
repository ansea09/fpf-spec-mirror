---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:1"
section_title: "Intent & applicability"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__002_intent-applicability.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:1 — Intent & applicability"
line_start: 96531
line_end: 96538
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

**Intent.** Relate an exact promise-content claim to the delivery Work and outcome being judged, the observations and measured values used as evidence, an explicit window and population, and the separate evaluation Work that applies the declared acceptance rule and returns a result on its declared scale. Map that result to F.10 status only when a receiving use needs status, and create a verdict episteme only when another use needs a durable assertion. Keep each object and relation distinct so a reader can see what would change the result.

**Use this when.** An SLO, SLA clause, safety margin, response-time target, quality gate, or other promise must be judged from actual occurrences.

**Do not use this when.** The question is only what the promise says, how the Method is described, or how a measurement is made. Use the direct A.2.3, A.3, A.15, or C.16 pattern. F.12 does not turn a lexical cell or comparison row into a verdict subject.

