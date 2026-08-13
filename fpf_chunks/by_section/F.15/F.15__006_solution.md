---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__006_solution.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:4 — Solution"
line_start: 95850
line_end: 95862
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.6"
  - "A.2.7"
  - "A.22"
  - "A.6.1"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.24.PUB"
  - "F.1-F.14"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.6"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:4 - Solution

The harness has two rule families:

1. **Static Conformance Rules (SCR).** Check exact current object and relation refs in one finite slice version. A rule result is a separately constituted claim, not a field value that becomes true because a record is filled.
2. **Regression and Stability Conformance Rules (RSCR).** Compare exact earlier and later refs for the changed member only. State the governed continuity or change claim, admitted losses, evidence, and receiving use; changed spelling or edition alone proves neither sameness nor difference.

Both families are F.15-local check declarations over already defined objects. A practitioner may apply their questions and obtain a local result without naming the checking activity as Tech `U.Work`. An exact rule application, when its identity is needed, uses A.6.1.

If a replayable result or example asserts dated assessment `U.Work`, point to its complete A.15.1/F.6 basis. A short record may omit only an assignment identifier unused by its receiving claim. Name the A.6.1 application and bindings when that application is also asserted.

C.2.1 separately constitutes the result claims and optional conformance-record episteme. A.10 and B.3 supply evidence-reliance and assurance rules; E.24.PUB supplies publication rules; G.11 supplies currentness rules.

