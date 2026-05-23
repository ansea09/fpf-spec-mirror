---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:4"
section_title: "Solution (thumbnail)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__005_solution-thumbnail.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:4 — Solution (thumbnail)"
line_start: 31329
line_end: 31352
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

### B.3.5:4 - Solution (thumbnail)

CT2R‑LOG introduces a **two‑link discipline** around each canonical edge:

1. **Alias link (concept‑level).**
   **Working‑Model relations** (e.g., `ut:ComponentOf`) are **alias patterns** over a general constructional principle. Denote by **`tv:AliasOf`**.

2. **Grounding link (evidence‑level).**
   Each **edge instance** carries **`tv:groundedBy`**:

   * **MANDATORY** for **all structural edges** (sub-properties of `ut:StructPartOf`): the target is a valid **`Γ_m` trace** from **Compose-CAL** (one of `sum`, `set`, `slice`). **Set** `validationMode=axiomatic`; **`postulate` SHALL NOT be used for structural edges**.
   * **Optional** for **epistemic edges** (e.g., `ConstituentOf`, `RepresentationOf`): if no `Γ_m` trace is appropriate, attach an **evidence object** whose admissibility is governed by the declared **`validationMode ∈ {inferential, postulate}`** (assurance rules).

2. **Validation flag (author intent).**
   Every declared edge or aggregation rule carries **`tv:validationMode`** with one of:
   * **`postulate`** — pragmatic working claim backed by observations;
   * **`inferential`** — reasoned consequence (proof outline);
   * **`axiomatic`** — constructive grounding via a `Γ_m.*` composition.

> **F–G–R alignment.**
> **F** (the published *Fact*): `:PumpA ut:ComponentOf :Skid12`.
> **G** (its *Grounding*): `:e123 tv:groundedBy :trace_Γm_sum_456`.
> **R** (declared *Reliability mode*): `tv:validationMode=axiomatic` → inputs B.3.3’s **AssuranceLevel** assessment.

