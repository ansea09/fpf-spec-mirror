---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:5"
section_title: "Minimal vocabulary"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__007_minimal-vocabulary.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:5 — Minimal vocabulary"
line_start: 92791
line_end: 92800
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

### F.15:5 - Minimal vocabulary

* **Unification slice** - the small set of contexts, senses, rows, RoleDescriptions, bridges, windows, aliases, and names being checked together.
* **Static Conformance Rule (SCR)** - a check that must hold in the current snapshot.
* **Regression and Stability Conformance Rule (RSCR)** - a check that compares an earlier and later snapshot.
* **Check claim** - one content assertion such as "this row spans two contexts" or "this RoleDescription refers to one SenseCell".
* **Witness** - one small example, counterexample, invariant, or edition note that makes the check inspectable.
* **Moving part** - any context, local sense, row, role-description label, bridge, status window, alias, or public name whose change could affect the slice.
* **Failed conformance** - a check result that makes the claim governed by the direct pattern before reuse.

