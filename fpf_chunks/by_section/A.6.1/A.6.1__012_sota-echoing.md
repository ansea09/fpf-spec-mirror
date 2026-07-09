---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
section_id: "A.6.1:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__012_sota-echoing.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "A.6.1 — U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind"
  - "A.6.1:11 — SoTA-Echoing"
line_start: 10801
line_end: 10812
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "B.3"
  - "C.16"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.18"
  - "E.20"
  - "F.18"
  - "U.BoundedContext"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Signature"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "AdmissibilityConditions"
  - "Bridge‑only"
  - "LawSet"
  - "Mechanism"
  - "OperationAlgebra"
  - "Transport"
---

### A.6.1:11 - SoTA-Echoing

| Source line | Source refs | Adopt, adapt, or reject | Effect in this pattern |
| --- | --- | --- | --- |
| Current scoped-effects and handlers work | Bosman, van den Berg, Tang, and Schrijvers, "A Calculus for Scoped Effects & Handlers", LMCS 20(4), 2024, arXiv:2304.09697; Matache, Lindley, Moss, Staton, Wu, and Yang, "Scoped Effects as Parameterized Algebraic Theories", ESOP 2024 extended version, arXiv:2402.03103. | Adopt and adapt: operations, equations, scopes, resources, handlers, and type information are separated rather than hidden in one implementation object. | `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, and context-local applicability are explicit surfaces. |
| Typed semantic translation and categorical data migration | Spivak and Schultz, *Seven Sketches in Compositionality* and CQL practice lines. | Adapt: typed translation and quotient ideas are useful, but cross-context use in FPF must be Bridge-only with Reliability penalties. | Mechanism morphism, quotient, product, and transport relations are explicit and bounded without admitting an extra root U-kind. |
| Policy-as-code and safety standards practice | Open Policy Agent and Rego practice; UL 4600:2020; ISO 21448 road-vehicle safety practice. | Adapt: guard predicates and safety conditions are reviewable only when context, window, and fail-closed behavior are explicit. | `AdmissibilityConditions` and `GammaTimePolicy` are separate from `LawSet`; evaluator tooling stays outside kernel semantics. |
| Session, typestate, and protocol-safety practice | Contemporary session-type and typestate practice after 2015. | Adapt: operation-sequence constraints matter, but they must be expressed as guards or laws rather than hidden automata in prose. | SlotSpecs, SlotKinds, and specialization-chain rules prevent positional or hidden-state drift. |
| Calibrated uncertainty and conformal prediction | Angelopoulos and Bates, "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification", arXiv:2107.07511; contemporary conformal-prediction and calibrated-uncertainty practice. | Adopt and adapt: uncertainty sets and calibration show why admissible comparison must preserve scale and uncertainty conditions. | Comparison mechanisms bind to measurement, scale, and scorer rules; partial orders stay set-valued unless the scorer is declared. |

Refresh this pattern when current work on effect systems, typed semantic translation, policy-as-code, safety standards, protocol types, calibrated uncertainty, characteristic-space comparison, or FPF's own signature, method, work, evidence, gate, and transport patterns changes the governing distinction.

