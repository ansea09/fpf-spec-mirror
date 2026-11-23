---
chunk_kind: "child"
pattern_id: "F.12"
pattern_title: "Evaluate Promise Fulfilment from Work Evidence (Service Acceptance)"
section_id: "F.12:15"
section_title: "Acceptance tests"
source_path: "FPF-Spec.md"
output_path: "by_section/F.12/F.12__016_acceptance-tests.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "F.12 — Evaluate Promise Fulfilment from Work Evidence (Service Acceptance)"
  - "F.12:15 — Acceptance tests"
line_start: 131669
line_end: 131695
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

* **SCR-F12-S01 (actual subjects).** Identify what was owed, to whom and under which conditions. The evidence establishes the result for the delivery, occurrence or population selected by that promise. Recover observations, measured values or a particular evaluation procedure when the commissioned judgement or the terms require them.
* **SCR-F12-S02 (scope match).** Evidence covers the decision claimed. For a result about linked undertakings, establish the connection that the agreement makes material, including any separately outstanding obligation.
* **SCR-F12-S03 (evidence).** The cited grounds support the promised outcome in the conditions judged. When a measurement supplies those grounds, its observations concern that characteristic or reach it through an established indicator relation.
* **SCR-F12-S04 (evaluation explicit).** The selected inputs, applied rule, supported result, characteristic, scale, unit, aggregation, threshold and exclusions are recoverable as required by the acceptance claim. Any claimed or rule-required performing System, evaluation Work, enacted Method and exact A.6.1 application satisfy their direct admission and binding conditions.
* **SCR-F12-S05 (indicator boundary).** Direct measurement adds no proxy. For a distinct indicator, identify both participants and apply the defining or testing rule. Return A.6.RCD `missing-governor` if no such rule is available. Limit the acceptance conclusion to the evidence the rule supports.
* **SCR-F12-S06 (direct relations).** Promise use, delivery, fulfilment, measurement, indicator, evidence use, assurance or material reliance, evaluation, status, and any verdict assertion use their defining or testing patterns.
* **SCR-F12-S07 (result and status).** The operation result stays on its declared scale; RequirementStatus and EvidenceStatus are mapped separately, and evidence insufficiency is never implicit target falsity.
* **SCR-F12-S08 (optional episteme).** Identify a durable C.2.1 verdict episteme when a receiving use needs that assertion, keeping it distinct from result and status.
* **SCR-F12-S09 (no generic Bridge).** F.9 is used only for a real local-meaning relation and establishes none of the other relations.
* **SCR-F12-S10 (temporal identity).** No timeless or retroactively rewritten result or status assertion appears.

#### F.12:15.2 - Regression

* **RSCR-F12-E01 (relation update).** A changed indicator, evidence, or semantic relation affects only evaluations that depended on it.
* **RSCR-F12-E02 (edition change).** Source-local meaning remains tied to the edition used by each evaluation.
* **RSCR-F12-E03 (population drift).** New population definitions create explicit new evaluations.
* **RSCR-F12-E04 (window partition).** Weekly and monthly results and statuses remain distinct; any roll-up states its aggregation.
* **RSCR-F12-E05 (indicator retirement).** Direct measurement changes future evaluations without silently rewriting prior indicator-dependent results or assertions.

#### F.12:15.3 - Didactic distillation

> “Start with what the recipient was promised and what verdict they need. Use the evidence and rule for that outcome at the required scope. When the result depends on measurements, first ask whether they directly concern the promised characteristic; if another indicator stands in, establish its relation or leave that basis unresolved. Apply the acceptance rule to its inputs and return the supported result on its declared scale. Recover an evaluation-Work or exact application identity when the claim or rule needs it. Use the acceptance result to assign RequirementStatus when its rule applies. Assess EvidenceStatus from the evidence for the stated use. Identify a durable verdict assertion when another use needs one. Plainly: met, not met, or cannot judge.”

