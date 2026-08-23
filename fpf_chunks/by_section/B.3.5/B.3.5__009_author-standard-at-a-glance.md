---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:7"
section_title: "Author Standard (at a glance)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__009_author-standard-at-a-glance.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:7 — Author Standard (at a glance)"
line_start: 38339
line_end: 38353
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

1. **Pick a Working‑Model relation** (ComponentOf/MemberOf/…); avoid raw `ut:PartOf` unless you are drafting meta‑level axioms. If no current publication choice or requirement elects CT2R-LOG, publish that direct claim and stop.

2. **When CT2R-LOG is elected, attach `tv:groundedBy`**:

   * Structural and covered by the profile? → **must** be a `Γ_m` trace ID.
   * Epistemic? → `Γ_m` trace *or* evidence object.
3. **For a covered claim, declare `tv:validationMode`** (**postulate** / **inferential** / **axiomatic**).

> **What managers see:** nothing new in the graph picture.
> **What auditors get:** a reliable trail from every edge covered by the elected profile back to its inspectable construction or evidence account.

