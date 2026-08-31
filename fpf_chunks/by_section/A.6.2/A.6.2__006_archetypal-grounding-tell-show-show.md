---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "Effect-free episteme morphing"
section_id: "A.6.2:5"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__006_archetypal-grounding-tell-show-show.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "A.6.2 — Effect-free episteme morphing"
  - "A.6.2:5 — Archetypal Grounding (Tell–Show–Show)"
line_start: 13725
line_end: 13806
dependencies:
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.9"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

### A.6.2:5 - Archetypal Grounding (Tell–Show–Show)

The examples below show how EFEM is intended to be used across the EntityOfConcern and Description-episteme boundary, specification-use refinements, and Viewpoint/MVPK publication lanes.

#### A.6.2:5.1 - Typed specification-use refinement `Specify_DescEp_SpecDesc` (species of EFEM)

*Context.* You have a `U.MethodDescription` for a safety check and want a more formal `U.MethodSpec` with checkable constraints or test-harness obligations about the same Method. Before calling the relation conservative, identify the exact claims that already support those constraints.

*Shape.*

* Domain: `X = U.MethodDescription` episteme with `entityOfConcernRef(X) : U.MethodRef`, `content(X) : U.ClaimGraph_D`, and `ReferenceScheme_D`; when the named engineering validation use selects viewpoint P, record that selection separately.
* Codomain: `Y = U.MethodSpec` episteme with the same `entityOfConcernRef(Y) = entityOfConcernRef(X)`, more structured `content(Y) : U.ClaimGraph_S`, and a more explicit ReferenceScheme. If the same named validation use continues, it preserves its selected viewpoint P separately.

`Specify_DescEp_SpecDesc` is a species of EFEM only when all of these hold:

* `entityOfConcernChangeMode(Specify_DescEp_SpecDesc) = preserve`. The shared Method establishes endpoint EntityOfConcern equality; the Method entity itself is not a logical premise.
* P1 — effect-free: it is the declared arrow between the two epistemes; any operation application that produces Y is separate.
* P2 — conservative: every behavioral claim, constraint, and test obligation in Y traces to exact claims in X, an additional named source episteme, or an independently current fact under its named relation and effective scheme.
* P3-P5 — category structure and scope: the declared arrows compose only when their exact endpoints and P3 mappings agree, and applicability is bounded by the named engineering scope, operating conditions, effective scheme, and any viewpoint selected for the named validation use.

If an author chooses a new threshold, acceptance condition, harness obligation, or other commitment not supported by that basis, Y has been strengthened and the proposed arrow fails P2. Identify the new assertion in Y's changed ClaimGraph. When an operation application or performed Work produced that strengthening, identify it separately; neither the new assertion nor its production becomes part of a conservative arrow.

This matches A.7 and E.10.D2: an EntityOfConcern and a Description episteme about it remain distinct. C.2.1 identifies the episteme by its complete claim content, exact EntityOfConcern, and effective ReferenceScheme; when a describing use or production relation matters, name that exact relation separately. This account needs no universal `EntityOfConcern -> Description` function and is not itself an episteme-to-episteme morphism. `Specify_DescEp_SpecDesc` is an optional EFEM species over a Description episteme after a specification-use or refinement gate is present. EFEM supplies only the conservative episteme-to-episteme laws; it does not grant specification use or make Specification a third peer in A.7.

#### A.6.2:5.2 - Internal normalisation of a View (species of EFEM, `entityOfConcernChangeMode = preserve`)

*Context.* In MVPK you compute an engineering view `V` of a system description; you then normalise the view (sort, factor, put equations into normal form) without changing what it says.

Let `X = V_raw`, `Y = V_norm`, both `U.EpistemeView` instances with the same:

* `entityOfConcernRef(X) = entityOfConcernRef(Y)` (same system);
* when grounding is current, the same exact grounding occurrence and grounding holon are found on both sides; this is an endpoint comparison, not a change made by `NormalizeView`;
* any viewpoint selected by the named normalization use is the same exact P for X and Y; this selection is outside episteme identity;
* `representationSchemeRef(X) = representationSchemeRef(Y)` (same notation).

The EFEM `NormalizeView : X→Y`:

* has `entityOfConcernChangeMode(NormalizeView) = preserve`;
* has a source-to-receiving ClaimGraph difference consisting only of the declared normalization. If an exact `EpistemeEditionRelation` or another neighboring relation matters, name its predicate and participants on each side and compare the endpoint facts; `NormalizeView` does not change that occurrence. An assertion such as “normalised at edition E” is part of Y's ClaimGraph and must pass P2;
* is effect-free and separately claims idempotence on the output-closed domain of valid `EpistemeView` values under the fixed scheme and normalization rules; equality means exact normalized ClaimGraph equality plus equality of all identity-bearing episteme values, and a fixture that composes `NormalizeView` with itself supplies the repeat witness (P4);
* is conservative (P2): no new claims, only re‑expression.

MVPK can then **assume** functoriality of such normalisations without re‑stating the EFEM laws.

#### A.6.2:5.3 - Retargeting sketch (`entityOfConcernChangeMode = retarget`)

*Context.* E.18 structural reinterpretation relates a physical-layout episteme to a functional-behaviour episteme. The EntityOfConcern changes from the physical assembly to the functional network.

Inside EFEM, this becomes a species with `entityOfConcernChangeMode = retarget`:
* input episteme describes `S₁` (e.g. a component hierarchy holon);
* output episteme describes `S₂` (e.g. a functional network holon);
* one exact arrow `r` relates the two endpoint epistemes under its declared formal rule, while a separate A.6.4 assertion `q` states the invariant, visible loss, bounded receiving use, conditions, support, and polarity;
* P2 checks only the formal consequence relation declared for `r`; any A.20 check on `q` evaluates the exact proposition in that separate assertion.

The details belong to A.6.4 and E.18; EFEM provides the generic discipline.

#### A.6.2:5.4 - Worked endpoint-value and relation-read profile (engineering SystemDescription episteme kind)
*(informative)*

To make the C.2.1 value and EFEM law discipline concrete, consider an engineering episteme of a dependent system-description kind whose exact EntityOfConcern is one `U.System`:

| Value named by the EFEM species | Kind or reference form | Use |
| --- | --- | --- |
| exact EntityOfConcern | `U.Entity` constrained to `U.System`; designated by `U.EntityRef` | identifies the system that the claims concern |
| claim content | `U.ClaimGraph` | carries the description or specification claims |
| effective ReferenceScheme | `U.ReferenceScheme` | makes the claims and their designations interpretable |

This table names the three values that identify an episteme; it is not a `RelationSignature` or SlotSpec table. `EntityOfConcernSlot`, `ClaimGraphSlot`, and `ReferenceSchemeSlot` are declaration-local SlotKinds only when the reusable C.2.1 `EpistemeConstitutionRelationSignature` is being inspected. An EFEM species states how the endpoint values compare. If its rule uses a selected viewpoint, empirical-grounding relation, or representation relation, it names the exact occurrence or use qualification separately and reads or compares the endpoint facts without changing the occurrence.

Two typical EFEM species over this kind are:
* `Specify_DescEp_SpecDesc_Sys : SystemDescription → SystemSpec` — an `EntityOfConcernChangeMode = preserve` species that:
  * relates independently identified source and receiving epistemes with the same exact EntityOfConcern, makes their effective ReferenceSchemes explicit, and cites any separately obtaining empirical-grounding relation or viewpoint selection only when the formal relation depends on it;
  * satisfies P2 only when every claim in the receiving specification is recoverable from exact source ClaimGraphs or independently current facts under named relations and schemes; the unchanged EntityOfConcern is an endpoint identity condition, not a proposition or additional premise;
  * satisfies C.2.1:7.1 by declaring its endpoint-value comparison, named relation-read profile, and change mode.

* `Normalize_EngView : EpistemeView → EpistemeView` — a view‑normalisation EFEM (again with `EntityOfConcernChangeMode = preserve`) that:
  * states how the formal relation uses the three C.2.1 identity values and makes the exact source-to-receiving ClaimGraph difference explicit; any difference between separately obtaining endpoint facts that it compares is named by the exact predicate and participants, and any normalization application remains separate;
  * is effect-free and separately claims idempotence on its output-closed engineering-view domain under the fixed scheme and normalization rules; equality means exact normalized ClaimGraph equality plus equality of all identity-bearing episteme values, and a composition fixture supplies the repeat witness (P4);
  * is conservative (P2) by construction: it never introduces new atoms about the selected system.

Concrete `A.6.3/A.6.4/E.17.*` patterns for engineering description and specification-use idioms state explicitly, under C.2.1:7.1 and `CC-EFEM.*`, which of the three C.2.1 endpoint values remain the same or differ and which exact separately obtaining relation occurrences their arrow rules read or compare.

