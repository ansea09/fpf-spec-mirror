---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "RepresentationTransduction — entityOfConcernRef-preserving representation-scheme transition"
section_id: "A.6.3.RT:4"
section_title: "Solution — entityOfConcernRef-preserving representation-scheme transition under A.6.3"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__005_solution-entityofconcernref-preserving-representation-scheme-transition-under-a-6-3.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "A.6.3.RT — RepresentationTransduction — entityOfConcernRef-preserving representation-scheme transition"
  - "A.6.3.RT:4 — Solution — entityOfConcernRef-preserving representation-scheme transition under A.6.3"
line_start: 11232
line_end: 11453
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
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
keywords:
---

### A.6.3.RT:4 - Solution — entityOfConcernRef-preserving representation-scheme transition under `A.6.3`

#### A.6.3.RT:4.1 - Informal definition

> `RepresentationTransduction` is a named pattern specialized under `A.6.3 U.EpistemicViewing` for entityOfConcernRef-preserving transitions across declared representation schemes.
>
> It preserves `entityOfConcernRef`, keeps the transform effect-free, and makes explicit what changes in representation factors, reasoning medium, recoverability, and loss profile.
>
> It may move between prose, table, diagram, structured notation, or another declared representation regime. It may not silently change the EntityOfConcern, silently import bridge semantics, or treat decode-mediated structure as if it were directly given.

#### A.6.3.RT:4.1.a - Pattern, case, and published rendering distinction

`RepresentationTransduction` is a **pattern description** and a named specialization under `A.6.3`. Concrete entityOfConcernRef-preserving representation changes are passive episteme cases or published renderings reviewed under this pattern; the pattern itself does not act, decide, or publish.

This distinction matters because the pattern governs **how** a representation change is recognised, justified, and checked. It does **not** turn every table, diagram, or structured notation into a giant standalone review artifact, and it does not reduce review to a mechanical reformatting step.

#### A.6.3.RT:4.1.b - Local working vocabulary

Use this vocabulary only after the ordinary use path leaves a live ambiguity or a claim-bearing relation-change question. Ordinary text-to-table, table-to-diagram, or diagram-to-notation cases do not need every term below; use only the term that changes the next representation decision or blocks a concrete overclaim.
- **Representation scheme** = the published form in which the same entity is rendered (for example prose, table, diagram, or structured notation).
- **Reasoning medium** = the form-specific inspection possibilities readers actually use when inspecting the published rendering.
- **Semiotic mode** = which meaning-bearing relation is doing the main work in the rendering, such as structural likeness, trace/index, conventional code, model-mediated correspondence, or decode-mediated recoverability.
- **Factor delta** = the explicit change in representation factors that matters for review.
- **Source-relation path** = the visible source relation back to pinned or otherwise reviewable source `U.Episteme` claim graph that keeps same-EntityOfConcern continuity honest.
- **Decode-mediated case** = a case where explicit access to the receiving representation depends on a declared decoding path rather than direct interpretation from an already published source episteme or source publication.
- **actionabilityShift** = a changed reader action-possibility interpretation or apparent readiness created by the rendering. It is not execution authority, gate status, action invitation, work authority, or proof that work may proceed.
- **recoverabilityEvidenceClass** = a local review field naming the recoverability evidence needed for decode-mediated or latent cases. It is not an `EvidenceKind`, and it is not required for ordinary non-latent representation shifts unless recoverability is part of the question under repair.
- **representationValidityAdmissibilityValue** = a local admissibility value used only when the representation shift is disputed, assurance-facing, gate-adjacent, externally relied on, decode-mediated, or likely to invite gate, evidence, work, or authority use beyond declared admissible use. It says which use the shifted representation makes admissible now; it is not a score, ordered rank, improvement scale, ontology class, evidence class, or `authoritySourceRef` destination.
- **sourceRelationClass** = the shared `E.17:5.1b` vocabulary used beside representation-validity value when the source relation itself is disputed or claim-bearing: pointer-only, available, retrieved, used, faithful, claim-admissible, claim-non-admissible, claim-contradicted, claim-plausible-only, source-omitted, source-loss-declared, claim-widened, added-linkage, independent-verification-present, admissible-for-this-use, downstream-use-forbidden, or reopen-trigger-present.

| representationValidityAdmissibilityValue | Admissible use | Required admissibility path | Shortcut rejected |
| --- | --- | --- | --- |
| `readability-only` | Inspection, discussion, source-finding, or planning preparation. | Source-relation path and non-admissible downstream-use line. | Clearer rendering means a wider claim. |
| `source-recoverable` | Receiving-side relations can be traced back to source-relation records. | Source-relation records, loss/provenance note, and recoverability statement. | Receiving form replaces source relation. |
| `structure-preserving` | Technical review of preserved relation structure. | Declared relation structure, preservation witness, and no-new-claim check. | Diagram/topology defines ontology by form. |
| `decode-bounded` | Bounded decode-mediated report or review. | Decode path, `recoverabilityEvidenceClass`, and recoverability scope. | Readable decode output is direct givenness. |
| `probe/intervention-bounded` | Bounded representation-to-property or representation-to-behavior claim. | Probe evidence, intervention evidence, or causal-abstraction relation that names the exact admissible use. | Probe confidence or intervention success becomes general ontology. |
| `bridge-bounded-source-equivalence` | Equivalence, substitution, or bridge use only where another governing pattern supplies it. | Existing bridge, equivalence, or substitution record outside RT, with the governing pattern named. | RT itself grants source equivalence or substitution. |

**Recoverability-for-use rule.** If the declared admissible use is inspection, source-finding, comparison, or technical review, `RepresentationTransduction` can close with entityOfConcernRef-preserving preservation, source-relation path, representation-scheme delta, and loss/recoverability notes. If the declared admissible use is work-planning preparation, this pattern is admissible only for reversible preparation until `A.15` supplies the role, method, plan, and work source relation. If the declared admissible use is evidence or currentness, gate or release, assurance, commitment, bridge or substitution, or engineering justification, the case must name the downstream governing source relation; otherwise the receiving representation remains orientation or review use only.

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
- carrier work such as rendering, export, upload, serialization, or OCR/parsing-like extraction;
- latent/distributed use without pinned source claim or publication, decode path or access route, recoverability evidence, admissible-use value, and remaining reader action.

#### A.6.3.RT:4.2.a - Reader guidance

Use this pattern when the EntityOfConcern stays fixed but the published result changes representation scheme or reasoning medium.
- If only wording changes, stay in `ConservativeRetextualization`.
- If the receiving item mainly teaches, narrates, or explains, move to `ExplanationFaithfulnessProfile`.
- If same-EntityOfConcern continuity fails, move to `A.6.4`.
- Stay here when changed representation scheme or reasoning medium remains the primary review question, even if some loss is present.
- If the receiving representation stays honest only by carrying its own narrower-use card, declared source-loss mode, non-admissible downstream-use line, and source-bearing reopen, move to `A.6.3.CSC Controlled Semantic Coarsening`; do not keep the case here as ordinary representation transduction.
#### A.6.3.RT:4.2.b - What a reviewer checks first

A reviewer usually starts with five questions:
1. Is the EntityOfConcern still the same, or has the EntityOfConcern shifted?
2. What changed in representation scheme and reasoning medium?
3. Can the receiving item still state a source-relation path back to a pinned source episteme or source publication with enough specificity for the declared admissible use?
4. Has the case quietly become explanation, bridge-bearing comparison, retargeting, or carrier work?
5. If decoding is involved, is the evidence class adequate for the declared admissible use rather than only for readable review?

If the representation shift is no longer the main review problem, and the receiving item instead stays honest only by carrying a narrower-use card with non-admissible downstream use and reopen duty, the case has crossed out of ordinary representation transduction even if the new form still looks like a neat table, diagram, or notation. Use `A.6.3.CSC Controlled Semantic Coarsening` for that source-to-rendering relation.

Here, **reopen** means return to the source-bearing content, while **handoff** means the governing pattern has changed. A coarsened representation may need both.

Only after these questions are answered clearly does a fuller claim-bearing decision block normally become necessary.

#### A.6.3.RT:4.3 - Working-model first; explicit decision block only when the case is claim-bearing

Most entityOfConcernRef-preserving representation shifts stay human-usable and reviewable without turning every table, diagram, or structured rendering into a giant metadata block. This pattern therefore follows **E.14's working-model-first discipline**: ordinary non-latent cases need enough explicitness to show what stayed the same, what changed in representation and reasoning medium, what was lost or foregrounded, and where the case would have to move to another governing pattern.

**Ordinary case (default).** For everyday entityOfConcernRef-preserving representation shifts, it is usually enough that the rendering or its surrounding publication keeps explicit:
- the source representation or source episteme publication, the receiving representation or rendering, and the statement that one `entityOfConcernRef` is preserved;
- the source `U.Episteme` claim or commitment preserved for the intended use;
- the representation scheme, reasoning medium, or expression-form delta;
- the remaining admissible reader action and the downstream use not made admissible by this representation shift.

That ordinary path is the default. It is admissible for inspection, source-finding, comparison, technical review, or reversible planning preparation. It does not by itself license work authority, evidence force, gate passage, assurance force, bridge substitution, abductive selection, temporal/dynamics currentness, or TGA-path currentness.

**Fuller continuity-witness decision block (only for claim-bearing cases).** A fuller block is warranted when the case is disputed, externally relied on, cross-context, correspondence-heavy, decode-mediated, assurance-facing, gate-adjacent, work-pressure, abductive-reopen, temporal/dynamics, or TGA-path-bearing. The block may inherit pattern ids and already-pinned metadata instead of restating them inline. When published, it makes these decision-block fields recoverable:

| Field | Required interpretation in this pattern |
| --- | --- |
| `sourceEpistemeOrPublication` | The source `U.Episteme`, `U.EpistemePublication`, episteme-lane `U.View`, or exact source publication being transformed or cited. |
| `receivingEpistemeOrPublication` | The receiving episteme, publication, view, diagram, table, functional description, explanation, decoded rendering, or TGA-facing publication item. |
| `preservedEntityOfConcernRef` | The one C.2.1 `entityOfConcernRef` preserved across the representation shift. |
| `receivingRepresentationOrRendering` | The receiving representation, diagram, table, functional description, decoded rendering, or publication item over that same `entityOfConcernRef`; if `entityOfConcernRef` changes, exit to `A.6.4`. |
| `groundingAndContext` | Grounding holon, bounded context, reference plane, and reference scheme as far as the intended use needs. |
| `claimOrCommitmentUnderTest` | The claim, invariant, commitment, relation, or project-side use whose continuity is being judged. |
| `viewpointAndView` | The viewpoint and view used to read the source and receiving material when they affect the claim. |
| `representationSchemeDelta` | The representation scheme, reasoning medium, representation factor, or inference-regime change that matters for review. |
| `preservedCommitments` | What the receiving item still carries from the source. |
| `withdrawnOrNewCommitments` | What the receiving item drops, narrows, adds, widens, or changes. |
| `admissibilityClass` | The source-relation or representation-validity admissibility class for the intended use named by value. |
| `continuityWitness` | The reason the entityOfConcernRef-preserving continuity is still reviewable. |
| `counterWitness` | Any fact that weakens entityOfConcernRef-preserving continuity, such as changed entity, changed predicate, changed frame, missing source-relation path, or non-admissible decode path. |
| `lossAndRecoverability` | Preserved distinctions, lost distinctions, recoverability scope, recoverability evidence, and source-bearing reopen condition. |
| `admissibleUse` | The admissible use named by value now. |
| `nonAdmissibleUse` | The downstream work, evidence, gate, assurance, bridge, decision, abductive, TGA-path, temporal, or dynamics use that is not carried by the current item. |
| `neighboringPatternHandoff` | The FPF pattern that carries the neighboring claim being made, when one is live. |
| `remainingAdmissibleReaderAction` | One short plain line saying what the reader may now do or which neighboring pattern now carries the claim being made. |

The decision block is not a new FPF kind, record, profile, publication form, or hidden admissibility object. It is a recoverable field set for the representation-transition case.

#### A.6.3.RT:4.3.a - Working admissibility defaults

By default in this pattern:
- primary admissible faces for non-latent cases are `PlainView` and `TechCard`;
- bounded report-only use is admissible when source pins, provenance, loss notes, and entityOfConcernRef-preserving continuity remains visible, and when the receiving item is not relying on one separate narrower-use card to remain honest;
- `InteropCard` use is admissible only when the governing publication-face source explicitly permits source-pinned, structure-preserving export without added semantics;
- `AssuranceLane` or gate-bearing use is not default and requires governing publication-face policy plus source-pinned same-EntityOfConcern continuity;
- latent/distributed variants remain bounded until explicit recoverability evidence and decode-path discipline are published.

#### A.6.3.RT:4.4 - Direct and correspondence-mediated profiles

**Direct RepresentationTransduction**
- source representation and receiving representation are representation-scheme variants over one entityOfConcernRef-preserving source line;
- no `CorrespondenceModelRef` is required;
- the main required admissibility path is explicit factor delta, reasoning-medium delta, and recoverability discipline.

**CorrespondenceRepresentationTransduction**
- the receiving representation is derived through a declared correspondence between epistemes or views of the same EntityOfConcern;
- `CorrespondenceModelRef` is required;
- the result remains under `A.6.3` only if same-entity conservativity is still reviewable by continuity witness and the correspondence does not silently import extra claims.

Correspondence-mediated representation work does **not** by itself grant bridge licence, substitution licence, or comparative-review licence. If the case needs those required admissibility records, they must be declared separately rather than hidden inside representation language.

#### A.6.3.RT:4.4.a - Recurring same-entity representation moves

Recurring same-entity moves under this pattern include:
- **Tabulation** — prose or dispersed claims are rendered into a table that exposes comparison or coverage more clearly.
- **Diagramming** — a table or prose relation set is rendered into a diagram that foregrounds structure while keeping the source-relation path visible.
- **Structured notation shift** — prose, table, or diagram content is rendered into a notation better suited for disciplined replay or technical inspection.
- **Correspondence-admissible representation shift** — the receiving representation depends on declared same-EntityOfConcern correspondence witness without thereby becoming a bridge case.

These are recurring move shapes under one specialization relation. They are not separate governing patterns and they do not override `E.17` face discipline.

#### A.6.3.RT:4.4.b - How a reviewer reads representation-factor and reasoning-medium change
A reviewer can say, in one short paragraph, what changed in representational shape, what changed in reasoning medium, and whether the primary change is also a `semioticModeShift` rather than only a scheme change. Typical read-outs are: "the table foregrounds comparability across rows", "the diagram foregrounds dependency shape", or "the notation foregrounds explicit argument positions."

When the case is more demanding, that paragraph also names whether salience, topology, actionability, admissible-use interpretation, calibration, or interactivity materially changed. If those shifts cannot be stated without slipping into new ontology, hidden bridge work, or a changed EntityOfConcern, the case is not yet ready to stay here. Use the representation-delta review crib sheet and the current semiotic-mode note when the deltas need a more normalized statement.

#### A.6.3.RT:4.5 - Shared representation rule bundle

##### A.6.3.RT:4.5.a. Preservation rule
`RepresentationTransduction` preserves the same EntityOfConcern line, bounded context, and declared claim-bearing source while changing the representation scheme and, often, the reasoning medium. It must state what remains preserved about the ontic scaffold, claim scope, publication scope, pins, provenance, and grounding. It must also state whether the case remains direct or correspondence-mediated.

##### A.6.3.RT:4.5.a.1. Local conservativity witness
For this pattern, a new EntityOfConcern-side claim is introduced when the receiving rendering:
- upgrades a source-visible relation into relation theory or dependency semantics not present in the source;
- turns geometry, notation, embedding proximity, or decoder output into ontology-by-default;
- adds bridge, substitution, comparative-review, or mechanism claims not already licensed by the source line or declared correspondence;
- collapses source alternatives, uncertainty, or bounded scope into one wider commitment;
- or treats decode-mediated recoverability as if it were direct givenness.

Conservativity is approximated here by checking, together, `entityOfConcernPolicy = preserve`, source-relation class, factor delta, reasoning-medium delta, loss profile, ontic scaffold preservation, and whether each receiving-side connective can be pointed back to pinned source `U.Episteme` claim graph or declared same-EntityOfConcern correspondence witness.

##### A.6.3.RT:4.5.b. Loss and reliability rule
A reviewed case under this pattern makes explicit which distinctions, inspection possibilities, or local cues are lost, foregrounded, or rearranged by the shift in representation regime. Reliability transport may remain source-bounded or be explicitly downgraded, but it must never be silently widened just because the receiving form looks clearer, more structured, or more formal.

##### A.6.3.RT:4.5.c. Authority and handoff rule
A case reviewed under this pattern stays same-entity and episteme-facing. It does not govern retargeting, bridge stance, explanation governance, executable docking, gate authority, evidence force, assurance force, work enactment, abductive selection, temporal/dynamics currentness, or TGA-path currentness. If any of those claims become live, name the neighboring pattern governing that claim and keep the representation shift to source-finding, inspection, comparison, technical review, reversible planning preparation, report-only use, or exploratory use until the neighboring source relation is supplied.

##### A.6.3.RT:4.5.c.1. Same-entity entry condition for decode-mediated cases
A decode-mediated or latent/distributed case may stay here only when the receiving rendering states a source-relation path back to already pinned and provenance-bearing source `U.Episteme` claim graph for the same EntityOfConcern.

The minimum entry condition is:
- pinned source claim or source publication;
- decode path or access route;
- recoverability evidence for the intended use;
- admissible-use value;
- remaining reader action.

A readable decoded result alone does not establish direct access to the EntityOfConcern, work authority, evidence force, gate passage, assurance force, TGA-path currentness, or ontology-frame retargeting. If the entry condition is missing, the current disposition is report-only, exploratory, source-bearing reopen, blocked current transfer, or a named neighboring-pattern handoff.

##### A.6.3.RT:4.5.d. Composition and reopen rule
Repeated same-regime normalization may be idempotent, but heterogeneous regime shifts are generally order-sensitive. Multi-publication chains are checked pairwise, but the final use must preserve accumulated loss rather than restarting as if each pair erased earlier losses.

Each step in a chain keeps recoverable:
- preserved `entityOfConcernRef` plus source and receiving representations;
- claim or commitment under test;
- representation-scheme delta;
- preserved and withdrawn commitments;
- loss and recoverability;
- remaining admissible reader action.

The case reopens whenever recoverability assumptions, pins, provenance, correspondence witness, publication-face admissibility, primary semiotic mode, or accumulated loss changes. A representation shift also reopens if what looked like one same-entity line turns out to require a new EntityOfConcern, a counter-witness disposition, or a decode path with higher evidence requirements than currently declared.

#### A.6.3.RT:4.6 - Hard boundary rules

A case reviewed under this pattern keeps the following explicit:
- `entityOfConcernPolicy = preserve` is mandatory;
- any change of `EntityOfConcernRef`, EntityOfConcern kind, ontology frame, admissible predicate set, or invariant-bearing receiving item applies `A.6.4`;
- purely textual rewrite cases stay with `ConservativeRetextualization`;
- explanation-facing cases stay with `ExplanationFaithfulnessProfile` unless the EntityOfConcern, kind, ontology frame, admissible predicate set, or invariant-bearing receiving item changes;
- carrier work stays outside this pattern;
- geometry, notation, embedding space, feature clustering, or readable decoded output must not become ontology-by-default;
- a `PathSliceId`, `CrossingRef`, or `DecisionLogRef` does not prove entityOfConcernRef-preserving continuity by itself;
- `StructuralReinterpretation` receives retargeting semantics from `A.6.4` and `E.18`; it is not proof of semantic continuity;
- changed problem formulation leaves this pattern for `B.5.2` when it changes abductive prompt, candidate generation, rival-set formation, selected prime hypothesis, plausibility filtering, or abductive reopen;
- temporal, dynamics, and control claims leave this pattern for `C.27` or `A.3.3` when freshness, rhythm, effort/inertia, state-space, trajectory, reusable transition law, or control relation is live;
- the family changes representation scheme, not face governance, and it therefore stays under existing `E.17.0 / E.17` face discipline rather than creating a new publication family.

If recoverability depends on decoding, probing, or intervention, the evidence class must bound admissible use; otherwise the case stays exploratory, report-only, or outside the admissible entityOfConcernRef-preserving path under `A.6.3.RT`. Low-evidence decode-mediated results are not canonical publications with reduced admissibility; they are bounded exploratory or report-only renderings. Non-latent cases remain the default entry path until decode-mediated recoverability is made explicit.

When a counter-witness exists but the receiving item remains useful, the current disposition is controlled coarsening, source-bearing reopen, bridge-bounded use, report-only use, exploratory use, or a named neighboring-pattern handoff. Do not keep an unnamed middle state where the item remains rhetorically useful but no FPF disposition is stated.

