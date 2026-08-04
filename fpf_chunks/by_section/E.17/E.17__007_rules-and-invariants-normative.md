---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:6"
section_title: "Rules and Invariants (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__007_rules-and-invariants-normative.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:6 — Rules and Invariants (normative)"
line_start: 80549
line_end: 80580
dependencies:
  - "A.15.4"
  - "A.22"
  - "A.6.2"
  - "A.6.3"
  - "A.6.9"
  - "A.7"
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

**Publication-composition local test bundle.** A face that claims compositional publication passes five local tests:

1. `identity`: `Emit_s(id_X)` is the identity face morphism for `FaceObj_s(X)`;
2. `composition witness`: the face for `g o f` matches the composition of the faces for f and g, or is marked non-compositional or explanatory-only;
3. `no-new-claim diff`: comparison with the selected source episteme shows only formatting, indexing, pinning, or conservative construction;
4. `monotone promotion`: a richer face adds fields, pins, or typing without retracting or strengthening the source claim;
5. `scope non-widening`: `U.PublicationScope` stays within the exact claim or work scope used by the selected description.

For composable arrows `X -f-> Y -g-> Z` and exact `s,t` in `F_face`:

1. **Functoriality and typing per face.**
   * `Emit_s(id_X) = id_{FaceObj_s(X)}`.
   * `Emit_s(g o f) = Emit_s(g) o Emit_s(f)` only when the face carries the local witness.
   * If `f : X -> Y`, then `Emit_s(f) : FaceObj_s(X) -> FaceObj_s(Y)` is total in the selected formal substrate. An ill-typed composite blocks that formal claim; it is not repaired by weakening conformance.
2. **Face-promotion coherence.**
   * If `s <= t`, the t-face is a more explicit publication form for the same selected source claims.
   * `PromoteFace[s->t]_X : FaceObj_s(X) -> FaceObj_t(X)` is natural in X.
   * Identity and composition of `PromoteFace` follow the selected formal substrate. `AssuranceLane` is outside the default formality chain.
3. **Source episteme and construction.**
   * Every `Emit_s` use names the exact source episteme edition and exact publication viewpoint reference.
   * When another episteme is actually constructed from the source, A.6.3 may govern that source-to-receiving relation. The face constructor is not a species of `U.EpistemicViewing`, and A.6.3 does not establish `U.View` membership.
   * Changed claim content, EntityOfConcern, or effective reference scheme identifies another episteme under C.2.1. Changed form, carrier, or publication occurrence does not by itself.
4. **Pin discipline.** Numeric or comparable claims used from a face retain exact unit, scale, reference-plane, and edition pins under their direct characteristic and measurement patterns.
5. **Publication is not work.** Build, rendering, upload, or delivery is exact `U.Work` performed by a system under exact role and method relations. A face, emitter symbol, view episteme, or publication occurrence does not act.
6. **Publication and carrier separation.** E.24.PUB identifies the selected episteme edition, publication occurrence, form, and presentation carrier separately. Provenance and assurance relations remain under A.10, G.6, and B.3.
7. **Cross-context and reference-plane use.** When a face makes a current bridge or translation claim, recover the exact contexts, senses, bridge, and governing relation. Visual juxtaposition and scheme difference alone establish none of them.
8. **PublicationScope discipline.** For a face use v selecting episteme E, `PublicationScope(v)` does not exceed the claim scope on which that publication relies. A capability description may also cite a work scope, but the publication scope does not grant work admissibility. `PromoteFace` does not widen either scope.

The equations are conceptual-form constraints on the optional morphism-publication profile. They do not turn face symbols, formulas, or diagrams into world-side relations, viewpoints, views, publication occurrences, or work.

