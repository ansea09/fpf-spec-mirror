---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:8"
section_title: "Compatibility & cross‑references"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__009_compatibility-cross-references.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:8 — Compatibility & cross‑references"
line_start: 31284
line_end: 31289
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

* **B.3.2 (LOG‑use).** CT2R‑LOG supplies the **places to hang proofs/evidence** that B.3.2 formalizes.
* **B.3.3 (Assurance levels).** `validationMode` + presence/quality of `tv:groundedBy` are the **inputs** to compute `AssuranceLevel (L0–L2)`.
* **B.3.4 (Evidence ageing).** If an edge relies on **postulated evidence**, its confidence **decays** per that pattern until refreshed; **axiomatic** edges from `Γ_m` traces do not age, but their **inputs** (tokens) might.

