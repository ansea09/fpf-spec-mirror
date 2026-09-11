---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
section_id: "A.6.6:4"
section_title: "Solution - State the direct relation, then add only what the receiving use needs"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__005_solution-state-the-direct-relation-then-add-only-what-the-receiving-use-needs.md"
commit_sha: "ef9ded2cb965193aa2484c84f06d65770439cef8"
heading_path:
  - "A.6.6 — Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
  - "A.6.6:4 — Solution - State the direct relation, then add only what the receiving use needs"
line_start: 19774
line_end: 19946
dependencies:
  - "A.10"
  - "A.14"
  - "A.2.4"
  - "A.2.6"
  - "A.6.0"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "A.6.6"
  - "A.6.REL"
  - "A.7"
  - "C.2.1"
  - "C.3.3"
  - "E.10"
  - "E.18"
  - "E.24.UK"
  - "E.8"
  - "F.0.1"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.9"
  - "U.KindBridge"
  - "U.Transfer"
keywords:
---

### A.6.6:4 - Solution - State the direct relation, then add only what the receiving use needs

#### A.6.6:4.0 - Ordinary direct path

Start with a readable sentence:

> `Thermocouple channel TC-17 is calibrated to standard ITS-90 for rig R3.`

Identify `TC-17` and `ITS-90`, then apply the direct `calibratedTo` predicate and its applicability rule to the current facts. If the task only asks whether that calibration relation obtains for this rig, the sentence and predicate result are complete. Do not create a declaration record, witness set, edition, or assurance package merely because those fields could be written down.

Add a qualifier only when it changes the direct assertion or a named receiving use:

- name scope when the relation is limited to a range, population, rig, publication, or other exact extent;
- name time when the predicate or the use is time-dependent;
- cite an evidence-use or provenance relation when a claim about the relation is relied on;
- open occurrence identity only when another claim must refer to the same occurrence, compare it, qualify it, or record its history; and
- open a reusable declaration only when the reuse test in A.6.6:4.3 is met.

The assertion episteme, reusable declaration, world-side relation occurrence, evidence, and any Work remain different objects.

#### A.6.6:4.1 - Optional scoped assertion record

When replay, comparison, publication, or repeated review needs a stable representation, a project may show one C.2.1 assertion episteme in this local form:

```text
scoped witnessed base declaration :=
  < dependent,
    base,
    directRelationKind,
    assertionPolarity,
    scope?,
    gammaTime?,
    evidenceUseRefs? >
```

This is a representation of claim content, not a public kind, `RelationSignature`, or world-side occurrence. `directRelationKind` resolves to an already governed relation kind; an affirmative assertion requires that relation's predicate to obtain for the actual participants, while a negative assertion requires nonobtaining to be established under the applicable criterion or closure basis. Failure to establish the affirmative does not establish the negative. `scope` and `gammaTime` are present only when the direct relation or named use needs them. `evidenceUseRefs`, when present, resolve to exact A.2.4 evidence-use relations for this assertion. The evidence epistemes, producing Work, operation result, carrier, provenance, currentness, and later reliance remain separately identified under A.2.4 and A.10.

A.6.6 admits neither `U.BaseDeclarationDiscipline` nor `U.ScopedWitnessedBaseDeclaration`. The latter is a retired spelling and must not be used as a kind or as a world-side relation occurrence.

The record's C.2.1 identity follows its complete ClaimGraph, exact EntityOfConcern, and effective ReferenceScheme. Changing an identity-bearing value identifies another episteme; a representation-only edit need not. Neither change by itself begins, ends, or alters the world-side relation it describes.

#### A.6.6:4.2 - Direct relation and optional assertion are different objects

The useful stable picture is a direct arrow in ordinary reading:

> dependent **stands in the named direct relation to** base.

The arrow is not a generic mathematical constructor. Its participant meanings, predicate, applicability, and occurrence identity come from the selected direct relation pattern. A scoped assertion episteme may affirm or deny that this predicate holds, and evidence may support reliance on that assertion. Filling the optional record or merely asserting the claim establishes no occurrence. An episteme or publication may have a constitutive role under the direct relation's own rule; evidential support remains independently governed.

Calibration, attribution, policy dependence, constructive grounding, and other cases therefore remain different relation kinds. A.6.6 supplies a recovery discipline, not one universal `BaseRelation` kind.

#### A.6.6:4.3 - Reusable declaration only for a named reuse

Use the direct relation's A.6.0 `RelationSignature` only after the relation kind is already admitted and at least two named consumers need the same reusable declaration content. That signature states the participant meanings, predicate, applicability, and occurrence-identity rule. A.6.5 SlotSpecs belong inside that reusable declaration; they are not required in an ordinary one-case assertion.

If no direct pattern supplies the relation kind, participants, or predicate, keep the exact local claim or return the A.6.RCD `missing-governor` result. Do not repair the gap by minting a generic `BaseRelation` kind or token, SlotSpecs, or a scoped-record type.

#### A.6.6:4.4 - What a reusable direct-relation declaration must say

For a named receiving use that genuinely needs a `RelationSignature`, the direct relation definition states:

- the dependent and base participant meanings and direction or symmetry;
- the obtaining predicate and applicability;
- the occurrence-identity rule supplied by the direct pattern;
- admissible participant kinds and reference modes;
- any scope, time, evidence, or cross-local condition that changes this predicate or the named reuse; and
- the direct continuity or change rules, when that history is current.

Different exact local kinds, F.17 senses, scopes, or ReferencePlanes are handled by their applicable direct relations. Source difference alone creates no Bridge. A RelationSignature declares reusable content; the reusable form by itself neither asserts a current case nor establishes an occurrence.

#### A.6.6:4.4a - Claim-scoped non-kind predicate-base branch

When one identified derivation or criterion-selection claim uses exact claim content as its base, reuse A.6.6's endpoint, scope, time, witness, Bridge/loss, change, and overread discipline without pretending that a new relation kind or special base-declaration occurrence has been admitted. Identify the exact dependent `U.ClaimGraph`, exact nonempty selected base subgraph by value, the `derive` or `evaluate` mode, exact derivation or evaluation-and-selection claim identity, bounded receiving use, and effective reference scheme. Add an exact A.2.6 ClaimScope, temporal policy/domain, source or witness qualification, or cross-scheme Bridge and loss account only when that independently varying fact changes the assertion.

The assertion is ordinary C.2.1 claim content under `derivedUsingRuleContent` or `evaluatedAgainstRuleContent`. The dependent and base are predicate parameters, not automatically A.6.5 SlotSpecs, participants of a reusable relation occurrence, or an intrinsic `rule-bearing` classification. Same-scheme use adds no Bridge. A source edition, designation, acceptance/currentness fact, trace, or witness qualifies the assertion but does not enter semantic-base identity. Equal graphs under the same scheme count as one semantic base with multiple qualifications; a changed graph is another base.

Change only the fact that changed: declare or withdraw a selected base, repoint the dependent, rescope, retime, refresh witnesses, or change the predicate relation. A changed subject, content, mode, bounded use, actual-use claim, scope extension, temporal policy, or interpreted endpoint identifies another C.2.1 assertion. A claimed edition succession additionally requires the continuity conditions of C.2.1:4.5. Do not infer a new relation kind, occurrence, evidence result, Work, authority, or reliance from that change.

A basis-family analysis is a separate, optional C.2.1 episteme opened only for a named comparison, replay, material-conflict, or reliance receiver. Its candidate universe, evaluations, pairwise compatibility, temporal partition, established family, and disposition neither edit this reusable predicate declaration nor become fields of each actual-use assertion.

#### A.6.6:4.4.1 - Perspective and voice

State the relation in the shortest ordinary sentence that keeps both participants and direction recoverable: `TC-17 is calibrated to ITS-90` is valid. Functional or arrow notation may be added when it helps a formal receiver; it is not the default. Base-view wording is also valid when it preserves the same relation and direction. Do not turn `B validates X` into an inverse relation unless that inverse is independently defined.

#### A.6.6:4.5 - Lexical discipline

**Normative lexical rule.** In Tech or normative prose, do not use umbrella metaphors (`anchor`, `attach`, `ground`, or `support`) in place of the actual relation. Prefer an ordinary relation-specific sentence; add functional or arrow notation only when a named receiver benefits from it.

**Red-flag rule (`anchor*` as dependence metaphor).**
* In **Tech or normative** prose, rewrite `anchor*` as an ordinary relation-specific sentence, or move to the already reserved primitive that actually governs the claim.
* In **Plain or source** commentary, quoted umbrella wording may remain for traceability when the repaired sentence immediately names the actual relation. It must not be converted into a generic `validatedBy`, `verifiedBy`, `SupportRelation`, or metaphor-headed token.

**Carve-outs (pattern-defined primitives).** This red-flag rule does **not** ban uses where “anchoring” is already a *pattern-defined primitive* elsewhere in the spec, such as E.10 MG-DA token-to-EntityOfConcern anchoring or A.10 evidence anchors. It still acts as a review trigger: confirm you are using the reserved sense, not smuggling a basedness meaning.

**Naming guard for relation vocabulary.** Do not mint a new direct relation whose name merely preserves a metaphor such as `Anchor*`, `Ground*`, or `Attach*`. Name the actual relation kind and use the corresponding ordinary verb phrase. In an optional assertion record, the local `directRelationKind` field identifies that already admitted relation kind; the field is not another relation kind.
**Lane guard for meaning.** If the intent is “say what this expression means in this source”, do not introduce an `Anchor…` or `Ground…` relation. Recover the source-local claim under F.0.1; use F.17 only when a durable `SchemeSenseCell` or obtaining `LocalSenseBasisRelation` is actually needed. Semantic meaning assignment is not a base-declaration record.

**Grounding disambiguation rule.** If the prose says “grounded”, its actual ordinary or governed meaning MUST be recovered. The following branches illustrate distinct meanings, not an exhaustive classification:
* constructive grounding (`tv:groundedBy`, base is a trace),
* situational/empirical grounding (base is a grounding holon or experimental setup),
* source-local meaning lane (exact source, scheme, expression, local claim, and optional F.17 cell or basis relation; no special base-declaration object).

**Bind deconfliction note.** Do not use “bind/binding” as a synonym for declaring, refreshing, or changing an assertion or reusable relation declaration. This local edit vocabulary does not rename name binding or other already governed binding relations, including A.6.1 application bindings. Use the local declaration-change label only when a named receiver needs that history.

#### A.6.6:4.6 - Base-change operation lexicon

The following local labels classify changes to an optional assertion episteme or reusable declaration when a named receiver needs that history. They do not describe the beginning, ending, or change of the world-side relation itself, and an ordinary direct assertion needs none of them. In decision or publication use, preserve the prior episteme when changing its ClaimGraph, exact EntityOfConcern, or effective ReferenceScheme; such a change identifies another episteme. A representation-only edit need not do so. Claim edition continuity only when the C.2.1:4.5 rule and case facts establish it.

Operation classes (conceptual):
1. **declareBase** - create a new optional assertion with explicit `dependent`, `base`, `directRelationKind`, and `assertionPolarity`, or a new reusable declaration for that same already governed direct relation kind; add only the scope, time, evidence-use, or other qualifications that its direct predicate or named receiver needs.
2. **withdrawBaseDecl** — retire an assertion or declaration (or render it inapplicable by scope narrowing or time restriction, depending on the direct relation's declaration).
3. **rebase** — change `base` while keeping the same `dependent` and `directRelationKind` (legality depends on the direct relation's declaration; often requires witness refresh).
4. **repointDependent** — change `dependent` while keeping the same `base` and `directRelationKind`.
5. **rescope** — change `scope` (widen/narrow/translate) under the direct relation's scope rule; widening often triggers witness refresh.
6. **retime** — change `Γ_time` selector/policy when time matters; not a substitute for witness-timespan/freshness predicates.
7. **refreshWitnesses** — add/refresh witnesses/pins when decision use continues across time advances, scope widening, or evidence refresh.
8. **changeDirectRelationKind** — not an edit-in-place. Changing `directRelationKind` changes claim meaning; mint a new assertion or declaration rather than silently rewriting the kind. When edition history is needed, relate it to the prior episteme only if C.2.1:4.5's continuity rule and case facts establish that relation. Use F.13 for a separately current lexical-continuity claim.

**Relation to A.6.5 slot operations (non-normative mapping).** A project may realize an edit to an optional assertion or declaration through A.6.5 slot operations. The semantic account must still say which episteme field changed. A separately claimed change to the actual relation uses the direct relation's change rule and any current Work; it is never inferred from the record edit.

**Relation to E.18 assurance ops (informative).** On `U.Transfer`, `ConstrainTo`, `CalibrateTo`, `CiteEvidence`, and `AttributeTo` have their own declared meanings and constraints. A project may use the local declaration-change labels to describe changes in a represented assertion, but those labels neither subsume the E.18 operations nor create their relations.

#### A.6.6:4.7 - Disambiguation guide for selecting the direct relation

When a draft uses an umbrella phrase (“anchored”, “attached”, “grounded”), replace it with the direct relation that actually fits the claim:

| Colloquial intent | Direct relation or reading (illustrative) | Participants and conditions | Typical supporting material, when needed |
| --- | --- | --- | --- |
| “This ID refers to that thing” | **Identification** (`identifies`) | For “ID I identifies entity E”, name I and E. If the source means an entity-ref or slot-content value instead, name that actual referent. | issuance record, registry pin |
| “This thing is indexed by that ID” | **Indexing** (`indexedBy`) | Entity E is indexed by ID I; apply the actual indexing rule. | issuance record, registry pin |
| “This thing is registered” | **Registration** (`registeredIn`) | Recover the participant registered, its registry or registry entry, and the domain's registration predicate and direction. | issuance record, registry pin |
| “Make measurements comparable by calibration” | **Calibration** (`calibratedTo`) | Name the instrument, model, or output said to be calibrated and the applicable standard or datum; the domain's calibration rule must determine their roles. | calibration Work plus certificate pin |
| “This is the datum of that” | **Datum relation** (`datumOf`) | Recover what is the datum of what, and the applicable domain rule; `datumOf` does not supply the calibration or normalisation predicate. | the domain-required basis; calibration Work or certificate pin only if that rule needs it |
| “Make measurements comparable by normalisation” | **Normalisation** (`normalisedTo`) | Name what is normalised—an instrument, model, or output—and the standard or datum used; recover the normalisation predicate and direction from its domain rule. | the domain-required basis; calibration Work or certificate pin only if that rule needs it |
| “This result bears on that claim” | **Evidence use** under A.2.4, with A.10 only when replayable provenance or reliance is needed | dependent: result or other evidence episteme; base: target claim | exact evidence-use relation; producing Work, result binding, carrier, provenance, currentness, and reliance remain separate |
| “This edge is grounded in construction” | **Constructive grounding** (`tv:groundedBy`) | dependent: WM edge; base: constructor trace (`Γ_m`) | trace pins, edition pins |
| “This description is about X” | **Ordinary aboutness** under A.7/C.2.1 | description episteme and its exact EntityOfConcern X; aboutness alone does not establish a source-to-receiving construction | the source or describing relation required by the use |
| “Construct a view of the same entity” | **Viewing** (`viewedVia`) under A.6.3 | separately identified source and receiving epistemes, the same exact EntityOfConcern, and the construction rule | viewing pins |
| “Retarget a description to another entity” | **Retargeting** (`retargetedAlong`) under A.6.4 | separately identified source and receiving epistemes with different exact EntitiesOfConcern, the retargeting arrow `r`, and separate bounded-use assertion `q` | exact `r` and `q`, and a separate current-case judgement when that case is evaluated |
| “Allowed only under policy P” | **Constraint / policy** (`constrainedBy`, `permittedUnder`) | dependent: work-step / publication item; base: policy/rule | policy pin, waiver/work ref |
| “Property belongs to object” | **Attribution / aboutness** (`attributedTo`, `aboutEntity`, `characterises`) | dependent: property/abstraction; base: object | observation/derivation witnesses |
| “This expression means … in this source” | **Source-local meaning lane** (F.0.1; F.17 only when a durable address or basis relation is needed) | local expression and local-sense claim | exact source passage and, when current, an obtaining basis relation |

This table is illustrative. Each row keeps its own direct relation and governor; it is not a list of species of one universal base relation or record. Grammatical subject and object expose a sentence's direction but do not by themselves determine dependent/base allocation. Where the domain predicate or participant allocation is not supplied, recover it from the source or leave that local choice open; this guide does not define it. Ordinary aboutness and source-local meaning do not by themselves select a basedness or construction branch.

*Note.* A.6.3 defines the viewing arrow. A.6.4 keeps the retargeting arrow `r`, bounded-use assertion `q`, and current-case judgement separate: `q`'s ClaimGraph contains the invariant, visible loss, named receiving use, conditions, and affirmative or negative polarity; the judgement compares exact facts with `q` and returns exactly `satisfies`, `fails`, or `cannot decide`. A `cannot decide` judgement names the missing fact and reopen condition. This table directs those construction cases to their own patterns; it defines no second operator, arrow, assertion, judgement, application, or Work.

#### A.6.6:4.7a - Support wording selection test

When a draft uses `support`, `supported by`, `supporting`, `support basis`, `support relation`, or a support-headed compound, do not first choose a more formal synonym. Ask what assertion the next reader needs.

If the sentence is genuinely about basedness, write the smallest direct form:

```text
dependent stands in <direct relation> to base
```

Identify the actual participants and apply that direct predicate. Stop there when it answers the use. Add scope, time, an assertion record, a reusable `RelationSignature`, occurrence identity, or evidence only when the predicate or one named receiver needs it.

If the sentence is not basedness, use the matching ontology:

| Support wording means... | Use... |
| --- | --- |
| an episteme bears on a claim | the exact A.2.4 evidence-use relation; use A.10 when provenance, currentness, rival explanations, or bounded reliance must be replayed |
| a claim is acceptable for material reliance | A.10 for the actual bounded-reliance basis; B.3 only for a separately identified assurance claim, with the exact evidence-use relations kept separate |
| a causal, intervention, counterfactual, or simulation-only use is admissible | C.28 |
| a mathematical lens exposes preserved or lost structure | C.29 for that lens; C.26 only for its applicable quantum-like/contextual-model case; F.9 only for a separately obtaining correspondence between exact local sense cells; the direct mathematical pattern for the actual mathematical object or rule |
| one thing helps or enables work | the applicable work, resource, capability, or action relation, or ordinary Plain help |
| a file, section, packet, or companion helps a reader | E.17, E.11, I.2, or ordinary orientation |
| a source, model, diagram, or view describes something | A.7, C.2.1, E.17, and the direct describing or source-use relation |

Do not create `SupportRelation`, `SupportBasis`, `SupportRecord`, `validatedBy`, or `verifiedBy` as a fallback. Work, a result episteme, its carrier, provenance, evidence use, and later reliance remain separate.

