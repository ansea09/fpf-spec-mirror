---
chunk_kind: "child"
pattern_id: "A.19.SURF-SPACE"
pattern_title: "Cross-Surface and Cross-Space Substrate"
section_id: "A.19.SURF-SPACE:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SURF-SPACE/A.19.SURF-SPACE__010_solution.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.19.SURF-SPACE — Cross-Surface and Cross-Space Substrate"
  - "A.19.SURF-SPACE:4 — Solution"
line_start: 23036
line_end: 23293
dependencies:
  - "A.0"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.SUPPORT-VIEW"
  - "A.6.P"
  - "C.18"
  - "C.19"
  - "G.10"
  - "G.5"
keywords:
  - "DistortionPosture"
  - "SourceSurfaceId"
  - "SourceToOutcomeRelation"
  - "SpaceRefRelationKind"
  - "cross-surface substrate"
  - "distinctDeclaredSpaceFrom"
  - "outcome-side space ref"
  - "sameDeclaredSpaceAs"
  - "search-side space ref"
  - "source surface"
---

### A.19.SURF-SPACE:4 - Solution

Declare the cross-surface or cross-space line through one explicit substrate stack, keep only the load-bearing core mandatory, and place every heavier requirement in conditional fields, support qualifiers, or companion declarations.

#### A.19.SURF-SPACE:4.1 - Governed object and outside work

Use this pattern to declare only the substrate stack below:

- the declared source surface that the line is acting on;
- the recoverable concrete source-surface identity when the family name alone would be ambiguous;
- the search-side reference to one declared `A.19` `CharacteristicSpace`;
- the outcome-side reference to one declared `A.19` `CharacteristicSpace`;
- the explicit `SpaceRefRelationKind` over those two ref positions;
- the explicit source-to-outcome relation;
- and the explicit distortion, uncertainty, or error posture for that relation.

Do not use this pattern to declare:

- `A.19` space typing itself;
- selector outcome publication, shortlist identity, or shipping closure;
- live pool policy or enactment planning;
- or optional support-view families that interpret or reorganize an already-declared substrate.

#### A.19.SURF-SPACE:4.2 - Minimal declaration stack

Use the following notation-independent stack:

```text
CrossSurfaceCrossSpaceSubstrate := <
  SourceSurfaceKind,
  SourceSurfaceId?,
  SearchSpaceRef,
  OutcomeSpaceRef,
  SpaceRefRelationKind,
  SourceToOutcomeRelation,
  DistortionPosture,
  SourceSurfaceComposition?,
  DerivedViewKind?,
  BasePaletteRef?,
  OutcomeMapRef?,
  SpaceMetricRef?,
  TransitionSupportRef?,
  BridgeDistortionNote?
>
```

Interpret the fields as follows:

- `SourceSurfaceKind` names the primary declared source-surface family that the line is anchored on.
- `SourceSurfaceId?` names the concrete declared source surface or declared set surface when several same-family surfaces are live or when one neighboring governing pattern must be cited to keep that identity unique. It may be omitted only when the concrete source surface is unambiguous from the declared line.
- `SearchSpaceRef` points to one declared `A.19` `CharacteristicSpace` in the search-side position.
- `OutcomeSpaceRef` points to one declared `A.19` `CharacteristicSpace` in the outcome-side position.
- `SpaceRefRelationKind` states how those two refs relate. In ordinary use, the token is either `sameDeclaredSpaceAs` or `distinctDeclaredSpaceFrom`.
- `SourceToOutcomeRelation` is one controlled declaration slot. State at least direction, mode, and carrier.
- `DistortionPosture` is one controlled declaration slot with one primary posture token plus optional clarifying note. In this slice, lawful posture tokens include `transparent-for-current-use`, `lossy-bridge`, `metric/model-dependent`, `transition-dependent`, `uncertainty-bearing`, `learned/adaptive`, and `unstable-under-refresh`.
- `SourceSurfaceComposition`, `DerivedViewKind`, and related `...Kind` values remain declaration fields or controlled field values unless some receiving governing pattern explicitly promotes them; they are not automatically independent heads merely because their names end with `Kind`.

This is an `A.6.5` / `A.6.P` move: `SearchSpaceRef` and `OutcomeSpaceRef` are ref-typed slot contents, while `SpaceRefRelationKind` is the explicit `RelationKind` token that governs how those two ref positions are read together.

#### A.19.SURF-SPACE:4.3 - Substrate declaration laws (SS-0..SS-7)

**SS-0 - One substrate line, one explicit stack.**
Treat a line as declared substrate only if one recoverable source-surface basis, two recoverable space refs, one explicit ref-to-ref relation kind, one explicit source-to-outcome relation, and one explicit posture are present together.

**SS-1 - Ref typing is preserved.**
`SearchSpaceRef` and `OutcomeSpaceRef` must resolve to declared `A.19` `CharacteristicSpace`. They do not become parallel space kinds, slot aliases, or role claims.

**SS-2 - Source-surface recoverability is mandatory.**
The reader must be able to recover not only the source-surface family but, when several same-family surfaces are simultaneously live, the concrete declared surface through `SourceSurfaceId?` or one cited neighboring governing pattern that uniquely identifies it.

**SS-3 - Relation requirement must be explicit.**
`SourceToOutcomeRelation` is conforming only when direction, mode, and carrier are explicit enough to tell what is related to what, through which carrier/relation mode, and through which declared support qualifier.

**SS-4 - Posture honesty is mandatory.**
`DistortionPosture` must say whether the line is transparent for current use or qualified by loss, metric/model dependence, transition dependence, uncertainty, learning/adaptation, or instability under refresh. The line may not hide qualification in atmospheric prose.

**SS-5 - Conditional and support fields stay subordinate.**
`SourceSurfaceComposition`, `DerivedViewKind`, `BasePaletteRef`, `OutcomeMapRef`, `SpaceMetricRef`, `TransitionSupportRef`, and `BridgeDistortionNote` may clarify the substrate, but they do not replace the core stack and do not become mandatory everywhere.

**SS-6 - Publication and policy stay outside.**
Publication metadata, shortlist identity, live-pool policy, and enactment policy remain neighboring decisions. A substrate line may feed them, but it does not decide them.

**SS-7 - Admission is fail-closed.**
If the source surface cannot be recovered, either space ref is unresolved, `SpaceRefRelationKind` cannot be chosen honestly, relation direction, mode, or carrier remains vague, or posture remains unclassified, then the line is not yet a declared substrate. Keep it as a working gloss or move it to the governing pattern that can close the missing requirement.

#### A.19.SURF-SPACE:4.4 - Profiles

Use one of these ordinary profiles:

- **Shared-space profile.**
  `SearchSpaceRef` and `OutcomeSpaceRef` both resolve to the same declared `CharacteristicSpace`, and `SpaceRefRelationKind = sameDeclaredSpaceAs`.
- **Cross-space profile.**
  `SearchSpaceRef` and `OutcomeSpaceRef` resolve to two distinct declared `CharacteristicSpace` declarations, and `SpaceRefRelationKind = distinctDeclaredSpaceFrom`.
- **Derived-source supplement.**
  If the visible source surface is one derived tradition, front, or palette view, keep `DerivedViewKind` and `BasePaletteRef` explicit so the derived surface does not silently become the default meaning of the base palette or source surface.

#### A.19.SURF-SPACE:4.5 - Operational declaration sequence (fail-closed)

When declaring one substrate-bearing line, proceed in this order:

0. **Entry test.** Confirm that the line really needs source-surface plus search/outcome-space plus relation/posture discipline. If it only needs `CharacteristicSpace` typing, use `A.19`. If it only needs publication or policy, apply the governing pattern that carries that publication or policy question.
1. **Recover the active source surface.** State `SourceSurfaceKind`. If several same-family surfaces are simultaneously live, fill `SourceSurfaceId?` or cite the neighboring governing pattern that makes that identity unique.
2. **Recover the space refs.** Point `SearchSpaceRef` and `OutcomeSpaceRef` to already-declared `CharacteristicSpace`.
3. **Choose the ref-to-ref relation kind.** Declare `sameDeclaredSpaceAs` only when both refs truly resolve to one declared space. Declare `distinctDeclaredSpaceFrom` only when they truly resolve to two distinct declared spaces. Do not leave this to reader inference.
4. **State the source-to-outcome relation.** Give direction, mode, and carrier explicitly. If one named `OutcomeMapRef` or another declared support qualifier carries the relation, cite that qualifier explicitly. If not, state the carrier directly in prose.
5. **State the posture.** Declare whether the line is transparent for current use or qualified by loss, metric/model dependence, transition dependence, uncertainty, learning/adaptation, or instability under refresh.
6. **Add only the fields that are really doing work.** Add composition, derived-view, base-palette, metric, transition, or bridge qualifiers only when the current case actually depends on them.
7. **Run the boundary check.** If the line starts deciding publication metadata, shortlist identity, live candidate policy, enactment policy, or support-view organization, stop and apply the pattern that governs that question.

**Fail-closed rule.** Do not treat the line as declared substrate if any of steps 1-5 remains unresolved. Incomplete recovery is a real defect here, not one stylistic omission.

#### A.19.SURF-SPACE:4.6 - Canonical rewrite forms

When the line is ready, it should be possible to rewrite it into one of these minimal forms.

**Shared-space form**

```text
SourceSurfaceKind      = ...
SourceSurfaceId?       = ...
SearchSpaceRef         = DeclaredCharacteristicSpace@...
OutcomeSpaceRef        = DeclaredCharacteristicSpace@...
SpaceRefRelationKind   = sameDeclaredSpaceAs
SourceToOutcomeRelation= <direction, mode, carrier>
DistortionPosture      = <posture token; optional note>
```

**Cross-space form**

```text
SourceSurfaceKind      = ...
SourceSurfaceId?       = ...
SearchSpaceRef         = SearchCharacteristicSpace@...
OutcomeSpaceRef        = OutcomeCharacteristicSpace@...
SpaceRefRelationKind   = distinctDeclaredSpaceFrom
SourceToOutcomeRelation= <direction, mode, carrier>
DistortionPosture      = <posture token; optional note>
```

If neither rewrite form can be completed honestly, the line is not yet publishable as substrate-bearing text.

#### A.19.SURF-SPACE:4.7 - Conditional fields stay conditional

Use `SourceSurfaceComposition` only when the line genuinely consumes several declared source surfaces.

When composition is active:

- `SourceSurfaceKind` still names the primary family the line is anchored on;
- `SourceSurfaceComposition` names the additional declared source-surface families or the explicit composed-source posture that widens that primary family;
- the composition field does not replace the primary family, and it does not silently retitle the whole line as one different source kind.

Use `DerivedViewKind` only when one derived view is materially active and the reader must be able to recover that derivation.

Use `BasePaletteRef` only when a derived tradition or palette view would otherwise hide the recoverable base palette.

#### A.19.SURF-SPACE:4.8 - Support qualifiers stay support-only

`OutcomeMapRef`, `SpaceMetricRef`, `TransitionSupportRef`, and `BridgeDistortionNote` are admitted as support-only qualifiers.

Use them when:

- one declared mapping really disciplines the source-to-outcome relation;
- one metric really disciplines spread, neighborhood, or comparison claims;
- one `TransitionSupportRef` really disciplines dynamic coupling or transfer;
- or one bridge-loss note is the relevant reason the relation is qualified.

Do not make those support qualifiers the semantic center of the substrate. They help explain the relation; they do not replace the line made explicit by `SourceSurfaceKind`, `SourceSurfaceId?`, `SearchSpaceRef`, `OutcomeSpaceRef`, and the declared relation/posture pair.

Qualifier semantics are first declared on the substrate side. Later support views may reuse those qualifiers, but they do not become the place where the qualifier is first invented or materially changed.

#### A.19.SURF-SPACE:4.9 - Descriptor maps and distance definitions dock here, but do not replace the space refs

When a neighboring line already uses `DescriptorMapRef` or `DistanceDefRef`, dock it explicitly:

- `DescriptorMapRef` may realize or support the search-side or outcome-side representation requirement, as the current line requires;
- `DistanceDefRef` may realize or support the metric requirement over that representation on either side, as the current line requires;
- but neither one replaces `SearchSpaceRef` or `OutcomeSpaceRef`;
- and `CharacteristicSpace` remains a different kind from `DescriptorMap`.

Use this docking rule whenever a reader could otherwise mistake one local representation layer for the whole search-side or outcome-side space reference.

#### A.19.SURF-SPACE:4.10 - Publication and shipping remain downstream consumers

`G.5` and `G.10` may carry metadata such as `SelectorOutcomeKind`, `SetSurfaceKind`, `SourceSurfaceKind`, `SourceSurfaceComposition`, `DerivedViewKind`, and `BasePaletteRef` when one selected or shipped surface is being published.

That does not mean `G.5` or `G.10` defines the substrate.

Read the boundary this way:

- this pattern defines the substrate that later publication must preserve;
- `G.5` publishes selector-facing outcome metadata;
- `G.10` ships publication metadata and pins;
- neither one redefines the search-side reference, the outcome-side reference, or the source-to-outcome relation.

#### A.19.SURF-SPACE:4.11 - Ordinary and heavier use

For ordinary use, one short declaration block is enough:

- one `SourceSurfaceKind`;
- `SourceSurfaceId?` when family-level naming alone would be ambiguous;
- one `SearchSpaceRef`;
- one `OutcomeSpaceRef`;
- one explicit `SpaceRefRelationKind`;
- one explicit relation line;
- one explicit posture line.

Use the heavier stack only when one of these is true:

- several declared source surfaces are genuinely composed;
- one derived view must stay recoverable;
- one support qualifier is materially active;
- one descriptor-map or distance-definition docking clause is needed to prevent collapse;
- or the reader would otherwise mistake publication metadata for substrate semantics.

#### A.19.SURF-SPACE:4.12 - Operator kit: choose, declare, self-check, apply governing neighbor

Use this compact kit whenever the task is practical declaration rather than one more explanatory paragraph.

| Decision point | What to do now | Admissible result | Stop or apply another pattern when... |
| --- | --- | --- | --- |
| `1. What is the line acting on?` | Name `SourceSurfaceKind`, and when several same-family surfaces are live also make the concrete source surface recoverable. | The reader can tell which surface the line is about. | The source surface still floats behind one vague family word. |
| `2. Are search and outcome in one declared space or in two?` | Point `SearchSpaceRef` and `OutcomeSpaceRef` to declared `CharacteristicSpace`, then choose `sameDeclaredSpaceAs` or `distinctDeclaredSpaceFrom`. | The space-role split is explicit. | The same-space versus cross-space question is still being guessed from context. |
| `3. What relation is actually being claimed?` | Write one explicit `SourceToOutcomeRelation` with direction, mode, and carrier. | The reader can inspect what is related to what, through which carrier and relation mode. | You are still leaning on one umbrella word such as `projection`, `portfolio`, or `maps into`. |
| `4. What qualification is honest?` | Choose the governing `DistortionPosture` token and add one note only when it really sharpens the case. | The line is honest about loss, uncertainty, learning/adaptation, or other qualification. | Qualification remains atmospheric prose or one fake default of transparency. |
| `5. Which heavier supports are truly active?` | Add only the qualifier fields that the current case actually uses. | Supports stay subordinate to the substrate. | The next question is really support-view work, publication, or policy. |

Use this minimal worksheet when drafting or repairing one substrate line:

```text
SourceSurfaceKind       = ...
SourceSurfaceId?        = ...
SearchSpaceRef          = ...
OutcomeSpaceRef         = ...
SpaceRefRelationKind    = sameDeclaredSpaceAs | distinctDeclaredSpaceFrom
SourceToOutcomeRelation = <direction, mode, carrier>
DistortionPosture       = <token; optional note>
Optional supports       = <only those actually active>
```

Run this self-check before you leave the line:

- if the worksheet cannot be filled without one hidden assumption, the declaration is not ready yet;
- if the next needed prose is mainly "how should the reader inspect this substrate?", continue in `A.19.SUPPORT-VIEW`;
- if the next needed prose is "what gets published, shipped, retained, or enacted?", apply `G.5`, `G.10`, `C.19`, or `C.24`;
- if the current line changes because one neighbor wants different naming, glossing, or repair vocabulary, keep the substrate declaration here and let `F.18`, `A.0`, or `A.6.P` handle that neighboring requirement explicitly.

#### A.19.SURF-SPACE:4.13 - Using the substrate with neighboring patterns

Once one substrate line is declared, use neighboring patterns in this order:

- Use `A.19.SUPPORT-VIEW` when the next requirement is interpretive help over the same substrate. The support view may foreground the line, but it does not become the ontology.
- Use `G.2` when that support becomes palette-first, tradition-facing atlas work. Keep the base palette and the cited substrate recoverable while doing it.
- Use `A.6.P` when one passage collapses source surface, space ref, support view, atlas view, or mapping into one umbrella word. Repair the wording back to the substrate declaration before adding more theory.
- Use `F.18` when the problem is label choice or naming-side comparison around this stack. Naming notes may explain why one head is better named; they do not settle the substrate relation.
- Use `A.0` when the task is cold-reader glossing of these tokens. Glosses help recognition; they do not replace the declaration block.

If a neighboring passage would change the source-to-outcome relation or the distortion posture, reopen this pattern first. Neighboring text may reuse the substrate, but it may not silently rewrite it.

