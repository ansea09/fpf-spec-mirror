---
chunk_kind: "child"
pattern_id: "A.14"
pattern_title: "Advanced Mereology: Components, Portions, Aspects & Phases"
section_id: "A.14:14"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.14/A.14__015_sota-echoing.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.14 — Advanced Mereology: Components, Portions, Aspects & Phases"
  - "A.14:14 — SoTA-Echoing"
line_start: 28529
line_end: 28567
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

The collection-belonging rule uses a constructional question: what is the collection, what gives it identity, and which relation actually obtains? A subject-specific rule supplies the belonging predicate.

| Source line | Useful contribution | Limit | A.14 decision and destination |
| --- | --- | --- | --- |
| Partridge et al., [the constructional turn](https://www.utwente.nl/en/eemcs/fois2024/resources/papers/partridge-et-al-taking-a-constructional-turn-to-radically-enrich-a-top-ontologys-foundation.pdf), and [BORO C-FORS 2025](https://research.borosolutions.net/boro-ontology/) | Set, sum, tuple, and assembly constructors have different outputs, dependence, and identity conditions. | BORO's extensional, 4D, and unrestricted-composition commitments are not FPF defaults. | **Adapt.** The collection rule in §4 and `CC-MEM-1` distinguish a collection's own belongs-to rule from a `C.13 sum`; `CC-MEM-2/3` require a separate constructive-part claim rather than deriving or prohibiting it from belonging. |
| Florio and Linnebo, [constructional ontology](https://www.utwente.nl/en/eemcs/fois2024/resources/papers/florio-linnebo-introduction-to-constructional-ontology.pdf), and Borgo and Righetti, [applied constructional ontology](https://doi.org/10.3233/FAIA250480) | Givens, constructors, inputs, and construction processes must be distinguished; set, sum, and ordered-pair constructions are not interchangeable. | The applied work is exploratory and does not supply FPF's domain-facing identity, admission, use, or history rules. Its plural membership is not a world-side belongs-to predicate. | **Adopt the explicit-choice obligation; reject predicate import.** The decision table and Step 5 ask for the entity, collection, and its own beginning, ending, recurrence, and history conditions. |
| Kit Fine, [*Towards a Theory of Part*](https://doi.org/10.5840/jphil20101071139) | Composition comes before derived part claims, and different operations have different application, identity, presence, and character principles. | Fine's broad use of *part* can also cover set elements or sequence places; that umbrella is too broad for a practitioner-facing FPF relation. | **Adopt operational priority; narrow the public result.** `CC-MEM-2` blocks both the inference from belonging to parthood and the inference that parthood is impossible; `CC-MEM-3` admits the second claim only after all six `A.1` matters pass. |
| Kit Fine, [*The Identity of Social Groups*](https://doi.org/10.5334/met.45) | Structured groups can persist through changing manifestations, and the same participants need not identify the same group. | An identity-through-change rule does not make a register, corpus, product series, or Suite a structured whole. | **Adopt the identity questions, not automatic embodiment.** `CC-MEM-1` requires the collection's identity and belonging history; the A.1 gate remains separate. |



The resulting collection alternatives are deliberately distinct:

- **Selected:** an ordinary subject-specific belongs-to sentence plus the collection's own rule.
- **Rejected:** one generic `MemberOf`, because it collapses formal inclusion, classification, participation, collection belonging, and constructive parthood.
- **Rejected for present public use:** one qualified generic collection-belonging predicate, because its qualifiers must recreate every subject rule.
- **Retained as a separate possible claim:** constructive parthood, but only when its direct relation obtains and all six `A.1` matters pass.

A.14 supplies no immediate cross-domain query key for all belongs-to relations; use `F.18` to name a narrower relation when repeated query, comparison, or declaration use justifies that extra vocabulary.

The other relations draw on the following bounded contributions. The cited models have different domains and identity commitments; A.14's rules are FPF adaptations.

- **Measured parts.** Krifka's historical [*Nominal Reference, Temporal Constitution and Quantification in Event Semantics* (1989)](https://semantics.uchicago.edu/kennedy/classes/s13/aspect/krifka89.pdf), §2, ties measurement to a specified part structure and restricts addition to non-overlapping parts. Tao's [*An Introduction to Measure Theory*](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-126-tao5-measure-book.pdf), §1.4.3, supplies the general limit: a nonempty set can have zero measure, so proper inclusion need not give strictly smaller measure. **Adapt:** :5.1 keeps POR-2 as an independent condition and gives one sufficient finite-measure case; POR-3 applies only to admitted disjoint joins. Same-stuff/content, compatible units, boundary identity and any conservation law remain separately stated conditions of the FPF use.
- **Temporal parts.** [BFO 2020](https://raw.githubusercontent.com/BFO-ontology/BFO-2020/master/21838-2/owl/bfo-core.owl), `BFO_0000139`, defines transitive temporal parthood between occurrents. The [OWL-Time Recommendation (2017)](https://www.w3.org/TR/2017/REC-owl-time-20171019/), §§4.2.23–4.2.35, distinguishes strict interval inclusion, equality and overlap. **Adapt:** :5.2 applies proper temporal restriction to a continuing holon under its own identity rule. That holon domain, identity condition, partition-only coverage and non-overlap, and identity-failure return are FPF choices. OWL-Time supplies interval relations; the subject pattern supplies holon identity.
- **Engineering product identity and composition.** [ISO 15926-2:2003](https://www.iso.org/standard/29557.html), §5.2.6 (accessible [standard excerpt](https://www.normsplash.com/Samples/ISO/123263834/ISO-15926-2-2003-en-2.pdf), pp. 108–113), distinguishes simple composition from arrangement and assembly, and functional continuity from matter/energy continuity. The same tank can satisfy both object criteria; a stream can instead have path-based identity. Its temporal-whole-part relation belongs to its own 4D model of possible individuals. **Adapt:** choose the identity criterion and composition relation before asserting a part claim. FPF's specific PortionOf conditions and resource conservation accounts come from :5.1 and the applicable domain, not from a blanket rule about all stocks or consumables in ISO 15926.
- **Engineering-model versions.** OMG's [*Systems Modeling API and Services 1.0* (March 2026)](https://www.omg.org/spec/SystemsModelingAPI/1.0/PDF), §§7.1.1–7.1.2 and 7.2.3, distinguishes a continuing `DataIdentity`, separately identified `DataVersion` values and commit history. **Adapt:** identify the compared endpoints and the history being asserted. These software identities do not supply C.2.1's episteme-identity test.
- **Provenance and research versions.** The historical [PROV-DM Recommendation (2013)](https://www.w3.org/TR/2013/REC-prov-dm-20130430/), §§5.2, 5.4 and 5.5, distinguishes revision, derivation, alternate and specialization relations. [Zenodo versioning](https://zenodo.org/help/versioning) distinguishes a version DOI from the concept DOI for all versions; its [file-correction policy](https://help.zenodo.org/docs/deposit/manage-files/#modify-files-after-publication) also permits bounded corrections without changing the DOI. **Adapt:** recover the content and provenance of each endpoint. FPF uses the C.2.1 identity triple and independently obtaining `EpistemeEditionRelation` for distinct epistemes; A.14 reserves `PhaseOf` for a proper temporal restriction of one unchanged episteme.

The catalogue keeps direct component, constituent, portion, bearer-dependent aspect, phase, and collection-belonging claims distinct, while a separately grounded constructive part claim remains possible without another universal relation vocabulary.


#### A.14:14.1 - Aspect branch application


For AspectOf, A.14 adapts the constructor-and-identity questions of Partridge et al. and Florio and Linnebo's Core Constructional Ontology: which bearer, facet rule, dependent aspect and identity conditions make this structural part? The bearer/facet conditions and required `StructPartOf` relation are FPF choices. Fine's historical composition-first treatment motivates identifying the composition operation before the part claim. A.14 adapts that line in `A.14:5.3`, the decision procedure, and `CC-ASP-1` through `CC-ASP-4`; `C.13 slice` remains an optional report, not the constructor of the aspect. The serious alternatives are routed rather than renamed: measured Characteristic (`C.16`/`A.19`), viewpoint or view (`E.17`), representation or projection (`C.29` or its direct pattern), selected partition, and temporal restriction (`PhaseOf`/`C.27.TA`). Identify the actual relation before reusing the word *aspect*.


