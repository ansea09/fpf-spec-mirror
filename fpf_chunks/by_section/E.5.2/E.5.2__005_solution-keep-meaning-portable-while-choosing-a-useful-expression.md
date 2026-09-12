---
chunk_kind: "child"
pattern_id: "E.5.2"
pattern_title: "Notational Independence"
section_id: "E.5.2:4"
section_title: "Solution - Keep meaning portable while choosing a useful expression"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.2/E.5.2__005_solution-keep-meaning-portable-while-choosing-a-useful-expression.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "E.5.2 — Notational Independence"
  - "E.5.2:4 — Solution - Keep meaning portable while choosing a useful expression"
line_start: 75415
line_end: 75435
dependencies:
  - "A.6.3.RT"
  - "C.2.8"
  - "C.37"
  - "E.5"
keywords:
  - "BPMN"
  - "UML"
  - "diagram"
  - "notation"
  - "semantics"
  - "syntax"
  - "tool-agnostic"
---

### E.5.2:4 - Solution - Keep meaning portable while choosing a useful expression

1. **Explain the meaning and operative use.**
   Normative content **SHALL** state the concepts, claims and conditions needed for its use, using prose and mathematics as appropriate. Explain the interpretation of meaning-bearing signs and relations. A diagram, calculus or learned vocal-gestural expression may carry a reasoning or construction step. When it does, explain the operation and its prerequisites locally or cite the guidance for that subject. The pattern about that subject or the applicable Method governs the reasoning or construction. The reader obtains the subject result by applying that Method. When changing representation scheme or reasoning medium, use A.6.3.RT to construct and compare the representation.

2. **State the semantic mapping.**
   When expressions are compared or one is translated, substituted or relied on as carrying the other's content, their semantic mapping **SHALL** be stated. Name the source expression and the expression being compared with it. Name their representation schemes when the rules matter to interpretation. State the correspondences for the claims and conditions needed by the intended use. If a relevant distinction is lost, state the loss and limit the equivalence claim accordingly. A meaning-preserving mapping leaves open what operations a reader can perform with each expression, with what preparation and effort.

3. **Reference the conceptual role.**
   If the Core cites a diagram, refer to its conceptual role, such as a boundary schematic, rather than making a file or syntax name part of the concept.

4. **Keep conceptual prefixes neutral.**
   Use E.10.P for the prefix registry and required anchors. A conceptual label's meaning **MUST NOT** depend on its expansion into a serialized name or URI. If a tool supplies such an expansion, describe the relation between the conceptual label and the tool's name or URI in Tooling or Pedagogy, and mark it informative.

5. **Keep conceptual forms distinct from tooling formats.**
   Cards, tables, conformance checklists and guards in the Core specify conceptual content and relations. Their data models, machine-checking formats and linters belong in Tooling. Core forms require no data-related or lint-specific notation. Ease of machine checking does not justify a Core concept or rule.

The first result is an expression whose meaning can be recovered, with an explanation of any reasoning or construction step it supports. Include a semantic mapping when the use compares it with another expression or depends on the content it carries from that expression.

If a claim changes, compare again with the named source expression; repair the correspondence or narrow the claimed equivalence and permitted use. Use A.6.3.RT to construct and compare a replacement when the intended operation is difficult or unavailable. If the representation scheme cannot express a needed distinction, select another scheme or redesign the scheme before claiming that the distinction is preserved.

