---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
section_id: "A.6.3.RT:4"
section_title: "Solution — entityOfConcernRef-preserving representation-scheme transition under A.6.3"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__005_solution-entityofconcernref-preserving-representation-scheme-transition-under-a-6-3.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "A.6.3.RT — Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
  - "A.6.3.RT:4 — Solution — entityOfConcernRef-preserving representation-scheme transition under A.6.3"
line_start: 13305
line_end: 13585
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.NAR"
  - "A.6.4"
  - "A.7"
  - "B.3"
  - "B.5.2"
  - "C.2.7"
  - "C.26"
  - "C.27"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.18"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
---

### A.6.3.RT:4 - Solution — entityOfConcernRef-preserving representation-scheme transition under `A.6.3`

#### A.6.3.RT:4.1 - Informal definition

> `RepresentationSchemeTransition` is a named pattern specialized under `A.6.3 U.EpistemicViewing` for entityOfConcernRef-preserving transitions across declared representation schemes.
>
> It preserves `entityOfConcernRef`, keeps the representation change effect-free, and makes explicit what changes in representation factors, reasoning medium, recoverability, and loss profile.
>
> It may move between prose, table, diagram, structured notation, or another declared representation regime. It may not silently change the EntityOfConcern, silently import bridge semantics, or treat decode-mediated structure as if it were directly given.

#### A.6.3.RT:4.1.a - Pattern, case, and published rendering distinction

`RepresentationSchemeTransition` is a **pattern description** and a named specialization under `A.6.3`. Concrete entityOfConcernRef-preserving representation changes are passive episteme cases or published renderings reviewed under this pattern; the pattern itself does not act, decide, or publish.

This distinction matters because the pattern governs **how** a representation change is recognised, justified, and checked. It does **not** turn every table, diagram, or structured notation into a giant standalone review artifact, and it does not reduce review to a mechanical reformatting step.

#### A.6.3.RT:4.1.a.1 - Concrete transition relation

`RepresentationSchemeTransition` names the method pattern. `RepresentationSchemeTransitionRelation@Context` is a context-dependent local species of `U.Relation` between a source representation episteme and a receiving representation episteme about the same EntityOfConcern. The relation is not the pattern, the dated work that produced a rendering, or the episteme that describes the transition. No new root U-kind is introduced.

```text
RepresentationSchemeTransitionRelation@Context <: U.Relation:
  BoundedContextSlot = <TransitionBoundedContextSlot, U.BoundedContext, U.BoundedContextRef>
  PreservedEntityOfConcernSlot = <PreservedEntityOfConcernSlot, U.Entity, U.EntityRef>
  SourceRepresentationSlot = <SourceRepresentationSlot, U.Episteme, U.EpistemeRef>
  ReceivingRepresentationSlot = <ReceivingRepresentationSlot, U.Episteme, U.EpistemeRef>
  SourceRepresentationSchemeDescriptionSlot = <SourceRepresentationSchemeDescriptionSlot, U.Episteme, U.EpistemeRef>
  ReceivingRepresentationSchemeDescriptionSlot = <ReceivingRepresentationSchemeDescriptionSlot, U.Episteme, U.EpistemeRef>
  direction = SourceRepresentationSlot -> ReceivingRepresentationSlot
```

These six SlotSpecs plus the stated direction are the exact `RelationSignature` for this local relation species. The relation depends on the bounded context and on both representation epistemes. Its identity is the tuple of bounded context, preserved EntityOfConcern, source representation edition, receiving representation edition, and declared pair of source and receiving schemes. A new carrier, layout, loss explanation, or publication edition does not by itself create a new relation. A changed endpoint edition, EntityOfConcern, context, or scheme pair does. A relation instance is referenced through a `U.EntityRef` constrained to `RepresentationSchemeTransitionRelation@Context`.

A separate episteme describes the relation and its use boundaries:

```text
RepresentationSchemeTransitionDescription@Context <: U.Episteme:
  boundedContextRef: U.BoundedContextRef
  entityOfConcernRef: U.EntityRef, referencing one RepresentationSchemeTransitionRelation@Context
  viewpointRef: U.ViewpointRef
  subjectRef: U.SubjectRef, decoding to <entityOfConcernRef, boundedContextRef, viewpointRef>
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  sourceRelationReferenceEpistemeRefs[1..*]: U.EpistemeRef, each referencing one RepresentationTransitionSourceRelationReference@Context
  preservedClaimRefs[]: U.EpistemeRef
  preservedCommitmentRefs[]?: U.EntityRef, each referencing one U.Commitment
  representationSchemeDeltaDescriptionRef: U.EpistemeRef
  reasoningMediumDeltaDescriptionRef?: U.EpistemeRef
  representationLossDescriptionRef?: U.EpistemeRef
  recoverabilityDescriptionRef?: U.EpistemeRef
  admissibleUseDescriptionRef: U.EpistemeRef
  nonAdmissibleDownstreamUseDescriptionRef: U.EpistemeRef
  returnConditionDescriptionRef: U.EpistemeRef
  changedClaimGoverningPatternRef?: U.EntityRef, referencing one U.MethodDescription

RepresentationTransitionSourceRelationReference@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one exact source relation instance
  entityOfConcernKindRef: U.KindRef
  boundedContextRef: U.BoundedContextRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  transitionRelationRef: U.EntityRef, referencing one RepresentationSchemeTransitionRelation@Context
  relationSignatureRef: U.EntityRef, referencing one U.Signature
  directGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
```

`RepresentationTransitionSourceRelationReference@Context` is a reference-bearing episteme whose EntityOfConcern is one exact source relation instance. It is not that relation. It can itself be cited through `U.EpistemeRef`. Its EntityOfConcern ref, exact kind ref, signature ref, transition-relation ref, and governing-pattern ref are all required and mutually consistent.

The source and receiving relation endpoints are description epistemes or episteme publications about the same named EntityOfConcern. The transition-description episteme keeps each actual source relation, exact kind, signature, and direct governing pattern recoverable instead of replacing them with provenance prose.

`representationSchemeDeltaDescriptionRef` is always present. `reasoningMediumDeltaDescriptionRef` is present only when the receiving representation changes what can be inspected, compared, or replayed. At least one of `representationLossDescriptionRef` and `recoverabilityDescriptionRef` is present; both are present when the transition loses distinctions and also claims a recovery route.

`admissibleUseDescriptionRef` says what the receiving representation supports now. `nonAdmissibleDownstreamUseDescriptionRef` says which stronger use has not been established. `returnConditionDescriptionRef` identifies when the user returns to the source representation or exact source relations. If the attempted downstream claim changes, `changedClaimGoverningPatternRef` identifies the method pattern that governs that claim.

A changed EntityOfConcern exits to A.6.4. A narrower receiving result that needs its own loss and return account exits to A.6.3.CSC. Narrative ordering exits to A.6.3.NAR. Evidence, assurance, gate, commitment, bridge, work, and architecture uses each use their own governing relation.

#### A.6.3.RT:4.1.b - Local working vocabulary

Use this vocabulary only after the ordinary use field set leaves ambiguity or a claim-bearing relation-change question. Ordinary text-to-table, table-to-diagram, or diagram-to-notation cases do not need every term below; use only the term that changes the next representation decision or blocks a concrete overclaim.
- **Representation scheme** = the published form in which the same entity is rendered (for example prose, table, diagram, or structured notation).
- **Reasoning medium** = the form-specific inspection possibilities users actually use when inspecting the published rendering.
- **Semiotic mode** = which meaning-bearing relation is doing the main work in the rendering, such as structural likeness, trace relation, index relation, conventional code, model-mediated correspondence, or decode-mediated recoverability.
- **Factor delta** = the explicit change in representation factors that matters for review.
- **Source-relation chain** = the visible source relation back to pinned or otherwise reviewable source `U.Episteme` claim graph that keeps same-EntityOfConcern continuity honest.
- **Decode-mediated case** = a case where explicit access to the receiving representation depends on a declared decoding relation rather than direct interpretation from an already published source episteme or source publication.
- **actionabilityShift** = a changed user action-possibility interpretation or apparent readiness created by the rendering. It is not execution authority, gate status, action invitation, work authority, or proof that work may proceed.
- **recoverabilityEvidenceClass** = a local review field naming the recoverability evidence needed for decode-mediated or latent cases. It is not an `EvidenceKind`; it remains absent for an ordinary non-latent representation shift unless recoverability is part of the question under repair.
- **representationAdmissibilityValue** = a local admissibility value used only when the representation shift is disputed, assurance-facing, gate-adjacent, externally relied on, decode-mediated, or likely to invite gate, evidence, work, or authority use beyond declared admissible use. It says which use the shifted representation makes admissible now; it is not a score, ordered rank, improvement scale, ontology class, evidence class, or `authoritySourceRef` destination.
- **sourceRelationClass** = the shared `E.17:5.1b` vocabulary used beside representation-admissibility value when the source relation itself is disputed or claim-bearing: pointer-only, available, retrieved, used, faithful, claim-admissible, claim-non-admissible, claim-contradicted, claim-plausible-only, source-omitted, source-loss-declared, claim-widened, added-linkage, independent-verification-present, admissible-for-this-use, downstream-use-forbidden, or reopen-trigger-present.

| representationAdmissibilityValue | Admissible use | Relation-set completeness condition | Shortcut rejected |
| --- | --- | --- | --- |
| `readability-only` | Inspection, discussion, source-finding, or planning preparation. | Source-relation chain and non-admissible downstream-use line. | Clearer rendering means a wider claim. |
| `source-recoverable` | Receiving-side relations can be traced back to source-relation records. | Source-relation records, loss and provenance note, and recoverability statement. | Receiving form replaces source relation. |
| `structure-preserving` | Technical review of preserved relation structure. | Declared relation structure, preservation witness, and no-new-claim check. | Diagram form or topology defines ontology by form. |
| `decode-bounded` | Bounded decode-mediated report or review. | Decode relation, `recoverabilityEvidenceClass`, and recoverability scope. | Readable decode output is direct givenness. |
| `probe-bounded` or `intervention-bounded` | Bounded representation-to-property or representation-to-behavior claim. | Probe evidence, intervention evidence, or causal-abstraction relation that names the declared admissible use. | Probe confidence or intervention success becomes general ontology. |
| `bridge-bounded-source-equivalence` | Equivalence, substitution, or bridge use only where another governing pattern supplies it. | Existing bridge, equivalence, or substitution record outside RT, with the governing pattern named. | RT itself grants source equivalence or substitution. |

**Recoverability-for-use rule.** If the declared admissible use is inspection, source-finding, comparison, or technical review, `RepresentationSchemeTransition` can close with entityOfConcernRef-preserving preservation, source-relation chain, representation-scheme delta, and loss or recoverability notes. If the declared admissible use is work-planning preparation, this pattern is admissible only for reversible preparation until `A.15` supplies the role, method, plan, and work source relation. Evidence or currentness, gate or release, assurance, commitment, bridge or substitution, and engineering-justification uses are admitted only when the case names the downstream governing source relation; otherwise the receiving representation remains orientation or review use only.

These terms are local review aids. They inherit the `E.17:5.1e` local-field rule: they do not create `U.Kind`, `publication-face kind`, `RelationKind`, `KindBridge`, `MechanismKind`, `EvidenceKind`, project-side FPF kind and reference named by value, new face family, or new ontology governing pattern.

#### A.6.3.RT:4.2 - Scope and exclusions

**In scope**
- text-to-table shift over the same EntityOfConcern;
- table-to-diagram shift over the same EntityOfConcern;
- diagram-to-structured-notation shift where the represented entity and claim-bearing source episteme stay preserved;
- functional-description diagrams, tables, screens, or notations when the same EntityOfConcern remains fixed and the main change is representation scheme or reasoning medium;
- other same-entity representation-scheme changes with explicit recoverability discipline.

**Out of scope**
- any change of `entityOfConcernRef` or hidden change of EntityOfConcern (`A.6.4`);
- explanation-facing renderings whose main purpose is didactic or explanatory rendering work (`ExplanationFaithfulnessProfile`);
- purely textual rewrites that stay inside one representation regime (`ConservativeRetextualization`);
- carrier work such as rendering, export, upload, serialization, OCR-style extraction, or parsing-style extraction;
- latent-representation use or distributed-representation use without pinned source claim or publication, decoding relation or access relation, recoverability evidence, admissible-use value, and remaining user action.

#### A.6.3.RT:4.2.a - User guidance

Use this pattern when the EntityOfConcern stays fixed but the published result changes representation scheme or reasoning medium.
- If only wording changes, stay in `ConservativeRetextualization`.
- If the receiving rendering mainly teaches, narrates, or explains, apply ExplanationFaithfulnessProfile.
- If same-EntityOfConcern continuity fails, apply A.6.4.
- Stay here when changed representation scheme or reasoning medium remains the primary review question, even if some loss is present.
- If the receiving representation stays honest only by carrying its own narrower-use card, declared source-loss mode, non-admissible downstream-use line, and a condition for return to the exact source representation or source relations, apply A.6.3.CSC Controlled Semantic Coarsening; do not keep the case here as ordinary representation-scheme transition.

#### A.6.3.RT:4.2.b - What the user checks first

A user usually starts with five questions:
1. Is the EntityOfConcern still the same, or has the EntityOfConcern shifted?
2. What changed in representation scheme and reasoning medium?
3. Can the receiving rendering still state a source-relation chain back to a pinned source episteme or source publication with enough specificity for the declared admissible use?
4. Has the case quietly become explanation, bridge-bearing comparison, retargeting, or carrier work?
5. If decoding is involved, is the evidence class adequate for the declared admissible use rather than only for readable review?

If the representation shift is no longer the main review problem, and the receiving rendering instead stays honest only by carrying a narrower-use card with non-admissible downstream use and reopen duty, the case has crossed out of ordinary representation-scheme transition even if the new form still looks like a neat table, diagram, or notation. Use `A.6.3.CSC Controlled Semantic Coarsening` for that source-to-rendering relation.

Here, **return to source relations** means returning to the exact source representation or source relations, while **changed governing-pattern claim** means that the now-attempted explanation, retargeting, bridge, work, evidence, gate, assurance, temporal, dynamics, carrier, or transformation-flow claim is governed by a named pattern. A coarsened representation may need both.

Only after these questions are answered clearly does a fuller claim-bearing continuity-review field set normally become necessary.

#### A.6.3.RT:4.3 - Working-model first; explicit continuity-review field set only when the case is claim-bearing

Most entityOfConcernRef-preserving representation shifts stay human-usable and reviewable without turning every table, diagram, or structured rendering into a giant metadata block. This pattern therefore follows **E.14's working-model-first discipline**: ordinary non-latent cases need enough explicitness to show what stayed the same, what changed in representation and reasoning medium, what was lost or foregrounded, and when another governing pattern governs the case.

**Ordinary case (default).** For everyday entityOfConcernRef-preserving representation shifts, it is usually enough that the rendering or its surrounding publication keeps explicit:
- the source representation or source episteme publication, the receiving representation or rendering, and the statement that one `entityOfConcernRef` is preserved;
- the source `U.Episteme` claim or commitment preserved for the intended use;
- the representation scheme, reasoning medium, or expression-form delta;
- the remaining admissible user action and the downstream use not made admissible by this representation shift.

That ordinary field set is the default. It is admissible for inspection, source-finding, comparison, technical review, or reversible planning preparation. It does not by itself license work authority, evidence force, gate passage, assurance force, bridge substitution, abductive selection, temporal currentness, dynamics currentness, or transformation-flow currentness.

**Fuller continuity-review field set (only for claim-bearing cases).** A fuller field set is warranted when the case is disputed, externally relied on, cross-context, correspondence-heavy, decode-mediated, assurance-facing, gate-adjacent, used to justify work preparation, used in abductive return to source hypotheses, or relied on for temporal, dynamics, or transformation-flow currentness. It may inherit pattern ids and already-pinned metadata instead of restating them inline. When published, it makes these fields recoverable:

| Field | Interpretation in this pattern |
| --- | --- |
| `entityOfConcernRef` | The exact `RepresentationSchemeTransitionRelation@Context` described by this episteme. Resolving it recovers the bounded context, preserved EntityOfConcern, source and receiving representation epistemes, and source and receiving scheme descriptions from the relation signature. |
| `sourceRelationReferenceEpistemeRefs[]` | Episteme references for every actual source relation needed for the declared use, including grounding, viewpoint, view, provenance, or publication relations when they are load-bearing; each referenced episteme keeps the relation value, exact kind, relation signature, and direct governing pattern. |
| `preservedClaimRefs[]` | Source claims that the receiving representation still carries for the declared use. |
| `preservedCommitmentRefs[]?` | Source commitments that remain preserved when a commitment is actually current; otherwise this position is absent. |
| `representationSchemeDeltaDescriptionRef` | What changed between the source and receiving representation schemes. |
| `reasoningMediumDeltaDescriptionRef?` | What changed in inspection, comparison, inference, or replay affordance when reasoning medium changed; absent when no such change is claimed. |
| `representationLossDescriptionRef?` | Lost, narrowed, foregrounded, or rearranged distinctions and any counter-witness that weakens continuity. |
| `recoverabilityDescriptionRef?` | Why continuity remains reviewable, which source relations recover omitted content, and what evidence supports recovery for the declared use. |
| `admissibleUseDescriptionRef` | What the receiving representation supports now. |
| `nonAdmissibleDownstreamUseDescriptionRef` | Which stronger downstream use has not been established. |
| `returnConditionDescriptionRef` | The condition under which the user returns to the exact source representation or source relations. |
| `changedClaimGoverningPatternRef?` | The direct method pattern for a changed claim when the current use no longer remains a representation-scheme-transition claim. |

At least one of `representationLossDescriptionRef` and `recoverabilityDescriptionRef` is present. When a reader-facing next action is useful, state it after the block in plain language rather than inventing another field.

The fuller field set belongs to `RepresentationSchemeTransitionDescription@Context`; it is not a second relation, profile, or hidden admissibility object. The description refers to the existing relation and states its preserved claims, source-relation basis, deltas, loss or recoverability, use boundary, and return condition.

#### A.6.3.RT:4.3.a - Working admissibility defaults

By default in this pattern:
- primary admissible faces for non-latent cases are `PlainView` and `TechCard`;
- bounded report-only use is admissible when source pins, provenance, loss notes, and entityOfConcernRef-preserving continuity remain visible, and when the receiving rendering is not relying on one separate narrower-use card to remain honest;
- `InteropCard` use is admissible only when the governing publication-face source explicitly permits source-pinned, structure-preserving export without added semantics;
- `AssuranceLane` or gate-bearing use is admitted only under a governing publication-face policy and source-pinned same-EntityOfConcern continuity;
- latent-representation variants and distributed-representation variants remain bounded until explicit recoverability evidence and decoding-relation discipline are published.

#### A.6.3.RT:4.4 - Direct and correspondence-mediated profiles

**Direct RepresentationSchemeTransition**
- source representation and receiving representation are representation-scheme variants over one entityOfConcernRef-preserving source line;
- `CorrespondenceModelRef` is absent;
- admission uses explicit factor delta, reasoning-medium delta, and recoverability discipline.

**CorrespondenceRepresentationSchemeTransition**
- the receiving representation is derived through a declared correspondence between epistemes or views of the same EntityOfConcern;
- `CorrespondenceModelRef` is present;
- the result remains under `A.6.3` only if same-entity conservativity is still reviewable by continuity witness and the correspondence does not silently import extra claims.

Correspondence-mediated representation work does **not** by itself grant bridge licence, substitution licence, or comparative-review licence. If the declared use needs those admissibility records, declare them separately rather than hiding them inside representation language.

#### A.6.3.RT:4.4.a - Recurring same-entity representation moves

Recurring same-entity moves under this pattern include:
- **Tabulation** — prose or dispersed claims are rendered into a table that exposes comparison or coverage more clearly.
- **Diagramming** — a table or prose relation set is rendered into a diagram that foregrounds structure while keeping the source-relation chain visible.
- **Structured notation shift** — prose, table, or diagram content is rendered into a notation better suited for disciplined replay or technical inspection.
- **Correspondence-admissible representation shift** — the receiving representation depends on declared same-EntityOfConcern correspondence witness without thereby becoming a bridge case.

These are recurring move shapes under one specialization relation. They are not separate governing patterns and they do not override `E.17` face discipline.

#### A.6.3.RT:4.4.b - How the user states representation-factor and reasoning-medium change
A user can state, in one short paragraph, what changed in representational shape, what changed in reasoning medium, and whether the primary change is also a `semioticModeShift` rather than only a scheme change. Typical statements are: "the table foregrounds comparability across rows", "the diagram foregrounds dependency shape", or "the notation foregrounds explicit argument positions."

When the case is more demanding, that paragraph also names whether salience, topology, actionability, admissible-use interpretation, calibration, or interactivity materially changed. If those shifts cannot be stated without slipping into new ontology, hidden bridge work, or a changed EntityOfConcern, the case is not yet ready to stay here. Use the representation-delta review crib sheet and the current semiotic-mode note when the deltas need a more normalized statement.

#### A.6.3.RT:4.5 - Shared representation rule bundle

##### A.6.3.RT:4.5.a. Preservation rule
`RepresentationSchemeTransition` preserves the same EntityOfConcern line, bounded context, and declared claim-bearing source while changing the representation scheme and, often, the reasoning medium. The transition record is complete when it states what remains preserved about the ontic scaffold, claim scope, publication scope, pins, provenance, and grounding, and whether the case remains direct or correspondence-mediated.

##### A.6.3.RT:4.5.a.1. Local conservativity witness
For this pattern, a new EntityOfConcern-side claim is introduced when the receiving rendering:
- upgrades a source-visible relation into relation theory or dependency semantics not present in the source;
- turns geometry, notation, embedding proximity, or decoder output into ontology-by-default;
- adds bridge, substitution, comparative-review, or mechanism claims not already licensed by the source line or declared correspondence;
- collapses source alternatives, uncertainty, or bounded scope into one wider commitment;
- or treats decode-mediated recoverability as if it were direct givenness.

Conservativity is approximated here by checking, together, `entityOfConcernPolicy = preserve`, source-relation class, factor delta, reasoning-medium delta, loss profile, ontic scaffold preservation, and whether each receiving-side connective can be pointed back to pinned source `U.Episteme` claim graph or declared same-EntityOfConcern correspondence witness.

##### A.6.3.RT:4.5.b. Loss and reliability rule
A reviewed case under this pattern makes explicit which distinctions, inspection possibilities, or local cues are lost, foregrounded, or rearranged by the shift in representation regime. Reliability transport may remain source-bounded or be explicitly downgraded; a clearer, more structured, or more formal receiving form does not widen the reliability claim.

##### A.6.3.RT:4.5.c. Governing-pattern boundary rule
A case reviewed under this pattern stays same-entity and representation-shift facing when the positive field spine remains visible: preserved `entityOfConcernRef`, source-relation chain, representation-scheme or reasoning-medium delta, loss or recoverability note, admissible use, and non-admissible downstream use.

When the current claim is no longer that representation shift, state the claim being made and apply the governing pattern for that claim. Typical crossed claims are retargeting, bridge stance, explanation governance, carrier work, gate authority, evidence force, assurance force, work enactment, abductive selection, temporal currentness, dynamics currentness, and transformation-flow currentness. Until that governing source relation is supplied, the shifted representation remains limited to source-finding, inspection, comparison, technical review, reversible planning preparation, report-only use, or exploratory use.

##### A.6.3.RT:4.5.c.1. Decode-mediated entry condition
A decode-mediated case, latent-representation case, or distributed-representation case may stay here only when the receiving rendering carries this entry set:
- pinned source claim or source publication for the same EntityOfConcern;
- source-relation chain back to the pinned source `U.Episteme` claim graph;
- decoding relation or access relation;
- recoverability evidence for the intended use;
- admissible-use value;
- remaining user action.

Readable decoded output is useful only inside that entry set. The source expression, latent region, distributed activation pattern, embedding, probe result, or decoded rendering may point to the representation-transition case as a whole or to one relation position inside it; recover the same `entityOfConcernRef`, source claim or publication, decoding or access relation, recoverability evidence, admissible use, and remaining user action separately. If the entry set is missing, keep the use report-only, exploratory, or blocked and return to the exact source representation or source relations when their content is needed; if another claim is being made, state the governing pattern for that claim.


##### A.6.3.RT:4.5.d. Composition and reopen rule
Repeated same-regime normalization may be idempotent, but heterogeneous regime shifts are generally order-sensitive. Multi-publication chains are checked pairwise, and the final use carries accumulated loss rather than restarting as if each pair erased earlier losses.

Each step in a chain keeps recoverable:
- preserved `entityOfConcernRef` plus source and receiving representations;
- claim or commitment under test;
- representation-scheme delta;
- preserved and withdrawn commitments;
- loss and recoverability;
- remaining admissible user action.

The case reopens whenever recoverability assumptions, pins, provenance, correspondence witness, publication-face admissibility, primary semiotic mode, or accumulated loss changes. A representation shift also reopens if what looked like one same-entity line turns out to concern a new EntityOfConcern, a counter-witness disposition, or a decoding relation whose current evidence basis no longer satisfies its declared use.

#### A.6.3.RT:4.6 - Boundary trigger table

Use this table after the positive field spine. It is not a second catalogue of everything RT cannot do; it names the local trigger that changes the next FPF move.

| Boundary trigger | Governing result |
| --- | --- |
| `entityOfConcernRef`, EntityOfConcern kind, ontology frame, admissible predicate set, or invariant-bearing receiving rendering changes | Apply `A.6.4` or the ontology-facing governing pattern. |
| The receiving rendering is only a textual rewrite | Apply `ConservativeRetextualization`. |
| The primary job is explanation-use adequacy for an existing source on an MVPK face | Apply `ExplanationFaithfulnessProfile` unless EntityOfConcern or ontology-frame change makes `A.6.4` primary. |
| Selected source structures are ordered into a sequential narrative for a declared reader or listener use | Apply `A.6.3.NAR`; keep RT only for the representation-scheme shift that remains after the narrative ordering, source loss, and source return are declared. |
| The work is rendering, export, upload, serialization, OCR-style extraction, parsing-style extraction, or other carrier work | Keep carrier work outside RT; start with the pattern governing carrier or extraction use, such as `A.7` when source extraction is the current question. |
| Geometry, notation, embedding space, feature clustering, decoded output, `PathSliceId`, `CrossingRef`, or `DecisionLogRef` is being used as ontology, continuity proof, gate, work, evidence, assurance, or transformation-flow currentness claim | Keep RT only for the representation shift and apply the governing pattern for the stronger claim. |
| Problem formulation, temporal claim, dynamics claim, control claim, or transformation-flow claim becomes primary | Apply `B.5.2`, `C.27`, `A.3.3`, `E.18`, or the governing pattern for that claim. |
| The receiving representation remains useful but the ordinary field spine cannot honestly hold | State controlled coarsening, explicit return to the exact source representation or source relations, bridge-bounded use, report-only use, exploratory use, or the named governing pattern for the changed claim. |

If recoverability depends on decoding, probing, or intervention, the evidence class bounds the admissible use. Low-evidence decode-mediated results remain bounded exploratory or report-only renderings; non-latent cases remain the default entry case until decode-mediated recoverability is made explicit.

