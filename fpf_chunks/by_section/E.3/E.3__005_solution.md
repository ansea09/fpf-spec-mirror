---
chunk_kind: "child"
pattern_id: "E.3"
pattern_title: "Principle Taxonomy, Precedence and Agent Autonomy Profiles (ABL)"
section_id: "E.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.3/E.3__005_solution.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "E.3 — Principle Taxonomy, Precedence and Agent Autonomy Profiles (ABL)"
  - "E.3:4 — Solution"
line_start: 78979
line_end: 79016
dependencies:
  - "E.1"
  - "E.2"
keywords:
  - "ABL"
  - "Arch"
  - "BLP waiver"
  - "Did"
  - "Epist"
  - "Gov"
  - "Prag"
  - "autonomy budget"
  - "conflict resolution"
  - "oversight"
  - "precedence"
  - "principle taxonomy"
  - "profile change"
---

### E.3:4 - Solution

#### E.3:4.1 - **Principle Taxonomy**
   For this precedence classification, assign each principle **exactly one** class from { `Gov`, `Arch`, `Epist`, `Prag`, `Did` }.

   | Class                                    | Scope & Purpose                           | Example Pillars                                   |
   | ---------------------------------------- | ----------------------------------------- | ------------------------------------------------- |
   | **Gov** (Governance)                     | Change process, community decision‑making | P‑10 Open‑Ended Evolution - P‑11 SoTA             |
   | **Arch** (Architectural)                 | Macro‑structure & invariants              | P‑1 Cognitive Elegance - P‑4 Kernel               |
   | **Epist** (Epistemological and Ontological) | Semantics, evidence, trust                | P‑3 Scalable Formality - P‑8 Consistency          |
   | **Prag** (Pragmatic)                     | Real‑world value & cost/benefit           | P‑7 Pragmatic Utility                             |
   | **Did** (Didactic)                       | Cognition & learnability                  | P‑2 Didactic Primacy - P‑6 Lexical Stratification |

   *Epistemological* sub‑concerns (reasoning, falsifiability) reside inside **Epist**, avoiding category sprawl yet keeping semantics and trust in one bucket.

 #### E.3:4.2 - **Precedence Stack**

Each precedence node is an exact applicable pillar, derived principle, guard or assurance requirement, or local policy. The table identifies its source level; it does not rank every sentence in one file above every sentence in another. In particular, level 1 is the Eleven Pillars, not the entire E.2 file.

   | Level | Governing Artefact                    | Overrides        |
   | ----- | ------------------------------------- | ---------------- |
   | 0     | **Vision & Mission** (E.1)            | everything       |
   | 1     | **Eleven Pillars** (E.2)              | all below        |
   | 2     | **Principles** (this pattern)         | patterns & DRRs  |
   | 3     | Architectural / Definitional patterns | local rules      |
   | 4     | Tooling & Pedagogy                    | informative only |

**Default class order.** Identify the applicable rules and their source levels. Within the higher-rule boundaries, apply any explicit priority governing this pair. Only an otherwise unresolved conflict uses the default class order:
`Gov ≫ Arch ≫ Epist ≫ Prag ≫ Did`

**Unresolved conflict.** These relations form a partial order. Two incompatible applicable rules may remain tied or incomparable after the source-level, explicit-priority and class comparisons. Return that exact pair, the shared action and applicability conditions, and **hold the dependent action**. Unrelated actions remain governed by their own applicable rules. Acyclicity does not guarantee a winner.

To resolve the hold, refer the pair to the authority empowered to amend the affected rules or their priority under their governing change process. That authority may adopt a priority or amend a rule's scope. Record the rationale, affected scope, Pillar Impact Analysis and edge effects under E.9; an exception also retains its required expiry. The DRR records the decision and does not itself authorize the change. Apply the resolution only after the necessary authorization, retaining higher-rule constraints and the graph rule below.

 **Graph Rule** — The precedence graph MUST be acyclic; any new edge that would form a cycle is **rejected**.

Governance principle vs Pragmatic principle clash: e.g. Core release schedule (Gov) outranks performance‑tuning (Prag).

