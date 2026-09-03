---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U-kind Names and SystemRoleKindDescription Labels"
section_id: "F.5:11"
section_title: "SoTA Decision for Precise, Readable Technical Names"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__013_sota-decision-for-precise-readable-technical-names.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "F.5 — Naming Discipline for U-kind Names and SystemRoleKindDescription Labels"
  - "F.5:11 — SoTA Decision for Precise, Readable Technical Names"
line_start: 94507
line_end: 94523
dependencies:
  - "A.10"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RSIR"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.3"
  - "C.3.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.24.UK"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
  - "G.6"
keywords:
  - "Plain and Tech designations"
  - "SystemRoleKindDescription label"
  - "U-kind name"
  - "local meaning"
  - "naming after ontology recovery"
  - "system-role-kind name"
---

### F.5:11 - SoTA Decision for Precise, Readable Technical Names

Source use was checked on 2026-08-20. The bounded question is: **after the object is recovered, what is the smallest naming result that stays technically precise, readable to a project reader, and honest about morphology and reuse?**

| Current line | Strong contribution | Limit at comparable one-name effort | FPF decision and receiving locus |
| --- | --- | --- | --- |
| [ISO 704:2022](https://www.iso.org/standard/79077.html) and [ISO 1087:2019](https://www.iso.org/standard/62330.html) | Separate objects, concepts, definitions, and designations; make concept relations and term formation inspectable. | Terminology work does not itself admit the FPF object, decide a system-role kind, make an assignment obtain, or state the direct use and publication boundaries. | **Adopt** naming after meaning, minimal generality, and inspectable term formation in sections 4.1-4.3 and checks `CC-F5-1` to `CC-F5-4`. **Reject** a preferred term or definition as object admission. |
| W3C Ontology-Lexica Community Group, [OntoLex-Lemon](https://www.w3.org/2016/04/ontolex/), 2016 Community Report | Separates lexical entry, written and morphological form, lexical sense, ontology reference, usage conditions, and sense relations. | A full lexical graph and syntax-semantics model is excessive for one local Tech/Plain pair, and its reference relation does not establish FPF object identity or reuse authority. | **Adapt** object-sensitive morphology and the separation of name, sense, and referent in sections 4.1-4.4. **Reject** mandatory full lexicon modeling; use F.18 only when durable naming actually needs a card. |
| [ISO 24495-1:2023](https://www.iso.org/standard/78907.html), current published plain-language standard | Requires written information that intended readers can find, understand, and use; it explicitly applies to technical writing and controlled languages. | Plain-language quality does not settle ontology, reference, or term identity, and a shorter familiar word can still widen the meaning. | **Adopt** one short Plain designation and reader-use check in section 4.2 and `CC-F5-4`. **Reject** simplification that changes the recovered value or removes a live distinction. |
| W3C [SKOS Reference](https://www.w3.org/TR/skos-reference/), Recommendation 2009 | Keeps preferred and alternative labels, notes, concepts, collections, and mapping relations distinct. | It is useful lineage for labels and aliases but does not model enough morphology or decide FPF kind, assignment, Work, evidence, or publication claims. | **Retain as lineage** for aliases and cross-local caution in rules 8-9 and `CC-F5-6`/`CC-F5-9`; do not treat a shared label or generic mapping as a Bridge or common referent. |

**Selected non-dominated contribution.** A bare preferred label is cheaper but can hide the wrong object and leaves a cold reader without a safe explanation. A full ontology lexicon is richer but normally costs more than one project naming decision needs. F.5 stops at one already recovered value, one Tech designation, and one short Plain explanation. The word form follows the kind of object, while explicit limits prevent the two labels from creating a second ontology. At that effort, the result is more usable than a formal-only name and more precise than an unexplained familiar word.

SysML is intentionally not used as a naming, ontology, or lineage authority here. Its notation does not settle the referent, local kind, description, assignment, participation, Method, Work, or readable term choice at issue.

Source-use boundary: external labels, Concept-Set rows, and citations are evidence for local meaning or common practice, not automatic Tech designations, admission decisions, or Work, result, and provenance identities. A source term becomes selected only after the exact value is admitted and the naming comparison passes; naming changes none of those objects.

