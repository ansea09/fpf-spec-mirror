---
chunk_kind: "child"
pattern_id: "A.3.4"
pattern_title: "U.Transformation: Bounded Change Under Conditions"
section_id: "A.3.4:8"
section_title: "Common Anti-Patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4/A.3.4__010_common-anti-patterns.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.3.4 — U.Transformation: Bounded Change Under Conditions"
  - "A.3.4:8 — Common Anti-Patterns"
line_start: 7394
line_end: 7404
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.F"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.30.ASV"
  - "E.18"
  - "E.18.1"
  - "E.18.2"
  - "E.20"
  - "E.24"
keywords:
  - "bounded change"
  - "functioning"
  - "input/output conditions"
  - "transformation"
  - "transformation-flow structure"
  - "transformed entity"
  - "transformer"
---

### A.3.4:8 - Common Anti-Patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Method name as change | "This method transforms X" with no transformed object, condition, or delta. | Identify `TransformationCore`; keep the method in the method slot. |
| Process diagram as work | A workflow diagram is treated as enacted work. | Use `E.18` or `A.3.2` for the diagram; use `A.15.1` for dated work. |
| Dynamics model as permission | A transition law is used to approve action. | Keep `A.3.3` for the model; use evidence, gate, decision, and assurance patterns for use authority. |
| Temporal trend as intervention | A rate or rhythm trend is treated as proof of changed behavior under an intervention. | Use `C.27.TA` for the temporal aspect, `C.27` for temporal-claim adequacy, and name the transformation relation separately. |
| Formal construction as work | A morphism or proof construction is treated as work performed in a project-world object. | Use `C.29` or the direct formal pattern for the mathematical relation; name realization and work separately. |
| Publication as transformation | A dashboard or report is treated as the changed state. | Use publication or source patterns for the publication; keep the transformation as the governed object. |

