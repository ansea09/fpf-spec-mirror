---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:5"
section_title: "Vocabulary & notation (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__007_vocabulary-notation-normative.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:5 — Vocabulary & notation (normative)"
line_start: 39880
line_end: 39896
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:5 - Vocabulary & notation (normative)

* **Working-Model relations (front‑stage).**
 `ut:ComponentOf`, `ut:PortionOf`, and `ut:AspectOf` are publication-grade structural relations under their direct A.14 rules. A collection uses the belongs-to predicate defined by the pattern for that collection; FPF has no public generic `ut:MemberOf` relation. Belonging is not a sub-property of `ut:PartOf`, `ut:StructPartOf`, or `ut:EpiPartOf`, but the same entities may separately stand in a constructive part relation when its own rule and all six A.1 matters pass.

* **Alias principle (lexical).**
  `tv:AliasOf` links a **public relation type** to the exact direct relation principle whose reading it carries (for example, `ComponentOf` points to the direct structural-component principle). The alias supports comparison; it neither defines an occurrence nor says that a `sum` expression produced the relation.

* **Grounding (per‑edge).**
 When this profile is elected for structural parthood, `tv:groundedBy` points to the applicable current C.2.1 construction trace and `validationMode=axiomatic`. When elected for collection belonging, it points to one current `C.13 set` trace under the collection's own rule and also uses `validationMode=axiomatic`. Other epistemic or constitutive claims may use a logical argument or evidence object under their permitted mode. Every target supports replay of the assertion's basis; it creates neither the direct occurrence nor entity identity.

* **Trace family.**
  `Γ_m.sum`, `Γ_m.set`, and `Γ_m.slice` are the C.13 forms used by the covered branches. `sum` and `slice` report structural-parthood constructions; `set` reports an already grounded collection and the belongs-to occurrences established under its own rule. No form creates the facts it reports, and no temporal or workflow form is added.

* **Validation flag.**
 `tv:validationMode ∈ {postulate, inferential, axiomatic}` is required on every claim covered by this elected profile. Structural parthood and collection belonging use `axiomatic` with their branch-specific current trace. A direct relation outside the profile has no B.3.5 field obligation.

