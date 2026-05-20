---
chunk_kind: "child"
pattern_id: "F.7"
pattern_title: "Concept‑Set Table"
section_id: "F.7:9"
section_title: "Micro‑illustrations (safe patterns)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.7/F.7__010_micro-illustrations-safe-patterns.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "F.7 — Concept‑Set Table"
  - "F.7:9 — Micro‑illustrations (safe patterns)"
line_start: 62610
line_end: 62632
dependencies:
  - "A.6.9"
  - "E.10.D1"
  - "F.0.1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "columns"
  - "comparisons"
  - "concept-set"
  - "differences"
  - "row"
  - "table"
---

### F.7:9 - Micro‑illustrations (safe patterns)

> Illustrative only; these presume corresponding **F.9 Bridges** exist with stated CL and losses.

**(a) Subtyping across type‑formalisms (Type‑structure row)**

| FPF Label                                  | Row Scope      | Row CL(min) | OWL 2             | Kind-CAL            | Rationale                                                        | Counter‑examples                                                         |
| ------------------------------------------ | -------------- | ----------- | ----------------- | ------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **is‑a (Tech)** / *type hierarchy* (Plain) | Type‑structure | CL = 3      | `rdfs:subClassOf` | `U.SubtypeRelation` | Both are partial‑order *class* subsumption used for inheritance. | FCA *concept* order is not a class subsumption; keep it out or CL drops. |

**(b) “Observation result value” (Measurement row)**

| FPF Label                           | Row Scope | Row CL(min) | SOSA/SSN                | ISO 80000‑1                    | ITIL 4                       | Rationale                                                                                           | Counter‑examples                                                |
| ----------------------------------- | --------- | ----------- | ----------------------- | ------------------------------ | ---------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **result‑value** / *measured value* | KD‑metric | CL = 2      | `sosa:Result` (literal) | `QuantityValue` (unit‑bearing) | *metric value* (service KPI) | Values can be read as numbers tied to a Characteristic; ITIL metric uses same notion when unitised. | ITIL “metric” may be composite indices (loss of unit fidelity). |

**(c) Contrast row: “process” (no sameness)**

| FPF Label              | Row Scope | Row CL(min) | BPMN 2.0              | PROV‑O                  | Thermodynamics           | Rationale                                                 | Counter‑examples                                                                   |
| ---------------------- | --------- | ----------- | --------------------- | ----------------------- | ------------------------ | --------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **process** (contrast) | —         | —           | *graph of flow nodes* | *time‑bounded activity* | *state‑space trajectory* | Same surface, **different** senses; no licensed sameness. | Any attempt to equate design‑graph with run‑occurrence fails stance compatibility. |


