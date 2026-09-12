---
chunk_kind: "child"
pattern_id: "A.17"
pattern_title: "Canonical “Characteristic” (A.CHR‑NORM)"
section_id: "A.17:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.17/A.17__005_solution.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "A.17 — Canonical “Characteristic” (A.CHR‑NORM)"
  - "A.17:4 — Solution"
line_start: 29685
line_end: 29718
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
  - "preference"
  - "property"
  - "quantity calculation"
  - "scale order"
  - "scoring"
---

### A.17:4 - Solution

**Establish “Characteristic” as the one canonical construct for “what is measured.”** In every FPF context, the _aspect or trait_ being measured MUST be referred to as a **Characteristic**. This term replaces “axis” or “dimension” in normative usage (those may appear _only_ as explanatory aliases in Plain register). By fixing a single name and schema, we cleanly separate a **Characteristic** from its **Scale** (and **Unit**), and from any observed **Value/Level** on that scale. The solution also differentiates single-entity vs multi-entity cases and binds all measurements to the standard CSLC sequence.

To enforce this solution, the following rules apply:

-   **A17-R1 (Canonical term).** In all normative models and specifications, the measured aspect **SHALL** be referred to as a **Characteristic**. (Legacy terms “Axis” or “Dimension” are retired from technical vocabulary – see Part J Lexicon Update.)

-   **A17-R2 (Entity vs. relation subtype).** Each Characteristic **MUST** declare its intended _arity_. An **Entity-Characteristic** applies to exactly one bearer (e.g. _Temperature_ of a reactor, _Evolvability_ of a software module), whereas a **Relation-Characteristic** applies to an ordered tuple of two or more bearers (e.g. _Distance_ between two sensors, _Coupling_ between modules, _Agreement_ among reviewers). The arity is part of the definition and **must be explicit** wherever it’s not obvious from naming.

- **A17-R3 (Characteristic space).** When several Characteristics form a declared space, identify their slots, Scales and admissible values under A.19. State the constraints and additional structure required by its use. A.3.3 constructs the state and transition account when the question concerns modeled change.

-   **A17-R4 (Lexical guardrails).** Normative text **SHALL** use only the canonical measurement terms: **Characteristic, Scale, Level, Value, Coordinate, Score, Normalization, Unit**. Synonyms like _axis_, _dimension_, _metric_, _grade_, _property_, etc., are **forbidden in formal usage**. (They may appear in narrative explanations or user-facing documentation _only if_ clearly defined as aliases for the canonical terms.) Authors **MUST** not use deprecated terms in identifiers or formal statements, and any didactic alias should be introduced with an explicit mapping to the official term. These lexical rules uphold clarity and are further detailed in **E.10 LEX‑BUNDLE**.

- **A17-R5 (Symbol policy).** **Γ** is reserved for holonic composition; **𝒢** denotes a ScoringMethod from Coordinates to a Score. Documents **SHALL NOT** reuse Γ for a ScoringMethod.

- **A17-R6 (Scale order and preference).** For an ordered Scale, use its order to compare values of the Characteristic: a higher temperature value means hotter. A use that ranks values by desirability **SHALL** declare its preference rule, such as higher-is-better, lower-is-better, a target or range, or another ordering. Describing or comparing magnitudes requires no preference rule.

- **A17-R7 (Scoring against preference).** A ScoringMethod **SHALL** state how its score order represents the declared preference. Where one input is higher-is-better or lower-is-better, improving that input while holding the others fixed **MUST NOT** worsen the score, for admissible inputs under the stated conditions. Target-based preference is checked against its declared target or loss rule; the preferred direction may change across the target. A quantity calculation or unit conversion uses its measurement relation and Scale rules under A.18/C.16.

- **A17-R8 (Arity declaration).** Authors **SHALL** mark a Characteristic as **`U.EntityCharacteristic`** (applies to exactly one bearer) or **`U.RelationCharacteristic`** (applies to a relation of cardinality ≥ 2). Examples: *Cohesion* → entity‑level; *Coupling* → relation‑level.

- **A17-R9 (Relational scale anchors).** For relation‑level cases, the Scale’s admissible values **SHALL** be defined over the **tuple** domain (e.g., distances, similarities, inter‑role latencies). Ambiguity that re‑reads a relational Characteristic as unary is **forbidden**.

- **A17-R10 (Intension vs Description).** The **Characteristic** remains the **Characteristic EntityOfConcern**; any rubric, catalogue of levels, or examples are **Description epistemes**. Keep the intensional Characteristic distinct from its descriptive episteme (cf. `U.Episteme` roles: Object–Concept–Symbol).

#### A.17:4.1 - CharacteristicSpace & Change Reasoning *(Normative/Clarifying)*

**R17 - State-space use.** When a change model uses a CharacteristicSpace, declare its Characteristics, Scales, units and admitted combinations under A.19. Add topology, distance or another structure when the inference relies on it.

**R18 - Allowed changes and state recognition.** For a model of change, state the allowed continuations and their conditions through A.3.3. Use a state predicate or checklist when the receiving use needs to recognize a condition. A.2.5 governs the particular case of a condition on an assignment to a system role; a gate or assurance use supplies its own required support.

**I7 — Vector interpretation.** A **U.Coordinate** vector may collect multiple coordinates for multi‑Characteristic reasoning; composition into a single Score, if desired, is an **explicit new 𝒢** on that vector.

