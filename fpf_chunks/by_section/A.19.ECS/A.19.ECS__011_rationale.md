---
chunk_kind: "child"
pattern_id: "A.19.ECS"
pattern_title: "Evaluation CharacteristicSpace Construction"
section_id: "A.19.ECS:9"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ECS/A.19.ECS__011_rationale.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "A.19.ECS — Evaluation CharacteristicSpace Construction"
  - "A.19.ECS:9 — Rationale"
line_start: 28551
line_end: 28556
dependencies:
  - "A.17-A.19"
  - "C.16"
  - "C.25"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8.ECSPF"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### A.19.ECS:9 - Rationale

Improvement cannot be better than its evaluation. A loop that changes an object version without a declared characteristic space can only produce activity, persuasion, or evaluator preference. An evaluation that lists scales without evaluated-object-kind discrimination, floor, evidence, missingness, trade-offs, and stop meanings cannot guide improvement safely.

Placing this method under `A.19` keeps the ontology clean. `A.19` governs the structure of `CharacteristicSpace`; `A.19.ECS` governs the construction method for evaluations of declared EntityOfConcern kinds and uses. `A.19.ECS` governs the selected characteristics, scales, coordinate construction, and evaluation-use boundaries of the evaluation characteristic space, not its publication or record form. An FPF pattern is only one possible publication form when the evaluation belongs in FPF; a local rubric, standard, table, or project rule is enough when the use is local. `E.23` stays a universal loop method because it does not need to know how every domain chooses its scales. Domain and FPF-specific evaluations such as `E.21`, `E.9.DA`, `E.2.DA`, and `F.18` keep coordinate choices inside those evaluations.

