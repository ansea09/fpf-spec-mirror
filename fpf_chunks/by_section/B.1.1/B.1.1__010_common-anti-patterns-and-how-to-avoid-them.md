---
chunk_kind: "child"
pattern_id: "B.1.1"
pattern_title: "Dependency Structure and Relation Grounding"
section_id: "B.1.1:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.1/B.1.1__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "B.1.1 — Dependency Structure and Relation Grounding"
  - "B.1.1:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 35757
line_end: 35766
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15.1"
  - "A.22"
  - "A.6.5"
  - "B.1"
  - "B.1.4"
  - "B.3.5"
  - "C.13"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.AD.BA"
keywords:
---

### B.1.1:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| DependencyGraph as ontology | The graph is treated as the thing being built. | Name the dependency structure and relation owners first. |
| External supplier as part | A supplier or infrastructure system is drawn inside the product. | Use a boundary-crossing relation, supply relation, commitment relation, A.6.C contract-language unpacking, evidence relation, publication-use relation, source-use relation, or another direct owner; use parthood only for admitted parts. |
| Mapping as parthood | A model, dashboard, or digital twin is a node inside the asset. | Use representation, publication, architecture-description, or evidence owners. |
| Order as component | A subsequent step is represented as a component of an earlier step. | Use order, method, or work occurrence owners. |
| Acyclicity as adequacy | The graph has no cycles, so the model is accepted. | Check whether the selected relation is grounded and whether graph checks answer the current concern. |

