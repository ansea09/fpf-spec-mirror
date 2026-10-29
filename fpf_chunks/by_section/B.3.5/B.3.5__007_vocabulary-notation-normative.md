---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
section_id: "B.3.5:5"
section_title: "Vocabulary & notation (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__007_vocabulary-notation-normative.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "B.3.5 — Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
  - "B.3.5:5 — Vocabulary & notation (normative)"
line_start: 45315
line_end: 45335
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:5 - Vocabulary & notation (normative)

* **Working-Model relations (front‑stage).**
 `ut:ComponentOf`, `ut:PortionOf`, and `ut:AspectOf` are publication-grade part relations under their direct A.14 rules. A collection uses the belongs-to predicate defined by the pattern for that collection; FPF has no public generic `ut:MemberOf` relation. Belonging is not a sub-property of `ut:PartOf`, `ut:StructPartOf`, or `ut:EpiPartOf`, but the same entities may separately stand in a constructive part relation when its own rule and all six A.1 matters pass.

* **Alias declaration (lexical).**
  `a tv:AliasOf t` states that local designation **a** denotes the same direct relation as accepted Tech designation **t** in the stated use. Both endpoints are designations. Identify the source or practice, effective scheme and local meaning under E.10:6.2.1; preserve the relation’s applicability and the roles and order of its participants. The direction points from the local expression to the Tech designation used to recover its meaning. Cite the defining passage, such as A.14 for `ComponentOf`, as the semantic source.

  A glossary sentence can make this declaration once for its stated use. An already clear Tech designation needs no additional alias. Apply F.17/F.18 when the naming task actually requires their records; an alias alone creates no need for a NameCard or SchemeSenseCell. E.10 separately governs the use of a Plain twin.

  To use an alias, recover the declared meaning and participant positions, then apply the direct relation’s rule to the assertion. Recheck the declaration when its meaning or use changes. A broader meaning, or an expression that reverses participant positions, needs its own account: for example, `hasComponent(whole, part)` expresses the inverse of `ComponentOf(part, whole)`. A bare alias declaration does not specify that reversal. When distinct local meanings require an actual semantic correspondence, use F.9; matching words alone leave that correspondence unresolved.

* **Grounding (per‑edge).**
 When this profile is elected for structural parthood, `tv:groundedBy` points to the applicable current C.2.1 construction trace and `validationMode=axiomatic`. When elected for collection belonging, it points to one current `C.13 set` trace under the collection's own rule and also uses `validationMode=axiomatic`. Other epistemic or constitutive claims may use a logical argument or evidence object under their permitted mode. Every target lets a reviewer inspect the assertion's basis.

* **Trace family.**
  `Γ_m.sum`, `Γ_m.set`, and `Γ_m.slice` are the C.13 forms used by the covered branches. `sum` and `slice` report structural-parthood constructions; `set` reports an already grounded collection and the belongs-to occurrences established under its own rule. Temporal and workflow claims retain their own patterns.

* **Validation flag.**
 `tv:validationMode ∈ {postulate, inferential, axiomatic}` is required on every claim covered by this elected profile. Structural parthood and collection belonging use `axiomatic` with their branch-specific current trace. A direct relation outside the profile has no B.3.5 field obligation.

