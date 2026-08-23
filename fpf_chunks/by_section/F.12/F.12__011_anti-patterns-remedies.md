---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:10"
section_title: "Anti-patterns & remedies"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__011_anti-patterns-remedies.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:10 — Anti-patterns & remedies"
line_start: 93531
line_end: 93548
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

### F.12:10 - Anti-patterns & remedies

| # | Anti-pattern | Symptom | Why harmful | Remedy |
| --- | --- | --- | --- | --- |
| **A1** | Plan as proof | A diagram or runbook is cited as acceptance evidence. | Description replaces occurrence and outcome. | Name Work and observations of its outcome. |
| **A2** | Output as outcome | Setpoint writes or commands prove service delivery. | Intended influence replaces observed result. | Use observations and measurement that directly concern the promised characteristic; if a distinct indicator relation is needed, define or test it and state its loss. |
| **A3** | Cell as subject | ClauseCell, WorkCell, or MeasureCell bears the result or status. | Lexical address replaces promise, Work, evaluation, and evidence. | Cite the actual values; retain a cell only as an address. |
| **A4** | Generic Bridge | One Bridge is claimed to connect promise, Work, measure, indicator, result, and status. | Several distinct relations disappear. | Use A.2.3 for promise-side relations, C.16 for measurement, the defining or testing pattern for an indicator relation, A.10 for evidence use, A.15.1 and A.6.1 for evaluation, F.10 for status, and F.9 only for local-meaning relations. |
| **A5** | Windowless result | “We met the SLA” has no period, population, evaluation Work, or applied rule. | The claim cannot be replayed. | State window, population, evaluation Work, application, result binding, and declared scale. |
| **A6** | Percentile mirage | Annual pooled p95 is used for a monthly promise. | Aggregation and promise scope differ. | Evaluate within the promise’s exact window and population. |
| **A7** | Proxy by label | Synthetic probes equal user experience because they are called a proxy. | The text skips the direct-measurement question and any actual indicator relation. | First test whether C.16 already measures the promised characteristic. If not, name both indicator participants and its defining or testing pattern; use C.16.P and return `missing-governor` when absent. |
| **A8** | Work mismatch | Evidence concerns another product, region, or occurrence. | The result is about the wrong subject. | Match every observation to the judged Work or population. |
| **A9** | Silent units | “Latency ≤ 120” omits scale or unit. | The threshold is ambiguous. | State characteristic, scale, unit, and conversion basis. |
| **A10** | Hidden aggregation | A global result rests on a subset with no rule. | Evidence scope is overstated. | State the aggregation or confine the result. |
| **A11** | Status on umbrella | “The service is Satisfied.” | Promise content, delivery Work, evaluation result, target clause, window, and F.10 status use disappear. | Recover the direct result first, then state the exact RequirementStatus use only if its rule applies. |
| **A12** | Retroactive renorming | A new monitor silently rewrites old results and status assertions. | Historical claims lose identity. | Preserve old basis; issue a new evaluation when authorised. |
| **A13** | Universal trichotomy | Every evaluation returns Satisfied, Violated, or Inconclusive. | RequirementStatus, EvidenceStatus, and the acceptance specification's own result scale collapse. | Use the declared result scale; map to F.10 status separately, and use a plain “met, not met, or cannot judge” summary only as a rendering. |

