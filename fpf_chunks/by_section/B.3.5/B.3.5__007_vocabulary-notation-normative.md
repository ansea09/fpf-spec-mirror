---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:5"
section_title: "Vocabulary & notation (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__007_vocabulary-notation-normative.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:5 — Vocabulary & notation (normative)"
line_start: 35156
line_end: 35172
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
  - "CT2R"
  - "Compose-CAL"
  - "assurance layer"
  - "constructive trace"
  - "grounding"
  - "working model"
---

### B.3.5:5 - Vocabulary & notation (normative)

* **Working-Model relations (front‑stage).**
 `ut:ComponentOf`, `ut:PortionOf`, `ut:AspectOf` are **publication-grade** sub-properties of `ut:StructPartOf` **(structural)**; `ut:MemberOf` is a sub-property of `ut:EpiPartOf` **(epistemic)**.

* **Alias principle (lexical).**
  `tv:AliasOf` links a **relation type** to its **generative rule schema** (e.g., “`ComponentOf` aliases the result of a `Γ_m.sum` with role=component”).

* **Grounding (per‑edge).**
 `tv:groundedBy` on an *edge instance* **MUST** point to a **Γₘ trace** (`sum|set|slice`) for **structural** edges (**set** `validationMode=axiomatic`); for **epistemic** edges it **MAY** point to an **evidence object** or a logical proof per declared `validationMode ∈ {inferential, postulate}`.

* **Trace family.**
  `Γ_m.sum`, `Γ_m.set`, `Γ_m.slice` are the only normative constructors for structural grounding; no temporal or workflow constructor is added here (time slices live in Sys‑CAL; parallelism via `set`).

* **Validation flag.**
 `tv:validationMode ∈ {postulate, inferential, axiomatic}` is **required** on every declared edge or aggregation rule; **for structural edges `postulate` is disallowed**.

