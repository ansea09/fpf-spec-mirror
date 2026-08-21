---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:6"
section_title: "Rules and Invariants (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__007_rules-and-invariants-normative.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:6 — Rules and Invariants (normative)"
line_start: 78563
line_end: 78594
dependencies:
  - "A.10"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.2"
  - "A.6.3"
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
   * Every `Emit_s` use names the exact source episteme edition. It resolves an exact `publicationViewpointRef` only when the selected episteme is claimed as a `U.View` or the formal operation's definition actually depends on that viewpoint.
   * When another episteme is actually constructed from the source, use A.6.3 to identify that source-to-receiving construction relation. The face constructor is not a species of `U.EpistemicViewing`, and A.6.3 does not establish `U.View` membership.
   * Changed claim content, EntityOfConcern, or effective reference scheme identifies another episteme under C.2.1. Changed form, carrier, or publication occurrence does not by itself.
4. **Pin discipline.** Numeric or comparable claims used from a face retain the unit, scale, reference-plane, and edition pins required by the applicable characteristic and measurement patterns.
5. **Publication is not work.** Build, rendering, upload, or delivery is `U.Work` only when A.15.1 admits the dated occurrence; F.6 then identifies the assignment under which each performer acted. Test any local system-role-kind classification separately. A short face may omit identifiers its bounded use does not need. A face, emitter symbol, view episteme, or publication occurrence does not act.
6. **Publication and carrier separation.** E.24.PUB identifies the selected episteme edition, publication occurrence, form, and presentation carrier separately. A.10 supplies the evidence/provenance source-to-use path, G.6 supplies addressable path citation, slicing, and local refresh, and B.3 supplies any assurance claim.
7. **Cross-context and reference-plane use.** For a semantic crossing, recover the F.17 endpoint senses, F.9 Bridge, and separate bounded-use claim. For a plane-dependent value, retain the characteristic, selected `ReferencePlane`, and applicable transfer or comparison rule. Add A.10 or B.3 only when reliance is current; an optional F.9 `CL` summarizes evidence strength and never grants use. Visual juxtaposition and scheme difference alone establish none of these claims.
8. **PublicationScope discipline.** For a face use v selecting episteme E, `PublicationScope(v)` does not exceed the claim scope on which that publication relies. A capability description may also cite a work scope, but the publication scope does not grant work admissibility. `PromoteFace` does not widen either scope.

The equations are conceptual-form constraints on the optional morphism-publication profile. They do not turn face symbols, formulas, or diagrams into world-side relations, viewpoints, views, publication occurrences, or work.

