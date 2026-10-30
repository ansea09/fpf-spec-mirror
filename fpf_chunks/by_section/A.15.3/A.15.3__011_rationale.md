---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem: Plan a Value for an Existing Declaration Member"
section_id: "A.15.3:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__011_rationale.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem: Plan a Value for an Existing Declaration Member"
  - "A.15.3:10 — Rationale"
line_start: 30308
line_end: 30313
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

The split is concrete: the declaration pattern defines member meaning and actual-use rule; A.6.5 or A.6.1 defines the applicable declaration form; the WorkPlan records intention under C.2.1 and A.15.2. Establish a later application, relation occurrence, result or comparison under its own predicate. Identify dated Work only when its occurrence is claimed. The planning row supplies none of those actual-use facts by itself.

