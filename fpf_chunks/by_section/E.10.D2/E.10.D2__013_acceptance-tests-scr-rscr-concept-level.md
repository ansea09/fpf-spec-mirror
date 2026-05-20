---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "Intension–Description–Specification Discipline (I/D/S)"
section_id: "E.10.D2:12"
section_title: "Acceptance tests (SCR/RSCR — concept‑level)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__013_acceptance-tests-scr-rscr-concept-level.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "E.10.D2 — Intension–Description–Specification Discipline (I/D/S)"
  - "E.10.D2:12 — Acceptance tests (SCR/RSCR — concept‑level)"
line_start: 52993
line_end: 53015
dependencies:
  - "A.7"
  - "C.2.1"
  - "C.2.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.10"
  - "F.15"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
  - "U.EpistemeSlotGraph"
keywords:
  - "I/D/S"
  - "description"
  - "intension"
  - "specification"
  - "testable"
  - "verifiable"
---

### E.10.D2:12 - Acceptance tests (SCR/RSCR — concept‑level)

#### E.10.D2:12.1 Static conformance checks (SCR)

* **SCR-D2-S01 (Suffix discipline).** Every episteme with suffix **–Spec** passes the **Spec-gate** (**F ≥ F4** ∧ testable invariants ∧ harness link ∧ Context named). Otherwise it bears **–Description**.
* **SCR‑D2‑S02 (Characterisation verbs).** Texts never say an intension “contains” RCS/RSG; they say it is **characterised by** them via the Description/Spec.
* **SCR‑D2‑S03 (Plane purity).** No episteme mixes role **states** and knowledge **statuses**; each appears only on its correct plane.
* **SCR‑D2‑S04 (context‑locality).** Every Description/Spec names its `U.BoundedContext`; wording reads correctly when prefixed by the Context.
* **SCR‑D2‑S05 (Two registers).** Tech **and** Plain labels present on all Descriptions/Specs.
* **SCR‑D2‑S06 (Carrier separation).** Identity statements refer to Epistemes; files are referenced only as `U.Carrier` encodings.
* **SCR‑D2‑S07 (Windowed evaluation).** All state attestations cite a window `W` (instant or interval).

#### E.10.D2:12.2 Regression checks (RSCR)

* **RSCR‑D2‑E01 (Spec demotion guard).** If a **–Spec** loses its harness or testability, it is demoted to **–Description**; diffs show no lingering “shall” claims.
* **RSCR‑D2‑E02 (Bridge drift).** If two Contexts begin to share identical labels, verify no Descriptions/Specs imply Cross‑context identity; add or revise **F.9 Bridges** instead.
* **RSCR‑D2‑E03 (Edition churn).** When a Context’s canon updates, previously valid attestations remain historical (windowed); new Specs/Descriptions cite the new edition.
* **RSCR‑D2‑E04 (Verb hygiene).** Automated grep over corpus finds “contains RSG/RCS” phrasing; none remain after refactor.
* **RSCR‑D2‑E05 (Status bleed).** Spot‑audit a random sample of role graphs to ensure no epistemic/deontic statuses appear as role states.

*Didactic takeaway.*
Think in three layers: **Intension** (what the thing *is*), **Description/Spec** (how we *state* its character and, when mature, *test* it), and **Evaluation** (what we can *attest* about it in a **window**). Keep Contexts local, planes separate, and “contains” out of your vocabulary.

