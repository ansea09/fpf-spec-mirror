---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:5"
section_title: "Vocabulary & notation (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__007_vocabulary-notation-normative.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:5 — Vocabulary & notation (normative)"
line_start: 38304
line_end: 38320
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
  `tv:AliasOf` links a **public relation type** to the exact direct relation principle whose reading it carries (for example, `ComponentOf` points to the direct structural-component principle). The alias supports comparison; it neither defines an occurrence nor says that a `sum` expression produced the relation.

* **Grounding (per‑edge).**
 When this profile is elected for a published structural relation assertion, `tv:groundedBy` **MUST** point to one current C.2.1 construction-trace episteme in the `sum`, `set`, or `slice` form (**set** `validationMode=axiomatic`). For epistemic assertions covered by the profile it **MAY** point to an evidence object or a logical proof under `validationMode ∈ {inferential, postulate}`. The target supports replay of the assertion's basis; it creates neither the direct relation occurrence nor whole identity.

* **Trace family.**
  `Γ_m.sum`, `Γ_m.set`, and `Γ_m.slice` are the only C.13 narrative forms used for structural grounding accounts here. Their claim content reports assembly, collection, or aspect facts already governed elsewhere; no temporal or workflow form is added.

* **Validation flag.**
 `tv:validationMode ∈ {postulate, inferential, axiomatic}` is **required** on every edge or aggregation rule covered by this profile; **for structural edges in the profile `postulate` is disallowed**. A direct relation claim outside the profile has no B.3.5 field obligation.

