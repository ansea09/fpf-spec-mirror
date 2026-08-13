---
chunk_kind: "child"
pattern_id: "F.13"
pattern_title: "Lexical Continuity & Deprecation"
section_id: "F.13:15"
section_title: "Acceptance tests (SCR/RSCR — concept‑level)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.13/F.13__016_acceptance-tests-scr-rscr-concept-level.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "F.13 — Lexical Continuity & Deprecation"
  - "F.13:15 — Acceptance tests (SCR/RSCR — concept‑level)"
line_start: 95441
line_end: 95458
dependencies:
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "deprecation"
  - "evolution"
  - "merging terms"
  - "renaming"
  - "splitting terms"
---

### F.13:15 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.13:15.1 - Static conformance (SCR)

* **SCR-F13-S01 (context-local continuity).** Every `renames/aliases` relates labels **within the same context** or the **same row/Role Description**; none cross Contexts.
* **SCR‑F13‑S02 (Truthfulness).** For each `renames`, there exists an unchanged **SenseCell/row**; otherwise the move is rejected.
* **SCR‑F13‑S03 (Alias budget).** For any one thing and register, the number of deprecated aliases is **≤ 1**.
* **SCR‑F13‑S04 (Non‑retroactivity).** No requirement or suggestion to rewrite past texts is present; continuity is expressed as **read‑paths**.
* **SCR‑F13‑S05 (Row integrity).** A row rename occurs only when the row’s **intension** is stable; if membership changed, a **row split/merge** is documented (F.7).
* **SCR‑F13‑S06 (Bridge discipline).** No alias/rename is used to imply Cross‑context sameness; any such relation belongs under **F.9**.

#### F.13:15.2 - Regression (RSCR)

* **RSCR‑F13‑E01 (Edition drift audit).** When a canon edition changes, all labels from that Context are checked against definitions; moves are `renames` if senses stable, else `splits/merges`.
* **RSCR‑F13‑E02 (Alias creep check).** Periodically ensure alias budgets remain within **≤ 1 per register**; surplus aliases are pruned.
* **RSCR‑F13‑E03 (Bridge leak check).** Scan continuity notes for Cross‑context hints; any such case is converted into a **Bridge** or deleted.
* **RSCR‑F13‑E04 (Didactic continuity).** Sampling of examples shows that readers can **resolve** legacy labels to current ones without confusion (via the continuity notes).

