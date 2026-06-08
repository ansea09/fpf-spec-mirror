---
chunk_kind: "parent"
pattern_id: "A.6.3.RT"
pattern_title: "RepresentationTransduction — entityOfConcernRef-preserving representation-scheme transition"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/A.6.3.RT.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "A.6.3.RT — RepresentationTransduction — entityOfConcernRef-preserving representation-scheme transition"
line_start: 10985
line_end: 11486
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

## A.6.3.RT - RepresentationTransduction — entityOfConcernRef-preserving representation-scheme transition
> **Status:** Stable

**Placement.** Specialization under `A.6.3 U.EpistemicViewing` for entityOfConcernRef-preserving representation-scheme transition.
**Builds on.** `A.6.3 U.EpistemicViewing`; `A.6.2 U.EffectFreeEpistemicMorphing`; `A.7`; `E.10.D2`; `C.2.7`; `E.17.0`; `E.17`; `F.9`; `F.18`.
**Coordinates with.** `ConservativeRetextualization`; `A.6.3.CSC Controlled Semantic Coarsening`; `ExplanationFaithfulnessProfile`; `E.17.ID.CR ComparativeReading`; `A.6.4 U.EpistemicRetargeting`; `F.9`; `F.9.1`; `E.18`; `A.15`; `A.10`; `B.3`; `B.5.2`; `A.20`; `A.21`; `C.27`; `A.3.3`; explicit decoding-access review.
**Name boundary.** In this pattern, `RepresentationTransduction` names an `A.6.3 U.EpistemicViewing` specialization for an entityOfConcernRef-preserving transition across declared representation schemes or reasoning media. It is not an `E.18` Transduction Graph Architecture node, not a TGA graph edge, not an `A.15` method description, work-plan, or work-occurrence claim, and not a changed-function or control-architecture claim.

**One-line summary.** `RepresentationTransduction` is an entityOfConcernRef-preserving shift in representation scheme that stays inside `A.6.3 U.EpistemicViewing`: it may move between prose, table, diagram, structured notation, or another declared representation regime, but it does **not** silently change `entityOfConcernRef`, promote geometry or notation into ontology-by-default, or hide decode-mediated recoverability behind rendering fluency.
**EntityOfConcern preservation discipline.** In this specialization, entityOfConcernRef-preserving representation change means the C.2.1 `entityOfConcernRef` stays stable while representation scheme, reasoning medium, recoverability, and loss are made explicit.

**Primary EntityOfConcern in plain terms.** One published rendering of the same EntityOfConcern in a different representation scheme or reasoning medium; not the whole source corpus, not a new ontology, and not carrier-operation work.
**Admissible move in plain terms.** Change representation scheme while keeping entityOfConcernRef-preserving continuity witness reviewable, factor deltas visible, and handoff explicit when the case has become explanation, retargeting, bridge work, or a narrower-use card.

**Use this when.** Use this pattern when the same EntityOfConcern needs to move across representation schemes or reasoning media such as prose, table, diagram, or structured notation, and the real job is still the representation shift rather than explanation, retargeting, or downstream action.

**Start here when.** Your first honest publication unit already changes representation scheme or reasoning medium, and the main review question is whether the receiving representation keeps a visible source-relation path and entityOfConcernRef-preserving continuity rather than becoming a new ontology, a hidden bridge, or a coarsened proxy.

**What goes wrong if missed.** A table, diagram, or notation shift gets treated as harmless formatting even after it has started hiding recoverability loss, silent EntityOfConcern or ontology shift, decode work, or a separate narrower-use card.

**What this buys.** One honest entityOfConcernRef-preserving representation shift with visible source-relation path, visible factor and reasoning-medium change, and an explicit handoff when the case stops being ordinary representation transduction.

**Working action spine.** The same `entityOfConcernRef` appears in a new representation scheme -> separate source representation or publication, receiving representation or rendering, preserved claim, representation scheme, reasoning medium, and admissible use -> use the rendering for inspection, source-finding, comparison, technical review, or reversible planning preparation -> output the ordinary use path or the fuller continuity-witness decision block when ambiguity, dispute, citation, reliance, bridge, work, gate, assurance, decode-mediated access, abductive reopen, temporal/dynamics, release, or TGA-path use is live -> hand off if work, evidence, gate, explanation, retargeting, bridge, carrier, coarsened-rendering, abductive, temporal, dynamics, or TGA claim appears.

**Ordinary use.** If the publication-facing item is admissible only for inspection, source-finding, comparison, or planning preparation, keep the explicit interpretation of the source representation or publication, the receiving representation or rendering, the one preserved `entityOfConcernRef`, preserved claim, representation-scheme change, and admissible and non-admissible use.

**Ordinary use path.**
1. Which source representation or publication and receiving representation or rendering are being compared, and is preservation of the same `entityOfConcernRef` explicit?
2. Which source claim or commitment remains preserved for the intended use?
3. What representation scheme, reasoning medium, or expression form changed?
4. What reader action remains admissible, and what downstream use is not admissible from this representation shift alone?

**Action/work boundary.** A representation shift may be admissible for method inspection or work-planning preparation, but the source for intended or actual work remains `A.15` plus the source `U.Episteme`, source `U.EpistemePublication`, or project-side FPF kind and reference named by value that governs that work claim.

**Reliance-facing use.** Open the fuller continuity-witness decision block only when the shifted representation will be externally relied on, disputed, cited as an admissibility reason, used across context, treated as gate/release/work preparation justification, carried through a decode-mediated or latent access path, used in abductive reopen, or used for temporal/dynamics or TGA-path currentness.

**Representation-validity grounding.** Recoverability is recoverability for one declared admissible use, not a general property of the receiving representation. A diagram, table, notation, decoded output, or model-state rendering may be recoverable enough for inspection or technical review when receiving-side relations trace back to source-relation records and loss notes, while still being insufficient for work-planning reliance, gate reliance, release reliance, evidence reliance, assurance reliance, or engineering justification. For any such reliance use, this pattern supplies only same-EntityOfConcern correspondence witness; the operative admissibility must come from the governing FPF pattern and project-side FPF kind and reference named by value named by `A.15`, `A.10`, `A.20`, `A.21`, `B.3`, `E.17.EFP`, `E.17.ID.CR`, `F.9`, or `F.9.1` as applicable. When the shifted representation will carry claim-bearing use, state the admissibility path that makes that use admissible by value: source-relation path, recoverability scope, decode path where needed, evidence class, any probe evidence, intervention evidence, or causal-abstraction claim, and the `E.17:5.1b` source-relation class when source pointer, source availability, source retrieval, source use, source faithfulness, claim admissibility, contradiction, omission, claim widening, or reopen trigger could diverge. Use `E.17:5.1c` for the shared use-boundary meanings of `orientation use`, `reliance use`, `operative claim`, `non-admissible downstream use`, and `reopen trigger`; use `E.17:5.1d` when the primary question under repair may belong to ordinary textual restatement, coarsening, explanation, comparison, bridge work, substitution, work, reliance, gate, evidence, assurance, retargeting, or carrier and front-end work.

A table, diagram, notation, decoded output, or model-state rendering may expose or cite its source relation. It does not become that source relation, architecture, ontology, evidence, gate, or work source by visual clarity, geometry, notation, proximity, or reuse. If the needed admissibility path is missing, a repair request, source-gap note, or evidence-work plan is prospective only; it does not retroactively make the earlier representation shift admissible.

**Stop condition.** Stop once the representation shift changes no next inspection, comparison, source-finding, or planning-preparation move and blocks no concrete overclaim about the represented entity, source relation, work, gate, or evidence.

**Admissible-use examples.**

| Admissible project-side use | Source-finding or reversible probe | Non-admissible downstream use |
| --- | --- | --- |
| A table or diagram makes the same EntityOfConcern easier to inspect while the source-relation path and representation-scheme change stay visible. | A diagram helps reversible planning or source inspection while the team checks recoverability, source-relation records, or decode path before gate, work, evidence, or justification use. | A diagram, geometry, table, or notation is treated as architecture, ontology, evidence, gate passage, work authority, or engineering justification by visual form alone. |

**Not this pattern when.** Not this pattern when only wording changes (`ConservativeRetextualization`), explanation becomes primary (`ExplanationFaithfulnessProfile`), the EntityOfConcern changes (`A.6.4`), or the receiving representation stays honest only by carrying its own narrower admissible use, non-admissible downstream use, declared source-loss mode, and source-bearing reopen card. In that last case, use `A.6.3.CSC Controlled Semantic Coarsening` instead of resolving it as ordinary `RepresentationTransduction`.

### A.6.3.RT:1 - Problem frame

The same EntityOfConcern often needs to be carried across more than one representation regime:
- prose into a table that makes comparison or coverage clearer;
- a table into a diagram that foregrounds dependency or topology;
- a diagram into a structured notation suitable for replay or technical review;
- a source representation into another regime that changes reasoning possibilities without changing the underlying EntityOfConcern.

In practice these shifts are often treated as harmless reformatting. But some representation changes alter reasoning possibilities, reduce recoverability, or quietly change what appears to be present in the source. FPF already has `A.6.3` for entityOfConcernRef-preserving conservative viewing. This pattern names the recurring entityOfConcernRef-preserving case where the published result changes representation scheme while the case still remains inside `A.6.3`.

### A.6.3.RT:2 - Problem

Without a dedicated named pattern for representation-scheme transitions:
1. teams treat text-to-table, table-to-diagram, and notation shifts as if they were all the same kind of harmless rewrite;
2. changes in reasoning medium and recoverability remain implicit;
3. latent/distributed cases tempt readers to treat geometry or feature clusters as ontology-by-default;
4. reviewers cannot tell when a case is still same-entity viewing and when it has become retargeting, explanation, carrier work, or decode-mediated reconstruction;
5. representation factors governed near `C.2.7` are discussed rhetorically rather than as explicit deltas.

### A.6.3.RT:3 - Forces

- **Same entity, different reasoning medium.** Teams need different representational forms without silently changing the EntityOfConcern.
- **Legibility vs recoverability.** A clearer representation is useful only if readers can still recover how it relates to source claims, source-relation records, and pins.
- **Representation change vs EntityOfConcern shift.** A new notation or geometry can make structure more visible, but it must not silently become a new EntityOfConcern or a new ontology.
- **Recoverability before decode ambition.** Start from cases where recoverability can be reviewed directly before leaning on decode-mediated reconstruction.
- **Governing-pattern restraint.** This pattern must stay under `A.6.3`, not swallow explanation governance, retargeting, bridge work, or carrier work.

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

### A.6.3.RT:5 - Archetypal grounding

#### A.6.3.RT:5.1 - Same-entity text-to-table shift
**Source slice.** `Service S showed three recurring latency spikes in the evening batch window. Trace T-44 and dashboard pin D-17 identify the same service and time window.`

**Published table slice.** `| Service | Window | Spike count | Source pins |
| Service S | Evening batch | 3 | T-44, D-17 |`

This is an admissible direct `RepresentationTransduction` if no new claims are introduced, the same EntityOfConcern stays explicit, and the representation-factor delta is declared. In ordinary engineering use, this usually needs a visible source-relation path, explicit loss notes if anything was omitted, and a clear statement that the table is still about the same service occurrence rather than a new EntityOfConcern.

#### A.6.3.RT:5.2 - Same-entity table-to-diagram shift
**Source table slice.** `| Node | Depends on |
| CoolingLoop | Sensor A |
| CoolingLoop | Valve B |`

**Published diagram slice.** `CoolingLoop -> Sensor A; CoolingLoop -> Valve B`

The move stays in this pattern only if the EntityOfConcern is preserved, the diagram does not silently add new semantic commitments, and reasoning-medium change is declared. If the diagram starts asserting dependency theory not actually stated by the source table, the case must reopen and may leave this pattern.

#### A.6.3.RT:5.2.a - Correspondence-mediated text-to-table shift
**Source prose slice.** `In the safety view, CL-2 maintains the required temperature condition during standard operating demand.`

**Published table slice.** `| View | Entity | Condition | Correspondence model |
| Safety | CL-2 | required temperature condition during standard operating demand | CM-12 |`

The move stays in this pattern only if the correspondence remains explicit, the EntityOfConcern stays preserved, and the resulting table does not quietly import bridge semantics or a changed EntityOfConcern. Because the required correspondence witness is doing real work here, a source-bearing continuity note is often warranted instead of relying only on the rendered table.

#### A.6.3.RT:5.2.b - Same-entity diagram-to-structured-notation shift
**Source diagram slice.** `CoolingLoop -> Sensor A; CoolingLoop -> Valve B`

**Published notation slice.** `dependsOn(CoolingLoop, SensorA)`
`dependsOn(CoolingLoop, ValveB)`

This remains under `RepresentationTransduction` when the notation states the same relation line already visible in the diagram, the EntityOfConcern remains preserved, and no additional dependency theory is silently imported by the notational rendering.

#### A.6.3.RT:5.2.c - Functional-description diagram/table/screen shift

**Source slice.** `The mixing cell transfers liquid from Tank A through heat exchanger H-2 to reactor R-4; the source description is about the same declared functional slice and keeps instrumentation/control claims outside this relation.`

**Published table/screen slice.** `| Function relation | Source | Target | Limit |`
`| transfer and heat before reaction | Tank A | R-4 via H-2 | no control-loop claim |`

This remains `RepresentationTransduction` only when the same EntityOfConcern is preserved and the table or screen changes representation scheme or reasoning medium without adding performed-work order, module structure, evidence, gate passage, or control architecture. If the diagram, table, or screen turns the receiving representation into a functional, control, or flow architecture claim rather than re-rendering the already declared functional slice, leave this pattern for `A.6.4`, `OntologicalReframing`, or `E.18` as applicable. If the diagram order is explanatory, causal, dependency-like, or didactic, do not read it as physical time order or performed-work sequence unless that temporal claim is present in the source episteme and separately admissible. If a parser or OCR step only extracts pixels, text, or carrier layout from a scanned diagram or screen, start with `A.7`; enter this pattern only when the extracted structure is being treated as an entityOfConcernRef-preserving representation of source `U.Episteme` claims with source-relation path and loss notes visible.

If the published screen becomes honest only by omitting exceptions, confidence bands, or source distinctions and by carrying a narrower admissible use with source-bearing return, move to `A.6.3.CSC Controlled Semantic Coarsening` rather than keeping the case here as ordinary representation transduction.

#### A.6.3.RT:5.3 - Boundary to textual rewrite
A source prose note is shortened, reordered, or translated but remains essentially textual. That case stays with `ConservativeRetextualization`, not this pattern.

#### A.6.3.RT:5.4 - Boundary to explanation-facing renderings
A representation shift is performed mainly to teach or narrate rather than to publish another same-entity representation regime. That case leaves this pattern and is reviewed under explanation governance.

#### A.6.3.RT:5.4.a - Boundary to bridge-bearing comparison
**Source slice.** `Local reliability note: Pump P-2 remained within operating range during test window W-3.`

**Published comparative slice.** `Pump P-2 in W-3 behaves like Unit U-7 in Plant B and can therefore be treated as operationally equivalent for this comparison.`

This does **not** stay in `RepresentationTransduction`. The rendering has moved from an entityOfConcernRef-preserving representation shift to comparative or bridge-bearing interpretation across contexts. Once the publication starts asserting cross-context equivalence, substitution, or comparative licence, the case must leave this pattern and move to explicit bridge-governed review.

#### A.6.3.RT:5.4.b - Boundary to carrier/export work
**Source rendering slice.** `| Service | Window | Spike count | Source pins |`

**Published export slice.** `latency-report.csv` and dashboard PNG generated from the same table.

This also stays outside `RepresentationTransduction`. The representation scheme was already chosen; what follows is carrier formatting, export, packaging, or rendering work on that representation. The didactic point is that not every change in visible form is a new entityOfConcernRef-preserving representation transition.

#### A.6.3.RT:5.4.c - Boundary to coarsened dashboard view
**Source slice.** `The incident worksheet tracks three causal branches, two confidence bands, and one still-open ambiguity note for Service S.`

**Published dashboard tile.** `Service S: current dashboard view foregrounds cache-failover evidence; alternative branches and confidence bands remain in the incident worksheet.`

This does **not** remain ordinary `RepresentationTransduction` if the tile is treated as more than a narrow report view. The tile foregrounds one causal branch and suppresses uncertainty and alternative branches, so it stays honest only with source-bearing return to the source-bearing worksheet and a non-admissible downstream-use line. It is not a causal proof, service status verdict, or action cue. Once that narrower-use card becomes primary, the case leaves ordinary entityOfConcernRef-preserving representation transduction and must use `A.6.3.CSC Controlled Semantic Coarsening` rather than being treated as a normal scheme shift.

#### A.6.3.RT:5.5 - Boundary to decode-mediated latent cases
A reviewer or decode path tries to restate a latent region or distributed feature cluster as explicit entity/relation content. This stays outside the admissible entityOfConcernRef-preserving path under `A.6.3.RT` unless the pinned source claim or publication, decode path or access route, recoverability evidence, admissible-use value, and remaining reader action are already present. Readable decode output alone is not enough.

#### A.6.3.RT:5.5.a - Guarded decode-mediated readout
**Pinned source cluster.** `Probe run P-8 is tied to model-state log M-12 and evaluation bundle EV-4 for the same diagnostic case.`

**Published exploratory slice.** `A decode-mediated readout suggests a cluster that may correspond to the same failure episode already pinned in P-8 / M-12 / EV-4. This rendering stays exploratory and report-only until the required recoverability evidence is published.`

This example remains guarded-open rather than green. The didactic point is that a decode-mediated rendering may still be useful, but it does not become a normal same-entity publication merely because the result looks readable.

### A.6.3.RT:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto/Epist**, **Prag**, **Did**.
This pattern intentionally biases toward same-entity representation shifts and away from hidden retargeting, explanation inflation, or ontology-by-default through notation or geometry. The main mitigation is explicit recoverability discipline, preserve-vs-retarget escape rules, and directly reviewable entry cases before decode-mediated ones.

### A.6.3.RT:7 - Conformance Checklist

A conformance check is retained only if it changes the next admissible use of the shifted representation, blocks a concrete overclaim, or preserves a source/reopen path needed for the declared admissible use.

#### A.6.3.RT:7.1 - RT-Core ordinary checks

1. **CC-RT-1 — Same EntityOfConcern remains explicit.**
   The case preserves `entityOfConcernRef` without special pleading.
2. **CC-RT-2 — Representation shift is the right family.**
   The result is genuinely a representation-scheme or reasoning-medium shift rather than mere textual rewrite, explanation work, carrier work, or changed EntityOfConcern.
3. **CC-RT-3 — Admissible and non-admissible use are visible.**
   The ordinary use path states the source representation or publication, the receiving representation or rendering, preservation of the same `entityOfConcernRef`, the source claim or commitment preserved for the intended use, the representation-scheme or reasoning-medium change, the admissible reader action, and the downstream use not made admissible by this representation shift.
4. **CC-RT-8 — Preserve-vs-retarget handoff is explicit.**
   If the case fails the ordinary checks, the handoff destination is explicit (`A.6.3.CR`, `E.17.EFP`, `A.6.3.CSC`, `A.6.4`, carrier work under `A.7`, or another governing pattern).
5. **CC-RT-14 — Functional-description publication overread is blocked.**
   Functional diagrams, tables, screens, exports, and parser/OCR results are kept separate from performed `U.Work`, gate passage, evidence, engineering justification, supervisory/control architecture, and carrier work. OCR/parsing starts with `A.7`; same-entity representation work stays here only when source-relation path, same EntityOfConcern, representation-scheme change, and loss notes remain visible.

#### A.6.3.RT:7.2 - RT-Conditional checks

1. **CC-RT-4 — Factor, reasoning-medium, and mode deltas are explicit when claim-bearing.**
   `representationFactorDelta`, `inferenceRegimeDelta`, and any claim-bearing `semioticModeShift` are explicit when they materially shape review or misuse risk.
2. **CC-RT-5 — Extended delta factors are explicit when claim-bearing.**
   `salienceShift`, `topologyShift`, `admissibleUseShift`, `calibrationShift`, and `interactivityShift` are named whenever they materially shape review or misuse risk.
3. **CC-RT-6 — Decode-mediated cases carry additional recoverability evidence.**
   If the case is decode-mediated or latent/distributed, the pinned source claim or publication, decode path or access route, recoverability evidence, admissible-use value, and remaining reader action are explicit.
4. **CC-RT-7 — Loss, provenance, pinning, and reliability are explicit when needed.**
   Losses, provenance, pinning, and reliability transport are stated or inherited by visible pinned reference when external reliance, dispute, gate, assurance, evidence, or cross-context use is live.
5. **CC-RT-9 — Direct vs correspondence split is explicit when correspondence is doing work.**
   The case states whether it is direct or correspondence-mediated; if correspondence-mediated, `CorrespondenceModelRef` is explicit.
6. **CC-RT-10 — Non-default face/rendering admissibility is explicit.**
   Any `InteropCard`, `AssuranceLane`, gate-bearing, or decode-bounded use states governing publication-face admissibility and keeps same-EntityOfConcern continuity visible.
7. **CC-RT-11 — Decode-mediated same-entity source-relation path is explicit.**
   A decode-mediated case states the source-relation path from the receiving rendering back to already pinned and provenance-bearing source `U.Episteme` claim graph for the same EntityOfConcern.
8. **CC-RT-12 — No hidden bridge or face-family inflation.**
   The case makes clear that representation work does not by itself grant bridge, substitution, or comparative-review licence and does not create a new face family.
9. **CC-RT-13 — Reopen triggers are explicit when recoverability, admissibility, or primary mode changes.**
   If recoverability assumptions, pins, provenance, correspondence witness, publication-face admissibility, or the primary semiotic mode change, the case records the reopen trigger explicitly.

### A.6.3.RT:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it is wrong | How to avoid it |
|---|---|---|
| Treating every format shift as harmless formatting | representation changes can alter reasoning possibilities and recoverability | publish factor delta and reasoning-medium delta explicitly |
| Collapsing representation-scheme shift, semiotic-mode shift, and viewpoint shift into one vague change | reviewers cannot tell what actually changed or what required admissibility record is primary | name scheme, mode, and viewpoint separately and use the canonical boundary exemplars when only one of them changed |
| Letting notation become ontology-by-default | diagram or geometry starts pretending to define the world rather than represent it | keep ontic scaffold preservation and recoverability explicit |
| Hiding retargeting under representation language | a changed EntityOfConcern is mislabeled as same-entity representation work | apply `A.6.4` whenever `EntityOfConcernRef` changes |
| Starting with latent/distributed cases before recoverability is explicit | decode demand overwhelms same-entity review | keep decode-mediated cases out until decoding access and evidence class are explicit |

### A.6.3.RT:9 - Consequences

- Same-entity representation shifts get an admissible place without inventing a new heavy governing pattern.
- Representation-factor and reasoning-medium changes become explicit rather than rhetorical.
- Recoverability and decode dependence become reviewable instead of hidden behind cleaner renderings.
- The pattern remains safely bounded by `A.6.3`, `A.6.4`, explanation governance, and carrier work.

### A.6.3.RT:10 - Rationale

This pattern is worth splitting out because representation changes are already happening in practice and they are not well served by treating every such case as either mere rewriting or full retargeting. Keeping the family under `A.6.3` preserves governing-pattern boundary while making representation-factor and recoverability evidence needs explicit.

### A.6.3.RT:11 - SoTA Alignment: Adopted/Adapted Invariants And Rejected Shortcuts

**SoTA alignment rule.** Read each row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and Relations of this pattern.

**Claim 1.** Best-known current architecture-description and model-based practice treats views, representation schemes, and reasoning media as claim-bearing rather than as decorative formatting.
**Practice source, local alignment, and adoption decision.** ISO/IEC/IEEE 42010:2022 and current SysML v2 view practice (source maturity = mature standard plus current technical specification/practice) treat viewpoint, view, model kind, and rendering discipline as explicit review subjects rather than mere layout choices. This pattern **adopts** explicit representation-scheme review, **adapts** it to entityOfConcernRef-preserving viewing under `A.6.3`, and **rejects** the shortcut where a clearer table, diagram, or notation is treated as if it had automatically earned ontology or authority not carried by the source relation.

**Claim 2.** Best-known contemporary notation-and-reasoning practice treats tables, diagrams, and structured notations as reasoning media with different inspection possibilities, not as neutral visual restyling.
**Practice source, local alignment, and adoption decision.** Post-2015 model-based and notation-sensitive review practice (source maturity = widely used technical practice) treats representational form as something that changes what readers can inspect, compare, or replay. This pattern **adopts** reasoning-medium review, **adapts** it through explicit factor and medium deltas, and **rejects** hidden dependency-theory uplift or silent added semantic commitment by prose-to-diagram or diagram-to-notation moves.

**Claim 3.** Best-known representation-aware practice treats latent geometry, decoded output, and representation structure as evidence-bounded interpretation that needs a declared admissibility path before it can carry an engineering claim.
**Practice source, local alignment, and adoption decision.** Representation engineering and causal-abstraction practice (source maturity = research/technical practice used for evaluation use) treats internal representations as inspectable, monitorable, manipulable, or experimentally aligned only through explicit methods that connect representation to behavior, causal role, or source relation. BLT/LCM-style model examples (source maturity = examples/analogy only here, not claim-bearing authority) show that representation regime matters, but they do not by themselves decide when a diagram, decoded output, or latent cluster becomes a valid engineering claim. This pattern **adopts** representation-validity grounding through source-relation path, recoverability scope, decode path, `recoverabilityEvidenceClass`, and declared probe/intervention evidence where claimed; it **rejects** the shortcut where latent geometry, diagram topology, or decoded prose becomes ontology by readability or model reputation.

**Local stance.** The claim-bearing SoTA claim for this pattern is narrow: representation regime and reasoning medium are admissible review subjects, but geometry, notation, topology, probe output, decoded prose, or latent/distributed structure do not become ontology, evidence, gate admissibility, work authority, or engineering justification unless a declared admissibility path makes that use admissible by value.

### A.6.3.RT:12 - Relations

- **Builds on:** `A.6.3`, `A.6.2`, `A.7`, `E.10.D2`, `C.2.7`, `E.17.0`, `E.17`, `F.9`, `F.18`
- **Coordinates with:** `ConservativeRetextualization`, `A.6.3.CSC Controlled Semantic Coarsening`, `ExplanationFaithfulnessProfile`, `E.17.ID.CR ComparativeReading`, `A.6.4`, `F.9`, `F.9.1`, `E.18`, `A.15`, `A.10`, `B.3`, `B.5.2`, `A.20`, `A.21`, `C.27`, `A.3.3`, explicit decoding-access review
- **Impact radius:** primary touch `A.6.3`; selected edit companion `A.6.4`; secondary review relation `C.2.7`, `E.17.0`, `E.17`, `F.9`, decode-mediated recoverability review, TGA path interpretation under `E.18`, and project-side exits under the neighboring pattern governing that claim when live
- **Boundary notes:** textual same-regime rewrites stay with `ConservativeRetextualization`; explanation-facing renderings stay with `ExplanationFaithfulnessProfile`; bounded comparative review cases apply `E.17.ID.CR ComparativeReading`; EntityOfConcern changes apply `A.6.4`; coarsened source renderings apply `A.6.3.CSC`; bridge, work, evidence, assurance, gate, abductive, temporal, dynamics, and TGA-path consequences remain bounded by explicit evidence and downstream handoff.

### A.6.3.RT:12a - Boundary with quantum-like state-representation shortcuts

Use RT first when the same EntityOfConcern is represented through a different representation scheme: text-to-table, model to diagram, diagram to structured record, state vector to typed description, or one notation to another. Ordinary representation-scheme change remains RT even when the new scheme is more compact.

Action path:

1. Confirm that the EntityOfConcern stays the same. If it changes, leave RT.
2. Name the source representation scheme and receiving representation scheme.
3. State what changed in representation factor, reasoning medium, mode, salience, topology, actionability, calibration, or interactivity.
4. State recoverability: what can be recovered from the receiving representation, by which decode path, and with which evidence.
5. If the receiving representation claims to preserve action, intervention, manipulation, explanation, or cross-abstraction structure, state the causal-abstraction or approximate-causal-abstraction mapping before treating the shortcut as QL coarsening.
6. Ask whether the shortcut depends on a QL cue: contextual probability, incompatible probes, instrument-like update, Hilbert-like or orthomodular representation, open-information-system update rule, probe frame, export-admissibility evidence requirement, or declared lossy export of a state that matters to the decision.
7. If no, keep the case under RT, CSC, ordinary abstraction, compression, diagramming, causal abstraction, approximation, or a declared representation-learning access pattern, whichever governs the actual admissibility claim.
8. If yes, coordinate with the `C.26` state-representation coarsening admissibility section and state admissible use, non-admissible use, and return condition.

For ordinary use, start with the standard shortcut mini-form:

| Mini-entry | Question |
| --- | --- |
| Source-loss question | Which representation scheme, state interpretation, fuller model, or evidence set loses distinctions in the shortcut? |
| Shortcut | Which cheaper, typed, quantized, symbolic, lower-detail, or otherwise transformed representation is used? |
| Loss | Which precision, expressivity, compatibility, recoverability, or evidence relation is not carried? |
| Admissible use | Which decision, explanation, triage, comparison, or action-selection move remains admissible for the shortcut? |
| Reopen | Which dispute, decision change, demand for use with a higher evidence requirement, evidence gap, or recoverability failure sends the reader back to the source representation or fuller model? |

Use a fuller C.26 coarsening record only when the shortcut becomes reusable, formal, empirical, high-stakes, or tied to comparative performance or tractability claims. In that fuller record, add the mechanism, baseline path, non-admissible use, and QL cue needed for the additional-admissibility claim.

Do not describe ordinary compression, low-bit implementation, diagramming, or representation learning as quantum-like unless the formal cue is claim-bearing.
### A.6.3.RT:12b - C.29 mathematical-lens use relation

> When an entityOfConcernRef-preserving representation-scheme transition imports a contested or claim-bearing mathematical lens, `A.6.3.RT` still governs the source and receiving representation schemes, entityOfConcernRef-preserving relation, preserved and lost scheme features, and transduction boundary. The applicable `C.29` output for the stated use (`MathLensUse.LensCandidateNote`, `MathLensUse.OneLine`, `MathLensUse.MiniCard`, or `MathLensUse.FullCard` when required) may be cited only for adequacy of the mathematical lens used in that transition. It does not replace the representation-transduction record or broaden the transition into bridge, evidence, or causal-claim-kind.

### A.6.3.RT:End

