---
chunk_kind: "child"
pattern_id: "C.16.Q"
pattern_title: "Quality-Term Precision Restoration"
section_id: "C.16.Q:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.Q/C.16.Q__006_solution.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.16.Q — Quality-Term Precision Restoration"
  - "C.16.Q:4 — Solution"
line_start: 59460
line_end: 59818
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

Recover the intended claim first. Use a known endpoint directly; retain a transitional ascription only for unresolved interpretation that the receiving work needs to inspect.

#### C.16.Q:4.0 - Trigger rule

Inspect quality wording when its sense, bearer, comparison or consequence is unclear, especially in a claimed improvement, admission or cross-tradition use. Familiar phrases such as *quality score*, *model quality* and *quality requirement* are cues to that question. Their appearance alone does not require a new ascription or a repeated repair of an already explicit endpoint.

#### C.16.Q:4.0a - Operational repair sequence

1. **Read the whole assertion.** Recover what the sentence claims or asks. Retain its wording when an inspectable before/after comparison is needed.
2. **Recover the evaluated subject.** Distinguish the EntityOfConcern being described from its description, publication face or carrier when that distinction changes the claim. Keep ordinary non-governed wording ordinary.
3. **Distinguish the live meanings.** Use the stated purpose, interpretation scheme, evaluation conditions and comparison to resolve plausible alternatives. If an existing endpoint already conveys the intended claim, use it and stop this repair. Keep a short Candidate-Set Note only when unresolved alternatives need to remain inspectable for the receiving decision or publication; use an existing explanation when it already does that job.
4. **Follow the recovered question.** For action-oriented wording, a relation, evidence, a gate or another non-quality question, apply its subject rule. Use A.6.A, A.6.P, C.16.P or another recovery pattern only while the corresponding meaning is still unclear. An adequately expressed question can finish without a `QualitySense`.
5. **Choose a sense when a transitional ascription is needed.** Select the applicable `QualitySense` and retain consequential rival interpretations while they remain unresolved. Explain a rejected alternative only when that distinction helps recover the intended claim.
6. **State the supported interpretation.** Use the known endpoint's form, or the transitional form under §4.1 with its required bearer, scheme, probe/model and comparison conditions, evaluator/viewpoint, scope and normal form. Add result, evidence, grounding or cross-local references only for independently established relations used by this claim.
7. **Apply conditions for a further use.** A clarified quality statement can contribute to a decision, evidence claim or other result. Establish that further use under its own rule; the word “quality” and completion of the repair do not establish it.

#### C.16.Q:4.1 - Transitional repair frame: evaluative classification anchored by `qualityTermAscription(...)`

A transitional ascription makes an unresolved evaluative interpretation explicit under one effective ReferenceScheme and a named endpoint pattern or source relation. It records the intended characterization without asserting a result or evidence relation merely through its fields.

`qualityTermAscription(...)` is the canonical transitional quality-term repair form when the endpoint choice is not yet fixed. It is not the universal resting place, not a relation kind by default, and not a shadow endpoint source.

Use of `qualityTermAscription(...)` presupposes enough articulation explicitness to name the bearer, effective scheme, probe/model frame, comparison frame or explicit `none`, ClaimScope, and at least one candidate evaluative family. Closure degree may remain low while `qualityTermAscription(...)` is transitional, but content that is still only a cue pack, forwarded cue, or open explanatory probe stays in `A.16.1`, `B.4.1`, or `B.5.2.0`. If a published record later loses an interpretation-bearing scheme, frame, scope, or direct source relation required for its stated use, retreat via `A.16.2`; changed witnesses, evidence use, or grounding reopen only the exact neighboring result or reliance claim they bear on.

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
  nonAdmissibleUse?
}
```

`effectiveReferenceScheme`, `probeOrModelFrameRef`, `comparisonFrameRef`, and `claimScope` are explicit even when the comparison value is `none`; no generic `context` or `frame` slot defines their semantics. A probe or model frame remains the exact domain-local probe/model configuration. A comparison frame resolves the applicable `CG-Spec`, comparator edition, comparison scope, reference plane, and interval under A.19.CPM; it is not a universal `Frame` kind.

The record designates, but does not embed, a viewpoint. A non-`none` `viewpointRef` is one `U.ViewpointRef` whose governed resolution yields an exact viewpoint episteme; the reference, the viewpoint episteme, and the evaluator remain different objects. `qualityResultClaimRef` is not assessment work, while witness refs and an A.10 evidence-provenance path establish neither a result nor empirical grounding. Cite `empiricalGroundingRelationRef` only for a separately obtaining C.2.1 relation between the identified episteme and exact holon under governed observation, intervention, measurement, test, or evaluation relations. Likewise, cite an F.9 Bridge occurrence and bounded-use claim only when each independently exists. Cite a Card only when that optional package exists. Cite a stance note only when its reference resolves a C.2.1 episteme whose `EntityOfConcern` is that exact use claim. At least one of `endpointPatternLocator` and `endpointSourceRelationRef` is required. The locator identifies the pattern passage that defines or tests the endpoint; it does not make the pattern an actor or require a separate assertion or `ClaimGraph` unless a named later use depends on that rule identity.

For a use whose quality meaning remains consequentially ambiguous, “X has quality” is insufficient. State the supported interpretation, use the known endpoint, or retain the unresolved alternatives in the transitional form when its entry conditions are met.

**Discipline note.**
`QualitySense` is a slot value inside the transitional repair form; it is not a replacement for the endpoint FPF pattern or explicit endpoint source reference. The sense token refines what kind of evaluative characterization is being made while the endpoint source, applicable pattern, or EntityOfConcern remains explicit.

**Separation note.**
`evaluatorRef` and `viewpointRef` are not synonyms. The evaluator is the observing, criticizing, or selecting party or policy. `viewpointRef` is a governed reference whose resolution yields one exact `U.Viewpoint` episteme; selecting or resolving it grants no membership, conformance, authority, or evaluation result.

The checked bearer, any dated assessment work, the resulting claim episteme, witness carriers, an A.10 evidence-provenance path, and an optional `EpistemeEmpiricalGroundingRelation` remain independently governed. A filled `qualityTermAscription(...)` may refer to each, but record completion, a result label, or stored witnesses makes none of the neighboring relations obtain.

#### C.16.Q:4.1b - Polarity discipline (bearer-centred; no silent inverse)

`qualityTermAscription` is bearer-centred.
A transitional ascription SHALL keep the evaluated participant in the bearer position and SHALL publish `evaluatorRef` and governed `viewpointRef` separately, using `none` when either is absent. A known endpoint retains its own form and the same participant distinctions.

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

Every transitional ascription SHALL identify an explicit **`QualitySense` token**. A known endpoint can express the intended evaluation directly without adding this token or record.

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

**Normative interpretation rules.** Choose the family from the actual claim; a domain label alone does not determine its sense.

* In NQD, QD or selector use, the evaluative Q head defaults to `QS.UseValue` unless another sense is explicitly declared.
* An engineering quality claim resolves to one explicit `U.Characteristic` with its CSLC Scale, or an explicit Bundle, preferably a C.25 Q-Bundle when its conditions apply.
* Description of experienced phenomenal character uses `QS.PhenomenalCharacter`; preconceptual fit or felt rightness uses `QS.PreconceptualFit`.
* A claim about distributed fit in a learned representation uses `QS.LatentFit`; a claim about closed-loop adequacy uses `QS.ControlAdequacy`. A model can also receive a different evaluation under its corresponding sense; the phrase “model quality” alone selects none of them.
* Evaluation of an explanation's epistemic merit uses `QS.ExplanatoryMerit`. A different claim, such as readability of its presentation, retains its own subject and criteria.
* For architecture wording, distinguish the bearer first. Engineering quality of the system and fitness of its architecture description use different subjects and criteria; the latter uses `QS.ArchitecturalDescriptionFitness`.

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

11. **Witnesses, evidence use, and empirical grounding when relied on.**
    Name the witnesses relied on for this use. If an evidence-provenance path is relied on, use A.10 for its descriptive account and cite each obtaining direct relation under the pattern that defines it. When empirical grounding is at issue, independently cite an obtaining `EpistemeEmpiricalGroundingRelation`, or state `none`; witness or record presence does not create that relation.

12. **Cross-local and endpoint boundaries.**
    Cite an exact F.9 Bridge occurrence and bounded-use claim only when they independently exist. Cite a Card only when that optional package exists, and cite an F.9.1 stance note only when its `EntityOfConcern` is that claim. State the endpoint pattern or endpoint source relation, the admissible use, and necessary applicability or stop conditions. Add an explanatory non-admissible-use guard only under F.19:4's independent-ground, plausible-reader, contribution, and smallest-clear-correction test.

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
* the signal use it supports and the additional declaration needed before treating a proxy as a `Characteristic`.

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

Within one exact `<ReferenceScheme, LocalSenseClaim>` interpretation basis, lexical restoration may choose a local sense or rename without asserting an F.9 Bridge. When a use depends on semantic correspondence between two quality senses with different interpretation bases, resolve both exact F.17 `SchemeSenseCell` values and test the direct F.9 Bridge predicate. Source-local description or separate citation of the two senses needs no such correspondence. Scheme difference, shared spelling, an analogy, a loss note, or a quality record establishes no Bridge.

If the Bridge obtains, cite its exact occurrence and state any proposed comparison, substitution, operationalization, or projection as a separate F.9 bounded-use claim. That claim names the direction, rule, tolerated loss, polarity, and effective ReferenceScheme. Apply A.10 or B.3 only for the reliance branch that is actually live. A Bridge Card remains optional reusable packaging.

Add an F.9.1 stance note only when a short interpretive cue helps a reader understand that exact bounded-use claim. The note is a separate C.2.1 episteme whose `EntityOfConcern` is the claim. Its optional label may be, for example:

* **`localRename`** — read this use as near-renaming within its declared local boundary; do not infer cross-local identity.
* **`operationalizes`** — read the receiving expression as a procedural or measurable aid for this use; do not infer work, implementation, permission, or suitability beyond the cited claim.
* **`partialAnalogy`** — read the stated correspondence as partial; do not infer substitution.
* **`projection`** — read this use as a deliberate reduction of the source reading; the F.9 claim still carries its rule and tolerated loss.
* **`nonEquivalent`** — treat this as a warning against equivalence and silent substitution; the label alone asserts neither `Disjoint`, negative polarity, nor an evidence score.

These tokens are optional reading labels inside a stance note. They are not Bridge kinds, direct relations, result claims, or substitutes for the Bridge, bounded-use claim, evidence, or loss account.

Examples:

* `QS.PreconceptualFit` and `QS.LatentFit` are usually only candidates for partial correspondence. If the proposed use depends on correspondence between their exact cross-local F.17 cells, test an F.9 kind such as `Partial-overlap`; an optional `partialAnalogy` note may help read the resulting bounded-use claim but cannot establish identity.
* A progression from `QS.PreconceptualFit` to `QS.PhenomenalCharacter` needs its exact direct relation or bounded-use account; shared articulation history does not make the senses identical.
* A felt cue can prompt a choice of engineering measure without asserting that the measure represents that cue. If the claim instead proposes a cross-local operationalization or projection, establish its Bridge, bounded-use rule and tolerated loss separately from the measurement result. Add a stance note only if it improves the reading.
* An engineering measure can be selected as an objective under a declared CG-frame. That use does not identify the whole engineering family with selector value. When it depends on a cross-local correspondence, state the actual F.9 use and any demonstrated loss; selecting an objective alone establishes no loss.
* An obtaining F.9 Bridge between `QS.ExplanatoryMerit` and `QS.UseValue` does not by itself establish identity. An F.9.1 `nonEquivalent` note may help read an existing bounded-use claim but cannot replace the Bridge finding or claim polarity.
* Pirsig-style **dynamic quality** may locally cue `QS.PreconceptualFit` or sometimes `QS.LatentFit`. Within one exact interpretation basis this may be a local rename; a proposed correspondence across bases needs exact F.17 cells and F.9 treatment. A source-local account can retain its own meaning. The label alone supplies neither identity nor empirical grounding.
* Pirsig-style **static quality** usually cues a `Characteristic` or `Bundle` publication under another declared sense; it is not identical with dynamic quality.
* `QS.ArchitecturalDescriptionFitness` and `QS.EngineeringQualityFamily` have different bearer lanes. Any cross-local correspondence must keep the exact description-side and system-side cells, Bridge occurrence, bounded-use claim, and losses separate and must name which description-fitness heads, if any, are proposed to proxy which system-side characteristics.

#### C.16.Q:4.8 - Change lexicon

Changes to a transitional ascription SHALL preserve the distinctions in this change lexicon. Ordinary wording is sufficient when it makes the changed value or reference clear; the tokens below can support a reusable record:

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

When a repaired quality statement carries a boundary claim, preserve its A.6.B classification. A local sentence with one recoverable logical job needs no separate Claim Register or publication form. For a reusable boundary account, distinguish:

* **L** — `qualityTermAscription` repair-form skeleton, `QualitySense` semantics, normal-form admissibility, cross-local routing, and the rule that any F.9.1 stance note remains a separate optional episteme about an already constituted bounded-use claim;
* **A** — admissibility conditions for using the ascription in selector, gating, and publication lanes (required qualifiers, witnesses, thresholds, qualification windows);
* **D** — publication requirements (lexical firewall, mandatory rewrites, publication duties);
* **E** — carrier-anchored evidence and work effects (measurements, traces, critique sheets, probe packs, selector logs).

Where this family is published as a reusable boundary publication, stable `L-Q*`, `A-Q*`, `D-Q*`, and `E-Q*` claim ids SHOULD be published (or the reused L/A/D/E-classified claim set should be cited by location), and paraphrase drift across quadrants SHALL be avoided.
Do not let the bare word *quality* carry L/A/D/E claim by itself.

#### C.16.Q:4.9 - Lexical guardrails

In **Tech and normative prose**:

* a consequentially ambiguous quality claim MUST resolve to its known endpoint or, when needed, an explicit transitional `QualitySense`;
* **high-quality, low-quality, quality metric, quality score, quality requirement, model quality, architecture quality, and solution quality** cue inspection of the intended claim;
* **quality characteristic** MAY appear only as:

  * a source-local term whose cited standard or tradition supplies its meaning, with F.9 used only for a needed semantic correspondence, or
  * a family label immediately rewritten into one explicit `U.Characteristic` or `Q-Bundle`;
* a claim using **quality requirement or quality requirements** SHALL make the required head and its requirement or acceptance relation recoverable. Use the applicable rule for that claim; a named Characteristic, Q-Bundle head or objective can supply the evaluated content. The phrase itself establishes no requirement or acceptance result;
* **architecture quality or architectural quality** MUST NOT appear without an explicit bearer lane (`EntityOfConcern being described`, `description` or another `episteme`, publication face, or carrier when the carrier itself is evaluated) and, when omission changes meaning, an explicit `referencePlane`;
* in QD and NQD contexts, bare **quality** MUST default to **`QS.UseValue`**;
* preconceptual uses MUST NOT be presented as if they were already Characteristics;
* latent and distributed fit MUST NOT be presented as if it were automatically explanatory merit;
* if the occurrence is primarily **action-invitation** talk, the text MUST NOT assign a `QualitySense`; use the recovered subject rule directly, or `A.6.A` while the action meaning remains unclear, with source-tradition `affordance` wording retaining its cited meaning when used;
* scope words (*applicability*, *envelope*, *generality*, *validity*) MUST NOT be used as hidden substitutes for `U.ClaimScope`, `U.WorkScope`, `U.PublicationScope`, or another exact governed scope;
* quoted metalinguistic uses of the token *quality* are allowed, but SHALL be marked as **token-under-discussion**, not as a boundary-bearing term.

#### C.16.Q:4.10 - Progressive elaboration

A transitional ascription can be elaborated as its interpretation becomes clearer. Changed grounds can also require revising or withdrawing earlier content; elaboration is not necessarily monotone:

1. Select a **`QualitySense`** and retain rival candidates while ambiguity is live.
2. Name the exact bearer, effective ReferenceScheme, `U.ClaimScope`, and any meaning-changing `Γ_time`, reference plane, representation scheme, or substrate.
3. Name the probe or model frame and the separate comparison frame or explicit `none`; then name evaluator and `U.ViewpointRef` independently.
4. Choose an admissible **normal form** and identify any separately constituted quality-result claim.
5. Add exemplars, probes, characteristic heads, bundle members, objective pins, witness refs, and exact A.10 evidence-provenance paths as needed. Cite empirical grounding only through an independently obtaining relation.
6. If cross-local correspondence is live, resolve exact F.17 cells, the obtaining F.9 Bridge, and the separate bounded-use claim. Add a Card only as optional packaging and an F.9.1 stance note only as optional reader help about that claim.
7. Preserve any boundary claim and its material dependencies under A.6.B; add stable hooks only when the receiving use needs them.
8. Never move between sense families, frames, schemes, scopes, result claims, or neighboring relations silently.

