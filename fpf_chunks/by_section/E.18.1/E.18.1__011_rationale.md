---
chunk_kind: "child"
pattern_id: "E.18.1"
pattern_title: "Principles-to-Work Carry-Through"
section_id: "E.18.1:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.1/E.18.1__011_rationale.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "E.18.1 — Principles-to-Work Carry-Through"
  - "E.18.1:10 — Rationale"
line_start: 77979
line_end: 77984
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.20"
  - "A.21"
  - "A.6.0"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.22.2"
  - "C.29"
  - "E.10"
  - "E.11.PUR"
  - "E.17"
  - "E.18"
  - "E.19"
  - "F.9"
  - "U.Mechanism"
  - "U.Signature"
keywords:
  - "P2W"
  - "accepted ProblemCard@Context"
  - "carry-through record"
  - "evaluation refresh"
  - "formal substrate"
  - "mechanism realization"
  - "method-family selection"
  - "principles-to-work"
  - "work planning"
---

### E.18.1:10 - Rationale

`E.18.1` is a child of `E.18` because P2W uses a transformation-flow structure as its setting when the carry-through relation spans several transformation-flow slices, loci, or returns. It does not define graph semantics or prescribe performed-work order. It defines a local carry-through pattern for turning accepted problem-side records into a next FPF use whose governing relation is named.

The design puts the positive carry-through table first because repeated negative distinction sets can make a pattern whose primary EntityOfConcern is P2W behave like reference policing. P2W needs precision, but precision is useful here only when it leaves a surviving action: write the carry-through record, recover the FPF kind or relation, use the governed record, stop, split, or return.

