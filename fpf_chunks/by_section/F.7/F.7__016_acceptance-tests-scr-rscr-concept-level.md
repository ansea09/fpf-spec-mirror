---
chunk_kind: "child"
pattern_id: "F.7"
pattern_title: "Concept‑Set Table"
section_id: "F.7:15"
section_title: "Acceptance tests (SCR/RSCR — concept‑level)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.7/F.7__016_acceptance-tests-scr-rscr-concept-level.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "F.7 — Concept‑Set Table"
  - "F.7:15 — Acceptance tests (SCR/RSCR — concept‑level)"
line_start: 88545
line_end: 88562
dependencies:
  - "A.6.9"
  - "E.10.D1"
  - "F.0.1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "columns"
  - "comparisons"
  - "concept-set"
  - "differences"
  - "row"
  - "table"
---

### F.7:15 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.7:15.1 - Static conformance checks (SCR)

* **SCR‑F7‑S01 (Context‑loyal cells).** Every non‑empty cell references an existing **SenseCell** (F.3) in a declared Context (F.1).
* **SCR‑F7‑S02 (Closure & bottleneck).** For each Concept‑Set row, **every pair** of cells has a Bridge path with CL ≥ **Row CL(min)** printed; **Row CL(min)** equals the **minimum** pairwise CL.
* **SCR‑F7‑S03 (Typed & scoped).** Each row declares a **Row Scope** from the controlled set and is **senseFamily‑uniform** (Role **or** Status **or** Measurement **or** Type‑structure…).
* **SCR‑F7‑S04 (Temporal compatibility).** Non‑contrast rows have **compatible** DesignRunTag across cells.
* **SCR‑F7‑S05 (Loss disclosure).** If any supporting Bridge has a recorded loss, the row includes **≥1 counter‑example** line.
* **SCR‑F7‑S06 (Parsimony).** Rows contain **2–4 Contexts** unless a one‑line necessity is stated for each extra Context.

#### F.7:15.2 - Regression checks (RSCR)

* **RSCR‑F7‑E01 (Bridge drift).** After any Bridge change (F.9), recompute **Row CL(min)**; flag rows whose scope is now overstated.
* **RSCR‑F7‑E02 (Sense split).** After a SenseCell splits (F.3), ensure rows referencing it either pick a child cell or retire.
* **RSCR‑F7‑E03 (Scope integrity).** No consumer pattern uses a row outside its declared **Row Scope**.
* **RSCR‑F7‑E04 (No stealth growth).** Additions of cells never lower **Row CL(min)** silently; if they do, either split the row or reduce scope.

