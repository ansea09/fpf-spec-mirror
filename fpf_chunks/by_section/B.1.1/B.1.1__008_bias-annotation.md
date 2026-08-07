---
chunk_kind: "child"
pattern_id: "B.1.1"
pattern_title: "Dependency Structure and Relation Grounding"
section_id: "B.1.1:5.1"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.1/B.1.1__008_bias-annotation.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "B.1.1 — Dependency Structure and Relation Grounding"
  - "B.1.1:5.1 — Bias-Annotation"
line_start: 35632
line_end: 35640
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

### B.1.1:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Graph as ontology | A graph node or edge is treated as the in-life object or relation. | Recover the dependency structure and direct relation owners before graph expression. |
| One-edge-fits-all | `depends on` carries parthood, order, representation, source use, evidence, and influence at once. | Split relation kinds and assign direct owners. |
| External influence as parthood | Supply, measurement, teaching, source use, or control is drawn as a component relation. | Use boundary-crossing, evidence, source-use, publication-use, transformation, or direct relation owner. |
| Design-description and run-occurrence collapse | A planned dependency graph is treated as evidence of performed work. | Separate design description, work occurrence, and evidence relations. |

