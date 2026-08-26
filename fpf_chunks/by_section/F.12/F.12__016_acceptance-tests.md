---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Service Acceptance–Work Evidence Link"
section_id: "F.12:15"
section_title: "Acceptance tests"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__016_acceptance-tests.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "F.12 — Service Acceptance–Work Evidence Link"
  - "F.12:15 — Acceptance tests"
line_start: 94672
line_end: 94698
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

### F.12:15 - Acceptance tests

#### F.12:15.1 - Static conformance

* **SCR-F12-S01 (actual subjects).** Every evaluation names exact promise content, delivery Work or population, observations and measured values, window, and rule; cells are optional addresses only.
* **SCR-F12-S02 (scope match).** Promise, Work, evidence, population, and window align.
* **SCR-F12-S03 (evidence).** Observations concern the promised outcome of the judged Work.
* **SCR-F12-S04 (evaluation explicit).** The performing System, evaluation Work, enacted Method, exact A.6.1 application and argument and result bindings, characteristic, scale, unit, aggregation, threshold, exclusions, and declared result values are stated as needed.
* **SCR-F12-S05 (indicator boundary).** Direct measurement adds no proxy. A distinct indicator relation names exact participants and a defining or testing pattern, or the evaluation stops at A.6.RCD `missing-governor`.
* **SCR-F12-S06 (direct relations).** Promise use, delivery, fulfilment, measurement, indicator, evidence use, assurance or material reliance, evaluation, status, and any verdict assertion use their defining or testing patterns.
* **SCR-F12-S07 (result and status).** The operation result stays on its declared scale; RequirementStatus and EvidenceStatus are mapped separately, and evidence insufficiency is never implicit target falsity.
* **SCR-F12-S08 (optional episteme).** A C.2.1 verdict episteme exists only for a named later use and remains distinct from result and status.
* **SCR-F12-S09 (no generic Bridge).** F.9 is used only for a real local-meaning relation and establishes none of the other relations.
* **SCR-F12-S10 (temporal honesty).** No timeless or retroactively rewritten result or status assertion appears.

#### F.12:15.2 - Regression

* **RSCR-F12-E01 (relation update).** A changed indicator, evidence, or semantic relation affects only evaluations that depended on it.
* **RSCR-F12-E02 (edition change).** Source-local meaning remains tied to the edition used by each evaluation.
* **RSCR-F12-E03 (population drift).** New population definitions create explicit new evaluations.
* **RSCR-F12-E04 (window partition).** Weekly and monthly results and statuses remain distinct; any roll-up states its aggregation.
* **RSCR-F12-E05 (indicator retirement).** Direct measurement changes future evaluations without silently rewriting prior indicator-dependent results or assertions.

#### F.12:15.3 - Didactic distillation

> “Name the exact promise, the delivery Work it covers, the promised characteristic, the observations and measured values, and the window and population. First ask whether the measurement is direct; if another indicator stands in, name its exact relation or stop. Then name the System's evaluation Work, enacted Method, operation inputs and result, and the declared result scale. Map that result to RequirementStatus or EvidenceStatus only through the exact rule, and create a verdict episteme only when another use needs it. Plainly: met, not met, or cannot judge. Judge what happened—not the plan, the command, the word *proxy*, or the table.”

