---
chunk_kind: "child"
pattern_id: "A.6.3"
pattern_title: "U.EpistemicViewing - EntityOfConcern-preserving episteme construction"
section_id: "A.6.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3/A.6.3__005_solution.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "A.6.3 — U.EpistemicViewing - EntityOfConcern-preserving episteme construction"
  - "A.6.3:4 — Solution"
line_start: 13408
line_end: 13513
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.6.0"
  - "A.6.2"
  - "A.6.3.CR"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.5"
  - "A.7"
  - "B.5.3"
  - "C.2"
  - "C.2.1"
  - "C.29"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
keywords:
---

### A.6.3:4 - Solution

**Local mantra.** Identify X and Y. Hold their EntityOfConcern fixed. State the conservative construction and admitted loss. Add exact correspondence dependencies when used. Test `U.View` membership separately under E.17.0.

#### A.6.3:4.1 - Identify both epistemes independently

Before declaring a viewing, recover for each of X and Y under C.2.1:

- exact claim content;
- exact EntityOfConcern;
- effective `U.ReferenceScheme`.

X and Y are separate epistemes whenever one of those identity discriminators differs. A filename, table, diagram, query result, `viewpointRef`, or publication form is not a substitute for either identity.

If the supposed receiving item has no recoverable claim content or EntityOfConcern, stop: there is no receiving episteme yet. If the exact EntityOfConcern differs, use A.6.4 retargeting rather than A.6.3.

#### A.6.3:4.2 - Declare the viewing construction

`U.EpistemicViewing` is the EntityOfConcern-preserving species of A.6.2 `U.EffectFreeEpistemicMorphing`. In the mathematical lens, one concrete viewing is written `v : X -> Y`.

The reusable A.6.0 declaration keeps these direct components:

```text
SubjectKind     = U.EpistemicViewing
RangedValueKind = ordered pair of exact U.Episteme values <X,Y>
ResultKind      = EpMorphism
SliceSet        = the declared ContextSlice set when applicability varies by slice
ExtentRule      = the admissible viewing morphisms in each selected slice
```

`EpMorphism` is the local mathematical-lens arrow value. It represents the governed construction; it is not the system that acts, the work occurrence, the receiving episteme, or a world-side transformation by spelling.

A concrete viewing declaration states:

1. exact X and exact Y;
2. that `EntityOfConcern(X)=EntityOfConcern(Y)`;
3. the claim-content construction from X and any additional exact sources to Y;
4. how the source and receiving reference schemes are related;
5. preserved claim components, admitted omissions or losses, and prohibited strengthening;
6. applicability conditions and any fixed configuration needed for replay.

#### A.6.3:4.3 - Apply the same-EntityOfConcern and conservativity laws

For every admitted `v : X -> Y`:

1. **Same EntityOfConcern.** X and Y designate the same exact EntityOfConcern. Similar labels, bridge claims, or one shared project do not establish this equality.
2. **No unsupported strengthening.** Every claim in Y about that entity is recoverable as a consequence, conservative re-expression, or explicitly admitted aggregation of claims in the identified sources under the declared reference and representation semantics.
3. **Declared loss.** Every omitted concern or claim family that affects receiving use is named, together with the condition under which the loss is admitted.
4. **Reference discipline.** A changed effective reference scheme is explicit. If the change alters available operations or representation semantics, use A.6.3.RT and C.29; do not call it formatting.
5. **No hidden retargeting.** Subsystem-to-system, method-to-work, model-to-modeled-system, or episteme-to-publication changes are not same-EntityOfConcern viewing.

For a lightweight check, take each claim in Y—or each group covered by one rule—and point to the source claims and the selection, rewriting, or aggregation rule that licenses it. Mark omitted claim groups. If a result claim cannot be traced this way, treat it as a new claim rather than a viewing result. If support cannot be decided exactly, state the structural or domain check used as an approximation and what it cannot establish. Add a proof only when disagreement, risk, or the receiving use makes it necessary.

Truth of source claims is a separate evaluation. Conservativity says what Y is licensed to claim from the sources; it does not establish that those claims are true in the world or adequate for a decision.

#### A.6.3:4.4 - Keep optional viewpoint selection and view membership separate

For the current use of receiving episteme Y, name the describing use and exact viewpoint P only when that selection changes what the receiver reads or checks. Keep Y, its EntityOfConcern, the use, and P distinct. Selecting P is outside C.2.1 identity and does not make E.17.0 conformance obtain.

After Y is identified, apply E.17.0 only when the current use needs `U.View` membership:

```text
EpistemeViewpointConformanceRelation(Y,P) obtains
  -> the same episteme Y is a U.View
```

Directly authored Y can be a view without any A.6.3 source relation. Conversely, a valid A.6.3 construction can yield Y that fails P's concern-coverage or semantic-form rules and therefore is not a view under P.

#### A.6.3:4.5 - Distinguish direct and correspondence-mediated construction

**Direct viewing.** Y is constructed from X and fixed configuration only. The declaration names the exact claim selection or rewriting rule and any loss. No generic correspondence object is required.

**Correspondence-mediated viewing.** Y depends on several exact source epistemes or on exact relations between their claim-bearing contents. Recover each direct correspondence, realization, trace, equivalence, or consistency relation under its governing pattern before using it. Then identify the C.2.1 episteme that states or describes those relations if the construction must cite it.

Plain `correspondence model` may name that exact claim-bearing episteme for convenience. It is not a public `U.CorrespondenceModel` kind, and its graph edges or table cells do not establish the direct relations. If a needed relation lacks a governor, return the exact missing-relation blocker or use A.6.RCD.

The viewing declaration cites the exact source epistemes and exact correspondence claims on which Y depends. It does not insert the correspondence episteme, evidence, or evaluation result into Y's C.2.1 identity unless Y's own claim content actually changes.

#### A.6.3:4.6 - Keep mathematical construction, work, production, and publication distinct

The viewing morphism performs no work. When a tool or person executes a query, rewrites text, runs a model, or renders a face, a system performs dated `U.Work` under A.15.1 by an exact method. The source epistemes, parameters, tools, and receiving entities participate only through their direct relations or A.6.1 operation bindings.

If that work first constitutes exact episteme Y and the identity-inception claim matters, A.15.PROD governs the local work/change/identity claim. Neither work nor inception establishes conservativity or E.17.0 conformance.

If Y is made available, E.24.PUB separately identifies the publication occurrence, publication form, and `U.PresentationCarrier`. Publication neither creates the A.6.3 construction nor grants `U.View` membership.

#### A.6.3:4.7 - Preserve composition and replay

For fixed source epistemes, rules, reference semantics, correspondence dependencies, and configuration:

- identity viewing preserves the same C.2.1 episteme;
- composing `f : X -> Y` with `g : Y -> Z` gives the same licensed receiving claims as the declared composite, up to the stated equivalence;
- deterministic viewings yield the same Y identity discriminators on replay;
- random seeds, model editions, external service state, or timing that can change Y are explicit inputs to the work or declaration, not hidden meta;
- applying an idempotent normalization twice yields the same receiving episteme up to the declared representation equivalence.

If two paths differ in claims, EntityOfConcern, or effective reference scheme beyond the declared equivalence, they do not identify the same receiving episteme and the composition claim fails.

#### A.6.3:4.8 - Stop at the lightest sufficient statement

For ordinary use, this can be enough:

> `Safety summary Y is conservatively constructed from plant description X; both concern Plant-7; Y omits maintenance-cost claims and introduces no safety claim not recoverable from X.`

Add a reusable declaration, explicit mathematical arrow, correspondence episteme, evaluation result, work occurrence, production claim, or publication objects only when a named receiving work or decision depends on that object.

