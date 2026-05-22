---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local‑First Unification Naming Protocol"
section_id: "F.18:21"
section_title: "Acceptance Harness (SCR/RSCR) for F.18"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__022_acceptance-harness-scr-rscr-for-f-18.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "F.18 — Local‑First Unification Naming Protocol"
  - "F.18:21 — Acceptance Harness (SCR/RSCR) for F.18"
line_start: 68163
line_end: 68192
dependencies:
  - "A.19.SUPPORT-VIEW"
  - "A.6.P"
  - "E.10"
  - "E.10.SEMIO"
  - "F.0.1"
  - "F.1-F.17"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:21 - Acceptance Harness (SCR/RSCR) for F.18

**Purpose.** Provide auditable, notation‑independent checks that a proposed unified name (and its publication on a UTS line) satisfies the **local‑first** unification discipline. The harness extends the general unification checks in **F.15** with **naming‑specific** obligations.

#### F.18:21.1 - Static Conformance Rules (SCR‑UNIFY)

| ID                                                                                                                                                                                                       | Requirement (normative “SHALL/SHALL NOT”)                   | Why this exists (conceptual)                                 | Where this is reflected |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ | ----------------------- |
| **SCR‑U‑01 (Row‑first).** A unified Tech/Plain name **SHALL** be published **only** on a **Concept‑Set row** whose cells are SenseCells drawn from declared Contexts. No free‑floating names.               | Names are *lenses* onto a defended **row**, not vice‑versa. | **F.7** row‑as‑unit; **F.17** UTS row discipline.            | §F.7; §F.17             |
| **SCR‑U‑02 (Bridge‑only equivalence).** Cross‑context sameness **SHALL** be claimed **only** via an explicit **Bridge** with a relation kind and **CL** + loss/fit note.                                    | Prevents “string‑match identity”.                           | **F.9** Bridges; **F.0.1** principles.                       | §F.9                    |
| **SCR‑U‑03 (Neutral Tech).** The **Unified Tech** label **SHALL** be **neutral**—not lifted wholesale from any single Context **unless** the row’s Concept‑Set shows exact identity.                        | Avoids importing a local worldview as global.               | **F.5** naming neutrality; **F.17** 9.8 naming neutrality.   | §F.5; §F.17             |
| **SCR‑U‑04 (Twin registers).** Each row **SHALL** carry **Tech** and **Plain** names with the Part E register discipline; Plain is teacher‑friendly, Tech is morphology‑stable.                          | Satisfies didactic primacy without jargon creep.            | **E.10** registers; **F.5** naming rules.                    | §E.10; §F.5             |
| **SCR‑U‑05 (No window‑in‑name).** Variations by **time/phase/scale** **SHALL** be handled by **applicability windows** on **Statuses** (or examples), **NOT** by baking modifiers into the unified name. | Prevents type/status explosion by adjectives.               | **F.10/F.12** windows; **F.14** explosion guard.             | §F.10; §F.12; §F.14     |
| **SCR‑U‑06 (Heterogeneity).** A UTS block **SHALL** demonstrate **≥ 3** independent domain families across its rows, or an explicit Bias‑Annotation shall scope the claim.                               | Enforces trans‑disciplinary reach or honest scope.          | **F.17** invariants 3; **E.8** Bias‑Annotation.              | §F.17; §E.8             |
| **SCR‑U‑07 (Member≠Component sanity).** Names **SHALL NOT** imply holarchic composition when the row unifies **collections**; keep **MemberOf** distinct from **ComponentOf**.                           | Stops structural category errors.                           | Part F principles / anti‑patterns.                           | §9.8; §13               |
| **SCR‑U‑08 (One‑breath rationale).** Each row **SHALL** include a **single‑sentence** Unification Rationale that states **why** the cells belong in the same Concept-Set row despite wording differences.             | Keeps the argument visible and auditable.                   | **F.17** invariant 7.                                        | §F.17                   |
| **SCR‑U‑09 (Alias budget).** Per register, deprecated aliases on a unified name **SHALL** be **≤ 1**; additional deprecated labels go to Annex/Glossary.                                                         | Controls lexical drift while preserving continuity.         | **F.13** alias budget rule.                                  | §F.13                   |
| **SCR‑U‑10 (No Cross‑context rename).** A rename **SHALL** occur **within** the same Context or same row; Cross‑context “renames” are **prohibited**—use Bridges.                                                 | Keeps locality intact; forbids silent conflation.           | **F.13** continuity; **F.9** Bridges.                        | §F.13; §F.9             |
| **SCR‑U‑11 (Semantic read‑through).** A unified Tech/Plain name **SHALL** pass a **semantic read‑through**: the Name Card lists **5–10 diverse NQD archetypal situations** and the **NQD‑front notes** record rejected candidate and their **mismatch patterns**. | Prevents labels that mislead across the intended situations; ties lexical choice to demonstrated use. | §F.18 §4.2; §F.18 §5. | §F.18 |

#### F.18:21.2 - Regression Rules (RSCR‑UNIFY)

| ID                                                                                                                                                                       | Regression duty across editions                                        | Effect |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- | ------ |
| **RSCR‑U‑E01 (Edition drift).** When a source Context updates, re‑validate the row: stable sense ⇒ **rename/alias**; changed sense ⇒ **split/merge** rows; never overwrite. | Preserves truthfulness without erasing history. **F.13** RSCR.         |        |
| **RSCR‑U‑E02 (CL honesty).** Bridges **SHALL NOT** increase their CL (claiming higher-CL sameness) without new witnesses; **SHOULD** reduce CL when editions diverge.     | Guards against optimism bias in equivalence. **F.17** migration cues.  |        |
| **RSCR‑U‑E03 (Alias creep).** Periodically prune aliases to the **≤ 1** budget per register.                                                                             | Maintains narratively crisp UTS. **F.13** RSCR‑Alias.                  |        |
| **RSCR‑U‑E04 (Name neutrality check).** If the Unified Tech label is traceable to one context’s idiom, re‑justify neutrality or retitle the row.                            | Keeps the name “ours,” not “theirs.” **F.17** 9.7–9.8.                 |        |
| **RSCR‑U‑E05 (Window misuse).** Reject newly proposed types that are really **windows** on an existing Status/Role.                                                      | Prevents explosion by adjectives. **F.14** S14/E11 patterns.           |        |

