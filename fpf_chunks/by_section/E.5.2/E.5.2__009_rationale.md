---
chunk_kind: "child"
pattern_id: "E.5.2"
pattern_title: "Notational Independence"
section_id: "E.5.2:8"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.2/E.5.2__009_rationale.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "E.5.2 — Notational Independence"
  - "E.5.2:8 — Rationale"
line_start: 75868
line_end: 75882
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

### E.5.2:8 - Rationale
A notation can preserve meaning while changing which operations a reader can perform readily. Explaining interpretation, comparing expressions when needed, and retaining their operative use supports **P-1 Cognitive Elegance** and **P-2 Didactic Primacy**. Keeping conceptual meaning in the Core and implementation formats in Tooling preserves **P-5 FPF Layering**.

**SoTA question and choice.** How can framework content remain understandable across notations while an expression also supports reasoning or construction? Adopt recoverable interpretation of concepts, claims and conditions. Adapt the portability rule to expressions that carry an operation: explain their use and prerequisites, and compare the content whenever another expression is used as equivalent.

A serious alternative is a prose-first rule that treats diagrams and written calculi as secondary illustrations. It keeps verbal definitions accessible, but can exclude an operation from the normative account when the operation is performed through the expression. Reject that blanket restriction. For example, in the Euclidean construction in A.6.3.RT:5.1.a, the same segment participates as a radius and as a triangle side. The prepared expression helps the reader combine those relations. Its role needs an explanation of that operation, beyond a caption describing the picture.

A second alternative is to require one canonical notation. This can provide shared interpretation and manipulation rules within a practice whose readers have learned them. Retain that option for such a practice. Extending it across FPF would also require readers in other practices to acquire those conventions, even when another expression supports their task. Compare these choices for the same content, operation and reader preparation. The selected rule accepts the cost of explaining local conventions and mapping compared expressions in exchange for allowing the expression suited to the work. It claims no universal advantage in learning time or performance.

**Effect on this pattern.** Section 4, item 1 and CC-NI.2 require guidance for an operation-bearing expression. Item 2 and CC-NI.3 require comparison when content is carried between expressions; the pump and timing cases in §5 show preservation and consequential loss. The heatmap case limits a coarsened expression's use. These moves keep interpretation and usable operations together; subject Methods still supply the reasoning or construction.

**Source roles and limits.** Macbeth's [paper-and-pencil analysis](https://doi.org/10.1093/philmat/nkr006) (2011, especially pp. 16-18 and 31-42) supplies the constructive argument from prepared expressions and shared parts. Dutilh Novaes's *Formal Languages in Logic* (2012, §§3.2, 5.2 and 6.1) supplies the account of learned manipulation and interpretation; her discussion on p. 202 makes temporary disregard of meaning neither necessary nor sufficient for a cognitive gain. These are conceptual grounds for the selected line and its reader-dependent limits. They provide neither a universal notation-design procedure nor a comparative estimate of learning or performance across all readers and notations.

**Reopen the choice** if interpretation and mapping satisfy this rule yet a needed claim or operation remains unrecoverable, or if a canonical-notation alternative supports the same work for the intended readers with less total preparation and explanation. Reconsider the affected requirement. An incorrectly prepared expression instead calls for the local repair or source return in §4.

