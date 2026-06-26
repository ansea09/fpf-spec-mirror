---
chunk_kind: "child"
pattern_id: "E.3"
pattern_title: "Principle Taxonomy & Precedence Model"
section_id: "E.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.3/E.3__005_solution.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "E.3 — Principle Taxonomy & Precedence Model"
  - "E.3:4 — Solution"
line_start: 63667
line_end: 63698
dependencies:
  - "E.2"
keywords:
  - "Arch"
  - "Did"
  - "Epist"
  - "Gov"
  - "Prag"
  - "classification"
  - "conflict resolution"
  - "hierarchy"
  - "precedence"
  - "principles"
  - "taxonomy"
---

### E.3:4 - Solution

#### E.3:4.1 - **Principle Taxonomy**
   Every principle is an instance of `U.Principle` assigned **exactly one** class ∈ { `Gov`, `Arch`, `Epist`, `Prag`, `Did` }.

   | Class                                    | Scope & Purpose                           | Example Pillars                                   |   |
   | ---------------------------------------- | ----------------------------------------- | ------------------------------------------------- | - |
   | **Gov** (Governance)                     | Change process, community decision‑making | P‑10 Open‑Ended Evolution - P‑11 SoTA             |   |
   | **Arch** (Architectural)                 | Macro‑structure & invariants              | P‑1 Cognitive Elegance - P‑4 Kernel               |   |
   | **Epist** (Epistemological and Ontological) | Semantics, evidence, trust                | P‑3 Scalable Formality - P‑8 Consistency          |   |
   | **Prag** (Pragmatic)                     | Real‑world value & cost/benefit           | P‑7 Pragmatic Utility                             |   |
   | **Did** (Didactic)                       | Cognition & learnability                  | P‑2 Didactic Primacy - P‑6 Lexical Stratification |   |

   *Epistemological* sub‑concerns (reasoning, falsifiability) reside inside **Onto**, avoiding category sprawl yet keeping semantics and trust in one bucket.

 #### E.3:4.2 - **Precedence Stack**

   | Level | Governing Artefact                    | Overrides        |
   | ----- | ------------------------------------- | ---------------- |
   | 0     | **Vision & Mission** (E.1)            | everything       |
   | 1     | **Eleven Pillars** (E.2)              | all below        |
   | 2     | **Principles** (this pattern)         | patterns & DRRs  |
   | 3     | Architectural / Definitional patterns | local rules      |
   | 4     | Tooling & Pedagogy                    | informative only |

**Within the precedence stack** the default order is:
`Gov ≫ Arch ≫ Epist ≫ Prag ≫ Did`

 **Graph Rule** — The precedence graph MUST be acyclic; any new edge that would form a cycle is **rejected**.

Governance principle vs Architectural principle clash: e.g. Core release schedule (Gov) outranks performance‑tuning (Prag)

