---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:1"
section_title: "Intent"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__002_intent.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:1 — Intent"
line_start: 39206
line_end: 39220
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

### B.3.5:1 - Intent

*Provide a single, human-facing family of **Working-Model** relations as the **public relation layer**, with explicit hooks for (G) grounding and (R) reliability, without exposing constructor jargon or overloading day-to-day authors.*

**What you get (manager/engineer view).**
 The same relations you already know (e.g., **ComponentOf**) remain the **public relation vocabulary**.

**What changes (auditor/ontologist view).**
* Each published edge carries two additional commitments:

  1. **`tv:groundedBy`** → points to a **reconstructible trace** (e.g., `Γ_m.sum`) whenever the edge is *structural*.
  2. **`validationMode ∈ {axiomatic, inferential, postulate}`** → declares how the author justifies the assertion.

This is the **alias‑plus‑grounding** split: **Compose‑CAL** builds the trace; **CT2R‑LOG** declares the alias pattern and links it; **Lang‑CHR** supplies the labels.

