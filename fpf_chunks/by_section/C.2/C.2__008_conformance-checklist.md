---
chunk_kind: "child"
pattern_id: "C.2"
pattern_title: "Epistemic holon composition (KD-CAL)"
section_id: "C.2:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2/C.2__008_conformance-checklist.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "C.2 — Epistemic holon composition (KD-CAL)"
  - "C.2:7 — Conformance Checklist"
line_start: 41872
line_end: 41879
dependencies:
  - "A.1"
  - "A.10"
  - "A.6.3.RT"
  - "B.3"
  - "C.2.1"
  - "C.29"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "U.Episteme"
  - "U.View"
keywords:
  - "ClaimScope"
  - "F-G-R"
  - "Formality"
  - "Reliability"
  - "assurance"
  - "epistemic"
  - "evidence"
  - "knowledge"
  - "provenance"
  - "trust"
---

### C.2:7 - Conformance Checklist

1. **C2-1 (Episteme constitution and neighbors).** Every `U.Episteme` **MUST** satisfy C.2.1 constitution through exact claim content, one exact EntityOfConcern, and one effective `U.ReferenceScheme`. Empirical grounding and edition are stated through their separate C.2.1 relations. Viewpoint selection and `U.View` conformance use E.17.0; representation uses C.29/A.6.3.RT; publication occurrence, form, and carrier use E.17/E.24.PUB. None is treated as an episteme slot or identity component merely because a record or notation places it beside the constitution values.
2. **C2‑2 (Coordinates).** Each episteme **SHALL** declare `[F,G,R]` with a brief rationale; **F** is `U.Formality ∈ {F0…F9}` per **C.2.3**, **exactly one episteme‑level F** computed as the **min over essential parts**. CL is declared for **pairs only**. A named notation scheme **MAY** use sub‑anchors (e.g., `F4[OCL]`, `F7[HOL]`), which **MUST** preserve the global order and **map to their parent anchor** from C.2.3.
3. **C2‑3 (Composition).** Authors **SHALL** choose Γ_mode (**series** vs **parallel**). For any justification **path** use **`R_eff(P) = max(0, min_i R_i − Φ(CL_min(P)))`**; for **parallel** independent lines to the *same claim*, take **`R(Γ) = max_P R_eff(P)`** (never exceeding the highest-R support line). Compute `F(Γ) = min` along the used paths. For **G**, use **path‑wise intersections** and then **SpanUnion({G_path}) constrained by support**. A traversal **MUST** name the actual scope-translation, notation, kind, plane, source-local, model-use, evidence-reuse, or other direct relation and apply only its declared congruence loss to `R`.
4. **C2‑4 (NotationBridge).** Multi‑notation representation components **SHOULD** register `NotationBridge` edges with CL and loss note; any cross‑notation reasoning **MUST** cite the bridge’s CL.
5. **C2‑5 (No action).** Epistemes **MUST NOT** be assigned actions; work is executed by systems in role.

