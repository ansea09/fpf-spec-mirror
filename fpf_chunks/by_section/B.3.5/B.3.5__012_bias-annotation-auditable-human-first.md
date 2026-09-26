---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
section_id: "B.3.5:10"
section_title: "Bias-Annotation (auditable, human-first)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__012_bias-annotation-auditable-human-first.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "B.3.5 — Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
  - "B.3.5:10 — Bias-Annotation (auditable, human-first)"
line_start: 42665
line_end: 42680
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:10 - Bias-Annotation (auditable, human-first)

The purpose of this section is to make **typical cognitive slips** visible and name the **counter-moves** an author or assurance reader should apply **in thought**—not with tools. These biases are generic; the remedies point to neighboring FPF guard-rails and patterns.

| Bias (name)                     | Symptom in the model                                                                                                          | Cognitive counter‑move (conceptual only)                                                                                                                                                                          | Where to check                                                       |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Formalism capture** | A trace, constructor expression, or `validationMode` is treated as the source of the direct relation or whole identity. | Recover the exact participants, direct relation occurrences, construction rule, and identity or reidentification rule first. Treat the trace as a current C.2.1 account and the mode as the author's assurance posture. | CC‑CT2R‑1, CC‑CT2R‑2, CC‑CT2R‑3; C.13 trace separation. |
| **Canonical inversion** | B.3.5 fields are demanded before direct use, or one assurance branch is imposed on every relation. | Use the direct claim first. After election, use the applicable branch: structural parthood or collection belonging takes its required axiomatic trace; other permitted claims may use inferential or postulate support. | CC-CT2R-2, CC-CT2R-3, CC-CT2R-5. |
| **Order/time leakage** | Inferring parthood from sequence, parallelism or interval inclusion alone. | Recover the independent part relation under A.15.1 or A.14 when it obtains, and keep Method/order/time claims separate. | B.1.5, C.27 and B.1.4; A.15.1 or A.14 for the exact part/phase claim. |
| **Notation lock‑in**            | Letting a diagram or syntax define the meaning (“it’s true because the diagram says so”).                                     | Enforce **Notational Independence**: meaning is defined in prose/maths; renderings are illustrative only.                                                                                                         | Part E guard‑rail on notational independence.                        |
| **Unexamined mapping fit** | A composed claim relies on a mapping without inspecting preserved and lost distinctions. | State the exact mapping, its applicability and loss. Use a numeric reliability consequence only when the receiving model establishes its meaning and calculation; ordinal CL alone is insufficient. | B.3 and the direct mapping or representation pattern. |
| **Collection/composition swap** | A belongs-to predicate is used as `PartOf`, or a part claim is used as collection belonging, and reliability is carried over as if both were one construction. | State collection belonging and constructive parthood separately under A.14. When both obtain, keep both claims and their different `set` and `sum` accounts. | A.14 and C.13. |
| **DesignRunTag chimera**          | Mixing design‑time and run‑time evidence into one “assurance” line.                                                           | Split the **scope** of the claim: `S ∈ {design, run}`; compare side‑by‑side rather than merging.                                                                                                                  | B.3:4.8 and its “Design/run chimera” anti-pattern. |

> **Reader reminder.** Bias audit is a **reading aid**. It never licenses tooling talk in Core; use the guard‑rails in Part E to keep semantics primacy and unidirectional dependence of layers.

