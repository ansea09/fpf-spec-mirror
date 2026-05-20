   * preserve `DescribedEntityRef` of `DescriptionContext`,
   * either preserve `ViewpointRef` or change it within the declared viewpoint bundle, with any additional constraints recorded in the family’s `CorrespondenceModel`,
   * never widen `ClaimScope` beyond what EV‑3 permits.
3. Treat **any change of DescribedEntity** (even if “intuitively minor”, such as moving from subsystem to system) as **out of scope** for A.6.3; such moves belong to A.6.4 `U.EpistemicRetargeting`.

#### A.6.3:4.4 - Profiles: `U.DirectEpistemicViewing` and `U.CorrespondenceEpistemicViewing`

`U.EpistemicViewing` is further structured into two important species; both inherit EV‑0…EV‑6.

1. **`U.DirectEpistemicViewing` — self‑contained views.**
   * Domain and codomain epistemes share:
     * the same `representationSchemeRef` (up to declared normalisation),
     * the same `ReferenceScheme` (or a refinement which is conservative and structurally documented).
   * No external `CorrespondenceModel` is needed: the view is computed **solely from the input episteme** and, optionally, fixed configuration.
   * Typical cases:
     * internal normalisation (sorting, rewriting) of an engineering view;
     * filtering `U.ClaimGraph` to keep only safety‑relevant claims;
     * simplifying a proof‑oriented specification to a more operational form under the same semantics.

1. **`U.CorrespondenceEpistemicViewing` — views relying on correspondence models.**
   * Viewing depends on:
     * one or more subject epistemes (e.g. requirements and design),
     * an explicit `CorrespondenceModel` that relates their ClaimGraphs and representation schemes.
   * The result is an episteme (often an `U.EpistemeView`) whose `describedEntityRef` matches that of the primary episteme, but whose content is computed **through** the correspondence links.
   * Typical cases:
     * ISO 42010‑style correspondences between architectural descriptions;
     * cross‑model views in model‑based systems engineering (MBSE), where view content is computed from multiple model fragments;
     * traceability‑based views aggregating requirements, design elements, and tests.

In both profiles:
* `CorrespondenceModel` remains an **episteme-lane publication**, not a new kernel‑type hidden inside A.6.3.
* `U.EpistemicViewing` stays **view‑like**: it reveals what is already there under the correspondence; it does not perform Γ‑style constructions of new Intensions.

#### A.6.3:4.4.a - Common same-entity specialization notes

Two recurring same-described-entity families can be read as specializations governed by `A.6.3`, provided that EV‑0…EV‑6 remain explicit.

1. **`ConservativeRetextualization`.**
   Use this when the target remains textual and the main change is wording, density, ordering, language, or bounded filtering of already available content. It stays in `A.6.3` only if `describedEntityRef` is preserved, no new claims about that entity are minted, and correspondence use does not collapse into bridge or substitution licence.

2. **`RepresentationTransduction`.**
   Use this when the target changes representation scheme or reasoning medium while still preserving the same described entity. It stays in `A.6.3` only if representation-factor delta, recoverability, loss, and preserve-vs-retarget boundaries remain explicit. Purely textual rewrites belong with `ConservativeRetextualization`; any change of `DescribedEntityRef` belongs with `A.6.4`.

These notes do not create new governing patterns. They mark recurring same-entity specialization boundaries that remain subordinate to `U.DirectEpistemicViewing` / `U.CorrespondenceEpistemicViewing` and to the general `A.6.3` invariants.


### A.6.3:5 - Archetypal grounding (Tell–Show–Show)

#### A.6.3:5.1 - Engineering system description → safety officer view (DirectEpistemicViewing)

*Context.*
A system team maintains a rich `SystemDescription` episteme for a plant holon `S` under an engineering viewpoint from TEVB. A safety officer needs a concise view showing only safety‑critical components, hazards, and mitigations.

*Shape.*

* **Domain `X`.**
  `X : U.SystemDescription` with:
  * `describedEntityRef(X) : U.SystemRef` (the plant `S`),
  * `groundingHolonRef(X) : U.HolonRef` (runtime environment),
  * `viewpointRef(X) : U.ViewpointRef` (engineering TEVB viewpoint),
  * `content(X) : U.ClaimGraph` (full behavioural & structural claims).
* **Codomain `Y`.**
  `Y : U.EpistemeView` with:
  * `describedEntityRef(Y) = describedEntityRef(X)`,
  * `groundingHolonRef(Y) = groundingHolonRef(X)`,
  * `viewpointRef(Y)` either equal to or a refinement of the original engineering viewpoint (TEVB safety sub‑viewpoint),
  * `content(Y)` containing only safety‑relevant claims, plus explicit aggregation nodes (e.g. hazard summaries).

`SafetyView : X→Y` is a **DirectEpistemicViewing**:
* `describedEntityChangeMode = preserve`,
* only `content`, `viewpointRef` (within TEVB) and `meta` change,
* KD‑CAL/LOG‑CAL checks show that every hazard/mitigation claim in `Y` is entailed by `X`,
* view is idempotent and deterministic given `X` and the selected safety profile.

This is the canonical “engineering view” archetype that later species in E.17.2/TEVB refer back to.

#### A.6.3:5.2 - MVPK publication view normalisation (DirectEpistemicViewing)

*Context.*
MVPK emits a `TechCard` view `V_raw` for an arrow `f` in a morphism class (e.g. a **gate-checked, crossing-visible** service with `OperationalGate(profile)` + `DecisionLog`). The publication pipeline wants a normalised view `V_norm` where:
* arrows are ordered canonically,
* units and names follow a fixed naming discipline,
* redundant cells are removed.

*Shape.*

* `X = V_raw`, `Y = V_norm`, both `U.EpistemeView` instances with:
  * same `describedEntityRef` (the morphism’s arrow or capability),
  * same `groundingHolonRef` (runtime/plant),
  * same `viewpointRef` (publication viewpoint),
  * same `representationSchemeRef` (TechCard schema).

`NormalizeTechCard : X→Y` is a **DirectEpistemicViewing**:
* changes only `content` and `meta` (e.g. “normalised at edition E”),
* is pure and idempotent (two passes give the same normal form),
* is conservative: no new claims about the arrow `f` appear; information is only reordered or discarded.

MVPK can rely on this as an A.6.3‑conformant step without restating EFEM invariants.

#### A.6.3:5.3 - Cross‑model consistency view (CorrespondenceEpistemicViewing)

*Context.*
A system has:
* a requirements episteme `R` (“what the system should do”), and
* a design episteme `D` (“how the system does it”),

both with `describedEntityRef` pointing to the same system holon `S`, but living in different notations and contexts. A systems engineer wants a view that shows **only those requirements that currently have design coverage**.

*Shape.*

* `R : U.SystemRequirementsDescription` with ClaimGraph `C_R`.
* `D : U.SystemDesignDescription` with ClaimGraph `C_D`.
* `CM : U.CorrespondenceModel` relating requirements to design elements.
* `Y : U.EpistemeView` with:
  * `describedEntityRef(Y) = describedEntityRef(R) = describedEntityRef(D) = S`,
  * `groundingHolonRef(Y)` inherited from `R`/`D` or declared via a Bridge,
  * `content(Y)` aggregating only those requirements in `C_R` for which `CM` records coverage in `C_D`.

`CoveredRequirementsView(R,D,CM) : X→Y` (with `X` a compound episteme or a bundle episteme over `R,D,CM`) is a **CorrespondenceEpistemicViewing**:
* relies essentially on `CM` (without it, the view is undefined — fail‑closed),
* must publish witnesses that two different ways of composing local correspondences give the same result up to declared equivalence,
* remains conservative: it does not assert that any requirement is covered unless that fact is recorded in `CM` and justified in `D`.

This archetype mirrors post‑2015 work on model synchronisation and bidirectional transformations, but anchored in the EpistemeSlotGraph.

### A.6.3:6 - Consequences

* **Clear separation of viewing vs retargeting.**
  `U.EpistemicViewing` and `U.EpistemicRetargeting` (A.6.4) now **cleanly separate**:

  * “view of the same entity” vs “description of a different entity under a bridge”, and
  * vertical morphisms (`α` fixed) vs retargeting morphisms (α changes under KindBridge).

* **Stable backbone for multi‑view patterns.**
  Multi‑view description (E.17.0), viewpoint bundle libraries (E.17.1/E.17.2), and MVPK publication now share a **single notion of view morphism**, aligned with C.2.1 slots and the I/D/S discipline.

* **SlotKind-specific discipline for tools.**
  Tools implementing views (queries, projections, report generators, LLM‑based summarisation) must declare:

  * which SlotKinds they read,
  * which SlotKinds they may write,
  * and that `DescribedEntitySlot` is preserved.
    This removes ambiguity around subject/described-entity changes and supports robust static checking.

* **Alignment with modern view/query practices.**
  The pattern aligns with:
  * ISO 42010:2011/2022 and its focus on **viewpoints**, **views**, and **correspondences** over an entity‑of‑interest;
  * SysML v2 “views‑as‑queries” paradigm, where views are queries over a stable model, not new models;
  * post‑2015 work on **optics** and **displayed categories**, treating views as structured projections over a fibred category of epistemes.

### A.6.3:7 - Rationale & SoTA‑echoing  *(informative)*

* **Optics and displayed categories.**
  In categorical terms, epistemes form a category `Ep` fibred over a category of described entities `Ref` via `α : Ep → Ref`. EpistemicViewing corresponds to **vertical morphisms** that preserve α. Their behaviour closely tracks **profunctor optics**: the DescribedEntitySlot plays the role of the “focus index”, while ClaimGraphs and representation schemes act as the data being transformed. Recent work on optics (2018‑onwards) provides compositional invariants that FPF leverages without committing to a specific optic calculus.

* **Multi‑view modelling and viewpoint libraries.**
  ISO 42010 and its successors, as well as MBSE practice from ~2015 onwards, have refined the separation between **viewpoints** (families of concerns, stakeholders, and notations) and **views** (instances under those viewpoints). `U.EpistemicViewing` gives FPF a substrate‑agnostic notion of “view” that can be instantiated for architecture descriptions, safety cases, or even research epistemes/publications, while TEVB and E.17.0 specialise it to engineering holons.

* **Bidirectional transformations and consistency management.**
  Modern BX research treats views and consistency restoration as structured transformations between models, with consistency relations acting as correspondences. `U.CorrespondenceEpistemicViewing` echoes this practice but insists that:
  * viewing is **non‑creative** in intensional terms (no new commitments),
  * any strengthening or change of described entity is explicitly modelled as retargeting or Intension change.

* **Hybrid symbolic/latent representations.**
  Contemporary work on LLMs and neurosymbolic systems often toggles between:
  * symbolic specifications (logical, tabular, diagrammatic), and
  * distributed or latent representations used for computation.
    By treating `U.RepresentationScheme` and `U.RepresentationOperation` as first‑class episteme components, FPF allows EpistemicViewing to range over:
  * purely symbolic projections,
  * latent‑space projections,
  * or hybrids that invoke external mechanisms before applying a pure view, without changing the core invariants.

### A.6.3:8 - Conformance checklist (normative)

**CC‑A.6.3‑1 - EFEM species and DescribedEntityChangeMode.**
Any pattern that claims to define `U.EpistemicViewing` **SHALL**:

* declare itself a species of `U.EffectFreeEpistemicMorphing` (A.6.2),
* fix `describedEntityChangeMode = preserve`,
* and state its Applicability profile (EoIClass, contexts, viewpoints, representation schemes).

**CC-A.6.3-2 - SlotKind-specific read/write discipline.**
For each species of EpistemicViewing, authors **MUST**:

* list the SlotKinds it **reads** (typically `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `RepresentationSchemeSlot`, `ReferenceSchemeSlot`),
* list the SlotKinds it **writes** (typically `ClaimGraphSlot`, optionally `ViewpointSlot`, `RepresentationSchemeSlot`, `ReferenceSchemeSlot`, and `meta`),
* assert explicitly that `DescribedEntitySlot` is read‑only,
* and state any constraints on `GroundingHolonSlot` / `ViewpointSlot` changes.

This satisfies A.6.5 and C.2.1 checkpoint CC‑C.2.1‑5.

**CC‑A.6.3‑3 - DescriptionContext discipline (for D/S epistemes).**
When domain/codomain epistemes are `…Description`/`…Spec`:
* viewing invariants SHALL be phrased in terms of `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`,
* `DescribedEntityRef` MUST be preserved,
* `BoundedContextRef` MUST be preserved unless a Bridge is explicitly cited,
* `ViewpointRef` MUST either be preserved or changed within a declared `U.ViewpointBundle`.

**CC‑A.6.3‑4 - Conservativity witness.**
For each species, authoring SHALL provide:
* a clear statement of what counts as a **new intensional claim** in the relevant discipline,
* and a sketch of how conservativity (EV‑3) is checked or approximated (e.g. via KD‑CAL entailment, proof-support invariants, or structural invariants).

**CC‑A.6.3‑5 - Profile classification.**
* Species that do not require a `CorrespondenceModel` MUST be marked as `U.DirectEpistemicViewing`.
* Species that do require such a model MUST be marked as `U.CorrespondenceEpistemicViewing` and SHALL:
  * document the shape of the `CorrespondenceModel`,
  * describe how witness epistemes ensure oplax naturality of compositions.

**CC‑A.6.3‑6 - Separation from Retargeting and Mechanisms.**
* Any species that may change `describedEntityRef` is **not** a conformant EpistemicViewing; it MUST be treated as `U.EpistemicRetargeting` (A.6.4) or as a different pattern.
* Any species that performs measurements, actuation, or other side‑effects MUST be declared as `U.Mechanism`/`U.WorkEnactment` and cannot be an EpistemicViewing.

### A.6.3:9 - Mini‑checklist (for authors)

When you introduce a new “view” in FPF, check:
1. **Same described entity?**
   Does `describedEntityRef` stay the same? If not, this is **Retargeting**, not Viewing.

2. **Which slots move?**
   Have you listed exactly which SlotKinds you read/write, and shown that `DescribedEntitySlot` is read‑only?

3. **Conservative?**
   Can you explain, in your discipline’s terms, why the view does not introduce new claims about the same entity?

4. **Profile?**
   Is this a self‑contained projection (`U.DirectEpistemicViewing`) or does it depend on a `CorrespondenceModel` (`U.CorrespondenceEpistemicViewing`)?

5. **Context & viewpoint?**
   Have you stated:
   * the EoIClass for `DescribedEntitySlot`,
   * the contexts/ReferencePlanes you assume,
   * and the viewpoint bundle (if any) you operate under?

If all answers are crisp and the invariants EV-0...EV-6 are satisfied, the pattern is a good candidate for `U.EpistemicViewing`.

### A.6.3:End

## A.6.3.CSC - Controlled Semantic Coarsening

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Placement.** `Controlled Semantic Coarsening` is a specialization under `A.6.3 U.EpistemicViewing` for same-lineage coarsening from one source-bearing side into one coarsened rendering, whether the coarsening was planned before publication or discovered during review of a target that can be retained only under a narrower-use card. That source-bearing side may be one governed source episteme, source publication, or declared source set with a stable source-set identifier and bounded membership; it is not an open corpus.

**Builds on.** `A.6.3`, `A.6.3.CR`, `A.6.3.RT`, `E.17.EFP`, `A.6.P`, `E.8`, `E.10`, `E.19`, and `F.18`.

**Coordinates with.** `E.17.ID.CR`, `F.9`, `F.9.1`, `A.15`, `A.6.4`, `A.20`, and `A.21`.

### A.6.3.CSC:1 - Problem frame

**Use this when.** A summary, briefing, redaction, dashboard tile, lookup handle, didactic compression, or other readable target coarsens one source-bearing side by dropping or narrowing distinctions, recoverability, reliability transport, or admissible-use posture, or when review discovers that the target can be retained only as a coarsened rendering.

**Plain recognition line.** A short version is useful only while the reader can still see what it came from, what it leaves out, and when to go back.

`Controlled Semantic Coarsening` governs one coarsened rendering that remains useful only because the source-bearing side stays identifiable, the admissible use is narrower, downstream use is non-admissible from the coarsened rendering alone, and escalation reopens that source-bearing side. It is the FPF governing pattern for that source-to-rendering relation. It is not a tag, token, `U.*` kind, publication face, carrier, bridge card, stance overlay, work plan, approval, or gate.


**Start here when.** Your first honest publication unit is a small controlled-coarsening card: source-bearing side, coarsened rendering, narrower admissible use, declared source-loss mode, non-admissible downstream use, and reopen trigger. Read `orientation use`, `reliance use`, `operative claim`, `non-admissible downstream use`, and `reopen trigger` through the shared `E.17:5.1c` terms; use `E.17:5.1d` when the primary live question may be ordinary rewrite, representation change, explanation, comparison, bridge or substitution, work or reliance, gate, evidence, assurance, retargeting, or carrier or front-end work instead of coarsening.

**Neighboring project records and governing patterns.** Ordinary same-entity wording belongs under `A.6.3.CR`; representation-scheme change belongs under `A.6.3.RT`; explanation-facing class discipline belongs under `E.17.EFP`; bounded comparison belongs under `E.17.ID.CR`; bridge or substitution use belongs under `F.9` or `F.9.1`; changed described entity belongs under `A.6.4`; work authority requires `A.15`-governed selected method, `U.WorkPlan`, performed `U.Work`, work-result record, or result-measurement record; gate or adjudication authority requires `A.20` or `A.21`-governed project records.

**What goes wrong if missed.** A helpful coarsened rendering starts acting like the source-bearing side: a summary becomes evidence, a redaction becomes accountability closure, a dashboard tile becomes a causal verdict, a comparison note starts supporting bridge or substitution use, or a briefing becomes work authority.

**What this buys.** FPF users get a cheap admissible way to publish coarsened renderings without hiding declared loss, overclaiming authority, or forcing every ordinary summary through a full assurance record. This is the positive path for bounded dashboard tiles, redactions, partner notes, lookup handles, workshop simplifications, and didactic compressions that help work without pretending to be the source-bearing side.

**Working action spine.** A coarsened rendering is useful for a narrower use but cannot carry the source-bearing side -> separate source-bearing side, coarsened rendering, narrower admissible use, declared source-loss mode, non-admissible downstream use, and reopen trigger -> use the coarsened rendering for orientation, triage, disclosure, retrieval, comparison, or planning preparation -> output the six-row mini-card -> reopen or hand off if reuse, reliance, citation, dispute, bridge, work, gate, privacy, or engineering-justification demand appears.

**Ordinary use.** If the coarsened rendering is admissible only for orientation, bounded disclosure, retrieval, workshop framing, preliminary triage, comparison, or planning preparation, use the six-row mini-card and stop there.

**Load-bearing use.** Open the load-bearing coarsening record only when the coarsened rendering will be externally relied on, disputed, cited, used across context, policy-bearing, bridge-adjacent, work-adjacent, gate-adjacent, privacy-sensitive, or engineering-justification-facing.

**Stop condition.** Stop at the mini-card when the coarsened rendering changes no next admissible work or reliance, disclosure, review, or planning-preparation move and blocks no concrete overclaim beyond its narrower admissible use.

**Admissible-use examples.**

| Admissible project use | Source-finding or reversible probe | Non-admissible downstream use |
| --- | --- | --- |
| A redacted partner note, bounded dashboard tile, lookup handle, workshop simplification, or didactic compression is admissible for triage, bounded disclosure, retrieval, coordination, or planning preparation inside its narrower use. | A tile or redacted note cues source-bearing reopen before release, audit, accountability, or engineering-justification reliance. | The coarsened rendering is used as release authority, evidence, audit closure, accountability finding, bridge or substitution support, work authority, or assurance conclusion. |


**Not this pattern when.** Not this pattern when the primary question is ordinary same-entity wording, representation-medium change, explanation fidelity, comparison, bridge or substitution use, changed described entity, work authority, approval, adjudication, or gate authority. Use the neighboring governing FPF pattern or `authoritySourceRef` target for that primary question.

### A.6.3.CSC:2 - Problem

FPF often needs a coarsened form of a source-bearing side: a manager summary, a redacted disclosure note, a dashboard tile, a lookup surrogate, a workshop simplification, or a didactic compression. The coarsened form can be valuable, but it becomes dangerous when readers forget that its admissible use is narrower than the source-bearing side.

The core failure is not ordinary omission by itself. The failure appears when the coarsened rendering stays honest only under an admissible-use card like this:

- the source-bearing side remains governing;
- the coarsened rendering has a declared `source-loss mode` or reduced recoverability;
- the target makes only the narrower use admissible;
- downstream use is non-admissible from the coarsened rendering alone;
- downstream use reopens the source-bearing side or moves to the exact governing FPF pattern or `authoritySourceRef` target that supports the requested use.

Without a named pattern for that relation, neighboring patterns repeat partial coarsening rules locally. The repetition hides the shared load and makes it too easy for coarsened renderings to travel as if they were the source-bearing side.

### A.6.3.CSC:3 - Forces

| Force | Tension |
| --- | --- |
| Reader economy vs source support | Readers need short, useful renderings, but shortness must not erase the source-bearing side or its limits. |
| Ordinary use vs load-bearing use | A small summary should stay cheap, while disputed, cited, external, policy, bridge, work, or gate-adjacent use needs more assurance. |
| Helpfulness vs unsupported authority reading | The clearer the coarsened rendering is, the more likely it is to be over-read as evidence, bridge or substitution support, approval, or execution authority. |
| Coarsening-chain reuse vs provenance reset | Reusing one coarsened rendering to make another saves effort, but it must not reset source path, loss envelope, uncertainty, or reopen duty. |
| Neighbor clarity vs family sprawl | The coarsening relation needs one governing pattern without stealing ordinary rewrite, representation, explanation, comparison, bridge, stance, work, or gate discipline from neighboring patterns. |

### A.6.3.CSC:4 - Solution

`Controlled Semantic Coarsening` governs one source-to-rendering relation.

- **Source-bearing side** means the governed `U.Episteme`, governed `U.EpistemePublication`, or declared source set that still carries the fuller claim, distinction, evidence relation, trace relation, or authority-reference relation. A declared source set must have a stable source-set identifier, bounded membership, and a reopen condition; an open corpus, folder, topic area, search-result cluster, or vague document neighborhood is not a source-bearing side.
- **Coarsened rendering** means the target readable form that carries a declared `source-loss mode`, reduced recoverability, reduced reliability transport, or narrower admissible use than the source-bearing side.
- **Narrower admissible use** means the practical use the coarsened rendering makes admissible, such as orientation, retrieval, bounded disclosure, workshop framing, or preliminary triage.
- **Non-admissible downstream use** means the use the coarsened rendering does not make admissible alone, such as approval, audit closure, release gate, work plan, equivalence, bridge or substitution use, accountability finding, or canonical technical claim.
- **Reopen trigger** means the condition that requires return to the source-bearing side, re-expansion in the current rendering or publication, or handoff to another governing FPF pattern or `authoritySourceRef` target.
- **Load-bearing case** means a coarsening case that will be cited, disputed, externally relied on, policy-bearing, bridge-adjacent, gate-adjacent, work-adjacent, privacy-sensitive, or assurance-facing.

#### A.6.3.CSC:4.1 - Ordinary mini-card

For ordinary use, publish only the smallest card that keeps the coarsened rendering honest.

| Row | Question |
| --- | --- |
| Source-bearing side | What governed source episteme, source publication, or declared source set remains governing and reopenable? |
| Coarsened rendering | What coarsened readable form is being offered to the reader? |
| Narrower admissible use | What use does this coarsened rendering make admissible? |
| Source-loss mode | Which declared source-loss mode is live: omitted-detail, qualifier-loss, redaction, aggregation, scope-narrowing, recoverability-loss, representation-factor-loss, or coarsening-loss? |
| Non-admissible downstream use | What downstream claim, effect, work, or reliance use is not admissible from this coarsened rendering alone? |
| Reopen trigger | What demand forces source-bearing return, re-expansion, or governing-pattern handoff? |

A CSC card makes only the narrower admissible use named on the card admissible for the coarsened rendering. It never makes the non-admissible downstream use admissible; it only tells the reader when and where to reopen the source-bearing side or hand off to the governing pattern that carries that downstream use.

The card may live inline. Inherited source pins count when the surrounding publication already makes the source-bearing side visible.

If the coarsened rendering is used only for local orientation and the source-bearing side remains adjacent, the six-row card may be inline or implicit by immediate context; do not create a durable `Controlled Semantic Coarsening` object unless reuse, reliance, citation, or dispute appears.

#### A.6.3.CSC:4.2 - First check

Before using this pattern, ask five questions:

1. Is there exactly one source-bearing side: one governed source episteme, source publication, or declared source set with stable identifier, bounded membership, and reopen condition?
2. Does the target declare a source-loss mode against that source-bearing side, or has review shown that it can be retained only as a coarsened rendering?
3. Does the target make only narrower use admissible?
4. Is downstream use explicitly non-admissible from the target alone?
5. Is the source-bearing reopen or governing-pattern handoff trigger visible?

If any answer is no, do not polish a coarsening story. Use the ordinary governing pattern or recover the exact project-side FPF kind and reference or authority-reference relation that actually supports the requested use. If the required support is missing, create only a prospective repair request, future decision request, prospective work-plan entry, or explicit source-gap note; do not treat that request or note as retroactive support for the coarsened rendering, earlier claim or effect, work occurrence, evidence, approval, gate passage, release permission, or engineering justification.

#### A.6.3.CSC:4.3 - Ordinary vs load-bearing

Ordinary cases should remain light. A short orientation summary, redacted partner note, workshop simplification, or lookup handle does not need the full assurance record if the six-row card is recoverable.

Load-bearing cases add only the fields that matter for the live use, dispute, reliance, citation, policy, bridge, work, gate, privacy, or assurance case. This list is not a daily gate for ordinary summaries, briefings, redactions, or lookup handles:

The fields below inherit the `E.17:5.1e` local-field rule. They are review aids for one coarsened-rendering case, not `U.Kind`, `SurfaceKind`, `RelationKind`, `KindBridge`, `EvidenceKind`, `GateDecision`, `SpeechAct`, `Commitment`, `U.Work`, `authoritySourceRef` target, or exact project-side FPF kind and reference unless another governing FPF pattern explicitly instantiates that object.

- `sourceBearingSideRef` and `coarsenedRenderingRef` when the source-bearing side, coarsened rendering, `PublicationUnit`, publication face, `PublicationSurface`, `InteropSurface`, or carrier could be confused;
- `targetPublicationUnitIfAny` when the coarsened rendering is carried by one `PublicationUnit` that is distinct from the publication, disclosure note, dashboard tile, or `InteropSurface` on which it appears;
- `governingPatternRef`, `projectSourceRecordRef`, or one privileged reopen path, so a coarsened rendering cannot reset its own provenance;
- `coarseningBranch`, `sourceLossMode`, and `admissibleUsePosture` as separate fields;
- `recoverabilityAfterCoarsening` when the source-loss mode affects claim support, accountability, admissible-use posture, or later citation;
- at least one kept claim bundle or distinction bundle, one coarsened or dropped bundle, and one reopen-only bundle when the case is disputed or later-cited;
- `sourceSupportPosture` when the `E.17:5.1b` postures could diverge: source pointer, source availability, source retrieval, source use, source faithfulness, claim support, contradiction, plausibility-only, omission, declared source-loss mode, added commitment, added linkage, independent verification, admissible use, non-admissible downstream use, or reopen trigger;
- uncertainty or abstention posture when branch reading, preserved distinctions, source pin, or admissible use cannot yet be stated stably;
- independent-verification question when downstream testing, assurance, gate, or external reliance appears;
- `audienceOverReadRisk`, plus a light reader-reliance or user-evidence check when readers may mistake the coarsened rendering for authority it does not carry;
- whether local re-expansion is enough to repair the current rendering or whether downstream use still needs return to the source-bearing side or named `authoritySourceRef` target.

#### A.6.3.CSC:4.4 - Branch and admissible-use discipline

`coarseningBranch` answers what sort of coarsening case this is. `sourceLossMode` names what was lost from the source-bearing side. `admissibleUsePosture` answers which use of the coarsened rendering remains admissible. Do not infer any one of the three from the others.

| Field | Values this pattern uses | Rule |
| --- | --- | --- |
| `coarseningBranch` | aggregation or quotient-like orientation; source-pinned surrogate, index, or handle; privacy or redaction case; exceptional interop-facing simplification | The branch names the kind of coarsening case, not the source-loss mode and not the authority granted by the coarsened rendering. |
| `admissibleUsePosture` | ordinary-admissible; source-pinned-only; authoritySourceRef-reopen-only; non-admissible-by-default | The use posture names which use the coarsened rendering makes admissible. |

Ordinary admissible use covers aggregation, quotient-like orientation, didactic or report summaries, and briefings only for the named narrower use. Source-pinned-only use covers surrogate, index, retrieval-hint, lookup, and handle forms; these may help find or orient to the source but do not provide claim support themselves. `authoritySourceRef-reopen-only` covers the exceptional case where the coarsened rendering names the source whose named authority relation must be reopened; the coarsened rendering itself does not become the `authoritySourceRef` target, evidence source, gate source, or work source.

Privacy or redaction cases are admissible here only when the card names the sharing boundary, the source-loss mode, what was withheld or coarsened, the main re-identification or accountability risk being reduced, the source-bearing review path, and the accountability or gate uses that remain non-admissible.

Exceptional interop-facing simplification is not ordinary coarsening. It is admissible here only when it stays source-tethered and names the operative relation kind, such as bounded contrast, broader or narrower, partial overlap, proxy, lossy normalization, or context-bounded match. If the coarsened rendering makes bounded contrast across contexts or source epistemes or source publications is the primary question, use `E.17.ID.CR`. If it implies equivalence, substitution, projection, or bridge or substitution use, use `F.9` or `F.9.1`.

#### A.6.3.CSC:4.5 - Source-loss mode, recoverability, and anti-overread

The card must name the live `sourceLossMode` before a coarsened rendering is treated as admissible for its stated use. A source-loss mode is not a strength scale. It names which source-bearing distinction failed to travel into the coarsened rendering.

| Source-loss mode | Declared loss |
| --- | --- |
| `omitted-detail` | A detail present on the source-bearing side is absent from the coarsened rendering. |
| `qualifier-loss` | A condition, caveat, uncertainty marker, scope qualifier, temporal qualifier, modality marker, recommendation status, evidence status, possibility status, obligation status, or decision status is absent, collapsed, or less explicit. |
| `redaction` | Detail is withheld for a sharing boundary, privacy, safety, legal, partner-disclosure, accountability, or release reason. |
| `aggregation` | Several source distinctions, alternatives, entities, states, records, or slices are combined into one aggregate or quotient-like readable form. |
| `scope-narrowing` | The coarsened rendering carries only a narrower claim scope, audience scope, time window, source slice, context, population, or use scope. |
| `recoverability-loss` | The reader cannot recover source distinctions, pins, trace, provenance, confidence, relation structure, source support, or decode path from the coarsened rendering at the level needed for the proposed use. |
| `representation-factor-loss` | A representation shift drops inspection possibilities, comparability, ordering, topology, relation structure, viewpoint support, publication-face support, or reasoning-medium factors that mattered on the source-bearing side. |
| `coarsening-loss` | The full CSC relation is live: source-bearing side, coarsened rendering, narrower admissible use, declared source-loss mode, non-admissible downstream use, and source-bearing reopen. |

Recoverability and admissible use are separate. A recoverable coarsened rendering is not automatically admissible for downstream use, and a non-admissible use is not repaired merely by saying the source could be found.

| Recoverability class | Reading |
| --- | --- |
| directly recoverable | the coarsened rendering itself still carries enough detail to recover the source-side distinction |
| source-pinned recoverable | the distinction is recoverable only by returning to the named source-bearing side |
| reconstruction or validation required | recovery needs a new reconstruction, test, or validation, so downstream use remains blocked until that work is done |
| not recoverable from admissible source epistemes or source publications | the available source epistemes or source publications, traces, or cited `authoritySourceRef` targets cannot restore the distinction; do not treat the coarsened rendering as support for downstream reliance |

A coarsening chain may not silently reset provenance. If one coarsened rendering is reused to make another, the same source-bearing side must stay explicit, the earlier source-loss mode and uncertainty posture must remain visible, and the new rendering must declare only the added source-loss delta. If that cannot be stated cleanly, reopen the source-bearing side rather than extending the chain.

Aggregation or quotient-like coarsening remains inside this pattern only while the coarsened rendering keeps one bounded described set, slice, case bundle, or alternative bundle explicit as the described entity or described set. If several entities, alternatives, or slices become one new class target or proxy target, apply `A.6.4`.

#### A.6.3.CSC:4.6 - Neighbor exits

| If the primary question is now... | Use this governing FPF pattern or `authoritySourceRef` target |
| --- | --- |
| Same-entity textual rewording without a separate narrower-use card | `A.6.3.CR` |
| Representation scheme or reasoning-medium shift | `A.6.3.RT` |
| Explanation-facing class over existing source `U.Episteme` or `U.EpistemePublication` | `E.17.EFP` |
| Bounded comparison over already pinned source epistemes or source publications | `E.17.ID.CR` |
| Equivalence, substitution, interop row, or bridge or substitution use | `F.9` |
| Stance over an already published bridge card | `F.9.1` |
| Changed described entity or proxy target | `A.6.4` |
| Carrier, export, OCR or parsing, or front-end behavior is primary | `A.7` first; then `A.6.3.RT`, `A.6.3.CSC`, `A.6.4`, or interpretation sources only if meaning-bearing structure, loss, retargeting, or interpretive lift is live |
| Briefing treated as work plan, work authority, or execution cue | `A.15` |
| Gate, approval, assurance, or adjudication authority | `A.20` or `A.21` |

Neighboring governing patterns may point here when a coarsened rendering relation becomes primary. They do not govern the shared coarsening relation by local repetition.

#### A.6.3.CSC:4.7 - Well-formedness constraints

**Well-formedness constraint CSC-WF-1 (source-to-rendering relation).** A controlled-coarsening case is well formed only when it contains exactly one source-bearing side, at least one coarsened-rendering side, one declared narrower admissible use, one non-admissible downstream use, and one visible source-bearing reopen or governing-pattern handoff condition. The source-bearing side may be one governed source episteme, source publication, or declared source set with stable source-set identifier and bounded membership; it must not be an open, vague corpus.

**Well-formedness constraint CSC-WF-2 (no authority upgrade).** A coarsened rendering does not gain evidence, bridge, work, approval, gate, or adjudication authority by repetition, fluency, audience convenience, citation, or publication on a more visible publication face or channel.

**Well-formedness constraint CSC-WF-3 (source path continuity).** A coarsening chain remains well formed only while the same source-bearing side, prior source-loss mode, uncertainty posture, and added source-loss delta remain recoverable.

### A.6.3.CSC:5 - Archetypal Grounding

**Tell.** Controlled semantic coarsening is the disciplined act of making a coarsened rendering useful while keeping the source-bearing side and the non-admissible downstream uses visible. It is not simplification as style. It is simplification under a source, use, loss, and reopen card.

**Show (System).** A service team has an incident review with trace details, confidence bands, and alternative branches. A manager dashboard tile says: `Cache failover evidence is the leading concern; details remain in IR-42.` The tile may orient planning, but it may not approve release, close audit, prove causality, or trigger work without reopening `IR-42`.

**Show (Episteme).** A research review bundle is given the lookup handle `cache-failover risk`. The handle is admissible for retrieval and orientation only. Any claim-bearing use reopens the review bundle because the handle does not carry the evidence, alternatives, or source support.

#### A.6.3.CSC:5.1 - Worked slices

**Manager orientation summary.** The source-bearing side is incident review `IR-42` with trace details, confidence bands, and alternative branches. The coarsened rendering is `Cache failover evidence is the leading concern; details remain in IR-42.` Its narrower admissible use is orientation for planning conversation. Its non-admissible downstream uses are approval, audit closure, release gate, causal proof, and work order.

**Redacted partner note.** The source-bearing side is a full incident record with actor identity, trace path, and recovery evidence. The coarsened rendering is a partner-facing redacted note that withholds actor identity and trace path. Its narrower admissible use is bounded disclosure and coordination. Accountability, legal, audit, readiness, and gate uses reopen the full incident record or name the relevant `authoritySourceRef` target.

**Redacted functional-description publication.** The source-bearing side is a functional architecture note that names flow relations, method-selection limits, work-plan prerequisites, result-measurement requirements, and two exception cases. The coarsened rendering is a partner-facing table that keeps the main flow relation and removes the exception cases and result-measurement details. Its narrower admissible use is bounded orientation for coordination. Work planning, gate passage, evidence, engineering justification, control-architecture use, and release permission reopen the source-bearing side or apply `A.15`, `A.10`, `B.3`, `A.20`, `A.21`, or `B.2.5` as the live claim requires.

**Exceptional interop-facing simplification.** The source-bearing side is two pinned context notes plus their bridge or comparison basis. The coarsened rendering is: `For this exchange only, Field A is treated as broader than Field B; see source notes for exceptions.` The rendering may orient the exchange, but any equivalence, substitution, projection, bridge-row, or approval use applies `F.9` or `F.9.1` or reopens the source-bearing side basis.

**Bad fit: hidden work authority.** `Deployment may proceed; see summary S-3.` This is not an admissible controlled coarsening card. The sentence tries to convert a coarsened summary into execution or gate authority. Use `A.15`, `A.20`, or `A.21`, and reopen the source-bearing side before any work or approval claim proceeds.

### A.6.3.CSC:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto and Epist**, **Prag**, **Did**. Scope: **Universal** for source-to-rendering relations that claim controlled semantic coarsening inside FPF.

This pattern favors **Prag** and **Did** by allowing useful coarsened renderings to remain cheap and readable. It also favors **Gov** and **Arch** by requiring non-admissible downstream use, source reopen, and neighboring-pattern application when release, policy, assurance, adjudication, bridge, work, evidence, or gate use is attempted. The mitigation for over-governance is the ordinary mini-card: ordinary cases stay light, and only dispute, citation, external reliance, policy, bridge, work, gate, privacy, assurance, release, or adjudication use adds load-bearing fields.

### A.6.3.CSC:7 - Conformance Checklist

A conformance check is retained only if it changes the next admissible use of the coarsened rendering, blocks a concrete overclaim, or preserves the source-bearing reopen path needed for the declared admissible use.

#### A.6.3.CSC:7.1 - CSC-Core

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-CSC-1 (Source visible).** | A conforming controlled-coarsening card SHALL name the source-bearing side or inherit it from the immediate source context. | Prevents the coarsened rendering from resetting provenance. |
| **CC-CSC-2 (Rendering explicit).** | A conforming card SHALL identify the coarsened rendering and keep it distinct from the source-bearing side. | Prevents citation laundering and source-to-rendering collapse. |
| **CC-CSC-3 (Admissible use).** | A conforming card SHALL state the narrower admissible use. | Keeps ordinary convenience from becoming broad authority. |
| **CC-CSC-4 (Non-admissible downstream use).** | A conforming card SHALL state the non-admissible downstream use. | Makes over-read and misuse visible early. |
| **CC-CSC-5 (Reopen or handoff).** | A conforming card SHALL state the source-bearing reopen trigger or governing-pattern handoff condition. | Gives readers an admissible next move under dispute, citation, reliance, policy, bridge, work, gate, privacy, assurance, release, or adjudication use. |
| **CC-CSC-6 (Ordinary economy).** | Authors SHOULD keep ordinary cases to the mini-card unless dispute, citation, external reliance, policy, bridge, work, gate, privacy, or assurance use is live. | Preserves usability and avoids daily-process inflation. |

#### A.6.3.CSC:7.2 - CSC-Conditional

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-CSC-7 (Use-specific assurance).** | Load-bearing cases SHALL add only the support fields needed for the live use, dispute, or reliance case. | Keeps the assurance surface tied to real risk. |
| **CC-CSC-8 (Branch and use split).** | Load-bearing or disputed cases SHALL keep `coarseningBranch` and `admissibleUsePosture` separate. | Prevents the coarsening branch from implying source-loss mode or authority. |
| **CC-CSC-9 (Source-loss mode and recoverability).** | Cases affecting claim support, accountability, admissible-use posture, or later citation SHALL state source-loss mode and recoverability class. | Prevents recoverability from being mistaken for admissible use. |
| **CC-CSC-10 (Coarsening-chain continuity).** | A coarsening chain SHALL satisfy `CSC-WF-3` or reopen the source-bearing side. | Prevents provenance reset by repeated summarization. |
| **CC-CSC-11 (Governing-pattern exits).** | Bridge, stance, work, gate, adjudication, and changed-entity claims SHALL be handled by their governing patterns or publications with named authority-reference relations. | Prevents CSC from stealing neighboring pattern duties. |
| **CC-CSC-12 (No authority by repetition).** | A conforming card SHALL satisfy `CSC-WF-2`. | Blocks authority laundering through fluency or citation. |
| **CC-CSC-13 (Source, rendering, and publication separation).** | Load-bearing cases SHALL separate source-bearing side, coarsened rendering, `PublicationUnit`, publication face, `PublicationSurface`, `InteropSurface`, and carrier when those could be confused. | Keeps `PublicationUnit`, publication face, and carrier roles distinct. |
| **CC-CSC-14 (Privacy and redaction).** | Privacy or redaction cases SHALL name the sharing boundary, withheld distinctions, risk basis, non-admissible accountability or gate uses, and source-bearing review path. | Prevents redaction from becoming closure. |
| **CC-CSC-15 (Interop simplification).** | Exceptional interop-facing simplifications SHALL name the operative relation kind and hand bridge or equivalence pressure to `F.9` or `F.9.1`. | Prevents simplified relation language from supporting bridge or substitution use. |
| **CC-CSC-16 (Source support posture).** | Load-bearing source-support cases SHALL use the `E.17:5.1b` vocabulary where needed: source pointer, source availability, source retrieval, source use, source faithfulness, claim support, contradiction, plausibility-only, omission, declared source-loss mode, added commitment, added linkage, independent verification, admissible use, non-admissible downstream use, and reopen trigger. | Keeps helpful renderings from passing as evidence. |

### A.6.3.CSC:8 - Common Anti-Patterns and How to Avoid Them


| Anti-pattern | Failure | Avoid by |
| --- | --- | --- |
| Helpful summary becomes authority | The coarsened rendering starts deciding downstream questions that it does not carry. | Publish non-admissible downstream use and reopen trigger. |
| Citation laundering | A coarsened rendering is cited as if it were the source. | Keep the source-bearing side named and reopenable. |
| Label-as-evidence | A lookup handle carries a claim. | State retrieval-only use. |
| Redaction-as-closure | Withheld detail is treated as resolved detail. | State the sharing boundary and accountability reopen condition. |
| Stance cure | `projection` or `nonEquivalent` is used instead of a bridge card or source return. | Apply `F.9` or `F.9.1` for the bridge claim. |
| Briefing-as-work | A summary becomes work plan, action cue, gate, or approval. | Use `A.15`, `A.20`, or `A.21` for the work, constraint, or gate claim. |
| Summary-chain source loss | A note summarizes an already coarsened note and loses the original source and loss envelope. | Keep the same source-bearing side and added loss delta visible, or reopen that source-bearing side. |
| Aggregation target shift | A quotient or bundle turns several entities or alternatives into one new proxy target. | Apply `A.6.4` rather than treating target shift as a same-lineage source-to-rendering case. |

### A.6.3.CSC:9 - Consequences

| Benefits | Trade-offs and mitigations |
| --- | --- |
| Cheap coarsened renderings stay admissible because the source, admissible use, loss, non-admissible use, and reopen path remain visible. | Authors must add a small card where they might otherwise write only a friendly summary. The mitigation is that ordinary cases need only the mini-card. |
| Neighboring patterns can hand coarsening boundary to one common governing pattern instead of repeating partial local doctrine. | Readers must still keep the primary question with the governing FPF pattern or `authoritySourceRef` target that carries it. The neighbor-exit table and bad-fit examples keep that disposition inspectable. |
| Load-bearing coarsening becomes reviewable without making every summary a full assurance object. | In high-risk cases the assurance record can grow. The use-specific field rule keeps growth tied to real risk. |

### A.6.3.CSC:10 - Rationale

Controlled coarsening is useful because FPF work often needs cheap readable forms. It is risky because cheap readable forms often travel farther than their admissible use. The pattern therefore does not ban coarsened renderings; it makes the source-to-rendering relation explicit enough that later users know when to stop, reopen, or hand off to another governing FPF pattern or `authoritySourceRef` target.

This pattern is narrower than a general simplification pattern. It applies only when the coarsened rendering remains tied to a source-bearing side and carries a narrower-use card.

The core memory aid is simple: a coarsened rendering may help reading, but it must not become the source-bearing side it was derived from. It may expose or cite the source-bearing side or the exact project-side FPF kind and reference that carries the requested support; that exposed source or value remains the support, not the coarsened rendering's readable face. If support is missing, a repair request, source-gap note, or reopen note may guide only future repair or return to source; it does not backdate the coarsened rendering into source support.

### A.6.3.CSC:11 - SoTA Alignment: Adopted Or Adapted Invariants And Rejected Shortcuts

**SoTA alignment rule.** Read each row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and Relations of this pattern.


**Purpose.** This section justifies the pattern's safeguards. It is not an additional operational checklist. The Solution, Conformance Checklist, worked slices, and Relations above carry the live pattern discipline.

**Positive SoTA role.** Use CSC when a coarsened readable rendering is still worth using in project work, but only for a narrower admissible use and without pretending that the rendering carries the source-bearing side's support.

| Claim need | Source idea and current source | Current source reference | Local FPF invariant and practical local test | Adopted or adapted invariant and rejected shortcut |
| --- | --- | --- | --- | --- |
| Fluent summaries and generated renderings can be useful without carrying source support. | Summarization and factuality work separates fluency from faithfulness, attribution, and fine-grained source support. | Maynez et al. (2020), *On Faithfulness and Factuality in Abstractive Summarization*; Min et al. (2023), *FActScore*; Es et al. (2023), *RAGAS*; source maturity = research papers and evaluation practice supporting evaluation posture. | `A.6.3.CSC` adopts the `E.17:5.1b` source-support distinction by separating source pointer, source availability, or source retrieval, source use, source faithfulness, claim support, contradiction, plausibility-only, omission, declared source-loss mode, added commitment, added linkage, independent verification, admissible use, non-admissible downstream use, and reopen trigger. | **Adopt or adapt.** Adopt the warning against fluent unsupported output; adapt it into a lightweight FPF card so ordinary summaries are not forced into full evaluation studies. |
| Redaction and de-identification reduce exposure without deleting accountability or audit questions. | Privacy-risk and de-identification guidance treats disclosure boundary, residual risk, and governance context as part of safe release. | NIST SP 800-188, *De-Identifying Government Datasets* (2023); source maturity = current government guidance. | The privacy and redaction branch requires sharing boundary, withheld distinctions, source-bearing review path, and non-admissible accountability or gate uses. | **Adapt.** Use privacy governance as a safeguard for bounded disclosure while rejecting redaction-as-closure. |
| Views, representations, and relation kinds remain load-bearing even when a publication face or rendering is made easier to read. | Architecture-description and model-based practice make viewpoint, view, model kind, and traceable relation explicit rather than treating a clearer view as neutral formatting. | ISO/IEC/IEEE 42010:2022; OMG SysML v2.0 Language Specification (2025); source maturity = mature standard plus current technical specification. | The pattern keeps coarsening distinct from representation transduction, explanation profiling, comparative reading, bridge cards, bridge-stance overlays, and work and gate authority. | **Adopt or adapt.** Adopt explicit view and relation discipline; adapt it to same-lineage coarsened renderings and neighbor exits. |
| Data and interoperability publication practice distinguishes discoverability, metadata, validation, and exchange from authority to substitute one object for another. | Web-data and semantic-web standards separate catalog metadata, provenance, structural metadata, and validation conditions from the data or relation itself. | W3C Data on the Web Best Practices (2017); W3C SHACL (2017); W3C DCAT v3 (2024); source maturity = mature web standards and recommendations for metadata, validation, and catalog interoperability. | Exceptional interop simplification must name its relation kind and apply `E.17.ID.CR`, `F.9`, or `F.9.1` when the case carries equivalence, substitution, projection, or bridge claims. | **Adapt or reject.** Adapt explicit metadata and validation discipline; reject using a simplified relation gloss as support for bridge or substitution use. |
| Explanation usefulness depends on the user and can be over-read as authority it does not carry. | Explainable-AI practice treats explanation as audience-facing support with limits, not as a universal guarantee. | NIST IR 8312, *Four Principles of Explainable Artificial Intelligence* (2021); source maturity = current government guidance. | `audienceOverReadRisk` and source reopen keep helpful prose subordinate to the source-bearing side when stakes rise. | **Adopt or adapt.** Adopt user-sensitive explanation limits; adapt them to FPF coarsening cases where a rendering is useful but not authoritative for downstream use. |

The practical implication is the same across these traditions: coarsened readable publication faces or renderings are valuable, but their admissible use depends on source support, relation kind, validation evidence, audience, and reopen path. The worked slices in `A.6.3.CSC:5.1` are the nearest recovery anchors for those SoTA rows.

**Semantic-web boundary.** In the W3C row, Data on the Web, SHACL, and DCAT support publication metadata, provenance, validation, cataloging, and interoperability. They do not by themselves support work occurrence, gate passage, bridge or substitution use, equivalence, release permission, or project claim support; those uses require the governing pattern or exact project-side FPF kind and reference that carries that claim.

### A.6.3.CSC:12 - Relations

- **Specializes:** `A.6.3 U.EpistemicViewing` for declared source-loss mode in a same-lineage source-to-rendering relation.
- **Coordinates with:** `A.6.3.CR`, `A.6.3.RT`, `E.17.EFP`, `E.17.ID.CR`, `F.9`, `F.9.1`, `A.15`, `A.6.4`, `A.20`, and `A.21`.
- **Does not replace:** conservative retextualization, representation transduction, explanation profiling, bounded comparative reading, bridge-card discipline, stance overlay, changed-object discipline, work authority, gate authority, or adjudication authority.
- **Entry relation:** neighboring patterns may hand off here when a coarsened rendering's narrower-use, non-admissible-use, and reopen card becomes the primary question.
- **Governing-pattern relation wording:** this pattern is a `specialization under A.6.3`, not a bundle, suite, profile, overlay, or review pack. Its governing role is limited to the controlled-coarsening relation itself.

### A.6.3.CSC:12a - Boundary with quantum-like state-representation coarsening

Use CSC first when one source-bearing side, model, state representation, or evidence set is made less detailed for a narrower use, or when review discovers that a target already in circulation can be retained only under a narrower-use card: summary, dashboard row, orientation note, partner-safe version, simplified diagram, or coarse working description. Ordinary controlled simplification remains CSC even when it is lossy.

Action path:

1. Name the source-bearing side and the coarsened version.
2. State the use scope of the coarsened version before stating what it means.
3. State the lost distinctions, evidence paths, comparability, uncertainty, state dimensions, or alternatives.
4. State admissible use and non-admissible use in practical terms.
5. State when to reopen the source-bearing side.
6. If the coarsened rendering claims to preserve action, intervention, manipulation, explanation, or cross-abstraction structure, state the causal-abstraction or approximate-causal-abstraction mapping before treating the shortcut as QL coarsening.
7. Ask whether the shortcut depends on a QL cue such as incompatible probes, contextual probability, instrument-like update, open-information-system update whose update rule, probe frame, or export admissibility is part of the modeling requirement, or no faithful-enough export of the represented state for the admissible use. If not, stay in CSC.
8. If yes, coordinate with the `C.26` state-representation coarsening support section while leaving CSC as the controlled-use boundary for the coarsened version.

For ordinary use, start with the standard shortcut mini-form:


| Mini-entry | Question |
| --- | --- |
| Source | Which source-bearing side, model, state representation, or evidence set is being coarsened? |
| Shortcut | Which less detailed rendering or working shortcut is used instead? |
| Loss | Which distinction, evidence path, comparability, uncertainty, state dimension, or alternative is not carried? |
| Admissible use | Which triage, orientation, explanation, or local decision use remains admissible? |
| Reopen | Which dispute, decision change, admissible-use shift, threshold crossing, or non-admissible-use demand sends the reader back to the source-bearing side? |

Use a fuller CSC and `C.26` coarsening boundary record only when the coarsened state representation will be reused, formalized, empirically compared, used in a high-stakes decision, or tied to a comparative performance claim:

| Field | Required content |
| --- | --- |
| Source-bearing side | Which richer source episteme or source publication, model, state representation, or evidence set is being coarsened |
| Coarsened version | What the reader receives instead |
| Lost distinctions | What precision, comparability, evidence path, state dimension, or alternative is not carried |
| Admissible use | Which triage, orientation, explanation, or local decision use remains admissible |
| Non-admissible downstream use | Which downstream decision, audit, assurance, release, causal, or work-order use is not admissible |
| Reopen path | When the source-bearing side or more precise state representation must be reopened |
| QL cue, if retained | Which incompatible-probe, contextual-probability, instrument-update, open-information-system update, probe, or export-admissibility, or faithful-enough-export requirement remains after ordinary CSC |

Useful outputs:

- a CSC mini-form when the issue is controlled simplification;
- a fuller C.26 coarsening support record only when a QL cue remains and the claim is reusable, formal, empirical, high-stakes, or comparative-performance-bearing;
- no QL wording when the case is only summary, anonymization, diagramming, audience adaptation, or ordinary coarsening.

### A.6.3.CSC:12b - C.29 MLA relation

> When controlled semantic coarsening depends on mathematical abstraction, quotienting, coarse-graining, or a learned coarse representation, `A.6.3.CSC` still governs the source-bearing return condition, narrowed admissible use, non-admissible downstream claim, and coarsened rendering. The applicable `C.29` output for the stated use (`MLA.LensCandidateNote`, `MLA.OneLine`, `MLA.MiniCard`, or `MLA.FullCard` when required) may be cited only for adequacy of the mathematical abstraction or coarse-graining lens. It does not make the coarsened rendering a bridge, replacement source, evidence record, or causal-use support.


### A.6.3.CSC:End
## A.6.3.CR - ConservativeRetextualization — same-described-entity textual re-expression
> **Status:** Stable

**Placement.** Specialization under `A.6.3 U.EpistemicViewing` for same-described-entity textual re-expression.
**Builds on.** `A.6.3 U.EpistemicViewing`; `A.6.2 U.EffectFreeEpistemicMorphing`; `A.7`; `E.10.D2`; `E.17.0`; `E.17`; `F.9`; `F.18`; `E.10`.
**Coordinates with.** `ExplanationFaithfulnessProfile`; `RepresentationTransduction`; `E.17.ID.CR ComparativeReading`; `A.6.4 U.EpistemicRetargeting`; `B.5.2`; `A.15`.

**One-line summary.** `ConservativeRetextualization` is a same-described-entity textual re-expression of an episteme that stays inside `A.6.3 U.EpistemicViewing`: it may shorten, reorder, filter, translate, or restate claims, but it does **not** silently change `describedEntityRef`, add new claims about that entity, or hide bridge work.
**Governed object in plain terms.** One published textual rendering over the same described entity; not the whole source corpus, not an explanation face, and not a downstream decision or publication with named authority-reference relation.
**Governing move in plain terms.** Restate already available content textually while preserving `describedEntityRef`, keeping source tether visible, and making loss or omission inspectable.

**Use this when.** Use this pattern when one already available source line about the same described entity needs a second textual form such as a report rewrite, summary, translation, or declared filtered restatement, and the real job is still same-entity textual re-expression rather than explanation, representation change, or retargeting.

**Start here when.** Your first honest publication unit is still a text over the same described entity, and the main review question is whether omissions, softening, or foregrounding remain conservative and source-tethered.

**What goes wrong if missed.** A summary, translation, or manager-readable rewrite gets treated as harmless editing even after it has started hiding explanation work, bridge work, changed authority posture, or a separate narrower-use card.

**What this buys.** One honest same-entity textual rewrite with visible source tether, visible omission or loss notes, and an explicit handoff when the case stops being only conservative retextualization.

**Working action spine.** Same described entity needs a second textual form -> separate source slice, published slice, omission or source-loss note, and admissible use -> use the rewrite for readable restatement, source-finding, review, comparison, or planning preparation -> output one source-slice to published-slice sentence or mini-card -> hand off if coarsened rendering, explanation, representation change, retargeting, work, evidence, gate, release, policy, assurance, adjudication, or bridge use is attempted.

**Ordinary use.** If the rewrite only supports orientation, source-finding, review, comparison, or planning preparation, one source-slice to published-slice sentence or mini-card with the admissible use and visible omission or source-loss note is enough.

**Cheap stop before CSC.** If the rewrite is local, source-visible, non-reliance-bearing, and does not change admissible use, stay in `ConservativeRetextualization` without opening a `Controlled Semantic Coarsening` card.

**Work-planning boundary.** A rewritten method-selection note, work-planning note, or result-measurement note may improve readability and source-finding, but selected-method support, intended `U.WorkPlan`, actual `U.Work`, and work-result measurement remain governed by `A.15` plus the source `U.Episteme`, source `U.EpistemePublication`, or exact project-side FPF kind and reference for that work.

**Load-bearing use.** Open the fuller rewrite-support record only when the rewritten text will be externally relied on, disputed, cited as source support, used across context, or read as release/gate/work preparation, engineering justification, approval, or evidence support.

**Multi-source boundary.** A textual rendering over several source slices stays in this pattern only when every target claim can be recovered from either one already available same-described-entity source line or declared same-described-entity correspondence support. The rewrite may align wording, shorten, translate, filter, or foreground with visible loss notes; it may not add comparative claims, hypotheses, rankings, recommendations, bridge/substitution licence, causal linkage, or a new connective theory. Those claims leave `ConservativeRetextualization` for `E.17.ID.CR`, `B.5.2` or an abductive prompt, `A.6.4`, `F.9` or `F.9.1`, or `A.6.3.CSC` as applicable.

**Stop condition.** Stop once the rewrite changes no next reading, review, comparison, source-finding, or planning-preparation move and blocks no concrete overclaim about source support, omission, work, gate, approval, or evidence.

**Admissible-use examples.**

| Admissible project-side use | Source-finding or reversible probe | Non-admissible downstream use |
| --- | --- | --- |
| A summary or translation restates the same source claim with visible source slice, published slice, and omission/loss note. | A generated or manager-readable summary helps the team find/check the source before relying on an approval, evidence, gate, work, or engineering-justification claim. | A summary silently adds modality, reliability, approval, evidence, gate support, or work authority that the source slice does not carry. |


**Not this pattern when.** Not this pattern when the case is primarily explanatory rendering (`ExplanationFaithfulnessProfile`), representation-scheme change (`RepresentationTransduction`), changed described entity (`A.6.4`), or a deliberately coarsened rendering whose narrower admissible use, non-admissible downstream use, and source-bearing reopen card has become primary. In that last case, use `A.6.3.CSC Controlled Semantic Coarsening` instead of resolving it as ordinary `ConservativeRetextualization`.

### A.6.3.CR:1 - Problem frame

Teams constantly need a second textual form of the same episteme:
- an internal technical statement rewritten as an engineer-manager-readable report;
- a longer source note rewritten as a shorter working summary;
- a source-language statement rewritten into another natural language;
- a dense claim set rewritten as a filtered report that keeps only one declared slice.

These transforms are often treated as harmless editing. In practice they can quietly shift into hidden reinterpretation, hidden bridge work, hidden explanation, or even hidden retargeting. FPF already has `A.6.3` for same-described-entity conservative viewing. What is still needed is a focused named pattern that states when a textual rewrite remains only a conservative viewing case under `A.6.3`.

### A.6.3.CR:2 - Problem

Without a dedicated pattern for conservative textual re-expression:
1. report, summary, translation, and filtered rewrite cases are handled ad hoc;
2. authors treat textual simplification as if it were automatically conservative;
3. the boundary to explanation-facing renderings stays blurry;
4. correspondence-mediated rewrites are not distinguished from direct rewrites;
5. later reviewers cannot tell whether the result is still a view of the same described entity or a new interpretive publication.

### A.6.3.CR:3 - Forces

- **Same entity, different wording.** Readers need different textual forms without reopening the described entity.
- **Compression vs loss visibility.** Shorter or plainer forms are often useful, but omissions and source-loss modes must stay explicit.
- **Direct vs correspondence-mediated rewrites.** Some rewrites read from one source episteme; others depend on a declared `CorrespondenceModel`.
- **Textual focus vs family creep.** The pattern should cover same-entity textual re-expression, not explanation, not representation-wide shifts, and not retargeting.
- **Publication discipline.** Admissible MVPK faces and publication renderings still matter even when the transform looks like "just a rewrite."

### A.6.3.CR:4 - Solution — same-described-entity textual re-expression under `A.6.3`

#### A.6.3.CR:4.1 - Informal definition

> `ConservativeRetextualization` is a named pattern specialized under `A.6.3 U.EpistemicViewing` for textual re-expression of the same described entity.
>
> It preserves `describedEntityRef`, keeps the transform effect-free, and allows only claim-preserving or explicitly loss-declared rewriting of already available content.
>
> It may change register, ordering, textual density, language, emphasis, or local wording. It may not silently introduce new claims, new bridge licences, new work, evidence, gate, release, policy, assurance, or adjudication support, or a changed described entity.

#### A.6.3.CR:4.1.a - Pattern, case, and publication distinction

`ConservativeRetextualization` is an **intensional pattern** and a named specialization under `A.6.3`. Concrete same-described-entity rewrites are passive episteme cases or publication texts reviewed under this pattern; the pattern itself does not act, decide, or publish.

This distinction matters because the pattern governs **how** a rewrite is recognised, justified, and checked. It does **not** require every short report paragraph, summary line, or translation sentence to carry a giant standalone record.

#### A.6.3.CR:4.1.b - Local working vocabulary

This pattern repeatedly uses a small working vocabulary.
- **Source slice** = the already available pinned or otherwise reviewable textual content being restated.
- **Published slice** = the resulting textual rendering that remains under same-described-entity discipline.
- **Ordinary case** = a reviewable same-entity rewrite where source tether, omission notes, and handoff conditions stay readable without a heavyweight review record.
- **Load-bearing case** = a case where dispute, policy, assurance, required correspondence support, or cross-context reliance makes a fuller record worth publishing.

`sourceSlice` and `publishedSlice` are local review labels for the source textual slice and the resulting textual rendering in one rewrite case. A `publishedSlice` is not automatically a `U.EpistemePublication`; it becomes one only when the governing publication discipline instantiates it as such.

These terms are only local reading aids. They inherit the `E.17:5.1e` local-field rule: they do not create `U.Kind`, `SurfaceKind`, `RelationKind`, evidence kind, exact project-side FPF kind and reference, new governing pattern, new publication face, or a second semantic rule track.

#### A.6.3.CR:4.2 - Scope and exclusions

**In scope**
- same-described-entity report rewrite;
- same-described-entity summary;
- same-described-entity translation between natural-language textual forms;
- declared filtering or foregrounding of already-present claims in textual form.
- correspondence-supported textual synthesis where every target claim remains recoverable to one same-described-entity source line or declared same-described-entity correspondence support.

**Out of scope**
- any change of `describedEntityRef` or hidden change of described entity (`A.6.4`);
- explanation-facing renderings whose main purpose is explanatory rendering rather than same-entity rewrite (`ExplanationFaithfulnessProfile`);
- representation-regime changes such as text→table, text→diagram, or text→latent form (`RepresentationTransduction`);
- comparison, abductive-prompt, ranking, recommendation, bridge-mediated, substitution, or action-selection work that introduces new claims rather than restating available ones.


#### A.6.3.CR:4.2.a - Reader guidance

Use this pattern when the described entity stays fixed and the published result still remains textual.
- If the main change is explanatory, move to `ExplanationFaithfulnessProfile`.
- If the main change is a representation-scheme shift, move to `RepresentationTransduction`.
- If the described entity changes, move to `A.6.4`.

#### A.6.3.CR:4.2.b - What a reviewer checks first

A reviewer usually does not begin by filling every field name. The first useful questions are simpler:
1. Is the published result still about the same described entity?
2. Is the result still textual, or has it become explanation or representation change?
3. Can the reader see what was omitted, softened, or foregrounded?
4. If several source slices or correspondence support are doing work, can each target claim be traced to one same-described-entity source line or declared same-described-entity correspondence support?
5. Is the source only pointed at, or is it actually used and still admissible for the intended use?
6. If any answer is doubtful, is the handoff target explicit?

If omissions, softening, or filtering are admissible only because the published result is coarsened, tied to narrower admissible use, non-admissible for downstream use, and tied to source-bearing return, the case has crossed out of ordinary conservative retextualization even if the prose still looks like a summary. Use `A.6.3.CSC Controlled Semantic Coarsening` for that source-to-rendering relation.

Here, **source-bearing return** means returning to the source-bearing content, while **handoff** means the governing pattern has changed. A coarsened textual slice may need both.

Only after these questions are answered does a fuller load-bearing review record usually become worth writing.

#### A.6.3.CR:4.3 - Working-model first; explicit review record only when the case is load-bearing

Most same-described-entity textual rewrites should stay human-usable. This pattern therefore follows **E.14’s working-model-first discipline**: ordinary report, summary, or translation cases do not need a giant inline metadata block. What they do need is enough explicitness that a reviewer can still tell what stayed the same, what was omitted, and where the case would have to move to another governing pattern.

**Ordinary case (default).** For everyday same-described-entity rewrites, it is usually enough that the text or its surrounding publication keeps explicit:
- which source `U.Episteme` claims are being re-expressed;
- that `describedEntityRef` remains preserved;
- whether the case is direct or correspondence-mediated when that is not obvious;
- what omissions or source-loss modes matter for the reader;
- where the case exits if it has turned into explanation, representation shift, retargeting, or world/gate-bearing publication content.

**Explicit review record (only for load-bearing cases).** A fuller record is warranted when the case is assurance-facing, gate-adjacent, cross-context, correspondence-heavy, policy-bearing, or likely to be disputed. The record may inherit pattern ids and already-pinned metadata instead of restating them inline. When published, that record normally captures:
- transform placement (`patternPlacementRef = A.6.3 specialization`, `governingPatternRef`, `sourcePublicationOrRecordForm`, `targetPublicationOrRecordForm`, `changeTargetRef`);
- preservation context (`describedEntityPolicy = preserve`, `boundedContextPolicy`, `viewpointPolicy`, `referenceSchemePolicy`, `representationSchemePolicy`, `groundingPolicy`, `referencePlanePolicy`);
- claim and publication discipline (`claimPolicy`, `claimScopePolicy`, `publicationScopePolicy`, `reliabilityTransportPolicy`, `pinningPolicy`, `provenancePolicy`, `lossProfile`);
- continuity and bridge discipline (`claimContinuityClass`, `microtheoryContinuityClass`, `onticContinuityClass`, `bridgeRequirement`, `conservativityWitness`);
- downstream and admissibility discipline (`worldContactPolicy`, `evidencePolicy`, `gatePolicy`, `workCrossing`, `upstreamGoverningPatternRef`, `downstreamGoverningPatternRef`, `admissibleFaces`, `admissiblePublicationRenderings`, `compositionRule`, `reopenCondition`);
- naming and presentation discipline (`publicNamePolicy`).

The point of this record is not bureaucratic completion for every paragraph. It is to make **load-bearing** cases reviewable without hiding meaning in style, topic familiarity, or editor intuition.

#### A.6.3.CR:4.3.a - Ordinary admissibility defaults

Default admissibility for ordinary same-described-entity textual cases:
- primary admissible faces are `PlainView` and `TechCard`;
- bounded report-only use is admissible when source pins, provenance, loss notes, and same-described-entity conservativity remain visible;
- `InteropCard` use is admissible only when the governing publication-face source explicitly permits source-pinned, text-preserving export without added semantics;
- `AssuranceLane` or gate-bearing use is not default and requires governing publication-face policy plus source-pinned conservativity without hidden strengthening.

#### A.6.3.CR:4.4 - Direct and correspondence-mediated profiles

**Direct ConservativeRetextualization**
- source slice and published slice are textual re-expressions of one source episteme;
- no `CorrespondenceModelRef` is needed;
- the main required support is explicit loss/provenance discipline.

**CorrespondenceConservativeRetextualization**
- the target textual rendering is derived from a declared correspondence between epistemes or views of the same described entity;
- `CorrespondenceModelRef` is required;
- the result remains under `A.6.3` only if the correspondence supports same-described-entity conservativity and no new claims are imported beyond the declared witness set.

Cross-language translation is not automatically direct. If the translation depends on declared correspondence, reference-scheme mediation, or bounded equivalence notes, it must be treated as correspondence-mediated rather than disguised direct rewriting.

#### A.6.3.CR:4.4.a - Recurring same-entity textual moves

The pattern covers a small family of recurring textual moves as long as the same described entity remains explicit:
- **Register shift** — a technical statement is rewritten into plainer engineer-manager prose without changing what is being said about the same entity.
- **Summary or filtered restatement** — a source note is shortened or focused on one declared slice, with omissions stated rather than hidden.
- **Cross-language restatement** — the same source claim is restated in another natural language while the same source tether and same-entity line remain explicit.
- **Correspondence-supported textual synthesis** — one textual rendering is produced from declared same-entity correspondences without importing extra bridge or substitution support load.

These are recurring move shapes, not separate governing patterns. The specialization relation remains the same: same-described-entity textual re-expression under `A.6.3`.

#### A.6.3.CR:4.5 - Shared conservative retextualization rule bundle

##### A.6.3.CR:4.5.a. Preservation rule
A case under `ConservativeRetextualization` preserves the same described-entity line, the declared bounded context, and the already available claim-bearing source while changing wording, register, language, ordering, or density. It states what remains preserved about claim scope, publication scope, pins, provenance, grounding, and ontic scaffold, and it says whether the case is `Direct` or `Correspondence`.

##### A.6.3.CR:4.5.b. Loss and reliability rule
A reviewed case makes explicit what is omitted, shortened, foregrounded, or carried only through a declared source-loss mode by the rewrite. Reliability transport may remain source-bounded or be explicitly downgraded, but it must never be silently widened by cleaner prose, more forceful rhetoric, or management-facing polish.

##### A.6.3.CR:4.5.c. Authority and handoff rule
A case reviewed under this pattern stays same-entity and episteme. It does not govern explanation governance, bridge stance, retargeting, gate authority, or work enactment. If the rewrite becomes explanatory, bridge-bearing, gate-bearing, or world-facing, the case must hand off to the appropriate downstream governing pattern and say so explicitly.

##### A.6.3.CR:4.5.d. Composition and reopen rule
Repeated direct rewrite over the same source line may be idempotent, but heterogeneous rewrites and correspondence-mediated rewrites are generally order-sensitive. A reviewed case must reopen whenever correspondence support, source pins, provenance, admissible-face assumptions, or same-described-entity conservativity stop being explicit.

##### A.6.3.CR:4.5.e. Non-collapse note for correspondence
Correspondence-mediated retextualization does **not** by itself grant bridge licence, substitution licence, or comparative-reading licence. If the case needs those required supports, they must be declared separately rather than being smuggled in through correspondence language.

##### A.6.3.CR:4.5.f. Local conservativity witness for borderline textual cases
For borderline textual rewrites, a reviewer treats the case as no longer conservative under this pattern unless each point below remains visibly preserved or is explicitly loss-declared with the handoff target stated.
- **Modality and force.** A rewrite may not silently turn possibility, uncertainty, permission, obligation, recommendation, decision status, bounded scope, temporal window, or hypothesis language into a wider commitment.
- **Caveats and qualifications.** A rewrite may not quietly remove conditions, exception notes, uncertainty markers, or temporal qualifiers that still matter for reading the same source.
- **Reliability posture.** Cleaner prose, better ordering, or manager-facing polish may not silently raise confidence, warrant posture, or readiness for action.
- **Bridge and substitution support load.** Same-entity textual fluency may not import cross-context equivalence, substitution, or comparative-reading licence unless that support is declared elsewhere.
- **Alternative preservation.** A rewrite may not collapse open alternatives, rival hypotheses, or declared plurality into one apparently settled reading unless the loss is stated and still admissible under this pattern.

This witness is local to `ConservativeRetextualization`. It does not replace the broader conservativity invariants of `A.6.3`; it makes them inspectable for textual rewrites where fluent prose can otherwise hide strengthening.

### A.6.3.CR:5 - Archetypal Grounding

#### A.6.3.CR:5.1 - Same-described-entity report rewrite
**Source note slice.** `Service S exceeded the latency threshold in the evening batch window. Trace T-44 and dashboard pin D-17 show the spike. Two low-confidence hypotheses remain open.`

**Published report slice.** `Evening-batch latency for Service S exceeded the threshold. Source pins: Trace T-44, Dashboard D-17. Low-confidence hypotheses are omitted here and remain in the pinned source note.`

This is an admissible direct `ConservativeRetextualization` because the described entity stays fixed, the report remains textual, and the omission is stated rather than hidden. In ordinary internal use, this often needs only source pins plus visible omission notes rather than a full explicit review record.

#### A.6.3.CR:5.1.a - Ordinary inherited-pin summary
**Pinned source cluster.** `Incident note N-14, trace T-44, and dashboard card D-17 are already published together under one incident review bundle.`

**Published stand-up slice.** `Evening-batch latency again exceeded the threshold for Service S. See N-14 / T-44 / D-17 for the pinned source cluster.`

This is still an admissible ordinary case even though the short stand-up slice does not restate every pin and qualifier inline. The didactic point is that lightweight use may inherit already-published pins and provenance when the tether stays visible to the reader.

#### A.6.3.CR:5.1.b - Benign omission that stays ordinary
**Source note slice.** `Service S exceeded the latency threshold in the evening batch window. Trace T-44 and dashboard pin D-17 show the spike. The note also lists two low-confidence hypotheses for later investigation.`

**Published stand-up slice.** `Evening-batch latency for Service S exceeded the threshold. Source pins: T-44, D-17. Low-confidence hypotheses are omitted from this stand-up note and remain in the pinned source.`

This stays ordinary `ConservativeRetextualization` because the omission is declared, the same described entity remains visible, and no separate narrower admissible use, non-admissible downstream use, and source-bearing return card is doing the real work. Ordinary omission alone is not controlled semantic coarsening.

#### A.6.3.CR:5.1.c - Functional-description textual summary

**Source note slice.** `The principle scheme says: choose method family MF-2 for small-batch mixing when material X remains below threshold T; selected method M-2 still requires work plan WP-17 and result measurement RM-4.`

**Published summary slice.** `For small-batch material X below T, method M-2 is the selected method. Work plan WP-17 and result measurement RM-4 remain required.`

This remains `ConservativeRetextualization` because it is a textual restatement of the same source-episteme claims and it keeps the work-planning and result-measurement requirements visible. It supports reading and source-finding. It does not by itself provide performed `U.Work`, evidence, gate passage, engineering justification, or control architecture. If the summary drops the work-plan and result-measurement requirements or makes the selected method look executable by summary alone, treat the text as `A.6.3.CSC Controlled Semantic Coarsening` or recover the exact project-side FPF kind and reference that actually supports the requested use.

#### A.6.3.CR:5.1.d - Generated-summary source-support variant

A generated or machine-assisted summary may stay in `ConservativeRetextualization` only when it remains a same-described-entity textual re-expression and its source support is visible enough for the intended use. This is the ordinary LLM-generated-summary case: a model-produced paragraph over a pinned inspection note, method-selection note, safety note, incident note, or other source slice is not automatically `ExplanationFaithfulnessProfile` merely because it was generated; it remains `ConservativeRetextualization` only while it restates source claims and leaves omissions, loss, and non-admissible uses visible. Ordinary source-finding use can stay light; use the compact variant below when the summary will be reused, cited, disputed, or relied on.

| Source-support question | CR-local meaning |
| --- | --- |
| source pointer present | The summary points to the source slice or source bundle it claims to restate. |
| source actually used | The inspectable generation or rewrite path used that source, not merely a similar topic or remembered background. If the path is unavailable, keep the summary source-pointer-only or orientation-only until a source-use path is recovered. |
| claim supported | Each load-bearing summary claim can be recovered from the source slice or declared correspondence support. |
| claim merely plausible | A sentence sounds likely but is not recoverable from the source; it must stay orientation-only or leave CR. |
| omission/loss | Relevant omitted qualifiers, alternatives, caveats, uncertainty, or conditions are visible enough for the admissible use. |
| claim widening | The summary does not turn possibility, hypothesis, bounded scope, or low-confidence wording into a wider commitment. |
| added linkage | New causal, bridge, comparison, work, gate, evidence, or explanation links are not introduced as if they were in the source. |

When the generated-summary case needs the shared vocabulary rather than this CR-local question list, read the posture through `E.17:5.1b`: `source-pointer-only`, `source-available`, `source-retrieved`, `source-used`, `source-faithful`, `claim-supported`, `claim-unsupported`, `claim-contradicted`, `claim-plausible-only`, `source-omitted`, `source-loss-declared`, `claim-widened`, `added-linkage`, `independent-verification-present`, `admissible-for-this-use`, `downstream-use-forbidden`, and `reopen-trigger-present`.

The summary may expose or cite the source slice it restates. It does not become that source slice by fluency, brevity, translation, layout, generated form, or reuse. If the source slice or required exact project-side FPF kind and reference is missing, a repair request or source-gap note is only prospective; it does not retroactively make the earlier summary source-supported.

If the generated summary is source-pointer-only, merely plausible, claim-widened, or carrying added linkage, do not treat it as a conservative source-equivalent summary. Either keep it as source-finding/orientation, repair it against the source, or hand off to `A.6.3.CSC`, `ExplanationFaithfulnessProfile`, `RepresentationTransduction`, `E.17.ID.CR`, `A.15`, `A.10`, or another exact governing pattern according to the live claim.

#### A.6.3.CR:5.2 - Same-described-entity rewrite via declared correspondence


**Source design slice.** `Cooling loop CL-2 preserves safe temperature margins during standard load.`

**Source safety slice.** `Cooling loop CL-2 maintains the temperature condition required for hazard-control claim HC-7 during standard load.`

**Published joint-review slice.** `For standard load, Cooling loop CL-2 is described in both the design and safety views as maintaining the required temperature condition. This summary relies on CorrespondenceModel CM-12 and does not add claims beyond that declared overlap.`

The synthesis may stay in this pattern only if the source relation remains explicit, every target claim remains recoverable to the design slice, the safety slice, or the declared `CorrespondenceModel`, and the text does not silently widen claims beyond the declared same-described-entity overlap. Because correspondence support is load-bearing here, a load-bearing review record is usually warranted.

#### A.6.3.CR:5.2.b - Cross-language re-expression without hidden bridge work
**Source slice.** `The backup controller stays in passive watch mode until the primary loop fails two consecutive heartbeat checks.`

**Published slice.** `Резервный контроллер остаётся в режиме пассивного наблюдения, пока основной контур не пропустит две последовательные проверки heartbeat.`

This remains in `ConservativeRetextualization` only if the translation is still tethered to the same source claim, preserves the same described entity, and does not quietly add cross-tradition bridge claims such as "equivalent architecture role" or "same operational guarantee" beyond what the source actually states.

#### A.6.3.CR:5.2.c - Boundary to controlled coarsening
**Source slice.** `Vendor bulletin VB-7 requires rollback when pressure drift exceeds 2.5%, and it keeps two equipment-specific exceptions in the pinned annex.`

**Published coarsened slice.** `Pressure drift above 2.5% is a warning condition in the bulletin. Check the pinned bulletin and annex before treating the note as rollback guidance.`

This does **not** remain ordinary `ConservativeRetextualization`. The coarsened slice drops equipment-specific exceptions and remains only an orientation warning: it is not an executable rollback command. It can stay honest only through narrower admissible use, non-admissible downstream use, and source-bearing return to the source-bearing bulletin. Once that narrower-use card becomes primary, the case leaves ordinary same-entity rewrite and must use `A.6.3.CSC Controlled Semantic Coarsening` rather than being treated as a harmless summary.

#### A.6.3.CR:5.3 - Boundary to explanation-facing renderings

A text is rewritten not mainly to restate the same source, but to explain why it matters, simplify reasoning for a learner, or narrate a mechanism. That move should leave `ConservativeRetextualization` and be reviewed under `ExplanationFaithfulnessProfile`.

#### A.6.3.CR:5.4 - Boundary to representation transduction
A prose note is rewritten as a table, matrix, diagram, or latent/distributed representation. Even if the described entity stays fixed, this is not only a textual rewrite; it belongs with `RepresentationTransduction`.

### A.6.3.CR:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto/Epist**, **Prag**, **Did**.
This pattern intentionally biases toward same-entity conservativity and away from explanation or retargeting inflation. The main mitigation is explicit handoff discipline to `ExplanationFaithfulnessProfile`, `RepresentationTransduction`, `A.6.4`, and later downstream governing patterns when the same-entity textual reading stops being honest.

### A.6.3.CR:7 - Conformance Checklist

1. **CC-CR-1 — Same described entity remains explicit.**
   The case preserves `describedEntityRef` without special pleading.
2. **CC-CR-2 — Textual re-expression remains the right family.**
   The result stays a textual re-expression rather than explanation or representation shift.
3. **CC-CR-3 — Loss, provenance, pinning, and reliability are explicit or inherited by pinned reference.**
   The case states these explicitly or inherits them through already-pinned content that remains visible to review.
4. **CC-CR-4 — Direct vs correspondence split is explicit.**
   The direct-vs-correspondence split is explicit and justified.
5. **CC-CR-5 — Correspondence support is named where needed.**
   If correspondence-mediated, `CorrespondenceModelRef` is declared.
6. **CC-CR-6 — Local conservativity witness remains satisfied.**
   The reviewed case does not silently widen modality, remove caveats, raise reliability posture, import bridge or substitution licence, or collapse declared alternatives beyond stated loss notes.
7. **CC-CR-7 — Handoff path is explicit on failure.**
   If the case fails any of the checks above, the handoff target is explicit (`ExplanationFaithfulnessProfile`, `RepresentationTransduction`, `A.6.4`, `B.5.2`, or another governing pattern).
8. **CC-CR-8 — Working-model first remains intact.**
   Ordinary same-entity rewrites stay lightweight; fuller explicit review records are reserved for load-bearing cases.

### A.6.3.CR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it is wrong | How to avoid it |
|---|---|---|
| Treating every summary as automatically conservative | summary demand hides omission and claim shift | publish loss/provenance discipline explicitly |
| Hiding correspondence in plain paraphrase | required correspondence support disappears into prose | declare `CorrespondenceModelRef` when needed |
| Letting a rewrite become explanation | explanation work quietly becomes a textual “rewrite” | move to explanation governance once didactic/explanatory work dominates |
| Letting `describedEntityRef` shift by topic similarity | same topic is not the same described entity | exit to `A.6.4` if `DescribedEntityRef` changes |

### A.6.3.CR:9 - Consequences

- Textual same-entity rewrites get an admissible place without inventing a new heavy governing pattern.
- Direct and correspondence-mediated variants stay visibly separated.
- Loss, provenance, and reliability transport become explicit instead of implicit editorial judgement.
- Ordinary working-model use stays lightweight, while load-bearing cases get a load-bearing review record when risk warrants it.
- The pattern remains safely bounded by `A.6.3`, `A.6.4`, explanation-facing work, and representation-shift work.

### A.6.3.CR:10 - Rationale

This pattern is worth splitting out because same-entity textual re-expression is common, useful, and safer than many neighboring transform families when it stays explicitly conservative. Keeping it under `A.6.3` as a named specialization preserves governing-pattern boundary while making a recurring authoring move easier to review, while still respecting E.14’s working-model-first discipline for ordinary cases.

### A.6.3.CR:11 - SoTA Alignment: Adopted/Adapted Invariants And Rejected Shortcuts

**SoTA alignment rule.** Read each row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and Relations of this pattern.

**Traditions covered.** This pattern binds itself to architecture-description governance, summarization factuality, translation-quality governance, and plain-language rewrite practice.

| Claim need | Source idea and current source | Current source reference | Local FPF invariant and practical local test | Adopted invariant, adapted invariant, and rejected shortcut |
|---|---|---|---|---|
| Conservative rewrite must stay visibly tied to the same described content rather than shifting through presentation fluency. | Architecture-description practice separates source publication, view, viewpoint, and required correspondence support instead of letting rendered prose silently change the described entity. | ISO/IEC/IEEE 42010:2022; source maturity = mature standard | `A.6.3.CR` keeps same-described-entity textual restatement under `A.6.3`, requires explicit handoff when `describedEntityRef` changes, and keeps bridge support load out of fluent rewrite. | **Adopt.** |
| Summary-like rewriting is not automatically harmless; factuality and faithfulness need source-sensitive checking. | Modern summarization work treats unsupported compression, strengthening, and hallucinated linkage as core failure modes rather than editorial noise. | Maynez et al. (2020), *On Faithfulness and Factuality in Abstractive Summarization*; source maturity = research paper supporting evaluation posture | `A.6.3.CR` adopts that stance and adapts it to FPF by making omission, reliability posture, and same-entity bounds explicit review concerns. | **Adopt/Adapt.** |
| Translation quality is governed through declared quality aspects such as accuracy, omission, and addition rather than by fluency alone. | Translation-quality governance separates adequacy from text smoothness and requires explicit treatment of omission/addition error classes. | W3C Multidimensional Quality Metrics (MQM) Community Group / MQM issue-type framework: ongoing framework and community practice, with stable issue-type work and current attention to human, machine, and generative-AI translation quality evaluation. | `A.6.3.CR` adapts this by treating correspondence-mediated and cross-language rewrites as admissible only when loss, provenance, and same-entity bounds stay explicit. | **Adapt; source maturity = ongoing framework/community practice.** |
| Plain-language rewrite may improve readability, but it must not silently change commitments, scope, or force. | Plain-language standards favour reader-oriented rewriting while preserving the original commitments and conditions that matter for use. | ISO 24495-1:2023; source maturity = mature standard | `A.6.3.CR` adopts reader-oriented simplification for ordinary cases and rejects the popular shortcut that “plainer text” alone proves conservativity. | **Adopt/Reject-popular-shortcut.** |

**Architecture-description governance.** `A.6.3.CR` adopts the discipline that rendered text must stay visibly tied to a declared source publication or `U.View` line. It therefore rejects same-topic textual polish as sufficient evidence of same-described-entity conservativity.

**Summarization factuality.** `A.6.3.CR` adapts modern factuality concerns into a local conservativity witness: source pointer, source actually used, claim support, contradiction, plausible-but-unsupported claim, omission, declared source-loss mode, claim widening, added linkage, independent verification, admissible use, forbidden downstream use, and reopen trigger are treated as reviewable support distinctions, not as style noise. The shared source-support vocabulary is `E.17:5.1b`; the shared use-boundary terms are `E.17:5.1c`; the primary-boundary chooser is `E.17:5.1d`. This pattern uses them only for same-described-entity textual restatement.

**Translation and plain-language traditions.** `A.6.3.CR` adopts the reader-oriented value of translation and plain rewrite, but rejects the still-popular habit of treating cross-language or plain-language textual fluency as automatic proof that no new claim has been introduced. The W3C MQM source is used for issue-type and evaluation discipline, not as a brand-level warrant that a translated or rewritten sentence is source-equivalent.

**Local stance.** Best-known current practice supports a narrow rule: same-described-entity textual restatement is admissible only when source tether, loss, provenance, and same-entity bounds remain explicit enough that the reader can still tell what was preserved, what was omitted, and when another governing pattern must be applied.

### A.6.3.CR:12 - Relations

- **Builds on:** `A.6.3`, `A.6.2`, `A.7`, `E.10.D2`, `E.17.0`, `E.17`, `F.9`, `F.18`, `E.10`
- **Coordinates with:** `ExplanationFaithfulnessProfile`, `RepresentationTransduction`, `E.17.ID.CR ComparativeReading`, `A.6.4`, `B.5.2`, `A.15`
- **Impact radius:** primary touch `A.6.3`; secondary review support `E.17.0`, `E.17`, `F.9`; failed conservativity cases apply `A.6.4`, `B.5.2`, or `A.15`
- **Boundary notes:** explanation-facing cases apply `ExplanationFaithfulnessProfile`; representation-regime shifts apply `RepresentationTransduction`; bounded comparative review cases apply `E.17.ID.CR ComparativeReading`; described-entity changes apply `A.6.4`.

### A.6.3.CR:End
## A.6.3.RT - RepresentationTransduction — same-described-entity representation-scheme transition
> **Status:** Stable

**Placement.** Specialization under `A.6.3 U.EpistemicViewing` for same-described-entity representation-scheme transition.
**Builds on.** `A.6.3 U.EpistemicViewing`; `A.6.2 U.EffectFreeEpistemicMorphing`; `A.7`; `E.10.D2`; `C.2.7`; `E.17.0`; `E.17`; `F.9`; `F.18`.
**Coordinates with.** `ConservativeRetextualization`; `A.6.3.CSC Controlled Semantic Coarsening`; `ExplanationFaithfulnessProfile`; `E.17.ID.CR ComparativeReading`; `A.6.4 U.EpistemicRetargeting`; `F.9`; `F.9.1`; `E.18`; `A.15`; `A.10`; `B.3`; `B.5.2`; `A.20`; `A.21`; `C.27`; `A.3.3`; explicit decoding-access review.
**Name boundary.** In this pattern, `RepresentationTransduction` names an `A.6.3 U.EpistemicViewing` specialization for a same-described-entity transition across declared representation schemes or reasoning media. It is not an `E.18` Transduction Graph Architecture node, not a TGA graph edge, not an `A.15` method description, work-plan, or work-occurrence claim, and not a changed-function or control-architecture claim.

**One-line summary.** `RepresentationTransduction` is a same-described-entity shift in representation scheme that stays inside `A.6.3 U.EpistemicViewing`: it may move between prose, table, diagram, structured notation, or another declared representation regime, but it does **not** silently change `describedEntityRef`, promote geometry or notation into ontology-by-default, or hide decode-mediated recoverability behind rendering fluency.

**Governed object in plain terms.** One published rendering of the same described entity in a different representation scheme or reasoning medium; not the whole source corpus, not a new ontology, and not carrier-operation work.
**Governing move in plain terms.** Change representation scheme while keeping same-described-entity support reviewable, factor deltas visible, and handoff explicit when the case has become explanation, retargeting, bridge work, or a narrower-use card.

**Use this when.** Use this pattern when the same described entity needs to move across representation schemes or reasoning media such as prose, table, diagram, or structured notation, and the real job is still the representation shift rather than explanation, retargeting, or downstream action.

**Start here when.** Your first honest publication unit already changes representation scheme or reasoning medium, and the main review question is whether the target stays source-tethered and same-described-entity rather than becoming a new ontology, a hidden bridge, or a coarsened proxy.

**What goes wrong if missed.** A table, diagram, or notation shift gets treated as harmless formatting even after it has started hiding recoverability loss, silent described-entity or ontology shift, decode work, or a separate narrower-use card.

**What this buys.** One honest same-described-entity representation shift with visible source tether, visible factor and reasoning-medium change, and an explicit handoff when the case stops being ordinary representation transduction.

**Working action spine.** Same described entity appears in a new representation scheme -> separate source described entity, receiving described entity, preserved claim, representation scheme, reasoning medium, and admissible use -> use the rendering for inspection, source-finding, comparison, technical review, or reversible planning preparation -> output the ordinary use path or the fuller continuity-witness decision block when ambiguity, dispute, citation, reliance, bridge, work, gate, assurance, decode-mediated access, abductive reopen, temporal/dynamics, release, or TGA-path use is live -> hand off if work, evidence, gate, explanation, retargeting, bridge, carrier, coarsened-rendering, abductive, temporal, dynamics, or TGA claim appears.

**Ordinary use.** If the publication-facing item only supports inspection, source-finding, comparison, or planning preparation, keep the explicit reading to the source described entity, receiving described entity, preserved claim, representation-scheme change, and admissible and non-admissible use.

**Ordinary use path.**
1. What source described entity and receiving described entity are being compared, and is preservation explicit?
2. Which source claim or commitment remains preserved for the intended use?
3. What representation scheme, reasoning medium, or expression form changed?
4. What reader action remains admissible, and what downstream use is not admissible from this representation shift alone?

**Action/work boundary.** A representation shift may support method inspection or work-planning preparation, but the source for intended or actual work remains `A.15` plus the source `U.Episteme`, source `U.EpistemePublication`, or exact project-side FPF kind and reference that governs that work claim.

**Load-bearing use.** Open the fuller continuity-witness decision block only when the shifted representation will be externally relied on, disputed, cited as support, used across context, treated as gate/release/work preparation support, carried through a decode-mediated or latent access path, used in abductive reopen, or used for temporal/dynamics or TGA-path currentness.

**Representation-validity grounding.** Recoverability is recoverability for one declared admissible use, not a general property of the target representation. A diagram, table, notation, decoded output, or model-state rendering may be recoverable enough for inspection or technical review when target relations trace back to source anchors and loss notes, while still being insufficient for work-planning reliance, gate reliance, release reliance, evidence reliance, assurance reliance, or engineering justification. For any such reliance use, this pattern supplies only same-entity correspondence support; the operative support must come from the governing FPF pattern and exact project-side FPF kind and reference named by `A.15`, `A.10`, `A.20`, `A.21`, `B.3`, `E.17.EFP`, `E.17.ID.CR`, `F.9`, or `F.9.1` as applicable. When the shifted representation will carry load-bearing use, state the support path that makes that exact use admissible: source tether, recoverability target, decode path where needed, evidence class, any probe or intervention support claimed, and the `E.17:5.1b` source-support posture when source pointer, source availability, source retrieval, source use, source faithfulness, claim support, contradiction, omission, claim widening, or reopen trigger could diverge. Use `E.17:5.1c` for the shared use-boundary meanings of `orientation use`, `reliance use`, `operative claim`, `unsupported downstream use`, and `reopen trigger`; use `E.17:5.1d` when the primary live question may belong to ordinary textual restatement, coarsening, explanation, comparison, bridge work, substitution, work, reliance, gate, evidence, assurance, retargeting, or carrier and front-end work.

A table, diagram, notation, decoded output, or model-state rendering may expose or cite its source support. It does not become that source support, architecture, ontology, evidence, gate, or work source by visual clarity, geometry, notation, proximity, or reuse. If the needed support path is missing, a repair request, source-gap note, or evidence-work plan is prospective only; it does not retroactively make the earlier representation shift supported.


**Stop condition.** Stop once the representation shift changes no next inspection, comparison, source-finding, or planning-preparation move and blocks no concrete overclaim about the represented entity, source support, work, gate, or evidence.

**Admissible-use examples.**

| Admissible project-side use | Source-finding or reversible probe | Non-admissible downstream use |
| --- | --- | --- |
| A table or diagram makes the same described entity easier to inspect while the source tether and representation-scheme change stay visible. | A diagram helps reversible planning or source inspection while the team checks recoverability, source anchors, or decode path before gate, work, evidence, or justification use. | A diagram, geometry, table, or notation is treated as architecture, ontology, evidence, gate passage, work authority, or engineering justification by visual form alone. |


**Not this pattern when.** Not this pattern when only wording changes (`ConservativeRetextualization`), explanation becomes primary (`ExplanationFaithfulnessProfile`), the described entity changes (`A.6.4`), or the target stays honest only by carrying its own narrower admissible use, non-admissible downstream use, declared source-loss mode, and source-bearing reopen card. In that last case, use `A.6.3.CSC Controlled Semantic Coarsening` instead of resolving it as ordinary `RepresentationTransduction`.

### A.6.3.RT:1 - Problem frame

The same described entity often needs to be carried across more than one representation regime:
- prose into a table that makes comparison or coverage clearer;
- a table into a diagram that foregrounds dependency or topology;
- a diagram into a structured notation suitable for replay or technical review;
- a source representation into another regime that changes reasoning possibilities without changing the underlying described entity.

In practice these shifts are often treated as harmless reformatting. But some representation changes alter reasoning possibilities, reduce recoverability, or quietly change what appears to be present in the source. FPF already has `A.6.3` for same-described-entity conservative viewing. This pattern names the recurring same-described-entity case where the published result changes representation scheme while the case still remains inside `A.6.3`.

### A.6.3.RT:2 - Problem

Without a dedicated named pattern for representation-scheme transitions:
1. teams treat text-to-table, table-to-diagram, and notation shifts as if they were all the same kind of harmless rewrite;
2. changes in reasoning medium and recoverability remain implicit;
3. latent/distributed cases tempt readers to treat geometry or feature clusters as ontology-by-default;
4. reviewers cannot tell when a case is still same-entity viewing and when it has become retargeting, explanation, carrier work, or decode-mediated reconstruction;
5. representation factors governed near `C.2.7` are discussed rhetorically rather than as explicit deltas.

### A.6.3.RT:3 - Forces

- **Same entity, different reasoning medium.** Teams need different representational forms without silently changing the described entity.
- **Legibility vs recoverability.** A clearer representation is useful only if readers can still recover how it relates to source claims, anchors, and pins.
- **Representation change vs described-entity shift.** A new notation or geometry can make structure more visible, but it must not silently become a new described entity or a new ontology.
- **Recoverability before decode ambition.** Start from cases where recoverability can be reviewed directly before leaning on decode-mediated reconstruction.
- **Governing-pattern restraint.** This pattern must stay under `A.6.3`, not swallow explanation governance, retargeting, bridge work, or carrier work.

### A.6.3.RT:4 - Solution — same-described-entity representation-scheme transition under `A.6.3`

#### A.6.3.RT:4.1 - Informal definition

> `RepresentationTransduction` is a named pattern specialized under `A.6.3 U.EpistemicViewing` for same-described-entity transitions across declared representation schemes.
>
> It preserves `describedEntityRef`, keeps the transform effect-free, and makes explicit what changes in representation factors, reasoning medium, recoverability, and loss profile.
>
> It may move between prose, table, diagram, structured notation, or another declared representation regime. It may not silently change the described entity, silently import bridge semantics, or treat decode-mediated structure as if it were directly given.

#### A.6.3.RT:4.1.a - Pattern, case, and published rendering distinction

`RepresentationTransduction` is an **intensional pattern** and a named specialization under `A.6.3`. Concrete same-described-entity representation changes are passive episteme cases or published renderings reviewed under this pattern; the pattern itself does not act, decide, or publish.

This distinction matters because the pattern governs **how** a representation change is recognised, justified, and checked. It does **not** turn every table, diagram, or structured notation into a giant standalone review artifact, and it does not reduce review to a mechanical reformatting step.

#### A.6.3.RT:4.1.b - Local working vocabulary

Use this vocabulary only after the ordinary use path leaves a live ambiguity or a load-bearing relation-change question. Ordinary text-to-table, table-to-diagram, or diagram-to-notation cases do not need every term below; use only the term that changes the next representation decision or blocks a concrete overclaim.
- **Representation scheme** = the published form in which the same entity is rendered (for example prose, table, diagram, or structured notation).
- **Reasoning medium** = the form-specific inspection possibilities readers actually use when inspecting the published rendering.
- **Semiotic mode** = what kind of meaning-bearing support is doing the main work in the rendering, such as structural likeness, trace/index, conventional code, model-mediated correspondence, or decode-mediated recoverability.
- **Factor delta** = the explicit change in representation factors that matters for review.
- **Source tether** = the visible link back to pinned or otherwise reviewable source `U.Episteme` claim graph that keeps same-entity support honest.
- **Decode-mediated case** = a case where explicit access to the target representation depends on a declared decoding path rather than direct reading from an already published source episteme or source publication.
- **actionabilityShift** = a changed reader action-possibility reading or apparent readiness created by the rendering. It is not execution authority, gate status, action invitation, work authority, or proof that work may proceed.
- **recoverabilityEvidenceClass** = a local review field naming the recoverability evidence support needed for decode-mediated or latent cases. It is not an `EvidenceKind`, and it is not required for ordinary non-latent representation shifts unless recoverability is part of the live question.
- **representationValiditySupportPosture** = a local support-posture value used only when the representation shift is disputed, assurance-facing, gate-adjacent, externally relied on, decode-mediated, or likely to invite gate, evidence, work, or authority use beyond declared support. It says what the shifted representation may support now; it is not a score, ordered rank, improvement scale, ontology class, evidence class, or `authoritySourceRef` target.
- **sourceSupportPosture** = the shared `E.17:5.1b` vocabulary used beside representation-validity posture when the source relation itself is disputed or load-bearing: pointer-only, available, retrieved, used, faithful, claim-supported, claim-unsupported, claim-contradicted, claim-plausible-only, source-omitted, source-loss-declared, claim-widened, added-linkage, independent-verification-present, admissible-for-this-use, downstream-use-forbidden, or reopen-trigger-present.

| representationValiditySupportPosture | What it supports | Required support | Shortcut rejected |
| --- | --- | --- | --- |
| `readability-only` | Inspection, discussion, source-finding, or planning preparation. | Source tether and non-admissible downstream-use line. | Clearer rendering means a wider claim. |
| `source-recoverable` | The reader can trace target relations back to source anchors. | Source anchors, loss/provenance note, and recoverability statement. | Target form replaces source support. |
| `structure-preserving` | Technical review of preserved relation structure. | Declared relation structure, preservation witness, and no-new-claim check. | Diagram/topology defines ontology by form. |
| `decode-supported` | Bounded decode-mediated report or review. | Decode path, `recoverabilityEvidenceClass`, and recoverability target. | Readable decode output is direct givenness. |
| `probe/intervention-supported` | Bounded representation-to-property or representation-to-behavior claim. | Probe evidence, intervention evidence, or causal-abstraction support that names the exact admissible use. | Probe confidence or intervention success becomes general ontology. |
| `bridge-supported-source-equivalence` | Equivalence, substitution, or bridge use only where another governing pattern supplies it. | Existing bridge, equivalence, or substitution support outside RT, with the governing pattern named. | RT itself grants source equivalence or substitution. |


**Recoverability-for-use rule.** If the declared admissible use is inspection, source-finding, comparison, or technical review, `RepresentationTransduction` can close with same-described-entity preservation, source tether, representation-scheme delta, and loss/recoverability notes. If the declared admissible use is work-planning preparation, this pattern supports only reversible preparation until `A.15` supplies the role, method, plan, and work source relation. If the declared admissible use is evidence or currentness, gate or release, assurance, commitment, bridge or substitution, or engineering justification, the case must name the downstream governing source relation; otherwise the target representation remains orientation or review support only.

These terms are local review aids. They inherit the `E.17:5.1e` local-field rule: they do not create `U.Kind`, `SurfaceKind`, `RelationKind`, `KindBridge`, `MechanismKind`, `EvidenceKind`, exact project-side FPF kind and reference, new face family, or new ontology governing pattern.

#### A.6.3.RT:4.2 - Scope and exclusions

**In scope**
- text-to-table shift over the same described entity;
- table-to-diagram shift over the same described entity;
- diagram-to-structured-notation shift where the represented entity and claim-bearing source episteme stay preserved;
- functional-description diagrams, tables, screens, or notations when the same described entity remains fixed and the main change is representation scheme or reasoning medium;
- other same-entity representation-scheme changes with explicit recoverability discipline.

**Out of scope**
- any change of `describedEntityRef` or hidden change of described entity (`A.6.4`);
- explanation-facing renderings whose main purpose is didactic or explanatory rendering work (`ExplanationFaithfulnessProfile`);
- purely textual rewrites that stay inside one representation regime (`ConservativeRetextualization`);
- carrier work such as rendering, export, upload, serialization, or OCR/parsing-like extraction;
- latent/distributed use without pinned source claim or publication, decode path or access route, recoverability evidence, admissible use-support value, and remaining reader action.


#### A.6.3.RT:4.2.a - Reader guidance

Use this pattern when the described entity stays fixed but the published result changes representation scheme or reasoning medium.
- If only wording changes, stay in `ConservativeRetextualization`.
- If the target mainly teaches, narrates, or explains, move to `ExplanationFaithfulnessProfile`.
- If same-entity support fails, move to `A.6.4`.
- Stay here when changed representation scheme or reasoning medium remains the primary review question, even if some loss is present.
- If the target stays honest only by carrying its own narrower-use card, declared source-loss mode, non-admissible downstream-use line, and source-bearing reopen, move to `A.6.3.CSC Controlled Semantic Coarsening`; do not keep the case here as ordinary representation transduction.
#### A.6.3.RT:4.2.b - What a reviewer checks first

A reviewer usually starts with five questions:
1. Is the described entity still the same, or has the described entity shifted?
2. What changed in representation scheme and reasoning medium?
3. Can the target still be tethered back to a pinned source episteme or source publication with enough specificity for the declared admissible use?
4. Has the case quietly become explanation, bridge-bearing comparison, retargeting, or carrier work?
5. If decoding is involved, is the evidence class adequate for the declared admissible use rather than only for readable review?

If the representation shift is no longer the main review problem, and the target instead stays honest only by carrying a narrower-use card with non-admissible downstream use and reopen duty, the case has crossed out of ordinary representation transduction even if the new form still looks like a neat table, diagram, or notation. Use `A.6.3.CSC Controlled Semantic Coarsening` for that source-to-rendering relation.

Here, **reopen** means return to the source-bearing content, while **handoff** means the governing pattern has changed. A coarsened representation may need both.

Only after these questions are answered clearly does a fuller load-bearing decision block normally become necessary.

#### A.6.3.RT:4.3 - Working-model first; explicit decision block only when the case is load-bearing

Most same-described-entity representation shifts stay human-usable and reviewable without turning every table, diagram, or structured rendering into a giant metadata block. This pattern therefore follows **E.14's working-model-first discipline**: ordinary non-latent cases need enough explicitness to show what stayed the same, what changed in representation and reasoning medium, what was lost or foregrounded, and where the case would have to move to another governing pattern.

**Ordinary case (default).** For everyday same-described-entity representation shifts, it is usually enough that the rendering or its surrounding publication keeps explicit:
- the source described entity and the receiving described entity, or the statement that the receiving item preserves the source described entity;
- the source `U.Episteme` claim or commitment preserved for the intended use;
- the representation scheme, reasoning medium, or expression-form delta;
- the remaining admissible reader action and the downstream use not made admissible by this representation shift.

That ordinary path is the default. It supports inspection, source-finding, comparison, technical review, or reversible planning preparation. It does not by itself support work authority, evidence force, gate passage, assurance force, bridge substitution, abductive selection, temporal/dynamics currentness, or TGA-path currentness.

**Fuller continuity-witness decision block (only for load-bearing cases).** A fuller block is warranted when the case is disputed, externally relied on, cross-context, correspondence-heavy, decode-mediated, assurance-facing, gate-adjacent, work-pressure, abductive-reopen, temporal/dynamics, or TGA-path-bearing. The block may inherit pattern ids and already-pinned metadata instead of restating them inline. When published, it makes these decision-block fields recoverable:

| Field | Required reading in this pattern |
| --- | --- |
| `sourceEpistemeOrPublication` | The source `U.Episteme`, `U.EpistemePublication`, episteme-lane `U.View`, or exact source publication being transformed or cited. |
| `receivingEpistemeOrPublication` | The receiving episteme, publication, view, diagram, table, functional description, explanation, decoded rendering, or TGA-facing publication item. |
| `sourceDescribedEntity` | The described entity before the representation shift. |
| `receivingDescribedEntity` | The described entity after the shift, or the statement that the source described entity is preserved. |
| `groundingAndContext` | Grounding holon, bounded context, reference plane, and reference scheme as far as the intended use needs. |
| `claimOrCommitmentUnderTest` | The claim, invariant, commitment, relation, or project-side use whose continuity is being judged. |
| `viewpointAndView` | The viewpoint and view used to read the source and receiving material when they affect the claim. |
| `representationSchemeDelta` | The representation scheme, reasoning medium, representation factor, or inference-regime change that matters for review. |
| `preservedCommitments` | What the receiving item still carries from the source. |
| `withdrawnOrNewCommitments` | What the receiving item drops, narrows, adds, widens, or changes. |
| `supportPosture` | The source-support or representation-validity support posture for the exact intended use. |
| `continuityWitness` | The reason the same-described-entity reading is still supportable. |
| `counterWitness` | Any fact that weakens same-described-entity support, such as changed entity, changed predicate, changed frame, missing source tether, or unsupported decode path. |
| `lossAndRecoverability` | Preserved distinctions, lost distinctions, recoverability target, recoverability evidence, and source-bearing reopen condition. |
| `admissibleUse` | The exact use that remains admissible now. |
| `nonAdmissibleUse` | The downstream work, evidence, gate, assurance, bridge, decision, abductive, TGA-path, temporal, or dynamics use that is not carried by the current item. |
| `neighboringPatternHandoff` | The FPF pattern that carries the live neighboring claim, when one is live. |
| `remainingAdmissibleReaderAction` | One short plain line saying what the reader may now do or which neighboring pattern now carries the live claim. |

The decision block is not a new FPF kind, record, profile, publication form, or hidden support object. It is a recoverable field set for the representation-transition case.

#### A.6.3.RT:4.3.a - Working admissibility defaults

By default in this pattern:
- primary admissible faces for non-latent cases are `PlainView` and `TechCard`;
- bounded report-only use is admissible when source pins, provenance, loss notes, and same-described-entity support remain visible, and when the target is not relying on one separate narrower-use card to remain honest;
- `InteropCard` use is admissible only when the governing publication-face source explicitly permits source-pinned, structure-preserving export without added semantics;
- `AssuranceLane` or gate-bearing use is not default and requires governing publication-face policy plus source-pinned same-entity support;
- latent/distributed variants remain bounded until explicit recoverability evidence and decode-path discipline are published.

#### A.6.3.RT:4.4 - Direct and correspondence-mediated profiles

**Direct RepresentationTransduction**
- source representation and target representation are representation-scheme variants over one same-described-entity source line;
- no `CorrespondenceModelRef` is required;
- the main required support is explicit factor delta, reasoning-medium delta, and recoverability discipline.

**CorrespondenceRepresentationTransduction**
- the target representation is derived through a declared correspondence between epistemes or views of the same described entity;
- `CorrespondenceModelRef` is required;
- the result remains under `A.6.3` only if same-entity conservativity is still supportable and the correspondence does not silently import extra claims.

Correspondence-mediated representation work does **not** by itself grant bridge licence, substitution licence, or comparative-reading licence. If the case needs those required supports, they must be declared separately rather than hidden inside representation language.

#### A.6.3.RT:4.4.a - Recurring same-entity representation moves

Recurring same-entity moves under this pattern include:
- **Tabulation** — prose or dispersed claims are rendered into a table that exposes comparison or coverage more clearly.
- **Diagramming** — a table or prose relation set is rendered into a diagram that foregrounds structure while remaining source-tethered.
- **Structured notation shift** — prose, table, or diagram content is rendered into a notation better suited for disciplined replay or technical inspection.
- **Correspondence-supported representation shift** — the target representation depends on declared same-entity correspondence support without thereby becoming a bridge case.

These are recurring move shapes under one specialization relation. They are not separate governing patterns and they do not override `E.17` face discipline.

#### A.6.3.RT:4.4.b - How a reviewer reads representation-factor and reasoning-medium change
A reviewer can say, in one short paragraph, what changed in representational shape, what changed in reasoning medium, and whether the primary change is also a `semioticModeShift` rather than only a scheme change. Typical read-outs are: "the table foregrounds comparability across rows", "the diagram foregrounds dependency shape", or "the notation foregrounds explicit argument positions."

When the case is more demanding, that paragraph also names whether salience, topology, actionability, admissible-use reading, calibration, or interactivity materially changed. If those shifts cannot be stated without slipping into new ontology, hidden bridge work, or a changed described entity, the case is not yet ready to stay here. Use the representation-delta review crib sheet and the current semiotic-mode support note when the deltas need a more normalized read-out.

#### A.6.3.RT:4.5 - Shared representation rule bundle

##### A.6.3.RT:4.5.a. Preservation rule
`RepresentationTransduction` preserves the same described-entity line, bounded context, and declared claim-bearing source while changing the representation scheme and, often, the reasoning medium. It must state what remains preserved about the ontic scaffold, claim scope, publication scope, pins, provenance, and grounding. It must also state whether the case remains direct or correspondence-mediated.

##### A.6.3.RT:4.5.a.1. Local conservativity witness
For this pattern, a new intensional claim is introduced when the target rendering:
- upgrades a source-visible relation into relation theory or dependency semantics not present in the source;
- turns geometry, notation, embedding proximity, or decoder output into ontology-by-default;
- adds bridge, substitution, comparative-reading, or mechanism claims not already licensed by the source line or declared correspondence;
- collapses source alternatives, uncertainty, or bounded scope into one wider commitment;
- or treats decode-mediated recoverability as if it were direct givenness.

Conservativity is approximated here by checking, together, `describedEntityPolicy = preserve`, source-tether posture, factor delta, reasoning-medium delta, loss profile, ontic scaffold preservation, and whether each target-side connective can be pointed back to pinned source `U.Episteme` claim graph or declared same-entity correspondence support.

##### A.6.3.RT:4.5.b. Loss and reliability rule
A reviewed case under this pattern makes explicit which distinctions, inspection possibilities, or local cues are lost, foregrounded, or rearranged by the shift in representation regime. Reliability transport may remain source-bounded or be explicitly downgraded, but it must never be silently widened just because the target form looks clearer, more structured, or more formal.

##### A.6.3.RT:4.5.c. Authority and handoff rule
A case reviewed under this pattern stays same-entity and episteme-facing. It does not govern retargeting, bridge stance, explanation governance, executable docking, gate authority, evidence force, assurance force, work enactment, abductive selection, temporal/dynamics currentness, or TGA-path currentness. If any of those claims become live, name the exact neighboring pattern and keep the representation shift to source-finding, inspection, comparison, technical review, reversible planning preparation, report-only use, or exploratory use until the neighboring source relation is supplied.

##### A.6.3.RT:4.5.c.1. Same-entity entry condition for decode-mediated cases
A decode-mediated or latent/distributed case may stay here only when the target rendering is tethered back to already pinned and provenance-bearing source `U.Episteme` claim graph for the same described entity.

The minimum entry condition is:
- pinned source claim or source publication;
- decode path or access route;
- recoverability evidence for the intended use;
- admissible use-support value;
- remaining reader action.

A readable decoded result alone does not establish direct access to the described entity, work authority, evidence force, gate passage, assurance force, TGA-path currentness, or ontology-frame retargeting. If the entry condition is missing, the current disposition is report-only, exploratory, source-bearing reopen, blocked current transfer, or a named neighboring-pattern handoff.

##### A.6.3.RT:4.5.d. Composition and reopen rule
Repeated same-regime normalization may be idempotent, but heterogeneous regime shifts are generally order-sensitive. Multi-publication chains are checked pairwise, but the final use must preserve accumulated loss rather than restarting as if each pair erased earlier losses.

Each step in a chain keeps recoverable:
- source and receiving described entity;
- claim or commitment under test;
- representation-scheme delta;
- preserved and withdrawn commitments;
- loss and recoverability;
- remaining admissible reader action.

The case reopens whenever recoverability assumptions, pins, provenance, correspondence support, target-face admissibility, primary semiotic mode, or accumulated loss changes. A representation shift also reopens if what looked like one same-entity line turns out to require a new described entity, a counter-witness disposition, or a decode path with higher evidence requirements than currently declared.

#### A.6.3.RT:4.6 - Hard boundary rules

A case reviewed under this pattern keeps the following explicit:
- `describedEntityPolicy = preserve` is mandatory;
- any change of `DescribedEntityRef`, described-entity kind, ontology frame, admissible predicate set, or invariant-bearing target applies `A.6.4`;
- purely textual rewrite cases stay with `ConservativeRetextualization`;
- explanation-facing cases stay with `ExplanationFaithfulnessProfile` unless the described entity, kind, ontology frame, admissible predicate set, or invariant-bearing target changes;
- carrier work stays outside this pattern;
- geometry, notation, embedding space, feature clustering, or readable decoded output must not become ontology-by-default;
- a `PathSliceId`, `CrossingRef`, or `DecisionLogRef` does not prove same-described-entity continuity by itself;
- `StructuralReinterpretation` receives retargeting semantics from `A.6.4` and `E.18`; it is not proof of semantic continuity;
- changed problem formulation leaves this pattern for `B.5.2` when it changes abductive prompt, candidate generation, rival-set formation, selected prime hypothesis, plausibility filtering, or abductive reopen;
- temporal, dynamics, and control claims leave this pattern for `C.27` or `A.3.3` when freshness, rhythm, effort/inertia, state-space, trajectory, reusable transition law, or control relation is live;
- the family changes representation scheme, not face governance, and it therefore stays under existing `E.17.0 / E.17` face discipline rather than creating a new publication family.

If recoverability depends on decoding, probing, or intervention, the evidence class must bound admissible use; otherwise the case stays exploratory, report-only, or outside the admissible same-described-entity path under `A.6.3.RT`. Low-evidence decode-mediated results are not canonical publications with reduced support; they are bounded exploratory or report-only renderings. Non-latent cases remain the default entry path until decode-mediated recoverability is made explicit.

When a counter-witness exists but the receiving item remains useful, the current disposition is controlled coarsening, source-bearing reopen, bridge support, report-only use, exploratory use, or a named neighboring-pattern handoff. Do not keep an unnamed middle state where the item remains rhetorically useful but no FPF disposition is stated.

### A.6.3.RT:5 - Archetypal grounding

#### A.6.3.RT:5.1 - Same-entity text-to-table shift
**Source slice.** `Service S showed three recurring latency spikes in the evening batch window. Trace T-44 and dashboard pin D-17 identify the same service and time window.`

**Published table slice.** `| Service | Window | Spike count | Source pins |
| Service S | Evening batch | 3 | T-44, D-17 |`

This is an admissible direct `RepresentationTransduction` if no new claims are introduced, the same described entity stays explicit, and the representation-factor delta is declared. In ordinary engineering use, this usually needs a visible source tether, explicit loss notes if anything was omitted, and a clear statement that the table is still about the same service occurrence rather than a new described entity.

#### A.6.3.RT:5.2 - Same-entity table-to-diagram shift
**Source table slice.** `| Node | Depends on |
| CoolingLoop | Sensor A |
| CoolingLoop | Valve B |`

**Published diagram slice.** `CoolingLoop -> Sensor A; CoolingLoop -> Valve B`

The move stays in this pattern only if the described entity is preserved, the diagram does not silently add new semantic commitments, and reasoning-medium change is declared. If the diagram starts asserting dependency theory not actually stated by the source table, the case must reopen and may leave this pattern.

#### A.6.3.RT:5.2.a - Correspondence-mediated text-to-table shift
**Source prose slice.** `In the safety view, CL-2 maintains the required temperature condition during standard load.`

**Published table slice.** `| View | Entity | Condition | Correspondence model |
| Safety | CL-2 | required temperature condition during standard load | CM-12 |`

The move stays in this pattern only if the correspondence remains explicit, the described entity stays preserved, and the resulting table does not quietly import bridge semantics or a changed described entity. Because the required correspondence support is doing real work here, a source-bearing continuity note is often warranted instead of relying only on the rendered table.

#### A.6.3.RT:5.2.b - Same-entity diagram-to-structured-notation shift
**Source diagram slice.** `CoolingLoop -> Sensor A; CoolingLoop -> Valve B`

**Published notation slice.** `dependsOn(CoolingLoop, SensorA)`
`dependsOn(CoolingLoop, ValveB)`

This remains under `RepresentationTransduction` when the notation stays tethered to the same relation line already visible in the diagram, the described entity remains preserved, and no additional dependency theory is silently imported by the notational rendering.

#### A.6.3.RT:5.2.c - Functional-description diagram/table/screen shift

**Source slice.** `The mixing cell transfers liquid from Tank A through heat exchanger H-2 to reactor R-4; the source description is about the same declared functional slice and keeps instrumentation/control claims outside this relation.`

**Published table/screen slice.** `| Function relation | Source | Target | Limit |`
`| transfer and heat before reaction | Tank A | R-4 via H-2 | no control-loop claim |`

This remains `RepresentationTransduction` only when the same described entity is preserved and the table or screen changes representation scheme or reasoning medium without adding performed-work order, module structure, evidence, gate passage, or control architecture. If the diagram, table, or screen changes the governed target into a functional, control, or flow architecture claim rather than re-rendering the already declared functional slice, leave this pattern for `A.6.4`, `OntologicalReframing`, or `E.18` as applicable. If the diagram order is explanatory, causal, dependency-like, or didactic, do not read it as physical time order or performed-work sequence unless that temporal claim is present in the source episteme and separately supported. If a parser or OCR step only extracts pixels, text, or carrier layout from a scanned diagram or screen, start with `A.7`; enter this pattern only when the extracted structure is being treated as a same-described-entity representation of source `U.Episteme` claims with source tether and loss notes visible.

If the published screen becomes honest only by omitting exceptions, confidence bands, or source distinctions and by carrying a narrower admissible use with source-bearing return, move to `A.6.3.CSC Controlled Semantic Coarsening` rather than keeping the case here as ordinary representation transduction.

#### A.6.3.RT:5.3 - Boundary to textual rewrite
A source prose note is shortened, reordered, or translated but remains essentially textual. That case stays with `ConservativeRetextualization`, not this pattern.

#### A.6.3.RT:5.4 - Boundary to explanation-facing renderings
A representation shift is performed mainly to teach or narrate rather than to publish another same-entity representation regime. That case leaves this pattern and is reviewed under explanation governance.

#### A.6.3.RT:5.4.a - Boundary to bridge-bearing comparison
**Source slice.** `Local reliability note: Pump P-2 remained within operating range during test window W-3.`

**Published comparative slice.** `Pump P-2 in W-3 behaves like Unit U-7 in Plant B and can therefore be treated as operationally equivalent for this comparison.`

This does **not** stay in `RepresentationTransduction`. The rendering has moved from a same-described-entity representation shift to comparative or bridge-bearing reading across contexts. Once the publication starts asserting cross-context equivalence, substitution, or comparative licence, the case must leave this pattern and move to explicit bridge-governed review.

#### A.6.3.RT:5.4.b - Boundary to carrier/export work
**Source rendering slice.** `| Service | Window | Spike count | Source pins |`

**Published export slice.** `latency-report.csv` and dashboard PNG generated from the same table.

This also stays outside `RepresentationTransduction`. The representation scheme was already chosen; what follows is carrier formatting, export, packaging, or rendering work on that representation. The didactic point is that not every change in visible form is a new same-described-entity representation transition.

#### A.6.3.RT:5.4.c - Boundary to coarsened dashboard view
**Source slice.** `The incident worksheet tracks three causal branches, two confidence bands, and one still-open ambiguity note for Service S.`

**Published dashboard tile.** `Service S: current dashboard view foregrounds cache-failover evidence; alternative branches and confidence bands remain in the incident worksheet.`

This does **not** remain ordinary `RepresentationTransduction` if the tile is treated as more than a narrow report view. The tile foregrounds one causal branch and suppresses uncertainty and alternative branches, so it stays honest only with source-bearing return to the source-bearing worksheet and a non-admissible downstream-use line. It is not a causal proof, service status verdict, or action cue. Once that narrower-use card becomes primary, the case leaves ordinary same-described-entity representation transduction and must use `A.6.3.CSC Controlled Semantic Coarsening` rather than being treated as a normal scheme shift.



#### A.6.3.RT:5.5 - Boundary to decode-mediated latent cases
A reviewer or decode path tries to restate a latent region or distributed feature cluster as explicit entity/relation content. This stays outside the admissible same-described-entity path under `A.6.3.RT` unless the pinned source claim or publication, decode path or access route, recoverability evidence, admissible use-support value, and remaining reader action are already present. Readable decode output alone is not enough.

#### A.6.3.RT:5.5.a - Guarded decode-mediated readout
**Pinned source cluster.** `Probe run P-8 is tied to model-state log M-12 and evaluation bundle EV-4 for the same diagnostic case.`

**Published exploratory slice.** `A decode-mediated readout suggests a cluster that may correspond to the same failure episode already pinned in P-8 / M-12 / EV-4. This rendering stays exploratory and report-only until the required recoverability evidence is published.`

This example remains guarded-open rather than green. The didactic point is that a decode-mediated rendering may still be useful, but it does not become a normal same-entity publication merely because the result looks readable.

### A.6.3.RT:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto/Epist**, **Prag**, **Did**.
This pattern intentionally biases toward same-entity representation shifts and away from hidden retargeting, explanation inflation, or ontology-by-default through notation or geometry. The main mitigation is explicit recoverability discipline, preserve-vs-retarget escape rules, and directly reviewable entry cases before decode-mediated ones.

### A.6.3.RT:7 - Conformance Checklist

A conformance check is retained only if it changes the next admissible use of the shifted representation, blocks a concrete overclaim, or preserves a source/reopen path needed for the declared admissible use.

#### A.6.3.RT:7.1 - RT-Core ordinary checks

1. **CC-RT-1 — Same described entity remains explicit.**
   The case preserves `describedEntityRef` without special pleading.
2. **CC-RT-2 — Representation shift is the right family.**
   The result is genuinely a representation-scheme or reasoning-medium shift rather than mere textual rewrite, explanation work, carrier work, or changed described entity.
3. **CC-RT-3 — Admissible and non-admissible use are visible.**
   The ordinary use path states the source described entity, receiving described entity or preservation claim, the source claim or commitment preserved for the intended use, the representation-scheme or reasoning-medium change, the admissible reader action, and the downstream use not made admissible by this representation shift.
4. **CC-RT-8 — Preserve-vs-retarget handoff is explicit.**
   If the case fails the ordinary checks, the handoff target is explicit (`A.6.3.CR`, `E.17.EFP`, `A.6.3.CSC`, `A.6.4`, carrier work under `A.7`, or another governing pattern).
5. **CC-RT-14 — Functional-description publication overread is blocked.**
   Functional diagrams, tables, screens, exports, and parser/OCR results are kept separate from performed `U.Work`, gate passage, evidence, engineering justification, supervisory/control architecture, and carrier work. OCR/parsing starts with `A.7`; same-entity representation work stays here only when source tether, same described entity, representation-scheme change, and loss notes remain visible.

#### A.6.3.RT:7.2 - RT-Conditional checks

1. **CC-RT-4 — Factor, reasoning-medium, and mode deltas are explicit when load-bearing.**
   `representationFactorDelta`, `inferenceRegimeDelta`, and any load-bearing `semioticModeShift` are explicit when they materially shape review or misuse risk.
2. **CC-RT-5 — Extended delta factors are explicit when load-bearing.**
   `salienceShift`, `topologyShift`, `admissibleUseShift`, `calibrationShift`, and `interactivityShift` are named whenever they materially shape review or misuse risk.
3. **CC-RT-6 — Decode-mediated cases carry additional recoverability evidence.**
   If the case is decode-mediated or latent/distributed, the pinned source claim or publication, decode path or access route, recoverability evidence, admissible use-support value, and remaining reader action are explicit.
4. **CC-RT-7 — Loss, provenance, pinning, and reliability are explicit when needed.**
   Losses, provenance, pinning, and reliability transport are stated or inherited by visible pinned reference when external reliance, dispute, gate, assurance, evidence, or cross-context use is live.
5. **CC-RT-9 — Direct vs correspondence split is explicit when correspondence is doing work.**
   The case states whether it is direct or correspondence-mediated; if correspondence-mediated, `CorrespondenceModelRef` is explicit.
6. **CC-RT-10 — Non-default face/rendering admissibility is explicit.**
   Any `InteropCard`, `AssuranceLane`, gate-bearing, or decode-bounded use states governing publication-face admissibility and keeps same-entity support visible.
7. **CC-RT-11 — Decode-mediated same-entity entry tether is explicit.**
   A decode-mediated case states how the target rendering is tethered back to already pinned and provenance-bearing source `U.Episteme` claim graph for the same described entity.
8. **CC-RT-12 — No hidden bridge or face-family inflation.**
   The case makes clear that representation work does not by itself grant bridge, substitution, or comparative-reading licence and does not create a new face family.
9. **CC-RT-13 — Reopen triggers are explicit when recoverability, admissibility, or primary mode changes.**
   If recoverability assumptions, pins, provenance, correspondence support, target-face admissibility, or the primary semiotic mode change, the case records the reopen trigger explicitly.

### A.6.3.RT:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it is wrong | How to avoid it |
|---|---|---|
| Treating every format shift as harmless formatting | representation changes can alter reasoning possibilities and recoverability | publish factor delta and reasoning-medium delta explicitly |
| Collapsing representation-scheme shift, semiotic-mode shift, and viewpoint shift into one vague change | reviewers cannot tell what actually changed or what required support is primary | name scheme, mode, and viewpoint separately and use the canonical boundary exemplars when only one of them changed |
| Letting notation become ontology-by-default | diagram or geometry starts pretending to define the world rather than represent it | keep ontic scaffold preservation and recoverability explicit |
| Hiding retargeting under representation language | a changed described entity is mislabeled as same-entity representation work | apply `A.6.4` whenever `DescribedEntityRef` changes |
| Starting with latent/distributed cases before recoverability is explicit | decode support load overwhelms same-entity review | keep decode-mediated cases out until decoding access and evidence class are explicit |

### A.6.3.RT:9 - Consequences

- Same-entity representation shifts get an admissible place without inventing a new heavy governing pattern.
- Representation-factor and reasoning-medium changes become explicit rather than rhetorical.
- Recoverability and decode dependence become reviewable instead of hidden behind cleaner renderings.
- The pattern remains safely bounded by `A.6.3`, `A.6.4`, explanation governance, and carrier work.

### A.6.3.RT:10 - Rationale

This pattern is worth splitting out because representation changes are already happening in practice and they are not well served by treating every such case as either mere rewriting or full retargeting. Keeping the family under `A.6.3` preserves governing-pattern boundary while making representation-factor and recoverability support needs explicit.

### A.6.3.RT:11 - SoTA Alignment: Adopted/Adapted Invariants And Rejected Shortcuts

**SoTA alignment rule.** Read each row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and Relations of this pattern.

**Claim 1.** Best-known current architecture-description and model-based practice treats views, representation schemes, and reasoning media as load-bearing rather than as decorative formatting.
**Practice source, local alignment, and adoption decision.** ISO/IEC/IEEE 42010:2022 and current SysML v2 view practice (source maturity = mature standard plus current technical specification/practice) treat viewpoint, view, model kind, and rendering discipline as explicit review targets rather than mere layout choices. This pattern **adopts** explicit representation-scheme review, **adapts** it to same-described-entity viewing under `A.6.3`, and **rejects** the shortcut where a clearer table, diagram, or notation is treated as if it had automatically earned ontology or authority not carried by the source support.

**Claim 2.** Best-known contemporary notation-and-reasoning practice treats tables, diagrams, and structured notations as reasoning media with different inspection possibilities, not as neutral visual restyling.
**Practice source, local alignment, and adoption decision.** Post-2015 model-based and notation-sensitive review practice (source maturity = widely used technical practice) treats representational form as something that changes what readers can inspect, compare, or replay. This pattern **adopts** reasoning-medium review, **adapts** it through explicit factor and medium deltas, and **rejects** hidden dependency-theory uplift or silent added semantic commitment by prose-to-diagram or diagram-to-notation moves.

**Claim 3.** Best-known representation-aware practice treats latent geometry, decoded output, and representation structure as evidence-bounded interpretation that needs a declared support path before it can carry an engineering claim.
**Practice source, local alignment, and adoption decision.** Representation engineering and causal-abstraction practice (source maturity = research/technical practice supporting evaluation posture) treats internal representations as inspectable, monitorable, manipulable, or experimentally aligned only through explicit methods that connect representation to behavior, causal role, or source support. BLT/LCM-style model examples (source maturity = examples/analogy only here, not load-bearing authority) show that representation regime matters, but they do not by themselves decide when a diagram, decoded output, or latent cluster becomes a valid engineering claim. This pattern **adopts** representation-validity grounding through source tether, recoverability target, decode path, `recoverabilityEvidenceClass`, and declared probe/intervention support where claimed; it **rejects** the shortcut where latent geometry, diagram topology, or decoded prose becomes ontology by readability or model reputation.


**Local stance.** The load-bearing SoTA claim for this pattern is narrow: representation regime and reasoning medium are admissible review targets, but geometry, notation, topology, probe output, decoded prose, or latent/distributed structure do not become ontology, evidence, gate support, work authority, or engineering justification unless a declared support path makes that exact use admissible.

### A.6.3.RT:12 - Relations


- **Builds on:** `A.6.3`, `A.6.2`, `A.7`, `E.10.D2`, `C.2.7`, `E.17.0`, `E.17`, `F.9`, `F.18`
- **Coordinates with:** `ConservativeRetextualization`, `A.6.3.CSC Controlled Semantic Coarsening`, `ExplanationFaithfulnessProfile`, `E.17.ID.CR ComparativeReading`, `A.6.4`, `F.9`, `F.9.1`, `E.18`, `A.15`, `A.10`, `B.3`, `B.5.2`, `A.20`, `A.21`, `C.27`, `A.3.3`, explicit decoding-access review
- **Impact radius:** primary touch `A.6.3`; selected edit companion `A.6.4`; secondary review support `C.2.7`, `E.17.0`, `E.17`, `F.9`, decode-mediated recoverability review, TGA path interpretation under `E.18`, and project-side exits under the exact neighboring pattern when live
- **Boundary notes:** textual same-regime rewrites stay with `ConservativeRetextualization`; explanation-facing renderings stay with `ExplanationFaithfulnessProfile`; bounded comparative review cases apply `E.17.ID.CR ComparativeReading`; described-entity changes apply `A.6.4`; coarsened source renderings apply `A.6.3.CSC`; bridge, work, evidence, assurance, gate, abductive, temporal, dynamics, and TGA-path consequences remain bounded by explicit evidence and downstream handoff.

### A.6.3.RT:12a - Boundary with quantum-like state-representation shortcuts

Use RT first when the same described entity is represented through a different representation scheme: text-to-table, model to diagram, diagram to structured record, state vector to typed description, or one notation to another. Ordinary representation-scheme change remains RT even when the new scheme is more compact.

Action path:

1. Confirm that the described entity stays the same. If it changes, leave RT.
2. Name the source representation scheme and target representation scheme.
3. State what changed in representation factor, reasoning medium, mode, salience, topology, actionability, calibration, or interactivity.
4. State recoverability: what can be recovered from the target representation, by which decode path, and with which evidence.
5. If the target representation claims to preserve action, intervention, manipulation, explanation, or cross-abstraction structure, state the causal-abstraction or approximate-causal-abstraction mapping before treating the shortcut as QL coarsening.
6. Ask whether the shortcut depends on a QL cue: contextual probability, incompatible probes, instrument-like update, Hilbert-like or orthomodular representation, open-information-system update rule, probe frame, export-admissibility evidence requirement, or declared lossy export of a state that matters to the decision.
7. If no, keep the case under RT, CSC, ordinary abstraction, compression, diagramming, causal abstraction, approximation, or a declared representation-learning access pattern, whichever governs the actual support claim.
8. If yes, coordinate with the `C.26` state-representation coarsening support section and state admissible use, non-admissible use, and return condition.

For ordinary use, start with the standard shortcut mini-form:

| Mini-entry | Question |
| --- | --- |
| Source-loss basis | Which representation scheme, state reading, fuller model, or evidence set loses distinctions in the shortcut? |
| Shortcut | Which cheaper, typed, quantized, symbolic, lower-detail, or otherwise transformed representation is used? |
| Loss | Which precision, expressivity, compatibility, recoverability, or evidence relation is not carried? |
| Admissible use | Which decision, explanation, triage, comparison, or action-selection move remains admissible for the shortcut? |
| Reopen | Which dispute, decision change, demand for use with a higher evidence requirement, evidence gap, or recoverability failure sends the reader back to the source representation or fuller model? |

Use a fuller C.26 coarsening record only when the shortcut becomes reusable, formal, empirical, high-stakes, or tied to comparative performance or tractability claims. In that fuller record, add the mechanism, baseline path, non-admissible use, and QL cue needed for the additional-support claim.

Do not describe ordinary compression, low-bit implementation, diagramming, or representation learning as quantum-like unless the formal cue is load-bearing.
### A.6.3.RT:12b - C.29 MLA relation

> When a same-described-entity representation-scheme transition imports a contested or load-bearing mathematical lens, `A.6.3.RT` still governs the source and target representation schemes, same-described-entity relation, preserved and lost scheme features, and transduction boundary. The applicable `C.29` output for the stated use (`MLA.LensCandidateNote`, `MLA.OneLine`, `MLA.MiniCard`, or `MLA.FullCard` when required) may be cited only for adequacy of the mathematical lens used in that transition. It does not replace the representation-transduction record or broaden the transition into bridge, evidence, or causal support.


### A.6.3.RT:End
## A.6.4 - `U.EpistemicRetargeting` — describedEntity‑retargeting morphism

**One‑line summary.** `U.EpistemicRetargeting` is the **describedEntity-retargeting** species of `U.EffectFreeEpistemicMorphing`: an effect‑free episteme→episteme morphism that **intentionally changes what the episteme is about** (the occupant of `DescribedEntitySlot` in C.2.1) under a declared `KindBridge` and invariant, while remaining conservative with respect to that invariant.

**Placement.** After **A.6.3 `U.EpistemicViewing`**, before **A.6.5 `U.RelationSlotDiscipline`**.

**Builds on.**
A.6.0 `U.Signature`; A.6.2 `U.EffectFreeEpistemicMorphing`; A.6.3 `U.EpistemicViewing`; A.6.5 `U.RelationSlotDiscipline`; A.7/E.10.D2 (I/D/S discipline, `DescriptionContext`); C.2.1 `U.Episteme — Epistemes and their slot graph`; C.2/C.3 (KD‑CAL/LOG‑CAL, ReferencePlane, Kind‑level reasoning); F.9 (Bridges, `KindBridge`, CL/CL^plane, SquareLaw witnesses).

**Used by.**
E.18 (E.TGA StructuralReinterpretation and other reinterpretation nodes); discipline packs for signal/spectrum transforms, data↔model retargetings, abstraction/refinement under kind‑invariants; KD‑CAL/LOG‑CAL retargeting rules; additional species for architecture and governance reinterpretations.

**Governed object in plain terms.** One effect-free episteme-to-episteme retargeting where the source episteme and receiving episteme intentionally describe different but bridge-related entities.

**Governing move in plain terms.** Change the occupant of `DescribedEntitySlot` under a declared `KindBridge` and invariant, while making preserved commitments, withdrawn commitments, admissible predicate changes, and source-bearing reopen conditions visible.

**Use this when.** Use this pattern when a representation, view, functional description, model, diagram, `StructuralReinterpretation`, or other episteme-facing item no longer describes the same entity, but a declared bridge and invariant make a controlled retargeting admissible.

**What goes wrong if missed.** A changed target is treated as "the same thing in another form", so readers inherit claims, gates, evidence, work authority, or TGA-path currentness that the new described entity does not support.

**What this buys.** One honest retargeting relation: the reader can see the source entity, receiving entity, bridge, invariant, preserved commitments, lost or new commitments, and the exact admissible use that remains.

**Not this pattern when.** Not this pattern when the described entity is preserved and the main change is wording (`A.6.3.CR`), representation scheme or reasoning medium (`A.6.3.RT`), controlled coarsening (`A.6.3.CSC`), explanation mode (`E.17.EFP`), bridge-supported comparison without retargeting (`F.9` or `F.9.1`), work (`A.15`), evidence (`A.10`), assurance (`B.3`), gate decision (`A.21`), temporal adequacy (`C.27`), or dynamics/control law (`A.3.3`).

### A.6.4:1 - Problem frame

Many important operations on descriptions **change the described entity** while preserving a structural or behavioural invariant:

* **Physical vs functional reinterpretation.**
  An episteme about a physical module (cabinet, rack, device) is re‑interpreted as an episteme about a function‑holon it realises. This is precisely what StructuralReinterpretation nodes in E.TGA attempt to do.

* **Signal vs spectrum.**
  A time‑domain signal description is re‑targeted to a description of its frequency‑domain spectrum. The underlying invariant (typically energy or inner‑product) is preserved, but the described entity changes from `time→value` trajectories to `frequency→amplitude/phase` distributions.

* **Data vs model.**
  An episteme about raw observations (dataset) is turned into an episteme about a learned or estimated model, keeping an invariant such as likelihood, sufficient statistics, or predictive performance.

All of these are **Ep→Ep transforms** that:
* do **not** change the Intension (`I`) directly (they operate on descriptions/specifications),
* do **not** merely slice or re‑express an episteme of the same entity (that would be EpistemicViewing, A.6.3),
* but **do change** the **DescribedEntity‑bundle** (`DescribedEntitySlot` and usually `GroundingHolonSlot`) under a formal bridge between kinds.

We need a single, reusable notion of **“epistemic retargeting”** that captures these operations as:
* **effect‑free** at the level of Work/Mechanism (EFEM discipline),
* **describedEntity-retargeting** in a controlled way,
* **invariant‑conservative** (no violation of the declared invariant between kinds),
* and **functorial** (retargetings compose cleanly and align with Bridges).

### A.6.4:2 - Problem

Without a dedicated pattern for EpistemicRetargeting:
1. **Retargeting is silently confused with viewing.**
   Structural reinterpretations (e.g., component→function, signal→spectrum, data→model) can be mistakenly treated as “just another view” of the same entity, even though they change `describedEntityRef`. This hides the fact that the **described entity** has changed and that a `KindBridge` and invariant are required.

2. **Invariants float untyped.**
   Fourier‑style moves, structural reinterpretations, and abstraction/refinement steps are often justified by “energy is preserved”, “this component realises that function”, or “this model summarises those data” — but these invariants are not connected to the episteme morphism class. Without a dedicated species:

   * invariants live only in text,
   * CL‑penalties and ReferencePlane crossings cannot be tracked systematically (Part F).

3. **Cross‑kind reasoning has no canonical morphism.**
   A general EFEM (A.6.2) can change `describedEntityRef` by setting `describedEntityChangeMode = retarget`, but:

   * nothing states what that means at the level of kinds (`Kind(describedEntityRef(X))` vs `Kind(describedEntityRef(Y))`),
   * nothing connects these moves to `KindBridge` and ReferencePlane policies.

4. **StructuralReinterpretation is ad‑hoc.**
   E.TGA treats StructuralReinterpretation as a graph node, but its semantics are much closer to a generic “retargeting under a bridge” pattern than to something specific to graph‑based architectures. Without a core pattern:

   * StructuralReinterpretation risks duplicating retargeting logic,
   * other discipline packs may reinvent their own ad‑hoc re‑targetings.

5. **I/D/S discipline is left underspecified.**
   For descriptions/specifications (`…Description` / `…Spec`), retargeting **changes `DescribedEntityRef` in `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`** (E.10.D2), but must say what happens to context and viewpoint. Without an explicit pattern, these decisions get scattered across different E‑patterns instead of being governed centrally.

### A.6.4:3 - Forces

* **Changing the described entity vs constructing something new.**
  Retargeting expresses **“describing a different but bridge-related entity through an explicit bridge”**, not arbitrary construction of a new Intension/episteme. The invariant lives **across** the pair of entities, not inside a single episteme.

* **Invariants may be lossy but must be explicit.**
  A retargeting is often **lossy** (e.g. data→model, signal→spectrum, structural→functional view), but:

  * it must preserve an explicitly declared invariant (energy, behaviour, statistics),
  * any additional commitment must be modelled as a change of Intension plus new D/S, not as a hidden side-effect.

* **Bridges and CL‑penalties.**
  Retargeting often crosses:
  * Kind‑planes (different `Kind(U.Entity)`),
  * ReferencePlanes (different observability or abstraction regimes).
    Part F already has `KindBridge`, plane Bridges and CL‑penalties; EpistemicRetargeting must **re‑use** them instead of introducing its own notion of “link”.

* **Functors over `α : Ep → Ref`.**
  In the fibred view of epistemes (C.2 / A.6.2), `α : Ep → Ref` maps each episteme to its described entity. EpistemicViewing preserves α (`α(v) = id`). Retargeting must:
  * change α in a controlled way (`α(r) = b : R₁→R₂` in `Ref`),
  * align with `KindBridge` and plane Bridges used for those base arrows.

* **Slot discipline and modularity.**
  C.2.1 and A.6.5 give epistemes a precise `SlotKind`/`ValueKind`/`RefKind` structure, including `DescribedEntitySlot` and `GroundingHolonSlot`. Retargeting laws must be stated **at the slot level**, not on ad‑hoc “fields”, so they can be reused across E.TGA, MVPK, and discipline packs.

### A.6.4:4 - Solution — `U.EpistemicRetargeting` as EFEM profile (`describedEntityChangeMode = retarget`)

#### A.6.4:4.1 - Informal definition

> **Definition (informal).**
> `U.EpistemicRetargeting` is the **describedEntity-retargeting species** of `U.EffectFreeEpistemicMorphing`.
> A `U.EpistemicRetargeting r : X->Y`:
>
> * takes an input episteme `X` and produces an output episteme `Y`,
> * **changes** the occupant of `DescribedEntitySlot` (`describedEntityRef(Y) != describedEntityRef(X)`),
> * relates the kinds of the source and receiving described entities via an explicit `KindBridge` in the appropriate ReferencePlane,
> * preserves a declared **invariant** across the pair of entities (e.g. energy, behaviour, sufficient statistics),
> * is **effect-free** at the level of Work/Mechanism (EFEM discipline),
> * and composes functorially with other retargetings and viewings.

In C.2.1 terms, `U.EpistemicRetargeting` **re-indexes** an episteme along a base-level bridge: it moves the `DescribedEntitySlot` (and often the `<DescribedEntitySlot, GroundingHolonSlot>` bundle) along a `KindBridge`, while re-expressing `content : U.ClaimGraph` and `referenceScheme` so that the declared invariant continues to hold at the new target.

#### A.6.4:4.1.a - Retargeting witness decision block

When a retargeting claim is load-bearing, the receiving text makes these decision-block fields recoverable:

| Field | Required reading |
| --- | --- |
| `sourceEpistemeOrPublication` | The source `U.Episteme`, `U.EpistemePublication`, episteme-lane `U.View`, or exact source publication being retargeted or cited. |
| `receivingEpistemeOrPublication` | The receiving episteme, publication, view, diagram, table, functional description, explanation, `StructuralReinterpretation`, or TGA-facing publication item. |
| `sourceDescribedEntity` | The described entity before retargeting. |
| `receivingDescribedEntity` | The described entity after retargeting. |
| `kindBridgeAndInvariant` | The `KindBridge`, reference-plane relation, and invariant that make the retargeting admissible. |
| `groundingAndContext` | Grounding holon, bounded context, reference plane, reference scheme, viewpoint, and view as far as the intended use needs. |
| `claimOrCommitmentUnderTest` | The claim, invariant, commitment, relation, or project-side use whose retargeted support is being judged. |
| `preservedCommitments` | What the receiving item still carries from the source under the declared invariant. |
| `withdrawnOrNewCommitments` | What the receiving item drops, narrows, adds, widens, or changes. |
| `admissiblePredicateChanges` | Which predicates or claim forms become admissible or inadmissible after the target changes. |
| `supportPosture` | The source-support, bridge-support, or invariant-support posture for the exact intended use. |
| `retargetingWitness` | The reason the changed described-entity reading is supportable now. |
| `counterWitness` | Any fact that weakens retargeting support, such as missing bridge, invariant failure, unsupported predicate transfer, source contradiction, or hidden work/evidence/gate reliance. |
| `lossAndRecoverability` | Preserved distinctions, lost distinctions, recoverability target, recoverability evidence, and source-bearing reopen condition. |
| `admissibleUse` | The exact use that remains admissible now. |
| `nonAdmissibleUse` | The downstream work, evidence, gate, assurance, bridge, decision, abductive, TGA-path, temporal, or dynamics use that is not carried by the current item. |
| `neighboringPatternHandoff` | The FPF pattern that carries the live neighboring claim, when one is live. |
| `remainingAdmissibleReaderAction` | One short plain line saying what the reader may now do or which neighboring pattern now carries the live claim. |

The decision block is not a new FPF kind, record, profile, publication form, or hidden support object. It is a recoverable field set for retargeting cases. Ordinary local retargeting can stay compact when the source entity, receiving entity, bridge, invariant, and remaining reader action are already explicit.

If the bridge or invariant is insufficient for the intended use, the receiving item can still be useful, but the current disposition is source-bearing reopen, bridge support, controlled coarsening, report-only use, exploratory use, or named neighboring-pattern handoff. Do not keep an unnamed middle state where the retargeted item remains rhetorically useful but no FPF disposition is stated.

#### A.6.4:4.2 - Signature (A.6.0 / A.6.5 alignment)

**Signature header.**
`U.EpistemicRetargeting` is a **Morphism‑kind** under A.6.0, specialised from EFEM:

```
SubjectBlock
  SubjectKind    = U.EpistemicRetargeting
  BaseType       = ⟨X:U.Episteme, Y:U.Episteme⟩      // episteme pair
  Quantification = SliceSet := U.ContextSliceSet;
                   ExtentRule := admissible retargeting morphisms
  ResultKind     = U.Morphism                        // an instance r
```

**Vocabulary (re‑uses A.6.2).**

* **Types.** `U.Episteme`, `U.SubjectRef`, `U.Morphism`, `U.EpistemicRetargeting`.
* **Operators.**

  * `id    : U.Morphism(X→X)`
  * `compose(g,f) : U.Morphism(X→Z)` where `f:X→Y`, `g:Y→Z`
  * `apply(r, x:U.Episteme) : U.Episteme`
  * `dom(r), cod(r) : U.Episteme`
  * `subjectRef(-) : U.SubjectRef`
* **Slot‑level discipline.**
  Domain and codomain epistemes are instances of some `U.Episteme` species (typically `U.EpistemeCard`, `U.EpistemeView`, or `U.EpistemePublication`) whose episteme kinds each provide SlotSpecs (A.6.5) including at least:

  * `DescribedEntitySlot` (ValueKind `U.Entity`, RefKind `U.EntityRef`, usually restricted to an `EoIClass ⊑ U.Entity`),
  * `GroundingHolonSlot?` (ValueKind `U.Holon`, RefKind `U.HolonRef`),
  * `ClaimGraphSlot` (ValueKind `U.ClaimGraph`, by‑value),
  * `ViewpointSlot?` (ValueKind `U.Viewpoint`, RefKind `U.ViewpointRef`),
  * `ReferenceSchemeSlot` (ValueKind `U.ReferenceScheme`, by‑value),
  * and, where C.2.1+ is in use, `RepresentationSchemeSlot`, `ViewSlot` and related slots.

The pattern only requires **SlotSpec compatibility** between domain and codomain kinds (in the sense of A.6.5); they need not be literally the same kind.

**Relation to EFEM and Viewing.**

* Every `U.EpistemicRetargeting` is an **EFEM morphism** with `describedEntityChangeMode = retarget` in the sense of A.6.2/C.2.1.
* It **inherits** EFEM laws P0–P5 and adds retargeting‑specific obligations ER‑0…ER‑6 below.
* `U.EpistemicViewing` (A.6.3) covers the complementary case `describedEntityChangeMode = preserve`, where the described entity does not change.

#### A.6.4:4.3 - Laws (ER‑0…ER‑6, over C.2.1 components)

All laws below are **in addition** to A.6.2’s EFEM laws P0–P5 and SHALL be read directly against C.2.1 components and A.6.5 SlotSpecs.

**ER‑0 - Species & DescribedEntityChangeMode.**

* Any morphism `r:X→Y` declared as `U.EpistemicRetargeting` **MUST**:
  * be a species of `U.EffectFreeEpistemicMorphing` (A.6.2), and
  * declare `describedEntityChangeMode(r) = retarget`.
* Consequently:
 * the pair `<DescribedEntitySlot, GroundingHolonSlot>` is the **target bundle** for the change (as in C.2.1 §7.3: DescribedEntity‑bundle retargeting),
 * `DescribedEntitySlot` is **write‑enabled** (unlike Viewing) but only under the constraints below,
  * there exist entities `T₁, T₂ : U.Entity` such that:
    * `describedEntityRef(X) = T₁`,
    * `describedEntityRef(Y) = T₂`,
    * `T₁ ≠ T₂` (as Ref/identity), and
    * `Kind(T₁)` and `Kind(T₂)` are related by a `KindBridge` in Part F’s sense (with declared CL^k).

**ER‑1 - Typed domain/codomain & DescribedEntity‑bundle behaviour.**

For any `r:X→Y` in `U.EpistemicRetargeting`:

1. `X` and `Y` are instances of `U.Episteme` species whose episteme kinds both realise at least the core C.2.1 slots (`DescribedEntitySlot`, `GroundingHolonSlot?`, `ClaimGraphSlot`, `ViewpointSlot?`, `ReferenceSchemeSlot`) and obey A.6.5.

2. At the SlotKind level:

   * `DescribedEntitySlot`:
     * **MUST change** (`describedEntityRef(Y) ≠ describedEntityRef(X)`),
     * the ValueKinds for the slot in the domain and codomain kinds **MUST** be related via an `EoIClass` pair that the `KindBridge` covers (e.g. `PhysicalModule` ↔ `FunctionHolon`, `Signal` ↔ `Spectrum`, `Dataset` ↔ `StatisticalModel`).

   * `GroundingHolonSlot`, if present:
     * is either preserved exactly (`groundingHolonRef(Y) = groundingHolonRef(X)`), or
     * changed only along a declared holon‑Bridge in the same ReferencePlane (for example, moving from one runtime to another under a deployment bridge) with CL^plane penalties recorded in Part F.

   * `ViewpointSlot`, if present:
     * is either preserved, or
     * changed only within a declared `U.ViewpointBundle` (E.17.1/E.17.2), with the corresponding `CorrespondenceModel` explaining how the invariant is maintained under the new viewpoint.

1. For any episteme that is a `…Description`/`…Spec` (E.10.D2), `subjectRef` decodes to `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`. Under EpistemicRetargeting:
   * `DescribedEntityRef` **MUST** change from `T₁` to `T₂` as in ER‑0,
   * `BoundedContextRef` is:
     * either preserved, or
     * changed along an explicit Context‑Bridge (E.10.D1, Part F),
   * `ViewpointRef` is treated as in (2) above (preserved or mapped within a bundle), and any resulting change in admissible claims is governed by ER‑2.

The pair `<DescribedEntitySlot, GroundingHolonSlot>` is treated as a **target bundle**: many practical retargetings work at the level of this bundle rather than DescribedEntity alone, especially in E.TGA.

**ER‑2 - Invariant-based conservativity (lossy but admissible).**

Let `X` and `Y = apply(r,X)` with:
* `describedEntityRef(X) = T₁`, `describedEntityRef(Y) = T₂`,
* `KindBridge(T₁,T₂)` and associated invariant `Inv` declared for this species (e.g. energy, behavioural relation, likelihood),
* `content_X`, `referenceScheme_X`,
* `content_Y`, `referenceScheme_Y`,
* `groundingHolonRef_X`, `groundingHolonRef_Y`.

Then:
1. There MUST exist a KD‑CAL/LOG‑CAL expression of `Inv` such that:
   * all claims about `Inv` that can be derived by reading `content_Y` through `referenceScheme_Y` relative to `<T₂, groundingHolonRef_Y>`
     **are entailed by**
     claims about `Inv` derivable from `content_X` through `referenceScheme_X` relative to `<T₁, groundingHolonRef_X>`.

2. Retargeting, as an EFEM instance, **may**:
   * discard information not needed to maintain `Inv` (lossy summarisation),
   * change representation schemes (e.g. time vs frequency domain),
   * move to different abstraction planes or ReferencePlanes (with Bridges and CL penalties declared),
   but **MUST NOT** violate the declared invariant.

3. Any intended change that adds commitments about `Inv` beyond what is derivable from `X` **is not a valid EpistemicRetargeting**. It must be modelled as:
   * a change of Intension (new D/S pair under A.7/E.10.D2), or
   * a chain of retargetings and Intension updates explicitly recorded in KD‑CAL/LOG‑CAL.

**ER‑3 - Functoriality, α‑reindexing & SquareLaw witnesses.**

EpistemicRetargeting **inherits EFEM functoriality** and specialises it to the retargeting case:

1. At the `Ep` level:
   * `apply(id, X) = X` (no retargeting),
   * `apply(r₂ ∘ r₁, X) = apply(r₂, apply(r₁, X))` whenever domains/codomains match,
   * the composite `r₂∘r₁` has `describedEntityRef(X) = T₁` and `describedEntityRef(cod(r₂∘r₁)) = T₃`, with a composed `KindBridge(T₁,T₃)` whenever the Bridges of `r₁` and `r₂` compose.

2. At the `Ref` level, under `α : Ep → Ref`:
   * each retargeting `r` induces a base arrow `α(r) : R₁→R₂` in `Ref`, compatible with the `KindBridge` used in ER‑0,
   * the square formed by:
     * `X→Y` in `Ep` (retargeting),
     * `α(X)→α(Y)` in `Ref` (base retargeting),
     * any measurement or evaluation morphisms on either side,
       **MUST** commute **up to a declared SquareLaw‑retargeting witness** (Part F / E.TGA), documenting that evaluating then retargeting vs retargeting then evaluating yields equivalent results (modulo CL‑penalties).

2. When retargetings use CorrespondenceModels between epistemes (e.g. aligning detailed hardware layouts with function networks), they MUST:
   * reference the CorrespondenceModel explicitly,
   * publish witness epistemes that certify commutativity of key squares, analogous to EV‑4 but now across **different described entities.**

**ER‑4 - Idempotency & determinism on fixed Bridge/invariant.**

For any `r:X→Y` in `U.EpistemicRetargeting`, with fixed:
* `KindBridge(T₁,T₂)` and ReferencePlane policies,
* invariant `Inv`,
* configuration (ContextSlice, representation families, CorrespondenceModels),

the following MUST hold:

* **Idempotency.**
  Applying `r` twice does not further change the described entity or invariant‑relevant content:
  * `apply(r, apply(r, X))` is **isomorphic** (in the EFEM sense) to `apply(r, X)`,
  * `describedEntityRef` is already `T₂` after the first application,
  * `content` and `referenceScheme` differ at most by declared structural equivalence (e.g. normal forms at the new target).

* **Determinism.**
  For fixed input `X` and fixed Bridge/invariant configuration, the result is uniquely determined modulo declared equivalence. Any source of non‑determinism (randomness, time, external service state) MUST either:
  * be made explicit as part of `content`/`meta` of `X`, or
  * be moved to a `U.Mechanism` outside the retargeting morphism.

**ER‑5 - Applicability, EoI‑pairs & CL‑discipline.**

Each species of `U.EpistemicRetargeting` MUST declare an **Applicability profile** (A.6.0) that includes:

1. **EoI‑pairs.**
   Admissible pairs of `EoIClass`es (ValueKinds of `DescribedEntitySlot` for domain and codomain), for example:
   * `(PhysicalModule, FunctionHolon)`,
   * `(Signal, Spectrum)`,
   * `(Dataset, StatisticalModel)`.

   For each such pair, the pattern MUST reference the appropriate `KindBridge` species in Part F.

2. **Grounding constraints.**
   Permitted classes of `groundingHolonRef` and ReferencePlanes, including whether:
   * grounding must stay within the same holon,
   * or may move along specific holon Bridges with CL^plane penalties.

3. **Viewpoint/context constraints.**
   Whether retargeting is allowed for all viewpoints or only for specific `U.ViewpointBundle`s (TEVB etc.), and any requirements on `BoundedContextRef`.

4. **CL‑discipline.**
   Minimum CL^k and CL^plane required for the Bridges used, aligning with F.9 and E.TGA’s StructuralReinterpretation rules.

Any attempt to apply a retargeting outside this Applicability profile is **ill‑typed**.

**ER‑6 - Compatibility with Viewing and Mechanisms.**

1. **Separation from Viewing.**

   * Any morphism that **does not change** `describedEntityRef` (and keeps `DescribedEntityChangeMode = preserve`) belongs to A.6.3 `U.EpistemicViewing`, not to `U.EpistemicRetargeting`.
   * Any morphism that **does** change `describedEntityRef` **MUST NOT** be declared as `U.EpistemicViewing`; it is either:
     * a `U.EpistemicRetargeting`, or
     * a more general pattern that composes several retargetings and Intension changes.

   In any composite `V∘r` or `r∘V`, describedEntity changes are localised to retargeting steps; Viewing steps are always `describedEntityChangeMode = preserve`.

2. **Separation from Mechanisms.**

   * Retargeting MAY depend on outputs produced by `U.Mechanism` (e.g., computing a Fourier transform, fitting a model), but those are separate Work/Mechanism steps.
   * `U.EpistemicRetargeting` itself remains **effect‑free**: it rearranges epistemes, slots and ClaimGraphs, but does not perform measurements or actuation.

#### A.6.4:4.4 - Boundary with representation, explanation, TGA, and neighboring claims

`U.EpistemicRetargeting` is triggered by changed described entity, described-entity kind, ontology frame, admissible predicate set, or invariant-bearing target. It is not triggered by changed wording, changed representation scheme, changed explanation mode, or publication formatting alone.

Boundary rules:
- if the described entity is preserved and the main change is representation scheme or reasoning medium, use `A.6.3.RT`;
- if the described entity is preserved and the main change is explanation mode, explanatory stance, or explanation-facing publication, use `E.17.EFP`;
- if the source and receiving items are only bridge-supported comparison, analogy, equivalence, or substitution support, use `F.9` or `F.9.1` instead of reading the bridge as identity;
- if the receiving item is useful only under narrower declared use with visible loss and source-bearing reopen, use `A.6.3.CSC`;
- if decoded or latent output is readable but not tied to source claim, access route, recoverability evidence, use-support value, and remaining reader action, keep it report-only, exploratory, source-bearing reopen, or in the named neighboring pattern;
- if a `StructuralReinterpretation`, `PathSliceId`, `CrossingRef`, or `DecisionLogRef` is present, use `E.18`, `A.20`, or `A.21` for graph, path, constraint, and gate relations. Those references do not prove semantic continuity or retargeting support by themselves;
- if changed problem formulation changes abductive prompt, candidate generation, rival-set formation, selected prime hypothesis, plausibility filtering, or abductive reopen, use `B.5.2`;
- if the receiving item is used as work, evidence, assurance, gate passage, temporal claim, dynamics law, or control relation, use `A.15`, `A.10`, `B.3`, `A.21`, `C.27`, `A.3.3`, or the exact neighboring governing pattern.

`StructuralReinterpretation` in `E.18` receives retargeting semantics from this pattern. It is not a TGA-local retargeting kind and not proof that the source and receiving items describe the same entity.

### A.6.4:5 - Archetypal grounding (Tell-Show-Show)



**Tell.**
EpistemicRetargeting captures **“same invariant, different described entity”** moves:

* the source episteme describes “this cabinet”, while the target episteme describes “the routing function it realises”;
* the source episteme describes “this signal over time”, while the target episteme describes “its spectrum over frequency”;
* the source episteme describes “this dataset”, while the target episteme describes “a model class with parameters θ learned from it”.

In each case, what remains stable is an **invariant** (behaviour, energy, likelihood), not the described entity itself.

**Show 1 — StructuralReinterpretation in E.TGA.**
* `X` describes a physical module holon `S_phys`.
* `Y` describes a function holon `S_func`.
* A `KindBridge(S_phys, S_func)` expresses “this module realises that function”.
* A StructuralReinterpretation node in E.TGA is an instance of `U.EpistemicRetargeting` whose invariant is the behaviour relation between `S_phys` and `S_func`.

**Show 2 — Signal↔Spectrum.**
* `X` describes a time‑domain signal `s(t)`; `DescribedEntityRef(X) = S_time`.
* `Y` describes its spectrum `S(ω)`; `DescribedEntityRef(Y) = S_freq`.
* `KindBridge(S_time, S_freq)` encodes Fourier duality in the relevant ReferencePlane.
* The invariant is energy (or inner product), expressed as a KD‑CAL statement; EpistemicRetargeting ensures that energy‑related claims in `Y` are entailed by `X`.

**Show 3 — Data→Model.**
* `X` describes a dataset `D` (observations); `DescribedEntityRef(X) = S_data`.
* `Y` describes a model `M` (e.g. a parametric family with learned parameters); `DescribedEntityRef(Y) = S_model`.
* `KindBridge(S_data, S_model)` encodes the intended data→model relation (e.g. MLE, Bayesian posterior).
* The invariant is likelihood or predictive performance; the retargeting laws ensure `Y` does not claim more about this invariant than is supported by `X`.

### A.6.4:6 - Consequences

* **Clear separation of Viewing vs Retargeting.**
  A.6.3 and A.6.4 now jointly distinguish:
  * **views**: same `DescribedEntityRef`, possible representation/viewpoint changes;
  * **retargetings**: different `DescribedEntityRef` under `KindBridge` and invariants.

* **Canonical governing pattern for StructuralReinterpretation.**
  E.TGA StructuralReinterpretation becomes a **species of `U.EpistemicRetargeting`**, not an ad‑hoc special node. This reduces duplication and clarifies how CL penalties and Bridges are used.

* **Invariants become first‑class.**
  Retargeting makes invariants explicit and type‑checked: every such morphism must state what it preserves and how that is expressed in KD‑CAL/LOG‑CAL.

* **Safer cross‑plane reasoning.**
  ReferencePlane crossings and kind‑level moves are handled via existing Bridges (Part F), with CL^plane/CL^k penalties and SquareLaw witnesses, instead of hidden in implementation details.

* **Better integration with I/D/S.**
  For `…Description`/`…Spec` epistemes, retargeting is the only place where `DescribedEntityRef` in `DescriptionContext` is allowed to change; all other I/D/S‑level operations (Describe/Specify, Viewing) keep it fixed.

### A.6.4:7 - Rationale & SoTA‑echoing  *(informative)*
* **Fibrations and base‑change (displayed categories, 2017+).**
  With epistemes forming a category `Ep` fibred over `Ref` via `α : Ep → Ref` (C.2 / A.6.2), EpistemicViewing corresponds to **vertical morphisms** (`α(v) = id`), while EpistemicRetargeting corresponds to **reindexing along base arrows** (`α(r) = b : R₁→R₂`). This lines up with base‑change and transport along fibrations in category theory.

* **Structured cospans and reinterpretation.**
  Modern work on structured cospans and open systems uses cospans and their morphisms to move between different presentations of a system while preserving a notion of interface/behaviour. Retargeting plays a similar role: it moves from one entity kind to another while preserving a declared invariant.

* **Fourier‑style dualities.**
  In signal processing and physics, Fourier and related transforms are often treated as isometries between function spaces, preserving energy while changing the domain of discourse. `U.EpistemicRetargeting` abstracts this pattern: the invariant is codified in KD‑CAL/LOG‑CAL; the morphism explicitly changes the described entity along a `KindBridge`.

* **Data/model duality in ML.**
  Contemporary ML workflows cycle between data and models; invariants such as likelihood, risk, and calibration matter more than raw equality of ClaimGraphs. Retargeting gives a structured way to talk about data→model (and, potentially, model→data) moves as episteme morphisms, rather than untyped “training” steps.

* **Consistency management and abstraction.**
  In model‑driven and bidirectional transformation literature, abstraction and refinement transfers information between models with different subject domains. Treating these as retargetings with explicit Bridges and invariants makes their assumptions amenable to CL accounting and KD‑CAL reasoning, instead of hiding them in tooling.

### A.6.4:8 - Conformance checklist (normative)

**CC‑A.6.4‑1 - EFEM species and DescribedEntityChangeMode.**
Any pattern that claims to define `U.EpistemicRetargeting` **SHALL**:

* declare itself a species of `U.EffectFreeEpistemicMorphing` (A.6.2),
* fix `describedEntityChangeMode = retarget`,
* and state its Applicability profile (EoI‑pairs, contexts, viewpoints, representation schemes, invariants).

**CC‑A.6.4‑2 - Slot‑level read/write discipline.**
Each species of EpistemicRetargeting **MUST**:
* list the SlotKinds it **reads** (at least `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ReferenceSchemeSlot`, plus any C.2.1+ slots used),
* list the SlotKinds it **writes** (at least `DescribedEntitySlot`, typically also `ClaimGraphSlot`, `ReferenceSchemeSlot`, and `meta`),
* state explicitly how `GroundingHolonSlot` and `ViewpointSlot` behave (preserved vs bridged),
* reference A.6.5 to show that SlotSpecs remain consistent across domain/codomain kinds.

**CC‑A.6.4‑3 - Bridge & invariant declaration.**
Each species SHALL:
* identify the relevant `KindBridge` species (and, where applicable, plane Bridges),
* declare the invariant(s) it preserves (in KD‑CAL/LOG‑CAL terms),
* sketch how invariant preservation is checked or approximated (e.g. through proofs, tests, or statistical guarantees).

**CC‑A.6.4‑4 - SquareLaw‑retargeting witnesses.**
Retargeting species that interact with E.TGA or other graph-level transductions **MUST**:
* describe the commutative squares (or more general diagrams) that express “evaluate then retarget = retarget then evaluate” up to equivalence,
* identify the corresponding SquareLaw‑retargeting witnesses and how they are represented as epistemes.

**CC‑A.6.4‑5 - D/S‑context behaviour.**
For retargetings over `…Description`/`…Spec` epistemes:
* laws MUST be phrased in terms of `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`,
* `DescribedEntityRef` MUST change in a way consistent with the declared `KindBridge`,
* `BoundedContextRef` MUST either be preserved or changed only via explicit Context‑Bridges,
* `ViewpointRef` MUST either be preserved or change within a declared `U.ViewpointBundle`.

**CC‑A.6.4‑6 - Separation from Viewing and Mechanisms.**
* Any species that leaves `describedEntityRef` unchanged is **not** a conformant EpistemicRetargeting; it belongs to `U.EpistemicViewing` (A.6.3) or another EFEM species.
* Any species that performs measurements, actuation, or other side‑effects MUST be declared as `U.Mechanism`/`U.WorkEnactment` and cannot be an EpistemicRetargeting.

**CC-A.6.4-7 - Retargeting witness and reopen discipline.**
For every load-bearing retargeting use, the source described entity, receiving described entity, `KindBridge`, invariant, preserved commitments, withdrawn or new commitments, admissible predicate changes, support posture, retargeting witness, and source-bearing reopen condition are recoverable. If bridge or invariant support is insufficient for the intended use, the case records source-bearing reopen, bridge support, controlled coarsening, report-only use, exploratory use, or named neighboring-pattern handoff.

**CC-A.6.4-8 - Neighboring-pattern handoff.**
Retargeting wording does not carry work authority, evidence force, assurance force, gate passage, abductive selection, temporal adequacy, dynamics law, control relation, bridge substitution, or TGA-path currentness unless the exact governing FPF pattern and exact project-side FPF kind or reference are named.

**CC-A.6.4-9 - StructuralReinterpretation boundary.**
When `StructuralReinterpretation`, `PathSliceId`, `CrossingRef`, or `DecisionLogRef` is used, the graph, path, constraint, and gate relations stay with `E.18`, `A.20`, or `A.21`. `StructuralReinterpretation` receives retargeting semantics from `A.6.4`; it is not proof of same-described-entity continuity and not a TGA-local retargeting kind.

### A.6.4:9 - Mini-checklist (for use)

When you think you need "retargeting" in FPF, ask:

1. **Does `describedEntityRef` change?**
   If no, this is Viewing (A.6.3), not Retargeting.

2. **Is there a `KindBridge` between source and receiving entities?**
   If not, add or select the bridge in Part F, or revise the Intension instead of treating the relation as retargeting.

3. **What invariant are you preserving?**
   Write it down in KD-CAL/LOG-CAL terms. If you cannot, retargeting is underspecified.

4. **How do `GroundingHolonRef`, context, and viewpoint behave?**
   State whether they stay the same, move along Bridges, or are out of scope.

5. **Can the operation be factored as Mechanism + pure retargeting?**
   If the step needs computation such as FFT or model fitting, separate the Mechanism from the EpistemicRetargeting.

6. **What remains admissible for the reader?**
   State the remaining reader action, and name source-bearing reopen or a neighboring pattern when the bridge, invariant, or source support is insufficient for the intended use.

### A.6.4:10 - Relations

* **Specialises / is specialised by.**
  * Specialises A.6.2 `U.EffectFreeEpistemicMorphing` as the `describedEntityChangeMode = retarget` profile.
  * Complements A.6.3 `U.EpistemicViewing` (describedEntity‑preserving EFEM) as the “retargeting” counterpart.

* **Constrained by.**
  * A.6.5 `U.RelationSlotDiscipline` for SlotKind/ValueKind/RefKind discipline.
  * C.2.1 `U.EpistemeSlotGraph` for episteme components and `DescribedEntitySlot`/`GroundingHolonSlot`.
  * E.10.D2 (I/D/S discipline; `DescriptionContext`).
  * Part F (Bridges, `KindBridge`, ReferencePlane crossings, CL/CL^plane).
  * E.10 (LEX‑BUNDLE naming rules, especially on `…Slot`/`…Ref` and ban on Subject/Object in episteme tech names).

* **Consumed by.**
  * E.18 (E.TGA StructuralReinterpretation and other cross‑kind architecture transformations).
  * E.17.0/E.17 (for cases where publication needs to move between different entities‑of‑interest but preserve invariants).
  * KD‑CAL/LOG‑CAL rules that reason about retargeting and invariant preservation across different described entities.

### A.6.4:End

## A.6.P — U.RelationalPrecisionRestorationSuite — Relational Precision Restoration (RPR) — Kind‑Explicit Qualified Relation Discipline

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (Core)

**Plain-name.** Relational precision restoration suite.

**Intent.** Provide a family-level, reusable discipline for repairing a recurring defect in FPF texts: **under‑specified relational language** (often phrased as a seemingly binary verb) that actually hides **(i)** higher arity (missing participant positions), **(ii)** multiple semantic change classes, **(iii)** asymmetry between `U.Viewpoint` specifications and `U.View` instances, **(iv)** boundary requirements (signature invariants vs admissibility vs deontics vs evidence/work), and **(v)** endpoint referential compression (pronominal/metonymic stand‑ins and over‑broad kinds).
RPR patterns turn “umbrella relations” into **kind‑explicit, slot‑explicit, qualified relation records** with an explicit **change-class lexicon** and **lexical guardrails**, while respecting the **A.6 Signature Stack** and **A.6.B Boundary Norm Square** separation.

**Placement.** Part A → cluster **A.6 Signature Stack & Boundary Discipline** → header pattern for the **relation‑precision restoration family** (A.6.5, A.6.6, A.6.8, A.6.9, A.6.H, and future A.6.x patterns).

**Builds on.**

* **A.6** (stack layering + boundary discipline requirements).
* **A.6.B `U.BoundaryNormSquare`** (L/A/D/E routing; claim atomicity; cross‑quadrant references).
* **A.6.S `U.SignatureEngineeringPair`** (TargetSignature vs ConstructorSignature; canonical constructor verb mapping; effect‑free constructor ops).
* **A.6.0 `U.Signature`** (SlotSpec requirement for argument positions).
* **A.6.5 `U.RelationSlotDiscipline`** (SlotKind/ValueKind/RefKind stratification + canonical slot verbs; `bind` reserved for name binding).
* **E.8** (pattern authoring discipline; Tell–Show–Show; SoTA echoing hygiene).
* **F.18** (promise vs utterance vs commitment; avoids “interface‑as‑promiser” category errors).
* **E.10** (LEX‑BUNDLE discipline; I/D/S versus publication-form and carrier lanes; L‑SURF token discipline; reserved primitives; Tech↔Plain pairing). *(Referenced conceptually; no extra authoring apparatus implied.)*

**Coordinates with.**

* **A.2.4 `U.EvidenceRole`** (witness semantics: role/timespan/freshness metadata for decision‑relevant witness sets).
* **A.2.6 scope + `Γ_time` discipline** (avoid implicit “current/latest”; make time selectors explicit when time matters).
* **A.7 Strict Distinction** (Object≠Description≠Carrier; avoid treating evidence/logs as properties of prose).
* **A.6.2–A.6.4** (effect‑free episteme morphisms, epistemic viewing/retargeting as disciplined slot writes).
* **A.10 evidence discipline** (witnesses are carrier‑anchored; freshness is adjudicated in work/evidence lanes).
* **C.2.1 `U.EpistemeSlotGraph`** (slot read/write profiles for constructor operators, when declared).
* **C.3.3 `U.KindBridge` + `CL^k` discipline** (repairing endpoint kind mismatches; kind-level congruence + loss notes).
* **E.17 MVPK / multi‑view publication** (faces are views; “no new semantics”; viewpoint accountability).
* **E.19 pattern quality gates** (review/refresh discipline for guardrails and conformance lists).
* **F.17 `UTS`** (when ambiguity clusters become recurring vocabulary: publish stable `RelationKind` tokens and facet head phrases as UTS/LEX‑governed term assets, so rewrites don’t live only inside A‑patterns).
* **F.9 Bridges + CL** for cross-Context or cross-plane reuse (no silent sameness).
* **C.2.2a, A.16, A.16.1, A.16.2, B.4.1, and B.5.2.0** for the language-state seam: language-state chart positions, admissible moves, pre-threshold cue preservation, route publication, admissible retreat/reopen, and prompt-shaped continuations that are not yet stable relation publication; use **A.16.0** only when lineage, branch, loss, or handoff history itself must be published as an explicit trajectory account.
* **C.2.LS, C.2.4, C.2.5, C.2.6, and C.2.7** for language-state facet governance: articulation explicitness, closure degree, language-state anchoring mode, and the language-state representation-factor bundle may be cited by RPR patterns but are not governed here.

**Specialisations already in Core.**
These retained specialisations are current because they each carry one stable reusable repair-load family. Their mnemonic heads remain admissible entry points, but generic `A.6.P` does **not** treat token recurrence alone as sufficient to mint one new specialisation per overloaded trigger word.

* **A.6.5**: RPR for n‑ary relations and slot discipline (archetype: “putting something into a place”; explicit SlotKinds + ValueKind/RefKind + slot‑operation lexicon).
* **A.6.6**: RPR for “relative‑to / basedness” claims (explicit `baseRelation` token + scoped, witnessed base declarations + base‑change lexicon; lexical red‑flags for `anchor*`).
* **A.6.8 (RPR‑SERV)**: RPR for the “service” cluster polysemy (facet‑explicit `serviceSituation` lens; canonical rewrites for `service`/`server`/`service provider`; classification tests for clause vs access point vs provider commitment vs work+evidence).
* **A.6.9 (RPR‑XCTX)**: RPR for cross‑Context “same / equivalent / align / map” talk (explicit Bridges with direction, endpoint refinement, substitution licence, CL and loss notes; blocks silent inversion and “alignment” umbrella verbs).
* **A.6.H (RPR‑WHOLE)**: RPR for “whole/part/integrity/complete” polysemy (WHOL triggers + Boundary–Parthood–Fold–Order/Time–Completeness lens; routes turnkey/end‑to‑end into A.15 coverage; includes publication-form↔referent↔work level test).


### A.6.P:0 — TERM/LEX token guards (local-first)

This pattern reserves the following tokens in Tech/normative prose:

* **RPR** — *Relational Precision Restoration* (the suite recipe; not a new `U.Type`).
* **RelationKind** — a Context-local vocabulary token (signature-level) that fixes polarity and SlotSpecs for participant/qualifier positions. It is a *registry entry/token*, not a relation instance.
* **QualifiedRelationRecord** — the slot-explicit relation instance record kind (Context-local episteme/record kind); instances carry a `relationKind` token reference plus explicit participant/qualifier slots.

**Mint-or-reuse note (recipe-level).** This pattern mints the suite label **RPR**, the role name **RelationKind**, and the generic shape name **QualifiedRelationRecord** as local-first terms for this family. It reuses existing FPF terms (`U.Signature`, SlotKind/ValueKind/RefKind, Bridges/CL, `U.Scope`, `Γ_time`, `U.View`/`U.Viewpoint`, evidence pins/carriers) without changing their meanings.

**Definitions (recipe-level; non-deontic).**

* **RelationKind token** — a declared vocabulary element (signature-level) whose public definition fixes polarity and SlotSpecs for participant/qualifier positions, and that is referenced by L/A/D/E-classified claims that govern admissibility, duties/commitments, and evidence/work.
* **QualifiedRelationRecord** — a Context-local episteme/record kind whose `relationKind` field points (by id/ref) to a RelationKind token and whose instance records make all relation-specification-required participant/qualifier slots explicit.

Rename-guards (common collisions):

* **agreement-like boundary wording** — Plain shorthand for a published boundary-interface description; a conforming text MUST NOT treat such wording as itself establishing a promise/obligation. Promises, duties, and gates are classified under `A.6.B`.
* **bind/binding** — reserved for **name binding** (Identifier → SlotKind/slot-instance) and MUST NOT be used as a synonym for relation instance edits.
* **same/synced/linked/connected/anchored/grounded** — treated as umbrella tokens; allowed as Plain gloss only when immediately mapped to an explicit RelationKind token (Tech) via rewrite rules.

### A.6.P:1 — Problem frame

FPF repeatedly encounters a predictable precision failure mode:

Authors describe a situation with an apparently simple relational phrase:

* “X **is the same as** Y”, “X **is linked to** Y”, “X **is synced with** Y”
* “X **depends on** Y”, “X **is grounded/anchored** in Y”
* “X **maps to** Y”, “X **aligns with** Y”, “X **is connected to** Y”

…but the intended meaning is actually:

1. **Hidden multiarity.** The claim requires additional participant positions: scope, time selector, witness carriers, policy, direction or inverse, reference scheme, representation scheme, mediator publication form, or mediator carrier.
2. **Kind elision.** The umbrella verb stands in for an unstated family of relation kinds (different invariants; different admissibility; different evidence support).
3. **Viewpoint fights.** Different stakeholders describe “the same” relation from incompatible viewpoints, creating polarity flips and silent re‑typing.
4. **Unnameable change semantics.** Authors say “update/bind/anchor/sync”, but mean distinct semantic change classes (retarget vs revise vs rescope vs retime vs witness refresh).
5. **Regression via prose.** Even after ontology repairs, umbrella language re‑enters and collapses distinctions unless structural precision is coupled to lexical guardrails.
6. **Pronominal/metonymic endpoints.** Even when the relation verb is fixed, endpoints may be referred to via pronoun‑like or umbrella tokens (or metonymic pointers), so the relation cannot be typed or audited until endpoint facets/kinds are restored from context.

A.6.P defines a **repeatable precision restoration recipe** that makes this defect repairable and reusable across future A.6.x patterns.

### A.6.P:2 — Problem

How can FPF represent and evolve “relations in prose” that are structurally richer than they appear, so that:

* the **relation kind** is explicit and reviewable,
* missing positions can be made explicit **without semantic drift**,
* changes to the relation can be narrated with **stable semantic change classes**,
* multi‑view publication can exist **without creating multiple incompatible relation specifications**, and
* cross-Context or cross-plane reuse cannot silently assume “sameness by label”?

### A.6.P:3 — Forces

| Force                                 | Tension                                                                                                |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Universality vs precision             | The repair must be reusable across domains, but must not hide the distinctions it is meant to recover. |
| Prose convenience vs relation-specification clarity | Humans want short verbs; engineering/assurance needs declared kinds, slots, and invariants.            |
| Kernel minimality vs safety           | Few primitives are good; umbrella relations are cross‑Context safety hazards.                          |
| Multi‑view reality vs coherence       | Viewpoints must be expressible without silent polarity flips or re‑typing.                             |
| Evolution vs auditability             | Relations change; edits must not rewrite meaning invisibly.                                            |
| Stack discipline                      | Signature invariants, admissibility, deontics, and evidence/work must not be mixed (A.6 + A.6.B).                      |

### A.6.P:4 — Solution — The RPR recipe (Lens → Slots → Change Lexicon → Guardrails), aligned to A.6 / A.6.B / A.6.S

A.6.P defines a **suite recipe**. A pattern is a **RPR‑pattern** (member of A.6.P) iff it provides the ingredients below.

#### A.6.P:4.0 — Trigger rule (when A.6.P applies)

A relation mention or relation-bearing phrase is in-scope for A.6.P when **any** of the following holds:

* the predicate/verb phrase is **lexically overloaded** (umbrella tokens such as “same”, “sync”, “link”, “connect”, “anchor”, “ground”, “align”, “map”, or “depends”), or
* one or more endpoints or qualifiers are expressed via **pronominal, deictic, or metonymic stand-ins** or **over-broad kind tokens** (e.g., “it/this/that”, “the service”, “the system”, “at the table”), such that multiple referents or facets remain plausible, or
* a **generic or over-broad head noun** carries its load only through a qualifier, modifier, or surrounding phrase (e.g., “comparative note”, “safe guidance”, “interactive view”, “reliable output”), so the object kind is still ambiguous even though the qualifier sounds informative, or
* the statement implicitly relies on **scope, Γ_time, viewpoint or view, or reference or representation schemes**, or
* the relation is used for **assurance, admissibility, gating, or publication** decisions, or
* the relation crosses **Contexts or planes** (requires Bridges + CL; no silent equivalence), or
* different stakeholders interpret endpoints differently (multi-view asymmetry and polarity fights).

**Repair order note.** When a load-bearing phrase is triggered because its **head noun** is too generic, first restore what kind of thing the head actually names: record or carrier, reading, process, lane, authority use, or another local kind with named authority-reference relation. Use local described-entity and claim-target discipline (`E.10`, `A.7`, and nearby authority-reference guidance). A narrowing qualifier such as `comparative`, `safe`, `interactive`, or `reliable` may narrow the phrase, but it does **not** by itself restore the head kind. Then apply A.6.P to restore the remaining relation or comparison load. Mixed-kind comparison checks come **after** those two repairs, not before them.

**Adoption test (review heuristic).** If a reviewer can reasonably ask any of: “Which kind is this?”, “What exactly does this span refer to (which facet/kind, and in which lane: Object vs Description vs Carrier)?”, “What relation or comparison load is hidden in this qualifier?”, “What else participates?”, “Under what scope/time/view?”, “What changed?”, or “What makes this admissible?”, then authors SHOULD treat the mention as in-scope and rewrite it into explicit kind+slots form before using it for cross-Context reuse or decision/publication claims.

**Precision/relaxation note.** A.6.P is not a blanket demand that every sentence stay maximally explicit forever. It is a trigger-based repair path for **load-bearing** prose. In design-time FPF texts and in run-time texts being prepared for admissible publication, review, gating, or reuse, the repair should be performed before any later didactic plain-language softening or admissible coarsening. Later relaxation is allowed only when the more precise upstream reading remains recoverable and authoritative.

**Generic trigger-word governance rule (normative).** Overloaded words are diagnostic entry points, not default future governing FPF patterns or `authoritySourceRef` targets. Generic `A.6.P` therefore requires this order: restore head kind first, restore the remaining relation/comparison load second, and only then judge whether one reusable repair-load family is justified as a new specialization. A new `A.6.P` specialization or broader trigger-word governing FPF pattern or `authoritySourceRef` target is owed only when one stable recurring load, one reusable lens or rewrite kit, and one `F.18 -> A.6.P`-surviving head already exist by value across more than one worked case. Otherwise token-specific retained knowledge stays with an existing admissible specialization or in one cluster-local / source-local note rather than expanding generic `A.6.P` into a token bucket store.

#### A.6.P:4.0 - Language-state entry note


RPR entry normally presupposes enough `C.2.4` articulation explicitness that at least one relation-like skeleton can be named explicitly, and often enough `C.2.5` closure that one candidate reading is worth publishing as a relation record rather than remaining cue-pack material.

If the content is still best treated as a cue pack, routed cue set, or unresolved candidate-route cue content, keep it in `A.16.1` / `B.4.1` rather than forcing relation publication prematurely. If the admissible continuation is still an open explanatory question, apply `B.5.2.0`. If a previously published relation must be reopened or backed off because the articulation/closure support collapses, apply `A.16.2` for that retreat rather than silently narrowing the published relation in place.

#### A.6.P:4.0a — Operational repair sequence (how repairs actually proceed)

The suite is presented as **lens → slots → change lexicon → guardrails** because the *stable abstraction* is what keeps repairs reusable. In actual editing, repairs often start from a **triggering token** and proceed through a context-reconstruction step.

Operationally, authors SHOULD follow this repair sequence when applying an RPR repair:

0. **Restore the head kind if needed.** If the triggering phrase uses a generic or over-broad head noun (`note`, `view`, `guidance`, `output`, `record`, `carrier`, and similar placeholders), first state what kind of thing it actually is in source-local terms (publication form, reading, process, authority use, and so on). Do not let a qualifier do this job by implication alone.
1. **Trigger on textual form.** Detect umbrella relation predicates, pronominal/umbrella endpoint tokens or metonymic pointers, and generic-head-plus-load-bearing-qualifier combinations (including domain clusters such as **service** in A.6.8 and cross-Context “same/equivalent/align/map” in A.6.9).
2. **Reconstruct the situation ontology from local context.** Enumerate candidate referents/facets for endpoints *(including A.7 lane: Object vs Description vs Carrier when it matters)*, candidate head kinds where the phrase is noun-led, and candidate `RelationKind` tokens or comparison loads for the overloaded predicate or qualifier, plus implied participants: scope, time, view, scheme, mediator publication form, and carriers. Capture the result as a **Candidate-Set Note** (A.6.P:4.0b) so review has a checkable record: candidates → selected facet/kind → why. When metonymy is plausible, include both the *literal* and the *intended* candidates.
3. **Choose a stable lens** that can represent the reconstructed arity/polarity without ad-hoc role invention.
4. **Refine the ontology under the lens.** Turn implied roles into SlotSpecs; repair endpoint kind mismatches explicitly (narrowing / KindBridge / retargetParticipant); separate object kind, relation load, and qualifier load; make qualifiers explicit as slots or routed conditions.
5. **Emit canonical rewrites + L/A/D/E hooks.** Produce Tech-form rewrites (`relationKind(…)` / arrow form) and state the A.6.B hooks: which parts are L vs A vs D vs E, and which witnesses/commitments/work claims are now demanded.
6. **Only then allow later relaxation.** If a Plain, didactic, or coarsened restatement is still wanted, derive it from the repaired form and keep the repaired form as the authoritative source for any reading that claims bridge, substitution, or reliance beyond the declared note.

**Decision/publication fail-closed (normative).** If an in-scope mention is used to justify an admissibility gate, publication claim, or cross-Context reuse, authors MUST resolve the candidate sets to a selected `RelationKind`, selected endpoint facets/kinds, and any required head-kind reconstruction and emit an explicit rewrite. If that cannot be done from available context and witnesses, keep the statement as Plain/informative gloss (or split into multiple explicit alternatives) and do not treat it as admissible input for the gate.

**Informative: referential compression spectrum.** Many triggers live on a spectrum from high to low referential precision:
pronouns/deictics → overloaded polysemes → coarse domain kinds → facet head phrases → precise domain terms.
Metonymy often shifts the candidate described entity or endpoint (e.g., a place phrase standing in for an object or a role). The repair sequence explicitly treats this as a **candidate-set** problem, not as “the dictionary meaning”.

**Metonymy micro-example (informative; endpoint-side trigger beyond anaphora).**

Draft: “Alice is **at the table**.”

`at the table` → candidates `{place, meeting, record/carrier, role}` → choose explicitly → rewrite into endpoint-refs + qualifiers:

```
CandidateSetNote(triggerSpan="at the table", role=endpointFacet(p₂)):
- candidates: {PlaceRef(Table#7), MeetingRef(NegotiationSession#3), RecordRef(AgendaDoc#12), RoleRef(DecisionMakerSeat#2)}
- selected:   MeetingRef(NegotiationSession#3) + RoleRef(DecisionMakerSeat#2)  // metonymy: place → meeting/role
- consequence: require explicit `meetingRef`, `roleRef`, `Γ_time`, `witnesses` (and route decision/admissibility separately via A.6.B)

participatesInMeetingUnder(
  personRef  = PersonRef(Alice),
  meetingRef = MeetingRef(NegotiationSession#3),
  roleRef    = RoleRef(DecisionMakerSeat#2),
  Γ_time     = snapshot(t),
  witnesses  = {attendanceLogPins}
)
```

If the literal location reading is intended, select `PlaceRef(Table#7)` and rewrite as `locatedAt(…)` with an explicit `Γ_time` qualifier.

This step is intentionally **not lexicon-only**. The lexical rewrite is the *output* of an ontology- and lens-constrained repair, not the starting point. If you cannot state the candidate referents/facets, the selected head kind where needed, and the selected `RelationKind` token, the repair is incomplete.

#### A.6.P:4.0b — Candidate‑Set Note (informative; review record)

When endpoint identity (pronoun/deixis/metonymy/coarse kind) or relation-kind selection is ambiguous, reviews can collapse into “lexicon debates”. A.6.P treats this as an ontology reconstruction step with an explicit, checkable intermediate record.

**Candidate‑Set Note template (informative).**

> **Collision note.** This “Candidate‑Set Note” is **not** the F.18 naming-process *candidate set* (NQD-front). It is a local disambiguation record for endpoint referents/facets and RelationKind selection during RPR repairs.

For each ambiguous role (relation kind, endpoint facet/kind, qualifier, mediator), record:

* **Trigger span:** the exact trigger token(s) in the draft (copy/paste).
* **Role being disambiguated:** `headKind` | `relationKind` | `endpointFacet(pᵢ)` | `endpointRef(pᵢ)` | `qualifier(qⱼ)` | `mediator`.
* **Lane (A.7) (when endpoint‑side):** `Object` | `Description` | `Carrier` (state explicitly when live contenders span lanes; lane‑mixing is a common source of boundary-interface category errors).
* **Candidate set:** a short list of plausible **head kinds**, **kinds/facets**, and/or **RelationKind tokens** (not synonyms), each with the local cue(s) that made it plausible.
* **Selected facet/kind (and selected RelationKind, if relevant):** the chosen candidate(s).
* **Why:** the discriminating test(s) that were applied, plus pointers to the specific local evidence/witness cues used (carriers, claims, records/carriers).
* **Consequence:** which SlotSpecs become required/forbidden and which A.6.B hooks are now triggered (L/A/D/E).

Minimal one‑screen representation:

| Candidates (kinds/facets/tokens) | Selected facet/kind | Why (tests + cues) | Consequence (slots + L/A/D/E hooks) |
| --- | --- | --- | --- |
| C1 …; C2 …; C3 … | … | … | … |

**Notes.**

* For **metonymy**, list both the literal candidate and the intended target candidate (and make the shift explicit).
* Keep the candidate set small: include only live contenders, and state the elimination test for the others.
* This note is **informative**: it does not replace routed L/A/D/E claims. It exists to prevent “lexicon instead of ontology”.

#### A.6.P:4.1 — Stable lens

A RPR‑pattern SHALL name a stable mathematical “lens” that prevents re‑inventing roles per domain. Examples of lenses (illustrative):

* **Kind-labelled qualified relation record** (default A.6.P lens)
* **n‑ary relation with distinguished positions** (A.6.5 style)
* **kind‑labelled dependence arrow over a base** (A.6.6 style)
* **span/cospan + declared loss/correspondence notes** (Bridge‑like families)
* **correspondence relation + repair operations** (sync/consistency families)

The lens is a compression device: one stable abstraction that keeps the relation’s **arity and polarity** stable and makes invariants speakable.

#### A.6.P:4.2 — Kind‑explicit relation tokens (no umbrella meaning‑surrogates)

For every in‑scope relational claim, authors SHALL select (or mint) an explicit **RelationKind token** as a declared vocabulary element.

A RelationKind token is authored as a `U.Signature`‑level vocabulary element with explicit SlotSpecs for its participant and qualifier positions (`⟨SlotKind, ValueKind, refMode⟩`). When no suitable token already exists, authors SHALL NOT improvise a one-off string by intuition. They SHALL route mint-or-reuse through **F.18**: use **MintNew** by default, build a seed candidate set, show an honest NQD-front, run the sense-seed read-through, and record why the selected token is chosen from the non-dominated front. Use **DocumentLegacy** only when the label is externally fixed and that status is stated explicitly.

**RelationKind relation specification skeleton (minimum, recipe-level).**
For each `RelationKind` token, a conforming Context publication SHALL publish a vocabulary entry whose **signature-level definition** is paired with (or points to) a **L/A/D/E-classified claim bundle** (“relation specification skeleton”) that declares (at minimum):

The leading **(L)/(A)/(D)/(E)** tags below indicate the intended **A.6.B quadrant classification** for each element of the skeleton.

* **(L) applicability** (A.6.0): the Contexts or planes where the kind is defined (local meaning is first-class).
* **(L) polarity**, and (if needed) explicit **inverse tokens** (no silent role flips in Tech prose).
* **(L) SlotSpecs** for all participant positions (and any qualifier slots exposed by the family) (`⟨SlotKind, ValueKind, refMode⟩`, where `refMode` is either `ByValue` or a concrete `RefKind` token per A.6.5).
* **(A) repair path for endpoint kind mismatches** (normative): allowed repairs are (i) explicit narrowing, (ii) a `KindBridge` (+ `CL^k` + loss notes), and/or (iii) explicit `retargetParticipant`. Renaming endpoints is not a repair.
* **(L) qualifier expectations**: which qualifiers are required, optional, or forbidden (scope, `Γ_time`, `U.Viewpoint` and `U.View`, reference scheme, representation scheme).
* **(D) qualifier placement discipline**: extra parameters belong in `scope` or explicit qualifier slots, not as adjectives attached to endpoint names.
* **(A/E) witness discipline**: when witnesses are required as an admissibility gate and what carrier-anchored witness sets look like in this family.
* **(L/A) admissible semantic change classes** (see §4.4) and whether they require a new edition.
* **(A/E) cross-Context or cross-plane policy** when applicable (Bridge ids + CL + loss notes policy).

**Important stack constraint (A.6 / A.6.S / A.6.B).**
Treat a relation specification as a routed set of claims, not a single magical object:

* **L‑claims** (signature invariants; polarity; SlotSpec typing) live in the signature-level invariant/rule set.
* **A‑claims** (admissibility gates) are authored as admissibility predicates (canonically placed in `Mechanism.AdmissibilityConditions` when an explicit mechanism exists) and may reference the RelationKind token by ID.
* **D‑claims** (duties/commitments) name accountable roles/agents and may reference `L-*`/`A-*` by ID.
* **E‑claims** (evidence/work effects) anchor to carriers and observation conditions and may reference `L-*`/`A-*` by ID.

#### A.6.P:4.3 — Slot‑explicit qualified relation records (recover hidden arity)

A conforming text SHALL ensure that each in‑scope relation instance is representable as a **Qualified Relation Record** (a first‑class record/episteme in the relevant Context) that fills the relation’s slots.

Conceptual notation‑neutral shape:

**Notation note (A.6.5 alignment).** In this family `refMode` is a slot‑content mode: either `ByValue` (inline value of the declared ValueKind) or a concrete `RefKind` token (slot holds a reference/pin of that RefKind).
```
QualifiedRelationRecord :=
⟨ relationKind : RelationKind, // vocabulary token / registry entry (signature-level)

  // participant positions (pattern-specific; relation specification fixes SlotSpecs)
  p₁ : SlotContent(VK₁, refMode₁),
  …,
  pₙ : SlotContent(VKₙ, refModeₙ),

  // qualifier kit (pattern-specific; relation specification selects subset)
  scope?       : SlotContent(U.Scope, ByValue | RefKind),
  Γ_time?      : SlotContent(U.GammaTimePolicy, ByValue), // time selector/policy; not an evidence freshness proxy
  viewpoint?   : SlotContent(U.Viewpoint, ByValue | RefKind),
  view?        : SlotContent(U.View, ByValue | RefKind),
  refScheme?   : SlotContent(U.ReferenceScheme, ByValue | RefKind),
  reprScheme?  : SlotContent(U.RepresentationScheme, ByValue | RefKind),

  witnesses?   : SlotContent(VK_wit, ByValue | RefKind)
⟩
```

**Slot naming guard.** `*Slot` suffix names positions (SlotKinds), not occupants; prose SHOULD use occupant names (`scope`, `witnesses`, `base`, `dependent`, …) for fillers. This is the same guard used in A.6.6 and A.6.5.

**Well‑formedness principle.** The record is typed by the relation specification: SlotSpecs are fixed by the selected RelationKind token, and missing slots are permitted only if the relation specification says they are optional. This mirrors A.6.6’s scoped/witnessed declaration move (SWBD): “shape + relation specification makes a concrete typed signature”.

**Well‑formedness constraints (non‑deontic).**

* **WF‑A6P‑QR‑1 (Required slots are present).** For any QualifiedRelationRecord `r` with `r.relationKind = k`, `r` provides values for every SlotSpec that `k` marks as required.
* **WF‑A6P‑QR‑2 (No silent kind swap).** `relationKind` is part of a record’s identity/edition boundary. If the kind changes, the result is represented as a distinct record/edition linked by an explicit `changeRelationKind` (or an explicit withdrawal + re‑declaration), not as an in-place mutation that preserves identity.

**Normative prose forms (Tech).**
In Tech/normative prose, authors SHALL express an in‑scope relation instance in one of the following equivalent forms:

* **Functional form:** `relationKind(p₁=…, …, pₙ=…, qualifiers…)`
* **Arrow form (binary projection only):** `p_left --relationKind{qualifiers}--> p_right`

Passive umbrella voice (“X is synced/linked/anchored …”) is permitted only as Plain gloss when immediately rewritten into one of the above forms.

**Cross-Context or cross-plane note (recipe-level).**
If any participant/qualifier implies cross‑Context or cross‑plane reuse, the L/A/D/E-classified claim bundle MUST cite the relevant Bridge ids + CL policy (and loss notes, when applicable) in the appropriate L/A/D/E-classified claims (typically `A-*` and/or `E-*`). Label identity is not an admissible substitute.

#### A.6.P:4.4 — Change‑class lexicon (operations are not adjectives)

A RPR‑pattern SHALL publish a **relation‑change lexicon**: a small set of semantic change classes used in normative prose to describe “what changed” without umbrella verbs.

Minimum semantic change classes (conceptual; specialisations may add more):

1. **declareRelation** — mint a new qualified relation record (slot‑explicit).
2. **withdrawRelation** — retire a relation instance (render it inactive for downstream use). If the intent is narrowing (still valid within a smaller scope/window), use `rescope`/`retime` rather than overloading withdrawal.
3. **retargetParticipant(slotKind, newRef)** — change a RefKind slot-content while preserving SlotKind and ValueKind (conceptually corresponds to slot‑level **retarget**).
4. **reviseByValue(slotKind, newValue)** — edit embedded by‑value content (conceptually corresponds to slot‑level assign/update or “by‑value edit”).
5. **rescope(newScope)** — change scope explicitly (no “in our context” prose).
6. **retime(newΓ_time)** — change `Γ_time` when time matters; not a substitute for witness freshness claims.
7. **refreshWitnesses(newWitnessSet)** — update witness bindings to point at appropriate carriers; generating evidence is Work, not a constructor op.
8. **changeRelationKind(newRelationKindToken)** — semantic change; MUST NOT be treated as an edit‑in‑place.

**Edition fence rule (A.6.S / A.6.6 alignment).**
In decision/publication lanes, any semantic change that alters meaning SHALL be represented as a new edition and connected via explicit continuity/withdrawal, rather than mutating the old record in place.

**Mapping note (informative, conceptual).**
These change classes are semantic; they may be realised by A.6.5 slot verbs (retarget vs by‑value edit) and, when the relation is a basedness family, by A.6.6 base‑change verbs. The semantic story must not collapse into “we edited something”.

#### A.6.P:4.5 — Lexical guardrails (ban umbrella metaphors as meaning‑surrogates)

A RPR‑pattern SHALL define **red‑flag umbrella tokens** for its ambiguity cluster, and SHALL provide canonical rewrite forms.

Normative base rules (suite-level):

* In **Tech / normative prose**, umbrella predicates (e.g., “same”, “synced”, “linked”, “connected”, “anchored/grounded”) MUST NOT substitute for an unnamed RelationKind token.
* **“bind/binding” is reserved for name binding** (Identifier → SlotKind/slot‑instance) and MUST NOT be used as a synonym for declaring/changing a relation instance. Use the change‑class lexicon instead.
* Pattern-defined carve‑outs MAY exist (reserved primitives elsewhere), but they remain review triggers to ensure the reserved sense is intended (as in A.6.6’s `anchor*` carve‑out rule).

**Recommended publication move (no extra authoring apparatus implied).** For stable ambiguity clusters, publish the red‑flag token list and canonical rewrites as a LEX‑BUNDLE entry (PTG=Guarded) and, when the cluster introduces new `RelationKind` tokens or stable facet head phrases, include them in the relevant UTS rows (F.17). This keeps rewrite discipline shareable outside the A.6 cluster.

#### A.6.P:4.5a - Trigger-word family split for discoverability vocabulary

The overloaded trigger-word family `discoverability` is not collapsed into one
universal substantive pattern.
`A.6.P`, `F.18`, and `E.10` govern the repair-side trigger-word, naming, collision, and
split-classification discipline for discoverability vocabulary.

For this amendment, route the settled jobs like this:

* description recognition signatures in general -> `A.6.RSIG`;
* pattern-entry discoverability -> `E.11`;
* Problem-frame recognition signatures -> `E.8`;
* worked entry readings -> `I.2`;
* entry lexeme support -> `F.17, F.18, and E.10`.

`A.6.P` therefore repairs the overloaded trigger-word side of the vocabulary.
It does not govern the substantive pattern bodies for description recognition,
pattern-entry discoverability, local recognition form, worked-entry depth, or
entry-lexeme support.

#### A.6.P:4.6 — Progressive elaboration (the “precision dial” rule)

A.6.P supports a controlled escalation path that preserves meaning and prevents drift:

1) Start with a minimal explicit **RelationKind token** + principal endpoints (a binary projection is allowed only if every omitted participant/qualifier slot is declared optional by the relation specification *and* irrelevant for the downstream lane(s)).

2) When ambiguity emerges, **do one (or more) explicitly**:
   * add missing participants as additional slots (turn the projection into n‑ary),
   * add explicit qualifiers: scope, `Γ_time`, viewpoint or view, reference or representation schemes, and witnesses,
   * refine the RelationKind token to a more specific one (new relation specification skeleton; `changeRelationKind`),
   * introduce Bridges + CL (and loss notes) when crossing Contexts/planes.

3) Authors MUST keep the transition monotone:
   * no silent re‑typing,
   * no implicit polarity flips,
   * no “edit‑in‑place” that changes meaning (use edition fences + explicit continuity/withdrawal links).

#### A.6.P:4.7 — Two-view and polarity discipline (no silent role flips)

A RPR‑pattern SHALL specify how the same relation is expressed from both “sides” without polarity flips:

* Either keep both endpoints visible with the same polarity-preserving token, **or**
* declare explicit inverse tokens and require them for inverse prose.

Implicit role flips (“B validates A” without explicit inverse) are prohibited in Tech/normative prose. This is already a core rule for basedness patterns and is generalised here.

#### A.6.P:4.8 — Disambiguation guide (rewrite/selection)

A RPR‑pattern SHALL include an actionable guide:

> “If the draft says *X*, decide between relation kinds A/B/C, expand missing slots, and rewrite into explicit kind+slots notation.”

For basedness families, A.6.6 provides an existence proof of such a guide (select baseRelation family; add scope/time/witnesses). A.6.P requires this move suite‑wide.

**Recommended format: RPR‑Disambiguation Guide (Winograd‑style, but ontology‑first).**
To keep disambiguation from collapsing into dictionary debates, present the guide as a compact decision scaffold:

* **trigger form** → **candidate RelationKinds / candidate facets (kinds)** → **discriminating questions/tests** → **canonical rewrite(s)** → **L/A/D/E L/A/D/E hooks**

Rules for the guide:

* Triggers may be **relation umbrellas** (“same/synced/linked/anchored…”) *or* **participant umbrellas** (pronominal/metonymic/over‑broad kind tokens). The guide SHALL state which role(s) the trigger is standing in for (relation kind, endpoint kind, qualifier, mediator).
* Candidate sets SHALL be stated as **kinds/facets/RelationKind tokens**, not as synonym lists. “Service” ⇒ {promise content, access point, provider principal, commitment, work+evidence, …} is the archetype (A.6.8).
* When endpoint‑side ambiguity is present, the guide SHOULD recommend producing a **Candidate‑Set Note** (A.6.P:4.0b) as part of the rewrite, so the chosen facet/kind is reviewable.
* Discriminating questions SHOULD be phrased as small **tests** that map directly to slot requirements (e.g., “Can you call it?” ⇒ `accessPointRef`; “Is it deontic?” ⇒ `commitmentRef` + accountable principal; “Is it actuals?” ⇒ `deliveryWorkRef` + witnesses).
* Canonical rewrites SHALL land in the A.6.P Tech forms (functional/arrow) and SHALL specify any newly required qualifiers (scope, Γ_time, `U.Viewpoint` and `U.View`, schemes, witnesses).
* Routing hooks SHALL name which claim(s) are expected in each quadrant (L/A/D/E) so that “unpacking” reliably produces reviewable obligations rather than prose paraphrases.

**Mini-row (metonymy; endpoint-side trigger, illustrative).**

`"at the table"` → `{PlaceRef(Table#7), MeetingRef(NegotiationSession#3), RoleRef(DecisionMakerSeat#2)}` → tests `{Is the claim about physical location? about participation? about accountable role? which carrier-anchored witnesses exist (badge/access log, calendar invite, minutes/recording)?}` → rewrite `{locatedAt(personRef=…, placeRef=…, Γ_time=…, witnesses=…) | participatesInMeetingUnder(personRef=…, meetingRef=…, roleRef?=…, Γ_time=…, witnesses=…)}` → L/A/D/E hooks `{L: publish RelationKind tokens + SlotSpecs + polarity/inverses; A: decision/publication use requires explicit Γ_time + witness set; D: forbid metonymic endpoint spans in Tech prose (require explicit refs); E: cite carrier-anchored witnesses and their observation conditions}`.

#### A.6.P:4.9 — A.6.B classification template for RPR relation families

Any RPR‑pattern that claims boundary-bearing relation semantics SHALL classify its normative content using **A.6.B**:

* **L‑claims**: signature‑level structure and invariants/rules (SlotSpecs, polarity, invariants).
* **A‑claims**: admissibility / “entry gate” rules for *using* relation instances in specified lanes (e.g., decision use requires witnesses; time dependence requires `Γ_time`; cross‑Context use requires Bridges/CL).
* **D‑claims**: deontic obligations on authors/agents (lexical firewall; prohibited umbrella use; rewrite obligations).
* **E‑claims**: work/evidence expectations and carrier anchoring (what counts as a witness; evidence freshness is a property of carriers, not prose).

A.6.P does not mandate a particular claim‑ID format; it mandates the **separation and cross‑reference discipline**.

**Atomicity + explicit references (normative, recipe-level).**
Per A.6.B, mixed sentences MUST be decomposed into **atomic** claims so each claim belongs to exactly one quadrant, and any dependencies MUST be expressed as explicit references (by claim ID or canonical location), not paraphrased duplicates.

**No upward dependencies (normative, recipe-level).**
`L-*` claims MUST NOT reference `A-*`, `D-*`, or `E-*`; `A-*` and `E-*` claims MUST NOT reference `D-*`. Where cross‑quadrant coupling is needed, link by explicit IDs in the allowed directions.

#### A.6.P:4.10 — A.6.S compatibility note (ConstructorSignature is optional but canonical for engineered families)

If an RPR‑pattern is applied as an engineered family (created/evolved over time), it SHOULD be expressible as:

* a **TargetSignature**: declared relation kinds + SlotSpecs + invariants/rules, and
* a minimal **ConstructorSignature**: effect‑free operations that rewrite under‑specified prose into the explicit form and evolve relation records using the change‑class lexicon (mapped to A.6.5/A.6.6 canonical verbs).

If a ConstructorSignature is provided, it SHOULD (conceptually) declare, for each constructor operator family:

* whether it is a species of **A.6.2 / A.6.3 / A.6.4**, and
* which **`U.EpistemeSlotGraph` slots** (C.2.1) it may read and write (SlotKind/ValueKind/RefKind profile).

**Publication note (recommended).**
If the TargetSignature or relation-kind registry is published via MVPK, treat every face as a **view** (no new semantics), keep viewpoint accountability explicit, and prefer stable claim IDs (Claim Register) so downstream carriers cite claims rather than paraphrasing.

### A.6.P:5 — Archetypal Grounding (System / Episteme)

A.6.P requires Tell–Show–Show grounding in both System and Episteme lanes.

#### A.6.P:5.1 — System archetype: “same system across environments”

**Tell.**
