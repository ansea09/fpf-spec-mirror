---
chunk_kind: "child"
pattern_id: "A.6.Q"
pattern_title: "U.QualityTermPrecisionRestoration — Quality Term Precision Restoration (Q-TERM)"
section_id: "A.6.Q:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.Q/A.6.Q__005_solution.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "A.6.Q — U.QualityTermPrecisionRestoration — Quality Term Precision Restoration (Q-TERM)"
  - "A.6.Q:4 — Solution"
line_start: 12873
line_end: 13241
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.17"
  - "A.18"
  - "A.2.6"
  - "A.6.A"
  - "A.6.B"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "C.25"
  - "E.17.0"
  - "E.17.2"
  - "F.9"
  - "F.9.1"
keywords:
  - "bridge reading"
  - "endpoint classification"
  - "evaluative ascription"
  - "language-state seam"
  - "quality senses"
  - "quality-term precision restoration"
---

### A.6.Q:4 - Solution

**Stable lens > Sense Family > Slots > Normal Form > Change Lexicon > Guardrails**

#### A.6.Q:4.0 - Trigger rule

A use of **quality** is in scope for A.6.Q when any of the following holds:

* the token **quality** or **high-quality / low-quality** appears in Tech or normative prose;
* a boundary statement relies on “quality” for admission, selection, explanation, comparison, assurance, or requirement-setting;
* different traditions are compared using the same word *quality*;
* a draft introduces *quality metric*, *quality score*, *quality characteristic*, *quality requirement*, *model quality*, *architecture quality*, *solution quality*, or *quality in QD* without a declared sense;
* the author intends the word to carry more than one of: evaluative fit, measurable characteristic, bundle, utility, or optimization objective.

#### A.6.Q:4.0a - Operational repair sequence

When the trigger fires, authors SHOULD follow the A.6.P operational repair path:

1. **Capture the trigger span.**
   Copy the exact trigger phrase using *quality* (or a red-flag derivative such as *high-quality*, *quality metric*, *quality characteristic*, *model quality*).

2. **Reconstruct the candidate set.**
   Enumerate plausible candidate senses and, when relevant, candidate endpoint governing FPF patterns or `authoritySourceRef` targets plus bearer lanes/facets (A.7: `Object | Description | Carrier`).
   If the occurrence is decision-bearing or publication-bearing, record this as a short **Candidate-Set Note** before selecting a repair.

   **Collision note.**
   This **Candidate-Set Note** is a local RPR disambiguation record for `quality` repairs; it is **not** the F.18 naming-process candidate set.

2a. **Check for an out-of-family affordance reading.**
   If the occurrence is primarily about an **action invitation** rather than an evaluative ascription, do **not** force a `QualitySense`.
   Classify it with `changeRelationKind(...)` into the appropriate relation family and treat the quality token as token-under-discussion only.

3. **Select one explicit quality sense.**
   Pick one `QualitySense` token and state why rival senses were rejected in this local context.

4. **Emit an endpoint-explicit or transitional rewrite.**
   Rewrite the sentence either into one explicit endpoint-pattern-governed evaluative form (`Characteristic | Q-Bundle | Objective | ExplanatoryMeritBundle | selector-value endpoint`) or, when endpoint choice is still being stabilized, into one explicit `evaluativeAscription(...)` transitional record with bearer, frame, evaluator/viewpoint, normal form, and explicit qualifiers.
5. **Classify boundary-bearing consequences.**
   If the repaired statement is used for admissibility, commitments, publication, or evidence-bearing decisions, classify the resulting `L/A/D/E` hooks with A.6.B instead of letting “quality” carry the required support by itself.

#### A.6.Q:4.1 - Transitional lens: evaluative classification anchored by `evaluativeAscription(...)`

A.6.Q stabilises the ambiguity cluster by treating every in-scope quality statement as **explicit evaluative content that must name the endpoint governing pattern or publication with named authority-reference relation that carries it**, not as a bare adjective.
`evaluativeAscription(...)` remains the canonical **transitional/metalinguistic repair record** when the endpoint choice is not yet fixed, but it is not the universal resting place.
Entry into A.6.Q therefore presupposes enough local `AE` to name the bearer, the frame, and at least one candidate evaluative family explicitly. `CD` may remain low while `evaluativeAscription(...)` is still serving as a transitional record, but if the content is still only a cue pack, a routed cue, or an open explanatory probe, it SHOULD remain in `A.16.1` / `B.4.1` / `B.5.2.0` rather than being published here prematurely. If a previously published evaluative record later loses the support needed to keep even that transitional status live, retreat via `A.16.2`.
In A.6.P terms, this pattern fixes one classification discipline plus one canonical transitional relation family:

* **`evaluativeAscription`** — the explicit transitional relation kind for “X has quality / quality improved / high-quality / quality in QD / quality characteristic / model quality” rewrites while preparing handoff to a more specific endpoint governing pattern or publication with named authority-reference relation.
#### A.6.Q:4.1a - RelationKind specification skeleton for `evaluativeAscription`

The family-specific `RelationKind` token is **`evaluativeAscription`**.
Its relation specification publication SHALL declare, at minimum:

* **(L)** applicability of the token in the local Context or plane set;
* **(L)** bearer-centred polarity (the bearer is the evaluated participant; inverse prose SHALL NOT silently swap bearer and evaluator);
* **(L)** participant SlotSpecs for bearer, sense, evaluation-frame, evaluator, and normal-form positions;
* **(A)** repair paths for bearer-kind mismatches: explicit narrowing, `KindBridge`, and/or explicit `retargetBearer(...)`;
* **(L)** qualifier expectations for `scope`, `Γ_time`, `viewpoint`, `view`, `referencePlane`, `refScheme`, `reprScheme`, `representationSubstrate`, and `bridgeRef`;
* **(D)** qualifier-placement discipline: frame/scope/time MUST NOT be smuggled into adjectives such as *high-quality*;
* **(A/E)** witness discipline for decision/publication lanes;
* **(L/A)** admissible semantic change classes and their edition-fence expectations;
* **(A/E)** cross-context and cross-plane policy when actual reuse is claimed (Bridge id + CL/loss-note policy).

Each in-scope occurrence SHALL be representable as a pattern-specific **QualifiedRelationRecord**:

```text
evaluativeAscriptionRecord :=
⟨
  relationKind            : evaluativeAscription,
  bearerTuple             : …,
  qualitySense            : QualitySense,
  evaluationFrame         : …,
  evaluator?              : …,
  viewpoint?              : U.Viewpoint,
  view?                   : U.View,
  referencePlane?         : ReferencePlane,
  refScheme?              : U.ReferenceScheme,
  reprScheme?             : U.RepresentationScheme,
  normalForm              : SignalPack | Characteristic | Bundle | Objective,
  scope?                  : U.Scope,
  Γ_time?                 : U.GammaTimePolicy,
  representationSubstrate?: embodied-kinesthetic | latent-distributed | symbolic-local | hybrid,
  bridgeRef?              : BridgeId,
  witnesses?              : EvidenceRefSet
⟩
```

So the sentence “X has quality” is never accepted as a terminal form.
It must be rewritten either into an explicit endpoint-pattern-governed evaluative form or into an explicit `evaluativeAscription(...)` transitional record with a declared endpoint governing pattern or publication with named authority-reference relation.

**Discipline note.**
`QualitySense` is a **slot value inside** the transitional relation family; it is not a replacement for the endpoint governing FPF pattern or `authoritySourceRef` target.
The stable intermediate lens is the ascription relation; the sense token refines **what kind of evaluative ascription** is being made while the endpoint target remains explicit.

**Separation note.**
`evaluator` and `viewpoint` are not synonyms.
When both matter, they SHALL be published separately: the evaluator is the observing / criticising / selecting party or policy, while the viewpoint is the declared `U.Viewpoint` under which the ascription is presented.
#### A.6.Q:4.1b - Polarity discipline (bearer-centred; no silent inverse)

`evaluativeAscription` is bearer-centred.
Tech / normative prose SHALL keep the evaluated participant in the bearer position and SHALL publish evaluator/viewpoint separately.

* “Architects rate the system highly” rewrites to `evaluativeAscription(bearer=System, evaluator=ArchitectureReviewBoard, …)`.
* “The benchmark says model quality is high” rewrites to `evaluativeAscription(bearer=Model, evaluator=BenchmarkPolicy, …)`.

There is no inverse token that silently makes the evaluator the bearer.
If inverse wording is used in Plain prose, authors SHALL rewrite it into the bearer-centred form (or mint an explicit inverse RelationKind token and publish its polarity specification).

#### A.6.Q:4.1c - Endpoint-first discipline

When the admissible endpoint governing FPF pattern or `authoritySourceRef` target is already known, authors SHOULD publish the endpoint-pattern-governed evaluative form directly and use `evaluativeAscription(...)` only when preserving the transitional ambiguity is itself informative. `evaluativeAscription(...)` is therefore a classification record, not a shadow endpoint source.

Typical direct endpoints are:

* engineering `-ility` heads published as one `Characteristic` or one `Q-Bundle`,
* selector-context uses published as an `Objective` headed by `QS.UseValue` unless overridden explicitly,
* architecture-description uses published under the description-side evaluative head already selected by the viewpoint bundle,
* explanatory-merit uses published under the explicit merit bundle when that bundle head is already known.

#### A.6.Q:4.2 - Core construct: `QualitySense`

Every in-scope use SHALL resolve to an explicit **`QualitySense` token**.

A `QualitySense` token publishes at least:

```text
QualitySense :=
  ⟨
    senseId,
    bearerArity,
    articulationMode,
    representationSubstrate,
    defaultNormalForm,
    admissibleNormalForms,
    evaluationFrameKind,
    admissibleEvidenceModes,
    admissibleChangeClasses,
    bridgePolicy
  ⟩
```

Where:

* **`articulationMode`** ∈
  `{ preconceptual, exemplar-grounded, proxy-grounded, characteristic-bound, bundle-bound, objective-bound }`
* **`representationSubstrate`** ∈
  `{ embodied-kinesthetic, latent-distributed, symbolic-local, hybrid }`
* **`defaultNormalForm`** ∈
  `{ SignalPack, Characteristic, Bundle, Objective }`
* **`admissibleNormalForms`** is the explicitly declared set of admissible publication forms for the sense.
  `defaultNormalForm` names the primary publication form; any additional forms MUST be declared here rather than inferred ad hoc.

#### A.6.Q:4.3 - Normative starter set of sense families

A Context MAY add local senses, but the following starter set is normative as the initial disambiguation menu:

| `QualitySense` token               | Use when “quality” means…                                                                                      | Default normal form | Typical substrate                | Must **not** be silently collapsed into                                    |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------: | -------------------------------- | -------------------------------------------------------------------------- |
| `QS.PreconceptualFit`              | preconceptual fit, felt rightness, “quality before definition”, kinesthetic/embodied salience                |         `SignalPack` | `embodied-kinesthetic` or `hybrid` | Characteristic, utility, fitness score                                     |
| `QS.PhenomenalCharacter`           | phenomenal character / qualia / felt characteristic when the experienced quality itself is described          |         `SignalPack` | `embodied-kinesthetic` or `hybrid` | `QS.PreconceptualFit`, engineering quality, utility                        |
| `QS.LatentFit`                     | distributed fit/tension in learned representations, world models, probes, prediction structures              |         `SignalPack` | `latent-distributed` or `hybrid` | `QS.PreconceptualFit`, engineering quality, explanatory merit              |
| `QS.ExplanatoryMerit`              | epistemic merit of an explanation, conjecture, problem frame, or theory                                      |             `Bundle` | `symbolic-local` or `hybrid`     | engineering `-ilities`, use-value                                          |
| `QS.ArchitecturalDescriptionFitness` | task-fit / compression merit of an architecture description, architecture model, or viewpoint bundle as a description of structure for downstream reasoning |             `Bundle` | `symbolic-local` or `hybrid`     | `QS.EngineeringQualityFamily`, `QS.ExplanatoryMerit`, publication polish   |
| `QS.EngineeringQualityFamily`      | reliability/availability/security/maintainability/evolvability/usability/etc.                                |             `Bundle` | `symbolic-local` or `hybrid`     | function/capability statements, preconceptual fit                          |
| `QS.UseValue`                      | usefulness of a candidate under a declared goal/CG-frame; the “Q” head in NQD/QD by default                  |          `Objective` | `symbolic-local` or `hybrid`     | engineering quality family, explanatory merit                              |
| `QS.ControlAdequacy`               | adequacy of a policy/model/controller in a closed action loop                                                |             `Bundle` | `hybrid`                         | bare model “quality”, felt fit                                             |

**Default-form note.**
`QS.EngineeringQualityFamily` and `QS.ControlAdequacy` default to `Bundle`.
A local Context MAY operationalize one explicit head as a `Characteristic`, but that is a declared operationalization, not a second default normal form.

**Normative rewrite note.**

* In **NQD / QD / selector** contexts, bare *quality* SHALL rewrite to **`QS.UseValue`** unless a different `QualitySense` is explicitly declared.
* In **engineering** contexts, bare *quality* SHALL rewrite either to:

  * one explicit **`U.Characteristic` + CSLC Scale**, or
  * one explicit **`Bundle`**, preferably authored as a **`Q-Bundle`** when composite.
* In **phenomenological** contexts, bare *quality* SHALL rewrite to **`QS.PhenomenalCharacter`** when the experienced quality itself is the topic of description, and to **`QS.PreconceptualFit`** when the talk is about preconceptual fit / felt rightness before stable characterisation.
* In **representation-learning / world-model** contexts, bare *model quality* SHALL rewrite to **`QS.LatentFit`** and/or **`QS.ControlAdequacy`**, with the distinction made explicit.
* In **epistemic evaluation** contexts, “good explanation” SHALL rewrite to **`QS.ExplanatoryMerit`**.
* In **architecture-description fitness or viewpoint** contexts, bare *architecture quality* or *architectural quality* SHALL first disambiguate the bearer lane: if the bearer is the described system, use **`QS.EngineeringQualityFamily`**; if the bearer is the description or episteme, use **`QS.ArchitecturalDescriptionFitness`**.

#### A.6.Q:4.4 - Required slots for a conforming `evaluativeAscription`

A conforming `evaluativeAscription` SHALL make explicit:

1. **Bearer tuple.**
   What is being evaluated, with arity explicit.

2. **`QualitySense`.**
   Which evaluative family is intended.

3. **Evaluation frame.**
   The criterion-basis under which the ascription is made.
   Examples: exemplar pack, probe pack, criticism/test pack, Q-bundle definition, CG-frame, acceptance spec, control horizon.

4. **Evaluator or viewpoint.**
   State the evaluator (observer, critic, selector policy, stakeholder family, or review body) and, when relevant, the `U.Viewpoint`, separately.
   The two SHALL NOT be silently collapsed when they differ.

5. **Normal form.**
   Whether the ascription is published as `SignalPack`, `Characteristic`, `Bundle`, or `Objective`.

6. **Scope and time when relevant.**
   The relevant USM scope (`U.ClaimScope`, `U.WorkScope`, `U.PublicationScope`, or generic `U.Scope`) and `Γ_time` SHALL be explicit when omission changes meaning.
   Freshness windows, qualification windows, or evidence decay windows SHALL be declared in the appropriate evidence or capability lane rather than smuggled into “quality” as an adjective.

7. **Reference plane when relevant.**
   Especially when the same trigger phrase can refer to the described entity, its description, its carrier, or a publication face under a different `ReferencePlane`.

8. **Reference / representation scheme when relevant.**
   Especially when the ascription depends on a declared reference scheme, representation scheme, or viewpoint-specific decoding convention.

9. **Representation substrate when relevant.**
   Especially when discussing parallels between preconceptual, latent-distributed, and symbolic-local treatments.

10. **Witness / evidence mode.**
   Exemplars, probes, measurements, bundle members, tests, traces, or closed-loop performance carriers.

#### A.6.Q:4.5 - Normal-form discipline

A `QualitySense` SHALL declare one admissible **default** normal form and MAY declare additional admissible normal forms explicitly.

**QNF-1 — `SignalPack`.**
Use for `QS.PhenomenalCharacter`, `QS.PreconceptualFit`, and many cases of `QS.LatentFit`.

A conforming `SignalPack` publishes:

* exemplar/contrast set or probe set,
* articulation notes,
* source episode, carrier, and observer,
* optional ordinal or thresholded summaries,
* explicit warning that the signal is **not** yet a `Characteristic` unless an admissible proxy is later declared.

**QNF-2 — `Characteristic`.**
Use only when the sense is truly one measurable characteristic on one declared scale.
This routes through **A.17/A.18/C.16** and inherits full scale legality.

**QNF-3 — `Bundle`.**
Use when the sense is composite.
Typical for `QS.ExplanatoryMerit`, many engineering quality families, and `QS.ControlAdequacy`.

A conforming bundle publishes:

* member heads,
* whether each head is Characteristic / status / mechanism / scope / test,
* aggregation policy if any,
* prohibition on hidden scalarisation.

**Engineering note.**
For engineering `-ility` families, the preferred bundle form is **`Q-Bundle`** (C.25), because it keeps **Measures[CHR]** distinct from **ClaimScope/WorkScope** and from **Mechanisms/Status**.
`Q-Bundle` is a **C.25 authoring profile of `Bundle`**, not a fifth normal form beside `SignalPack | Characteristic | Bundle | Objective`.
Do not publish a free-floating bundle with hidden metric semantics.

**QNF-4 — `Objective`.**
Use for `QS.UseValue` in selection/generation/search contexts.

A conforming objective publishes:

* CG-frame / objective `authoritySourceRef` target,
* admissible comparators,
* acceptance / selector policy,
* reference plane and window,
* relation to novelty/diversity/constraints.

#### A.6.Q:4.6 - Functional vs quality-family discipline

A.6.Q SHALL prevent the collapse of **function/capability** claims into **quality-family** claims.

* A statement about **what a system does** belongs to functional/procedural description.
* A statement about **how well / how safely / how robustly / how maintainably** it does so belongs to `QS.EngineeringQualityFamily`.
* “Quality characteristic” and “functional characteristic” SHALL NOT be used as interchangeable labels.
* In engineering contexts, `-ility` names are **quality-family labels**, not automatically Characteristics.
  They become admissible only as one explicit `U.Characteristic` or one explicit `Bundle` (preferably authored as `Q-Bundle` when composite).
* Cross-references are allowed; category collapse is not.

#### A.6.Q:4.7 - Bridge discipline across traditions

Whenever two different traditions are compared using the word *quality*, the author SHALL publish an explicit **bridge stance** and loss note.

Allowed bridge stances:

* **`localRename`** — near-synonymous within one Context.
* **`operationalizes`** — one sense is turned into a proxy or measurable form.
* **`partialAnalogy`** — structurally similar but not identical.
* **`projection`** — one richer sense is projected into a narrower evaluative frame.
* **`nonEquivalent`** — same word, no admissible bridge asserted.

Examples:

* `QS.PreconceptualFit` - `QS.LatentFit` is usually `partialAnalogy`, not identity.
* `QS.PreconceptualFit` - `QS.PhenomenalCharacter` is usually a progression-by-articulation relation, not identity.
* `QS.PreconceptualFit` > engineering measures is usually `operationalizes` or `projection`, with loss notes.
* `QS.EngineeringQualityFamily` > `QS.UseValue` is usually `projection` under a CG-frame.
* `QS.ExplanatoryMerit` - `QS.UseValue` is **not** identity unless a Context explicitly defines such a projection.
* Pirsig-style **dynamic quality** usually applies `QS.PreconceptualFit` (sometimes `QS.LatentFit`) only as `localRename` / `partialAnalogy` under a declared `U.BoundedContext`; it is not identity by label.
* Pirsig-style **static quality** usually applies `Characteristic` or `Bundle` publication under some other declared sense; it is not identity with dynamic quality.
* `QS.ArchitecturalDescriptionFitness` - `QS.EngineeringQualityFamily` is usually `projection` or `nonEquivalent` unless the Context explicitly states which heads of description-fitness are intended to proxy which system-side characteristics.

#### A.6.Q:4.8 - Change lexicon

A conforming pattern SHALL narrate changes with a stable change lexicon aligned to A.6.P:

* **`declareevaluativeAscription(...)`** — create a new explicit quality ascription record.
* **`withdrawevaluativeAscription(...)`** — retire a prior record.
* **`retargetBearer(...)`** — change the evaluated bearer tuple while keeping the same relation family.
* **`reviseSense(...)`** — change the value in the `qualitySense` slot.
* **`reArticulate(...)`** — change `articulationMode` while preserving sense family.
* **`reProxy(...)`** — change proxy/probe/operationalisation details.
* **`reBundle(...)`** — change bundle members or aggregation policy.
* **`reScale(...)`** — change characteristic scale or scale type.
* **`reFrame(...)`** — change evaluation frame.
* **`reView(...)`** — change evaluator/viewpoint.
* **`rescope(...)`** — change `U.Scope`.
* **`retime(...)`** — change `Γ_time`.
* **`refreshWitnesses(...)`** — refresh evidence or witness bindings.
* **`changeRelationKind(...)`** — semantic move to a different relation family; never edit in place silently.

A silent **sense rewrite** is a breaking semantic change.
If the ascription ceases to mean “quality ascription” at all, use `changeRelationKind(...)` rather than pretending the same record survived unchanged.

**A.6.P rewrite note.**
`retargetBearer(...)` is the family-specific form of `retargetParticipant(BearerSlot, …)`.
`reviseSense(...)`, `reArticulate(...)`, `reProxy(...)`, `reBundle(...)`, `reScale(...)`, `reFrame(...)`, and `reView(...)` are family-specific refinements of `reviseByValue(...)` and SHALL preserve the A.6.5 distinction between ref retargeting and by-value edits.

#### A.6.Q:4.8a - A.6.B classification template for `evaluativeAscription`

When a repaired quality statement becomes boundary-bearing, classify it explicitly:

* **L** — `evaluativeAscription` relation specification skeleton, `QualitySense` semantics, normal-form admissibility, and declared bridge stances;
* **A** — admissibility conditions for using the ascription in selector, gating, and publication lanes (required qualifiers, witnesses, thresholds, qualification windows);
* **D** — author and publisher obligations (lexical firewall, mandatory rewrites, publication duties);
* **E** — carrier-anchored evidence/work effects (measurements, traces, critique sheets, probe packs, selector logs).

Where this family is published as a reusable boundary publication, authors SHOULD publish stable `L-Q*` / `A-Q*` / `D-Q*` / `E-Q*` claim ids (or explicitly cite the reused L/A/D/E-classified claim set by location) and SHALL avoid paraphrase drift across quadrants.
Do not let the bare word *quality* carry L/A/D/E force by itself.

#### A.6.Q:4.9 - Lexical guardrails

In **Tech / normative prose**:

* bare **quality** MUST NOT appear without immediate resolution to a `QualitySense`;
* **high-quality / low-quality / quality metric / quality score / quality requirement / model quality / architecture quality / solution quality** are red-flag tokens;
* **quality characteristic** MAY appear only as:

  * a bridge label to an external standard/tradition, or
  * a family label immediately rewritten into one explicit `U.Characteristic` or `Q-Bundle`;
* **quality requirement / quality requirements** MUST NOT remain bare noun phrases; authors SHALL rewrite them into explicit `RequirementRole` / `U.Commitment` / `U.PromiseContent.acceptanceSpec` structures over one named `U.Characteristic`, one `Q-Bundle` head, or one explicit objective head;
* **architecture quality / architectural quality** MUST NOT appear without an explicit bearer lane (`Object | Description | Carrier`) and, when omission changes meaning, an explicit `referencePlane`;
* in QD/NQD contexts, bare **quality** MUST default to **`QS.UseValue`**;
* preconceptual uses MUST NOT be presented as if they were already Characteristics;
* latent/distributed fit MUST NOT be presented as if it were automatically explanatory merit;
* if the occurrence is primarily **action-invitation** talk, authors MUST NOT force a `QualitySense`; they SHALL exit to the appropriate relation family;
* scope words (*applicability*, *envelope*, *generality*, *validity*) MUST NOT be used as hidden substitutes for `U.Scope`, `U.ClaimScope (G)`, or `U.WorkScope`;
* quoted metalinguistic uses of the token *quality* are allowed, but SHALL be marked as **token-under-discussion**, not as a boundary-bearing term.

#### A.6.Q:4.10 - Progressive elaboration

A.6.Q supports monotone elaboration:

1. Start by selecting a **`QualitySense`** and capturing rival candidates when ambiguity is live.
2. Declare bearer, frame, viewpoint, and substrate.
3. Choose an admissible **normal form**.
4. Add exemplars / probes / characteristic heads / bundle members / objective pins.
5. Add bridges and loss notes if comparing traditions.
6. If the repaired sentence is boundary-bearing, emit `L/A/D/E` L/A/D/E hooks rather than letting “quality” carry them implicitly.
7. Never move between sense families silently.

