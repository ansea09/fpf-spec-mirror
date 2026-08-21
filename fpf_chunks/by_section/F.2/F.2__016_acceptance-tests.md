---
chunk_kind: "child"
pattern_id: "F.2"
pattern_title: "Term Harvesting & Normalisation"
section_id: "F.2:15"
section_title: "Acceptance tests"
source_path: "FPF-Spec.md"
output_path: "by_section/F.2/F.2__016_acceptance-tests.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "F.2 — Term Harvesting & Normalisation"
  - "F.2:15 — Acceptance tests"
line_start: 88366
line_end: 88384
dependencies:
  - "A.11"
  - "A.7"
  - "E.10.D1"
  - "F.0.1"
  - "F.1"
  - "F.17"
  - "F.3"
  - "F.4"
  - "F.9"
keywords:
  - "LNF"
  - "LocalExpression"
  - "LocalSenseClaim"
  - "effective ReferenceScheme"
  - "exact source and edition"
  - "optional SchemeSenseCell"
---

### F.2:15 - Acceptance tests

#### F.2:15.1 - Static conformance

* **SCR-F2-S01 (basis).** Every note names the exact source and edition and the effective scheme required to recover the claim.
* **SCR-F2-S02 (idiomatic LNF).** Each LNF preserves meaningful spelling, hyphenation, casing, and modifiers.
* **SCR-F2-S03 (two registers).** Tech is faithful and Plain is explanatory without added scope.
* **SCR-F2-S04 (lexical boundary).** No note substitutes for behaviour, obligation, measurement, kind, assignment, Work, or evidence.
* **SCR-F2-S05 (no cross-source claim).** F.2 asserts no equivalence, hierarchy, transfer, or permission between local meanings.
* **SCR-F2-S06 (minimal generality).** Each LocalSenseClaim is no broader than its source use and receiving question.

#### F.2:15.2 - Regression

* **RSCR-F2-E01 (edition change).** A changed edition produces a newly recovered claim only where meaning changed; earlier source identity remains visible.
* **RSCR-F2-E02 (normaliser stability).** LNF edits do not silently widen or narrow the claim.
* **RSCR-F2-E03 (language honesty).** Translation does not create unproved sameness.
* **RSCR-F2-E04 (no stealth relation).** New notes still contain no cross-source identity or use claim.
* **RSCR-F2-E05 (head-term focus).** The working set remains small and tied to actual downstream questions.

