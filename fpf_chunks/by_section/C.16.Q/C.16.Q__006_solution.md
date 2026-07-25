---
chunk_kind: "child"
pattern_id: "C.16.Q"
pattern_title: "Quality-Term Precision Restoration"
section_id: "C.16.Q:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.Q/C.16.Q__006_solution.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "C.16.Q — Quality-Term Precision Restoration"
  - "C.16.Q:4 — Solution"
line_start: 47179
line_end: 47533
dependencies:
  - "A.10"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2.6"
  - "A.6.A"
  - "A.6.B"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16"
  - "C.16.P"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "C.25"
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "E.17.2"
  - "E.21"
  - "E.8"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
---

### C.16.Q:4 - Solution

**Stable repair frame > Sense Family > Slots > Normal Form > Change Lexicon > Guardrails**

#### C.16.Q:4.0 - Trigger rule

A use of **quality** is in scope for C.16.Q when any of the following holds:

* the token **quality** or **high-quality or low-quality** appears in Tech or normative prose;
* a boundary statement relies on “quality” for admission, selection, explanation, comparison, assurance, or requirement-setting;
* different traditions are compared using the same word *quality*;
* a draft introduces *quality metric*, *quality score*, *quality characteristic*, *quality requirement*, *model quality*, *architecture quality*, *solution quality*, or *quality in QD* without a declared sense;
* the occurrence is intended to carry more than one of: evaluative fit, measurable characteristic, bundle, utility, or optimization objective.

#### C.16.Q:4.0a - Operational repair sequence

When the trigger fires, follow the `E.10.ARCH` recovery order specialized to quality-term or evaluative characterization:

1. **Capture the trigger span.**
   Copy the trigger phrase using *quality* or a red-flag derivative such as *high-quality*, *quality metric*, *quality characteristic*, or *model quality*.

2. **Recover the bearer and publication lane.**
   Name the bearer and the relevant A.7 lane or kind: EntityOfConcern being described, description, `episteme` or publication face, carrier when the carrier itself is evaluated, pattern, model, policy, explanation, candidate, architecture description, work result, relation, action loop, or ordinary prose.

3. **Reconstruct candidate quality senses and endpoint patterns.**
   Enumerate plausible candidate senses and, when relevant, candidate endpoint-governing FPF patterns or explicit endpoint source references. If the occurrence is decision-bearing, publication-bearing, or cross-tradition-bearing, record a short quality-term candidate note before selecting the repair.

4. **Exit when the claim being made is not quality-term or evaluative characterization.**
   If the occurrence is primarily action invitation, relation construction, bridge, basedness, endpoint mismatch, evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens use, characteristic and scale construction, or source-use, do not assign a `QualitySense`. Apply `A.6.P`, `A.6.A`, `C.16.P`, `C.29`, `C.2.P`, or the pattern governing the recovered claim.

5. **Select one explicit quality sense.**
   Pick one `QualitySense` token and state why rival senses were rejected in this local context.

6. **Emit an endpoint-explicit or transitional rewrite.**
   Rewrite the sentence either into one explicit endpoint-pattern-governed evaluative form (`Characteristic | Q-Bundle | Objective | ExplanatoryMeritBundle | selector-value endpoint`) or, when endpoint choice is still being stabilized, into one explicit `qualityTermAscription(...)` transitional repair form with bearer, frame, evaluator and viewpoint, normal form, and explicit qualifiers.

7. **Classify boundary-bearing consequences.**
   If the repaired statement is used for admissibility, commitments, publication, evidence-bearing decisions, gates, release, or work, apply the governing pattern instead of letting *quality* carry the required claim by itself.

#### C.16.Q:4.1 - Transitional repair frame: evaluative classification anchored by `qualityTermAscription(...)`

`C.16.Q` stabilizes the ambiguity cluster by treating every in-scope quality statement as explicit evaluative content that must name the endpoint governing pattern or publication with named authority-reference relation that carries it, not as a bare adjective.

`qualityTermAscription(...)` is the canonical transitional quality-term repair form when the endpoint choice is not yet fixed. It is not the universal resting place, not a relation kind by default, and not a shadow endpoint source.

Entry into `C.16.Q` presupposes enough articulation explicitness to name the bearer, evaluation frame, and at least one candidate evaluative family. Closure degree may remain low while `qualityTermAscription(...)` is serving as a transitional repair form, but if the content is still only a cue pack, forwarded cue, or open explanatory probe, keep it in `A.16.1`, `B.4.1`, or `B.5.2.0` rather than publishing it here prematurely. If a previously published evaluative record later loses the evidence, witness, or authority-reference relation needed to keep even that transitional status live, retreat via `A.16.2`.

The transitional form is:

```text
qualityTermAscription :=
{
  bearerTuple,
  qualitySense: QualitySense,
  evaluationFrame,
  evaluator?,
  viewpoint?: U.Viewpoint,
  view?: U.View,
  referencePlane?,
  refScheme?: U.ReferenceScheme,
  reprScheme?: U.RepresentationScheme,
  normalForm: SignalPack | Characteristic | Bundle | Objective,
  scope?: U.Scope,
  gammaTime?,
  representationSubstrate?: embodied-kinesthetic | latent-distributed | symbolic-local | hybrid,
  bridgeRef?,
  witnesses?,
  endpointGoverningPatternRef,
  admissibleUse,
  nonAdmissibleUse
}
```

So the sentence "X has quality" is never accepted as a terminal form. It must be rewritten either into an explicit endpoint-pattern-governed evaluative form or into this transitional repair form with a declared endpoint-governing pattern or explicit endpoint source relation.

**Discipline note.**
`QualitySense` is a slot value inside the transitional repair form; it is not a replacement for the endpoint FPF pattern or explicit endpoint source reference. The sense token refines what kind of evaluative characterization is being made while the endpoint source, governing pattern, or EntityOfConcern remains explicit.

**Separation note.**
`evaluator` and `viewpoint` are not synonyms. When both matter, publish them separately: the evaluator is the observing, criticizing, or selecting party or policy, while the viewpoint is the declared `U.Viewpoint` under which the ascription is presented.

#### C.16.Q:4.1b - Polarity discipline (bearer-centred; no silent inverse)

`qualityTermAscription` is bearer-centred.
Tech and normative prose SHALL keep the evaluated participant in the bearer position and SHALL publish evaluator and viewpoint separately.

* “Architects rate the system highly” rewrites to `qualityTermAscription(bearer=System, evaluator=ArchitectureReviewBoard, …)`.
* “The benchmark says model quality is high” rewrites to `qualityTermAscription(bearer=Model, evaluator=BenchmarkPolicy, …)`.

There is no inverse token that silently makes the evaluator the bearer.
If inverse wording is used in Plain prose, the wording SHALL be rewritten into the bearer-centred form (or publish an explicit inverse form under the pattern governing the recovered claim that governs it).

#### C.16.Q:4.1c - Endpoint-first discipline

When the admissible endpoint-governing FPF pattern or explicit endpoint source reference is already known, the endpoint-pattern-governed evaluative form SHOULD be published directly, and `qualityTermAscription(...)` SHOULD remain only when preserving the transitional ambiguity is itself informative. `qualityTermAscription(...)` is therefore a transitional characterization record, not a shadow endpoint source.

Typical direct endpoints are:

* engineering `-ility` heads published as one `Characteristic` or one `Q-Bundle`,
* selector-context uses published as an `Objective` headed by `QS.UseValue` unless overridden explicitly,
* architecture-description uses published under the description-side evaluative head already selected by the viewpoint bundle,
* explanatory-merit uses published under the explicit merit bundle when that bundle head is already known.

#### C.16.Q:4.2 - Core construct: `QualitySense`

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
* **`admissibleNormalForms`** is the explicitly declared set of admissible evaluative normal forms for the sense.
  `defaultNormalForm` names the primary evaluative normal form; any additional endpoint forms MUST be declared here rather than inferred ad hoc. If the quality ascription is published, route publication face, form, unit, carrier, and rendering questions to E.17, E.8, or the publication pattern governing the claim.

#### C.16.Q:4.3 - Normative starter set of sense families

A Context MAY add local senses, but the following starter set is normative as the initial disambiguation menu:

| `QualitySense` token               | Use when “quality” means…                                                                                      | Default normal form | Typical substrate                | Must **not** be silently collapsed into                                    |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------: | -------------------------------- | -------------------------------------------------------------------------- |
| `QS.PreconceptualFit`              | preconceptual fit, felt rightness, “quality before definition”, kinesthetic or embodied salience                |         `SignalPack` | `embodied-kinesthetic` or `hybrid` | Characteristic, utility, fitness score                                     |
| `QS.PhenomenalCharacter`           | phenomenal character, qualia, or felt characteristic when the experienced quality itself is described          |         `SignalPack` | `embodied-kinesthetic` or `hybrid` | `QS.PreconceptualFit`, engineering quality, utility                        |
| `QS.LatentFit`                     | distributed fit or tension in learned representations, world models, probes, prediction structures              |         `SignalPack` | `latent-distributed` or `hybrid` | `QS.PreconceptualFit`, engineering quality, explanatory merit              |
| `QS.ExplanatoryMerit`              | epistemic merit of an explanation, conjecture, problem frame, or theory                                      |             `Bundle` | `symbolic-local` or `hybrid`     | engineering `-ilities`, use-value                                          |
| `QS.ArchitecturalDescriptionFitness` | task-fit and compression merit of an architecture description, architecture model, or viewpoint bundle as a description of structure for downstream reasoning |             `Bundle` | `symbolic-local` or `hybrid`     | `QS.EngineeringQualityFamily`, `QS.ExplanatoryMerit`, publication polish   |
| `QS.EngineeringQualityFamily`      | reliability, availability, security, maintainability, evolvability, usability, and related engineering families                                |             `Bundle` | `symbolic-local` or `hybrid`     | function or capability statements, preconceptual fit                          |
| `QS.UseValue`                      | usefulness of a candidate under a declared goal or CG-frame; the “Q” head in NQD or QD by default                  |          `Objective` | `symbolic-local` or `hybrid`     | engineering quality family, explanatory merit                              |
| `QS.ControlAdequacy`               | adequacy of a policy, model, or controller in a closed action loop                                                |             `Bundle` | `hybrid`                         | bare model “quality”, felt fit                                             |

**Default-form note.**
`QS.EngineeringQualityFamily` and `QS.ControlAdequacy` default to `Bundle`.
A local Context MAY operationalize one explicit head as a `Characteristic`, but that is a declared operationalization, not a second default normal form.

**Normative rewrite note.**

* In **NQD, QD, or selector** contexts, bare *quality* SHALL rewrite to **`QS.UseValue`** unless a different `QualitySense` is explicitly declared.
* In **engineering** contexts, bare *quality* SHALL rewrite either to:

  * one explicit **`U.Characteristic` + CSLC Scale**, or
  * one explicit **`Bundle`**, preferably published as a **`Q-Bundle`** when composite.
* In **phenomenological** contexts, bare *quality* SHALL rewrite to **`QS.PhenomenalCharacter`** when the experienced quality itself is the topic of description, and to **`QS.PreconceptualFit`** when the talk is about preconceptual fit or felt rightness before stable characterisation.
* In **representation-learning and world-model** contexts, bare *model quality* SHALL rewrite to **`QS.LatentFit`**, **`QS.ControlAdequacy`**, or both, with the distinction made explicit.
* In **epistemic evaluation** contexts, “good explanation” SHALL rewrite to **`QS.ExplanatoryMerit`**.
* In **architecture-description fitness or viewpoint** contexts, bare *architecture quality* or *architectural quality* SHALL first disambiguate the bearer lane: if the bearer is the system-side bearer, use **`QS.EngineeringQualityFamily`**; if the bearer is the description or episteme, use **`QS.ArchitecturalDescriptionFitness`**.

#### C.16.Q:4.4 - Required slots for a conforming `qualityTermAscription`

A conforming `qualityTermAscription` SHALL make explicit:

1. **Bearer tuple.**
   What is being evaluated, with arity explicit.

2. **`QualitySense`.**
   Which evaluative family is intended.

3. **Evaluation frame.**
   The evaluation criterion or criterion frame under which the ascription is made.
   Examples: exemplar pack, probe pack, criticism or test pack, Q-bundle definition, CG-frame, acceptance spec, control horizon.

4. **Evaluator or viewpoint.**
   State the evaluator (observer, critic, selector policy, stakeholder family, or review body) and, when relevant, the `U.Viewpoint`, separately.
   The two SHALL NOT be silently collapsed when they differ.

5. **Normal form.**
   Whether the ascription is published as `SignalPack`, `Characteristic`, `Bundle`, or `Objective`.

6. **Scope and time when relevant.**
   The relevant USM scope (`U.ClaimScope`, `U.WorkScope`, `U.PublicationScope`, or generic `U.Scope`) and `Γ_time` SHALL be explicit when omission changes meaning.
   Freshness windows, qualification windows, or evidence decay windows SHALL be declared in the appropriate evidence or capability lane rather than smuggled into “quality” as an adjective.

7. **Reference plane when relevant.**
   Especially when the same trigger phrase can refer to the EntityOfConcern being described, its description, its carrier, or a publication face under a different `ReferencePlane`.

8. **Reference and representation scheme when relevant.**
   Especially when the ascription depends on a declared reference scheme, representation scheme, or viewpoint-specific decoding convention.

9. **Representation substrate when relevant.**
   Especially when discussing parallels between preconceptual, latent-distributed, and symbolic-local treatments.

10. **Witness and evidence mode.**
   Exemplars, probes, measurements, bundle members, tests, traces, or closed-loop performance carriers.

#### C.16.Q:4.5 - Normal-form discipline

A `QualitySense` SHALL declare one admissible **default** evaluative normal form and MAY declare additional admissible evaluative normal forms explicitly.

The normal forms in this section are endpoint or evaluative forms. They are not publication forms by themselves. Publication face, publication form, publication unit, carrier, rendering, export, and front-end questions remain with `E.17`, `E.8`, or the endpoint-governing publication pattern named by value.

**QNF-1 - `SignalPack`.**
Use for `QS.PhenomenalCharacter`, `QS.PreconceptualFit`, and many cases of `QS.LatentFit`.

A conforming `SignalPack` contains:

* exemplar or contrast set or probe set,
* articulation notes,
* source episode, carrier, and observer,
* optional ordinal or thresholded summaries,
* explicit warning that the signal is **not** yet a `Characteristic` unless an admissible proxy is later declared.

**QNF-2 - `Characteristic`.**
Use only when the sense is truly one measurable characteristic on one declared scale.
This uses **A.17, A.18, and C.16** and inherits full scale legality.

**QNF-3 - `Bundle`.**
Use when the sense is composite.
Typical for `QS.ExplanatoryMerit`, many engineering quality families, and `QS.ControlAdequacy`.

A conforming bundle contains:

* member heads,
* whether each head is Characteristic, status, mechanism, scope, or test,
* aggregation policy if any,
* prohibition on hidden scalarisation.

**Engineering note.**
For engineering `-ility` families, the preferred bundle endpoint is **`Q-Bundle`** (C.25), because it keeps **Measures[CHR]** distinct from **ClaimScope and WorkScope** and from **Mechanisms and Status**.
`Q-Bundle` is a **C.25-governed bundle endpoint** rather than a fifth normal form beside `SignalPack | Characteristic | Bundle | Objective`.
Do not use a free-floating bundle with hidden metric semantics.

**QNF-4 - `Objective`.**
Use for `QS.UseValue` in selection, generation, or search contexts.

A conforming objective contains:

* CG-frame or objective endpoint source reference,
* admissible comparators,
* acceptance or selector policy,
* reference plane and window,
* relation to novelty, diversity, and constraints.

#### C.16.Q:4.6 - Functional vs quality-family discipline

C.16.Q SHALL prevent the collapse of **function or capability** claims into **quality-family** claims.

* A statement about **what a system does** uses `A.6.F` first when function-like wording hides the FPF kind named by value, relation, or claim, then the pattern governing the recovered capability, method, work, role, `A.6.M` module-interface, architecture, mathematical, evidence, assurance, gate, decision, or release claim whose primary `EntityOfConcern`, bearer, relation record, or characteristic-space construction is recovered.
* A statement about **how well, how safely, how robustly, or how maintainably** it does so belongs to `QS.EngineeringQualityFamily`.
* “Quality characteristic” and “functional characteristic” SHALL NOT be used as interchangeable labels.
* In engineering contexts, `-ility` names are **quality-family labels**, not automatically Characteristics.
  They become admissible only as one explicit `U.Characteristic` or one explicit `Bundle` (preferably expressed through `Q-Bundle` when composite).
* Cross-references are allowed; category collapse is not.

#### C.16.Q:4.7 - Bridge discipline across traditions

Whenever two different traditions are compared using the word *quality*, the repair SHALL publish an explicit **bridge stance** and loss note.

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
* Pirsig-style **dynamic quality** usually applies `QS.PreconceptualFit` (sometimes `QS.LatentFit`) only as `localRename` or `partialAnalogy` under a declared `U.BoundedContext`; it is not identity by label.
* Pirsig-style **static quality** usually applies `Characteristic` or `Bundle` publication under some other declared sense; it is not identity with dynamic quality.
* `QS.ArchitecturalDescriptionFitness` - `QS.EngineeringQualityFamily` is usually `projection` or `nonEquivalent` unless the Context explicitly states which heads of description-fitness are intended to proxy which system-side characteristics.

#### C.16.Q:4.8 - Change lexicon

A conforming quality-term repair publication SHALL narrate changes with a stable change lexicon aligned to A.6.P:

* **`declareQualityTermAscription(...)`** — create a new explicit quality ascription record.
* **`withdrawQualityTermAscription(...)`** — retire a prior record.
* **`retargetBearer(...)`** — change the evaluated bearer tuple while keeping the same quality-term repair form.
* **`reviseSense(...)`** — change the value in the `qualitySense` slot.
* **`reArticulate(...)`** — change `articulationMode` while preserving sense family.
* **`reProxy(...)`** — change proxy, probe, or operationalisation details.
* **`reBundle(...)`** — change bundle members or aggregation policy.
* **`reScale(...)`** — change characteristic scale or scale type.
* **`reFrame(...)`** — change evaluation frame.
* **`reView(...)`** — change evaluator and viewpoint.
* **`rescope(...)`** — change `U.Scope`.
* **`retime(...)`** — change `Γ_time`.
* **`refreshWitnesses(...)`** — refresh evidence or witness bindings.
* **`assignToGoverningPattern(...)`** — semantic move to a non-quality governing pattern; never edit in place silently.

A silent **sense rewrite** is a breaking semantic change.
If the ascription ceases to mean “quality ascription” at all, use `assignToGoverningPattern(...)` rather than pretending the same record survived unchanged.

**A.6.P rewrite note.**
`retargetBearer(...)` is the family-specific form of `retargetParticipant(BearerSlot, …)`.
`reviseSense(...)`, `reArticulate(...)`, `reProxy(...)`, `reBundle(...)`, `reScale(...)`, `reFrame(...)`, and `reView(...)` are family-specific refinements of `reviseByValue(...)` and SHALL preserve the A.6.5 distinction between ref retargeting and by-value edits.

#### C.16.Q:4.8a - A.6.B boundary classification template for quality-term repair

When a repaired quality statement becomes boundary-bearing, classify it explicitly:

* **L** — `qualityTermAscription` repair-form skeleton, `QualitySense` semantics, normal-form admissibility, and declared bridge stances;
* **A** — admissibility conditions for using the ascription in selector, gating, and publication lanes (required qualifiers, witnesses, thresholds, qualification windows);
* **D** — publication requirements (lexical firewall, mandatory rewrites, publication duties);
* **E** — carrier-anchored evidence and work effects (measurements, traces, critique sheets, probe packs, selector logs).

Where this family is published as a reusable boundary publication, stable `L-Q*`, `A-Q*`, `D-Q*`, and `E-Q*` claim ids SHOULD be published (or the reused L/A/D/E-classified claim set should be cited by location), and paraphrase drift across quadrants SHALL be avoided.
Do not let the bare word *quality* carry L/A/D/E claim by itself.

#### C.16.Q:4.9 - Lexical guardrails

In **Tech and normative prose**:

* bare **quality** MUST NOT appear without immediate resolution to a `QualitySense`;
* **high-quality, low-quality, quality metric, quality score, quality requirement, model quality, architecture quality, and solution quality** are red-flag tokens;
* **quality characteristic** MAY appear only as:

  * a bridge label to an external standard or tradition, or
  * a family label immediately rewritten into one explicit `U.Characteristic` or `Q-Bundle`;
* **quality requirement or quality requirements** MUST NOT remain bare noun phrases; the text SHALL rewrite them into explicit `RequirementRole`, `U.Commitment`, or `U.PromiseContent.acceptanceSpec` structures over one named `U.Characteristic`, one `Q-Bundle` head, or one explicit objective head;
* **architecture quality or architectural quality** MUST NOT appear without an explicit bearer lane (`EntityOfConcern being described`, `description`, `episteme` or publication face, or carrier when the carrier itself is evaluated) and, when omission changes meaning, an explicit `referencePlane`;
* in QD and NQD contexts, bare **quality** MUST default to **`QS.UseValue`**;
* preconceptual uses MUST NOT be presented as if they were already Characteristics;
* latent and distributed fit MUST NOT be presented as if it were automatically explanatory merit;
* if the occurrence is primarily **action-invitation** talk, the text MUST NOT assign a `QualitySense`; it SHALL exit to `A.6.A` or another action-invitation governing pattern, with source-tradition `affordance` wording kept only as a quoted cue when needed;
* scope words (*applicability*, *envelope*, *generality*, *validity*) MUST NOT be used as hidden substitutes for `U.Scope`, `U.ClaimScope (G)`, or `U.WorkScope`;
* quoted metalinguistic uses of the token *quality* are allowed, but SHALL be marked as **token-under-discussion**, not as a boundary-bearing term.

#### C.16.Q:4.10 - Progressive elaboration

C.16.Q permits monotone elaboration:

1. Start by selecting a **`QualitySense`** and capturing rival candidates when ambiguity is live.
2. Declare bearer, frame, viewpoint, and substrate.
3. Choose an admissible **normal form**.
4. Add exemplars, probes, characteristic heads, bundle members, and objective pins.
5. Add bridges and loss notes if comparing traditions.
6. If the repaired sentence is boundary-bearing, emit `L/A/D/E` hooks rather than letting “quality” carry them implicitly.
7. Never move between sense families silently.

