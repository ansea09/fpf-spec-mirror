---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
section_id: "A.6.3.RT:4"
section_title: "Solution — entityOfConcernRef-preserving representation-scheme transition under A.6.3"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__005_solution-entityofconcernref-preserving-representation-scheme-transition-under-a-6-3.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "A.6.3.RT — Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
  - "A.6.3.RT:4 — Solution — entityOfConcernRef-preserving representation-scheme transition under A.6.3"
line_start: 14397
line_end: 14657
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
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
  - "C.2.1"
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

#### A.6.3.RT:4.1.a - Pattern, construction, occurrence, Work, and description

`RepresentationSchemeTransition` is a pattern description specialized under `A.6.3`. One ordinary case first identifies exact source episteme `X`, exact receiving episteme `Y`, and exact viewing declaration `v : X -> Y`. The declaration is a mathematical and claim-bearing construction; it performs no Work and is not a relation occurrence merely because a table, diagram, or file was produced.

Keep four objects distinct:

1. the A.6.3 construction `v : X -> Y`;
2. an optional positive `RepresentationSchemeTransitionRelation@Context` occurrence satisfying the rule below;
3. exact dated representation-transformation Work performed by a system under A.15.1; and
4. an optional C.2.1 episteme that describes the occurrence, preservation, loss, use, and return.

#### A.6.3.RT:4.1.a.1 - Six-participant transition relation and non-hybrid entry

`RepresentationSchemeTransitionRelation@Context` is the later-specific, bounded-model-use species of `U.Relation`. The suffix `@Context` is a retrieval label for one exact A.1.1 Plain **bounded context**, technically an independently selected `BoundedModelUseStructure : U.Structure`; it admits no discarded generic context kind or reference and no description-context field.

```text
RepresentationSchemeTransitionRelation@Context <: U.Relation:
  TransitionModelUseStructureSlot = <TransitionModelUseStructureSlot, U.Structure, U.StructureRef constrained to one exact BoundedModelUseStructure>
  PreservedEntityOfConcernSlot = <PreservedEntityOfConcernSlot, U.Entity, U.EntityRef>
  SourceRepresentationEpistemeSlot = <SourceRepresentationEpistemeSlot, U.Episteme, U.EpistemeRef>
  ReceivingRepresentationEpistemeSlot = <ReceivingRepresentationEpistemeSlot, U.Episteme, U.EpistemeRef>
  SourceRepresentationSchemeDescriptionSlot = <SourceRepresentationSchemeDescriptionSlot, U.Episteme, U.EpistemeRef>
  ReceivingRepresentationSchemeDescriptionSlot = <ReceivingRepresentationSchemeDescriptionSlot, U.Episteme, U.EpistemeRef>
  direction = SourceRepresentationEpistemeSlot -> ReceivingRepresentationEpistemeSlot
```

These six SlotSpecs and the direction are the exact `RelationSignature`. The two endpoint epistemes are independently constituted under C.2.1: each has exact claim content, the same exact EntityOfConcern bound in `PreservedEntityOfConcernSlot`, and its own effective `U.ReferenceScheme`. Each scheme-description episteme is also independently constituted; its claim content describes one exact source or receiving scheme, its EntityOfConcern is that scheme, and its own effective reference scheme makes the description interpretable. Neither a scheme label nor a visible notation fills that position.

**Obtaining rule.** A positive occurrence obtains only when all of the following hold together:

1. all six participants resolve exactly and the `BoundedModelUseStructure` is already selected under A.1.1 because its model-use organization changes this transition use;
2. one system under an exact role assignment performs exact dated representation-transformation Work whose governed input, result, reference, or A.6.1 bindings use all six participant values for this transition;
3. the exact A.6.3 declaration `v : X -> Y` states the claim-content construction, the relation between the endpoint effective reference schemes, the same-EntityOfConcern condition, preserved content, explicit loss or recoverability, prohibited strengthening, and applicability for the receiving use; and
4. every correspondence on which the construction depends is an exact separately governed relation or claim, not a graph edge, similar content, scheme difference, or a generic correspondence record.

The Work, performer, role assignment, method, operation application, source-use relations, and any A.15.PROD inception claim remain under their direct owners and are not seventh relation participants or identity discriminators. Performed Work alone does not prove the A.6.3 construction or make the relation obtain. Conversely, an inspectable `v : X -> Y` without exact Work and an independently selected `BoundedModelUseStructure` remains an ordinary RT construction; do not assert `RepresentationSchemeTransitionRelation@Context`.

**Occurrence identity.** The occurrence is participant-determined by the complete six-participant tuple, including the exact source/receiving scheme-description pair. A change to any participant identifies another occurrence. A repeat Work episode, evidence change, publication occurrence, form, carrier, layout, transition-description edition, or C.29 output does not reidentify an unchanged participant tuple. Changing `X` or `Y` claim content, EntityOfConcern, or effective reference scheme first identifies another episteme and therefore another tuple.

#### A.6.3.RT:4.1.a.2 - Transition-description and source-relation epistemes

When the occurrence must be described for reuse or review, identify one ordinary C.2.1 transition-description episteme by:

- exact claim content that designates the six-participant occurrence and states the relied-on Work and viewing declaration, source-relation or correspondence dependencies, preserved and lost content, scheme and reasoning-medium delta, admissible use, non-admissible use, and return condition;
- that exact relation occurrence as its EntityOfConcern; and
- the effective `U.ReferenceScheme` under which those claims designate the occurrence and its participants.

This is an ordinary C.2.1 episteme, not a context-selection record, another relation, a work record, or a filled-card ontology. A changed description claim graph identifies another description episteme without changing the occurrence.

If the declared use needs a reference-bearing episteme for one exact source relation, identify it independently by its own C.2.1 triple: claim content designating the exact relation occurrence and stating its exact relation kind, signature, direct governor, and use in `v`; that source relation as EntityOfConcern; and its effective reference scheme. The episteme is not the source relation and citation does not make the relation obtain.

The endpoints of the transition are exact epistemes `X` and `Y`. A selected publication occurrence may make either edition available, a publication form may express it, a `U.PresentationCarrier` may bear that form, and a C.29 representation may correspond to it for an explicit modeling or reasoning use. None of those neighbors substitutes for an endpoint or enters the six-participant identity.

At least one explicit loss or recoverability claim is present. The description also states the receiving use and the condition for return to exact `X` or to an exact governed source relation. Changed EntityOfConcern exits to A.6.4; a receiving episteme that is useful only under a narrower-use card exits to A.6.3.CSC; narrative ordering exits to A.6.3.NAR. Viewpoint, `U.View` membership, grounding, publication, evidence, assurance, bridge, gate, and receiving Work remain independently governed.

#### A.6.3.RT:4.1.b - Local working vocabulary

Use this vocabulary only after the ordinary use field set leaves ambiguity or a claim-bearing relation-change question. Ordinary text-to-table, table-to-diagram, or diagram-to-notation cases do not need every term below; use only the term that changes the next representation decision or blocks a concrete overclaim.
- **Representation scheme** = the declared regime under which exact episteme claim content is represented and interpreted for the current use; a publication form or carrier may express that content but is not the scheme, episteme, or transition.
- **Reasoning medium** = the form-specific inspection possibilities users actually use when inspecting the published rendering.
- **Semiotic mode** = which meaning-bearing relation is doing the main work in the rendering, such as structural likeness, trace relation, index relation, conventional code, model-mediated correspondence, or decode-mediated recoverability.
- **Factor delta** = the explicit change in representation factors that matters for review.
- **Source-relation chain** = exact governed relations and C.2.1 source epistemes on which `v : X -> Y` depends; pointers, graph edges, publication availability, and provenance prose do not make those relations obtain.
- **Decode-mediated case** = a case where interpreting exact receiving episteme `Y` depends on a declared decoding or access relation. A published source form, latent state, decoded output, or carrier may provide access but cannot substitute for exact source episteme `X`, exact `Y`, or the relation.
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
- latent- or distributed-representation use without exact source episteme `X`, exact receiving episteme `Y`, construction `v`, decoding/access relation, recoverability evidence, admissible use, and remaining user action; a source publication occurrence is only an access neighbor;

#### A.6.3.RT:4.2.a - User guidance

Use this pattern when exact `X` and exact `Y` keep the same EntityOfConcern while their effective representation schemes or reasoning media differ. A published form may expose `Y`; publication is not the construction.
- If only wording changes, stay in `ConservativeRetextualization`.
- If the receiving rendering mainly teaches, narrates, or explains, apply ExplanationFaithfulnessProfile.
- If same-EntityOfConcern continuity fails, apply A.6.4.
- Stay here when changed representation scheme or reasoning medium remains the primary review question, even if some loss is present.
- If the receiving representation stays honest only by carrying its own narrower-use card, declared source-loss mode, non-admissible downstream-use line, and a condition for return to the exact source representation or source relations, apply A.6.3.CSC Controlled Semantic Coarsening; do not keep the case here as ordinary representation-scheme transition.

#### A.6.3.RT:4.2.b - What the user checks first

A user usually starts with five questions:
1. Is the EntityOfConcern still the same, or has the EntityOfConcern shifted?
2. What changed in representation scheme and reasoning medium?
3. Can exact receiving episteme `Y` still cite the governed source relations needed by `v` and return to exact source episteme `X`; if access is through publication, are the occurrence, form, and carrier separately identified?
4. Has the case quietly become explanation, bridge-bearing comparison, retargeting, or carrier work?
5. If decoding is involved, is the evidence class adequate for the declared admissible use rather than only for readable review?

If the representation shift is no longer the main review problem, and the receiving rendering instead stays honest only by carrying a narrower-use card with non-admissible downstream use and reopen duty, the case has crossed out of ordinary representation-scheme transition even if the new form still looks like a neat table, diagram, or notation. Use `A.6.3.CSC Controlled Semantic Coarsening` for that source-to-rendering relation.

Here, **return to source** means returning to exact source episteme `X` or to the exact governed source relations on which `v` depends. A changed explanation, retargeting, bridge, work, evidence, gate, assurance, temporal, dynamics, carrier, or transformation-flow claim opens its named direct governor; controlled coarsening may require both source return and another governor.

Only after these questions are answered clearly does a fuller claim-bearing continuity-review field set normally become necessary.

#### A.6.3.RT:4.3 - Ordinary construction statement; occurrence description only after occurrence obtains

Most representation-scheme changes do not need a giant record. They do always need exact epistemic endpoints. For an ordinary non-latent case, state:

- exact source episteme `X` and receiving episteme `Y`, with each C.2.1 identity triple recoverable;
- exact A.6.3 construction `v : X -> Y`, including how source claims construct receiving claims and how the two effective reference schemes relate;
- same exact EntityOfConcern, preserved content, admitted omission or loss, and prohibited strengthening;
- the representation-scheme or reasoning-medium delta;
- admissible use, non-admissible downstream use, and return to exact `X` or its governed source relations.

That ordinary statement is admissible for inspection, source-finding, comparison, technical review, or reversible planning preparation. When dispute, reliance, correspondence, decode-mediated access, assurance, a gate-adjacent use, or justification requires more detail but the six-participant `...@Context` occurrence does not obtain, expand this same `v` statement with the exact source-relation or correspondence dependencies, scheme and reasoning-medium delta, loss or recoverability detail, admissible and non-admissible use, and return. Stronger reliance does not by itself require separately constituted scheme-description epistemes, an exact selected bounded model-use structure, the representation-transformation Work used by the §4.1.a.1 obtaining test, a transition-occurrence reference, or an occurrence-description episteme. Recover any independently current Work, publication, viewpoint, grounding, evidence, assurance, or receiving-use fact under its direct owner without converting the ordinary construction into the stronger occurrence.

**Occurrence-description content.** Only after an exact `RepresentationSchemeTransitionRelation@Context` occurrence obtains under §4.1.a.1 may a durable C.2.1 transition-description episteme describe it. That episteme has the exact six-participant occurrence as its EntityOfConcern, claim content that designates the occurrence and states the relied-on construction, Work, preservation, loss, use, and return, and its own effective `U.ReferenceScheme`. Dispute, reliance, correspondence, decode, assurance, gate adjacency, or justification may make this description useful, but none makes the occurrence obtain. Its claim content may make the following values recoverable; they are content about the already obtaining occurrence, not additional episteme identity fields or relation participants:

| Content needed for this occurrence-description use | Interpretation |
| --- | --- |
| `transitionRelationRef` | Required exact six-participant occurrence; its signature resolves the selected `BoundedModelUseStructure`, preserved EntityOfConcern, `X`, `Y`, and the exact source- and receiving-scheme-description epistemes. |
| `viewingConstructionRefOrStatement` | Exact `v : X -> Y` with claim construction, endpoint effective-scheme relation, applicability, preservation, loss, and prohibited strengthening. |
| `representationTransformationWorkRef` | Exact A.15.1 Work already used in the occurrence obtaining test; its performer, role assignment, method, bindings, and any inception claim remain separate. |
| `sourceRelationReferenceEpistemeRefs[]` | C.2.1 epistemes about exact governed source relations actually used; each relation still needs its own obtaining basis. |
| `preservedClaimRefs[]` | Exact source claims carried into `Y` for the declared use. |
| `preservedCommitmentRefs[]?` | Exact commitments preserved when a commitment is current; otherwise absent. |
| `representationSchemeDeltaDescriptionRef` | What differs between the exact source and receiving scheme-description epistemes already participating in the occurrence. |
| `reasoningMediumDeltaDescriptionRef?` | Changed inspection, comparison, inference, or replay affordance when material. |
| `representationLossDescriptionRef?` | Lost, narrowed, foregrounded, or rearranged distinctions. |
| `recoverabilityDescriptionRef?` | How omitted content is recovered from exact `X` or exact source relations for the declared use. |
| `admissibleUseDescriptionRef` | What the receiving episteme supports now. |
| `nonAdmissibleDownstreamUseDescriptionRef` | Which stronger use has not been established. |
| `returnConditionDescriptionRef` | When the user returns to exact `X`, its source relations, or another direct governor. |

At least one of loss and recoverability is explicit; both are explicit when distinctions are lost and a recovery route is claimed. A publication may expose the occurrence description, but publication does not constitute `X`, `Y`, `v`, the transition occurrence, the Work, or the description episteme.

#### A.6.3.RT:4.3.a - Working admissibility defaults

By default in this pattern:
- primary admissible faces for non-latent cases are `PlainView` and `TechCard`;
- bounded report-only use is admissible when source pins, provenance, loss notes, and entityOfConcernRef-preserving continuity remain visible, and when the receiving rendering is not relying on one separate narrower-use card to remain honest;
- `InteropCard` use is admissible only when the governing publication-face source explicitly permits source-pinned, structure-preserving export without added semantics;
- `AssuranceLane` or gate-bearing use is admitted only under a governing publication-face policy and source-pinned same-EntityOfConcern continuity;
- latent-representation variants and distributed-representation variants remain bounded until explicit recoverability evidence and decoding-relation discipline are published.

#### A.6.3.RT:4.4 - Direct and correspondence-mediated constructions

**Direct representation-scheme construction.** Exact receiving episteme `Y` is constructed from exact source episteme `X` and fixed declared configuration. The construction names the exact claim-content rule, the source and receiving effective reference schemes, preserved content, loss, and applicability. No generic correspondence object is required.

**Correspondence-mediated representation-scheme construction.** `Y` depends on additional exact source epistemes or exact governed relations among their claim-bearing contents. Recover each needed direct relation and, when the construction cites a claim about it, the exact C.2.1 assertion episteme. The viewing declaration names those exact dependencies. A correspondence table, model, graph edge, scheme difference, or similar content is neither the relation nor proof that it obtains.

Both profiles retain the same exact EntityOfConcern for `X` and `Y`. Correspondence does not repair retargeting and does not grant bridge, substitution, comparative-review, evidence, or publication licence. A C.29 mathematical representation is added only when a current mathematical modeling or reasoning use needs it; its output stays local and does not become the transition occurrence.

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
`RepresentationSchemeTransition` preserves the same exact EntityOfConcern across independently constituted `X` and `Y` while changing the declared representation scheme and, often, reasoning medium. An exact `BoundedModelUseStructure` participates only in the stronger `...@Context` occurrence; it is not an episteme identity discriminator. The transition account is complete only when it identifies `X`, `Y`, their effective schemes, exact construction, preserved and lost content, admissible use, and return; publication scope, pins, provenance, grounding, and selected model-use structure enter only through their independently governed relations when current.

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
A case stays here when the **required field set** remains visible: exact `X`, exact `Y`, `v : X -> Y`, preserved EntityOfConcern, governed source-relation chain, scheme/medium delta, loss or recoverability, admissible use, non-admissible use, and return. This is Plain completeness guidance, not a new structure or identity record.

When the current claim is no longer that representation shift, state the claim being made and apply the governing pattern for that claim. Typical crossed claims are retargeting, bridge stance, explanation governance, carrier work, gate authority, evidence force, assurance force, work enactment, abductive selection, temporal currentness, dynamics currentness, and transformation-flow currentness. Until that governing source relation is supplied, the shifted representation remains limited to source-finding, inspection, comparison, technical review, reversible planning preparation, report-only use, or exploratory use.

##### A.6.3.RT:4.5.c.1. Decode-mediated entry condition
A decode-mediated case, latent-representation case, or distributed-representation case may stay here only when the receiving rendering carries this entry set:
- exact source episteme `X` for the same EntityOfConcern, with any publication occurrence, form, or carrier identified separately when used for access;
- source-relation chain back to the pinned source `U.Episteme` claim graph;
- decoding relation or access relation;
- recoverability evidence for the intended use;
- admissible-use value;
- remaining user action.

A source expression, latent region, distributed activation pattern, embedding, probe result, decoded rendering, publication form, or carrier may help locate the case but cannot fill `X` or `Y`. Recover both exact epistemes, the same EntityOfConcern, the construction, decoding or access relation, recoverability evidence, admissible use, and remaining user action separately. If this entry set is missing, keep the use report-only, exploratory, or blocked and return to exact `X` or its governed source relations; if another claim is being made, apply its direct governor.


##### A.6.3.RT:4.5.d. Composition and reopen rule
Repeated same-regime normalization may be idempotent, but heterogeneous regime shifts are generally order-sensitive. Multi-publication chains are checked pairwise, and the final use carries accumulated loss rather than restarting as if each pair erased earlier losses.

Each step in a chain keeps recoverable:
- exact source and receiving epistemes with their C.2.1 identity triples and preserved EntityOfConcern;
- claim or commitment under test;
- representation-scheme delta;
- preserved and withdrawn commitments;
- loss and recoverability;
- remaining admissible user action.

The case reopens whenever recoverability assumptions, pins, provenance, correspondence witness, publication-face admissibility, primary semiotic mode, or accumulated loss changes. A representation shift also reopens if what looked like one same-entity line turns out to concern a new EntityOfConcern, a counter-witness disposition, or a decoding relation whose current evidence basis no longer satisfies its declared use.

#### A.6.3.RT:4.6 - Boundary trigger table

Use this table after the required field set. It is not a second catalogue of everything RT cannot do; it names the local trigger that changes the next FPF move.

| Boundary trigger | Governing result |
| --- | --- |
| `entityOfConcernRef`, EntityOfConcern kind, ontology frame, admissible predicate set, or invariant-bearing receiving rendering changes | Apply `A.6.4` or the ontology-facing governing pattern. |
| The receiving rendering is only a textual rewrite | Apply `ConservativeRetextualization`. |
| The primary job is explanation-use adequacy for an existing source on an MVPK face | Apply `ExplanationFaithfulnessProfile` unless EntityOfConcern or ontology-frame change makes `A.6.4` primary. |
| Selected source structures are ordered into a sequential narrative for a declared reader or listener use | Apply `A.6.3.NAR`; keep RT only for the representation-scheme shift that remains after the narrative ordering, source loss, and source return are declared. |
| The work is rendering, export, upload, serialization, OCR-style extraction, parsing-style extraction, or other carrier work | Keep carrier work outside RT; start with the pattern governing carrier or extraction use, such as `A.7` when source extraction is the current question. |
| Geometry, notation, embedding space, feature clustering, decoded output, `PathSliceId`, `CrossingRef`, or `DecisionLogRef` is being used as ontology, continuity proof, gate, work, evidence, assurance, or transformation-flow currentness claim | Keep RT only for the representation shift and apply the governing pattern for the stronger claim. |
| Problem formulation, temporal claim, dynamics claim, control claim, or transformation-flow claim becomes primary | Apply `B.5.2`, `C.27`, `A.3.3`, `E.18`, or the governing pattern for that claim. |
| Exact receiving episteme `Y` remains useful but the construction, loss, or return account cannot honestly hold | Lower or block the use; apply controlled coarsening when a narrower-use `Y` exists, otherwise return to exact `X` or its governed source relations. A readable form or carrier alone is not `Y`. |

If recoverability depends on decoding, probing, or intervention, the evidence class bounds the admissible use. Low-evidence decode-mediated results remain bounded exploratory or report-only renderings; non-latent cases remain the default entry case until decode-mediated recoverability is made explicit.

