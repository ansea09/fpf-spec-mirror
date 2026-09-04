---
chunk_kind: "child"
pattern_id: "F.7"
pattern_title: "Concept-Set Table"
section_id: "F.7:15"
section_title: "Acceptance tests"
source_path: "FPF-Spec.md"
output_path: "by_section/F.7/F.7__016_acceptance-tests.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "F.7 — Concept-Set Table"
  - "F.7:15 — Acceptance tests"
line_start: 95091
line_end: 95108
dependencies:
  - "A.6.9"
  - "B.3"
  - "C.16"
  - "E.10.D1"
  - "F.0.1"
  - "F.1"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.9"
keywords:
  - "comparison surface"
  - "direction"
  - "evidence"
  - "exact local claim"
  - "loss"
  - "obtaining relation"
  - "optional SchemeSenseCell"
  - "receiving use"
---

### F.7:15 - Acceptance tests

#### F.7:15.1 - Static conformance

* **SCR-F7-S01 (exact entries).** Every local entry identifies an exact claim or F.17 cell and its source and edition.
* **SCR-F7-S02 (no row-created fact).** No relation or permission is inferred from co-placement, label similarity, or layout.
* **SCR-F7-S03 (relation basis).** Every positive relation cites the pattern that defines, constrains, or tests it, states direction where relevant, and cites its evidence.
* **SCR-F7-S04 (receiving use).** Every practical use conclusion is separate from the row and has its own basis.
* **SCR-F7-S05 (loss disclosure).** Material limitations and counterexamples remain visible.
* **SCR-F7-S06 (parsimony).** Every extra entry changes the current comparison or use.

#### F.7:15.2 - Regression

* **RSCR-F7-E01 (relation drift).** A changed relation triggers re-evaluation of dependent use conclusions, not a global row score.
* **RSCR-F7-E02 (sense split).** A split local claim leaves no ambiguous cell reference.
* **RSCR-F7-E03 (use integrity).** No consumer treats a row label as licence outside the stated conclusion.
* **RSCR-F7-E04 (no stealth growth).** New entries create no silent relation, closure, or widened use.

