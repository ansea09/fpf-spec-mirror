---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "Static and Regression Conformance Harness for Unification"
section_id: "F.15:5"
section_title: "Minimal vocabulary"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__007_minimal-vocabulary.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "F.15 — Static and Regression Conformance Harness for Unification"
  - "F.15:5 — Minimal vocabulary"
line_start: 97845
line_end: 97856
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.6"
  - "A.2.7"
  - "A.22"
  - "A.6.1"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.24.PUB"
  - "F.1-F.14"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.6"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:5 - Minimal vocabulary

* **Finite harness scope** - an F.15-local by-value selection of exact current refs, versions, triggered rules, and one receiving use; not a U-kind, relation, evidence set, or selected Structure by default.
* **Static Conformance Rule (SCR)** - an F.15-local declared predicate over exact current inputs.
* **Regression and Stability Conformance Rule (RSCR)** - an F.15-local declared predicate over exact earlier/later inputs plus the continuity or change claim and receiving use.
* **Check application** - an actual A.6.1 operation application with exact rule and object bindings, when current.
* **Dated assessment Work** - a specific `U.Work` occurrence used only for a replayable performance claim. Each performer must already have the A.13 core and the Work must already be independently admitted under A.15.1. F.6 is additionally required only when the receiving claim needs precise assignment-bound attribution.
* **Result claim** - one C.2.1 episteme asserting `pass`, `fail`, or `undetermined` for one exact rule application, scope version, and use; not a general status value.
* **Witness** - an exact example, counterexample, invariant, trace, or edition note cited by the result claim; its presence is not the result or an evidence-use relation.
* **Conformance record** - an optional C.2.1 episteme that packages refs to the scope, applications/work, result claims, witnesses/evidence paths, non-admitted uses, and reopen conditions; it performs no check.
* **Changed member** - one exact prior/later pair whose governed identity, relation truth, description, designation, status use, or publication availability may affect the receiving use.

