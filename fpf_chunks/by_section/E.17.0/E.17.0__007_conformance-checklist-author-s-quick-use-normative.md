---
chunk_kind: "child"
pattern_id: "E.17.0"
pattern_title: "U.MultiViewDescribing - Viewpoints, Views & Correspondences"
section_id: "E.17.0:6"
section_title: "Conformance checklist (author’s quick use)  (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.0/E.17.0__007_conformance-checklist-author-s-quick-use-normative.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "E.17.0 — U.MultiViewDescribing - Viewpoints, Views & Correspondences"
  - "E.17.0:6 — Conformance checklist (author’s quick use)  (normative)"
line_start: 68936
line_end: 68960
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.4"
  - "A.7"
  - "C.2.1"
  - "E.10"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemeSlotRelation"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
  - "U.ViewpointBundleLibrary"
keywords:
---

### E.17.0:6 - Conformance checklist (author’s quick use)  *(normative)*

When defining a new `U.MultiViewDescribing` species or using it in a discipline pack:

1. **Declare the EntityOfConcernClass.**
   *Explicitly state `EntityOfConcernClass ⊑ U.Entity` and ensure all families restrict `EntityOfConcernSlot` accordingly.*

2. **Define the viewpoint set Σ.**
   *List `U.Viewpoint` instances (possibly via a `U.ViewpointBundle`) with stakeholder families, concern entries, allowed EpistemeKinds, and conformance rules.*

3. **Require DescriptionContext for Description-episteme and specification-use cases.**
   *Ensure every `…Description`/`…Spec` episteme in the family has `DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩` and that `ViewpointRef ∈ Σ`.*

4. **Specify admissible EpistemicViewing species.**
   *List the `U.EpistemicViewing` profiles used to derive views; declare their Applicability profiles and assert they are entityOfConcern‑preserving (EV‑6).*

5. **Attach CorrespondenceModel where needed.**
   *Whenever cross‑view consistency matters, introduce a `U.CorrespondenceModel` episteme and reference it from any `U.CorrespondenceEpistemicViewing`.*

6. **Separate describing from publication.**
   *Check that pattern text does not treat EntityOfConcern-to-Description or specification-use refinement as “publication”, and that any talk of literal `publication face/form` or `interop publication form` `publication-face kind` values or carriers is clearly delegated to MVPK/publication-face-kind discipline.*

7. **Respect SlotKind, ValueKind, and RefKind discipline.**
   *Use `*Slot` only for SlotKinds, `*Ref` only for RefKinds and fields; avoid `Subject`/`Object` roots in episteme types; use `EntityOfConcernSlot` and `viewpointRef` instead.*

