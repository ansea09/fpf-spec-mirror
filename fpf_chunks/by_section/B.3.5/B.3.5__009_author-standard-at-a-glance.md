---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:7"
section_title: "Author Standard (at a glance)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__009_author-standard-at-a-glance.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:7 — Author Standard (at a glance)"
line_start: 35686
line_end: 35700
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

### B.3.5:7 - Author Standard (at a glance)

When you add or import a relation edge:

1. **Pick a Working‑Model relation** (ComponentOf/MemberOf/…); avoid raw `ut:PartOf` unless you are drafting meta‑level axioms.

2. **Attach `tv:groundedBy`**:

   * Structural? → **must** be a `Γ_m` trace ID.
   * Epistemic? → `Γ_m` trace *or* evidence object.
3. **Declare `tv:validationMode`** (**postulate** / **inferential** / **axiomatic**).

> **What managers see:** nothing new in the graph picture.
> **What auditors get:** a reliable trail from every published edge back to a principled constructor or an evidence pack.

