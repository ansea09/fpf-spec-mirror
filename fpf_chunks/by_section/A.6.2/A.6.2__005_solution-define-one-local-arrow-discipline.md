---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "Effect-free episteme morphing"
section_id: "A.6.2:4"
section_title: "Solution — define one local arrow discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__005_solution-define-one-local-arrow-discipline.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "A.6.2 — Effect-free episteme morphing"
  - "A.6.2:4 — Solution — define one local arrow discipline"
line_start: 13556
line_end: 13724
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

### A.6.2:4 - Solution — define one local arrow discipline

#### A.6.2:4.1 - Informal definition

> **Definition.** An **effect-free episteme morphism** is a local mathematical arrow `f : X -> Y` between two exact epistemes. Under its selected formal substrate, it states how claim content, the EntityOfConcern, and any material reference or representation scheme correspond. The arrow itself performs no Work, runs no mechanism, and creates no episteme.

This is a local mathematical class under C.29, not an admitted durable U-kind. The pattern keeps the short name **EFEM** for that class. A reusable A.6.0 FormalSubstrate signature may declare its vocabulary and P0-P5 laws, but that signature episteme is not the class and is not one arrow.

An arrow in this class:

* has exact domain and codomain epistemes identified under C.2.1;
* is effect-free: no Work, mechanism application, system change, or carrier mutation follows from the arrow;
* states the exact conservativity rule it claims;
* obeys the declared identity and composition laws; and
* declares the local two-value characteristic `EntityOfConcernChangeMode` as `preserve` or `retarget`.

Within the selected formal substrate, one arrow is identified by its exact domain, codomain, arrow rule or designator, and declared formal equivalence. Two arrows can have the same endpoints and still be different. Changing a claim about whether the same arrow is suitable for another use does not reidentify the arrow.

The ordinary FPF objects remain separate:

* `f` is the local mathematical arrow;
* the A.6.0 FormalSubstrate signature is a C.2.1 episteme declaring reusable vocabulary and laws for the arrow family;
* a C.2.1 assertion about the suitability of `f` for one use is another episteme whose claim content names that use, its conditions, and its polarity;
* an operation application and any Work that computes, authors, or changes an episteme are identified only when they actually occur.

The A.6.3 viewing branch has endpoint epistemes about the same EntityOfConcern. The A.6.4 retargeting branch has endpoints about independently different entities; a separate use assertion states the invariant, visible loss, receiving use, conditions, support, and polarity.

#### A.6.2:4.2 - Direct signature components (A.6.0 alignment)

When repeated use needs a reusable formal declaration, an A.6.0 `U.Signature(profile=FormalSubstrate)` episteme may declare this local arrow family. Its direct declaration components are:

```text
SubjectKind     = local formal type EpMorphism
RangedValueKind = admitted ordered-pair range over exact U.Episteme values satisfying the declared endpoint-kind constraints
ResultKind      = omitted; the arrow is the declared subject, not an operation result
Applicability   = selected formal substrate, admitted endpoint kinds, and arrow-family conditions
```

`SubjectKind` here is a type inside the selected formal substrate, not a durable FPF U-kind. Add `SliceSet` and `ExtentRule` only if one declared local type genuinely has slice-varying membership; do not use them to hide a use-specific suitability claim.

**Vocabulary.**

* `U.Episteme` — the exact domain and codomain values.
* `EpMorphism` — the local formal type of arrows in the selected substrate.
* `EntityOfConcernChangeMode = {preserve, retarget}` — a local two-value characteristic of one arrow, derived from its resolved endpoint EntitiesOfConcern rather than a durable U-kind.
* `Ep` — the selected category whose objects are the admitted exact epistemes and whose arrows are the admitted `EpMorphism` values. Call it a category only when it contains the required identities and is closed under every declared composition.
* `EoCBase` — the endpoint-only thin category used to compare EntityOfConcern identity. Its objects are the exact independently resolved EntitiesOfConcern represented in the substrate. Between every ordered pair of admitted objects `A,B` it has one formal endpoint arrow `u_{A,B}`; `u_{A,A}` is the identity, and composition follows endpoints. These arrows are not independently meaningful domain or world-side relations.
* `dom(f)` and `cod(f)` — the exact endpoint epistemes; `id_X` and `compose(g,f)` — the declared identity and composition operations.
* `α : Ep -> EoCBase` — the declared mapping on objects and arrows. `α(X)` is X's exact EntityOfConcern after `entityOfConcernRef(X)` resolves it. For `f : X -> Y`, `α(f)` is the unique endpoint arrow `u_{α(X),α(Y)}`. It deliberately forgets f's arrow rule; different Ep arrows with the same endpoint EntitiesOfConcern therefore have the same image.
For each arrow, recover the C.2.1 identity values of X and Y and state which identity-bearing values or ClaimGraph parts are preserved or differ. If the arrow rule uses a neighboring relation, name its exact predicate and participants on each side and state which endpoint facts it reads or compares. Equal or different endpoint profiles do not mean that the arrow changed a relation occurrence or made it obtain or cease; any actual relation change and producing application or Work remain under their direct patterns. `SubjectRef` remains only a legacy source projection; resolve it to the exact episteme and EntityOfConcern.

A claim that `f` is suitable for one exact use is a separate C.2.1 assertion. An actual operation application has its own declared argument and result bindings under A.6.1, and any system that performs it and any resulting Work remain under their direct patterns. Neither the signature nor the mathematical statement `f : X -> Y` supplies that occurrence.

**Laws and applicability.** P0-P5 below govern the local arrow class. A.6.5 SlotSpecs enter only when an exact reusable direct-relation declaration is current; they are not fields of X, Y, or `f`.

#### A.6.2:4.3 - Laws P0–P5 (normative)

All laws below test membership in the local EFEM arrow class under the selected formal substrate. They do not assert membership in a durable U-kind.

##### A.6.2:4.3.1 - P0 — Typed episteme, endpoint-value, and relation-read profile (C.2.1-grounded)

For any arrow `f : X→Y` presented as an effect-free episteme morphism:

1. **Typed epistemes.** `X` and `Y` are epistemes of declared kinds `K_X, K_Y : U.EpistemeKind`, each identified under C.2.1 by exact claim content, one EntityOfConcern, and one effective ReferenceScheme. Grounding and representation relations are added only when current; a viewpoint selected for a named describing use remains outside episteme identity.

2. **Value and use projection.** For each episteme `E`—and separately for a named describing use when one is current—EFEM laws may refer to:
   * `content(E) : U.ClaimGraph` — E's exact identity-bearing claim content;
   * `entityOfConcernRef(E) : U.EntityRef` — designates E's exact EntityOfConcern;
   * `selectedViewpointRef?(use) : U.ViewpointRef` — only when the named describing use selects one exact viewpoint; this is not a component of E's identity;
   * `referenceScheme?(E) : U.ReferenceScheme` — E's effective designation and interpretation scheme;
   * `representationSchemeRef?(E) : U.RepresentationSchemeRef` — only when an exact C.29 representation scheme and correspondence relation are current for E; this is not a C.2.1 identity component;
   * a separately current neighboring fact — name the exact `EpistemeEditionRelation`, exact A.10 evidence or provenance relation, or other governed predicate and its participants when the arrow family reads or compares it; do not collect these facts in a generic projection. If E asserts such a fact, that assertion is already part of `content(E)`.

   When grounding matters, name the exact grounding relation, its grounding holon, and the claims it covers; grounding is not another component of episteme identity.

3. **Derived `EntityOfConcernChangeMode` and subtype restriction.**
   Each admitted arrow receives its mode from its resolved endpoint EntitiesOfConcern:

   * `entityOfConcernChangeMode(f) = preserve` when X and Y concern the same exact entity; a current grounding relation remains a separately governed fact;
   * `entityOfConcernChangeMode(f) = retarget` when X and Y concern independently different entities. Any claim that f supports one receiving use is a separate A.6.4 assertion `q` with its own invariant, visible loss, receiving use, conditions, support, and polarity.

   The parent EFEM class contains both modes. A named species or subtype may admit only one mode, but that restriction does not by itself make the subtype closed under composition. Classify each composite again from its final endpoints under P3.
4. **Legacy SubjectRef and describing-use discipline.**
   For Description epistemes, including those admitted for specification use, resolve legacy `subjectRef(E)` to exact E and its EntityOfConcern. State which endpoint claim content, EntityOfConcern, and effective scheme are preserved or differ. When grounding or a selected describing-use viewpoint matters, name the exact occurrence or use qualification on each side and state which facts the rule reads or compares. The morphism changes no such occurrence; viewpoint selection is neither identity nor conformance.

##### A.6.2:4.3.2 - P1 — Effect-free arrow, separate execution

The mathematical statement `f : X -> Y` neither changes a system nor says that a system computed, authored, stored, transmitted, or published Y.

When a system actually measures, simulates, translates, normalizes, fits, or otherwise produces or changes an episteme, identify separately:

* the exact A.6.1 operation application and its argument and result bindings, when that declaration is current;
* the system and any performed Work;
* the affected or newly constituted episteme and its C.2.1 identity facts; and
* any production, evidence, publication, or reliance relation that actually obtains under its own direct governor.

The same arrow can relate already existing epistemes, or be used in several separately identified applications. Conversely, two applications do not become the same because they use the same arrow. No bare result or universal production relation follows from the arrow or its declaration.

##### A.6.2:4.3.3 - P2 — Claim conservativity (no unlicensed commitments)

Let `content_X = content(X)` and `content_Y = content(Y)`, with their effective ReferenceSchemes and exact EntitiesOfConcern. Interpret each ClaimGraph through its effective scheme. Name any additional exact source episteme, current fact, grounding relation, or scheme correspondence that the arrow rule actually admits; an entity or label by itself is not a claim premise. Then:

> Every assertion in `content_Y` must be recoverable as a logical consequence, conservative re-expression, selection, or declared aggregation of the identified source ClaimGraphs and exact admitted facts under the named schemes. This includes assertions about an episteme's edition, source, status, witness, provenance, or evidence. Calling an assertion metadata does not exempt it from P2.

An EFEM arrow may omit claims or conservatively reorganize and re-express them. It may not introduce an unsupported atomic commitment, silently widen claim scope, or cross a ReferencePlane without the exact relation required for that move.

A separately obtaining edition, provenance, evidence, or status relation remains outside episteme identity. If the arrow family compares such a relation across X and Y, name the exact predicate and participants on each side. The arrow records that comparison; it does not create or update the relation. If Y asserts the relation, that assertion is identity-bearing `content_Y` and must pass the same source-to-result trace as every other assertion.

Where `entityOfConcernChangeMode(f) = retarget`, the arrow declaration states its formal cross-entity correspondence; it does not itself establish conservativity for a receiving use. A separate A.6.4 assertion states the invariant, visible loss, bounded use, conditions, support, and polarity for that use. An ordinary time-to-frequency representation of the same signal instead routes through C.29 and A.6.3.RT. A Fourier relation enters a retargeting case only after C.2.1 independently identifies a different receiving EntityOfConcern.

##### A.6.2:4.3.4 - P3 — Category structure and EntityOfConcern mapping

Use this law only after the selected FormalSubstrate declares both categories and the mapping below. `Ep` has admitted exact epistemes as objects and admitted EFEM arrows as arrows. It is a category only when it contains the required identities and every composite of admitted arrows with a matching middle episteme. If that closure is absent, keep the individual arrows and do not claim this category or functor.

`EoCBase` is the endpoint-only thin category over the exact resolved EntitiesOfConcern represented in the substrate. For every admitted pair `A,B`, it contains one formal arrow `u_{A,B}`. Its only endomorphism at A is `u_{A,A}=id_A`, and `compose(u_{B,C},u_{A,B})=u_{A,C}`. This formal arrow records only endpoint identity or difference; it is not an F.9 Bridge, a domain relation, or a claim that any world-side relation obtains.

```text
α : Ep -> EoCBase
```

On objects, `α(X)` is the exact EntityOfConcern resolved through `entityOfConcernRef(X)`; the reference is only the means of resolution. For `f : X -> Y`, `α(f)=u_{α(X),α(Y)}`. Thus a preserve-mode arrow maps to the base identity even when f is not an identity arrow in Ep, while a retarget-mode arrow maps to the unique formal arrow between its different endpoint entities. `α` intentionally forgets the rule that distinguishes two Ep arrows with the same endpoint entities.

**Practitioner check.** Point to exact X, Y, and f; resolve both EntitiesOfConcern; and identify the resulting endpoint arrow. For a proposed composition, point to the exact middle episteme and the admitted composite, then check P0-P2 for that composite. If the family lacks a required identity or composite, use its individual arrows without claiming the category or functor. No extra proof or record is required unless the receiving use calls for one.

1. **Identities.** For each admitted episteme X, Ep contains `id_X : X -> X`. For every `f : X -> Y`:

   ```text
   dom(id_X) = X
   cod(id_X) = X
   compose(id_Y, f) = f = compose(f, id_X)
   α(id_X) = id_α(X)
   ```

   `id_X` preserves the episteme's claim content, EntityOfConcern, effective ReferenceScheme, and every other declared episteme value. A viewpoint selected for one named describing use remains a separate use qualification.

2. **Composition.** For admitted `f : X -> Y` and `g : Y -> Z`, Ep contains an admitted `h = compose(g,f) : X -> Z`; h must satisfy P0-P2. It also satisfies:

   ```text
   dom(h) = X
   cod(h) = Z
   α(h) = compose(α(g), α(f))
   compose(k, compose(g,f)) = compose(compose(k,g), f)
   ```

   The α equation is replayable from endpoints. For a retargeting round trip from entity A through B back to A, both sides are the unique base endomorphism `u_{A,A}=id_A`; this says nothing about inverse world-side relations or identical Ep arrow rules. The composite has `preserve` mode when X and Z concern the same exact entity and `retarget` mode when they concern different entities.

   A preserve-only or retarget-only subtype is not thereby closed under parent composition. A composite remains in that subtype only when its final mode and all additional subtype laws match; otherwise it remains an EFEM arrow in the parent class. A separate assertion says whether the composite suits one final receiving use and states its invariant, accumulated visible loss, conditions, support, and polarity.

3. **Scheme-aware composition.** If endpoint RepresentationSchemes or effective ReferenceSchemes differ, name the exact C.29 or A.6.3.RT correspondence used by each route and state the equality or declared equivalence that makes the two routes agree. Use `natural`, `oplax`, or similar terminology only when the substrate supplies the actual mapping, comparison arrow, diagram, and working probe. Otherwise state the required two-route agreement in ordinary language. Any witness episteme remains separately identified.

##### A.6.2:4.3.5 - P4 — Arrow and repeat boundary

The common EFEM model treats `f : X -> Y` as one arrow with exact endpoints, an arrow rule or designator, and declared formal equivalence. It does not treat every arrow as a function that can be evaluated on an object, and it makes no claim that a separately declared operation is deterministic. A concrete substrate may add an evaluation operation only after declaring its argument kind, result kind, and relation to these exact arrows; that extra operation is not part of the common EFEM laws.

No universal idempotence follows. A normalization or another endomorphism `f : X -> X` may separately claim a repeat law such as `compose(f,f) ≃ f` only when composition is defined on the declared domain, `≃` is the substrate's stated equivalence, and a working fixture or proof supplies the witness. This mathematical repeat claim is not evidence that an operation was executed twice.

##### A.6.2:4.3.6 - P5 — Formal domain and separate use conditions

Each arrow family states the formal domain in which its laws apply:

* the allowed kinds of the two exact endpoint EntitiesOfConcern;
* any exact grounding relations or endpoint facts that the arrow rule reads;
* the admitted RepresentationScheme and ReferenceScheme pairs and any C.29 or A.6.3.RT correspondence needed by the formal relation; and
* any ClaimScope constraint required by the arrow law itself.

If `X` or `Y` lies outside that domain, the arrow is not a member of this local family. This is distinct from an operation application being admitted or rejected. A use-specific scope, operating condition, selected viewpoint, invariant, visible loss, support, and polarity belong in the separate use assertion when they decide whether one arrow supports one receiving use; changing that assertion does not reidentify the arrow.

When the use also relates two exact F.17 local senses and the F.9 predicate obtains, cite that Bridge and a separate bounded-use claim. When it crosses a ReferencePlane, cite the applicable plane relation. If transport is performed, identify the A.6.1 application separately. Different labels, contexts, schemes, planes, or operating conditions alone create none of these relations.

