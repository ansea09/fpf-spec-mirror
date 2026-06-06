---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:16"
section_title: "Acceptance tests (SCR/RSCR — concept-level)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__018_acceptance-tests-scr-rscr-concept-level.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:16 — Acceptance tests (SCR/RSCR — concept-level)"
line_start: 71176
line_end: 71192
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "B.3"
  - "C.16.Q"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "E.10.D1"
  - "E.17.1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.Mechanism"
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

### F.9:16 - Acceptance tests (SCR/RSCR — concept-level)

#### F.9:16.1 - Static conformance (SCR)

* **SCR-F9-S01 (Well-typed).** Every Bridge names **two SenseCells**, each bound to a **Context** from F.1, and states **senseFamily**, **kind**, **dir** (if needed), **CL**, **Loss**, and **scope**.
* **SCR-F9-S02 (senseFamily discipline).** Any Bridge that supports **Role/Enactment-eligible** substitution is **senseFamily-preserving** and has kind in {`Equivalence`, `Narrower-than`, `Broader-than`}.
* **SCR-F9-S03 (Loss visibility).** Every Bridge has **non-empty Loss Notes** (the word "none" is valid only with **CL=3** and stated invariants).
* **SCR-F9-S04 (Counter-example hygiene).** Bridges with **CL <= 2** carry at least one **counter-example**; Bridges with **CL=3** cite **matching invariants**.
* **SCR-F9-S05 (Row compliance).** Every Concept-Set row shows a **scope** no greater than the **minimum CL** across its supporting Bridges; no row relies on **Interpretation** Bridges.

#### F.9:16.2 - Regression (RSCR)

* **RSCR-F9-E01 (Edition churn).** When a Context's edition changes, re-validate all Bridges touching it; flag `CL` drift and update rows' scopes if needed.
* **RSCR-F9-E02 (Counter-example drift).** New counter-examples lower **CL**; deletions do not automatically raise **CL**.
* **RSCR-F9-E03 (senseFamily drift).** If a Cell's `senseFamily` is corrected, all Bridges crossing that Cell are re-typed; any substitution that would now cross senseFamilies is invalidated.
* **RSCR-F9-E04 (Weakest-link enforcement).** Adding a low-CL Bridge to a row reduces the row's scope; if the row's published scope would exceed the new minimum, split or downgrade the row.

