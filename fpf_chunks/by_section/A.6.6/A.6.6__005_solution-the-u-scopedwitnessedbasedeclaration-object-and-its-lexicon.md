---
chunk_kind: "child"
pattern_id: "A.6.6"
pattern_title: "Base Declaration Discipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)"
section_id: "A.6.6:4"
section_title: "Solution — The U.ScopedWitnessedBaseDeclaration object and its lexicon"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.6/A.6.6__005_solution-the-u-scopedwitnessedbasedeclaration-object-and-its-lexicon.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "A.6.6 — Base Declaration Discipline - Kind-explicit, scoped, witnessed base declaration discipline (with base-change lexicon)"
  - "A.6.6:4 — Solution — The U.ScopedWitnessedBaseDeclaration object and its lexicon"
line_start: 19357
line_end: 19570
dependencies:
  - "A.10"
  - "A.14"
  - "A.2.4"
  - "A.2.6"
  - "A.6.0"
  - "A.6.3"
  - "A.6.3-A.6.4"
  - "A.6.4"
  - "A.6.5"
  - "A.6.P"
  - "A.7"
  - "C.2.1"
  - "C.3.3"
  - "E.10"
  - "E.18"
  - "E.8"
  - "F.15"
  - "F.18"
  - "F.9"
keywords:
  - "SWBD"
  - "anchoring"
  - "base declaration"
  - "baseRelation"
  - "basedness"
  - "rebase"
  - "rescope"
  - "retime"
  - "scope"
  - "support-as-basedness"
  - "witnesses"
  - "Γ_time"
---

### A.6.6:4 - Solution — The `U.ScopedWitnessedBaseDeclaration` object and its lexicon

#### A.6.6:4.1 - Canonical object

**Definition.** A **`U.ScopedWitnessedBaseDeclaration`** (SWBD) is a first-class base-declaration value shape (a signature in the A.6.0/A.6.5 sense): it reifies “dependent is usable relative to base via baseRelation, under scope/time, witnessed by pins”.

```
U.ScopedWitnessedBaseDeclaration ::=
  〈 * DependentSlot     : SlotContent(VK_dep,  refMode_dep),
    * BaseSlot          : SlotContent(VK_base, refMode_base),
    * BaseRelationSlot  : SlotContent(U.NameToken, ByValue),     // relation-specific token; not free text; not publication-side object*
    * ScopeSlot         : SlotContent(U.Scope, ByValue),         // concretely: ClaimScope | WorkScope | PublicationScope
    * GammaTimeSlot?    : SlotContent(GammaTimePolicy, ByValue)?,
    * WitnessSetSlot?   : SlotContent(VK_wit,  refMode_wit)? 〉
 ```

Where:

* **`DependentSlot`** is the dependent content whose admissibility/usability/interpretation is being constrained.
* **`BaseSlot`** is the base, such as a reference frame, target, declared entity, standard, policy, or evidence carrier, that the dependent is declared relative to.
* **`BaseRelationSlot`** is a **declared relation/predicate/operator token** (a vocabulary element with a signature and relation-specific constraints) that states the precise kind of dependence. It is not a prose metaphor and is not a `publication-side object`/publication carrier.
* **`ScopeSlot`** is an explicit USM scope object (`U.Scope`): Claim scope (**G**), Work scope, or Publication scope.
* **`GammaTimeSlot`** is an explicit time selector/policy when time-dependent assumptions exist.
* **`WitnessSetSlot`** is a set of witness references/pins establishing justification or enforcement when the declaration is used for decisions.

**Notation.** `SlotContent(VK, refMode)` is a compact shorthand for “a slot whose SlotSpec declares `ValueKind=VK` and `refMode ∈ {ByValue | RefKind}` (A.6.5)”.

**SlotSpec note.** `VK_*`, `RK_*`, and `refMode_*` above are **not** “anything goes”: they are fixed by the selected `BaseRelationSlot` vocabulary entry and must be declared as SlotSpecs (A.6.5). In other words, SWBD is a reusable *shape*, but the selected local `baseRelation` declaration makes it a concrete, typed signature.

**Instance/prose notation note (convention).** In the prose and examples below, the slot fillers are written as `dependent`, `base`, `baseRelation`, `scope`, `Γ_time`, `witnesses` (no `*Slot` suffix). The `*Slot` suffix is reserved for SlotKinds/positions only (A.6.5 / E.10).

**Well-formedness constraints.**
* **WF‑BD‑1 (No kind-elision).** A base declaration is well-formed only if `BaseRelationSlot` is present and points to a declared vocabulary element with a known signature.
* **WF‑BD‑2 (No silent re-typing).** `DependentSlot` and `BaseSlot` type-check against the `baseRelation` vocabulary entry (ValueKinds + `refMode`). If the intended endpoint kinds do not match, the repair option is explicit (Bridge, narrowing, or explicit retargeting), rather than a rename.
* **WF‑BD‑3 (Time explicit when time matters).** If the declaration’s interpretation depends on time, `GammaTimeSlot` is explicit; “latest/current” is not a substitute.
* **WF‑BD‑4 (Decision use requires witnesses).** If the declaration is used for assurance, gating, or admissibility decisions, `WitnessSetSlot` is non-empty and resolvable.
* **WF‑BD‑5 (Edition fence for decision/publication).** An SWBD that is cited by PublicationScope or used for decision is immutable per edition: any permitted change class is represented as a new declaration linked via explicit continuity/withdrawal, not as an in-place rewrite.
* **WF‑BD‑6 (No silent cross-local reuse).** If an SWBD consumes a relation between different exact local kinds, distinct F.17 cells, translated scopes, or ReferencePlanes, it cites the applicable C.3.3, F.9, scope, or plane relation and the limits of the receiving use. Merely drawing dependent and base from different sources does not create a Bridge. No informal “it is the same entity anyway” prose is an admissible substitute.

This is the discipline-level analogue of A.6.5’s move: disambiguation is achieved by making the missing structural component explicit and non-optional in decision-relevant contexts.

#### A.6.6:4.2 - Underlying mathematical lens

SWBD reifies a **kind-labelled dependence arrow over a base**:

* a dependence edge **(dependent → base)**,
* labelled by a declared **relation token** (`baseRelation`),
* qualified by explicit **scope** and (when time matters) explicit **`Γ_time`**,
* optionally supported by a **witness set** (mandatory for decision use).

This “object over a base” lens is stable across disciplines:
calibration is “measurement over standard”, admissibility is “claim over evidence”, attribution is “property over object”, and constructive grounding is “edge over trace”.

#### A.6.6:4.3 - Slot discipline for SWBD

Any signature that introduces SWBD (or SWBD-like relations) SHALL define SlotSpecs per A.6.5: every position declares **SlotKind / ValueKind / RefKind-or-ByValue**.

Recommended canonical SlotKinds for SWBD:

* `DependentSlot`
* `BaseSlot`
* `BaseRelationSlot`
* `ScopeSlot`
* `GammaTimeSlot`
* `WitnessSetSlot`

**Slot vs filler guard.** `*Slot` names the **position** (SlotKind), not a container relation. In prose, say “fills `BaseSlot` with …” or “uses `baseRef` …” rather than calling the base itself “a BaseSlot”. (`Slot` suffix is structural; E.10.)

**Slot-level invariants (derived from WF‑BD‑1..4; testable).**
* **Invariant (SlotSpec completeness).** In any SWBD signature, the SlotSpec for `DependentSlot` and `BaseSlot` declares admissible `ValueKind` and `refMode` explicitly (A.6.5). If those types cannot be stated, the `baseRelation` vocabulary entry is not yet defined.
* **Invariant (Relation tokenness).** `BaseRelationSlot` holds a declared `U.NameToken` that resolves to a vocabulary entry with a known signature and relation-specific constraints (A.6.0 + A.6.5). It is not free text and is not typed as a publication-lane object (`publication-side object*`).
* **Invariant (Scope objectness).** `ScopeSlot` holds a `U.Scope` object (ClaimScope/WorkScope/PublicationScope) and is not replaced by “where it applies” prose.
* **Invariant (Time gating).** If time-dependent assumptions exist, the SWBD includes `GammaTimeSlot` carrying a `GammaTimePolicy` (WF‑BD‑3).
* **Invariant (Witness gating).** If the declaration participates in assurance/gating/admissibility decisions, the SWBD includes a non-empty, resolvable `WitnessSetSlot` (WF‑BD‑4).

**Field naming guard (implementation; informative).** When materialising SWBD as a record or representation, implementations SHOULD avoid naming data fields with the `*Slot` suffix. Prefer `dependentRef`, `baseRef`, `baseRelationRef`, `scope`, `gammaTime`, and `witnesses`, or the corresponding terms in the selected local declaration. `*Slot` remains reserved for SlotKinds and SlotSpecs (A.6.5).

#### A.6.6:4.4 - BaseRelation declaration

A `baseRelation` token is not “just a label”. For each selected local baseRelation declaration, its definition SHALL include:

* **Relation-end polarity.** Which end is dependent and which end is base (or declare symmetry explicitly).
* **Typing expectations.** Admissible ValueKinds and `refMode` for `DependentSlot` and `BaseSlot`.
* **Token discipline (LEX).** The token SHALL satisfy E.10 token-class morphology for relations/verbs; it SHALL NOT use metaphor heads (`Anchor*`, `Ground*`, `Attach*`) as a meaning-surrogate. If a source phrase must be retained for traceability, record it as source wording through F.18 naming discipline while keeping the relation-specific token specific.
* **Repair path for mismatches.** If an endpoint’s self-kind does not match the expected ValueKind, the allowed repairs are declared (KindBridge, explicit narrowing, or explicit retargeting); “renaming the endpoint” is not a repair.
* **Parameter placement.** Any additional qualifiers required by the relation kind (ranges, metrics, reference planes, policies) SHALL be represented either inside `scope` (preferred) or as explicit additional slots in an extended base-declaration signature; they MUST NOT be smuggled as adjectives on the endpoints.
* **Scope class.** Whether the declaration is claim-scoped (**G**), work-scoped, or publication-scoped.
* **Time discipline.** Whether `Γ_time` is required, optional, or forbidden for this relation kind.
* **Witness discipline.** Whether witnesses are always required versus required only for decision use, and what witness-use relations or pinned witness records are admissible: evidence-use relations, edition pins, calibration certificate pins, proof-bearing publications, or policy pins named by subject patterns.
* **Admissible change classes.** Which base-change operations are permitted (below) and what continuity requirements apply.
* **Cross-local and cross-plane policy.** State whether the relation may connect different exact local kinds, distinct F.17 cells, translated scopes, or ReferencePlanes. When it may, name the applicable C.3.3, F.9, scope, or plane relation, admitted use, and loss or limit; source difference alone is insufficient.

This mirrors A.6.5: a SlotKind without ValueKind/RefMode is underspecified; a baseRelation without its vocabulary entry is equally underspecified.

#### A.6.6:4.4a - Claim-scoped non-kind predicate-base branch

When one identified derivation or criterion-selection claim uses exact claim content as its base, reuse A.6.6's endpoint, scope, time, witness, Bridge/loss, change, and overread discipline without pretending that a base relation kind or SWBD occurrence has been admitted. Identify the exact dependent `U.ClaimGraph`, exact nonempty selected base subgraph by value, the `derive` or `evaluate` mode, exact derivation or evaluation-and-selection claim identity, bounded receiving use, and effective reference scheme. Add an exact A.2.6 ClaimScope, temporal policy/domain, source or witness qualification, or cross-scheme Bridge and loss account only when that independently varying fact changes the assertion.

The assertion is ordinary C.2.1 claim content under `derivedUsingRuleContent` or `evaluatedAgainstRuleContent`. The dependent and base are A.6.0 predicate parameters, not A.6.5 SlotSpecs, participants of a `BaseRelation`, or an intrinsic `rule-bearing` classification. Same-scheme use adds no Bridge. A source edition, designation, acceptance/currentness fact, trace, or witness qualifies the assertion but does not enter semantic-base identity. Equal graphs under the same scheme count as one semantic base with multiple qualifications; a changed graph is another base.

Change only the fact that changed: declare or withdraw a selected base, repoint the dependent, rescope, retime, refresh witnesses, or change the predicate relation. A changed subject, content, mode, bounded use, actual-use claim, scope extension, temporal policy, or interpreted endpoint creates the appropriate successor C.2.1 assertion. Do not infer a new relation kind, occurrence, evidence result, Work, authority, or reliance from that change.

A basis-family analysis is a separate, optional C.2.1 episteme opened only for a named comparison, replay, material-conflict, or reliance receiver. Its candidate universe, evaluations, pairwise compatibility, temporal partition, established family, and disposition neither edit this reusable predicate declaration nor become fields of each actual-use assertion.

#### A.6.6:4.4.1 - Perspective/voice discipline (dependent-view vs base-view)

**Normative rule.** In Tech / normative prose, authors SHALL express a based declaration in one of the following explicit forms:

* `baseRelation(dependent, base)` (functional notation), or
* `dependent --baseRelation--> base` (arrow notation).

Authors SHALL NOT use passive/umbrella voice (“X is anchored/grounded/attached”) as a substitute for an explicit `baseRelation(dependent, base)` form, because it invites direction flips and silent re-typing.

**Base-view is allowed only if the polarity is preserved.** If authors use base-view wording (“B validates X”), they SHALL either (i) keep both endpoints visible using the same polarity-preserving token (e.g., `validatedBy(X,B)`), or (ii) use an explicit inverse token that is declared in the baseRelation declaration. Authors SHALL NOT flip endpoint positions implicitly in prose.

#### A.6.6:4.5 - Lexical discipline

**Normative lexical rule.** In Tech / normative prose and Tech register naming, authors MUST NOT use umbrella metaphors (“anchor/anchoring”, “attach/attachment”, “ground/grounding”) as substitutes for an explicit `baseRelation` token.

**Red-flag rule (`anchor*` as dependence metaphor).**
* In **Tech / normative** prose: authors MUST treat `anchor*` as **prohibited** as a meaning-surrogate for an unnamed dependence kind. Authors SHALL rewrite into explicit `baseRelation(dependent, base)` form (or move to the correct reserved primitive lane).
* In **Plain / source** commentary only: authors MAY quote `anchor*` as a source umbrella only if it is immediately paired with an explicit baseRelation token (e.g., “source ‘anchored’ ⇒ `validatedBy(...)`”) and does not introduce a new relation-specific token.

**Carve-outs (pattern-defined primitives).** This red-flag rule does **not** ban uses where “anchoring” is already a *pattern-defined primitive* elsewhere in the spec, such as E.10 MG-DA token-to-EntityOfConcern anchoring or A.10 evidence anchors. It still acts as a review trigger: confirm you are using the reserved sense, not smuggling a basedness meaning.

**Naming guard for baseRelation tokens.** Do not mint new baseRelation tokens whose head noun is a metaphor (`Anchor*`, `Ground*`, `Attach*`). If you are tempted to do so, you either (i) have not named the relation kind yet, or (ii) are retaining source wording that must be recorded against an existing, more specific relation token through F.18.

Instead:
1) Name the **BaseRelation token** (declared vocabulary element), and
2) Use a **relation-specific verb phrase** that corresponds to that token.

**Lane guard for meaning.** If the intent is “say what this expression means in this source”, do not introduce a baseRelation named `Anchor…` or `Ground…`. Recover the source-local claim under F.0.1; use F.17 only when a durable `SchemeSenseCell` or obtaining `LocalSenseBasisRelation` is actually needed. Semantic meaning assignment is not expressed by SWBD.

**Grounding disambiguation rule.** If the prose says “grounded”, it MUST be rewritten into one of:
* constructive grounding (`tv:groundedBy`, base is a trace),
* situational/empirical grounding (base is a grounding holon or experimental setup),
* source-local meaning lane (exact source, scheme, expression, local claim, and optional F.17 cell or basis relation; not SWBD).

**Bind deconfliction note.** Authors MUST NOT use the verb “bind/binding” as a synonym for declaring/refreshing/changing a base declaration. “bind/binding” is reserved for **name binding** (LEX discipline). For SWBD edits, authors SHALL use the base‑change lexicon (below) instead.

#### A.6.6:4.6 - Base-change operation lexicon

As A.6.5 distinguishes slot operations by whether they change a stored reference, resolve a reference, or replace a value, A.6.6 distinguishes **base declaration changes** by which component changes and what semantics are affected.

Operation classes (conceptual):

These names denote **semantic change classes**. In decision/publication lanes, implementations MUST represent these changes by minting a new SWBD (new id/edition) and linking it to the prior one via explicit continuity/withdrawal (WF‑BD‑5 / CC‑BD‑10), rather than mutating the prior record.

1. **declareBase** — create a new base declaration with explicit `dependent`, `base`, `baseRelation`, `scope`, and, when applicable, `Γ_time`, plus witnesses when decision-relevant.
2. **withdrawBaseDecl** — retire a declaration (or render it inapplicable by scope narrowing or time restriction, depending on baseRelation declaration).
3. **rebase** — change `base` while keeping the same `dependent` and `baseRelation` (legality depends on the baseRelation declaration; often requires witness refresh).
4. **repointDependent** — change `dependent` while keeping the same `base` and `baseRelation`.
5. **rescope** — change `scope` (widen/narrow/translate) under the baseRelation’s scope rule; widening often triggers witness refresh.
6. **retime** — change `Γ_time` selector/policy when time matters; not a substitute for witness-timespan/freshness predicates.
7. **refreshWitnesses** — add/refresh witnesses/pins when decision use continues across time advances, scope widening, or evidence refresh.
8. **changeBaseRelation** — not an edit-in-place. Changing `baseRelation` changes meaning; mint a new declaration and relate them via an explicit continuity relation (F.13 discipline), rather than silently rewriting the kind.

**Relation to A.6.5 slot operations (non-normative mapping).** These are *semantic change classes*; an implementation may realise them using A.6.5 slot operations on the SWBD record fields. Example: a **rebase** may be implemented as a `retarget` of `baseRef` on a *new* SWBD edition. The point of A.6.6 is that “we retargeted a ref” is not the semantic story; “we rebased the declaration” is.

**Relation to E.18 assurance ops (informative).** On `U.Transfer`, the allowed ops—`ConstrainTo`, `CalibrateTo`, `CiteEvidence`, and `AttributeTo`—can be viewed as pattern-defined specialisations of `declareBase`, `rescope`, `rebase`, and `refreshWitnesses` for specific declared `baseRelation` readings, with stricter declared constraints and lintability.

#### A.6.6:4.7 - Disambiguation guide for selecting a baseRelation

When a draft uses an umbrella phrase (“anchored”, “attached”, “grounded”), replace it by selecting a declared `baseRelation` reading:

| Colloquial intent | Declared `baseRelation` reading (illustrative) | Dependent | Base | Typical witnesses |
| --- | --- | --- | --- | --- |
| “This ID refers to that thing” | **Identification / indexing** (`identifies`, `indexedBy`, `registeredIn`) | entity-ref / slot-content | identifier / registry entry | issuance record, registry pin |
| “Make measurements comparable” | **Calibration and datum** (`calibratedTo`, `datumOf`, `normalisedTo`) | instrument, model, or output | standard or datum | calibration work plus certificate pin |
| “This claim is admissible because …” | **Evidence admissibility** (`validatedBy`, `verifiedBy`) | claim | evidence carrier or proof | A.10/G.6 carrier, source-currentness, or provenance records; proof-bearing publications |
| “This edge is grounded in construction” | **Constructive grounding** (`tv:groundedBy`) | WM edge | constructor trace (`Γ_m`) | trace pins, edition pins |
| “This description is about X under a view” | **Viewing / retargeting (specialised)** (`viewedVia`, `retargetedAlong`) | episteme/view | selected EntityOfConcern | view operator pins, Bridge ids (if retargeting) |
| “Allowed only under policy P” | **Constraint / policy** (`constrainedBy`, `permittedUnder`) | work-step / publication item | policy/rule | policy pin, waiver/work ref |
| “Property belongs to object” | **Attribution / aboutness** (`attributedTo`, `aboutEntity`, `characterises`) | property/abstraction | object | observation/derivation witnesses |
| “This expression means … in this source” | **Source-local meaning lane** (F.0.1; F.17 only when a durable address or basis relation is needed) | local expression | local-sense claim | exact source passage and, when current, an obtaining basis relation |

This table is illustrative; the discipline requirement is that the chosen baseRelation be explicit, declared, and relation-specific. The “Meaning lane” row is included only as a **do-not-model-with-SWBD** reminder.

*Note.* The `viewedVia` / `retargetedAlong` operators are defined by the A.6.3/A.6.4 viewing/retargeting patterns; this table only classifies them as “relative-to-base” cases.

#### A.6.6:4.7a - Support wording selection test

When a draft uses `support`, `supported by`, `supporting`, `support basis`, `support relation`, or a support-headed compound, do not first choose a nicer synonym. First decide whether the phrase is a based declaration.

A support phrase is governed by A.6.6 only when all of the following can be stated:

```text
dependent:
base:
baseRelation:
scope:
Γ_time?, if time matters:
witnesses?, if decision/publication/admissibility use is live:
admissibleUse:
nonAdmissibleUse:
```

If these fields can be stated, rewrite the phrase as `baseRelation(dependent, base)` or `dependent --baseRelation--> base` and use an SWBD or a selected local SWBD specialization. Examples include `validatedBy(claim, evidenceCarrier)`, `calibratedTo(measurementOutput, standard)`, `normalisedTo(metric, datum)`, `attributedTo(propertyClaim, selectedEntity)`, `aboutEntity(description, entityOfConcern)`, and `permittedUnder(workStep, policy)`.

If these fields cannot be stated, do not create a `SupportRelation`, `SupportBasis`, `SupportRecord`, or local support-headed type. Classify by reading and apply the matching ontology:

| Support wording means... | Governing ontology to apply |
| --- | --- |
| a source, model, diagram, publication, or view describes, constrains, or exposes something | source-description, specification-use, and publication patterns (`A.7`, `A.6.3`, `A.6.2`, `C.2.3`, `E.17`, local source rules) |
| an observation, test, proof, carrier, or source phrase such as *evidence role* says that an episteme bears on a claim | recover the exact bounded evidence-use, status-use, provenance, or support relation through `A.2.4`, `A.10`, or `G.6`; a separately obtaining system-role classification or assignment may itself be evidence only through another evidence-use fact |
| a claim is acceptable in an assurance or trust calculus | assurance patterns (`B.3`) plus evidence ontology named by value when evidence is live |
| a causal, intervention, counterfactual, off-policy, or simulation-only use is admissible | causal-use pattern (`C.28`) |
| a mathematical lens, mapping, or model makes a use admissible or exposes preserved/lost structure | mathematical-lens patterns (`C.29`, `C.26`, `F.9`) |
| a metric, score, threshold, benchmark, or characteristic warrants a comparison | measurement/characteristic/comparison patterns (`C.16`, `C.25`, `G.9`) |
| one thing helps work, enables an action, supplies a resource, or makes operation easier | work/resource/action patterns (`A.15`, `A.15.4`, `A.6.A`, `C.11`) or ordinary Plain help |
| one file, section, packet, companion, entry cue, or expanded case helps a reader find, inspect, or compare another item | publication, entry, or navigation patterns (`E.17`, `E.11`, `I.2`) or ordinary orientation |

This test prevents support wording from becoming either a source-relation bucket or a basis bucket. A.6.6 governs only the support cases that are genuinely base-relative.

