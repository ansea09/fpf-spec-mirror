---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
section_id: "A.6.6:4"
section_title: "Solution - State the direct relation, then add only what the receiving use needs"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__005_solution-state-the-direct-relation-then-add-only-what-the-receiving-use-needs.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "A.6.6 — Base Declaration Discipline - Direct relation first; reusable declaration only when needed"
  - "A.6.6:4 — Solution - State the direct relation, then add only what the receiving use needs"
line_start: 19647
line_end: 19811
dependencies:
  - "A.10"
  - "A.14"
  - "A.2.4"
  - "A.6.0"
  - "A.6.3"
  - "A.6.4"
  - "A.6.5"
  - "A.6.6"
  - "A.6.REL"
  - "C.2.1"
  - "E.10"
  - "F.17"
  - "F.18"
  - "F.9"
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
- open a reusable declaration only when at least two named consumers need the same participant meanings, predicate, laws, and applicability.

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

This is a representation of claim content, not a public kind, `RelationSignature`, or world-side occurrence. `directRelationKind` resolves to an already governed relation kind; the assertion is true only when that relation's predicate is satisfied for the actual participants. `scope` and `gammaTime` are present only when the direct relation or named use needs them. `evidenceUseRefs`, when present, resolve to exact A.2.4 evidence-use relations for this assertion. The evidence epistemes, producing Work, operation result, carrier, provenance, currentness, and later reliance remain separately identified under A.2.4 and A.10.

The record's C.2.1 identity follows its complete ClaimGraph, exact EntityOfConcern, and effective ReferenceScheme. Revising the record changes an episteme. It does not by itself begin, end, or alter the world-side relation it describes.

#### A.6.6:4.2 - Direct relation and optional assertion are different objects

The useful stable picture is a direct arrow in ordinary reading:

> dependent **stands in the named direct relation to** base.

The arrow is not a generic mathematical constructor. Its participant meanings, predicate, applicability, and occurrence identity come from the selected direct relation pattern. A scoped assertion episteme may state that this predicate holds, and evidence may support reliance on that assertion. Neither the assertion nor its evidence makes the relation obtain.

Calibration, attribution, policy dependence, constructive grounding, and other cases therefore remain different relation kinds. A.6.6 supplies a recovery discipline, not one universal `BaseRelation` kind.

#### A.6.6:4.3 - Reusable declaration only for a named reuse

Use the direct relation's A.6.0 `RelationSignature` only after the relation kind is already admitted and at least two named consumers need the same reusable declaration content. That signature states the participant meanings, predicate, applicability, and occurrence-identity rule. A.6.5 SlotSpecs belong inside that reusable declaration; they are not required in an ordinary one-case assertion.

If no direct pattern supplies the relation kind, participants, or predicate, keep the exact local claim or return the A.6.RCD `missing-governor` result. Do not repair the gap by minting a generic `BaseRelation` kind or token, SlotSpecs, or a scoped-record type.

#### A.6.6:4.4 - What a reusable direct-relation declaration must say

For a named receiving use that genuinely needs a `RelationSignature`, the direct relation definition states:

- the dependent and base participant meanings and direction or symmetry;
- the obtaining predicate and applicability;
- the occurrence-identity rule when occurrence identity is used;
- admissible participant kinds and reference modes;
- any scope, time, evidence, or cross-local condition that changes this predicate or the named reuse; and
- the direct continuity or change rules, when that history is current.

Different exact local kinds, F.17 senses, scopes, or ReferencePlanes are handled by their applicable direct relations. Source difference alone creates no Bridge. A RelationSignature declares reusable content; it neither asserts a current case nor creates an occurrence.

#### A.6.6:4.4a - Claim-scoped non-kind predicate-base branch

When one identified derivation or criterion-selection claim uses exact claim content as its base, reuse A.6.6's endpoint, scope, time, witness, Bridge/loss, change, and overread discipline without pretending that a new relation kind or special base-declaration occurrence has been admitted. Identify the exact dependent `U.ClaimGraph`, exact nonempty selected base subgraph by value, the `derive` or `evaluate` mode, exact derivation or evaluation-and-selection claim identity, bounded receiving use, and effective reference scheme. Add an exact A.2.6 ClaimScope, temporal policy/domain, source or witness qualification, or cross-scheme Bridge and loss account only when that independently varying fact changes the assertion.

The assertion is ordinary C.2.1 claim content under `derivedUsingRuleContent` or `evaluatedAgainstRuleContent`. The dependent and base are predicate parameters, not automatically A.6.5 SlotSpecs, participants of a reusable relation occurrence, or an intrinsic `rule-bearing` classification. Same-scheme use adds no Bridge. A source edition, designation, acceptance/currentness fact, trace, or witness qualifies the assertion but does not enter semantic-base identity. Equal graphs under the same scheme count as one semantic base with multiple qualifications; a changed graph is another base.

Change only the fact that changed: declare or withdraw a selected base, repoint the dependent, rescope, retime, refresh witnesses, or change the predicate relation. A changed subject, content, mode, bounded use, actual-use claim, scope extension, temporal policy, or interpreted endpoint creates the appropriate successor C.2.1 assertion. Do not infer a new relation kind, occurrence, evidence result, Work, authority, or reliance from that change.

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

**Grounding disambiguation rule.** If the prose says “grounded”, it MUST be rewritten into one of:
* constructive grounding (`tv:groundedBy`, base is a trace),
* situational/empirical grounding (base is a grounding holon or experimental setup),
* source-local meaning lane (exact source, scheme, expression, local claim, and optional F.17 cell or basis relation; no special base-declaration object).

**Bind deconfliction note.** Do not use “bind/binding” as a synonym for declaring, refreshing, or changing an assertion or reusable relation declaration. “Bind/binding” remains reserved for name binding. Use the local declaration-change label only when a named receiver needs that history.

#### A.6.6:4.6 - Base-change operation lexicon

The following local labels classify changes to an optional assertion episteme or reusable declaration when a named receiver needs that history. They do not describe the beginning, ending, or change of the world-side relation itself, and an ordinary direct assertion needs none of them. In decision or publication use, editing the assertion or declaration creates a successor episteme under its own identity and continuity rules rather than silently mutating the prior edition.

Operation classes (conceptual):
1. **declareBase** - create a new optional assertion with explicit `dependent`, `base`, `directRelationKind`, and `assertionPolarity`, or a new reusable declaration for that same already governed direct relation kind; add only the scope, time, evidence-use, or other qualifications that its direct predicate or named receiver needs.
2. **withdrawBaseDecl** — retire an assertion or declaration (or render it inapplicable by scope narrowing or time restriction, depending on the direct relation's declaration).
3. **rebase** — change `base` while keeping the same `dependent` and `directRelationKind` (legality depends on the direct relation's declaration; often requires witness refresh).
4. **repointDependent** — change `dependent` while keeping the same `base` and `directRelationKind`.
5. **rescope** — change `scope` (widen/narrow/translate) under the direct relation's scope rule; widening often triggers witness refresh.
6. **retime** — change `Γ_time` selector/policy when time matters; not a substitute for witness-timespan/freshness predicates.
7. **refreshWitnesses** — add/refresh witnesses/pins when decision use continues across time advances, scope widening, or evidence refresh.
8. **changeDirectRelationKind** — not an edit-in-place. Changing `directRelationKind` changes claim meaning; mint a new assertion or declaration and relate it to the prior one through an explicit continuity relation (F.13 discipline), rather than silently rewriting the kind.

**Relation to A.6.5 slot operations (non-normative mapping).** A project may realize an edit to an optional assertion or declaration through A.6.5 slot operations. The semantic account must still say which episteme field changed. A separately claimed change to the actual relation uses the direct relation's change rule and any current Work; it is never inferred from the record edit.

**Relation to E.18 assurance ops (informative).** On `U.Transfer`, `ConstrainTo`, `CalibrateTo`, `CiteEvidence`, and `AttributeTo` have their own declared meanings and constraints. A project may use the local declaration-change labels to describe changes in a represented assertion, but those labels neither subsume the E.18 operations nor create their relations.

#### A.6.6:4.7 - Disambiguation guide for selecting the direct relation

When a draft uses an umbrella phrase (“anchored”, “attached”, “grounded”), replace it with the direct relation that actually fits the claim:

| Colloquial intent | Direct relation (illustrative) | Dependent | Base | Typical supporting material, when needed |
| --- | --- | --- | --- | --- |
| “This ID refers to that thing” | **Identification / indexing** (`identifies`, `indexedBy`, `registeredIn`) | entity-ref / slot-content | identifier / registry entry | issuance record, registry pin |
| “Make measurements comparable” | **Calibration and datum** (`calibratedTo`, `datumOf`, `normalisedTo`) | instrument, model, or output | standard or datum | calibration work plus certificate pin |
| “This result bears on that claim” | **Evidence use** under A.2.4, with A.10 only when replayable provenance or reliance is needed | result or other evidence episteme | target claim | exact evidence-use relation; producing Work, result binding, carrier, provenance, currentness, and reliance remain separate |
| “This edge is grounded in construction” | **Constructive grounding** (`tv:groundedBy`) | WM edge | constructor trace (`Γ_m`) | trace pins, edition pins |
| “This description is about X under a view” | **Viewing / retargeting (specialised)** (`viewedVia`, `retargetedAlong`) | episteme/view | exact source and receiving episteme and EntityOfConcern values | viewing pins, or the exact A.6.4 arrow r and separate use assertion q |
| “Allowed only under policy P” | **Constraint / policy** (`constrainedBy`, `permittedUnder`) | work-step / publication item | policy/rule | policy pin, waiver/work ref |
| “Property belongs to object” | **Attribution / aboutness** (`attributedTo`, `aboutEntity`, `characterises`) | property/abstraction | object | observation/derivation witnesses |
| “This expression means … in this source” | **Source-local meaning lane** (F.0.1; F.17 only when a durable address or basis relation is needed) | local expression | local-sense claim | exact source passage and, when current, an obtaining basis relation |

This table is illustrative. Each row keeps its own direct relation and governor; it is not a list of species of one universal base relation or record. The meaning row remains only a do-not-model-as-basedness reminder.

*Note.* A.6.3 and A.6.4 define the viewing or retargeting arrow and any separate use claim. This table only classifies their references as relative-to-base cases; it defines no second operator, arrow, application, or use assertion.

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
| a claim is acceptable for material reliance | B.3, with the exact evidence relations kept separate |
| a causal, intervention, counterfactual, or simulation-only use is admissible | C.28 |
| a mathematical lens exposes preserved or lost structure | C.29, C.26, F.9, or the direct mathematical pattern |
| one thing helps or enables work | the applicable work, resource, capability, or action relation, or ordinary Plain help |
| a file, section, packet, or companion helps a reader | E.17, E.11, I.2, or ordinary orientation |
| a source, model, diagram, or view describes something | A.7, C.2.1, E.17, and the direct describing or source-use relation |

Do not create `SupportRelation`, `SupportBasis`, `SupportRecord`, `validatedBy`, or `verifiedBy` as a fallback. Work, a result episteme, its carrier, provenance, evidence use, and later reliance remain separate.

