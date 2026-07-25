---
chunk_kind: "child"
pattern_id: "A.17"
pattern_title: "Canonical “Characteristic” (A.CHR‑NORM)"
section_id: "A.17:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.17/A.17__004_forces.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.17 — Canonical “Characteristic” (A.CHR‑NORM)"
  - "A.17:3 — Forces"
line_start: 27505
line_end: 27518
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2.3"
  - "A.3.3"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2"
  - "D.3"
  - "E.10"
  - "U.Dynamics"
  - "U.PromiseContent.acceptanceSpec"
keywords:
  - "attribute"
  - "axis"
  - "characteristic"
  - "dimension"
  - "measurement"
  - "property"
---

### A.17:3 - Forces

-   **F1 – Single anchor of meaning.** Any numeric value is meaningless unless one can ask “value of _what_?”. The measurement’s meaning must be anchored in a single clearly named aspect.

-   **F2 – Arity clarity.** Some characteristics apply to a single entity (e.g. its mass or length), while others inherently relate multiple entities (e.g. distance between two points, coupling between modules, agreement between judges). If arity isn’t explicit, claims and calculations become corrupted.

-   **F3 – Scale integrity.** Different kinds of scales permit different operations – e.g. you can average temperatures (ratio scale) but not ranks or grades (ordinal scale) without losing meaning. If one mixes values without regard to scale type or units, the result is nonsense (**pseudo-arithmetic**).

-   **F4 – Composition discipline.** In complex evaluations, multiple measurements may need to be combined. Without a disciplined approach, people might perform ad-hoc math on apples and oranges (adding scores from unrelated characteristics, etc.). A proper pattern must require any combination to go through a defined monotonic **ScoringMethod** (e.g. a weighted formula) instead of arbitrary aggregation.

-   **F5 – Transdisciplinarity.** The measurement framework should work for **any domain**. The same conceptual scaffold must serve physical science (e.g. lab temperature readings), software engineering (e.g. module cohesion ratings), and even subjective assessments (e.g. figure-skating scores) without bias. One vocabulary, many CG‑frames.

-   **F6 – Open-endedness.** As systems evolve, their performance or quality metrics also evolve. Rigid stage labels (“Phase 1, Phase 2…”) don’t capture iterative improvement. The pattern should favor an **open-ended state-space** view (revisiting states via checklists, as in an RSG – **RoleStateGraph** with re-entry) over any fixed stage sequence with “terminal” stages.

