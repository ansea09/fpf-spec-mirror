---
chunk_kind: "child"
pattern_id: "F.13"
pattern_title: "Lexical Continuity & Deprecation"
section_id: "F.13:15"
section_title: "Acceptance tests (SCR/RSCR — concept‑level)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.13/F.13__016_acceptance-tests-scr-rscr-concept-level.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "F.13 — Lexical Continuity & Deprecation"
  - "F.13:15 — Acceptance tests (SCR/RSCR — concept‑level)"
line_start: 106982
line_end: 106999
dependencies:
  - "F.1"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "deprecation"
  - "historical reading"
  - "lexical continuity"
  - "local aliases"
  - "renaming labels"
  - "retirement"
  - "splitting and merging labels"
---

### F.13:15 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.13:15.1 - Static conformance (SCR)

* **SCR-F13-S01 (local continuity).** Every `renames/aliases` preserves the exact semantic projection, intended use and any independently governed value. An external row or description label resolves its target under the applicable rule.
* **SCR-F13-S02 (Truthfulness).** Each rename retains its exact old and new expressions. A changed LocalExpression has a distinct F.17 cell even when meaning is unchanged. Any claim of governed-value or episteme continuity satisfies that subject's rule.
* **SCR‑F13‑S03 (Alias budget).** For any one thing and register, the number of deprecated aliases is **≤ 1**.
* **SCR‑F13‑S04 (Non‑retroactivity).** No requirement or suggestion to rewrite past texts is present; continuity is expressed as **read‑paths**.
* **SCR-F13-S05 (Row integrity).** A display-label rename preserves the exact comparison content and receiving use. Changed row content receives its warranted revision, split or merge under F.7; changed F.17 identity-bearing claims receive the corresponding later row episteme.
* **SCR‑F13‑S06 (Bridge discipline).** No alias/rename is used to imply Cross‑context sameness; any such relation belongs under **F.9**.

#### F.13:15.2 - Regression (RSCR)

* **RSCR-F13-E01 (Edition drift audit).** Compare affected earlier/later definitions and naming uses. Stable meaning can support a rename with distinct expression-bearing cells; changed meaning requires the subject-governed revision, replacement, split, merge or retirement before fresh naming settlement.
* **RSCR‑F13‑E02 (Alias creep check).** Periodically ensure alias budgets remain within **≤ 1 per register**; surplus aliases are pruned.
* **RSCR-F13-E03 (Bridge leak check).** A claimed correspondence between different semantic projections is tested under F.9 only when a current use needs it. Retain exact meanings and an honest unresolved result when obtaining is unestablished; do not create a Bridge by rewriting a note.
* **RSCR‑F13‑E04 (Didactic continuity).** Sampling of examples shows that readers can **resolve** legacy labels to current ones without confusion (via the continuity notes).

