---
chunk_kind: "child"
pattern_id: "A.6.REL"
pattern_title: "Relation Obtaining and Individuation: Distinguish Occurrences When Needed"
section_id: "A.6.REL:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.REL/A.6.REL__012_sota-echoing.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "A.6.REL — Relation Obtaining and Individuation: Distinguish Occurrences When Needed"
  - "A.6.REL:11 — SoTA-Echoing"
line_start: 16019
line_end: 16041
dependencies:
  - "A.6.0"
  - "A.6.5"
  - "C.2.1"
  - "C.29"
  - "E.24"
  - "E.24.UK"
  - "F.18"
keywords:
---

### A.6.REL:11 - SoTA-Echoing

#### A.6.REL:11.1 - Ontological SoTA and constructional sources

This pattern uses these sources to constrain its account of occurrence existence and identity. They provide ontological comparisons, not notation selection.

| Ontological source | What it contributes | Use and boundary in this pattern |
|---|---|---|
| Florio and Linnebo, [Introduction to Constructional Ontology](https://www.utwente.nl/en/eemcs/fois2024/resources/papers/florio-linnebo-introduction-to-constructional-ontology.pdf), 2024 | Separates constructors, inputs, construction process and output identity. | Section 4.3 recovers the acting System, enacted Method, inputs and performed Work when the direct rule makes that Work constitutive. Creating a row or assertion alone supplies no such construction. |
| Borgo and Righetti, [Towards Applied Constructional Ontology](https://doi.org/10.3233/FAIA250480), 2025 | Tests constructional reconstruction of foundational ontologies and exposes conceptual, structural, completeness and consistency questions; it is an early applied step, not a finished recipe. | The construction branch requires a recoverable direct rule rather than treating an inherited representation or taxonomy as its own justification. |
| Partridge, [BORO Ontology](https://borosolutions.net/boro-ontology), C-FORS 2025 presentation | Presents a 4D extensional, categorical and constructional ontology with an ontology-evolution method. | Temporal extent and constituting occurrences contribute here only when the direct identity rule includes them. This use does not import universal 4D identity, unrestricted composition or BORO's category architecture. |
| Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint | Provides a foundational-ontology implementation with differentiated relational-aspect and reification patterns. | Section 4.4 distinguishes relation, assertion, reifier and optional relator. The OWL implementation supplies no independent proof of FPF occurrence existence or identity. |
| [OntoUML Relator](https://ontouml.readthedocs.io/en/init-ontouml/classes/sortals/relator/index.html), specification lineage | Models a relator as a dependent truth-maker for a material relation. | This lineage comparison helps delimit the optional relator branch: the direct material ontology must supply the relator, its participant-dependence relations and identity rule. |

#### A.6.REL:11.2 - Representation and implementation stress tests

This pattern uses these sources to test whether the selected ontological distinctions can be represented and used. They do not determine what relation occurrences exist or how they are identified.

| Representation or implementation line | Distinction tested | Bounded use in A.6.REL |
|---|---|---|
| [TypeDB 3.x `links` statement](https://typedb.com/docs/typeql-reference/statements/links/) | A query can expose a relation variable with named source-language *role players*, while shorthand remains available when the represented relation instance need not be referenced. That source term denotes neither an FPF system-role kind nor a system-role assignment. | This representation supports a readable direct relation and a separately referenced instance. It does not establish the FPF relation kind, obtaining condition or identity rule. |
| [RDF 1.2 Concepts](https://www.w3.org/TR/rdf12-concepts/), Candidate Recommendation Snapshot, 7 April 2026 | Distinguishes a proposition expressed by a triple term, assertion of a triple and reifiers used for further statements. | Sections 4.4 and 5.3 keep proposition, assertion and reifier distinct. Graph syntax and reifier identity supply no world-side identity rule. |

