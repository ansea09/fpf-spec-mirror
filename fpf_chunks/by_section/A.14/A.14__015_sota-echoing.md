---
chunk_kind: "child"
pattern_id: "A.14"
pattern_title: "Advanced Mereology: Components, Portions, Aspects & Phases"
section_id: "A.14:14"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.14/A.14__015_sota-echoing.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "A.14 — Advanced Mereology: Components, Portions, Aspects & Phases"
  - "A.14:14 — SoTA-Echoing"
line_start: 24538
line_end: 24572
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.2"
  - "A.2.1"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.5"
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.2"
  - "B.3.5"
  - "C.13"
  - "C.16"
  - "C.27.TA"
  - "C.29"
  - "C.3"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
keywords:
  - "AspectOf"
  - "ComponentOf"
  - "ConstituentOf"
  - "PhaseOf"
  - "PortionOf"
  - "aspect"
  - "belongs to"
  - "component"
  - "constituent"
  - "member"
  - "part"
  - "phase"
  - "portion"
---

### A.14:14 - SoTA-Echoing

This edition's collection-belonging rule follows the current constructional line: first identify what is being constructed and what gives it identity, then state the relation that actually obtains. It does not import a ready-made universal membership predicate.

| Source line | Useful contribution | Limit | A.14 decision and destination |
| --- | --- | --- | --- |
| Partridge et al., [the constructional turn](https://www.utwente.nl/en/eemcs/fois2024/resources/papers/partridge-et-al-taking-a-constructional-turn-to-radically-enrich-a-top-ontologys-foundation.pdf), and [BORO C-FORS 2025](https://research.borosolutions.net/boro-ontology/) | Set, sum, tuple, and assembly constructors have different outputs, dependence, and identity conditions. | BORO's extensional, 4D, and unrestricted-composition commitments are not FPF defaults. | **Adapt.** Solution item 5 and `CC-MEM-1` distinguish a collection's own belongs-to rule from a `C.13 sum`; `CC-MEM-2/3` require a separate constructive-part claim rather than deriving or prohibiting it from belonging. |
| Florio and Linnebo, [constructional ontology](https://www.utwente.nl/en/eemcs/fois2024/resources/papers/florio-linnebo-introduction-to-constructional-ontology.pdf), and Borgo and Righetti, [applied constructional ontology](https://doi.org/10.3233/FAIA250480) | Givens, constructors, inputs, and construction processes must be distinguished; set, sum, and ordered-pair constructions are not interchangeable. | The applied work is exploratory and does not supply FPF's domain-facing identity, admission, use, or history rules. Its plural membership is not a world-side belongs-to predicate. | **Adopt the explicit-choice obligation; reject predicate import.** The decision table and Step 5 ask for the entity, collection, and its own beginning, ending, recurrence, and history conditions. |
| Kit Fine, [*Towards a Theory of Part*](https://doi.org/10.5840/jphil20101071139) | Composition comes before derived part claims, and different operations have different application, identity, presence, and character principles. | Fine's broad use of *part* can also cover set elements or sequence places; that umbrella is too broad for a practitioner-facing FPF relation. | **Adopt operational priority; narrow the public result.** `CC-MEM-2` blocks both the inference from belonging to parthood and the inference that parthood is impossible; `CC-MEM-3` admits the second claim only after all six `A.1` matters pass. |
| Kit Fine, [*The Identity of Social Groups*](https://doi.org/10.5334/met.45) | Structured groups can persist through changing manifestations, and the same participants need not identify the same group. | An identity-through-change rule does not make a register, corpus, product series, or Suite a structured whole. | **Adopt the identity questions, not automatic embodiment.** `CC-MEM-1` requires the collection's identity and belonging history; the A.1 gate remains separate. |

#### Aspect branch application

For AspectOf, the BORO and CCO rows above supply the constructor-sensitive question: which bearer, facet rule, dependent aspect, and identity conditions make this structural part? Fine's composition-first pressure blocks a bare *aspect* label from deciding parthood. A.14 adapts that line in `A.14:5.3`, the decision procedure, and `CC-ASP-1` through `CC-ASP-4`; `C.13 slice` remains an optional report, not the constructor of the aspect. The serious alternatives are routed rather than renamed: measured Characteristic (`C.16`/`A.19`), viewpoint or view (`E.17`), representation or projection (`C.29` or its direct pattern), selected partition, and temporal restriction (`PhaseOf`/`C.27.TA`). This route is no worse for correctness and cheaper for a cold reader than a universal *aspect* kind; its cost is that the author must identify the actual relation before reusing the word.

The resulting collection alternatives are deliberately distinct:

- **Selected:** an ordinary subject-specific belongs-to sentence plus the collection's own rule.
- **Rejected:** one generic `MemberOf`, because it collapses formal inclusion, classification, participation, collection belonging, and constructive parthood.
- **Rejected for present public use:** one qualified generic collection-belonging predicate, because its qualifiers must recreate every subject rule and make the first move harder.
- **Retained as a separate possible claim:** constructive parthood, but only when its direct relation obtains and all six `A.1` matters pass.

At comparable correctness and temporal adequacy, the selected answer is no worse than the qualified or separately named alternatives and is cheaper for a cold reader and maintainer. A generic predicate looks cheaper only because it omits decisive conditions. The real cost is that A.14 supplies no immediate cross-domain query key for all belongs-to relations; use `F.18` to name a narrower relation when repeated query, comparison, or declaration use justifies that extra vocabulary.

The rest of the catalogue retains its own governing source lines:

- **Metrical mereology** advances motivate **PortionOf** with explicit μ and Σ-laws, preventing the classic “stuff as components” fallacy.
- **Temporal parts and identity through change** motivate **PhaseOf** as transitive proper temporal parthood, with nesting and overlap allowed, partition-specific coverage and non-overlap, and escalation when identity criteria fail.
- **Engineering product models**, including the ISO 15926 family, pressure authors to keep functional classification, physical product breakdown, and stocks or consumables distinct; A.14 routes those claims to their direct relations instead of one part tree.
- **Knowledge-episteme edition histories** in contemporary MBSE and open-science practice motivate explicit endpoint identities and provenance-preserving composition. FPF uses the C.2.1 identity triple and independently obtaining `EpistemeEditionRelation` for distinct editions; A.14 retains `PhaseOf` only for a proper temporal restriction of one unchanged episteme.

The net effect is a minimal-sufficient catalogue: direct component, constituent, portion, bearer-dependent aspect, phase, and collection-belonging claims stay distinct, while a separately grounded constructive part claim remains possible without another universal relation vocabulary.

Treat this source account as current for this edition. Reopen only the affected A.14 rule if a cited constructional source changes a distinction used here, a newer relation architecture provides the same claim correctness and history at lower reader or maintenance cost, or a direct consumer needs a meaning that the current rule cannot express. Recheck `A.14:5.3` and `CC-ASP-1` through `CC-ASP-4` for an AspectOf change; recheck Solution item 5 and `CC-MEM-1` through `CC-MEM-3` for a collection-belonging or separately grounded parthood change. An ordinary change to a bearer, facet rule, aspect occurrence, collection rule, belonging occurrence, or optional trace reopens only that claim and its support, not this source decision.

