---
chunk_kind: "child"
pattern_id: "E.24"
pattern_title: "U.Ontic and Ontic Introduction Discipline"
section_id: "E.24:5.8"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24/E.24__013_sota-echoing.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "E.24 — U.Ontic and Ontic Introduction Discipline"
  - "E.24:5.8 — SoTA-Echoing"
line_start: 91187
line_end: 91216
dependencies:
  - "A.19.ECS"
  - "A.6.0"
  - "A.6.3"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.3.5"
  - "C.13"
  - "C.2.1"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.14"
  - "E.17.0"
  - "E.21"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "U.View"
keywords:
---

### E.24:5.8 - SoTA-Echoing

E.24 does not claim to replace ontology engineering, OWL-style formal ontology, or UFO-style foundational ontology. Its governing reason is the current FPF need for action-facing ontology compactness, plus a narrow SoTA echo:

| Source family | Current lesson for E.24 | FPF decision |
| --- | --- | --- |
| W3C [SKOS Reference](https://www.w3.org/TR/skos-reference/), 2009, and W3C [OWL 2 Primer](https://www.w3.org/TR/owl2-primer/), 2012. | Reference-baseline use, not a current-best SoTA claim: SKOS remains useful for controlled vocabularies, labels, broader and narrower relations, and concept schemes; OWL remains useful for classes, properties, individuals, axioms, and declarative semantics. | Adopt as baseline and adapt: do not present FPF ontology as one taxonomy tree. Use taxonomy relations where they fit, but introduce an ontic only when one exact identity rule and a minimal set of governed relations are needed across dependent use; add reusable declarations only for relations whose typed reuse is current. Current competitive guidance comes from the 2024-2026 modular ontology, interoperability, process-representation, and foundational-ontology rows below. |
| Modular ontology design patterns, MODL/MOMo, and commonsense ontology micropatterns, including [Shimizu and Hitzler 2024](https://arxiv.org/abs/2411.09601) and [Eells, Dave, Hitzler, and Shimizu 2024](https://arxiv.org/abs/2402.18715). | Current ontology-engineering work emphasizes reusable small ontology structures and pattern libraries, including LLM-assisted ontology engineering where modularity becomes more important, not less. | E.24 adapts the modular-pattern lesson: a durable ontic is a reusable FPF ontology unit with a pattern governing its direct relation set and with each dependent pattern paired to its exact reliance basis, not a local checklist copied across patterns. |
| [Qiang 2025, revised 16 June 2026 (v12)](https://arxiv.org/abs/2507.12311). | Overlapping and conflicting concepts block interoperability; the proposed framework combines design patterns, matching and versioning, and validation across the ontology lifecycle. | E.24 prevents shadow ontology and type explosion before matching and versioning becomes a rescue operation. It asks whether a proposed ontology unit becomes a durable ontic, is already governed by existing patterns, stays only as claims in a bounded local episteme, or is not admitted for use. |
| [Norouzi, Hertling, Waitelonis, and Sack 2025 process-representation ODP work](https://arxiv.org/abs/2509.23776). | Process ontologies and workflow ontologies often contain implicit design patterns; reuse suffers when those patterns are not explicit and accessible to domain experts. | Adopt as a caution for any process-like or temporal subject: a bounded local episteme carries only the claims and references needed for one use; reusable process, method, work, or temporal ontology stays explicit. If such material needs a durable ontic, state its direct relation kinds, participant meanings, obtaining and occurrence-identity rules, and subject patterns. |
| [Almeida, Guizzardi, Sales, and Fonseca 2026 gUFO](https://arxiv.org/abs/2603.20948); UFO and OntoUML role, relator, situation, and high-order type practice. | Current foundational-ontology work uses type typology, reification of intrinsic and relational aspects, situations, and high-order types to avoid naive taxonomic flattening. | Use as a stress comparator without importing its taxonomy or assignment architecture: route bare *role* through E.10.ROLE, recover which object is current, and follow A.2/C.3.2, A.2.1, A.6.5, or F.6 for that object's own rule content. |

For the working reader, these rows discipline named parts of the method. The SKOS and OWL baseline bounds taxonomy-only use in `E.24:4.1` and `E.24:5.4`; modular ontology patterns support the reusable ontic and subject-pattern move in `E.24:4.3` and `E.24:4.4`; interoperability work supports the stable-identity and currentness tests; process-representation work disciplines the workflow case in `E.24:5.2`; and gUFO supplies a stress comparator for recovering the exact object behind *role* without importing or repeating its ontology.

This SoTA echo justifies a bounded conclusion: FPF ontology can remain more compact than a taxonomy-only design when one governed subject needs stable identity, several coordinated direct relations, reusable declarations, and dependent patterns. It does not make every modular ontology pattern an FPF ontic. External source content changes an ontic-introduction decision only when an accepted source-use decision selects it for the subject under concern; current FPF use still depends on the resulting subject pattern.

Use external sources when one ontic or subject matter itself depends on a source tradition. Put that source decision in the DRR and in the pattern description containing the exact rule content for that subject matter. Do not make E.24 contain a borrowed external theory of every durable ontic.

#### E.24:5.9 - Currentness and Lowering Logic

Treat E.24 as current for ontic-introduction decisions while the subject patterns for relation-occurrence identity, reusable relation declarations, episteme identity, U-kind admission, wording-use restoration, and durable naming preserve the boundaries used here. Reopen one subject's ontic-introduction decision when one of these changes governs that subject:

- a new accepted FPF pattern changes direct relation identity, SlotSpec discipline, `EntityOfConcern` discipline, U-kind admission, or durable-name discipline;
- a bounded local episteme begins to be cited as if it governed a durable ontic;
- a planned pattern label acquires current subject pattern text and changes the ontic-introduction decision;
- dependent patterns start copying direct-relation rules or `RelationSignature` declarations instead of relying on their subject patterns;
- external source work governs the introduction method itself rather than one selected ontic or subject matter.

Do not let an unresolved ontology disposition constrain dependent use. Use `E.24:4.1` until the payload is selected for direct subject-assertion use, a bounded local episteme, or a durable ontic, or is explicitly stopped unresolved. Record source-use status independently: quote-only, reduced use, or stronger source use does not settle the payload's kind, identity, relation set, dependent-use reliance, or non-use boundary.

