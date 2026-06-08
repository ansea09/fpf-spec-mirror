---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme — Epistemes and their slot graph"
section_id: "C.2.1:6"
section_title: "Interaction with EntityOfConcern and Description-episteme boundary, specification use/refinement, and DescriptionContext  (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__007_interaction-with-entityofconcern-and-description-episteme-boundary-specification-use-refinement-and-descriptioncontext-normative.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "C.2.1 — U.Episteme — Epistemes and their slot graph"
  - "C.2.1:6 — Interaction with EntityOfConcern and Description-episteme boundary, specification use/refinement, and DescriptionContext  (normative)"
line_start: 34381
line_end: 34422
dependencies:
  - "A.1"
  - "A.6.2-A.6.4"
  - "A.6.5"
  - "A.7"
  - "B.1.3"
  - "C.2"
  - "E.10.D2"
  - "E.17"
  - "E.17.0-E.17.2"
  - "E.18"
keywords:
---

### C.2.1:6 - Interaction with EntityOfConcern and Description-episteme boundary, specification use/refinement, and DescriptionContext  *(normative)*

C.2.1 is the **episteme-side slot schema** that `EntityOfConcern` / Description-episteme discipline (A.7, E.10.D2) relies on. The link is made via `DescriptionContext`, not by treating EntityOfConcern value, Description epistemes, and specification use/refinement as layers, carriers, or peer ontology classes.

#### C.2.1:6.1 - DescriptionContext over C.2.1 components

For any episteme that is a **Description** in the sense of E.10.D2, including a Description episteme admitted for specification use, the field `subjectRef : U.SubjectRef` is interpreted as a **DescriptionContext triple**:
```
DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩
```

where:
* `EntityOfConcernRef : U.EntityRef` — fills `EntityOfConcernSlot` (ValueKind `U.Entity`, species often constrained via EntityOfConcernClass ⊑ `U.Entity`).
* `BoundedContextRef : U.BoundedContextRef` — points to the context that fixes vocabulary, units, and legal inferences for this description (E.10.D1).
* `ViewpointRef : U.ViewpointRef` — fills `ViewpointSlot` (ValueKind `U.Viewpoint`) and determines which concerns, role-bearing system families, stakeholder groups, and conformance rules apply.

**Normative requirement (DESCCTX-13).**
For every `…Description` episteme, and every `…Spec` use admitted by neighbouring specification use/refinement gates:
1. `subjectRef` **SHALL** be decodable to a well‑formed DescriptionContext triple.
2. `EntityOfConcernRef` from that triple **SHALL** be identical to the field `entityOfConcernRef` that fills `EntityOfConcernSlot` in the corresponding `U.EpistemeCard`/`U.EpistemeView`.
3. `ViewpointRef` in DescriptionContext **SHALL** agree with `viewpointRef` in the episteme card or be uniquely derivable from a `U.ViewpointBundle` in E.17.1 (with the derivation rule documented).

EntityOfConcern values such as `U.System`, `U.Method`, `U.Role`, or `U.Episteme` appear in C.2.1 as values of `EntityOfConcernSlot` when an episteme describes, views, or retargets them. They are not the Description episteme produced by that use. The `EntityOfConcern` / Description-episteme boundary separates the EntityOfConcern value from the Description episteme; specification use/refinement is a separate gated use or refinement of that Description episteme, not a third peer ontology class. This boundary does not ban epistemes from being EntityOfConcern values.

**Example.** A formal postulate theorem in physics can be a Description episteme about the behaviour of a physical grounding holon. Its `EntityOfConcernSlot` points to the physical grounding holon, or to the exact behavior, method, or work entity only when a governing pattern has selected that entity under concern; its claim graph carries the theorem, postulates, and derivation; its formal language belongs to formality and publication-expression discipline. It becomes a specification only if a bounded use assigns specification force, such as acceptance criteria, harness checks, normative invariants, C.16 measurement criteria, or verification use. Formal notation alone does not change the slot graph into a third `Specification` ontology class.
#### C.2.1:6.2 - EntityOfConcern-to-Description morphism and specification-use exit over C.2.1

* **Describing (`Describe_EoC_DescEp : EntityOfConcern -> DescriptionEpisteme`).**
  Produces an episteme whose:
  * `content : U.ClaimGraph` encodes the descriptive claims about the `EntityOfConcern` value,
  * `entityOfConcernRef` points to the EntityOfConcern value,
  * `groundingHolonRef` (if present) fixes where the description is evaluated or tested,
  * `viewpointRef` selects the describing viewpoint.

  `Describe_EoC_DescEp` is **conformant** to A.6.2 but not an Ep→Ep morphism (domain is the `EntityOfConcern` value, codomain is a Description-side `U.Episteme`). C.2.1 provides the **codomain schema** and ensures that the resulting Description has a valid DescriptionContext.

C.2.1 does not decide that a Description episteme has become a Specification. If a bounded use formalises, constrains, test-harnesses, accepts, or publishes a Description episteme as a specification, the governing pattern must name the exact specification-use gate: A.6.2 for effect-free episteme refinement, C.2.3 for formality and checkability, A.21 or the relevant gate/acceptance pattern for harness and acceptance force, C.16 for measurement criteria, E.17 for publication expression, and E.10 for suffix discipline. The C.2.1 requirement is only that the Description episteme keeps the same `entityOfConcernRef`, `BoundedContextRef`, and `ViewpointRef` unless an retargeting or viewing pattern named by value declares otherwise.

C.2.1 does **not** define the full `EntityOfConcern` / Description-episteme boundary or the specification-use gates; it only insists that any `...Description` episteme, and any `...Spec` use admitted by neighbouring gates, must:
* implement `U.EpistemeCard` or `U.EpistemeView` **with** `content`, `entityOfConcernRef`, `groundingHolonRef?`, `viewpointRef?`, and `referenceScheme?` fields, and
* wire these fields into `subjectRef` as DescriptionContext.

