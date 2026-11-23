---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:6"
section_title: "Rules and Invariants (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__007_rules-and-invariants-normative.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:6 — Rules and Invariants (normative)"
line_start: 115490
line_end: 115521
dependencies:
  - "A.10"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.3.RT.OE"
  - "A.6.9"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.24.PUB"
  - "E.8"
  - "F.9"
  - "F.9.1"
  - "U.View"
keywords:
---

### E.17:6 - Rules and Invariants (normative)

**Local publication-composition test.** For a claim about specified objects, arrows and forms, check the applicable local properties. For a law over a category, use the domain-wide conditions below.

1. `identity`: `Emit_s(id_X)` is the identity face morphism for `FaceObj_s(X)`;
2. `composition witness`: compare the face for `g o f` with the composition of the faces for f and g under the selected equality. A verified match supports this pair. A failed comparison leaves the composition claim unavailable for this pair.
3. `no-new-claim diff`: compare the meaning and conditions of the face with the selected source episteme, including any paraphrase, pin or conservative construction.
4. `monotone promotion`: a richer face adds fields, pins, or typing without retracting or strengthening the source claim;
5. `scope non-widening`: `U.PublicationScope` stays within the claim or work scope used by the selected description.

For the optional formal profile, declare the source objects and arrows in scope, the target face category for each form `s`, and the equality used there. Give the rule that sends each object X to `FaceObj_s(X)` and each source arrow `f : X -> Y` to an arrow `Emit_s(f) : FaceObj_s(X) -> FaceObj_s(Y)`. Specify its action on the information retained by the face. If two source inputs have the same face representation but require different represented outputs, that information alone cannot determine the proposed action (C.29.1:4.4).

1. **Functoriality and typing per face.**
   * For each object X in the claimed domain, `Emit_s(id_X) = id_{FaceObj_s(X)}`.
   * For every composable pair `X -f-> Y -g-> Z` in that domain, `Emit_s(g o f) = Emit_s(g) o Emit_s(f)`. Derive the laws from the action on arrows, check the identities and all pairs of a finite domain, or define the action on a generating presentation and show that it respects its defining relations and extends to the specified action. A use concerning one composite can end at its verified equality.
   * If `f : X -> Y`, then `Emit_s(f) : FaceObj_s(X) -> FaceObj_s(Y)` is total in the selected formal substrate. An ill-typed composite blocks that formal claim. Weakening conformance does not repair it.
2. **Face-promotion coherence.**
   * If `s <= t`, the t-face is a more explicit publication form for the same selected source claims.
   * For a natural promotion give a component `PromoteFace[s->t]_X : FaceObj_s(X) -> FaceObj_t(X)` for every object. For every arrow `f : X -> Y`, establish `PromoteFace[s->t]_Y o Emit_s(f) = Emit_t(f) o PromoteFace[s->t]_X`. For functors on the stated domain, checking the squares on generators suffices when they generate all arrows. For a claim about just one arrow, its square is sufficient.
   * Identity and composition of `PromoteFace` follow the selected formal substrate. `AssuranceLane` is outside the default formality chain.
3. **Source episteme and construction.**
   * Every `Emit_s` use names the source episteme edition. It resolves a `publicationViewpointRef` only when the selected episteme is claimed as a `U.View` or the formal operation's definition depends on that viewpoint.
   * When another episteme is constructed from the source, use A.6.3 to identify that source-to-receiving construction relation. The face constructor is not a species of `U.EpistemicViewing`, and A.6.3 does not establish `U.View` membership.
   * Changed claim content, EntityOfConcern, or effective reference scheme identifies another episteme under C.2.1. Changed form, carrier, or publication occurrence does not by itself.
4. **Pin discipline.** Numeric or comparable claims used from a face retain the unit, scale, reference-plane, and edition pins required by the applicable characteristic and measurement patterns.
5. **Publication is not work.** Build, rendering, upload, or delivery is `U.Work` only when each performer has its A.13 core and A.15.1 independently admits the dated occurrence. F.6 enters only when the publication account also consumes precise assignment-bound attribution through the same obtaining A.13 assignment; missing or failed F.6 alone leaves independently admitted Work intact.
6. **Publication and carrier separation.** E.24.PUB identifies the selected episteme edition, publication occurrence, expression, reusable form and carrier separately. A.10 supplies the evidence/provenance source-to-use path, G.6 supplies addressable path citation, slicing, and local refresh, and B.3 supplies any assurance claim.
7. **Cross-context and reference-plane use.** For a semantic crossing, recover the F.17 endpoint senses, F.9 Bridge, and separate bounded-use claim. For a plane-dependent value, retain the characteristic, selected `ReferencePlane`, and applicable transfer or comparison rule. Add A.10 or B.3 only when reliance is current; an optional F.9 `CL` summarizes evidence strength and never grants use. Visual juxtaposition and scheme difference alone establish none of these claims.
8. **PublicationScope discipline.** For a face use v selecting episteme E, `PublicationScope(v)` does not exceed the claim scope on which that publication relies. A capability description may also cite a work scope, but the publication scope does not grant work admissibility. `PromoteFace` does not widen either scope.

The equations are conceptual-form constraints on the optional morphism-publication profile. They do not turn face symbols, formulas, or diagrams into world-side relations, viewpoints, views, publication occurrences, or work.

