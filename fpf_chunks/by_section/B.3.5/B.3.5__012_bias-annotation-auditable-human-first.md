---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:10"
section_title: "Bias-Annotation (auditable, human-first)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__012_bias-annotation-auditable-human-first.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:10 — Bias-Annotation (auditable, human-first)"
line_start: 40294
line_end: 40309
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
| **Order/time leakage**          | Encoding sequence or phase as part‑whole edges.                                                                               | Apply **Strict Distinction**: order/time belong to Γ\_method and Γ\_time, not to mereology or CT2R relations.                                                                                                       | B.3 “keep order/time in their own lanes”; cross‑ref Γ\_ctx/Γ\_time.  |
| **Notation lock‑in**            | Letting a diagram or syntax define the meaning (“it’s true because the diagram says so”).                                     | Enforce **Notational Independence**: meaning is defined in prose/maths; renderings are illustrative only.                                                                                                         | Part E guard‑rail on notational independence.                        |
| **Congruence blindness**        | Composing strong parts through weak mappings without acknowledging the fit penalty.                                           | Make **edge‑fit first‑class**: reason about Congruence Level (CL) on connections; penalise low fit conceptually.                                                                                                  | B.3 universal aggregation skeleton (Φ(CL)); anti‑patterns list.      |
| **Collection/composition swap** | A belongs-to predicate is used as `PartOf`, or a part claim is used as collection belonging, and reliability is carried over as if both were one construction. | State collection belonging and constructive parthood separately under A.14. When both obtain, keep both claims and their different `set` and `sum` accounts. | A.14 and C.13. |
| **DesignRunTag chimera**          | Mixing design‑time and run‑time evidence into one “assurance” line.                                                           | Split the **scope** of the claim: `S ∈ {design, run}`; compare side‑by‑side rather than merging.                                                                                                                  | B.3 typed claim tuple & anti‑pattern “DesignRunTag chimera”.           |

> **Reader reminder.** Bias audit is a **reading aid**. It never licenses tooling talk in Core; use the guard‑rails in Part E to keep semantics primacy and unidirectional dependence of layers.

