---
chunk_kind: "child"
pattern_id: "A.17"
pattern_title: "Canonical “Characteristic” (A.CHR-NORM): Name What Is Measured"
section_id: "A.17:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.17/A.17__005_solution.md"
commit_sha: "b223469ecafb9735c1d9bac220671e3336618339"
heading_path:
  - "A.17 — Canonical “Characteristic” (A.CHR-NORM): Name What Is Measured"
  - "A.17:4 — Solution"
line_start: 34324
line_end: 34359
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
  - "F.7"
  - "F.9"
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

**Establish “Characteristic” as the one canonical construct for “what is measured.”** In every FPF context, the _aspect or trait_ being measured MUST be referred to as a **Characteristic**. This term replaces “axis” or “dimension” when they are used as names for the measured aspect; Plain aliases must keep that mapping clear. By fixing a single name and schema, we cleanly separate a **Characteristic** from its **Scale** (and **Unit**), and from any observed **Value/Level** on that scale. The solution also differentiates single-entity vs multi-entity cases and binds all measurements to the standard CSLC sequence.

**Recover the same aspect.** Identify a Characteristic by the aspect it distinguishes, the domain and arity of its possible subjects, the roles of an ordered subject tuple when relevant, and the conditions constitutive of that aspect. A changed reading, bearer, observation window or description does not by itself define a new Characteristic. A different Scale can express the same aspect through a justified conversion. Conversely, an unchanged name does not preserve the Characteristic if it now distinguishes another aspect or changes the subject roles. Preserve the original definition and establish the correspondence needed by the receiving comparison; unresolved equivalence is not identity. A content evaluation and a physical observation can both use this rule without being the same measurement practice.

To enforce this solution, the following rules apply:

-   **A17-R1 (Canonical term).** In all normative models and specifications, the measured aspect **SHALL** be referred to as a **Characteristic**. “Axis” and “Dimension” are not technical substitutes for the measured aspect.

-   **A17-R2 (Entity vs. relation subtype).** Each Characteristic **MUST** declare its intended _arity_. An **Entity-Characteristic** applies to exactly one bearer (e.g. _Temperature_ of a reactor, _Evolvability_ of a software module), whereas a **Relation-Characteristic** applies to an ordered tuple of two or more bearers (e.g. _Distance_ between two sensors, _Coupling_ between modules, _Agreement_ among reviewers). The arity is part of the definition and **must be explicit** wherever it’s not obvious from naming.

- **A17-R3 (Characteristic space).** When several Characteristics form a declared space, identify their slots, Scales and admissible values under A.19. State the constraints and additional structure required by its use. Use A.3.3.CC when compatible combinations must be constructed: it selects variables and constraints and compares implicit descriptions, parametrizations and finite sets. A.3.3 completes the state and transition account when the question concerns modeled change.

- **A17-R4 (Lexical guardrails).** When naming the measured aspect, its scale, its value or position, or an evaluative result, normative text **SHALL** use the corresponding governed term: Characteristic, Scale, Unit, Level/Value, Coordinate, Score, Normalization or ScoringMethod. Do not use axis, dimension, metric, grade or property as an undeclared substitute for those constructs. A disciplinary term naming another defined subject keeps that meaning; a mathematical dimension or metric, for example, is not renamed Characteristic. A Plain alias may be used when its mapping is clear. Apply E.10 to an unresolved lexical question.

- **A17-R5 (Symbol policy).** The **Γ_** prefix is reserved for algebraic operators under E.10:8.3 and E.10.P. Each operator retains its defining laws, including those for holonic composition or a declared scale-lawful fold under A.19.ULSAM. **𝒢** denotes a ScoringMethod from Coordinates to a Score. Documents **SHALL NOT** reuse Γ for a ScoringMethod.

- **A17-R6 (Scale order and preference).** For an ordered Scale, use its order to compare values of the Characteristic: a higher temperature value means hotter. A use that ranks values by desirability **SHALL** declare its preference rule, such as higher-is-better, lower-is-better, a target or range, or another ordering. Describing or comparing magnitudes requires no preference rule.

- **A17-R7 (Scoring against preference).** A ScoringMethod **SHALL** state how its score order represents the declared preference. Where one input is higher-is-better or lower-is-better, improving that input while holding the others fixed **MUST NOT** worsen the score, for admissible inputs under the stated conditions. Target-based preference is checked against its declared target or loss rule; the preferred direction may change across the target. A quantity calculation or unit conversion uses its measurement relation and Scale rules under A.18/C.16.

- **A17-R8 (Arity declaration).** Authors **SHALL** identify whether a Characteristic applies to exactly one bearer or to an ordered tuple of two or more bearers, and declare the tuple roles. For example, a cohesion Characteristic defined for one module is unary; a coupling Characteristic defined for an ordered pair of modules is relational. This arity declaration suffices for direct use; a receiving typed interface can require a C.3 classification when it needs a recurring membership decision.

- **A17-R9 (Relational readings).** For a Relation-Characteristic, the admissible subject tuples belong to its declared domain; the Scale supplies the admissible values attributed to those tuples. A reading **SHALL** identify the tuple it concerns and express its result on that Scale.

- **A17-R10 (Characteristic and description).** Distinguish the Characteristic from an episteme that describes it. A rubric, catalogue of levels or examples can contribute to that description; identify a separate episteme under C.2.1 when the receiving use needs its claim content, EntityOfConcern and effective ReferenceScheme.

#### A.17:4.1 - CharacteristicSpace & Change Reasoning *(Normative/Clarifying)*

**R17 - State-space use.** When a change model uses a CharacteristicSpace, declare its Characteristics, Scales, any applicable units and admitted combinations under A.19. Add topology, distance or another structure when the inference relies on it.

**R18 - Allowed changes and state recognition.** For a model of change, state the allowed continuations and their conditions through A.3.3. Use a state predicate or checklist when the receiving use needs to recognize a condition. A.2.5 governs the particular case of a condition on an assignment to a system role; a gate or assurance use supplies its own required support.

**I7 — Vector interpretation.** A vector may collect multiple Scale-specific Coordinates for multi‑Characteristic reasoning; composition into a single Score, if desired, requires an explicitly identified applicable **ScoringMethod 𝒢** on that vector.

