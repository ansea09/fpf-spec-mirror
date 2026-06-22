---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:17"
section_title: "Acceptance tests"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__021_acceptance-tests.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:17 — Acceptance tests"
line_start: 78799
line_end: 78817
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.10.D1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:17 - Acceptance tests

#### F.9:17.1 - Static conformance

* **SCR-F9-S01 (Well-typed).** Every Bridge names two `SenseCells`, each bound to a context from F.1, and states `senseFamily`, kind, direction when needed, `CL`, Loss Notes, and admitted use.
* **SCR-F9-S02 (senseFamily discipline).** Any substitution Bridge preserves `senseFamily` and uses Equivalence, Narrower-than, or Broader-than.
* **SCR-F9-S03 (Loss visibility).** Every Bridge has non-empty Loss Notes. "None" is valid only with `CL = 3` and stated invariants.
* **SCR-F9-S04 (Counter-example hygiene).** Bridges with `CL <= 2` carry at least one counter-example or boundary case; Bridges with `CL = 3` cite invariants.
* **SCR-F9-S05 (Row compliance).** Every Concept-Set row shows an admitted use no greater than the weakest participating Bridge.
* **SCR-F9-S06 (Role boundary).** Any role-facing Bridge states that role assignment and performed-work attribution remain with A.2.1, F.6, and A.15.1.

#### F.9:17.2 - Regression checks

* **RSCR-F9-E01 (Edition churn).** When a context edition changes, revalidate all Bridges touching it.
* **RSCR-F9-E02 (Counter-example drift).** New counter-examples lower `CL`; deleting examples does not automatically raise it.
* **RSCR-F9-E03 (senseFamily drift).** If a cell's `senseFamily` changes, all Bridges crossing that cell are retyped.
* **RSCR-F9-E04 (Weakest-link enforcement).** Adding a lower-CL Bridge to a row lowers the row's admitted use or forces a split.
* **RSCR-F9-E05 (Role-boundary preservation).** No Bridge revision creates a `U.RoleAssignment` or performed-work attribution without the direct governing pattern.

