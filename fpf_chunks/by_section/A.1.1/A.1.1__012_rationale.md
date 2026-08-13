---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "Bounded Model-Use Structure and DDD Bounded-Context Recovery"
section_id: "A.1.1:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__012_rationale.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "A.1.1 — Bounded Model-Use Structure and DDD Bounded-Context Recovery"
  - "A.1.1:10 — Rationale"
line_start: 2236
line_end: 2241
dependencies:
  - "A.1"
  - "A.14"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.22"
  - "A.3.1"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.17.0"
  - "E.24.PUB"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
---

### A.1.1:10 - Rationale

The selected object must survive two decisive tests. One subsystem under two models needs two bounded contexts without duplicating the subsystem. One model coherently used across several loci may need one bounded context without pretending those loci are parts of another whole. A dependent `U.Structure` over exact relations passes both tests.

The practical DDD lesson retained here is that boundaries matter because model applicability, actual use, expression consistency, and relationships can change engineering decisions. FPF does not copy that sentence as one ontology: it separates participant-determined fixed-content coherence from maintenance Work, identifies each bounded model-use structure without crossings, and includes an independently obtaining crossing only as a selected relation occurrence in a distinct A.22 structure over already identified endpoints.

