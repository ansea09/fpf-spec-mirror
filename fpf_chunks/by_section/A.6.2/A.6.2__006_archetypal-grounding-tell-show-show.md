---
chunk_kind: "child"
pattern_id: "A.6.2"
pattern_title: "U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
section_id: "A.6.2:5"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.2/A.6.2__006_archetypal-grounding-tell-show-show.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "A.6.2 — U.EffectFreeEpistemicMorphing — Effect‑free morphisms of epistemes"
  - "A.6.2:5 — Archetypal Grounding (Tell–Show–Show)"
line_start: 13173
line_end: 13253
dependencies:
  - "A.1"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "C.2.1"
  - "C.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.Signature"
keywords:
---

### A.6.2:5 - Archetypal Grounding (Tell–Show–Show)

The examples below show how EFEM is intended to be used across the EntityOfConcern and Description-episteme boundary, specification-use refinements, and Viewpoint/MVPK publication lanes.

#### A.6.2:5.1 - Typed specification-use refinement `Specify_DescEp_SpecDesc` (species of EFEM)

*Context.* You have an informal `U.MethodDescription` for a safety check and want a more formal `U.MethodSpec` with test harness obligations, but **about the same method**.

*Shape.*

* Domain: `X = U.MethodDescription` episteme with
  `entityOfConcernRef(X) : U.MethodRef`, `content(X) : U.ClaimGraph_D`, and `ReferenceScheme_D`; when the named engineering validation use selects viewpoint P, record that selection separately.
* Codomain: `Y = U.MethodSpec` episteme with the **same** `entityOfConcernRef(Y) = entityOfConcernRef(X)`, more structured `content(Y) : U.ClaimGraph_S`, and a more explicit ReferenceScheme. If the same named validation use continues, it preserves its selected viewpoint P separately.

`Specify_DescEp_SpecDesc` is a species of EFEM:

* `entityOfConcernChangeMode(Specify_DescEp_SpecDesc) = preserve`.
* P1 — effect‑free: it transforms epistemes only.
* P2 — conservative: any behavioral claims in the Spec must be logical consequences of the informal Description and the exact Method that both epistemes concern. If the Spec adds a commitment not entailed by that basis, the operation is not a valid EFEM instance; identify the new claim as a separate C.2.1 episteme and state the operation, its entry condition, and its result under the rule that defines that operation.
* P3-P5 — functorial and scoped: specifications compose, and applicability is bounded by the named engineering scope, operating conditions, effective scheme, and any viewpoint selected for the named validation use.

This matches A.7 and E.10.D2: EntityOfConcern-to-Description (`Describe_EoC_DescEp`) is the strict-boundary describing step and is not itself an episteme→episteme morphism; `Specify_DescEp_SpecDesc` is an optional EFEM species over a Description episteme after a specification use/refinement gate is present. EFEM supplies the episteme→episteme laws for that refinement; it does not make Specification a third peer in A.7.

#### A.6.2:5.2 - Internal normalisation of a View (species of EFEM, `entityOfConcernChangeMode = preserve`)

*Context.* In MVPK you compute an engineering view `V` of a system description; you then normalise the view (sort, factor, put equations into normal form) without changing what it says.

Let `X = V_raw`, `Y = V_norm`, both `U.EpistemeView` instances with the same:

* `entityOfConcernRef(X) = entityOfConcernRef(Y)` (same system);
* the exact grounding relation and grounding holon used by the normalization remain unchanged, when grounding is current;
* any viewpoint selected by the named normalization use is the same exact P for X and Y; this selection is outside episteme identity;
* `representationSchemeRef(X) = representationSchemeRef(Y)` (same notation).

The EFEM `NormalizeView : X→Y`:

* has `entityOfConcernChangeMode(NormalizeView) = preserve`;
* changes only `content` and maybe `meta` (e.g. “normalised at edition E”);
* is idempotent and deterministic (P4);
* is conservative (P2): no new claims, only re‑expression.

MVPK can then **assume** functoriality of such normalisations without re‑stating the EFEM laws.

#### A.6.2:5.3 - Retargeting sketch (bridge‑backed, `entityOfConcernChangeMode = retarget`)

*Context.* E.18 structural reinterpretation maps a physical layout view into a functional behaviour view, changing the EntityOfConcern from “physical module assembly” to “functional graph” along a KindBridge.

Inside EFEM, this becomes a species with `entityOfConcernChangeMode = retarget`:
* input episteme describes `S₁` (e.g. a component hierarchy holon);
* output episteme describes `S₂` (e.g. a functional network holon);
* a declared `KindBridge(S₁,S₂)` and invariant (e.g. behavioural equivalence) provide the semantic glue;
* P2 conservativity is checked **w.r.t. that invariant**.

The details belong to A.6.4 and E.18; EFEM provides the generic discipline.

#### A.6.2:5.4 - Worked value-and-relation profile (engineering SystemDescription episteme kind)
*(informative)*

To make the C.2.1 value and EFEM law discipline concrete, consider an engineering episteme of a dependent system-description kind whose exact EntityOfConcern is one `U.System`:

| Value named by the EFEM species | Kind or reference form | Use |
| --- | --- | --- |
| exact EntityOfConcern | `U.Entity` constrained to `U.System`; designated by `U.EntityRef` | identifies the system that the claims concern |
| claim content | `U.ClaimGraph` | carries the description or specification claims |
| effective ReferenceScheme | `U.ReferenceScheme` | makes the claims and their designations interpretable |

This table names actual episteme values; it is not a `RelationSignature` or SlotSpec table. `EntityOfConcernSlot`, `ClaimGraphSlot`, and `ReferenceSchemeSlot` are declaration-local SlotKinds only when the reusable C.2.1 `EpistemeConstitutionRelationSignature` is being inspected. An EFEM species reads or changes the actual participants. It names any selected viewpoint, empirical-grounding relation, or representation relation separately.

Two typical EFEM species over this kind are:
* `Specify_DescEp_SpecDesc_Sys : SystemDescription → SystemSpec` — an `EntityOfConcernChangeMode = preserve` species that:
  * **reads** the exact EntityOfConcern and effective ReferenceScheme, separately uses an obtaining empirical-grounding relation or named describing-use viewpoint only when current, and **writes** refined claim content and possibly a strengthened effective ReferenceScheme;
  * satisfies P2 by only adding claims that are logical consequences of the original description plus the fixed `EntityOfConcern` (A.7 and E.10.D2);
  * satisfies C.2.1:7.1 by declaring its value-and-relation read/change profile and change mode.

* `Normalize_EngView : EpistemeView → EpistemeView` — a view‑normalisation EFEM (again with `EntityOfConcernChangeMode = preserve`) that:
  * **reads** the three C.2.1 identity values and every separately declared neighboring relation on which the operation depends, and **changes** only the output claim content and `meta`;
  * is idempotent and deterministic (P4) and pure (P1);
  * is conservative (P2) by construction: it never introduces new atoms about the selected system.

Concrete A.6.3/A.6.4/E.17.* patterns for engineering description and specification-use idioms state explicitly, under C.2.1:7.1 and CC-EFEM.*, which episteme values and separately obtaining relations their EFEM species read or change.

