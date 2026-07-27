---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__002_use-this-when.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:0 — Use this when"
line_start: 71979
line_end: 72896
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.2"
  - "A.15.PROD"
  - "A.19.SPR"
  - "A.2"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.3.2"
  - "A.6.0"
  - "A.6.5"
  - "A.6.6"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.17"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.5"
  - "F.18"
  - "F.19"
  - "F.5"
keywords:
---

### E.10:0 - Use this when

**What goes wrong if missed.** Precision repair turns into taste or synonym replacement. A broad head such as `support`, `surface`, `carrier`, `route`, `mapping`, `kind`, `basis`, `force`, `load`, `bearing`, `object`, or `record` is replaced by another broad head, while the relation, source-use relation, admissible use, or direct governing FPF pattern application remains unrecovered.

**What this buys.** `E.10` gives one cheap trigger scan before heavier repair. Ordinary wording stays ordinary, local lexical mistakes close locally, and FPF-governed wording uses the smallest pattern that can recover the governed object, relation, claim, admissible use, and remaining reader use. The result is precise enough to compose with FPF without replacing one umbrella word with another or turning every phrase into a new pattern, card, or review artifact.

Use `E.10` when a word, head, or local phrase in conformant FPF text is starting to hide what kind it names, which register it belongs to, which context of meaning governs it, or which relation or action claim it carries.

**First useful lexical scan.** Restore the head kind and register of the local wording. If no FPF-governed use remains, make the small local rewrite under `E.10` and stop. If an `E.10:0.2` row selects a precision-restoration realization pattern or a governing pattern, apply that pattern instead of inventing a synonym. If the repaired wording becomes a durable reusable head, apply `F.18` after the selected precision-restoration branch has recovered the kind and use. Governing FPF patterns are named only after that repair has made the EntityOfConcern, relation, claim, admissible use, project-side reference, or non-use disposition recoverable by value.

**Cheap stop.** If one local lexical repair restores kind, relation, and admissible use without changing the normative meaning of FPF, stop with the repaired wording; do not create or use a Name Card, DRR, review profile, or larger epistemic precision restoration note by habit. Ordinary application starts at `E.10:0.2`, applies only the row selected by the sentence under repair, and then stops at local repair, the selected restoration pattern or governing pattern, controlled precision reduction, or `F.18` when a durable reusable head is actually being minted. Later LEX sections are detailed checks for the selected case, not a universal interpretation sequence.

**Not this pattern when.** Do not use `E.10` as the ontology that governs the recovered claim. If the use under repair is evidence, assurance, work, gate, decision, causal use, publication, relation precision, or epistemic precision, the accepted text names the governing FPF pattern application explicitly; `E.10` contributes only the wording-problem classification. For non-FPF source prose, use `C.2.P` source-expression unpacking mode and borrow `E.10` only as a repair test, not as a conformance verdict.

#### E.10:0.0a - One-screen ordinary use

Ordinary `E.10` use is one bounded FPF-governed wording repair, not a full lexical audit. The bounded complete accepted result is:

1. `BoundedTextSpan`: the exact sentence, row, section, pattern version, `DRR` slice, or project text deliberately using FPF-governed terms, pattern references, relation names, or conformance claims under repair.
2. `TriggerSpan`: the word or phrase that carries possible FPF-governed use.
3. `SelectedInterpretation`: ordinary no FPF-governed use, local head repair, register repair, morphology repair, relation-like precision restoration, episteme precision restoration, publication precision restoration, source-use relation or source-ref target recovery, durable naming, or not-triggered false positive.
4. `FinalWordingOrBlocker`: the accepted local wording, the governing-pattern result, or the blocker that remains.
5. `StopBackToSubstance`: once the final wording or blocker is written, return to the domain question that made the phrase matter. Further lexical classification is non-use unless another phrase still hides an FPF-governed claim.

**Plain branch rule for relation-like wording.** Start with the ordinary sentence the reader needs to write, then select one branch. Do not make the reader classify all four.

1. **World fact.** If the sentence asserts that two or more world-side things are related, name those things and say what direct relation obtains: for example, `Pump P feeds tank T`. Apply the pattern that governs that predicate. Name a separate relation occurrence only when a later claim must refer to that same occurrence, compare or qualify it, track its change or continuity, or use it as a participant of another relation. A `feeds` column or an arrow labelled `feeds` is a near-miss: neither makes the fact obtain.
2. **Reusable relation declaration.** If the text tells later authors what the same relation means across several claims or consumers, state that reusable meaning and its participant meanings, then map them to one `RelationSignature` and its A.6.5 `SlotSpec` declarations. One fact such as `P feeds T` is a near-miss: it does not declare a reusable predicate or participant vocabulary.
3. **Relation claim or report.** If the text records that somebody or some source claims a relation, name the C.2.1 claim-bearing episteme and its participant designations: for example, `Inspection note N states that P feeds T`. The note is not a participant in the feeding relation, and recording the claim does not make feeding obtain.
4. **Representation.** If a field, table cell, graph element, or formula stands for something, name the representation element, represented object, and correspondence. Use C.29 when a mathematical-lens use is current; otherwise use the direct representation owner. A column position, argument place, or drawn arrow with no stated correspondence is a near-miss: its shape creates no participant, `SlotSpec`, kind, or obtaining relation.

If none of these branches applies, keep ordinary or quoted wording, name the other governed object and its direct owner, or leave an explicit blocker. The visible result is one readable domain sentence, one reusable declaration, one claim-bearing episteme, one representation with its correspondence, or an explicit non-use or blocker—not a catalogue of all possible owners.

The detailed tables below are reference material for triggered cases, not a fixed interpretation sequence. For a modest repair, one sentence, one trigger span, one selected interpretation, and one final wording or blocker is enough only when it discharges every FPF-governed use in that span.

**Minimal first-use example.** The sentence `The candidate basis is required before pattern use` has one trigger span: `required`. Here the sentence is about candidate-basis completeness, not an accountable undertaking. Apply the direct E.11 construction and write: `The candidate basis is complete for this use only when every reusable basis position declared by the public candidate-use template has a current project filler admitted by that position's CandidatePatternUseBasisCompletenessCondition@FPFReadme.` The repaired sentence preserves the practical consequence, creates no general Requirement object, and closes the E.10 use. Return to the candidate-pattern-use question; do not open the later lexical apparatus or create a wording-repair record. Replay the repair from the quoted sentence and the current E.11 template and completeness-condition definitions. Reopen it if those E.11 definitions change, or if the project statement acquires an accountable subject and authority relation; the latter case applies A.2.8 rather than the completeness construction.

When `E.10` is applied beyond one sentence, add a bounded-text line: exact accepted `DRR` named by value, FPF pattern, monolith section, extracted host, review packet, pattern section, source span, or other named text span; trigger spans or grouped trigger locations; selected interpretation; repair boundary; and expected non-use boundary. This prevents accidental whole-corpus sweeps and makes change impact inspectable.

When a wording-repair note needs formal fields, record one `plainIntent` and the selected branch from `E.10:0.0a` before the technical fields. Keep `triggerSpan`, `boundedTextSpan`, `selectedInterpretation`, `LEX.TokenClass?`, `register`, `USM.Scope?`, `EntityOfConcern and Description-episteme boundary and specification use?`, `governingPattern`, and `finalWordingOrBlocker`; then add only the fields required by the selected branch and its direct owner. If none of the four relation-like branches applies, name the concrete governed object and owner instead. Do not use `slotOrUsePosition` as a union field for actual participants, A.6.5 `SlotSpec` values, participant designations, or representation places.

Local patterns may cite the relevant `E.10` recognition row, but they should not reproduce large wording-recognition lists or create local lexical registries unless a named local application profile has its own primary `EntityOfConcern`, first useful output, and governing-pattern boundary. New recurring wording families enter `E.10` only when they recur across FPF-governed texts and cannot be handled by one local pattern; specialized patterns carry the detailed ontology when the problem is no longer lexical. Stale or overly broad recognition rows are narrowed or retired.

Self-application is bounded. When `E.10` is under improvement, use `E.10` only for its own wording-trigger repairs; use `E.21` for pattern-quality evaluation, `E.22` for improvement-oriented quality-evaluation framing, `E.23` for the improvement loop, `E.2.DA` for FPF-level Pillar effect, and the direct pattern governing relation, episteme, publication, source-use, naming, or quality-word claims.

#### E.10:0.1 - Scope split

`E.10` governs lexical conformance for FPF pattern text, extracted pattern hosts, `FPF-Spec` monolith text, FPF governing documents, accepted `DRR` text, and any project, product, research, engineering, or review text that deliberately uses FPF terms, pattern references, FPF relation names, FPF kind claims, FPF admissibility claims, or claims FPF conformance.

For ordinary source text, intake notes, seminar transcripts, external reviews, project documents, source publications, tool outputs, or other text that does not itself claim FPF-governed use, use `C.2.P` source-expression unpacking mode. That use may borrow `E.10` tests, `A.6.P` relation repair, `A.6.6` basedness repair, `F.18` naming tests, or another governing pattern as methods, but it does not judge the source text as failed FPF wording.

#### E.10:0.2 - Problem and applicability table

`E.10` is a lexical trigger scan and conformance pattern. Its primary `EntityOfConcern` for one pattern use is one wording use in conformant FPF text as a lexical or register sign: the head, register, morphology, local label, name candidate, kind-reference, relation-bearing cue, or replacement candidate used by the sentence.

`E.10` recognizes which wording-use problem the sentence raises and selects the first applicable closure disposition. It does not itself become the ontology for the recovered relation, episteme, evidence, work, gate, decision, publication, architecture, characteristic, quality, or project-side FPF kind and reference named by value.

The full shared recovery order and applicability-row architecture are in `E.10.ARCH`. One E.10 use contains the cheap scan, local rewrite option, direct known governing-pattern rule, compact applicability table, bounded complete result rule, and fail-closed non-use boundary.

`exact` is not a precision marker by itself. It is admissible only for literal identity or bounded source identity: an exact sentence, source passage, trigger span, formula, episteme edition whose claims define that formula, same referent, or same declared `CharacteristicSpace`. When `exact` modifies an FPF pattern, kind, relation, record, object, field, use, claim, gate, source, or governing pattern, write the ordinary identity claim and, for relation-like wording, select the applicable `E.10:0.0a` branch. Then name only the direct owner and branch-specific objects needed by that sentence. Add a source-use relation, admissible use, claim kind, value set, or scope only when omitting it would change what the sentence identifies or licenses. `Exact` without that local identity and use test closes nothing. If recovery fails, use a quote-only, reduced-use, blocked-use, or incomplete-rewrite disposition.

Classification is not closure. A conforming result ends in one of these by-value outcomes:

- local wording accepted or locally rewritten;
- selected precision-restoration pattern applied;
- direct governing FPF pattern applied because the primary `EntityOfConcern`, obtaining direct relation and actual participants, receiver-needed relation occurrence, reusable A.6.5 declaration, claim-bearing episteme and any participant designations, or C.29 representation and explicit correspondence are already recoverable;
- controlled precision-reduction result with declared loss and reopen condition;
- `F.18` durable-name application after the kind under repair or relation is known;
- quote-only, reduced-use cue, blocked use, incomplete rewrite, ordinary prose, or not-triggered disposition.

**Grouping-mark self-application.** Slash marks, paired-register marks, `and`, `plus`, `&`, and compact grouping marks are triggers only when the grouping itself carries FPF-governed meaning. Retain conventional notation, formula symbols, ratios, discipline abbreviations, path-like quoted source tokens, product names, titles, URLs, or pattern-reference notation when the sentence's use is only notational; examples include `CI/CD`, `1/2`, `≡/⋈/⊂/⟂`, and exact source tokens. Rewrite claim-bearing grouped heads into explicit lists that keep unlike kinds separate; explicit alternative cases; obtaining direct relations with actual participants; reusable relation-declaration sets with their `RelationSignature` and A.6.5 `SlotSpec` values; claim-bearing epistemes; C.29 tuple or other representation elements with explicit represented objects and correspondences; or selected FPF kinds named by value. Do not let a slash hide one kind choice, an unresolved alternative, a relation claim, an admissible-use boundary, or a missing governing pattern.

**Modifier, compound-head, and enumeration-as-kind self-application.** A modifier without a recovered head, a compound whose head word is only a vague carrier such as `source`, `support`, `basis`, `note`, `record`, `field`, `condition`, or `use`, or a repeated enumeration that starts acting like one kind is an `E.10` trigger when it carries FPF-governed use. First expand the phrase into one ordinary sentence. For relation-like wording, select one `E.10:0.0a` branch and recover only that branch's result; otherwise name the head kind, closed value set, explicit alternatives, or non-use and its direct owner. If the direct governing pattern is known, use it. If source-ref target wording, publication, carrier, or project-side reference is still hidden, use `C.2.P`; if move, step, action, or readiness wording is current, use `E.10.MOVE`; if architecture or stratification source-label wording is current, use `E.10.ARCH`, `C.30.P`, or `C.30.STRAT`. If no direct-owner result can be written, lower the phrase to ordinary prose, quote-only wording, a reduced-use cue, split alternatives, or blocked use; do not close by inventing a broader umbrella name.

**Source-to-use continuity prompt.** When the trigger word is `source` or a source-like modifier, conforming final wording preserves the source-to-use relation, not only the recovered head kind. Check five questions before closing: which concrete source expression, source `U.Episteme`, source `U.EpistemePublication`, publication face, carrier relation, source-ref marker with its referenced object kind named or, when it targets a reusable declaration, the exact A.6.5 `SlotSpec` named, source-currentness relation, source-bearing relation, relation-claim slice, project-side FPF kind and reference, declared-use boundary, or explicit non-use disposition is current; which exact governed entity from that source-side set is used now; which direct source-to-use, transformation, rendering, or other use relation carries it forward; which current use is admissible; and which reopen condition or governing pattern applies if the use becomes stronger. A source-ref marker alone is not a repair result: if the referenced object kind or exact declaration-local `SlotSpec` is not recoverable, close as source-finding, quote-only, reduced-use, or blocked use. Do not close on `value` unless the governing pattern actually has a value slot. If the answer is hidden, route to `C.2.P`, `A.6.3.CSC`, `E.17`, `A.10`, or the direct governing pattern rather than accepting a precise but unhelpful noun.

`source-return condition` is not this whole prompt. It is a narrower reverse or escalation condition used when a derivative, coarsened, extracted, compressed, rendered, or reused carrier has already moved away from a named source expression, source `U.EpistemePublication`, source-bearing relation, transform record, evidence relation, or governing pattern position and a stronger use opens return to that named endpoint or governing pattern. Use `source-to-use path` or the direct source relation when the current sentence is about departure from a source expression, source publication, or source-bearing relation into use.

| FPF-governed use found by `E.10` | First applicable restoration or governing pattern | Closure result |
| --- | --- | --- |
| No FPF-governed use after context check | Keep ordinary prose, quote, didactic phrase, or not-triggered text. | No precision-restoration pattern opens. |
| Local lexical or register ambiguity only | Local rewrite under `E.10`. | Repaired wording plus remaining reader use, or ordinary-prose demotion. |
| Modifier-without-head, vague compound head, or enumeration-as-kind wording whose governed head, declaration, direct relation, representation, alternative cases, or direct governing pattern is hidden | Apply `E.10` head-kind recovery first, then the direct governing pattern if recoverable. Otherwise use the selected restoration branch: `A.6.P` for relation construction, `C.2.P` for source-ref target, publication, carrier, or project-side reference recovery, `E.10.MOVE` for move, step, action, or readiness wording, `E.10.ARCH` plus `C.30.P` or `C.30.STRAT` for architecture or stratification source-label wording, `E.24` when a real ontic candidate decision is current, or `F.18` only after the governed kind and use are recovered. | Selected FPF kind or alternative-case set; obtaining direct relation and actual participants; receiver-needed relation-occurrence identity; reusable `RelationSignature` with A.6.5 `SlotSpec` values only when declaration is current; claim-bearing episteme and participant designations only when an assertion is current; C.29 representation element and explicit correspondence only when representation is current; ordinary-prose demotion; reduced-use cue; blocked use; or incomplete-rewrite disposition. No list or compound head becomes a kind by itself. |
| Relation-like wording or relation-bearing use | Apply `A.6.P` or a retained A.6 relation specialization. Only when exact participants are recovered and no current direct relation closes the named receiving claim, route the residual to `A.6.RCD`. | State the obtaining named direct relation, actual participants, and qualifier values. Distinguish one relation occurrence only for a named receiving use; add a reusable `RelationSignature` and A.6.5 participant or qualifier `SlotSpec` values only when declaration is current; keep a row that states the claim as a claim-bearing episteme with participant designations, and keep any graph, tuple, field, or table element as a C.29 representation with explicit correspondence. Otherwise return the exact residual `A.6.RCD` membership: disposition 2, a local compound claim; disposition 3, a reusable predicate-definition episteme, optionally continuing to a derived-kind candidate plus its proposed direct subject settlement only when a named receiver additionally needs stable occurrence semantics; or disposition 4, a primitive-kind candidate plus its candidate standalone direct pattern. `E.24` and `E.24.UK` retain admission, and `A.6.0` declaration follows only after admission. Every branch preserves admissible relation use, blocked overread, and remaining reader use. |
| Relation, signature, interface, role, assignment, enactment, slot, field, parameter, argument, endpoint, port, API, protocol, connector, capability, affordance, method, function, concern, interest, or role-holder wording whose current governed object or claim kind is hidden | Apply `A.6.RSIR` only when the direct governing pattern is not already clear. If a world-side relation use is current, recover its participants and existing direct relation through `A.6.P`; use `A.6.RCD` only when those participants are exact but no current direct relation closes the named receiving claim. If the current object is already recovered, use the direct pattern instead: `A.6.P`, `A.6.5`, `A.6.0`, `A.2`, `A.2.1`, `A.15`, `A.6.M`, `A.6.F`, `A.6.A`, method and work patterns, publication and episteme patterns, evidence patterns, status patterns, gate patterns, or another governing pattern named by value. | Recovered project concern, current EntityOfConcern or claim kind, selected direct governing pattern, recovered direct relation and participants when relation use is current, exact `A.6.RCD` disposition only when the residual route is triggered, slot-discipline need, retained source-label use, blocked overread, and stop before minting generic `U.Interface`, a standalone role-slot ontology, `U.Concern`, `U.Interest`, or episteme-role ontology. |
| Source-expression, publication, publication form, face, carrier, rendering, `PublicationUnit`, framework publication or access carrier, FPF-governed use, or `reading`, `read`, or `quality-read` wording whose entity or construction is not yet recovered | Apply `C.2.P` first. If the recovered construction is only publication or access exposure, use `E.17`, `E.17.AUD`, or `E.4.*` as applicable; if it is evidence, source-currentness, generated-output admission, work-reliance repair, architecture use, or structure use, use `A.10` or `G.11`, `C.35`, `A.15.4`, `C.30.P`, `C.33`, or `C.34` after `C.2.P` recovers the carrier relation set. If the recovered entity or construction is evaluation for improvement, use the evaluation pattern governing that evaluation claim, such as `E.22`, `E.21`, or `E.9.DA`. | Source-local meaning, publication and carrier relation set, publication-form relation when that relation is being made, EntityOfConcern, project-side FPF kind, use disposition, downstream governing pattern named by value when the carrier is evidence, currentness, generation, framework publication or access, work-reliance repair, architecture use, structure use, or evaluation, adjacent overread blocked, and remaining reader use. |
| Ontic, ontic candidate, concept cluster, semantic area, ontological neighborhood, slot relation, schema, data structure, record, card, table, or publication-form wording whose EntityOfConcern and publication boundary are hidden | Apply `E.24.CD` when repeated material may call for an ontic candidate decision; apply `E.24.PUB` when the confusion is among ontic, ontic-description episteme, publication form, view, record, card, table, schema, or data-structure expression. Use `E.24` or the direct governing pattern when the ontic or subject pattern is already recovered. | Candidate ontic cluster, EntityOfConcern, and subject pattern; only after durable settlement, the exact E.24 `onticSlotRelation` and its actual participants; or, under their separate owners, an ontic-description episteme, reusable `RelationSignature` and A.6.5 `SlotSpec` values, publication form, C.29 representation element and explicit correspondence, or source relation. Preserve admissible use, blocked publication-form overread, and remaining reader use. |
| Admissibility-like, external-rule-looking, authority-looking, readiness-looking, validity-looking, pass-looking, fail-looking, or conformance-looking wording whose bearer, claim kind, source relation, value frame, bounded use, or governing pattern is hidden | Use the direct governing pattern when recoverable: evidence, assurance, gate, constraint validity, work, work plan, publication use, temporal use, `A.15.4` appearance-based reliance repair, external-rule claim, pattern-quality result, state-like value, dated-work finalization or completion claim, measurement-result episteme, evaluation result, `C.11` `ChoiceResult` or decision record, or another claim-specific pattern. If the word is only the trigger, restore by `E.10.ARCH` and the claim-specific pattern; do not mint a generic admissibility object. | Bearer, claim kind, value frame or decision class, source relation when that relation is being made, bounded admissible use, non-admissible overread, reopen or stop condition, and governing pattern; otherwise quote-only, reduced-use, or blocked-use. |
| Method, practice, technique, algorithm, program, solver, proof, recipe, workflow, process, procedure, access-path, query-plan, control-strategy, method algebra, method graph, selector calculus, or programming-paradigm wording whose governed method-side object or direct relation is hidden | Recover that governed object or direct relation before rewriting: `A.3.1 U.Method`, `MethodRelationStructure@BoundedContext` when method composition or method-family relation is current, `A.3.2 U.MethodDescription`, `A.6.0` formal-substrate declaration, `C.29` mathematical-lens use, `A.6.1` with `E.20` mechanism claim, `A.15.2 U.WorkPlan`, `A.15.1 U.Work`, `A.2.1` role assignment, `A.2.7` role relation structure, `A.1.1` bounded context, `C.20` discipline position, `C.36.P` when practice or technique is cultural-evolution wording, `G.5` method-family registry or selector outcome, `A.10` evidence relation, quote-only source wording, or another direct governing pattern. | Pre- and post-repair governed object and direct owner—one exact `U.Method`, one exact method-side relation, one-method `U.MethodDescription` episteme, formal-substrate declaration, C.29 representation and correspondence, mechanism, plan, dated Work, transformation, result, or other direct claim—plus admissible use, blocked overread, and remaining reader use. Do not replace one umbrella with `method`, `practice`, `mechanism`, `algorithm`, `workflow`, or `method algebra` by taste. |
| Input, raw-material, source-data, source-material, output, result, outcome, deliverable, handoff, or reusable work-name wording whose exact relation involving a Work occurrence or exact occurrence basis is hidden | For epistemic source data or source material, use `C.2.P` first and then `A.6.P.WMR` for a separately current claim involving a Work occurrence; keep physical raw material under its direct physical governor. Otherwise apply `A.6.P.WMR` after generic relation recovery. Use `F.18` only for a durable name after the governed value and use are recovered. | First recover the exact entity under its own admitted kind and the exact related object. Keep claim subject, modality and exact temporal extent, polarity, and recovery/support state separate, then return exactly one family: exact direct subject-relation claim, positive or governed negative; exact `A.6.1` operation-application binding; exact local `A.15.PROD`/`A.6.RCD` claim; or exact non-assertability result. Select `factually unsupported` for the failed known `EpistemeUsedByReviewWorkAsReference` predicate, `missing-information` for the unavailable ETL receiving-use fact under a known governor, and `missing-governor` for the absent `Patient_8472` / `HE-8472` health-effect relation kind and owner. Only the last branch names the affected use and future owner; none supplies opposite polarity. A performed-work name additionally rests on its `A.15.1` occurrence basis, and neighboring governed results remain separate. |
| Transformation, change, pipeline, dataflow, flow, network, circuit, path, slice, workflow, process, operation, or close change-situation wording whose governed change object, direct relation, declaration-local operation binding, or representation place is hidden | Apply `A.3.4.P` first. If `U.Transformation`, `TransformationFlowStructure`, mathematical description, method, method description, mechanism, work plan, dated work, functioning relation, temporal aspect, evidence, source, publication, gate, decision, assurance, exact changed referent, declaration-local operation-result binding, measurement-result episteme, evaluation result, `C.11` `ChoiceResult` or decision record, or quote-only source wording is already recovered, use the direct governing pattern. | Recovered transformation identity or non-transformation value; exact changed referent and any obtaining direct relation with actual participants; declaration-local operation-result binding only when that A.6.1 declaration is current; C.29 representation and explicit correspondence when source wording names a field, argument, graph element, or other representation place; exact separately governed measurement, evaluation, choice, decision, or other direct-pattern claim when current; governing pattern; retained use; blocked overread; and remaining reader use. Do not replace one source label with `flow`, `network`, `process`, `method`, `function`, or `transformation` by taste. |
| Move-like wording such as first move, working move, next move, pattern move, project move, architecture move, local move, or readiness move whose governed text span, claim being made, object under wording repair, direct FPF target, and remaining reader use are hidden | Apply `E.10.MOVE` first unless a local governing pattern has already recovered the exact local object, such as A.16 language-state move, C.24 `nextPlannedAction`, or C.30 architecture candidate use. | Recovered governed text span, claim being made, object under wording repair, source wording class when source wording is being classified, and direct FPF target such as `PatternUseRecommendation@Context`; `PatternUseSequence@Context` only as the `totalOrder` specialization of one named `PatternUseCoordination@Context`; P2W carry-through; WorkPlan; `WorkEntryReadiness@Context`; GateDecision; an actual Work occurrence admitted under `U.Work`; A.16 local move; C.24 next action; C.30 architecture candidate use; ordinary prose; quote-only wording; or blocker. Do not mint root `U.Move`. |
| Declarative representation wording overread as imperative action, method, work, deontic permission, work authorization, release authorization, evidence, or pattern dispatch: graph path, path slice, flow valuation, evidence-path wording, state predicate, SQL-like query, checklist predicate, table, dashboard, publication face, mathematical representation, method-description representation, source-chain relation, file path, or FPF pattern relation | Apply `C.2.P.DR` unless the direct governing pattern already closes the repair. Accepted direct cases include `E.18` graph path or `PathSlice`, `A.10 evidence relation or evidence-provenance relation for a claim, effect, or use`, `A.19.SPR` state predicate or value, `E.17` publication face, `C.29` mathematical-lens use, `A.3.1` method, `A.3.2` method description, `A.15.2` work plan, `A.15.1` work occurrence, carrier file path, source-chain relation, and declarative pattern relation under `E.8` or `F.19`. | Visible expression or artifact; exact current direct object, claim, or relation; exact representation use or explicit correspondence, or `none`; and the stronger action or inference that stays blocked. When current, also name the source or publication relation, direct governing pattern, retained use, non-admissible overread, and stop or reopen trigger. A visible artifact is not classified as a representation merely by its form. |
| Architecture or structure wording with hidden selected structure, `ArchitectureOf@Context` relation, architecture-description use, structural-view use, source-return condition, or named C.30 subcase | Apply `C.30.P`. If `A.22`, `C.30`, `C.30.ASV`, or a named C.30 subpattern is already recoverable, use it directly. | Recovered selected structure, `ArchitectureOf@Context`, architecture description, structural view, source-return condition, governing-pattern result, or stop. |
| Holon, system, episteme-as-holon, collection, part-whole, multilevel, interlevel, boundary, interaction, functioning, capability, emergence, BOSC, MHT, MET, MFT, `post`-like, or promotion-like wording whose object kind, part-whole relation, boundary-crossing relation, transformation relation, architecture relation, ethical conflict relation, or admissible-use boundary is hidden | Recover the object kind and relation first. Use `B.2.P` only for emergence-family, MHT-family, MET-family, MFT-family, synergy, metric-mirage, whole-reidentification, and collection wording entangled with those ambiguities. After recovery use the direct governing pattern: `A.1` for the holon or system claim, `C.2.1` or the publication pattern named by value for episteme and publication claims, the part-whole or collection governing pattern named by value, `B.2` for whole reidentification, `B.2.2` for result-system MHT, `B.2.3` for result-episteme MHT, `B.2.4` for capability or functioning whole reidentification, `B.2.5` for supervisor-subholon feedback relation, `A.3.4.P` for transformation wording, `A.6.F` for functioning or capability-like wording, `C.30`, `C.30.ASV`, `C.30.LCA`, `C.30.ILC`, `C.30.STRAT`, `D.2`, `D.3`, `D.4`, or another governing pattern named by value. | Recovered holon, system, episteme, collection, part-whole relation, boundary-crossing relation, transformation relation, architecture relation, supervisor-subholon feedback relation, interlevel ethical conflict, mediation use, source-label repair, admissible use, non-admissible overread, and stop. Do not mint `U.Level`, `U.SystemLevel`, `U.HolonLevel`, `U.Frustration`, `U.Emergence`, or treat governing-pattern selection as procedural control flow. |
| Culture, cultural evolution, style, tradition, genre, scene, technique, practice, platform, regime, measurement regime, attractor, developmental machinery, or close cultural-evolution wording whose current object is hidden | Immediate disposition: recover the current object first: method family, work family, role assignment, discipline, canon or memory episteme, recognition or selection regime, mediation system or architecture, measurement or visibility relation, publication label, variant set, dynamics or mathematical-lens claim, bounded context, development-loop relation, or cultural-evolution case. Use the method-like row above when `practice` or `technique` is just the ordinary word for a way of doing; use `C.36` when a collective-holon or discipline-facing cultural-evolution case is current; use `C.36.P` for repeated wording-use recovery; use `F.17`, `F.18`, and `F.9` for durable terms and bridges; use `A.3.1`, `A.3.2`, `A.15`, `C.20`, `C.23`, `A.3.3`, `C.27`, `C.29`, `C.18`, `C.19`, `G.5`, `G.11`, `E.18.1`, `C.22.2`, `C.16`, `A.19`, or `C.11` according to the recovered object. | One root cultural ontology by source word, root `U.Culture`, `U.Style`, `U.Tradition`, `U.Practice`, `U.Platform`, `U.PlatformRegime`, `U.MeasurementRegime`, `U.DevelopmentalMachine`, loose style-as-attractor ontology, or one umbrella replacement word. |
| External holon-class or Holon Graph Architecture (HGA) graph-expression wording such as `AgentHolon`, `OrganisationHolon`, `DataHolon`, `ProcessHolon`, `Portal`, `Projection`, event envelope, provenance, target holon, projection envelope, projected content, envelope, payload, RDF graph, node, edge, traversal, or boundary-governed payload whose FPF object is hidden | Recover the claim before importing the source label. Use `A.1` for admitted system or holon claims; `C.2.1`, `E.17`, architecture-description, publication, source-relation, or evidence governing patterns for data, document, projected content, description, publication, view, or evidence claims; `A.10`, source-relation, evidence-relation, dated-work, or publication governing patterns for event and provenance claims; `A.3.4.P`, method governing patterns, work-plan governing patterns, or work governing patterns for process-like wording; `A.6.RSIR`, `A.6.P`, `A.6.0`, `A.6.5`, `A.6.M`, `A.6.C`, `A.6.8`, or policy governing patterns for portal, access, traversal, boundary-crossing, signature, module-interface, service-access, protocol, agreement-like, or evidence-relation claims; `C.29`, `A.22`, `C.30.ASV`, `C.30.AD`, `E.17`, source-relation, or publication governing patterns for graph, RDF, node, edge, or traversal expression claims; use `A.6.B` only for L, A, D, or E statement classification inside a boundary package. | W3C Community Group Holon Graph Architecture (HGA) vocabulary is retained as a serious source-finding cue or comparison term only after the recovered FPF object is named and differences from FPF are explicit. Do not mint source-class U-kinds such as `U.AgentHolon`, `U.DataHolon`, `U.ProcessHolon`, `U.Portal`, `U.Projection`, `U.Envelope`, or `U.Payload`; do not turn semantic-web class names or graph-expression vocabulary into FPF ontology. |
| Markov blanket, Markov border, computational boundary, boundary leak, or active-inference boundary wording whose object kind or claim kind is hidden | Recover whether the source-bearing external phrase names accepted local Markov dynamics, a mathematical or probabilistic lens, holon delimitation, boundary-crossing relation, relation precision, signature or slot declaration, interface, interface module, functional element, physical component, boundary description or publication, boundary-package statement classification, or agency-threshold claim. | Use `A.3.3`, `C.29`, `C.26`, `C.26.3`, `A.1`, the direct relation-governing pattern, `A.6.RSIR`, `A.6.P`, `A.6.0`, `A.6.5`, `A.6.M`, `A.6.F`, `A.14`, `C.13`, `B.3.5`, `C.30.AD`, `E.17`, `A.13`, `A.19`, or `C.16` according to recovered claim; use `A.6.B` only for L, A, D, or E statement classification inside a boundary package. Do not mint `U.MarkovBlanket`, generic `U.Boundary`, generic `U.Interface`, or binary `U.Agent`; do not collapse statistical separation, physical boundary, interface module, description, boundary-package classification, and agency threshold. |
| Stratification or structure-source-label wording such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate` when the FPF kind under repair, relation, claim-use, or source-use disposition is not yet recovered | Apply `C.30.STRAT` first. If a control-layer relation, module-interface relation, architecture-to-`TransformationFlowStructure` relation, mathematical scale relation, coarse-graining relation, publication relation set, gate relation, or other governed use named by value is already recovered, use that governing pattern directly. | Recovered FPF kind, relation, claim-use, source-use disposition, and governing pattern; `StratificationSourceLabelRepairNote`; ordinary source label; quote-only, reduced-use, or blocked-use disposition; or stop. |
| Characteristic, scale, score, coordinate, metric, indicator, threshold, comparison, or scalar-quality wording with hidden construction | Apply `C.16.P`. If `A.17`, `A.18`, `C.16`, `A.19`, `C.25`, `C.29`, `E.21`, or a governing pattern is already recoverable, use it directly. | Recovered `Characteristic`, `Scale`, `Coordinate`, `Value`, `Score`, unit, scoring method, comparison basis, indicator role, governing-pattern result, or stop. |
| State-family wording with hidden bearer, state frame, value set, admissible use, or governing pattern: `state`, `status`, `posture`, `readiness`, `stance`, currentness, or close compounds | Apply `A.19.SPR`. If the governing pattern and state-like field are already recoverable by value, use that governing pattern directly. | Recovered bearer, state frame or governing pattern, value or classification, admissible use, non-admissible overread, reopen condition, governing-pattern result, or stop. |
| Quality or evaluative characterization wording | Apply `C.16.Q`, `C.25`, `E.21`, or another characterization pattern governing the claim after any needed `C.16.P` repair. If the found problem is relation construction, apply `A.6.P` instead. | Quality-term repair, Q-bundle or pattern-quality coordinate use, relation split or bridge split when that relation or bridge claim is being made, and blocked scalar, gate, or release overread. |
| Function-like wording with hidden FPF kind, relation, claim, view, or governing-pattern application: `function`, `functional`, `functionality`, `effect`, or close compounds | Apply `A.6.F` first when kind and relation recovery is needed. If the FPF kind named by value or pattern relation is already recovered by value, use the governing pattern directly. | FPF kind or relation named by value assignment, governing-pattern application, mathematical-lens use, quality pattern application, characteristic pattern application, module-interface pattern application, ordinary-prose demotion, or stop. |
| Intentional loss of precision for a narrower admissible use | Apply the controlled precision-reduction pattern, normally `A.6.3.CSC`, with `E.17.*`, `A.6.3.RT`, `F.9`, or `C.29` when that relation is being made. | Source-bearing side, declared loss, narrower admissible use, blocked downstream use, and reopen condition. |
| Durable reusable head, lineage label, concept-set row, cross-context name-use, or UTS-facing name | Apply `F.18` after the selected repair has recovered what the name would name. | Name card or naming row only for durable naming need; one-off local wording closes locally. |
| Trigger found but kind, relation, substrate, governing pattern, admissible use, or remaining reader use cannot be recovered | Fail closed. | Quote-only wording, reduced-use cue, blocked use, incomplete rewrite, ordinary prose, or not FPF-governed wording. |

`reading`, `read`, and `quality-read` are trigger wording only when the sentence uses the word to carry interpretation, publication use, source-use assignment, evaluation, comparison, evidence, gate, work, decision, release, assurance, or admissibility claim. Do not create `ReadingPrecisionRestoration`. Recover the actual EntityOfConcern; the exact publication, carrier, or source-use relation and its governed participants; the evaluation claim or bundle; an obtaining direct relation and actual participants; a world-side Work occurrence; or a separate claim-bearing episteme about one, then apply `C.2.P`, `E.17.ID.CR`, `E.22` plus object-under-improvement evaluation named by value, `A.6.P`, or the direct FPF pattern governing that claim.

`function`, `functional`, `functionality`, and `effect` are trigger wording when the FPF kind named by value, relation, claim, view, or governing-pattern application is hidden. Do not assign the wording by architecture default. `A.6.F` remains the function-like wording unpacker; mathematical function, mapping, relation, loss, objective, value functional, or operator goes to `C.29` when mathematical-lens use is being claimed. Functional-architecture use goes to `C.30` or `C.30.ASV` when the architecture or structural-view claim is recovered by value; architecture-to-`TransformationFlowStructure` use goes to the current Architecture Transformation-Flow Structure Relation (`C.30.TFS-REL`).

`layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, and `gate` are source labels when they first arrive from engineering, mathematical, publication, or project prose without a recovered FPF kind. Do not mint `U.Layer`, `U.Level`, `U.Tier`, `U.Stack`, or a universal stratification kind. Use `C.30.STRAT` to recover the governing pattern, or go directly to the governing pattern when the FPF kind under repair, relation, claim-use, or source-use disposition is already recovered by value: `C.30.LCA` for control-layer relations, `A.6.M` for module-interface relations, the current Architecture Transformation-Flow Structure Relation (`C.30.TFS-REL`) for architecture-to-`TransformationFlowStructure` claims, `E.18` for selected transformation-flow structure, `C.16.P` or `C.29` for scale relation, coarse-graining relation, or mathematical use, `C.2.P` for publication relation set or source-use relation, and gate patterns, work patterns, or decision patterns when those claims are being made.

Description, publication, and representation mediation source words need the same recovery discipline. Treat `stack`, `lane`, `profile`, `mediation`, `binding`, `representation`, `publication`, `model`, `space`, `graph`, `latent`, `weights`, `embedding`, `vector store`, `carrier`, `dashboard`, `posture`, `route`, `path`, `surface`, and close compounds as trigger wording when the sentence has FPF-governed use and the exact governed object, obtaining direct relation and actual participants, reusable A.6.5 declaration, claim-bearing episteme, or representation correspondence is hidden. Recover the current EntityOfConcern; the direct relation and actual participants; a `RelationSignature` and A.6.5 `SlotSpec` values only when declaration is current; or the C.29 representation element, represented object, and explicit correspondence; then name the direct governing pattern, admissible use, blocked overread, and remaining reader use before writing the final phrase. Do not replace the trigger with another umbrella head; do not mint a durable name unless `F.18` is explicitly selected.

Local patterns may cite the relevant `E.10` recognition row. They do not reproduce the wording-recognition table or create local lexical registries unless a named local application profile has its own primary `EntityOfConcern`, first useful output, and governing-pattern boundary. Specialized restoration patterns carry the detailed ontology when the problem is no longer lexical.

#### E.10:0.2a - Bounded complete result and direct known governing-pattern rule

The direct known governing-pattern rule is:

> If the governing pattern and the current `EntityOfConcern`, obtaining direct relation and actual participants, receiver-needed relation occurrence, reusable A.6.5 declaration, claim-bearing episteme and any participant designations, or C.29 representation and explicit correspondence are already recoverable by value, use that governing pattern directly.

Apply a precision-restoration realization pattern such as `A.6.P`, `A.6.F`, `C.2.P`, `C.30.P`, `C.30.STRAT`, `C.16.P`, `C.16.Q`, or `A.19.SPR` only when wording hides the EntityOfConcern under repair, relation, characteristic, scale, score, quality characterization, source-use disposition, state-family field, admissible use, or remaining reader use.

The bounded complete result is the shortest result that fully recovers the kind under repair and remaining reader use. Shortest is not lowest effort: every FPF-governed use has a by-value disposition, and `not triggered` or ordinary prose is stated as such with the checked span.

- local rewrite for a one-sentence local ambiguity;
- compact repair note or row when one precision-restoration pattern is needed;
- governing-pattern application when the FPF kind under repair, relation, claim-use, source-use disposition, or admissible-use boundary is already recoverable;
- full restoration check only when several claims being made, admissible-use cases, source-currentness relations, cross-pattern authority, or downstream reliance remain under repair;
- fail-closed non-use when recovery is not possible.

After kind and governing pattern recovery, state the remaining admissible reader use: what the reader may now do, why the distinction matters, or which FPF pattern now carries the claim being made. If the repaired wording is kind-correct but inert, the repair is incomplete.

**Value-substitution check.** A wording repair also fails when it optimizes lexical purity while making the working text worse: less readable for its declared reader, less affordable to apply, less semantically composable with named governing patterns, less clear about the primary `EntityOfConcern`, obtaining direct relation and actual participants, receiver-needed relation occurrence, reusable A.6.5 declaration, claim-bearing episteme and any participant designations, or representation and correspondence, or less action-guiding. In that case, narrow the repair, keep ordinary wording with a recovery note that states the recovered kind and use, use the direct governing pattern, or leave the issue blocking by value. Do not trade real kind, relation, source-use, or admissible-use recovery for smooth prose; this check prevents precision-restoration theatre, not ontology repair.

Tool-assisted trigger inventories may help find candidate spans, but they cannot close ontological precision repair. Closure remains the exact governed object and direct owner; any obtaining direct relation and actual participants; any receiver-needed occurrence, reusable A.6.5 declaration, claim-bearing episteme and participant designations, or C.29 representation and explicit correspondence that is current; admissible use; non-admissible overread; and remaining reader use by value.

**Replacement-candidate closure.** A repair that replaces one trigger word with another word or phrase is not closed until the replacement candidate itself passes the same `E.10` trigger scan. If the candidate is another umbrella word, quasi-scale, process metaphor, role-free deontic word, or untyped head, recover the kind named by value, relation, admissible use, and governing pattern, apply `F.18` when a durable name is being minted, or fail closed. A bounded repair can repeat `E.10` until the candidate wording reaches a stable closure point: ordinary wording with no FPF-governed use, local repair with recovered kind and use, governing-pattern application, `F.18` durable-name result, controlled precision-reduction result, or explicit blocker. Do not accept a smoother synonym as repair evidence.

**MG-DA cold-reader closure.** A repair is closed only when a reader who has not read the `DRR`, campaign notes, or reviewer memory can recover the exact governed object and its FPF kind or ordinary non-FPF status; the obtaining direct relation and actual participants or the claim-bearing episteme; any separately current declaration, designation, or representation and correspondence; the admissible reader use; and the next governing pattern when a stronger claim is being made. Replacing a trigger with `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, `specialization`, or another broad head fails this check unless the sentence names the specific governed object and direct-owner use that make the wording meaningful: for example the obtaining relation and actual participants when a relation is claimed, the exact A.6.5 `SlotSpec` when a reusable value declaration is current, the condition bearer when a condition is claimed, or the receiving governing pattern when authority is being assigned. A complete `specialization` phrase says what specializes what, by which specialization relation or governing pattern, and which inherited or changed declarations or uses matter. This is the MG-DA test for wording repair: the repaired phrase preserves meaningful generality without losing the domain object a practitioner recognizes.

#### E.10:0.2b - Wording-Use Trigger Check Registry

`E.10:0.2` is the shared trigger scan. This section is the check registry for high-pressure wording in FPF-governed text and source prose being unpacked for possible FPF use. It does not create a second all-purpose ontology and does not create domain-pattern outcomes. It selects a closure disposition: local rewrite, selected precision-restoration realization pattern, governing pattern, controlled precision reduction, `F.18` durable-name application, or fail-closed non-use.

The words below are frequent in conformant FPF text and in project texts that deliberately use FPF-governed terms, pattern references, relation names, or conformance claims.
Files carrying FPF pattern text are useful search examples, not the boundary of language cleanup: the same rule applies wherever the text under repair is claim-bearing FPF, project guidance that deliberately uses FPF-governed terms, pattern references, relation names, or conformance claims, or source prose being unpacked for possible FPF use.
They are not banned words.
They are words that trigger kind recovery when they carry an ontology, authority, evidence, or admissibility claim. The table gives alternatives to recover from; it is not a group kind. The chosen result may be a local wording repair, a selected restoration pattern or governing-pattern application, controlled precision reduction, or an explicit not-triggered disposition.
| Trigger words | Recovery choices; write the selected direct-owner result—governed object, obtaining direct relation and actual participants, receiver-needed occurrence, current A.6.5 declaration, claim-bearing episteme, or C.29 representation and correspondence—or a not-triggered disposition before use | Inadmissible reading |
| --- | --- | --- |
| `case`, `scenario`, `example`, `pilot`, `anti-case` | worked case, recognition case, pilot case, negative control, project situation, evidence case, comparison case, or source example | proof, evidence, universal pattern, accepted `DRR`, source basis, or decision by itself |
| `basis` | source basis, decision basis, evidence basis, comparison basis, threshold basis, grounding basis, admissibility basis, or authority basis | generic reason, untyped support, or "whatever the text relies on" |
| `force`, `load`, `bearing`, `claim force`, `claim-force-bearing`, `force-bearing`, `claim-bearing`, `relation force`, `qualifier force`, `support force`, or close compounds | claim being made or admissible-use boundary, relation-bearing use, or a `support` use recovered under `E.10:0.2` as ordinary or quoted non-use, a direct subject relation with its things and predicate named, or one common alternative stating what describes, bears on, enables, or helps what and for which use; qualifier claim; action-guidance use whose governing pattern is named; evidence-use criterion; assurance, gate, work, decision, release, or admissibility use; or a conventional pattern-language `Forces` entry naming a tension that shapes the pattern | unstated strength scale, hidden authority, unnamed evidence weight, unnamed importance, process load, generic pressure, or proof that a wording repair closed |
| `context`, `scope`, `frame` | bounded context, project operational context, review context packet, source context, reference frame, viewpoint frame, or claim scope | world, situation, authority, authority-reference status, or hidden qualifier |
| `state`, `status`, `posture`, `readiness`, `stance`, `currentness`, or close state-family compounds | state-like claim over a named bearer, state frame or governing pattern, value or classification, admissible use, non-admissible overread, and reopen condition; apply `A.19.SPR` when hidden | maturity adjective, authority, gate passage, deontic permission, release authorization, evidence, assurance, source authority, work completion, or process state by appearance |
| `claim`, `claim content`, `claim referent` | claim node or claim content in a claim-bearing episteme, claim-bearing publication, admissibility target, EntityOfConcern, or referent relation | sentence, opinion, text fragment, document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use, or whole publication unit |
| `evidence`, `witness`, `ground`, `proof` | evidence record, evidence relation, evidence-provenance relation, witness, grounding relation, source pin, observation, validation result, or assurance argument component | authority, approval, gate, engineering justification, or truth by label |
| `authority`, `permission`, `approval`, `commitment`, `obligation` | role assignment, speech act, commitment record, authority relation, gate record, decision record, or policy claim | visible label, author confidence, reviewer praise, explanation, or provenance mark |
| `requirement`, `required`, or close requirement-headed compounds | run `E.10:0.2b.1`; recover bearer, exact claim or relation kind, direct governing pattern, practical consequence, and subject-owned construction | generic Requirement family, untyped condition, hidden command, commitment without accountable subject, or one shared suffix for unlike engineering claims |
| `admissible`, `lawful`, `legal`, `legality`, `allowed`, `permitted`, `authorized`, `valid`, `pass`, `ready`, `conformant`, `eligible`, or close admissibility-like compounds | claim-specific value, gate decision, constraint-validity result, evidence or assurance use, source-currentness relation, work-plan readiness, dated-work finalization or completion claim, measurement-result episteme, evaluation result, `C.11` `ChoiceResult` or decision record, external-rule claim, publication-use boundary, state-like value, pattern-quality result, or bounded admissible use whose bearer, source relation, value frame, non-admissible overread, reopen condition, and governing pattern are named | generic deontic permission, generic authorization, external-rule truth, gate passage, evidence strength, release decision, work completion, source authority, or conformance by label alone |
| `algorithm`, `program`, `solver`, `proof`, `recipe`, `method`, `workflow`, `process`, `procedure`, `access path`, `query plan`, `control strategy`, `method algebra`, `method graph`, `selector calculus`, or programming-paradigm labels | `U.Method` as one semantic way of doing; `MethodRelationStructure@BoundedContext` when exact method-side relations or compositions are current; `U.MethodDescription` only for one claim-bearing episteme whose exact EntityOfConcern is one admitted `U.Method` and whose claims pass the A.3.2 substantive-description threshold; a separately governed claim-bearing episteme when the EntityOfConcern is a method relation structure or another subject; `U.Signature(profile=FormalSubstrate)`; mathematical-lens or C.29 representation use; `U.Mechanism` declaration or realization; `U.WorkPlan`; one dated Work occurrence admitted under `U.Work`; method-family registry or selector outcome; evidence relation; control relation; source quote; or another direct governing pattern selected by the exact governed object, direct relation and actual participants, declaration, representation use, or claim kind | one generic method, software-only algorithm, method algebra as root object, mechanism by default, `U.MethodDescription` by procedural or document form, performed work by description, or instruction sequence by representation style |
| `input`, `raw material`, `source data`, `source material`, `output`, `result`, `outcome`, `deliverable`, `handoff`, or an action nominal or reusable work name | exact entity, exact related method, plan, work, transformation, evaluation, delivery, transfer, or receiving use, and one truthful `A.6.P.WMR` exit; `C.2.P` first for epistemic source data or source material; direct physical governor for physical raw material; `A.15.1` occurrence basis before naming performed work; `F.18` only after the governed value is recovered | universal input, output, work result, transformation result, outcome, deliverable, handoff, or production family; actual work inferred from an action nominal, WBS element, Work Package, method description, planned filling, or nearby result record |
| `transformation`, `change`, `pipeline`, `dataflow`, `flow`, `network`, `circuit`, `path`, `slice`, `workflow`, `process`, `operation`, or close change-situation labels | apply `A.3.4.P` when wording points to a situation of change; recover one exact `U.Transformation` and its exact changed referent when that claim is current; for performed-work action, recover one exact dated Work occurrence `W` admitted under `U.Work`, its covering `U.RoleAssignment` `RA`, the admitted holder system `S = actualPerformerSystem(W, RA) = RA.HolderSystemSlot` as the actual performer, canonical `performedUnderAssignment(W, RA)` under `F.6`, and the separately governed work-to-change relation required by the use; for non-work action, recover another exact direct actor-side relation; keep every influence source under its exact kind and only its exact architecture, work, communication, constraint, or candidate-synthesis relation. Then recover any separately current method, method description, mechanism, work plan, dated work, functioning or functional structure, `TransformationFlowStructure`, mathematical description, dynamics, temporal aspect, evidence, source, publication, gate, decision, assurance, declaration-local operation-result binding, measurement-result episteme, evaluation result, `C.11` `ChoiceResult` or decision record, quote-only source wording, or other direct governing pattern by value. | one source-label ontology, generic flow or network head, continuity by source label alone, graph proof, path proof, method by default, work by default, function by default, generic transformer or actor by label, architecture influence as action, universal transformation result, or transformation occurrence by wording alone |
| `holon`, `system`, `episteme`, `collection`, `level`, `boundary`, `interaction`, `functioning`, `capability`, `emergence`, `BOSC`, `MHT`, `MET`, `MFT`, `post`, `promotion`, or close multilevel-holon labels | recover the object kind and relation being claimed: system holon, episteme holon, collection relation, part-whole relation, grounding holon, boundary-crossing relation, transformation relation, functioning or capability relation, architecture relation, control relation, supervisor-subholon feedback relation, interlevel ethical conflict, mediation use, source-label repair, or quote-only source wording. Use `B.2.P` only for emergence-family, MHT-family, MET-family, MFT-family, synergy, metric-mirage, whole-reidentification, and collection wording entangled with those ambiguities; then use `A.1`, `C.2.1`, the part-whole or collection governing pattern named by value, `B.2`, `B.2.2`, `B.2.3`, `B.2.4`, `B.2.5`, `A.3.4.P`, `A.6.F`, `C.30`, `C.30.ASV`, `C.30.LCA`, `C.30.ILC`, `C.30.STRAT`, `D.2`, `D.3`, `D.4`, or the direct governing pattern named by value | generic holon hierarchy, system-only architecture, episteme-as-document collapse, false level kind, boundary-as-proof, interaction-as-part-whole, emergence as proof word, MHT, BOSC, MET, or MFT as free heuristic, generic loop-governing pattern, promotion as process travel, or `post` as an unexplained new phase |
| `culture`, `cultural evolution`, `style`, `tradition`, `genre`, `scene`, `technique`, `practice`, `platform`, `regime`, `measurement regime`, `attractor`, `developmental machinery`, or close cultural-evolution labels | Detailed trigger repair after the immediate disposition row has selected the current object: recover method family, work family, role assignment, discipline, canon or memory episteme, recognition or selection regime, mediation system or architecture, measurement or visibility relation, publication label, variant set, dynamics or mathematical-lens claim, bounded context, development-loop relation, or cultural-evolution case before use. If `practice` or `technique` is only the ordinary word for a way of doing, apply the method-like recovery row and `A.3.1` first. Apply `C.36` for cultural-evolution cases, `C.36.P` for repeated wording-use recovery, `F.17`, `F.18`, and `F.9` for term and bridge work, and the direct governing pattern for method, work, discipline, dynamics, archive, selected-set, choice, measurement, architecture, or refresh claims. | root culture or style kind by label, platform or regime as root ontology, loose attractor metaphor as dynamics claim, genre tree as proof of cultural identity, or replacing one broad source word with another broad FPF-looking word |
| `route`, `path`, `workflow`, `lifecycle`, `dispatch`, `exit`, `receiver`, `call`, `invoke`, `run`, `flow`, `EvidencePath`, or close movement and control metaphors over representations or pattern relations | `C.2.P.DR` repair, `E.18` graph path or `PathSlice`, `A.10 evidence relation or evidence-provenance relation for a claim, effect, or use`, state predicate, checklist predicate, SQL-like query, table representation, dashboard representation, publication face, source-chain relation, carrier file path, mathematical-lens use, method claim, method-description claim, work plan, dated work occurrence, or declarative FPF pattern relation under `E.8` or `F.19` | imperative program, action route, deontic-permission route, work-authorization route, release-authorization route, evidence route, pattern dispatch, or work sequence unless that governing kind is recovered by value |
| `profile`, `harness`, `catalog`, `registry`, `index`, `map` | profile with a named source-basis relation, evidence-basis relation, architecture-basis relation, or review-basis relation or use; review harness; entry index; registry record; source-ref map with a named map kind and target kind; navigation index; catalog publication; benchmark harness; publication form; companion publication; publication-companion relation; or governing record named by value | governing FPF pattern, governing source, ontology, method, or release decision unless named by value |
| `entry`, `front door`, `corridor`, `route` | navigation aid, recognition entry, navigation-bearing publication, corridor overview, or movement, control, and temporal relation | governing pattern body, fixed process sequence, release readiness, or proof that the target publication or target record is complete |
| `same`, `parity`, `identity`, `equivalence`, `mirror` | same EntityOfConcern, semantic equivalence, bridge relation, version identity, carrier mirror relation, or file mirror relation | similarity, substitutability, no-loss transform, source equality, or authority equality by wording resemblance |
| `file`, `path`, `host`, `packet`, `bundle`, `package` | carrier path, file carrying FPF pattern text, review-facing target packet, review-facing context packet, package-form decision, or transport bundle | episteme, publication form, pattern body, review result, `authoritySourceRef` target, governing FPF pattern, or authority-reference relation |
| `quality`, `characteristic`, `metric`, `indicator`, `score` | `U.Characteristic`, quality term, Q-bundle, scale, indicator, observed value, benchmark, or evaluation record | vague praise, scalar truth, success proof, or replacement for the named characteristic space |
| `slot`, `field`, `row`, `label`, `badge`, `mark` | actual participant of an obtaining direct relation; A.6.5 `SlotSpec` inside a current reusable `RelationSignature`; participant designation only inside a current assertion or relation-occurrence-description episteme; schema field, table row, or C.29 representation element with its represented object and explicit correspondence; publication label; provenance mark; status badge; or cue | kind, world-side participant, obtaining relation, evidence, authority, gate passage, or proof of currentness by position or label alone |
| `EntityOfConcern`, `EntityOfInterest`, `EoI`, `EoIClass`, `describedEntity`, `DescribedEntityRef`, `primary described entity`, or EntityOfConcern-like heads | EntityOfConcern, EntityOfConcern reference, EntityOfConcern class constraint, publication-unit primary entity of concern, source-language wording translated to the adopted EntityOfConcern family, ordinary topic or subject, or project-side kind and reference pair | universal object, second C.2.1 slot family, relation-valued bucket, free publication-unit field, authoring target, carrier, or reader interest |

##### E.10:0.2b.1 - `requirement` and `required` recovery

Treat `requirement` and `required` as trigger wording, not as a shared engineering kind or a durable suffix. Recover the exact construction before rewriting:

1. Name the bearer: the entity, relation, claim, candidate basis, result expectation, dependency position, evaluation state, or accountable subject to which the wording applies.
2. Name the claim or relation kind. Do not stop at `condition`, `item`, `value`, `record`, or another container head.
3. Name the direct governing pattern. A lexical resemblance does not transfer ownership to E.10.
4. State the practical consequence: what use becomes admissible or blocked, which value is current, what return opens, or which accountable commitment exists.
5. Write the exact subject-owned construction and rescan the replacement wording. Close with ordinary prose only when no FPF-governed construction is being asserted.

```text
RequirementWordingRecovery:
  GovernedTextSpan:
  BearerRef:
  BearerKindRef:
  ClaimOrRelationKindRef:
  DirectGoverningPatternRef:
  PracticalConsequenceDescriptionRef:
  ExactRecoveredConstructionRef:
  FinalWordingOrBlocker:
```

This is a temporary wording-restoration check, not a project record and not a `Requirement` ontology. Its positions take the exact values already governed by the subject pattern.

| Current claim behind the wording | Exact recovery and practical consequence |
| --- | --- |
| An accountable subject undertakes a duty, accepts a recommendation-as-duty, or is prohibited under an issuing or authority relation. | `A.2.8 -> U.Commitment`; the commitment changes the accountable subject's declared duty, recommendation-as-duty, or prohibition stance for the stated scope and validity window. |
| A valid grant permits a beneficiary, no prohibition is found in a current sufficiently complete frame, dated work exercises a grant, actual dated work is found not to violate any applicable prohibition in a current sufficiently complete frame, or a same-scope permission conflict is found. | `A.2.8.PER` -> the exact `GrantedPermissionRelation@Context`, `NonProhibitionFinding@Context`, `PermissionExerciseRelation@Context`, `NonViolationFinding@Context`, or `PermissionNormConflictFinding@Context`; do not route it through `U.Commitment`. |
| A subject structure, value, or use must remain inside a stated engineering boundary. | The exact constraint claim under the subject pattern; the constraint blocks or admits the named use and does not create a commitment without an accountable subject and authority relation. |
| A public pattern-use template says which candidate-basis positions must have current fillers. | E.11 `CandidatePatternUseBasisCompletenessCondition@FPFReadme`; it describes positive completeness and does not order a participant to fill a form. |
| One candidate pattern use can precede another only because the first candidate's result is its basis. | E.11.PUR precedence with `prerequisiteResult` and the prerequisite candidate's exact `PatternUseResultExpectation@Context`; no duplicate result-kind field is created. |
| One transformation-flow position depends on another. | E.18.3 `basisDependency` with its exact supporting relation; dependency is not obligation. |
| An improvement loop cannot continue until missing information positions become sufficient. | E.23 `holdUntilInformationBasisSufficient` with non-empty unfilled-position descriptions and one sufficiency condition. |
| A framework-authoring dependency is absent or not current for the next use. | E.4.DPF separates availability from relevance; only a missing dependency carries an acquisition-condition description, and only `missing + currentForNextAuthoringUse` blocks the next authoring use. |
| A candidate framework organization must cover declared relation families for a stated use. | One E.4.DPF constraint claim node with covered family ref-kind pairs, admitted-use description, and coverage-criterion description; any WorkPlan acceptance target remains separate basis. |

Name admission precedes slot verification. `CandidatePatternUseBasisRelation@Context` is admissible because the head exposes the basis relation and its two sides; `CandidatePatternUseBinding` is not repaired by kind-correct fields because `Binding` hides that subject relation. Likewise, `BoundaryConditionKindSlot` names a slot whose values classify boundary conditions; `BoundaryRoleSlot` would falsely suggest a role value. Apply F.18 only when a durable name is actually being minted.

#### E.10:0.2c - Lexical Trigger Rewrite Rules


##### E.10:0.2c.1 - EntityOfConcern, primary entity of concern, and local topic wording

Do not replace every topic-like or object-like phrase with `EntityOfConcern`.
Classify the sentence first.

| If local wording meant... | Rewrite as... |
| --- | --- |
| the EntityOfConcern named by a claim-bearing episteme or episteme-lane `U.View` | the actual `EntityOfConcern` participant under C.2.1; use `EntityOfConcernRef` or `entityOfConcernRef` only under the direct reference pattern governing that reference, and keep the episteme or `U.View` separately governed |
| the admissible class constraint on actual EntityOfConcern participants corresponding to one current episteme-constitution declaration | `EntityOfConcernClass` only where that declaration or an EntityOfConcern-preserving law is being applied |
| the primary entity of concern for one bounded `PublicationUnit` | `publicationUnitPrimaryEntityOfConcern` when the unit carries or exposes a claim-bearing episteme or episteme-lane `U.View`; otherwise the non-claim-bearing kind or reference named by value, or plain `topic` or `subject` only when no claim-bearing episteme participant, current A.6.5 declaration, or direct reference use is current |
| wording such as `describedEntity`, `DescribedEntityRef`, `primary described entity`, `EntityOfInterest`, or `EoIClass` | recover the actual `EntityOfConcern` participant under C.2.1, the publication-unit primary-EntityOfConcern use, or the local FPF kind; use `EntityOfConcernSlot` only as an A.6.5 `SlotSpec` inside a current reusable constitution `RelationSignature`; keep `entityOfConcernRef` and `EntityOfConcernRef` under their direct reference owners; and rewrite to the exact current value among those, `EntityOfConcernChangeMode`, `EntityOfConcernClass`, `publicationUnitPrimaryEntityOfConcern`, or the local FPF kind named by value. If no use can be recovered by value, keep the old wording only as quoted source or trigger wording and block reliance. |
| a review target | `review target`, review-facing target packet named by value, FPF pattern, pattern section, or file-carrier set only when the file-carrier interpretation is being made |
| a local table or paragraph topic with no claim-bearing episteme, governed participant, current declaration, or direct reference use | `topic`, `subject`, or direct noun |
| an FPF-side pattern, pattern section, accepted `DRR`, FPF publication, FPF view, document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use, or companion or projection material being improved | governing FPF pattern, pattern section, accepted `DRR`, FPF publication, FPF view, document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use, or companion or projection material |
| a project-side episteme, publication, record, carrier, or activity under work | project episteme, view, or publication named by value, `A.10` evidence relation, typed evidence record, `A.20` constraint or adjudication decision record, `A.21 GateDecision`, `A.21 DecisionLogRef`, `B.3` assurance or engineering-justification record, typed status record whose FPF status pattern is named, `A.2.8 U.Commitment`, exact `A.2.8.PER` permission result, `C.11 ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, one `A.15.1` dated Work occurrence admitted under `U.Work`, a separate episteme about that occurrence, `A.15 U.WorkPlan`, `U.Method`, `U.MethodDescription`, carrier relation, or front-end relation |

Recovery check:

```text
EntityOfConcern rewrite:
  sentence under repair:
  claim-bearing episteme or episteme-lane view used? yes or no
  EntityOfConcern participant; grounding relation; ClaimGraph; viewpoint declaration, assertion, or representation use triggered:
  PublicationUnit primary entity of concern, if any:
  review-target interpretation, process-description interpretation, source-basis-document interpretation, if any:
  source wording retained? yes or no, with reason:
  chosen replacement:
  distinction preserved:
  remaining admissible reader use:
```

##### E.10:0.2c.2 - publication-unit wording that implies authoring or interpretation work

When a phrase makes the bounded unit sound like authoring work or interpretation work, split the sentence by kind under repair.

| If local wording meant... | Rewrite as... |
| --- | --- |
| bounded human-inspected unit inside a publication | `PublicationUnit` |
| the act of writing or editing | authoring or editing Work when one dated occurrence is current; otherwise a planning cue or content inside an already admitted `U.WorkPlan` when only intended work is current. An exact episteme is `U.WorkPlan` only after A.15.2 recovers one present EntityOfConcern, one horizon, at least one `PlanItem`, and substantive coordination claims about possible future performed work. When the sentence instead concerns the authored object, use a separately identified claim-bearing episteme under its own exact kind. Any production or change relation between the Work and that episteme needs its own direct governor. The authored episteme is `U.MethodDescription` only if its exact EntityOfConcern is one admitted `U.Method` and its claims independently pass A.3.2; the writing or editing act is never the MethodDescription. |
| a pattern body or section | governing pattern body, pattern section, or `PublicationUnit` of that pattern |
| a file or rendered medium | carrier, front-end, rendering, or document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use |
| a publication form | publication form |
| a generic publication face | generic publication face, or `U.View` only when the governing pattern states that relation |
| a declared MVPK face | declared MVPK face, and `U.EpistemeView` only under MVPK constraints |
| a claim-bearing episteme or episteme species named by value | `U.Episteme`, `U.EpistemePublication`, episteme-lane `U.View` with explicit episteme tether, or episteme species named by value |

Do not make a permanent technical modifier by joining authoring, interpretation, and unit-boundary concerns.
That mix hides whether the sentence is about a publication unit, authoring work, reader inspection, or a carried claim.

##### E.10:0.2c.3 - `content`

Do not use `content` as a governing head.
Split it into:
- claim-bearing episteme content;
- publication-unit text;
- publication form;
- generic publication face;
- declared MVPK face;
- carrier data;
- payload of a record kind named by its governing pattern;
- pattern section;
- source-basis excerpt;
- review target.

Plain explanatory prose may use `content` only when the sentence does not carry ontology, authority, or admissibility.

##### E.10:0.2c.4 - `publication`

Every FPF-governed `publication` sentence names the publication construction being used:
- act or occurrence of publishing, or publishing work;
- `U.EpistemePublication`;
- publication form;
- generic publication face;
- declared MVPK face;
- `PublicationUnit`;
- carrier or rendering;
- document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use;
- external-standard publication;
- project record publication.

If the sentence says a publication "supports", "authorizes", "proves", "permits", or "makes admissible" something, split the basis: fill `relationClaimSlice` when a relation claim is being made, fill `admissibleUse` when a boundary-use claim is being made, and fill `projectSideFPFRef` when project-side records, evidence or provenance relations, gate decisions, constraint or adjudication decisions, assurance records, work, action invitations, speech acts, commitments, methods, or carriers are being used. If either side is not triggered, say so explicitly rather than filling it with generic support.

##### E.10:0.2c.5 - `surface`, `view`, `face`

Do not treat these as synonyms.

| Word | First split |
| --- | --- |
| `view` | `U.View`, `U.EpistemeView`, reader viewpoint, UI view, declared-substrate interpretive view, or review view |
| `face` | generic publication face, declared MVPK face, UI face, or public-facing companion publication |
| `surface` | Treat as trigger wording, not as an accepted Tech head. Recover one of: publication face, publication form, publication unit, carrier, rendering, UI or front-end face, physical or geometric surface, companion publication, companion or projection material, carrier relation, or another FPF object named by value. |

If the sentence can survive only because these are blurred, the sentence is not ready.

##### E.10:0.2c.6 - `source`, `target`

These are relation words, not final kinds.

Split `source` into source `U.Episteme`, source `U.EpistemePublication`, `U.View` over a source `U.Episteme`, document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use, `A.10` evidence relation, authority-reference relation, named FPF pattern cited as source, file carrier, source frame or source context only when the named relation and endpoint kind are present, the actual source-side participant of an obtaining named relation, the source-side A.6.5 `SlotSpec` only when a reusable relation declaration is current, or project-side FPF kind and reference named by value.

Split `target` into EntityOfConcern, target `U.Episteme`, review target, governing FPF pattern, project target, work target, target publication form, project-side FPF kind and reference named by value, target frame, target context, the actual target-side participant of an obtaining named relation, or the target-side A.6.5 `SlotSpec` only when a reusable relation declaration is current.

Generic `object` and `target` are not final recovered kinds. Keep them only when the sentence explicitly declares a named field or participant designation inside a current episteme, such as `ObjectKindUnderImprovement`, `ObjectVersionUnderImprovement`, or `ObjectVersionUnderQualityEvaluation`; names a `review target`; or states one direct-relation participant meaning whose actual-participant kind is supplied by value nearby. If a reusable relation declaration is current, name its A.6.5 `SlotSpec` separately. When the governed kind is known, write that kind by value: FPF pattern version, `DRR`, FPF corpus slice, publication form, `PublicationUnit`, file carrier, system carrier, exact changed referent, exact entity or value bound as the result of one particular `A.6.1` operation application, candidate proposal, evidence or provenance relation, gate decision, work plan, method description, object-under-improvement evaluation, or another named FPF kind.

Do not recover an FPF pattern, publication form, `PublicationUnit`, pattern body, or view as a `carrier`. In C.2.1+ the Tech kind is `U.PresentationCarrier`; ordinary carrier wording names a publication-side relation to the system, medium, file, rendering, front-end, or transport object that bears or renders a publication or symbol. If the text means the FPF pattern publication form, write `FPF pattern publication form`; if it means the file, rendered, front-end, or transport side, write file carrier, rendering, front-end relation, transport carrier, or another carrier relation named by value.

Common repair examples:

| Problem wording | Recovery needed |
|---|---|
| `target version` in improvement prose | `ObjectVersionUnderImprovement` or `ObjectVersionUnderQualityEvaluation`, unless `target` is quoted source wording |
| `pattern carrier` | `FPF pattern publication form` when the pattern is the publication form; file carrier or rendering only when the system-side bearer is being claimed |
| `object evaluation` when the evaluated kind is known | object-under-improvement evaluation name, such as `PatternQualityQBundle`, `DRRDecisionAdequacyEvaluationCharacteristicSpace`, `FPFPillarAdequacyEvaluationCharacteristicSpace`, or declared local evaluation |
| `thing`, `object`, `target`, `artifact`, or `material` as final head | FPF kind named by value, project-side FPF kind, or blocker |

Do not publish "source and target" if the selected relation needs the actual FPF kind.

##### E.10:0.2c.7 - `input`, `raw material`, `source data`, `source material`, `artifact`, `output`, `result`, `outcome`, `deliverable`

These are high-risk relation-dependent source-word umbrellas, not final kinds or one result family. First name the exact entity and the exact object relative to which the word is being used. For epistemic `source data` or `source material`, close the exact source expression, episteme or publication, and source-to-use relation under `C.2.P` first. Keep physical raw material with its direct physical constituent, affected-referent, resource-use, supply, transfer, or transformation governor.

When the remaining current claim is relative to a method, plan, dated work, transformation, evaluation, delivery, transfer, or receiving use, apply `A.6.P.WMR`. Recover claim subject, modality and exact temporal extent, polarity, and recovery/support state independently. Closure is exactly one of four truthful families: an exact direct subject-relation claim, positive or governed negative; an exact `A.6.1` operation-application binding; an exact local `A.15.PROD` or `A.6.RCD` claim; or an exact non-assertability result whose reason is independently `factually unsupported`, `missing-information`, or `missing-governor`. A failed known predicate and an unavailable fact keep their known governor and name no future owner; only a genuinely absent predicate/condition/owner names the affected receiving use and future owner. Classification, a generic `result relation`, a method-description field, planned filling, a designation that merely type-checks against an A.6.5 `SlotSpec`, or a polarity inference is not closure.

Before opening that branch, test whether the phrase already names an independently governed `U.Episteme`; `U.View` or `U.EpistemeView`; publication form; publication face, including a declared MVPK face; `PublicationUnit`; carrier, front-end, or rendering relation; project-side FPF kind and reference named by value; evidence carrier or evidence relation; document under a named source-basis, evidence-basis, architecture-basis, or review-basis relation or use; review target; `C.11` `ChoiceResult`; measurement-result episteme; evaluation result; diagnostic finding; decision; or another project object whose record kind and direct governor are named by value. Retain ordinary `input`, `output`, `result`, `outcome`, or `deliverable` only while the exact direct governor remains recoverable. If no governor closes the selected WMR claim, return the bounded blocker. If the missing item is instead a non-WMR kind, retain an architecture-first candidate disposition under its direct owner. Do not invent either one inside pattern prose or replace it with a universal kind or relation.

##### E.10:0.2c.8 - `record`

Use `record` only when the governing FPF pattern or project practice names the record kind and relation. The nearby wording says which FPF kind the record instantiates or records, for example:

- `A.10` evidence or provenance relation or evidence record for a named claim;
- `A.21` `GateDecision` or `DecisionLogRef`;
- `A.20` constraint or adjudication decision record;
- `C.11` `ChoiceResult` or decision record;
- `A.15` `U.WorkPlan`, one `A.15.1` dated Work occurrence admitted under `U.Work`, or a separately identified claim-bearing episteme about that occurrence; use a record-kind name only when its exact kind and direct record governor are recoverable;
- `A.2.8 U.Commitment`, exact `A.2.8.PER` permission result, or `A.2.9 SpeechAct` publication;
- a separately identified assignment-assertion or occurrence-description episteme that designates one exact `RA : U.RoleAssignment`, or a status-register entry under its named governing pattern; neither record is the world-side assignment occurrence;
- `E.19` review run record or another named review record whose review target and review relation are explicit;
- process run record in process documents.

Do not let `record` mean "any file that remembers something", "the missing source", or "the thing to create when support is absent". If a named support relation cannot be asserted because a required actual participant or governed value is absent, name that exact missing participant or value. If a reusable declaration is incomplete, name its missing `SlotSpec` or other missing declaration content and repair that declaration. If a receiving assertion or relation-occurrence-description episteme lacks a participant designation, name the missing designation under that episteme. If a `U.WorkPlan` lacks a planned participant designation or planned value, name that missing plan content under the WorkPlan. Create a prospective repair request, future decision request, prospective work-plan entry, or explicit missing-source-relation note as applicable; none backdates support, establishes actual participation, or makes the direct relation obtain.

##### E.10:0.2c.9 - `model`, `diagram`, `screen`, `dashboard`, `table`, `note`, `memo`, `summary`, `explanation`

These are recognition examples, not governing kinds.
Classify each occurrence as one of:
- episteme or episteme publication;
- `U.View`, `U.EpistemeView`;
- publication form;
- generic publication face;
- declared MVPK face;
- `PublicationUnit`;
- carrier, front-end, or rendering;
- project-side FPF kind and reference named by value;
- explanation and source-finding relation under `E.17.EFP`;
- evidence, currentness, and provenance relation under `A.10`;
- gate-bearing claim or effect under `A.20` or `A.21`;
- assurance and engineering-justification record under `B.3`;
- work and reliance encountered-item repair relation under `A.15.4`.

Keep the ordinary example word only after the governing kind is visible nearby.

##### E.10:0.2c.10 - `reader`, `reviewer`, `author`, `operator`

Do not use people-position words as hidden kind names.

Use:
- `working reader` or `intended practitioner` for ordinary usability;
- `engineer-manager` when the FPF use case is the engineer-manager applying the pattern in work;
- `reviewer` only for a participant in a named review relation; use review process, review gate, or review target for the process, gate, or object;
- `author` only for authoring or editing work;
- `operator` only for an actual `U.Role`, operator position or process operator in the selected context.

If a text says "reader-facing" or "review-facing", it also names what is facing that person: generic publication face, declared MVPK face, packet, document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use, `PublicationUnit`, carrier, or UI or front-end.

##### E.10:0.2c.11 - `owner`, `home`, `host`, `locus`

These are not interchangeable.

`owner` may be kept as architecture-discussion shorthand only when the kind under repair is an explicit responsibility assignment or stewardship assignment. It is not an admissible substitute for `pattern`, `DRR`, `U.Episteme`, `U.EpistemePublication`, publication unit, file carrier, or project record.

Split into:
- governing FPF pattern relation or authority-reference relation;
- named governing source set;
- explicit source-maintenance role assignment;
- file carrying FPF pattern text;
- file carrier;
- publication unit;
- process-control role assignment;
- role assignment;
- evidence record or evidence source;
- governing FPF pattern or project target;
- support root.

Never use `owner` to avoid deciding whether the sentence is about a governing FPF pattern, authority-reference relation, file carrier, responsibility assignment, or process control.

##### E.10:0.2c.12 - `route`, `branch`, `handoff`, `path`, `trajectory`, `move`, `flow`

Recover the movement, control, and temporal relation set before using these words:
- `E.10.MOVE` for project-move, first-move, working-move, next-move, pattern-use, work-entry-readiness, architecture-candidate-use, call-planning next-action, or other move-like wording whose direct FPF target is hidden;
- `A.16` local move;
- `A.16.0` trajectory account;
- `A.19`, `C.2.2a` position in characteristic space or state space;
- `B.2.5` control relation, control-layer relation;
- process handoff;
- selector relation or selection mechanism;
- work transfer;
- `E.18` graph path or `PathSlice` expression;
- `A.6.3`, `A.6.4` episteme morphism or retargeting.

When `handoff` instead names an entity, package, result, delivery, transfer, acceptance, or receiving-use boundary, apply `A.6.P.WMR` to that exact relation-bearing claim. Use `E.10.MOVE` for a process-baton or project-move case only when that movement itself is current; a handoff record or package remains an episteme or governed entity, not the transfer.

If no movement, control, and temporal relation is being made, keep the word ordinary and non-authorizing.

##### E.10:0.2c.13 - `use`, `supported use`, `action`, `effect`

Split the word before accepting it:
- applying an FPF pattern to a problem situation;
- interpreting or using a publication, view, record, cue, or carrier;
- relying on a named project episteme, a named source-basis document, or a project-side FPF kind and reference named by value for a named claim or effect;
- admissible act, work, or claim under a named FPF pattern; an obtaining direct relation recovered through `A.6.P` with its actual participants named; a literal or source-local relation phrase retained only as wording; or a project-side FPF kind and reference named by value;
- non-admissible act, work, or claim requiring one other named value: FPF pattern; an `A.6.P`-recovered direct relation with its actual participants; a literal or source-local relation phrase identified only as wording; project-side FPF kind and reference named by value; `C.11` `ChoiceResult`; `C.11` decision record; `A.6.A` action invitation; `A.15` `U.WorkPlan`; one `A.15.1` dated Work occurrence admitted under `U.Work` or a separate episteme about it; `U.Method`; `U.MethodDescription`; `A.20` constraint or adjudication decision record; `A.21` `GateDecision`; `A.21` `DecisionLogRef`; `A.10` evidence relation; typed evidence record; `B.3` assurance or engineering-justification record; typed status record whose FPF status pattern is named; carrier relation; or front-end relation;
- planned work;
- an actual Work occurrence admitted under `U.Work`, kept distinct from any assertion or record about it;
- evidence of interpretation or effect;
- gate or admission decision.

Do not let `supported use` become a generic capability of a document.
The FPF-governed wording names the `admissibleUse` target named by value and non-admissible stronger or adjacent use, `relationClaimSlice` when a relation claim is being made, and `projectSideFPFRef` when a project-side FPF kind and reference named by value is being used.
If the sentence says "supported", conforming wording names the `admissibleUse` target named by value and non-admissible stronger or adjacent use, `relationClaimSlice` when a relation claim is being made, and `projectSideFPFRef` when a project-side FPF kind and reference named by value is being used. Do not satisfy the rule by naming only a project record, evidence record, gate record, assurance record, engineering-justification record, only an FPF pattern, or one mixed project-side entry when several `A.7` or `A.15` role, method, work-plan, and actual-work kinds are being used.

##### E.10:0.2c.14 - `sign`, `concept`, `denotat`, and school-semiotic labels

Do not import the school-semiotic triad as architecture ontology.
When a source or review text says `sign`, `signifier`, `signified`, `concept`, `denotat`, `representamen`, `interpretant`, or `sign vehicle`, apply the composite recovery order before the term appears in FPF-facing prose.

Possible recoveries include:
- `U.Episteme` or episteme species named by value;
- selected `EntityOfConcern`, grounding, reference-plane relation;
- `U.View`, `U.EpistemeView`;
- publication form, generic publication face, declared MVPK face, or `PublicationUnit`;
- carrier, front-end, or rendering;
- cue, displayed wording, mark, status display, credential display, provenance mark, signature evidence;
- evidence record, gate record, work-state record, commitment record, role-assignment record, or another project-side FPF kind and reference named by value;
- FPF pattern, pattern section, accepted `DRR`, FPF publication, or FPF view when the object is on the FPF side.

Use `concept` only where current `FPF` already has the relevant concept-set, UTS, local-meaning, or Part F machinery available.
Otherwise recover the claim-bearing episteme; the obtaining direct relation and actual participants; the current A.6.5 declaration, participant designation, or C.29 representation and explicit correspondence when one of those is actually present; or the record kind and governor named by value.

##### E.10:0.2c.15 - `pattern`, generic FPF-side object wording, `locus`, `row`, `target`

`Pattern` is not a free synonym for regularity.
If the intended object is an FPF pattern, write `FPF pattern` or name the governing pattern.
If it is not an FPF pattern, do not write `recovered FPF construction` as the final value. Choose one recovered value by sentence function: episteme, view, publication, publication form, generic publication face, declared MVPK face, `PublicationUnit`, carrier relation, front-end relation, project-side FPF kind and reference named by value, document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use, review target, obtaining direct relation and actual participants, receiver-needed relation occurrence, reusable `RelationSignature` and A.6.5 `SlotSpec` values, claim-bearing episteme with any current participant designations, C.29 representation element and explicit correspondence, `C.11` `ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, `A.15` `U.WorkPlan`, one `A.15.1` dated Work occurrence admitted under `U.Work` or a separate episteme about it, `U.Method`, `U.MethodDescription`, `A.20` constraint or adjudication decision record, `A.21` `GateDecision`, `A.21` `DecisionLogRef`, `A.10` evidence relation, typed evidence record, `B.3` assurance or engineering-justification record, or typed status record whose FPF status pattern is named.

Avoid generic FPF-side object wording, generic named-target wording, `locus`, `row`, and `host` when they hide kind.
Use them only when the kind is literally a table row, document with named source-basis relation or use, file carrying FPF pattern text, or review target and the sentence does not need a narrower FPF kind.
For FPF-facing wording that carries a claim being made, direct relation, admissible use, or remaining reader use, these are candidate recoveries, not a group kind: governing FPF pattern, pattern section, accepted `DRR`, FPF publication, FPF view, record kind named by its governor, obtaining direct relation and actual participants, receiver-needed relation occurrence, claim-bearing episteme, reusable A.6.5 declaration, or C.29 representation and explicit correspondence. Choose one by sentence function and keep separately governed objects separate.

##### E.10:0.2c.16 - Union-field unpacking under A.6.P

Do not write `authority-bearing FPF pattern`, `authority-bearing FPF row`, `FPF row named by value`, `selected FPF pattern, record, or relation`, `governing FPF relation`, or `required project record or action` as final fields.

When one of these union-fields appears, make the A.6.P choice explicit:
- if the sentence is making a relation claim, recover the `RelationKind`, actual participants, qualifiers, scope, time, viewpoint, and admissibility target, then state the obtaining direct relation and those participants; distinguish one relation occurrence only for a named receiving use; add a reusable `RelationSignature` and A.6.5 `SlotSpec` values only when declaration is current; and keep any claim-bearing row or field as an assertion episteme, participant designation, or C.29 representation and explicit correspondence under its own owner rather than as the relation itself;
- if the sentence is not making one relation claim, unpack the context under repair into FPF-side kind, reference, or relation named by value and one project-side FPF kind with its reference, or state that no project-side FPF kind is triggered;
- if the same unpacking recurs across cases with one stable recovery shape, record a light A.6.P specialization candidate rather than minting a vocabulary-wide replacement field.

Apply this unpacking whenever a publication, display, cue, explanation, dashboard tile, schema, signature, badge, or generated output is being read as evidence, gate passage, work, deontic permission, work authorization, approval speech act, commitment, release authorization, safety assurance, evidence sufficiency, or engineering justification.

Do not fill one authoring union-field position with whichever nearby FPF kind is easiest to name. A project publication, claim-bearing episteme, or record of a kind named by its governor is a description-side object; one `A.15.1` dated Work occurrence admitted under `U.Work` is a world-side individual, while `A.6.A` action invitation, `A.2.9` `SpeechActRef`, `A.2.8` `U.Commitment`, `U.Method`, and `U.MethodDescription` belong to other kinds or relations.

##### E.10:0.2c.17 - Heterogeneous kind lists

Do not repair a heterogeneous list by giving it one broader umbrella name.
When a sentence lists unlike candidates such as pattern, `DRR`, publication, `U.View`, carrier relation, front-end relation, project-side FPF kind and reference named by value, `C.11` `ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, `A.15` `U.WorkPlan`, one `A.15.1` dated Work occurrence admitted under `U.Work`, a separate claim-bearing episteme asserting a fact about that Work occurrence, `U.Method`, `U.MethodDescription`, `A.20` constraint or adjudication decision record, `A.21` `GateDecision`, `A.21` `DecisionLogRef`, `A.10` evidence relation, typed evidence record, `B.3` assurance or engineering-justification record, or typed status record whose FPF status pattern is named, do not promote the row to a new kind. Classify the list as one of:
- one kind under repair selected at bounded complete generality;
- several obtaining direct relations with actual participants;
- a reusable relation-declaration set with exact `RelationSignature` and A.6.5 `SlotSpec` values;
- a C.29 tuple representation with explicit represented objects and correspondences;
- several alternative cases;
- an indicator of failed ontology.

If the list asserts several direct relations, name each obtaining relation and its actual participants. If it declares reusable relation shapes, name each `RelationSignature` and A.6.5 `SlotSpec` value and do not infer that any relation obtains.
If it is a C.29 tuple representation, name the representation elements, represented objects, and explicit correspondences; if the same material is also a reusable relation declaration, name its `RelationSignature` and A.6.5 `SlotSpec` values separately.
If it is an alternative-case set, split the cases.
If it is failed ontology, return to architecture before pattern or `DRR` prose depends on the list.

##### E.10:0.2c.18 - `strong`, `stronger`, `weak`, `weaker`, `support`

Do not use strength metaphors unless a named FPF scale, evidence class, threshold, or characteristic space is being used.

Preferred rewrites:
- `stronger claim` -> wider claim scope, higher evidence-basis threshold, gate or admission threshold, claim requiring world-contact evidence or authority relation, authority claim, or named evidence-support class;
- `weaker claim` -> narrower claim scope, lower evidence-support class, bounded admissible act, work, or claim, `source-loss mode` under `A.6.3.CSC` when a source-to-rendering loss is being claimed, coarsened rendering, or explicit abstain or reopen condition;
- `support` -> keep ordinary or quoted source wording when no FPF claim relies on it. Otherwise recover the claim before replacing the word; do not coin a generic `SupportRelation`. If the reading is base, anchor, or basedness, apply `A.6.6` and state `dependent`, `base`, `baseRelation`, `scope`, applicable `Γ_time`, witnesses, `admissibleUse`, and `nonAdmissibleUse`.

For FPF-governed `support`, test the direct-subject branch before consulting the common alternatives. Ask whether the sentence states a recognizable fact between subject-domain things rather than evidence, assurance, admissibility, work help, or reader help. If it does, name the things and say plainly what relation obtains between them; these are the actual participants and direct predicate. Go to the pattern that governs that relation. If the relation or a participant remains unclear, use `A.6.P` to recover it. Once the participants and needed predicate are clear, use `A.6.RCD` only when no current pattern governs that predicate.

When the sentence is not already a recognizable direct subject relation, the following are common alternatives, not a complete list:
- source-description relation: a source episteme, publication, view, model, graph, trace, generated representation, or document describes, exposes, renders, cites, or makes inspectable one claim-bearing item;
- EntityOfConcern or grounding-holon grounding: the claim-bearing episteme, view, representation, or pattern application is grounded in its actual EntityOfConcern participant, actual grounding holon, local world contact, or observation setting; `EntityOfConcernSlot` and `GroundingHolonSlot` remain A.6.5 `SlotSpec` values only inside a current reusable declaration and do not constitute those participants;
- base, anchor, or basedness relation: the phrase means relative-to, based-on, anchored-in, base change, or scoped grounding as a base relation; use `A.6.6` support wording selection and rewrite as `baseRelation(dependent, base)` or SWBD, not as a generic `SupportBasis`, `SupportRelation`, or `SupportRecord`;
- evidence or witness support: an evidence-use relation, evidence-provenance relation, witness relation, witness carrier, observation, test, observation record, or test record bears on a claim;
- assurance or engineering-justification support: an assurance argument, trust calculus, safety case, or engineering-justification claim is being made;
- causal-use relation or evidence relation: a causal-use question, rung, estimand, `CausalEvidenceSupportBasis`, `CausalUseSupportVerdict`, supported use, and unsupported use are being claimed;
- mathematical-lens use or lens-use admissibility: a mathematical lens, mapping, similarity, or formal object makes a bounded claim admissible or exposes preserved structure and lost structure;
- characteristic, measurement, threshold, or comparison basis: a characteristic, metric, scale, benchmark, threshold, or comparison basis is being used;
- admissible-use or boundary-use basis: the sentence says what use, act, claim, publication use, or reliance is admissible;
- work, enablement, prerequisite, resource, or operational help: one thing helps, prepares, routes, resources, enables, or makes work easier without evidence, authority, truth, or admissibility claim;
- publication companion, entry, navigation, or reader help: a file, section, index, map, review packet, support document, or companion helps readers find, inspect, compare, or review another item.

Write the concrete sentence before choosing an owner. `Test T supports claim C` becomes `Test T is evidence for claim C` and goes to `A.10`. `Index I supports readers` can become `Index I helps readers find section S` and remains bounded reader help; it does not establish the truth of section S. `Column C supports roof R` remains a structural claim: state the structural relation it asserts, for example that C bears R's load, and use that relation's current owner. If its relation or a participant is unclear, use `A.6.P`; if both are clear but no current pattern owns the predicate, use `A.6.RCD` and return the missing-governor result.

For a common alternative, go straight to its owner once the sentence names the things involved, what one does for the other, the permitted use, and the blocked stronger conclusion. Use `C.2.P` and the direct description, source-use, grounding, or publication pattern; `A.6.6` for basedness; `A.10` for evidence; `B.3` for assurance; `C.28` for causal use; `C.29` for mathematical-lens use; `C.16` for characteristic, measurement, threshold, or comparison construction; or the pattern for the stated admissible use, work, resource, publication companion, or reader help. Do not send one of these common lexical choices to `A.6.P` to choose again.

Support-headed names such as `SupportRecord`, `SupportSource`, `SupportLine`, `SupportForm`, a support phrase that hides a state-family claim, `SupportSection`, `SupportMaterial`, `support basis`, `support relation`, `support view`, and `supported use` are diagnostic triggers. They are conformant only when rewritten to an exact governed object under its direct owner: a claim-bearing episteme or record kind named by value; an A.6.5 `SlotSpec` only when a reusable declaration is current; a publication function; a state-family value under `A.19.SPR` only when that claim is current; an obtaining direct relation and actual participants; an admissible-use boundary; or, for the A.19 case, `DeclaredSubstrateInterpretiveView` under `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW`. If the phrase is base-dependence, A.6.6 is the governing pattern and conforming text exposes `dependent`, `base`, `baseRelation`, `scope`, applicable `Γ_time`, witnesses, `admissibleUse`, and `nonAdmissibleUse`. Otherwise rewrite the head to the selected interpretation: source-description relation, EntityOfConcern grounding, grounding-holon relation, evidence-provenance relation, source-use relation, source-currentness claim, source adoption decision, source adaptation decision, source rejection decision, obtaining direct relation and actual participants, admissible-use boundary, assurance claim, C.28 causal-use relation or causal-use verdict, C.29 lens-use output, C.16 characteristic construction, measure relation, comparability relation, bridge card, comparison card, work enablement relation, publication companion, or ordinary reader help.

A support-headed phrase selected by an accepted `DRR`, pattern authoring draft, table heading, schema field, coordinate name, or selected reusable authoring vocabulary is already durable enough to trigger `F.18` unless the text explicitly marks it as source-only, quote-only, or rejected. Do not accept `subject to F.18 later` as `E.10` closure when the phrase is already being used to guide authoring, review, landing, or reusable FPF wording. Either complete the naming decision now, replace the head with the selected interpretation named by value, or leave the naming issue blocking by value.

If no FPF claim relies on `support`, keep the ordinary or quoted wording and do not invent an ontology for it. Otherwise the reader must be able to say what supports what, in what sense, for which use, and what must not be inferred. Keep a recognizable direct subject relation in its domain and choose a common lexical alternative here in `E.10:0.2`. Use `A.6.3.CSC` for a source-loss mode and `C.2.P` for the source expression and its use. Use `A.6.P` only when the direct predicate or a participant remains unclear; once both are clear, use `A.6.RCD` only when no current pattern governs that predicate.

##### E.10:0.2c.19 - Applying patterns versus procedural calls

FPF patterns are applied in problem situations.
When another FPF pattern governs the claim, the text names the FPF pattern application and the ontology, conformance claim, or conformance section named by value being applied. The pattern-governed relation is declarative: the text states which pattern applies and which exact governed object, claim-bearing episteme, obtaining direct relation and actual participants, current declaration, or representation use it governs.

Use `apply pattern`, `use the pattern guidance`, `the pattern governs this problem situation`, or `the case falls under this pattern` when the FPF-side pattern application is being made.
Do not use `project action` as a final class. For project-side activity, choose exactly one kind or relation under repair for the sentence: `U.Method`; `U.MethodDescription`; `U.Mechanism`; `A.15` `U.WorkPlan`; one `A.15.1` dated Work occurrence admitted under `U.Work`; a separate claim-bearing episteme asserting a fact about that Work occurrence; exact entity plus a direct relation involving that occurrence recovered through `A.6.P.WMR`; exact `A.6.1` operation-application binding; local `A.15.PROD` claim; measurement-result episteme; evaluation or diagnostic finding; `C.11` `ChoiceResult`; `C.11` decision record; `A.6.A` action invitation; `A.20` constraint or adjudication decision record; `A.21` `GateDecision`; `A.21` `DecisionLogRef`; `A.10` evidence relation; typed evidence record; `B.3` assurance or engineering-justification record; typed status record whose FPF status pattern is named; carrier relation; front-end relation; or another accepted project-side FPF kind.
Use `route`, `path`, `branch`, `handoff`, `trajectory`, `move`, or `flow` only after the movement, control, and temporal relation set has named the FPF kind under repair.

##### E.10:0.2c.20 - FPF-side and project-side episteme and publication contexts

Semioarchitecture often talks about two different described contexts:
- FPF-side episteme and publication context: `FPF` as episteme, FPF patterns, pattern sections, `DRR`s, FPF publications, FPF views, support documents and documents with named source-basis, evidence-basis, architecture-basis, or review-basis relations or uses, and review targets;
- project-side episteme and publication context: the engineer-manager's project epistemes, publications, views, records, carriers, cues, evidence records, `A.20` constraint or adjudication decision records, `A.21` gate decisions, `A.21` decision-log refs, `B.3` assurance or engineering-justification records, commitments, one `A.15.1` dated Work occurrence admitted under `U.Work` plus any separate episteme about it, `C.11` `ChoiceResult` values, `C.11` decision records, and `A.6.A` action invitations.

Do not blur them with `source`, `artifact`, `object`, `material`, `target`, `pattern`, or broad `semiosis`.
If both contexts are being used, split the sentence into `relationClaimSlice` when a relation claim is being made, `admissibleUse` when a boundary-use claim is being made, and `projectSideFPFRef` when a project-side FPF kind and reference named by value is being used.
If one context is not being used, state `not triggered` rather than leaving a placeholder.

##### E.10:0.2c.21 - `decision`, `action`, `work`, `method`, `plan`

Do not let `action` cover every project-side event. An action nominal such as `testing`, `assembly`, `maintenance`, `evaluation`, or `inspection` is a morphology cue, not a governed kind. Placement in function- or flow-structure prose identifies no `U.Function`: apply `A.6.F` when the function-like use remains claim-bearing and its exact FPF object or relation is hidden; otherwise name the already recovered method, method description, required-transformation or required-effect claim, actual `U.Transformation`, `TransformationFlowStructure` locus, functional-view record, plan content, exact Work occurrence, or other governed value under its direct pattern. A WBS element, activity, or Work Package remains plan- or assignment-episteme content about intended work; none of these uses identifies an actual Work occurrence admitted under `U.Work`.

Split decision-making and decision records under `C.11`; role, method, work-plan, and actual-work alignment under `A.15`; planned work under `A.15.2`; exact dated Work occurrences under `A.15.1`; actual launch or performed values under independently obtaining direct relations or A.6.1 bindings; separate performed-work, finalization, result, telemetry, and gate records under their direct record or gate patterns; action invitation under `A.6.A`; communicative acts under `A.2.9`; commitments under `A.2.8`; and strong grants under `A.2.8.PER`. A method-description field, planned filling, compatible type, ticket, or nearby result record establishes no actual participant relation.

A reusable name for exact performed work goes to `F.18` only after the occurrence is grounded under `A.15.1`: each actual performer is an admitted `U.System`; each exact obtaining covering `RA : U.RoleAssignment` has that System as holder; any explicit attribution uses `performedUnderAssignment(W, RA)` under `F.6`; and actual `enactsMethod`, temporal extent, containing system, affected referent, direct bindings, and resource-use facts remain separately recoverable. Add the applicable continuity policy only when occurrence identity is material. Keep separately current direct subject or resource-use claims, `A.15.PROD` production claims, measurement-result epistemes, evaluation results, `C.11` choices or decisions, delivery occurrences, acceptance verdicts, and downstream-effect claims under their own governors.

P2W language from `E.18` transformation-flow structure is not a generic `source-to-work` slogan. Use it only when the chain from principles, theories, and signatures through method choice, work planning, work execution, separately governed measurement or evaluation, and cycle return is actually being made.

##### E.10:0.2c.22 - Whole-corpus trigger use

When a whole-corpus cleanup is selected, use this pattern's trigger guide over claim-bearing FPF text and project text that deliberately uses FPF-governed terms, pattern references, relation names, or conformance claims.

Do not do a global string replacement. Classify each unclear term occurrence by the bounded complete rewrite mode and preserve accepted FPF names unless a separate accepted naming decision changes them.

##### E.10:0.2c.23 - `case`, `scenario`, `example`, `pilot`, `anti-case`

These words are useful for recognition and testing, but they often hide whether the text is talking about a project situation, evidence, a worked slice, a negative control, or a decision basis.

Split before use:
- working problem situation;
- worked case or example;
- pilot case;
- anti-case, negative control;
- evidence case;
- comparison case;
- source example;
- benchmark case;
- candidate corpus example.

A case can illustrate or test a pattern.
It does not by itself become evidence, a pattern, a `DRR`, a source basis, or an authority-reference relation.
If the case is being used to justify a claim-bearing text change, choose and name each EntityOfConcern under repair or relation separately: evidence record or evidence-provenance relation, decision basis or decision record, authority relation, relation to a governing FPF pattern, or relation to an accepted `DRR`.

##### E.10:0.2c.24 - `basis`, `context`, `scope`, `frame`

These are boundary, context, relation, and scope words.
They are not admitted as final kinds.

Split:
- source basis;
- decision basis;
- evidence basis;
- comparison basis;
- threshold basis;
- grounding basis;
- admissibility basis;
- review context packet;
- bounded context;
- claim scope;
- viewpoint frame or reference frame.

If a basis changes what may be done, fill `admissibleUse`; fill `relationClaimSlice` only when a relation claim is being made, and fill `projectSideFPFRef` when a project-side FPF kind and reference named by value is being used.
If context changes the EntityOfConcern, apply the `EntityOfConcern`, grounding, and reference-plane checks before any bridge, parity, or identity claim.

##### E.10:0.2c.24a - translation and multilingual heads

A translated term is not automatically the same FPF head. A translation may preserve reader access while losing kind precision, admissible use, source-use boundary, or source-description relation. A bilingual alias is not a Bridge by itself and does not create equivalence, substitution, UTS admission, or cross-context naming relation.

When translated wording has FPF-governed use, recover the FPF kind named by value, local head, publication construction, source relation, and admissible use before accepting the translation. A translated explanation is a derivative rendering; operative claims need claim-bound source relations and `E.17.EFP` or `A.10` when reliance use is being made. A translated `PublicationUnit` may preserve form while shifting `publicationUnitPrimaryEntityOfConcern` or carried publication move; apply `E.17.AUD` or `E.17.AUD.OOTD` when that shift is being claimed. Local translated heads may use `E.17.AUD.LHR` or `C.2.P` without full `F.18` unless durable cross-context naming, UTS row, Core-facing term, or reusable FPF head is intended.

##### E.10:0.2c.25 - `state`, `status`, `posture`, `readiness`

Do not let state-family wording become a maturity adjective, evidence claim, assurance result, gate passage, deontic permission, release authorization, source authority, work completion, or process state by appearance.

When a state-family word has FPF-governed use, apply `A.19.SPR` unless the governing pattern and local state-like field are already recoverable by value.

Minimum closure:

```text
State-family wording:
  triggerSpan:
  bearerRef:
  stateFrameOrGoverningPatternRef:
  stateValueOrClassification:
  criteriaOrEvidenceRef?:
  admissibleUse:
  nonAdmissibleOverread:
  validityWindowOrReopenCondition?:
  finalWordingOrBlocker:
```

Typical governing patterns:

| If the wording means... | Use... |
| --- | --- |
| position in a declared `CharacteristicSpace` | `A.19`, with `C.16.P` first if characteristic, scale, coordinate, score, or threshold construction is hidden |
| reusable state-transition or dynamics law | `A.3.3` |
| language-state position for an episteme, publication, or wording-use object | `C.2.P` where source-publication recovery is needed, then `C.2.2a` and `A.16.*` |
| source wording, source relation, source currentness, source publication, or source-bearing use disposition | `C.2.P`, `E.17`, `E.9.DA`, or the source-related field named by value |
| evidence-provenance relation, evidence relation, or reliance disposition | `A.10` |
| assurance result, assurance claim, or assurance input | `B.3` |
| local CV, constraint, adjudication, gate, or release readiness | `A.20`, `A.21`, or the release pattern governing the claim or gate pattern |
| temporal claim status or temporal-use classification | `C.27`, retaining `dynClaimPosture` only as a declared C.27 field |
| mathematical-lens use admissibility | `C.29`, retaining `LensUseAdmissibilityValue` only as a declared C.29 field |
| `DRR` decision-adequacy result or source-relation classification | `E.9.DA` |
| pattern-quality result or quality-evaluation status | `E.21`; `E.19` remains review and admission profile |
| landing, monolith, review, queue, handoff, transport, or current campaign state | the process file or release carrier named by value, not user-facing pattern prose unless that state is the pattern's own object |

A retained `...Posture`, `...Status`, `...Readiness`, or `...State` field is complete only when it declares field name, bearer kind, governing pattern, value set or classification source, admissible use, non-admissible overread, and reopen or change condition when applicable. If those are missing, rewrite to the exact governing-pattern claim or record kind named by value, mark quote-only or reduced-use, or leave the rewrite blocked.

Do not replace `support` with a support phrase that hides a state-family claim, a source-use bucket, a basis-headed bucket, or another state-family substitute. First decide whether the sentence states a direct subject relation; if it does, name its participants and predicate and use its owner. Otherwise apply the common base-relation, source-use, evidence, assurance, lens-use, characteristic, admissible-use, work-help, or reader-help interpretation that actually carries the claim.

##### E.10:0.2c.25a - `live`, `current`, `active`, and status or article overwrap

`live`, `current`, `active`, `open`, `pending`, and similar status-like modifiers are trigger wording when they attach to `pattern`, `record`, `object`, `field`, `operation`, `route`, `locus`, `move`, `text`, `claim`, `question`, `use`, or `relation` without saying which exact bearer and state or currentness value, temporal qualifier of an obtaining direct relation or assertion, source or use relation, or claim function the modifier adds.

First recover whether the modifier expresses a real FPF value:

- If it means source currentness, state, status, readiness, publication-use disposition, quality result, admission state, campaign state, or process state, apply `A.19.SPR`, `C.2.P`, `E.9.DA`, `E.21`, `E.19`, the release or process carrier named by value, or the governing pattern for that value.
- If it means a claim, question, use, or relation is currently asserted, relied on, or action-bearing in the described situation, keep the modifier only when the sentence also names the exact claim or claim-bearing episteme, obtaining direct relation and actual participants or source/use relation, admissible use, and direct governing pattern, or says why ordinary prose is enough.
- If it only points to "the thing under discussion", treat it as phrase-level apparatus and apply `F.19`: write `the pattern`, `pattern of concern`, record kind named by value, affected field, operation claim, relation claim, or other object named by value instead of `live X`.
- If it is development, review, projection, landing, or current-campaign state about an FPF pattern version, keep it in the process, quality, projection, release, or campaign carrier rather than in the pattern unless that state is the pattern's own primary `EntityOfConcern`.

Do not close this row by deleting `live` or replacing it with `current`, `active`, `at issue`, or another status word. Closure is a `KindRestorationCheck`: the modifier is ordinary prose; a state or currentness value under its direct owner; a temporal qualifier of an exact direct relation or assertion; a retained claim, use, or relation marker with named admissible use; an `F.19` apparatus removal; or a blocker.

##### E.10:0.2c.26 - `claim`, `evidence`, `witness`, `ground`, `proof`

`Claim` is not a synonym for sentence or prose.
`Evidence` is not a synonym for source, proof, approval, or confidence.

For `claim`, recover:
- claim-bearing episteme;
- claim node, claim content;
- EntityOfConcern or claim referent;
- viewpoint and representation scheme when needed for the claim;
- admissibility target when the claim is used.

For evidence-like words, recover:
- evidence record or evidence-provenance relation;
- witness or source pin;
- grounding relation;
- validation result;
- assurance argument component;
- provenance mark only as provenance, not as evidence by itself.

If evidence is being read as engineering justification, gate passage, deontic permission, work authorization, safety assurance, evidence sufficiency, release authorization, or release confidence, apply the governing FPF pattern or use the project-side FPF kind and reference named by value instead of strengthening the evidence word.

##### E.10:0.2c.27 - `authority`, `permission`, `approval`, `commitment`, `obligation`

These are deontic claims or claims carrying an authority-reference relation, not visual or rhetorical properties.

Recover:
- role assignment or exact permission-beneficiary ref;
- speech act or issuing act;
- commitment record under `A.2.8` for obligation, recommendation-as-duty, or prohibition;
- exact `A.2.8.PER` strong grant, weak non-prohibition/non-violation finding, exercise relation, or permission-conflict finding;
- policy claim and policy/currentness frame;
- authority relation;
- entry predicate or gate record or decision record when that is the actual claim;
- authority-changing decision;
- wording such as `delegated permission`: recover the exact `A.2.9` granting or delegating speech-act occurrence and, only when the named current policy validly institutes one, the resulting current `A.2.8.PER GrantedPermissionRelation@Context`; retain the exact grantor assignment, beneficiary ref or role assignment, policy and currentness basis, scope and window, and any separately governed on-behalf-of or work relation. The cue mints neither `DelegatedPermissionRelation` nor another generic delegation or authorization kind; if the actual direct owner cannot be recovered, block operative use of the wording rather than name an ownerless relation;
- contestability, revocation, scope, window, and expiry condition.

Labels, badges, signatures, dashboards, certificates, comments, reviewer praise, and generated explanations may cue authority-looking cases.
They do not carry authority unless the authority act, authority record, authority-reference relation, and evidence or provenance relation selected by the direct authority pattern are named.

##### E.10:0.2c.28 - `profile`, `harness`, `catalog`, `registry`, `index`, `map`

These usually point to a review profile, review harness, registry record, catalog publication, navigation index, map, publication form, companion publication, publication-companion relation, or relation between one companion publication and the publication unit or project record it helps readers inspect or use. Choose that kind named by value before writing; do not leave `support record` as the recovered head unless the named FPF pattern really defines that record kind.
Treat one as a governing FPF pattern body, accepted campaign `DRR`, named current architecture document, or relation to one of them only when the named FPF pattern, accepted `DRR`, or architecture document and the obtaining direct relation with its actual participants are given by value; keep any row, index entry, or map element as a claim-bearing episteme or C.29 representation under its own owner.

Split:
- review profile;
- review harness;
- source map;
- navigation index;
- registry record;
- catalog publication;
- benchmark harness;
- entry aid or discoverability aid;
- governing pattern body.

If the named companion publication, review profile, review harness, registry record, index, or map mainly helps readers find, compare, test, or review something, keep it as a companion, navigation, or testing aid until a named FPF pattern or accepted `DRR` records the recurring action-guidance gain by value.

##### E.10:0.2c.29 - `entry`, `front door`, `corridor`, `route`

These terms often mix navigation, recognition, movement, and authority.

Split:
- entry publication or navigation aid;
- first-use recognition text;
- navigation-bearing publication;
- movement, control, and temporal relation;
- process sequence;
- corridor overview;
- governing FPF pattern named by the problem under repair; if source or local wording merely groups patterns, name the cluster phrase or relation phrase as literal wording and name the governing patterns by value; if an actual relation between patterns is being claimed, name the exact direct relation, its actual pattern participants, and its direct governor.

An entry can make the right pattern easier to find.
It does not prove the pattern is sufficient, complete, or ready for gate use.

##### E.10:0.2c.30 - `same`, `parity`, `identity`, `equivalence`, `mirror`

Similarity is not identity.
Before accepting same, parity, or equivalence wording, name which relation is being claimed:
- mirror file in parity with a governing source;
- same EntityOfConcern;
- same claim content;
- semantic equivalence;
- bridge relation;
- version identity;
- file or carrier equality;
- source-publication identity;
- no-loss transform.

If the relation is about mirror parity, verify against the governing source or state that the check is not performed.
If the relation is semantic, use `A.6.3`, `A.6.4`, `F.9`, or the selected bridge pattern or equivalence pattern rather than relying on matching labels.

##### E.10:0.2c.31 - `file`, `path`, `host`, `packet`, `bundle`, `package`

These are carrier, transport, or package-form words.

Split:
- file or carrier;
- mirror file;
- file carrying FPF pattern text;
- document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use;
- review-facing target packet;
- review-facing context packet;
- release package;
- pattern package, pattern family, or pattern group under an accepted decision;
- governing source section.

A packet or bundle can carry a review target by value.
It is not automatically the authority-reference status, the target pattern, the accepted review result, or the FPF `authoritySourceRef` target.

##### E.10:0.2c.32 - `quality`, `characteristic`, `metric`, `indicator`, `score`

Do not let evaluation words float.

Split:
- `U.Characteristic`;
- characteristic space;
- Q-bundle;
- `E.21 PatternQualityQBundle`;
- scale;
- indicator;
- observed value;
- benchmark result;
- review finding;
- decision threshold;
- qualitative judgment with no scale.

`metric` is especially risky because FPF often treats it as imprecise shorthand for scale, value, or indicator machinery.
If the text says a quality improved, name what changed: characteristic, scale, observed value, threshold, decision consequence, or admissible act, work, or claim.
If "quality improved" refers to an FPF pattern version, name whether the change affects an `E.21` coordinate floor or declared coordinate target, status payload, stop condition, bounded non-use, or governing-pattern application.

##### E.10:0.2c.33 - `slot`, `field`, `row`, `label`, `badge`, `mark`, `cue`

These words are not kinds by themselves.

Split:
- A.6.5 `SlotSpec` inside a current reusable episteme-constitution `RelationSignature`;
- actual participant of an obtaining direct relation;
- A.6.5 `SlotSpec` inside another current reusable `RelationSignature`;
- participant designation inside a current assertion or relation-occurrence-description episteme;
- schema field;
- table row;
- row in a pattern body;
- publication label;
- provenance mark;
- status badge;
- pre-articulation cue;
- displayed cue;
- evidence marker.

A label, badge, mark, or cue may trigger review.
It does not prove currentness, identity, authority, evidence, gate passage, deontic permission, or release authorization unless the source relation and the evidence or provenance relation selected by the direct pattern are named by value.

#### E.10:0.2d - Current Scan Reading
For conformant text cleanup and source-expression unpacking, high-risk phrases are not automatically wrong. The shared scan is `E.10:0.2`; the rows below are episteme-publication-heavy candidate recovery prompts, not a second registry and not group kinds. Choose the recovered value by sentence function before reuse:
- topic-like or object-like wording: recover the actual `EntityOfConcern` or other governed participant of a claim-bearing episteme, the claim-bearing episteme itself, or a current A.6.5 episteme-constitution declaration and exact `SlotSpec`; otherwise recover the non-claim-bearing project kind;
- publication-unit wording that implies authoring or interpretation work: distinguish `U.Episteme`, `U.EpistemePublication`, `PublicationUnit`, file, source note, review target;
- `content`: usually one of claim graph, text span, publication unit, carrier bytes, or document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use;
- primary-entity field names: use `publicationUnitPrimaryEntityOfConcern` when a bounded `PublicationUnit` carries or exposes a claim-bearing episteme or episteme-lane `U.View`; otherwise use the non-claim-bearing kind or reference named by value when no claim-bearing episteme participant, A.6.5 declaration, or direct reference use is current;
- `surface`: keep `publication face or publication form` or `interop publication form` only when `publication-face kind` discipline is named by value; otherwise rewrite to generic publication face, declared MVPK face, publication carrier, interop carrier, UI or front-end face, companion publication, source named by value, evidence, assurance, obtaining direct relation and actual participants, C.29 representation and explicit correspondence, or carrier relation;
- `artifact`, `material`, `output`, and `content`: do not let them stay as heads in architecture or pattern prose when they carry ontology or authority;
- `source`, `target`: acceptable only when the actual source-side and target-side participants of the obtaining direct relation are named, or—when reusable declaration is current—the endpoint kinds and exact A.6.5 `SlotSpec` values are named; a schema field, table cell, graph endpoint, or mathematical argument stays a C.29 representation element until explicit correspondence is stated;
- `reader`, `reviewer`: safe only when the word really names a usability reader, review participant, or review process; otherwise name the generic publication face, declared MVPK face, packet, or `PublicationUnit`;
- pre-FPF sign vocabulary: recover FPF episteme kinds, publication kinds, view kinds, carrier kinds, and record kinds before reuse; do not rebuild FPF episteme and publication ontology on a concept-sign-denotation triad;
- generic FPF-side object wording, `locus`, `row`, `host`, or `target`: choose the recovered value named by value: FPF pattern, pattern section, accepted `DRR`, FPF publication, FPF view, document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use, file carrier, review target, record kind named by its governor, obtaining direct relation and actual participants, receiver-needed relation occurrence, claim-bearing episteme, reusable A.6.5 declaration, or C.29 representation and explicit correspondence;
- `supported use`: replace with the `admissibleUse` target named by value and non-admissible stronger or adjacent use, `relationClaimSlice` when a relation claim is being made, and `projectSideFPFRef` when a project-side FPF kind and reference named by value is being used;
- `strong`, `stronger`, `weak`, `weaker`: replace with scope, evidence class, threshold, gate or admission threshold, `source-loss mode` under `A.6.3.CSC` when a source-to-rendering loss is being claimed, coarsened rendering, or explicit abstain or reopen condition;
- `authority-bearing FPF pattern or row`: split into governing FPF pattern or pattern section, `relationClaimSlice` when a relation claim is being made, `admissibleUse` named by value when a boundary-use claim is being made, and `projectSideFPFRef` when a project-side FPF kind and reference named by value is being used;
- `route`, `call`, `invoke`, or procedure-like pattern wording: replace with pattern application or with project-side Work occurrence admitted under `U.Work`, `U.Method`, `C.11` decision value, or `A.6.A` action invitation.

High-risk residue classes:
- restore pre-FPF sign vocabulary to FPF kinds by context;
- unpack FPF-side umbrellas such as generic FPF-side object wording, generic named-target wording, `locus`, `row`, `host`, and `source` into the recovered value named by value, such as `FPF pattern`, `pattern section`, `DRR`, `FPF publication`, `U.View`, document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use, file carrier, record kind named by its governor, obtaining direct relation and actual participants, receiver-needed relation occurrence, claim-bearing episteme, reusable A.6.5 declaration, C.29 representation and explicit correspondence, or file-carrier phrase;
- unpack project-side umbrellas such as `input`, `raw material`, `source data`, `source material`, `artifact`, `output`, `result`, `outcome`, `deliverable`, `handoff`, `screen`, `dashboard`, `credential`, `badge`, and `explanation` into the exact governed entity and relation: publication or carrier use; project-side FPF kind and reference named by value; exact direct subject-relation claim or exact `A.6.1` operation-application binding; exact local `A.15.PROD` or `A.6.RCD` claim; `A.10` evidence relation; measurement-result episteme; evaluation or diagnostic finding; `C.11` `ChoiceResult` or decision record; gate, assurance, status, action-invitation, work-plan, dated-work, method, or method-description use under its direct pattern; or an exact `A.6.P.WMR` non-assertability result independently reasoned as `factually unsupported`, `missing-information`, or `missing-governor`. Only `missing-governor` names the affected receiving use and future owner. Do not leave a generic work-result or result-measurement record as the recovered value;
- make admissibility phrases such as `supported use`, stronger or adjacent use not carried by the pattern of concern, insufficient evidence relation, and similar formulas name the `admissibleUse` target named by value and non-admissible stronger or adjacent use, `relationClaimSlice` when a relation claim is being made, and `projectSideFPFRef` when a project-side FPF kind and reference named by value is being used;
- check pattern-control metaphors such as `route`, `call`, `invoke`, `exit`, `path`, `branch`, `chooser`, and `workflow` for declarative pattern application versus real movement, control, and temporal claims.

#### E.10:0.2e - Trigger Concordance And Closure Mechanism

`E.10` is applied to a bounded FPF-facing text object, not only to one remembered example sentence. Before claiming `E.10` closure over an accepted `DRR`, FPF pattern, extracted pattern host, monolith section, review-facing packet, or FPF-facing guidance, complete trigger concordance when a high-pressure trigger is FPF-governed across the bounded object.

Do not build a heavy concordance for every ordinary word. Trigger concordance applies when one trigger word or trigger-headed phrase:

- appears in a selected name, durable reusable name, heading, table column, schema field, coordinate name, status value, or selected reusable authoring vocabulary;
- recurs across the problem frame, decision, selected names, validation, and handoff-like action claims or conformance subjects often enough to carry the local architecture;
- acts as a replacement head for another broad head;
- appears in a returned finding or accepted basis as a term whose meaning is carried into FPF wording;
- or remains the only word that lets the sentence appear precise.

The mechanism is:

1. Inventory the trigger spans inside the bounded object, with exact locations or grouped locations and count. Mark structural role: ordinary prose, selected name, heading, table column, field, example, quote-only wording, source-only wording, relation phrase, publication phrase, or source-use phrase.
2. Group occurrences by local interpretation, not by trigger word alone: ordinary no FPF-governed use, local lexical repair, relation-like use, episteme use, publication use, source-use, durable naming need, quote-only or source-only wording, false positive, or blocker.
3. For each local interpretation, choose and complete the repair consequence. Local repair may close under `E.10`. Relation-like wording applies `A.6.P` or its retained specialization; `A.6.RCD` opens only for the exact residual claim whose participants are known and which no current direct relation closes. Episteme wording, publication wording, or source-use wording applies `C.2.P`. Durable reusable naming applies `F.18` after the kind under repair and use recovery. Quote-only or source-only wording needs a non-use disposition. Classification labels are not closure endpoints.
4. Rewrite the bounded object, or leave a blocker. A note saying `apply A.6.P when triggered`, `apply C.2.P when triggered`, `apply the governing pattern when the recovered claim is being made`, `subject to F.18 later`, `classified under A.6.P`, `classified under C.2.P`, or `boundaries are stated nearby` is not closure unless the recovered result is already present in the final wording or the still-triggered repair is explicitly blocking. Every FPF-governed trigger has a non-empty `Final wording or blocker` cell.
5. Reread saturation. If one trigger word still carries several different local interpretations after repair, or dominates the selected names of the bounded object, the text has likely preserved an umbrella rather than repaired it. Split the local interpretations into names or governing-pattern applications named by value before accepting the wording.

Use this compact closure table when the governing review selects trigger concordance:

| Trigger span or name | Locations and count with structural role | selected interpretation | Recovery needed | Final wording or blocker | Closure disposition |
| --- | --- | --- | --- | --- | --- |
|  |  | ordinary no FPF-governed use; local repair; relation-like use; episteme, publication, or source-use; durable naming; quote-only; false positive; blocker | `E.10`, `A.6.P`, `C.2.P`, `F.18`, or not triggered |  | closed locally; recovered and integrated; quote-only; not triggered by value; still blocking |

Allowed closure dispositions are only:

- ordinary wording with no FPF-governed use accepted;
- local lexical repair closed under `E.10`;
- `A.6.P` recovery completed and integrated into the text;
- `C.2.P` recovery completed and integrated into the text;
- `F.18` naming decision completed after kind and use recovery and integrated into the text;
- quote-only, source-only, or non-use disposition stated by value;
- false positive stated by value;
- still blocking.

Do not close trigger concordance with a summary statement that `E.10 was applied`, with a citation to `A.6.P` or `C.2.P` alone, with a correct classification but no governing-pattern repair product, with a later-work promise, or with a table that covers only representative examples while the remaining FPF-governed occurrences keep the same unresolved head.

#### E.10:0.3 - Recovery and disposition table

`E.10` gives only a small local recovery and disposition form. It does not unpack relation-like or episteme-publication-heavy source meaning by itself.

| `E.10` result | Recovery product | Disposition |
| --- | --- | --- |
| local wording accepted | Ordinary wording with no FPF-governed use. | Leave as ordinary prose. |
| local wording rewrite | Repaired phrase that names the local kind named by value, register, ordinary sense, or admissible lighter wording. | Accept locally after the replacement-candidate anti-umbrella rule. |
| relational precision restoration triggered | Trigger span plus a relation-like use whose direct predicate or actual participant remains unclear: endpoint, qualifier, slot, scope, time, viewpoint, basedness, service, bridge wording, whole-part, mapping, comparison, or dependency. A `support` phrase enters this row only when `E.10:0.2` has identified a direct subject relation or common alternative but the reader still cannot name its direct predicate or an actual participant. | Apply `A.6.P` or the specialization for that relation to recover the missing predicate or participant. Once both are clear, apply `A.6.RCD` only if no current pattern governs that predicate. A common lexical alternative that is already clear goes straight to its owner and is not chosen again in `A.6.P`; if the trigger is a false positive, say why. |
| epistemic precision restoration triggered | Trigger span plus the episteme, publication, source-use relation, or source-expression relation under repair. | Apply `C.2.P` before accepting current FPF wording; if the trigger is a false positive, state that reason by value. |
| combined precision restoration triggered | Trigger span plus both relation-like wording and episteme, publication, or source-use wording. | Apply `C.2.P` for the source-currentness relation and claim-bearing episteme or publication relation set; apply `A.6.P` for the relation-bearing slice. |

#### E.10:0.4 - Closure rules

| Closure question | Conforming answer |
| --- | --- |
| Can `E.10` alone close the case? | Yes only for `not-triggered`, false-positive by value, ordinary wording with no FPF-governed use, and local lexical-repair outcomes whose replacement candidate has also passed `E.10`. |
| What counts as `closed by value`? | The final wording or recorded disposition names the direct-owner result: recovered kind; obtaining direct relation and actual participants; receiver-needed occurrence; current A.6.5 declaration; claim-bearing episteme and any current participant designations; C.29 representation and explicit correspondence; admissible use and non-admissible stronger or adjacent use; source-use disposition; publication construction; durable naming decision; or false-positive reason. The reader can recover what the trigger meant without chat memory or a future pass. |
| What counts as `A.6.P` or `C.2.P` application? | A governing-pattern application is not the classification label. It is the completed recovery product: selected relation interpretation; obtaining direct relation and actual participants or reason-specific blocker; receiver-needed relation occurrence; current declaration, assertion episteme, participant designation, publication construction, or C.29 representation and explicit correspondence under its separate owner; endpoint, qualifier, scope, admissible-use, and source-use repair; project-side reference; false-positive reason; quote-only or non-use disposition; or named blocker integrated by value into the text or closure account. |
| Can `E.10` close relation-like wording by itself? | Not while the direct predicate or an actual participant remains unclear. For `support`, `E.10:0.2` first separates ordinary or quoted non-use, a recognizable direct subject relation, and common lexical alternatives. Ordinary non-use can stop here. A clear direct subject relation goes to its owner; a clear common alternative goes straight to the owner named in `E.10:0.2`. Apply `A.6.P` only to recover an unclear predicate or participant, and apply `A.6.RCD` only after both are clear and no current pattern governs that predicate. Do not choose a common alternative again in `A.6.P`. |
| Can `E.10` close episteme-publication or source-use wording by itself? | No. If the problem under repair is source wording, episteme, publication, view, face, carrier, publication unit, EntityOfConcern, grounding, FPF transfer, project-side claim, admissible-use claim, or pattern-application wording, the conforming text applies `C.2.P` or states the false-positive reason by value. |
| Can a replacement term close the case because it sounds more precise? | No. A repair is not conforming merely because the original overloaded word was replaced. The replacement candidate passes the same trigger scan and anti-umbrella test. |
| Can a trigger-headed selected name close with `F.18 later`? | No, not when the name is already selected by an accepted `DRR`, table heading, schema field, coordinate, pattern authoring draft, or selected reusable authoring vocabulary. Complete `F.18` now after kind and use recovery, replace the head with wording named by value, or leave the naming issue blocking by value. |
| Can a correct classification close the case without changing the text? | No. Correct classification only starts the consequence. For an FPF-governed trigger, closure means changed final wording, a governing-pattern result recorded by value, or an explicit blocker. |
| Can a high-frequency trigger close through representative examples? | No. When the governing review selects trigger concordance, representative examples may guide grouping, but the closure account covers all FPF-governed occurrences or exact grouped locations and counts and states what remains ordinary, repaired, quote-only, rejected, or blocking. |
| Where do trigger words and examples belong? | In this shared `E.10` scan architecture or in a named local application profile tied to its own primary `EntityOfConcern`, obtaining direct relation and actual participants, reusable A.6.5 declaration, claim-bearing episteme and any participant designations, or C.29 representation and explicit correspondence. Do not copy growing word lists into `F.18`, `A.6.P`, `C.2.P`, `E.19`, or local checklists. |

