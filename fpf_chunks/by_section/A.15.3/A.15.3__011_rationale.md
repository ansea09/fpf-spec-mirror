---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__011_rationale.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:10 — Rationale"
line_start: 25355
line_end: 25360
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

Planning needs a way to preserve intended values without turning every planning field into ontology. RelationSignature SlotSpecs, A.6.1 operation declarations, and other direct declarations already supply reusable member meanings and corresponding later actual-use predicates. A.15.3 contributes only the positive intended use of those members in one WorkPlan.

This split preserves four authorities and identities: the target direct pattern owns the reusable member meaning and actual-use predicate; A.6.5 or A.6.1 owns the relevant declaration discipline; the WorkPlan remains one C.2.1 episteme whose A.15.2/A.15.3 claim content states the intention; and any later Work, application binding, relation occurrence, result, or comparison is independently identified. A row reference connects those objects for planning but constitutes none of them.

