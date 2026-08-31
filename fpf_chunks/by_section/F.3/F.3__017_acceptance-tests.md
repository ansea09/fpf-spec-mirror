---
chunk_kind: "child"
pattern_id: "F.3"
pattern_title: "Source-Local Sense Clustering"
section_id: "F.3:16"
section_title: "Acceptance tests"
source_path: "FPF-Spec.md"
output_path: "by_section/F.3/F.3__017_acceptance-tests.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "F.3 — Source-Local Sense Clustering"
  - "F.3:16 — Acceptance tests"
line_start: 93481
line_end: 93499
dependencies:
  - "A.11"
  - "A.7"
  - "E.10.D1"
  - "F.1"
  - "F.17"
  - "F.2"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "LocalSenseClaim"
  - "alias consolidation"
  - "counterexample"
  - "effective ReferenceScheme"
  - "optional SchemeSenseCell"
  - "source expression"
---

### F.3:16 - Acceptance tests

#### F.3:16.1 - Static conformance

* **SCR-F3-S01 (basis).** Every LocalSenseClaim names its source and edition and the effective reference scheme.
* **SCR-F3-S02 (labels).** Tech and Plain denote the same bounded claim.
* **SCR-F3-S03 (fidelity and time stance).** Each claim is grounded in cited source use, preserves any source-grounded design-time, run-time, or other temporal distinction, and contains no imported substantive calculus.
* **SCR-F3-S04 (parsimony).** The claim set is small enough for the receiving question.
* **SCR-F3-S05 (counterexample).** Ambiguous heads have a concrete boundary test.
* **SCR-F3-S06 (no inferred relation).** Clustering asserts no cross-source identity, hierarchy, transfer, or permission.

#### F.3:16.2 - Regression

* **RSCR-F3-E01 (merge soundness).** Every merge has a failed relevant distinction test.
* **RSCR-F3-E02 (split necessity).** Every split cites an argument, entailment, temporal, or counterexample difference.
* **RSCR-F3-E03 (edition honesty).** Changed editions are not silently absorbed into an old claim.
* **RSCR-F3-E04 (label stability).** Label changes do not change the claim unnoticed.
* **RSCR-F3-E05 (downstream continuity).** After a split or merge, direct citations and any F.17 cells remain unambiguous; no silent aliasing occurs.

