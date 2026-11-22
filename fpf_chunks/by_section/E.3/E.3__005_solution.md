---
chunk_kind: "child"
pattern_id: "E.3"
pattern_title: "Principle Taxonomy, Precedence and Agent Autonomy Profiles (ABL)"
section_id: "E.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.3/E.3__005_solution.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "E.3 — Principle Taxonomy, Precedence and Agent Autonomy Profiles (ABL)"
  - "E.3:4 — Solution"
line_start: 98370
line_end: 98411
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

   *Epistemological* sub‑concerns (reasoning, falsifiability) reside inside **Epist**, keeping semantics and trust in one class.

 #### E.3:4.2 - **Precedence Stack**

Identify who would do what, for whom or to what, and when. Which provisions govern that decision? Can a course of action meet them together? A rule can require an action, forbid it, reserve a choice to a participant, or let another decision maker choose. A team can select a common format if the governing rule delegates that choice to the team. If the rule reserves the choice to each sender, a team instruction that removes the sender’s choice conflicts with it. Apply compatible provisions together. If applicability turns on a missing fact, compare what each possible rule would allow or require. When all support the same action on the same terms, it can proceed. Obtain the fact if it changes the decision or the required procedure, or if the task asks which rule applies.

The **FPF precedence rank** orders applicable provisions in the FPF constitution. A smaller number gives the provision priority where the two conflict. Rank 1 belongs to the eleven pillars themselves. The derived BLP policy also printed in E.2 has its own terms in §6. A passage that quotes a binding rule takes its force from that rule. When an organization adopts guidance for its own work, the terms of adoption establish where it binds.

| FPF precedence rank | Source | Effect for an FPF decision |
| --- | --- | --- |
| 0 | Vision & Mission (E.1) | Charter commitments govern what FPF may admit. |
| 1 | The Eleven Pillars (E.2:4) | Their applicable constraints bind principles and patterns within the charter. |
| 2 | Derived principles, including the precedence rules in E.3 | They govern pattern choices and proposals for change within the pillars. |
| 3 | Architectural and definitional patterns | Their applicable provisions constrain choices left to local rules in a conforming use. |
| 4 | Tooling and pedagogy | Their own suggestions guide implementation and teaching. |

**Apply the priority that governs the conflict.** Within higher-ranking constraints, first use an explicit priority for the provisions in conflict. For a remaining conflict between classified principles, use the default class order:
`Gov ≫ Arch ≫ Epist ≫ Prag ≫ Did`

Apply the priority to the disputed choice and retain the other obligations. Several provisions can leave an obligation with no permitted way to satisfy it even when every pair is compatible. To establish that conflict, show how the provisions close every permitted alternative. If the alternatives are still unknown, identify what would establish them. After resolving a conflict, check the proposed course against the provisions together. Separately establish whether the people and resources needed for that course are available.

**When a conflict remains**, identify the provisions responsible, the affected action and the conditions that make them apply. Hold the dependent action. Independent permitted work can proceed. An existing ruling may already settle this case. If a holder is empowered to resolve this conflict, apply their actual decision within its scope and effective period. Until they decide, a known decision maker gives the parties someone to ask.

When the case would need an exception, use only an exception the governing terms authorize for these circumstances. If the mandate does not cover the conflict, keep the affected action on hold. To change a rule or priority for future cases, obtain the decision of the body or bodies empowered to change it. Record the rationale, affected scope, Pillar Impact Analysis and edge effects of an FPF change under E.9. For an exception governed by the FPF policy in §6, its DRR, rationale and expiry are required. An organization’s own policy sets the terms for exceptions within its authority. An earlier ruling governs a later case only when the governing terms give it that reach.

 **Graph Rule** — The precedence graph MUST be acyclic; any new edge that would form a cycle is **rejected**.

A release-schedule rule classified as Gov takes priority over a conflicting performance-tuning preference classified as Prag when the ranks and applicable explicit priorities leave the choice to the class order.

