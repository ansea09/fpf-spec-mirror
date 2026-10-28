---
chunk_kind: "child"
pattern_id: "C.13"
pattern_title: "Constructional Mereology (Compose‑CAL)"
section_id: "C.13:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.13/C.13__006_solution.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "C.13 — Constructional Mereology (Compose‑CAL)"
  - "C.13:4 — Solution"
line_start: 57615
line_end: 57682
dependencies:
  - "A.1"
  - "A.14"
  - "B.3.5"
  - "C.2.1"
keywords:
  - "composition"
  - "construction account"
  - "mereology"
  - "part-whole"
  - "set"
  - "slice"
  - "sum"
---

### C.13:4 - Solution

#### C.13:4.1 - Solution sketch

Use the coarsest of three construction narratives that fits the object being described. In each case, write the shorthand only after the required facts are recoverable.

| Form | Practical reading | Facts required before the trace is truthful | What the form does not establish |
| --- | --- | --- | --- |
| `Γ_m.sum(parts)` | These exact constituents are assembled as this integrated whole. | one exact candidate whole; exact constituent entities; exact obtaining constructive part-relation occurrences; the assembly rule or method and its applicability; the candidate's identity or reidentification rule | that proximity, one drawing, a parts list, or the constituent set alone makes the whole; that every constituent change ends the whole |
| `Γ_m.set(elems)` | These entities belong to this collection under the collection's own rule. | one identified collection; identified entities; the belongs-to occurrences that obtain; the collection's belongs-to and identity rules | that the notation creates the collection or relation; component integration, acting-system organization, agency, A.1 holonhood, constructive parthood, or transitive belonging |
| `Γ_m.slice(entity, facet)` for an aspect; `Γ_m.slice(whole, portionBoundary)` for a measured portion | This aspect or portion is distinguished under the rule for its own relation. | For an aspect: the aspect, bearer, facet rule, obtaining AspectOf occurrence and identity rule. For a portion: the portion, whole, same-stuff/content basis, boundary, extensive measure and unit, obtaining PortionOf relation and identity conditions; see :4.1.1. | a facet establishing a measured portion, or an amount identifying a particular part without its boundary |

The familiar argument lists are readable shorthand, not complete ontological signatures. A complete use names the described object and states the direct facts beside the shorthand. Input order does not matter to the list of designated inputs, but assembly relations, rules, facets, portion boundaries and identity conditions do matter. The same input set under a different assembly can yield another whole.

A construction may obtain in the world even when no trace episteme has been written. When another piece of work needs an inspectable trace, materialize a C.2.1 episteme whose claim content names the described object; its constituents, entities that belong, bearer, or containing whole; the relation occurrences that obtain; the construction rule; and the identity conditions. Creating, editing, publishing or losing the account does not, by itself, establish a change in the construction it describes. A register update that also changes belonging must be assessed under the collection's constitutive rule.

Do not add a fourth constructor merely to carry time, execution order, parallelism, representation, evidence, or a domain label. Keep those claims with their direct patterns beside the construction account.

##### C.13:4.1.1 - A measured-portion account

Use the portion profile of `slice` when the receiving work needs to inspect a `PortionOf` claim. First identify the portion x and whole y under A.14:5.1. State what delimits x within y, why they are the same kind of stuff or content, the extensive measure μ and its unit or declared conversion, and the conditions under which both identities and the relation hold. An amount alone leaves the particular portion unidentified. These facts support the ordinary sentence “x is a portion of y under this measure and boundary rule.”

`Γ_m.slice(y, portionBoundary)` is optional shorthand for that account. Its second argument identifies the delimiting rule; it is not the aspect profile's facet argument. The result describes x and its already established PortionOf relation. For `ProperPortionOf`, also check `0 < μ(x) < μ(y)` under A.14:5.1; additivity alone does not establish it. For a joined portion, apply A.14's disjointness and admitted-join conditions before adding measures. A boundary, unit or measure change reopens the affected account; the direct identity rule decides whether the portion or whole continues.

In this constructed example, Billet-20 is an identified 20 kg stock. EndPortion-5 is the same material between its left end face and a specified cross-section inside that billet; its mass is 5 kg under the same measurement conditions. The account names both objects, those boundaries and the identity conditions of the stock and portion, so it supports `ProperPortionOf(EndPortion-5, Billet-20)` and the ratio 5/20 = 25%. An AspectOf or integrated ComponentOf claim requires its own relation grounds. If the indicated cross-section is unknown, “5 kg of Billet-20” gives an amount but leaves this particular portion unresolved. After physical separation, inspect the new boundaries and stock identity before carrying the earlier relation into the new state.

The same operation can describe identified report text spanning pages 1–10 of a 120-page edition under fixed pagination. That account establishes the text extent; a claim that those pages form a logical constituent needs its separate content relation. Repagination requires recovering the same text span and recalculating its page measure. The text may remain the same while its page-count account changes.

When B.3.5 is elected for the PortionOf assertion, link `tv:groundedBy` to this C.2.1 account and declare `validationMode=axiomatic`. Evidence needed to establish its boundary, mass or other facts remains subject to the receiving assurance question. Without that profile election, the direct relation remains usable under A.14.

#### C.13:4.2 - Normative Standard (high‑level)

* **C13-N1 — Direct facts first.** A C.13 trace is conformant only when every named constituent or collection entity and every named part, collection-belonging, or aspect occurrence is independently identified under its direct pattern.
* **C13-N2 — Whole identity stays direct.** The candidate whole follows its direct identity and reidentification rule. Equality of an input list or trace does not decide whether the existing whole continues or a new whole must be identified; a permitted constituent replacement can preserve one whole, while the same constituents under another assembly can form another whole.
* **C13-N3 — Construction form.** `sum`, `set`, and `slice` are the only C.13 forms. Reordering or duplicate designation does not change the listed inputs; it does not merge distinct entities or relation occurrences and does not erase assembly, facet, or portion-boundary differences.
* **C13-N4 — Mereological discipline.** Direct part patterns and A.14 govern acyclicity, antisymmetry, transitivity where applicable, recurrence, and occurrence identity. C.13 does not strengthen a direct relation by calculus convention.
* **C13-N5 — Trace separation.** A materialized trace is a C.2.1 episteme. Its notation or publication alone establishes neither the described entities and relations, their construction and identity rules, nor holonhood.
* **C13-N6 — A collection account is not component assembly.** `set` supports a collection account; it does not imply integrated assembly, `ComponentOf`, system agency, or A.1 recognition. Use `sum` only when constructive part relations and assembly are independently grounded.
* **C13-N7 — Elected assurance grounding stays with B.3.5.** A direct structural Working-Model edge may be published without a C.13 trace. When that publication elects B.3.5 or a named current requirement demands the profile, follow B.3.5 for the required `tv:groundedBy` link and declared `validationMode`; C.13 supplies the reconstructible trace content. Evidence, warrant, currentness, and reliance remain separate, and neither the link nor the mode replaces the direct construction or identity facts.
* **C13-N8 — Subject owners remain authoritative.** Method, work, and discipline construction may use C.13 only after their direct patterns identify actual parts and whole-forming relations. A selected dependent `U.Structure` does not become a whole, collection, aspect, or holon by selection or name.
* **C13-N9 — Transformation composition stays fail-closed.** A C.13 entity-construction trace, method decomposition, work decomposition, common changed referent, or temporal subdivision establishes neither transformation parthood nor a composite transformation. Without a direct transformation-composition governor, retain the independently identified changes and the exact blocker; infer neither composition nor atomism.

#### C.13:4.3 - Scope, applicability, terms & notation

Use Compose-CAL when the current claim concerns the construction of one exact system, episteme, method, work occurrence, discipline, collection, aspect, or measured portion and its direct part patterns already supply the required participants and obtaining relations. Do not apply it merely because a sentence contains `part`, a diagram groups nodes, or a selected structure organizes relations.

- **`Γ_m`** — the three-form notation for a C.13 construction narrative.
- **construction trace** — claim content that names the object being described; its inputs; the direct relations that obtain; its construction rule; and its identity conditions; when materialized, it is a C.2.1 episteme.
- **constructive part relation** — an exact world-side relation occurrence governed by its direct pattern; it is designated by the trace but not created by it.
- **assembly rule or method** — the rule explaining the construction: assembly from constituents, collection belonging, aspect distinction under a facet, or portion delimitation under a measure. The account cites that rule separately from the object it describes.
- **identity or reidentification rule** — the direct rule that identifies the described object and says which changes preserve or end it.

**Alias readiness.** These are common readable projections only when their direct relation meanings match the case:

- `ComponentOf` may accompany a `sum` construction;
- an ordinary belongs-to sentence may accompany a `set` construction; the collection's own pattern supplies its meaning, occurrence history, and any recurrence rule;
- `AspectOf` may accompany a `slice` construction;
- `PortionOf` uses the measured-portion profile of `slice` in :4.1.1, with A.14's same-stuff/content, measure and boundary conditions;
- `ConstituentOf` needs the direct logical or content-part relation; material mixtures use their exact portion or component owner.

The readable label and the trace answer different questions. The label states which direct relation obtains; the trace explains how the exact relation set supports this construction. Neither one is evidence merely by being present.

#### C.13:4.4 - Structural CT2R Typing-Grounding Use

When a target kind or logical representation must reuse both a `Γ_m` construction account and an independently grounded Working-Model relation, use `StructuralCT2RTypingGroundingUnfoldingStructureBlock` from `B.3.5` or an equivalent `A.22.CGUS` specialization. The block describes an independently selected `A.22` structure; any CGUS qualification is established separately. C.13 supplies the subject-side construction relations and states which mereological structure the target preserves or loses. Recover any required bridge, kind intent, proof, empirical evidence and admissible reuse under their governing patterns. Apply `A.7.1` when an inadequate working account must be diagnosed against the subject construction.

Use this split especially when a readable relation label such as ComponentOf, a collection's belongs-to predicate, AspectOf, ConstituentOf, or RepresentationOf is being reused beyond what its sentence warrants. The label does not by itself prove constructive grounding or a wider structural projection. Name the construction trace and Working-Model relation, the target kind or logical representation, any bridge used, the structure preserved and collapsed, and the proof or evidence relation required by the stronger claim. If the evidence instead diagnoses a mismatch that requires revision of the working ontology, apply `A.7.1`.

