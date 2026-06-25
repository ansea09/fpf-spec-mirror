---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:8"
section_title: "Compatibility & cross‑references"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__010_compatibility-cross-references.md"
commit_sha: "6bbbb622859fbbcddc02b23ea76bee4dd71c6291"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:8 — Compatibility & cross‑references"
line_start: 34670
line_end: 34675
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

### B.3.5:8 - Compatibility & cross‑references

* **C.6 Proof and Inference Use Calculus (LOG‑CAL).** CT2R‑LOG supplies the **places to hang proofs/evidence** that C.6 formalizes.
* **B.3.3 (Assurance levels).** `validationMode` + presence/quality of `tv:groundedBy` are the **inputs** to compute `AssuranceLevel (L0–L2)`.
* **B.3.4 (Evidence ageing).** If an edge relies on **postulated evidence**, its confidence **decays** per that pattern until refreshed; **axiomatic** edges from `Γ_m` traces do not age, but their **inputs** (tokens) might.

