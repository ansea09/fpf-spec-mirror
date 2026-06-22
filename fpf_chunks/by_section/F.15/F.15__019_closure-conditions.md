---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:15"
section_title: "Closure conditions"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__019_closure-conditions.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:15 — Closure conditions"
line_start: 81033
line_end: 81044
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "B.3"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "F.1"
  - "F.1-F.14"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
  - "U.Role"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:15 - Closure conditions

A unification slice is locally admissible for reuse when:

1. every triggered static conformance rule holds for the current snapshot;
2. every changed moving part has a regression result;
3. each failed rule names the direct governing pattern before reuse;
4. at least one witness exists for each live Bridge, row, RoleDescription rename, status-window change, or public naming change;
5. the record names tempting non-admitted uses such as role assignment, performed-work attribution, source authority, publication authority, status transfer, and evidence use.

Closure is local to the slice and current use. A later context edition, row change, Bridge endpoint change, RoleDescription change, public-name change, or status-window change reopens the relevant RSCR rows.

