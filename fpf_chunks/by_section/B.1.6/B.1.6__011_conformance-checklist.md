---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__011_conformance-checklist.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:7 — Conformance Checklist"
line_start: 34071
line_end: 34082
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "B.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.2-family"
  - "B.2.P"
  - "C.13"
  - "C.16"
  - "C.27"
  - "C.29"
  - "E.17"
keywords:
---

### B.1.6:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-B1.6-1 | The aggregation names dated work occurrence refs or explicitly narrows use to planned estimates. | Prevents plans and method descriptions from masquerading as performed work. |
| CC-B1.6-2 | Resource-accounting basis, units, measurement refs, evidence refs, and source refs are named. | Keeps resource values comparable and reviewable. |
| CC-B1.6-3 | Holon delimitation and any boundary-crossing relation used for accounting are named by value. | Prevents an unexplained boundary word from carrying the claim. |
| CC-B1.6-4 | Time windows, phase refs, and overlap and deduplication policy are present when slices or shared resources are aggregated. | Prevents double counting and missing epochs. |
| CC-B1.6-5 | Method, method-description, work-plan, transformation, and whole-reidentification claims use their direct owners. | Keeps work-resource aggregation from absorbing neighboring objects. |
| CC-B1.6-5a | Work-entry readiness, full-kit condition, and resource readiness before work entry use `A.15.5`; B.1.6 cites such refs only as neighboring inputs when a resource aggregation claim also exists. | Keeps planned or reserved resource availability from becoming measured performed-work aggregation. |
| CC-B1.6-6 | `Gamma_work` is used only as notation over a recovered aggregation record. | Keeps algebraic notation from becoming ontology by spelling. |

