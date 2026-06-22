---
chunk_kind: "child"
pattern_id: "E.24"
pattern_title: "U.Ontic and Ontic Introduction Discipline"
section_id: "E.24:5.8"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24/E.24__013_sota-echoing.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "E.24 — U.Ontic and Ontic Introduction Discipline"
  - "E.24:5.8 — SoTA-Echoing"
line_start: 73760
line_end: 73787
dependencies:
  - "A.15"
  - "A.19.ECS"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "A.6.5"
  - "B.3.5"
  - "C.13"
  - "C.2.1"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.27.TA"
  - "C.29"
  - "C.30.STRAT"
  - "E.10"
  - "E.10.ARCH"
  - "E.14"
  - "E.18"
  - "E.2.DA"
  - "E.20"
  - "E.21"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### E.24:5.8 - SoTA-Echoing

E.24 does not claim to replace ontology engineering, OWL-style formal ontology, or UFO-style foundational ontology. Its governing reason is the current FPF need for action-facing ontology compactness, plus a narrow SoTA echo:

| Source family | Current lesson for E.24 | FPF decision |
| --- | --- | --- |
| W3C [SKOS Reference](https://www.w3.org/TR/skos-reference/), 2009, and W3C [OWL 2 Primer](https://www.w3.org/TR/owl2-primer/), 2012. | Reference-baseline use, not a current-best SoTA claim: SKOS remains useful for controlled vocabularies, labels, broader and narrower relations, and concept schemes; OWL remains useful for classes, properties, individuals, axioms, and declarative semantics. | Adopt as baseline and adapt: do not present FPF ontology as one taxonomy tree. Use taxonomy relations where they fit, but introduce an ontic only when stable identity and typed slot relation are required. Current competitive guidance comes from the 2024-2026 modular ontology, interoperability, process-representation, and foundational-ontology rows below. |
| Modular ontology design patterns, MODL/MOMo, and commonsense ontology micropatterns, including [Shimizu and Hitzler 2024](https://arxiv.org/abs/2411.09601) and [Eells, Dave, Hitzler, and Shimizu 2024](https://arxiv.org/abs/2402.18715). | Current ontology-engineering work emphasizes reusable small ontology structures and pattern libraries, including LLM-assisted ontology engineering where modularity becomes more important, not less. | E.24 adapts the modular-pattern lesson: a durable ontic is a reusable FPF ontology unit with a governing head pattern and dependent-pattern obligations, not a local checklist copied across patterns. |
| [Qiang 2025/2026 ontology-interoperability ecosystem](https://arxiv.org/abs/2507.12311). | Overlapping and conflicting concepts block interoperability; current approaches combine design patterns, matching and versioning, and validation across the ontology lifecycle. | E.24 prevents shadow ontology and type explosion before matching and versioning becomes a rescue operation. It asks whether a proposed head is a durable ontic, existing governing-pattern use, local use frame, or non-use. |
| [Norouzi, Hertling, Waitelonis, and Sack 2025 process-representation ODP work](https://arxiv.org/abs/2509.23776). | Process ontologies and workflow ontologies often contain implicit design patterns; reuse suffers when those patterns are not explicit and accessible to domain experts. | E.24 uses this as a caution for any process-like or temporal subject: do not hide process, method, work, or temporal material in a local use frame. If such material needs a durable ontic, write its own slot relation and governing pattern. |
| [Almeida, Guizzardi, Sales, and Fonseca 2026 gUFO](https://arxiv.org/abs/2603.20948); UFO and OntoUML role, relator, situation, and high-order type practice. | Current foundational-ontology work uses type typology, reification of intrinsic and relational aspects, situations, and high-order types to avoid naive taxonomic flattening. | E.24 keeps role-assignment, relation-slot, signature, interface-as-boundary, episteme and publication distinctions, and mechanism, method, and work distinctions as slot-governed ontology architecture rather than one taxonomic tree. |

This SoTA echo justifies a bounded conclusion: ontic-based FPF ontology architecture gives compactness and structure compared with a taxonomy-only design when the governed subject depends on identity, relation slots, dependent patterns, and action-facing use. It does not make every modular ontology pattern an FPF ontic. External sources govern the decision only when the DRR selects their payload for the specific ontic or subject matter under decision.

Use external sources when one ontic or subject matter itself depends on a source tradition. Put that source decision in the DRR and in the governing pattern for that subject matter. Do not make E.24 carry a borrowed external theory of every durable ontic.

#### E.24:5.9 - Currentness and Lowering Logic

Treat E.24 as current for ontic-introduction decisions only while the current FPF slot, precision-restoration, naming, and pattern-quality apparatus remain the governing source set. Lower E.24's current authority for a case when one of these changes governs that case:

- a new accepted FPF pattern changes slot discipline, `EntityOfConcern` discipline, or durable-name discipline;
- a local use frame begins to be reused as if it were a durable ontic;
- a draft locus becomes a current pattern and changes the ontic-introduction decision;
- dependent patterns start copying a slot relation instead of relying on the governing head pattern;
- external source work governs the introduction method itself rather than one selected ontic or subject matter.

Lower the decision before use when E.24 cannot decide among durable ontic, local use frame, existing governing-pattern use, quote-only source label, or reduced-use source label. A failed decision is not resolved by adding more fields; it is resolved by returning to `E.24:4.1` and settling which object, slot relation, semantic area, ontological neighborhood, and governing patterns actually govern the decision.

