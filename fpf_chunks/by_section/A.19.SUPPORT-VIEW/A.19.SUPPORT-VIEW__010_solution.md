---
chunk_kind: "child"
pattern_id: "A.19.SUPPORT-VIEW"
pattern_title: "Cross-Surface Support View"
section_id: "A.19.SUPPORT-VIEW:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SUPPORT-VIEW/A.19.SUPPORT-VIEW__010_solution.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.19.SUPPORT-VIEW — Cross-Surface Support View"
  - "A.19.SUPPORT-VIEW:4 — Solution"
line_start: 23585
line_end: 23822
dependencies:
  - "A.0"
  - "A.19"
  - "A.19.SURF-SPACE"
  - "A.6.3"
  - "A.6.P"
  - "C.19"
  - "C.24"
  - "E.17"
  - "E.17.0"
  - "G.10"
  - "G.2"
  - "G.5"
keywords:
  - "CrossSurfaceAtlasView"
  - "CrossSurfaceSupportView"
  - "TraditionAtlasView"
  - "TypedSetViews"
  - "atlas support"
  - "support qualifiers"
  - "support view"
  - "support-only reading"
  - "thin support"
---

### A.19.SUPPORT-VIEW:4 - Solution

Declare support views as support-only readings over one already-declared substrate-bearing basis, keep them explicitly under existing view law, and reserve atlas form for the cases that truly need it.

#### A.19.SUPPORT-VIEW:4.1 - Governed object and outside work

Use this pattern to declare:

- one `CrossSurfaceSupportView`, the ordinary/common head of this support-view family;
- one support-only reading over one already-declared substrate-bearing basis: either one explicit `A.19.SURF-SPACE` line or one already-declared source surface or declared set surface whose supporting spaces, mappings, and qualifiers remain recoverable through such a line;
- the support question that makes this view worth showing;
- the recoverable source surface or source surfaces that the support view is reading;
- any active set surface, derived view, or base palette that the current reading keeps in play;
- any cited spaces or mappings that the current reading depends on, provided those remain recoverable through declared refs or the cited substrate-bearing line;
- and any optional supporting qualifiers that the current view genuinely needs.

`CrossSurfaceAtlasView` is one fuller specialization inside that same family. It is not the common head.

Do not use this pattern to declare:

- `CharacteristicSpace` itself;
- the substrate role/relation stack from `A.19.SURF-SPACE`;
- selector outcomes, shortlist heads, or shipping outputs;
- live pool policy or enactment policy;
- or a new generic law for views, viewpoints, or publication surfaces.

#### A.19.SUPPORT-VIEW:4.2 - Minimal support view declaration

A conforming support view makes the following explicit:

- which support-family head is active: ordinary `CrossSurfaceSupportView` or fuller `CrossSurfaceAtlasView`;
- which already-declared substrate-bearing basis it is reading: either the explicit substrate line or the declared source-surface entry point or set-surface entry point that keeps that substrate recoverable;
- which support question the view is answering;
- which source surface or source surfaces must stay recoverable while the view is active;
- which active set surface, if any, the current reading is using over that source surface;
- which cited spaces and mappings, if any, the current reading depends on, and how they remain recoverable;
- which optional supporting qualifiers are genuinely doing work in the current case;
- and which neighboring publication, policy, naming, or support questions stay outside this view.

The minimum ordinary support view declaration is therefore:

1. one declared substrate-bearing basis from `A.19.SURF-SPACE`: either the explicit base substrate line or one declared source surface or declared set surface whose substrate remains recoverable with it;
2. one explicit support question;
3. one recoverable active source-surface basis, plus any active set surface drawn from it when the reading uses one;
4. any cited spaces, mappings, and qualifying uncertainty/distortion supports remain recoverable whenever the reading cites them;
5. one explicit statement that this is support-only and does not redefine substrate or publication semantics.

#### A.19.SUPPORT-VIEW:4.3 - Support view declaration laws (SV-0..SV-8)

**SV-0 - View-law docking is explicit.**
Every conforming support view is one domain-specific use-site under existing `A.6.3` / `E.17.0` law. It does not introduce one autonomous new theory of views.

**SV-1 - The described entity is preserved.**
The support view preserves the described entity already carried by the base line. If the current prose would change that described entity, the line is no longer one support view over the same substrate.

**SV-2 - The base substrate remains the semantic center.**
The support view may foreground aspects of the base line, but it does not replace or repair the base substrate declaration. Substrate repair belongs back in `A.19.SURF-SPACE`.

**SV-3 - Source, set-surface, and palette recoverability are mandatory.**
The current source surface, any active set surface drawn from it, and any active derived view or base palette must remain recoverable while the support view is active.

**SV-4 - Support qualifiers remain foregrounding devices only.**
`OutcomeMapRef`, `SpaceMetricRef`, `TransitionSupportRef`, and `BridgeDistortionNote` may be foregrounded, but they do not become the support view's ontology and they do not silently change the base relation or posture.

**SV-5 - Thin support and atlas support are different profiles.**
Ordinary `CrossSurfaceSupportView` is a complete admissible profile, not a placeholder. `CrossSurfaceAtlasView` is used only when the fuller composite support question is real.

**SV-6 - Atlas form requires a complete composite record.**
If atlas form is active, the view must keep the base substrate, the active source or set surface, the relevant `TypedSetViews`, any cited spaces, any cited mappings, and any qualifying support explicit enough that the reader can recover why thin support was not enough.

**SV-7 - Local specialization stays local.**
If `TraditionAtlasView` is used, it remains one `G.2` specialization of `CrossSurfaceAtlasView`; it does not become the common head of the family.

**SV-8 - Admission is fail-closed.**
If the current line would change the described entity, add new generic view law, repair the substrate, decide publication, or decide policy, it is not a conforming support view here. Apply the pattern that governs that question instead of stretching the family.

#### A.19.SUPPORT-VIEW:4.4 - Profiles

Use one of these profiles explicitly:

- **Thin-support profile.**
  Use ordinary `CrossSurfaceSupportView` when one source basis plus one support question is enough, and the current reading does not need several typed set views or several support qualifiers held together at once.
- **Atlas-support profile.**
  Use `CrossSurfaceAtlasView` when the reader must hold several declared views, spaces, mappings, or qualifiers together to understand the same base substrate-bearing line.

If neither profile can be chosen honestly, the line is not ready as support-view text.

#### A.19.SUPPORT-VIEW:4.5 - Operational declaration sequence (fail-closed)

When declaring one support view, proceed in this order:

0. **Entry test.** Confirm that one already-declared substrate exists and that the current support question can cite it either directly or through one declared source-surface entry point or set-surface entry point that keeps it recoverable, rather than drifting into substrate repair, publication, or policy.
1. **Name the active support head.** Use ordinary `CrossSurfaceSupportView` unless the current reading genuinely needs the fuller atlas form.
2. **Cite the base line.** Name the already-declared substrate the view is reading, or cite the source-surface entry point or set-surface entry point together with the recoverable substrate it depends on.
3. **State the support question directly.** Say what the view helps the reader see that the substrate alone leaves hard to inspect.
4. **Keep the base surfaces recoverable.** Name the active source surface, and if the view is over one declared front, archive, shortlist, palette, or other set surface drawn from that source, keep that active set surface recoverable too.
5. **Recover derived-view and palette structure when it matters.** If the view depends on one derived tradition or palette reading, state `DerivedViewKind` and `BasePaletteRef`.
6. **Add the actual supports.** Add `TypedSetViews`, cited spaces, mappings, metrics, transition supports, or distortion notes only when the current reading truly depends on them.
7. **Run the preservation check.** If the support prose would materially change the base source-to-outcome relation or the base distortion/uncertainty/error posture, stop and reopen the substrate declaration.
8. **Run the boundary check.** If the prose starts changing the described entity, minting new generic view law, publishing selected sets, shipping outputs, or deciding policy, apply the pattern that governs that question.

**Fail-closed rule.** Do not treat the line as a support view if steps 2-7 cannot be completed honestly. Missing base-line recovery or hidden posture change is a real defect here.

#### A.19.SUPPORT-VIEW:4.6 - Thin support remains a complete admissible form

Many cases need one support view but not one atlas-form support package.

Stay with one thinner support view when:

- the current reading needs only one declared source surface or one derived view over it;
- the current question does not need several typed set views assembled at once;
- one explicit support sentence is enough to keep the current line readable;
- or the case does not genuinely depend on metrics, transitions, or bridge-loss notes.

This matters because the support layer should stay proportionate to the support question. If a thin interpretive view already solves the reader's problem, forcing atlas form would over-type the line and create fake necessity.

#### A.19.SUPPORT-VIEW:4.7 - Atlas form is fuller support and needs a complete record

Use `CrossSurfaceAtlasView` for the fuller support cases:

- when several typed set views over one declared source surface or one active derived set surface must be read together;
- when one atlas-form reading helps the reader inspect cross-scale structure, cross-space structure, support plurality, or mapping plurality;
- when the current interpretation genuinely depends on one declared map, metric, transition support, or distortion note and those supports must stay visible together with the active source surfaces or active set surfaces they qualify.

The minimal admissible atlas-support declaration therefore contains:

- the cited base substrate or source-surface entry point or set-surface entry point;
- the active source surface and any active set surface drawn from it;
- `TypedSetViews` when several declared set views are being held together;
- any cited `SearchSpaceRef`, `OutcomeSpaceRef`, or other declared space refs that the atlas reading depends on;
- any cited `OutcomeMapRef`, `SpaceMetricRef`, `TransitionSupportRef`, or `BridgeDistortionNote` that materially disciplines the reading;
- `DerivedViewKind` and `BasePaletteRef` whenever the atlas reading is over one derived palette or tradition view;
- one explicit reason thin support is insufficient.

If atlas form cannot state that composite support view without invention, stay with thin support or apply the pattern that governs the missing question.

#### A.19.SUPPORT-VIEW:4.8 - No autonomous local view law is introduced here

Read the docking to `A.6.3` / `E.17.0` strictly:

- the support view preserves the described entity already carried by the base line;
- it does not silently mint new intensional commitments about that same described entity;
- it does not replace one viewpoint bundle or one publication-view family with one new local invention;
- and it does not collapse viewpoint, view, and surface into one word.

If a case would need a different described entity, a different generic view law, or one new viewpoint family, this pattern is no longer the governing pattern.

#### A.19.SUPPORT-VIEW:4.9 - Support qualifiers stay support-only

`OutcomeMapRef`, `SpaceMetricRef`, `TransitionSupportRef`, and `BridgeDistortionNote` are admitted here only as support qualifiers.

They are declared first on the substrate side. This pattern may foreground or organize them for the reader, but it may not silently widen, narrow, or otherwise change the base substrate posture.

Use them when the current support view genuinely needs them:

- `OutcomeMapRef` when the current reading must show how one declared source or set surface bears on one outcome surface;
- `SpaceMetricRef` when neighborhood, spread, reachability, or crowding claims are load-bearing in the current reading;
- `TransitionSupportRef` when the current reading depends on explicit transition or cross-scale state-change support;
- `BridgeDistortionNote` when the reader must keep one declared loss or distortion visible near the current reading.

If the support view would newly introduce `lossy-bridge`, `uncertainty-bearing`, `transition-dependent`, `learned/adaptive`, or another materially different posture that the substrate did not already declare, reopen the substrate declaration instead of treating that posture change as view-only convenience.

#### A.19.SUPPORT-VIEW:4.10 - Publication, set-surface, and pool-policy boundaries

This pattern does not publish selected sets, declare shortlist heads, or decide which candidate lines stay live.

Keep the split explicit:

- `A.19.SUPPORT-VIEW` helps the reader inspect one already-declared substrate;
- `G.5` publishes selector outcomes and their source/publication metadata;
- `G.10` ships publication surfaces and pins;
- `C.19` governs live candidate-pool and frontier policy;
- `C.24` governs enactment/planning posture.

If the prose starts deciding who survives, what is published, or what is shipped, it has already left this pattern.

#### A.19.SUPPORT-VIEW:4.11 - `G.2` keeps the tradition-facing atlas specialization

When the current support view is tradition-facing and palette-first recoverability matters, use the local specialization governed by `G.2`.

Read the relation this way:

- `A.19.SUPPORT-VIEW` states the generic support-view family and the generic fuller atlas form `CrossSurfaceAtlasView`;
- `G.2` keeps the palette-first, tradition-facing specialization `TraditionAtlasView`;
- `TraditionAtlasView` is therefore one local specialization of the fuller atlas form, not the common head of the whole support family.

This keeps the family honest in both directions:

- the common support-view family does not force `Tradition` or `Atlas` into every case;
- and the `G.2` specialization does not lose its palette-first recoverability.

#### A.19.SUPPORT-VIEW:4.12 - Operator kit: choose, record, preserve, apply governing neighbor

Use this compact kit whenever you need one support view that can actually be used, checked, and bounded against neighboring patterns in practice.

| Decision point | What to do now | Admissible result | Stop or apply another pattern when... |
| --- | --- | --- | --- |
| `1. Which base line am I reading?` | Cite the base substrate or recoverable source-surface entry point or set-surface entry point. | The support view is anchored on one visible base line. | The view still floats free of the line it is supposed to help read. |
| `2. What support question is this view answering?` | State the question directly in one sentence. | The reader can tell what this view helps inspect. | The view mostly repeats theory without naming the practical inspection load. |
| `3. Do I need thin support or atlas support?` | Choose ordinary `CrossSurfaceSupportView` unless several views, spaces, mappings, or qualifiers must be held together at once. | The support head is chosen honestly. | Atlas language appears by reflex, or thin support would already solve the reading problem. |
| `4. Which surfaces and qualifiers must stay recoverable?` | Keep the active source surface, active set surface, derived view, base palette, and cited qualifiers visible only when they truly do work. | Recoverability stays proportional to the support question. | The base palette or base surface disappears behind the fullest visible overlay. |
| `5. Is the line still support-only?` | Check whether the prose preserves the base substrate and its described entity. | The view remains one reading, not one rewrite of the underlying line. | The prose is really changing the substrate, publishing outputs, or deciding policy. |

Use this compact support view declaration when drafting or repairing the line:

```text
SupportHead               = CrossSurfaceSupportView | CrossSurfaceAtlasView
BaseSubstrateRef          = ...
SupportQuestion           = ...
ActiveSourceSurface       = ...
ActiveSetSurface?         = ...
DerivedViewKind?          = ...
BasePaletteRef?           = ...
TypedSetViews?            = ...
CitedSpaceRefs?           = ...
SupportQualifiers?        = ...
WhyThinIsEnough? /
WhyAtlasIsNeeded?         = ...
```

Run this self-check before you leave the passage:

- if the support view would change the base relation or posture, reopen `A.19.SURF-SPACE`;
- if the atlas-necessity line is empty, stay with thin support;
- if the next live question is naming repair, terminology precision, publication, or policy, apply `F.18`, `A.6.P`, `G.5`, `G.10`, `C.19`, or `C.24` instead of stretching support-view prose across those boundaries.

#### A.19.SUPPORT-VIEW:4.13 - Using the support view with neighboring patterns

Read neighboring patterns in this order once the support view declaration is in place:

- Use `G.2` when the support view becomes palette-first, tradition-facing atlas work. That is one local specialization of atlas support, not the common family head.
- Use `F.18` when the live question is label choice around support-view, atlas, palette, or map language. Naming notes may explain the labels, but they do not change the base substrate or the support question.
- Use `A.6.P` when one passage collapses view, surface, space, map, or palette into one umbrella word. Repair the layer split first, then continue.
- Use `A.0` when cold-reader glossing is what the current line lacks. Glosses help recognition; they do not replace the base support view declaration.
- Use `G.5`, `G.10`, `C.19`, or `C.24` when the passage starts deciding outputs, survivor sets, or planning posture.

If a neighboring passage would change the described entity or the base substrate posture, this pattern is no longer the governing pattern for that sentence. Reopen the base line or apply the pattern that governs the new question.

