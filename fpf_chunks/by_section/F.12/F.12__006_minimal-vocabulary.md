---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:5"
section_title: "Minimal vocabulary"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__006_minimal-vocabulary.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:5 — Minimal vocabulary"
line_start: 96252
line_end: 96266
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

### F.12:5 - Minimal vocabulary

* **Promise-content claim** — the exact `U.PromiseContent` under A.2.3, including its subject, scope, target, and conditions.
* **Work** — the actual dated `U.Work` occurrence, or an explicitly defined population of Work occurrences, being judged.
* **Observation** — the actual observation occurrence and its result under C.2 and C.16.
* **Measured value** — a value for a named characteristic on an explicit scale and unit.
* **Window** — the time, batch, episode, phase, or other bounded evaluation interval under F.10.
* **Evaluation Work** — the dated Work in which a System enacts the evaluation Method over the selected facts and states.
* **Evaluation application and result** — the A.6.1 operation application with exact argument bindings and a result value on the acceptance specification's declared scale.
* **Evaluation rule and result scale** — the stated comparison or aggregation and its declared admissible results. Boolean, trichotomous, graded, `N/A`, and `Inconclusive`-including scales are examples, not defaults.
* **Status use** — a separate F.10 application of an exact EvidenceStatus or RequirementStatus value to its exact target, scope, window, and use after the direct result is recovered.
* **Verdict episteme** — an optional C.2.1 episteme that states the evaluation result or status when another use needs a durable assertion; it is not the operation result or the fulfilment relation.
* **Indicator or proxy relation** — only a separately defined or tested relation in which one observed characteristic or result stands in for another subject or outcome for this use, with exact participants, coverage, and loss. The word *proxy* does not create it.
* **Evidence use and reliance** — an A.10 evidence-use relation and, only for assurance or material reliance, the B.3 branch. Neither creates an indicator relation or the acceptance result.

