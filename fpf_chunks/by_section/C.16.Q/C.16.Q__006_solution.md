---
chunk_kind: "child"
pattern_id: "C.16.Q"
pattern_title: "Quality-Term Precision Restoration"
section_id: "C.16.Q:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.Q/C.16.Q__006_solution.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "C.16.Q — Quality-Term Precision Restoration"
  - "C.16.Q:4 — Solution"
line_start: 48697
line_end: 49079
dependencies:
  - "A.10"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CPM"
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
  - "C.30.AD"
  - "C.30.ASV"
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "E.17.2"
  - "E.21"
  - "E.8"
  - "F.18"
  - "F.9"
  - "F.9.1"
  - "U.ClaimScope"
  - "U.ContextSlice"
  - "U.ViewpointRef"
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
   Name the bearer and the relevant A.7 distinction between the EntityOfConcern being described, its description or another `episteme`, a publication face, and a carrier evaluated in its own right. Examples of bearers include a pattern, model, policy, explanation, candidate, architecture description, work result, relation, or action loop. Keep ordinary prose with no FPF-governed use ordinary.

3. **Recover interpretation locality and reconstruct candidates.**
   Recover the effective ReferenceScheme, probe/model frame, separate A.19.CPM comparison frame or `none`, `U.ClaimScope`, evaluator, and `U.ViewpointRef` or `none`. Then enumerate plausible senses and the patterns or source relations for their candidate endpoints. If the occurrence is decision-bearing, publication-bearing, or cross-local, record these alternatives in a short quality-term Candidate-Set Note before selecting the repair.

4. **Exit when the claim being made is not quality-term or evaluative characterization.**
   If the occurrence is primarily action invitation, relation construction, bridge, basedness, endpoint mismatch, evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens use, characteristic and scale construction, or source-use, do not assign a `QualitySense`. Apply `A.6.P`, `A.6.A`, `C.16.P`, `C.29`, `C.2.P`, or the pattern for the recovered claim.

5. **Select one explicit quality sense.**
   Pick one `QualitySense` token and state why rival senses were rejected in this local context.

6. **Emit an endpoint-explicit or transitional rewrite.**
   Rewrite the sentence either into the evaluative form defined for a known endpoint (`Characteristic | Q-Bundle | Objective | ExplanatoryMeritBundle | selector-value endpoint`) or, while endpoint choice is still being stabilized, into one explicit `qualityTermAscription(...)` transitional repair form with bearer, effective ReferenceScheme, probe/model and comparison frames, evaluator and `U.ViewpointRef`, `U.ClaimScope`, normal form, result boundary, and separate witness/evidence/grounding and cross-local qualifiers.

7. **Classify boundary-bearing consequences.**
   If the repaired statement is used for admissibility, commitments, publication, evidence-bearing decisions, gates, release, or work, apply the pattern for that downstream claim instead of letting *quality* carry it by itself.

#### C.16.Q:4.1 - Transitional repair frame: evaluative classification anchored by `qualityTermAscription(...)`

`C.16.Q` stabilizes the ambiguity cluster by treating every in-scope quality statement as explicit evaluative content under one effective ReferenceScheme and a named endpoint pattern or source relation, not as a bare adjective, generic context field, or evidence-bearing result by implication.

`qualityTermAscription(...)` is the canonical transitional quality-term repair form when the endpoint choice is not yet fixed. It is not the universal resting place, not a relation kind by default, and not a shadow endpoint source.

Entry into `C.16.Q` presupposes enough articulation explicitness to name the bearer, effective scheme, probe/model frame, comparison frame or explicit `none`, ClaimScope, and at least one candidate evaluative family. Closure degree may remain low while `qualityTermAscription(...)` is transitional, but content that is still only a cue pack, forwarded cue, or open explanatory probe stays in `A.16.1`, `B.4.1`, or `B.5.2.0`. If a published record later loses an interpretation-bearing scheme, frame, scope, or direct source relation required for its stated use, retreat via `A.16.2`; changed witnesses, evidence use, or grounding reopen only the exact neighboring result or reliance claim they bear on.

The transitional form is:

```text
qualityTermAscription :=
{
  bearerTuple: exact bearer designator(s),
  qualitySense: QualitySense,
  effectiveReferenceScheme: U.ReferenceScheme,
  probeOrModelFrameRef: exact domain-local probe or model frame,
  comparisonFrameRef: exact A.19.CPM-governed comparison frame | none,
  evaluatorRef: exact evaluator or policy ref | none,
  viewpointRef: U.ViewpointRef | none,
  referencePlane?,
  representationSchemeRef?: U.RepresentationScheme ref,
  normalForm: SignalPack | Characteristic | Bundle | Objective,
  claimScope: U.ClaimScope,
  contextSliceRefs?: exact U.ContextSlice refs,
  gammaTime?,
  representationSubstrate?: embodied-kinesthetic | latent-distributed | symbolic-local | hybrid,
  qualityResultClaimRef?: exact separately constituted result-episteme ref,
  witnessRefs?: exact witness refs,
  evidenceProvenancePathRefs?: refs to exact direct relations in an A.10 path,
  empiricalGroundingRelationRef?: exact EpistemeEmpiricalGroundingRelation occurrence ref | none,
  bridgeOccurrenceRef?: exact F.9 Bridge occurrence ref | none,
  bridgeUseClaimRef?: exact F.9 bounded-use claim ref | none,
  bridgeCardRef?: exact F.9 Bridge Card ref | none,
  bridgeStanceNoteRef?: exact F.9.1 stance-episteme ref | none,
  endpointPatternLocator?: pattern ref for the endpoint,
  endpointSourceRelationRef?: exact direct source or publication relation ref,
  admissibleUse,
  nonAdmissibleUse
}
```

`effectiveReferenceScheme`, `probeOrModelFrameRef`, `comparisonFrameRef`, and `claimScope` are explicit even when the comparison value is `none`; no generic `context` or `frame` slot defines their semantics. A probe or model frame remains the exact domain-local probe/model configuration. A comparison frame resolves the applicable `CG-Spec`, comparator edition, comparison scope, reference plane, and interval under A.19.CPM; it is not a universal `Frame` kind.

The record designates, but does not embed, a viewpoint. A non-`none` `viewpointRef` is one `U.ViewpointRef` whose governed resolution yields an exact viewpoint episteme; the reference, the viewpoint episteme, and the evaluator remain different objects. `qualityResultClaimRef` is not assessment work, while witness refs and an A.10 evidence-provenance path establish neither a result nor empirical grounding. Cite `empiricalGroundingRelationRef` only for a separately obtaining C.2.1 relation between the identified episteme and exact holon under governed observation, intervention, measurement, test, or evaluation relations. Likewise, cite an F.9 Bridge occurrence and bounded-use claim only when each independently exists. Cite a Card only when that optional package exists. Cite a stance note only when its reference resolves a C.2.1 episteme whose `EntityOfConcern` is that exact use claim. At least one of `endpointPatternLocator` and `endpointSourceRelationRef` is required. The locator identifies the pattern passage that defines or tests the endpoint; it does not make the pattern an actor or require a separate assertion or `ClaimGraph` unless a named later use depends on that rule identity.

So the sentence "X has quality" is never accepted as a terminal form. It must be rewritten either into the evaluative form for a known endpoint or into this transitional repair form with its interpretation-bearing and neighboring-object boundaries declared.

**Discipline note.**
`QualitySense` is a slot value inside the transitional repair form; it is not a replacement for the endpoint FPF pattern or explicit endpoint source reference. The sense token refines what kind of evaluative characterization is being made while the endpoint source, applicable pattern, or EntityOfConcern remains explicit.

**Separation note.**
`evaluatorRef` and `viewpointRef` are not synonyms. The evaluator is the observing, criticizing, or selecting party or policy. `viewpointRef` is a governed reference whose resolution yields one exact `U.Viewpoint` episteme; selecting or resolving it grants no membership, conformance, authority, or evaluation result.

The checked bearer, any dated assessment work, the resulting claim episteme, witness carriers, an A.10 evidence-provenance path, and an optional `EpistemeEmpiricalGroundingRelation` remain independently governed. A filled `qualityTermAscription(...)` may refer to each, but record completion, a result label, or stored witnesses makes none of the neighboring relations obtain.

#### C.16.Q:4.1b - Polarity discipline (bearer-centred; no silent inverse)

`qualityTermAscription` is bearer-centred.
Tech and normative prose SHALL keep the evaluated participant in the bearer position and SHALL publish `evaluatorRef` and governed `viewpointRef` separately, using `none` when either is absent.

* When the evaluating architects are identified as `ArchitectureReviewBoard`, “Architects rate the system highly” rewrites to `qualityTermAscription(bearerTuple={System}, evaluatorRef=ArchitectureReviewBoard, viewpointRef=none, …)`.
* When the benchmark's evaluation policy is identified as `BenchmarkPolicy`, “The benchmark says model quality is high” rewrites to `qualityTermAscription(bearerTuple={Model}, evaluatorRef=BenchmarkPolicy, viewpointRef=none, …)`.

There is no inverse token that silently makes the evaluator the bearer.
If inverse wording is used in Plain prose, rewrite it into the bearer-centred form, or use the explicit inverse form supplied by the applicable pattern.

#### C.16.Q:4.1c - Endpoint-first discipline

When the endpoint pattern or explicit endpoint source relation is already known, publish the evaluative form it defines directly. Keep `qualityTermAscription(...)` only when preserving the transitional ambiguity is itself informative. `qualityTermAscription(...)` is therefore a transitional characterization record, not a shadow endpoint source.

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
    probeOrModelFrameKind,
    comparisonFrameRequired,
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
  `defaultNormalForm` names the primary evaluative normal form; any additional endpoint forms MUST be declared here rather than inferred ad hoc. `probeOrModelFrameKind` constrains only the domain-local probe/model configuration, while `comparisonFrameRequired` states whether a separate A.19.CPM comparison configuration must be named. `bridgePolicy` can require F.9 recovery or forbid silent reuse, but it cannot establish a Bridge. If the quality ascription is published, handle publication face, form, unit, carrier, and rendering questions under E.17, E.8, or the applicable publication pattern.

#### C.16.Q:4.3 - Normative starter set of sense families

A declared local vocabulary under one effective ReferenceScheme MAY add local senses, but the following starter set is normative as the initial disambiguation menu:

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
A declared local use under one effective ReferenceScheme MAY operationalize one explicit head as a `Characteristic`, but that is a declared operationalization, not a second default normal form.

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
   Name the exact evaluated bearer designator or tuple and its arity. A description, carrier, evaluator, or result claim cannot silently replace that bearer.

2. **`QualitySense`.**
   Name the intended evaluative family.

3. **Effective ReferenceScheme.**
   State the effective `U.ReferenceScheme` by value so every designator and local sense in the ascription is interpretable. A generic context label or a representation scheme is not a substitute.

4. **Probe or model frame.**
   Name the exact domain-local exemplar pack, probe pack, test or criticism pack, Q-bundle definition, CG-frame, acceptance specification, control horizon, or other governed probe/model configuration.

5. **Comparison frame.**
   Name the exact A.19.CPM-governed comparison configuration separately, including the effective comparator and comparison scope when a comparison is made. Publish `none` when the ascription proposes no comparison; do not let the probe/model frame silently select one.

6. **Evaluator and viewpoint reference.**
   State the evaluator or policy and, independently, either one `U.ViewpointRef` or `none`. A non-`none` reference SHALL resolve to one exact viewpoint episteme under E.17.0; neither the reference nor its resolution is the evaluator.

7. **Normal form and result boundary.**
   State whether the ascription uses `SignalPack`, `Characteristic`, `Bundle`, or `Objective`. If separately performed assessment work produced a result claim, cite that exact C.2.1 episteme through `qualityResultClaimRef`; do not identify the work, result, bearer, or transitional record with one another.

8. **ClaimScope, selected slices, and time.**
   State one `U.ClaimScope` and its exact `U.ContextSlice` membership when the members matter. State `Γ_time` when omission changes meaning. `U.WorkScope` and `U.PublicationScope` remain with their own work or publication claims rather than substituting for this claim scope. Freshness, qualification, and evidence-decay windows remain in their exact evidence, capability, or currentness lanes rather than being smuggled into *quality*.

9. **Reference plane when relevant.**
   Name the plane when the same trigger phrase could concern the EntityOfConcern being described, its description, a carrier, or a publication face.

10. **Representation scheme and substrate when relevant.**
    Keep the effective reference scheme distinct from any representation scheme, viewpoint-specific decoding convention, or embodied-kinesthetic, latent-distributed, symbolic-local, or hybrid substrate. Name each when omission changes interpretation.

11. **Witnesses, evidence use, and empirical grounding.**
    Name exact exemplars, probes, measurements, bundle members, tests, traces, closed-loop performance carriers, or other witnesses. If an evidence-provenance path is relied on, cite its exact direct relations under A.10. Independently cite an obtaining `EpistemeEmpiricalGroundingRelation`, or state `none`; witness or record presence does not create that relation.

12. **Cross-local and endpoint boundaries.**
    Cite an exact F.9 Bridge occurrence and bounded-use claim only when they independently exist. Cite a Card only when that optional package exists, and cite an F.9.1 stance note only when its `EntityOfConcern` is that claim. State the endpoint pattern or endpoint source relation, the admissible use, and nearest non-admissible use rather than letting *quality* or a stance token carry them.

#### C.16.Q:4.5 - Normal-form discipline

A `QualitySense` SHALL declare one admissible **default** evaluative normal form and MAY declare additional admissible evaluative normal forms explicitly.

The normal forms in this section are endpoint or evaluative forms. They are not publication forms by themselves. Publication face, publication form, publication unit, carrier, rendering, export, and front-end questions remain with `E.17`, `E.8`, or the applicable endpoint-publication pattern.

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

* A statement about **what a system does** uses `A.6.F` first when function-like wording hides the FPF kind, relation, or claim, then applies the pattern for the recovered capability, Method, Work, system-role kind or assignment, `A.6.M` module-interface, architecture, mathematical, evidence, assurance, gate, decision, or release claim.
* A statement about **how well, how safely, how robustly, or how maintainably** it does so belongs to `QS.EngineeringQualityFamily`.
* “Quality characteristic” and “functional characteristic” SHALL NOT be used as interchangeable labels.
* In engineering contexts, `-ility` names are **quality-family labels**, not automatically Characteristics.
  They become admissible only as one explicit `U.Characteristic` or one explicit `Bundle` (preferably expressed through `Q-Bundle` when composite).
* Cross-references are allowed; category collapse is not.

#### C.16.Q:4.7 - Local repair stances and cross-local Bridge discipline

Within one exact `<ReferenceScheme, LocalSenseClaim>` interpretation basis, lexical restoration may choose a local sense or rename without asserting an F.9 Bridge. When two quality senses have different interpretation bases, first resolve both exact F.17 `SchemeSenseCell` values and test the direct F.9 Bridge predicate. Scheme difference, shared spelling, an analogy, a loss note, or a quality record establishes no Bridge.

If the Bridge obtains, cite its exact occurrence and state any proposed comparison, substitution, operationalization, or projection as a separate F.9 bounded-use claim. That claim names the direction, rule, tolerated loss, polarity, and effective ReferenceScheme. Apply A.10 or B.3 only for the reliance branch that is actually live. A Bridge Card remains optional reusable packaging.

Add an F.9.1 stance note only when a short interpretive cue helps a reader understand that exact bounded-use claim. The note is a separate C.2.1 episteme whose `EntityOfConcern` is the claim. Its optional label may be, for example:

* **`localRename`** — read this use as near-renaming within its declared local boundary; do not infer cross-local identity.
* **`operationalizes`** — read the receiving expression as a procedural or measurable aid for this use; do not infer work, implementation, permission, or suitability beyond the cited claim.
* **`partialAnalogy`** — read the stated correspondence as partial; do not infer substitution.
* **`projection`** — read this use as a deliberate reduction of the source reading; the F.9 claim still carries its rule and tolerated loss.
* **`nonEquivalent`** — treat this as a warning against equivalence and silent substitution; the label alone asserts neither `Disjoint`, negative polarity, nor an evidence score.

These tokens are optional reading labels inside a stance note. They are not Bridge kinds, direct relations, result claims, or substitutes for the Bridge, bounded-use claim, evidence, or loss account.

Examples:

* `QS.PreconceptualFit` and `QS.LatentFit` are usually only candidates for partial correspondence. If their exact F.17 cells are cross-local, test an F.9 kind such as `Partial-overlap`; an optional `partialAnalogy` note may help read the resulting bounded-use claim but cannot establish identity.
* A progression from `QS.PreconceptualFit` to `QS.PhenomenalCharacter` needs its exact direct relation or bounded-use account; shared articulation history does not make the senses identical.
* Using `QS.PreconceptualFit` to choose engineering measures is a proposed operationalization or projection use. Name the actual Bridge, separate use rule and tolerated loss, and direct measurement or characterization result. Add a stance note only if it improves the reading.
* Relating `QS.EngineeringQualityFamily` to `QS.UseValue` is normally a directional, loss-bearing proposed use under a declared CG-frame, not identity and not permission to substitute one score for the other.
* An obtaining F.9 Bridge between `QS.ExplanatoryMerit` and `QS.UseValue` does not by itself establish identity. An F.9.1 `nonEquivalent` note may help read an existing bounded-use claim but cannot replace the Bridge finding or claim polarity.
* Pirsig-style **dynamic quality** may locally cue `QS.PreconceptualFit` or sometimes `QS.LatentFit`. Within one exact interpretation basis this may be a local rename; across bases it needs exact F.17 cells and F.9 treatment. The label alone supplies neither identity nor empirical grounding.
* Pirsig-style **static quality** usually cues a `Characteristic` or `Bundle` publication under another declared sense; it is not identical with dynamic quality.
* `QS.ArchitecturalDescriptionFitness` and `QS.EngineeringQualityFamily` have different bearer lanes. Any cross-local correspondence must keep the exact description-side and system-side cells, Bridge occurrence, bounded-use claim, and losses separate and must name which description-fitness heads, if any, are proposed to proxy which system-side characteristics.

#### C.16.Q:4.8 - Change lexicon

A conforming quality-term repair publication SHALL narrate changes with a stable change lexicon aligned to A.6.P:

* **`declareQualityTermAscription(...)`** — create a new explicit quality-ascription record.
* **`withdrawQualityTermAscription(...)`** — retire a prior record.
* **`retargetBearer(...)`** — retarget the evaluated bearer ref or tuple while keeping the repair-form schema.
* **`reviseSense(...)`** — change the value in the `qualitySense` slot.
* **`reArticulate(...)`** — change `articulationMode` while preserving the sense family.
* **`reProxy(...)`** — change proxy, probe, or operationalization details.
* **`reBundle(...)`** — change bundle members or aggregation policy.
* **`reScale(...)`** — change characteristic scale or scale type.
* **`reProbeOrModelFrame(...)`** — change the exact domain-local probe or model frame.
* **`reComparisonFrame(...)`** — change the independently governed A.19.CPM comparison configuration.
* **`retargetEvaluator(...)`** — change the evaluator or policy ref without changing the viewpoint by implication.
* **`retargetViewpointRef(...)`** — retarget the governed `U.ViewpointRef`; resolution yields another exact viewpoint episteme only when the new reference resolves.
* **`reReferenceScheme(...)`** — change the effective ReferenceScheme explicitly; because that changes interpretation, re-check C.2.1 identity for any published claim episteme.
* **`rescopeClaim(...)`** — change `U.ClaimScope` or its exact `U.ContextSlice` members.
* **`retime(...)`** — change `Γ_time`.
* **`refreshWitnessRefs(...)`** — refresh witness bindings without silently changing an evidence-provenance path or grounding relation.
* **`replaceEvidenceProvenancePath(...)`** — replace the cited A.10 path of exact direct relations without manufacturing a quality result.
* **`replaceEmpiricalGroundingRelationRef(...)`** — cite another independently obtaining C.2.1 grounding occurrence; a record edit cannot make it obtain.
* **`retargetBridgeOccurrenceRef(...)`** — retarget an exact F.9 occurrence ref; it does not retarget a bounded-use claim, optional Bridge Card, or optional stance note by implication.
* **`exitQualityAscription(...)`** — end use of the quality-ascription form and continue with the pattern for the recovered non-quality claim; never silently retype the old record.

A silent **sense rewrite** is a breaking semantic change.
If the ascription ceases to mean “quality ascription” at all, close it with `exitQualityAscription(...)` and publish the recovered claim in the form needed for its use rather than pretending the same record survived unchanged.

**A.6.P rewrite note.**
`retargetBearer(...)` is the family-specific form of `retargetParticipant(BearerSlot, …)`. It, `retargetEvaluator(...)`, `retargetViewpointRef(...)`, and `retargetBridgeOccurrenceRef(...)` are reference-retargeting moves and SHALL preserve the A.6.5 distinction between a reference and the object it resolves. `reviseSense(...)`, `reArticulate(...)`, `reProxy(...)`, `reBundle(...)`, `reScale(...)`, `reProbeOrModelFrame(...)`, and `reComparisonFrame(...)` refine `reviseByValue(...)`. `reReferenceScheme(...)` and `rescopeClaim(...)` change interpretation-bearing values and require an identity check for any published C.2.1 episteme. Witness, evidence-path, result-claim, grounding-relation, Bridge, bounded-use-claim, Card, and stance-note refs change independently; no edit silently rewrites another.

#### C.16.Q:4.8a - A.6.B boundary classification template for quality-term repair

When a repaired quality statement becomes boundary-bearing, classify it explicitly:

* **L** — `qualityTermAscription` repair-form skeleton, `QualitySense` semantics, normal-form admissibility, cross-local routing, and the rule that any F.9.1 stance note remains a separate optional episteme about an already constituted bounded-use claim;
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
* **quality requirement or quality requirements** MUST NOT remain bare noun phrases; rewrite them into explicit requirement-use, source-use, gate, commitment, acceptance-spec, characteristic, `Q-Bundle`, objective, or publication-use claims or relations using the applicable pattern and one named `U.Characteristic`, `Q-Bundle` head, or objective head; the wording itself establishes none of those objects;
* **architecture quality or architectural quality** MUST NOT appear without an explicit bearer lane (`EntityOfConcern being described`, `description` or another `episteme`, publication face, or carrier when the carrier itself is evaluated) and, when omission changes meaning, an explicit `referencePlane`;
* in QD and NQD contexts, bare **quality** MUST default to **`QS.UseValue`**;
* preconceptual uses MUST NOT be presented as if they were already Characteristics;
* latent and distributed fit MUST NOT be presented as if it were automatically explanatory merit;
* if the occurrence is primarily **action-invitation** talk, the text MUST NOT assign a `QualitySense`; use `A.6.A` or another applicable action-invitation pattern, with source-tradition `affordance` wording kept only as a quoted cue when needed;
* scope words (*applicability*, *envelope*, *generality*, *validity*) MUST NOT be used as hidden substitutes for `U.ClaimScope`, `U.WorkScope`, `U.PublicationScope`, or another exact governed scope;
* quoted metalinguistic uses of the token *quality* are allowed, but SHALL be marked as **token-under-discussion**, not as a boundary-bearing term.

#### C.16.Q:4.10 - Progressive elaboration

C.16.Q permits monotone elaboration:

1. Select a **`QualitySense`** and retain rival candidates while ambiguity is live.
2. Name the exact bearer, effective ReferenceScheme, `U.ClaimScope`, and any meaning-changing `Γ_time`, reference plane, representation scheme, or substrate.
3. Name the probe or model frame and the separate comparison frame or explicit `none`; then name evaluator and `U.ViewpointRef` independently.
4. Choose an admissible **normal form** and identify any separately constituted quality-result claim.
5. Add exemplars, probes, characteristic heads, bundle members, objective pins, witness refs, and exact A.10 evidence-provenance paths as needed. Cite empirical grounding only through an independently obtaining relation.
6. If cross-local correspondence is live, resolve exact F.17 cells, the obtaining F.9 Bridge, and the separate bounded-use claim. Add a Card only as optional packaging and an F.9.1 stance note only as optional reader help about that claim.
7. If the repaired sentence is boundary-bearing, emit `L/A/D/E` hooks rather than letting *quality* carry them implicitly.
8. Never move between sense families, frames, schemes, scopes, result claims, or neighboring relations silently.

