---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "RepresentationTransduction — same-described-entity representation-scheme transition"
section_id: "A.6.3.RT:4"
section_title: "Solution — same-described-entity representation-scheme transition under A.6.3"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__005_solution-same-described-entity-representation-scheme-transition-under-a-6-3.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "A.6.3.RT — RepresentationTransduction — same-described-entity representation-scheme transition"
  - "A.6.3.RT:4 — Solution — same-described-entity representation-scheme transition under A.6.3"
line_start: 11071
line_end: 11294
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.6.2"
  - "A.6.3"
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
  - "E.17.ID.CR"
  - "E.18"
  - "F.18"
  - "F.9"
  - "F.9.1"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
keywords:
  - "diagram"
  - "notation shift"
  - "reasoning medium"
  - "recoverability"
  - "representation transduction"
  - "same-described-entity representation change"
  - "source tether"
  - "state-representation shortcut"
  - "table"
---

### A.6.3.RT:4 - Solution — same-described-entity representation-scheme transition under `A.6.3`

#### A.6.3.RT:4.1 - Informal definition

> `RepresentationTransduction` is a named pattern specialized under `A.6.3 U.EpistemicViewing` for same-described-entity transitions across declared representation schemes.
>
> It preserves `describedEntityRef`, keeps the transform effect-free, and makes explicit what changes in representation factors, reasoning medium, recoverability, and loss profile.
>
> It may move between prose, table, diagram, structured notation, or another declared representation regime. It may not silently change the described entity, silently import bridge semantics, or treat decode-mediated structure as if it were directly given.

#### A.6.3.RT:4.1.a - Pattern, case, and published rendering distinction

`RepresentationTransduction` is an **intensional pattern** and a named specialization under `A.6.3`. Concrete same-described-entity representation changes are passive episteme cases or published renderings reviewed under this pattern; the pattern itself does not act, decide, or publish.

This distinction matters because the pattern governs **how** a representation change is recognised, justified, and checked. It does **not** turn every table, diagram, or structured notation into a giant standalone review artifact, and it does not reduce review to a mechanical reformatting step.

#### A.6.3.RT:4.1.b - Local working vocabulary

Use this vocabulary only after the ordinary use path leaves a live ambiguity or a load-bearing relation-change question. Ordinary text-to-table, table-to-diagram, or diagram-to-notation cases do not need every term below; use only the term that changes the next representation decision or blocks a concrete overclaim.
- **Representation scheme** = the published form in which the same entity is rendered (for example prose, table, diagram, or structured notation).
- **Reasoning medium** = the form-specific inspection possibilities readers actually use when inspecting the published rendering.
- **Semiotic mode** = what kind of meaning-bearing support is doing the main work in the rendering, such as structural likeness, trace/index, conventional code, model-mediated correspondence, or decode-mediated recoverability.
- **Factor delta** = the explicit change in representation factors that matters for review.
- **Source tether** = the visible link back to pinned or otherwise reviewable source `U.Episteme` claim graph that keeps same-entity support honest.
- **Decode-mediated case** = a case where explicit access to the target representation depends on a declared decoding path rather than direct reading from an already published source episteme or source publication.
- **actionabilityShift** = a changed reader action-possibility reading or apparent readiness created by the rendering. It is not execution authority, gate status, action invitation, work authority, or proof that work may proceed.
- **recoverabilityEvidenceClass** = a local review field naming the recoverability evidence support needed for decode-mediated or latent cases. It is not an `EvidenceKind`, and it is not required for ordinary non-latent representation shifts unless recoverability is part of the live question.
- **representationValiditySupportPosture** = a local support-posture value used only when the representation shift is disputed, assurance-facing, gate-adjacent, externally relied on, decode-mediated, or likely to invite gate, evidence, work, or authority use beyond declared support. It says what the shifted representation may support now; it is not a score, ordered rank, improvement scale, ontology class, evidence class, or `authoritySourceRef` target.
- **sourceSupportPosture** = the shared `E.17:5.1b` vocabulary used beside representation-validity posture when the source relation itself is disputed or load-bearing: pointer-only, available, retrieved, used, faithful, claim-supported, claim-unsupported, claim-contradicted, claim-plausible-only, source-omitted, source-loss-declared, claim-widened, added-linkage, independent-verification-present, admissible-for-this-use, downstream-use-forbidden, or reopen-trigger-present.

| representationValiditySupportPosture | What it supports | Required support | Shortcut rejected |
| --- | --- | --- | --- |
| `readability-only` | Inspection, discussion, source-finding, or planning preparation. | Source tether and non-admissible downstream-use line. | Clearer rendering means a wider claim. |
| `source-recoverable` | The reader can trace target relations back to source anchors. | Source anchors, loss/provenance note, and recoverability statement. | Target form replaces source support. |
| `structure-preserving` | Technical review of preserved relation structure. | Declared relation structure, preservation witness, and no-new-claim check. | Diagram/topology defines ontology by form. |
| `decode-supported` | Bounded decode-mediated report or review. | Decode path, `recoverabilityEvidenceClass`, and recoverability target. | Readable decode output is direct givenness. |
| `probe/intervention-supported` | Bounded representation-to-property or representation-to-behavior claim. | Probe evidence, intervention evidence, or causal-abstraction support that names the exact admissible use. | Probe confidence or intervention success becomes general ontology. |
| `bridge-supported-source-equivalence` | Equivalence, substitution, or bridge use only where another governing pattern supplies it. | Existing bridge, equivalence, or substitution support outside RT, with the governing pattern named. | RT itself grants source equivalence or substitution. |


**Recoverability-for-use rule.** If the declared admissible use is inspection, source-finding, comparison, or technical review, `RepresentationTransduction` can close with same-described-entity preservation, source tether, representation-scheme delta, and loss/recoverability notes. If the declared admissible use is work-planning preparation, this pattern supports only reversible preparation until `A.15` supplies the role, method, plan, and work source relation. If the declared admissible use is evidence or currentness, gate or release, assurance, commitment, bridge or substitution, or engineering justification, the case must name the downstream governing source relation; otherwise the target representation remains orientation or review support only.

These terms are local review aids. They inherit the `E.17:5.1e` local-field rule: they do not create `U.Kind`, `SurfaceKind`, `RelationKind`, `KindBridge`, `MechanismKind`, `EvidenceKind`, exact project-side FPF kind and reference, new face family, or new ontology governing pattern.

#### A.6.3.RT:4.2 - Scope and exclusions

**In scope**
- text-to-table shift over the same described entity;
- table-to-diagram shift over the same described entity;
- diagram-to-structured-notation shift where the represented entity and claim-bearing source episteme stay preserved;
- functional-description diagrams, tables, screens, or notations when the same described entity remains fixed and the main change is representation scheme or reasoning medium;
- other same-entity representation-scheme changes with explicit recoverability discipline.

**Out of scope**
- any change of `describedEntityRef` or hidden change of described entity (`A.6.4`);
- explanation-facing renderings whose main purpose is didactic or explanatory rendering work (`ExplanationFaithfulnessProfile`);
- purely textual rewrites that stay inside one representation regime (`ConservativeRetextualization`);
- carrier work such as rendering, export, upload, serialization, or OCR/parsing-like extraction;
- latent/distributed use without pinned source claim or publication, decode path or access route, recoverability evidence, admissible use-support value, and remaining reader action.


#### A.6.3.RT:4.2.a - Reader guidance

Use this pattern when the described entity stays fixed but the published result changes representation scheme or reasoning medium.
- If only wording changes, stay in `ConservativeRetextualization`.
- If the target mainly teaches, narrates, or explains, move to `ExplanationFaithfulnessProfile`.
- If same-entity support fails, move to `A.6.4`.
- Stay here when changed representation scheme or reasoning medium remains the primary review question, even if some loss is present.
- If the target stays honest only by carrying its own narrower-use card, declared source-loss mode, non-admissible downstream-use line, and source-bearing reopen, move to `A.6.3.CSC Controlled Semantic Coarsening`; do not keep the case here as ordinary representation transduction.
#### A.6.3.RT:4.2.b - What a reviewer checks first

A reviewer usually starts with five questions:
1. Is the described entity still the same, or has the described entity shifted?
2. What changed in representation scheme and reasoning medium?
3. Can the target still be tethered back to a pinned source episteme or source publication with enough specificity for the declared admissible use?
4. Has the case quietly become explanation, bridge-bearing comparison, retargeting, or carrier work?
5. If decoding is involved, is the evidence class adequate for the declared admissible use rather than only for readable review?

If the representation shift is no longer the main review problem, and the target instead stays honest only by carrying a narrower-use card with non-admissible downstream use and reopen duty, the case has crossed out of ordinary representation transduction even if the new form still looks like a neat table, diagram, or notation. Use `A.6.3.CSC Controlled Semantic Coarsening` for that source-to-rendering relation.

Here, **reopen** means return to the source-bearing content, while **handoff** means the governing pattern has changed. A coarsened representation may need both.

Only after these questions are answered clearly does a fuller load-bearing decision block normally become necessary.

#### A.6.3.RT:4.3 - Working-model first; explicit decision block only when the case is load-bearing

Most same-described-entity representation shifts stay human-usable and reviewable without turning every table, diagram, or structured rendering into a giant metadata block. This pattern therefore follows **E.14's working-model-first discipline**: ordinary non-latent cases need enough explicitness to show what stayed the same, what changed in representation and reasoning medium, what was lost or foregrounded, and where the case would have to move to another governing pattern.

**Ordinary case (default).** For everyday same-described-entity representation shifts, it is usually enough that the rendering or its surrounding publication keeps explicit:
- the source described entity and the receiving described entity, or the statement that the receiving item preserves the source described entity;
- the source `U.Episteme` claim or commitment preserved for the intended use;
- the representation scheme, reasoning medium, or expression-form delta;
- the remaining admissible reader action and the downstream use not made admissible by this representation shift.

That ordinary path is the default. It supports inspection, source-finding, comparison, technical review, or reversible planning preparation. It does not by itself support work authority, evidence force, gate passage, assurance force, bridge substitution, abductive selection, temporal/dynamics currentness, or TGA-path currentness.

**Fuller continuity-witness decision block (only for load-bearing cases).** A fuller block is warranted when the case is disputed, externally relied on, cross-context, correspondence-heavy, decode-mediated, assurance-facing, gate-adjacent, work-pressure, abductive-reopen, temporal/dynamics, or TGA-path-bearing. The block may inherit pattern ids and already-pinned metadata instead of restating them inline. When published, it makes these decision-block fields recoverable:

| Field | Required reading in this pattern |
| --- | --- |
| `sourceEpistemeOrPublication` | The source `U.Episteme`, `U.EpistemePublication`, episteme-lane `U.View`, or exact source publication being transformed or cited. |
| `receivingEpistemeOrPublication` | The receiving episteme, publication, view, diagram, table, functional description, explanation, decoded rendering, or TGA-facing publication item. |
| `sourceDescribedEntity` | The described entity before the representation shift. |
| `receivingDescribedEntity` | The described entity after the shift, or the statement that the source described entity is preserved. |
| `groundingAndContext` | Grounding holon, bounded context, reference plane, and reference scheme as far as the intended use needs. |
| `claimOrCommitmentUnderTest` | The claim, invariant, commitment, relation, or project-side use whose continuity is being judged. |
| `viewpointAndView` | The viewpoint and view used to read the source and receiving material when they affect the claim. |
| `representationSchemeDelta` | The representation scheme, reasoning medium, representation factor, or inference-regime change that matters for review. |
| `preservedCommitments` | What the receiving item still carries from the source. |
| `withdrawnOrNewCommitments` | What the receiving item drops, narrows, adds, widens, or changes. |
| `supportPosture` | The source-support or representation-validity support posture for the exact intended use. |
| `continuityWitness` | The reason the same-described-entity reading is still supportable. |
| `counterWitness` | Any fact that weakens same-described-entity support, such as changed entity, changed predicate, changed frame, missing source tether, or unsupported decode path. |
| `lossAndRecoverability` | Preserved distinctions, lost distinctions, recoverability target, recoverability evidence, and source-bearing reopen condition. |
| `admissibleUse` | The exact use that remains admissible now. |
| `nonAdmissibleUse` | The downstream work, evidence, gate, assurance, bridge, decision, abductive, TGA-path, temporal, or dynamics use that is not carried by the current item. |
| `neighboringPatternHandoff` | The FPF pattern that carries the live neighboring claim, when one is live. |
| `remainingAdmissibleReaderAction` | One short plain line saying what the reader may now do or which neighboring pattern now carries the live claim. |

The decision block is not a new FPF kind, record, profile, publication form, or hidden support object. It is a recoverable field set for the representation-transition case.

#### A.6.3.RT:4.3.a - Working admissibility defaults

By default in this pattern:
- primary admissible faces for non-latent cases are `PlainView` and `TechCard`;
- bounded report-only use is admissible when source pins, provenance, loss notes, and same-described-entity support remain visible, and when the target is not relying on one separate narrower-use card to remain honest;
- `InteropCard` use is admissible only when the governing publication-face source explicitly permits source-pinned, structure-preserving export without added semantics;
- `AssuranceLane` or gate-bearing use is not default and requires governing publication-face policy plus source-pinned same-entity support;
- latent/distributed variants remain bounded until explicit recoverability evidence and decode-path discipline are published.

#### A.6.3.RT:4.4 - Direct and correspondence-mediated profiles

**Direct RepresentationTransduction**
- source representation and target representation are representation-scheme variants over one same-described-entity source line;
- no `CorrespondenceModelRef` is required;
- the main required support is explicit factor delta, reasoning-medium delta, and recoverability discipline.

**CorrespondenceRepresentationTransduction**
- the target representation is derived through a declared correspondence between epistemes or views of the same described entity;
- `CorrespondenceModelRef` is required;
- the result remains under `A.6.3` only if same-entity conservativity is still supportable and the correspondence does not silently import extra claims.

Correspondence-mediated representation work does **not** by itself grant bridge licence, substitution licence, or comparative-reading licence. If the case needs those required supports, they must be declared separately rather than hidden inside representation language.

#### A.6.3.RT:4.4.a - Recurring same-entity representation moves

Recurring same-entity moves under this pattern include:
- **Tabulation** — prose or dispersed claims are rendered into a table that exposes comparison or coverage more clearly.
- **Diagramming** — a table or prose relation set is rendered into a diagram that foregrounds structure while remaining source-tethered.
- **Structured notation shift** — prose, table, or diagram content is rendered into a notation better suited for disciplined replay or technical inspection.
- **Correspondence-supported representation shift** — the target representation depends on declared same-entity correspondence support without thereby becoming a bridge case.

These are recurring move shapes under one specialization relation. They are not separate governing patterns and they do not override `E.17` face discipline.

#### A.6.3.RT:4.4.b - How a reviewer reads representation-factor and reasoning-medium change
A reviewer can say, in one short paragraph, what changed in representational shape, what changed in reasoning medium, and whether the primary change is also a `semioticModeShift` rather than only a scheme change. Typical read-outs are: "the table foregrounds comparability across rows", "the diagram foregrounds dependency shape", or "the notation foregrounds explicit argument positions."

When the case is more demanding, that paragraph also names whether salience, topology, actionability, admissible-use reading, calibration, or interactivity materially changed. If those shifts cannot be stated without slipping into new ontology, hidden bridge work, or a changed described entity, the case is not yet ready to stay here. Use the representation-delta review crib sheet and the current semiotic-mode support note when the deltas need a more normalized read-out.

#### A.6.3.RT:4.5 - Shared representation rule bundle

##### A.6.3.RT:4.5.a. Preservation rule
`RepresentationTransduction` preserves the same described-entity line, bounded context, and declared claim-bearing source while changing the representation scheme and, often, the reasoning medium. It must state what remains preserved about the ontic scaffold, claim scope, publication scope, pins, provenance, and grounding. It must also state whether the case remains direct or correspondence-mediated.

##### A.6.3.RT:4.5.a.1. Local conservativity witness
For this pattern, a new intensional claim is introduced when the target rendering:
- upgrades a source-visible relation into relation theory or dependency semantics not present in the source;
- turns geometry, notation, embedding proximity, or decoder output into ontology-by-default;
- adds bridge, substitution, comparative-reading, or mechanism claims not already licensed by the source line or declared correspondence;
- collapses source alternatives, uncertainty, or bounded scope into one wider commitment;
- or treats decode-mediated recoverability as if it were direct givenness.

Conservativity is approximated here by checking, together, `describedEntityPolicy = preserve`, source-tether posture, factor delta, reasoning-medium delta, loss profile, ontic scaffold preservation, and whether each target-side connective can be pointed back to pinned source `U.Episteme` claim graph or declared same-entity correspondence support.

##### A.6.3.RT:4.5.b. Loss and reliability rule
A reviewed case under this pattern makes explicit which distinctions, inspection possibilities, or local cues are lost, foregrounded, or rearranged by the shift in representation regime. Reliability transport may remain source-bounded or be explicitly downgraded, but it must never be silently widened just because the target form looks clearer, more structured, or more formal.

##### A.6.3.RT:4.5.c. Authority and handoff rule
A case reviewed under this pattern stays same-entity and episteme-facing. It does not govern retargeting, bridge stance, explanation governance, executable docking, gate authority, evidence force, assurance force, work enactment, abductive selection, temporal/dynamics currentness, or TGA-path currentness. If any of those claims become live, name the exact neighboring pattern and keep the representation shift to source-finding, inspection, comparison, technical review, reversible planning preparation, report-only use, or exploratory use until the neighboring source relation is supplied.

##### A.6.3.RT:4.5.c.1. Same-entity entry condition for decode-mediated cases
A decode-mediated or latent/distributed case may stay here only when the target rendering is tethered back to already pinned and provenance-bearing source `U.Episteme` claim graph for the same described entity.

The minimum entry condition is:
- pinned source claim or source publication;
- decode path or access route;
- recoverability evidence for the intended use;
- admissible use-support value;
- remaining reader action.

A readable decoded result alone does not establish direct access to the described entity, work authority, evidence force, gate passage, assurance force, TGA-path currentness, or ontology-frame retargeting. If the entry condition is missing, the current disposition is report-only, exploratory, source-bearing reopen, blocked current transfer, or a named neighboring-pattern handoff.

##### A.6.3.RT:4.5.d. Composition and reopen rule
Repeated same-regime normalization may be idempotent, but heterogeneous regime shifts are generally order-sensitive. Multi-publication chains are checked pairwise, but the final use must preserve accumulated loss rather than restarting as if each pair erased earlier losses.

Each step in a chain keeps recoverable:
- source and receiving described entity;
- claim or commitment under test;
- representation-scheme delta;
- preserved and withdrawn commitments;
- loss and recoverability;
- remaining admissible reader action.

The case reopens whenever recoverability assumptions, pins, provenance, correspondence support, target-face admissibility, primary semiotic mode, or accumulated loss changes. A representation shift also reopens if what looked like one same-entity line turns out to require a new described entity, a counter-witness disposition, or a decode path with higher evidence requirements than currently declared.

#### A.6.3.RT:4.6 - Hard boundary rules

A case reviewed under this pattern keeps the following explicit:
- `describedEntityPolicy = preserve` is mandatory;
- any change of `DescribedEntityRef`, described-entity kind, ontology frame, admissible predicate set, or invariant-bearing target applies `A.6.4`;
- purely textual rewrite cases stay with `ConservativeRetextualization`;
- explanation-facing cases stay with `ExplanationFaithfulnessProfile` unless the described entity, kind, ontology frame, admissible predicate set, or invariant-bearing target changes;
- carrier work stays outside this pattern;
- geometry, notation, embedding space, feature clustering, or readable decoded output must not become ontology-by-default;
- a `PathSliceId`, `CrossingRef`, or `DecisionLogRef` does not prove same-described-entity continuity by itself;
- `StructuralReinterpretation` receives retargeting semantics from `A.6.4` and `E.18`; it is not proof of semantic continuity;
- changed problem formulation leaves this pattern for `B.5.2` when it changes abductive prompt, candidate generation, rival-set formation, selected prime hypothesis, plausibility filtering, or abductive reopen;
- temporal, dynamics, and control claims leave this pattern for `C.27` or `A.3.3` when freshness, rhythm, effort/inertia, state-space, trajectory, reusable transition law, or control relation is live;
- the family changes representation scheme, not face governance, and it therefore stays under existing `E.17.0 / E.17` face discipline rather than creating a new publication family.

If recoverability depends on decoding, probing, or intervention, the evidence class must bound admissible use; otherwise the case stays exploratory, report-only, or outside the admissible same-described-entity path under `A.6.3.RT`. Low-evidence decode-mediated results are not canonical publications with reduced support; they are bounded exploratory or report-only renderings. Non-latent cases remain the default entry path until decode-mediated recoverability is made explicit.

When a counter-witness exists but the receiving item remains useful, the current disposition is controlled coarsening, source-bearing reopen, bridge support, report-only use, exploratory use, or a named neighboring-pattern handoff. Do not keep an unnamed middle state where the item remains rhetorically useful but no FPF disposition is stated.

