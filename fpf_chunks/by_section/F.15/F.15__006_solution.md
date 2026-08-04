---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__006_solution.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:4 — Solution"
line_start: 94643
line_end: 94651
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

Both families are F.15-local check declarations over already governed objects. Actual check application uses A.6.1 bindings and, when performed work is claimed, A.15.1. C.2.1 independently constitutes result claims and the optional conformance-record episteme. A.10/B.3 govern reliance, E.24.PUB governs availability, and G.11 governs currentness.

