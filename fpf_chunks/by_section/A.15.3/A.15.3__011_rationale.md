---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__011_rationale.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:10 — Rationale"
line_start: 24883
line_end: 24888
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "U.WorkPlan"
keywords:
  - "WorkPlan claim content"
  - "actual-use predicate"
  - "baseline replay"
  - "concrete RefKind and policy"
  - "direct owner"
  - "edition pin"
  - "exact declaration member"
  - "intended-performance designator"
  - "no actuality by plan"
  - "open-world omission"
  - "participant/argument/result meaning"
  - "positive planned designation"
  - "semantic cardinality"
---

### A.15.3:10 - Rationale

Planning needs a way to preserve intended values without turning every planning field into ontology. Existing `RelationSignature` SlotSpecs, A.6.1 operation declarations, and other declarations already define reusable member meanings and actual-use predicates. A.15.3 records only the intended use of those members inside one WorkPlan.

The split is concrete: the declaration pattern defines the member and actual-use rule; A.6.5 or A.6.1 defines its declaration form; the WorkPlan remains one C.2.1 episteme whose A.15.2/A.15.3 content records the intention; and later Work, applications, relation occurrences, results, and comparisons are identified separately. A row cites these objects for planning but constitutes none of them.

