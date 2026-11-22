---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
section_id: "B.3.5:11"
section_title: "Conformance Checklist (normative, author-facing)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__013_conformance-checklist-normative-author-facing.md"
commit_sha: "a9845e2c1029313e518c91a459ff7fab39e2831e"
heading_path:
  - "B.3.5 — Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
  - "B.3.5:11 — Conformance Checklist (normative, author-facing)"
line_start: 47722
line_end: 47736
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:11 - Conformance Checklist (normative, author-facing)

| ID                                              | Requirement                                                                                                                                                                                                                                   | Purpose                                                                   |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **CC-CT2R-1 (Canonical-first).**                | A relation published for readers **SHALL** be stated in Working-Model terms, such as `ut:ComponentOf` or an ordinary belongs-to sentence, as the canonical form; any constructive or logical justification is recorded as **grounding** (not as the definition).                                         | Preserve human-first canon and didactic primacy.                          |
| **CC‑CT2R‑2 (Mode declaration).**               | For every relation or rule covered by an elected B.3.5 profile, the author **SHALL** declare `tv:validationMode ∈ {postulate, inferential, axiomatic}` in prose. A relation outside the profile needs no B.3.5 mode. | Declare elected assurance intent without taxing ordinary use. |
| **CC‑CT2R‑3 (Structural axiomatic grounding).** | A covered structural parthood assertion uses `validationMode=axiomatic` and links to its applicable current C.2.1 `sum` or `slice` construction trace. The account reports independently grounded participants, occurrences, rule, and identity conditions. | Make elected structural assurance inspectable without turning it into a truth-maker. |
| **CC‑CT2R‑4 (No parthood from order/time alone).** | Authors **SHALL NOT** infer parthood from sequence, parallelism or temporal slicing alone. Any Work-part or proper-phase claim satisfies A.15.1 or A.14 independently; Method order and temporal relations use their patterns. | Preserve distinct relation meanings while allowing independently established temporal parts. |
| **CC‑CT2R‑5 (Collection vs part).** | Authors keep collection belonging under the collection's own rule distinct from every `PartOf` branch. A claim needs no profile fields; after B.3.5 election it uses `validationMode=axiomatic` and one current `C.13 set` trace. If constructive parthood also obtains, state and support that claim separately. | Prevent category errors without taxing ordinary belongs-to prose or prohibiting a stronger independently grounded claim. |
| **CC‑CT2R‑5a (Set trace reports).** | The elected set trace names the collection, the entity said to belong, the already established occurrence, the collection's own belongs-to rule, and the identity conditions. The set trace supplies no structural-composition reliability. | Keeps optional assurance from becoming ontology. |
| **CC‑CT2R‑6 (Mapping fit).** | Where a claim relies on a mapping or alignment, state its applicability and what follows in the direction used. Establish that distinctions lost in the mapping leave the receiving conclusion warranted, or recover the missing information. Any numerical adjustment requires a justified receiving model, compatible scale and calculation. | Make the reach of the inference inspectable. |
| **CC‑CT2R‑7 (Notational independence).**        | Core meaning **MUST NOT** hinge on any specific diagram or syntax; illustrative renderings, if present, are labelled *informative*.                                                                                                           | Ensure longevity and cross‑discipline portability.                        |
| **CC‑CT2R‑8 (Layer direction).**                | Present the readable Working-Model claim before its needed Mapping, Logical, Constructive or Empirical support. Authors **SHALL NOT** let assurance notation or record structure dictate the public vocabulary. If support defeats or narrows the claim, revise the claim under its defining pattern and expose the change.                                                  | Preserve unidirectional dependence of layers.                             |
| **CC‑CT2R‑9 (Claim and scope).** | State the relation claim and the use it serves. For an elected assurance profile, authors **SHALL** state the assurance claim and its scope. When tasked with choosing the relations, explain which distinctions the recipient needs and how the selected claims support the requested conclusion together. Identify the distinct subjects, evidence and conditions of any design and run claims used. | Connect the grounding of each assertion to the recipient’s use. |

