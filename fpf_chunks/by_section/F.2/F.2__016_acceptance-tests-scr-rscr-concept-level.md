---
chunk_kind: "child"
pattern_id: "F.2"
pattern_title: "Term Harvesting & Normalisation"
section_id: "F.2:15"
section_title: "Acceptance tests (SCR/RSCR — concept‑level)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.2/F.2__016_acceptance-tests-scr-rscr-concept-level.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "F.2 — Term Harvesting & Normalisation"
  - "F.2:15 — Acceptance tests (SCR/RSCR — concept‑level)"
line_start: 87340
line_end: 87359
dependencies:
  - "A.11"
  - "A.7"
  - "D.CTX"
  - "E.10.D1"
  - "F.0.1"
  - "F.1"
  - "F.3"
  - "F.4"
  - "F.9"
keywords:
  - "lexical unit"
  - "normalization"
  - "provenance"
  - "source-text terms"
  - "term harvesting"
---

### F.2:15 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.2:15.1 - Static conformance (SCR)

* **SCR‑F2‑S01 (context‑locality).** Every unit cites a Context from F.1.
* **SCR‑F2‑S02 (Idiomatic LNF).** Each LNF reflects the Context’s spelling/hyphenation/casing with **minimal edits**.
* **SCR‑F2‑S03 (Two registers).** Each unit carries both **Tech** and **Plain** labels; if not, a reason exists tied to didactics.
* **SCR‑F2‑S04 (Lexical‑only).** No gloss contains behaviour, deontics, measurement math, or type axioms.
* **SCR‑F2‑S05 (No Cross‑context claims).** Nowhere does F.2 assert equivalence/similarity/subsumption across Contexts.
* **SCR‑F2‑S06 (Minimal generality).** Glosses match the Context’s use; no globalisation.
* **SCR‑F2‑S07 (Temporal honesty).** For Contexts with fixed DesignRunTag, units and glosses respect it.

#### F.2:15.2 - Regression (RSCR)

* **RSCR‑F2‑E01 (Edition split).** Introducing a new edition yields new units under a new Context; earlier units persist unchanged.
* **RSCR‑F2‑E02 (Normaliser stability).** Adjusting an LNF does not silently widen/narrow the gloss.
* **RSCR‑F2‑E03 (Language split).** Adding a second language yields a second Context; no bilingual collapse in F.2.
* **RSCR‑F2‑E04 (No stealth bridges).** After updates, F.2 still contains **zero** Cross‑context identity claims; any mapping appears only in F.9.
* **RSCR‑F2‑E05 (Head‑term focus).** Periodic check shows the unit set remains small and oriented to F.3/F.4/F.9 needs.

