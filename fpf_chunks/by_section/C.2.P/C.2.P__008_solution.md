---
chunk_kind: "child"
pattern_id: "C.2.P"
pattern_title: "Epistemic Precision Restoration"
section_id: "C.2.P:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P/C.2.P__008_solution.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "C.2.P — Epistemic Precision Restoration"
  - "C.2.P:4 — Solution"
line_start: 34352
line_end: 34705
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.A"
  - "A.6.F"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16.P"
  - "C.16.Q"
  - "C.2.1"
  - "C.30.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.12"
  - "E.17"
  - "E.17.0"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "E.2"
  - "E.6"
  - "E.7"
  - "E.8"
  - "E.9"
  - "F.18"
keywords:
---

### C.2.P:4 - Solution

Repair episteme-publication-heavy wording by epistemic precision restoration, not by dictionary replacement.

A successful rewrite satisfies these field-validity constraints:

1. the head kind and sentence function are recoverable under `E.10`;
2. a stable reusable name has `F.18` status;
3. a relation, comparison, dependency, support, sameness, grounding, mapping, or endpoint claim has `A.6.P` relation precision, with admissibility and project-side reliance questions split into their own fields;
4. a claim-bearing episteme, exact episteme species, episteme-lane view, or exact project-side FPF kind and reference has the needed `C.2.1` typing or named exact FPF claim or admissible-use boundary;
5. publication, view, face, and carrier distinctions satisfy `E.17.0`, `E.17`, and MVPK;
6. the repaired text satisfies `E.2` Pillars, especially `P-2 Didactic Primacy`, by preserving or restoring one remaining admissible reader move: a usable action, a recognition reason that tells the working reader why the distinction matters, or a named exact FPF pattern application that carries the live claim; when both Tech and Plain registers are live, the Plain or didactic line maps back to the recovered Tech kind, relation, or exact FPF pattern application under `E.10:6.2`; ordinary Plain wording and intentional didactic metaphor stay light when they carry no FPF-governed use, but ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim in a more expressive Plain line must be recoverable through the repaired Tech fields; FPF-governed Problem frames, Problem sections, recognition texts, examples, and worked slices must still show the broad working situation and first useful move, or the rewrite is incomplete;
7. the final phrase preserves the distinction without adding another claim;
8. unrecoverable meaning, kind, register mapping, or remaining reader move fails closed.

The detailed solution below carries the glossary and rewrite rules as ordinary pattern subsections. It is not an external container: these subsections are the pattern's detailed epistemic precision-restoration guidance.

#### C.2.P:4.0a - EpistemicPrecisionRestorationRecord

For FPF-governed cases, the recovery product is a compact pattern-local `EpistemicPrecisionRestorationRecord` or an equivalent local rewrite note. Ordinary local phrase repair may end as the repaired sentence itself when kind, relation, and admissible use are now clear and no downstream reliance, cross-context reuse, grouped-kind risk, hidden authority claim, project-side overclaim, conflict among publication, EntityOfConcern, and project-side action claims, or contested source meaning remains live. Prefer the plain names `epistemic precision-restoration note`, `compact epistemic precision-restoration row`, or `local rewrite note` when durable inspection does not require the code-like field name. The recovery note is a lightweight pattern-local authoring or review product, not a new ontology, not a dispatch table, not a durable FPF record kind, and not a mandatory heavyweight project record. It becomes a durable FPF record only if another accepted pattern or accepted `DRR` explicitly admits it as one. It records only the trigger, the recovered FPF kind and relation set, the requirement from the exact governing FPF pattern, and the final rewrite disposition that must remain inspectable after the repair.

Minimum fields when FPF-governed:

Recover by sentence function and live claim, not word form. For words such as `source`, `support`, `status`, `valid`, `ready`, `approved`, and `used`, first ask what the sentence would let the reader do or rely on: source-finding only, source availability, source use, evidence relation, gate passage, decision status, readiness threshold, work permission, assurance, engineering justification, or ordinary orientation. Then fill only the field whose exact FPF kind, relation, or project-side reference is live.

| Field | Meaning | Governing FPF source when live |
| --- | --- | --- |
| `triggerSpan` | The exact word, phrase, field, row, or sentence fragment carrying episteme-publication claim-bearing use. | `E.10` and this pattern. |
| `sentenceFunction` | Whether the span is definition, claim, instruction, comparison, publication description, evidence statement, gate statement, work statement, reliance statement, example, quote, or another named function. | `E.8`, `E.10`, and the local pattern being authored. |
| `recoveredHeadKind` | The exact FPF kind or explicit non-use disposition recovered from the phrase. | `F.18`, `A.6.P`, `A.7`, and the governing pattern for that kind. |
| `laneAndKindSet` | The live side, kind, and relation set: FPF-side pattern text; project-side episteme, publication, and work; the `A.7` EntityOfConcern, Description episteme, and carrier distinction when live; publication form, generic publication face, MVPK face under E.17 constraints, `U.View`, `PublicationUnit`, carrier, front-end, and cue when live; and exact work, evidence, gate, decision, or action-invitation value when live. | `A.7`, `E.17`, current episteme and publication patterns, and exact project-side FPF patterns. |
| `publicationRelationSet` | `U.EpistemePublication`, publication form, generic publication face, MVPK face under E.17 constraints, bounded `PublicationUnit`, carrier, carrier relation, and front-end relation when live. | `C.2.1`, `E.17.0`, `E.17`, MVPK, and `A.7`. |
| `claimBearingEpistemeOrRecord` | Exact claim-bearing `U.Episteme`, exact episteme-lane `U.View` with explicit episteme tether when the governing FPF pattern makes that view live, exact project record kind and reference, or no claim-bearing episteme or record disposition. Publication form, generic publication face, carrier, `PublicationUnit`, and source cue stay in `publicationRelationSet` or `projectSideFPFRef` unless the claim is explicitly about that publication form, publication face, carrier, publication unit, or source cue. An MVPK face under E.17 constraints is handled through the exact episteme-lane `U.View` typing when that typing is live. | `C.2.1`, `E.17`, and the exact governing pattern for the record if live. |
| `relationClaimSlice` | Empty, or a local note that `A.6.P` relation precision is live for this sentence. It must name the relation problem being handled: relation, comparison, dependency, support, sameness, grounding, mapping, endpoint claim, or cross-context bridge claim. The recovery then names `RelationKind`, `QualifiedRelationRecord`, relation phrase, candidate-set note, or bridge card when live. | `A.6.P`. |
| `admissibleUse` | The exact admissible use, non-admissible stronger or adjacent use, and L-, A-, D-, and E-claim split when the sentence makes a boundary-use claim. | `A.6.B`, `A.6`, and the exact governing pattern for the use. |
| `projectSideFPFRef` | The exact project-side FPF kind and reference when the sentence would be used for work, evidence, gate, constraint, adjudication, decision, commitment, method, action invitation, assurance, or engineering justification. | `A.15`, `A.15.4`, `A.10`, `A.20`, `A.21`, `B.3`, `C.11`, `A.2.8`, `A.2.9`, `A.6.A`, or another exact FPF pattern. |
| `precisionRestorationExit` | Empty, or the exact precision-restoration or receiving pattern that takes over after source wording, current FPF wording, publication, and carrier recovery: `A.6.P`, `A.6.F`, `C.30.P`, `C.16.P`, `C.16.Q`, `A.6.3.CSC`, `F.18`, or an exact evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens, architecture, characteristic, quality, or publication pattern. | `E.10`, `E.10.ARCH`, and the exact receiving pattern named in the field. |
| `selectedRewrite` | The final exact wording or record-shaped value. | This pattern plus the exact governing FPF pattern named above. |
| `remainingAdmissibleReaderMove` | One short line, Plain-facing when the text serves a working reader, naming what the reader may now do, why the distinction still matters, or which exact named FPF pattern governs the live claim. This field is the local `E.2` `P-2` preservation check for FPF-governed epistemic precision restoration, not an optional commentary line. When both Tech and Plain registers are live, this line must map back to the recovered Tech kind, relation, or exact FPF pattern application. It may be more readable or memorable than the Tech line, and may use an intentional didactic metaphor, but any ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim must remain recoverable through that repaired Tech interpretation. If no such line can be stated, the rewrite is incomplete or must fall to a non-use disposition. | This pattern, `E.2`, `E.8`, `E.10:6.2`, `E.12`, and the exact named FPF pattern when another pattern governs a live claim. |
| `disposition` | Local recovery outcome: recovered by value, reduced-use cue, understandable FPF extension candidate, blocked use, rewrite incomplete, or not triggered. This slot is not a recovered FPF kind. | This pattern. |

Use the short form when only one field is live. Use the full record when several fields are live or when the phrase might otherwise create a grouped kind, hidden authority claim, project-side overclaim, conflict among publication, EntityOfConcern, and project-side action claims, contested source-use meaning, or procedure-like ordering of pattern applications.

#### C.2.P:4.1 - General Recovery Check
Use this recovery check whenever text proposes a new term, repairs an episteme-publication-heavy term, asks for language precision, or relies on wording around `PublicationUnit`, `EntityOfConcern`, publication, view, face, carrier, source-side relation, receiving-side relation, publication face, EntityOfConcern, or bounded publication-unit status.

0. **Mode selection.**
   Decide whether the current use is source-expression clarification over non-FPF prose or FPF-governed use. In source-expression clarification, preserve source-local nuance and do not force the whole source into FPF vocabulary. In FPF-governed use, the wording must satisfy `E.10` and the exact governing patterns named by the recovery.

1. **E.10 trigger scan and head-kind recovery.**
   Use `E.10:0.2` as the shared trigger scan. Decide what the head noun names before accepting the phrase: EntityOfConcern, Description episteme, or Description episteme admitted for specification use, `U.Episteme`, `U.View`, publication form, generic publication face, MVPK face under E.17 constraints, carrier or rendering, exact project-side FPF kind and reference, `A.15.1` dated `U.Work` occurrence, `A.6.A` action invitation, `A.2.9` `SpeechActRef`, `A.2.8` `U.Commitment`, `U.Method`, `U.MethodDescription`, document with named source, evidence, architecture, reviewed publication, review packet, review record, or review state, or source-local ordinary sense. Apply EntityOfConcern and Description-episteme boundary and specification use, Context, Tech, Plain, and carrier humility rules before treating a word as meaning-bearing.

2. **F.18 naming pass when a stable term is being chosen.**
   If the phrase is becoming a reusable head, fill at least the lightweight Name Card facts: Context, Kind, purpose and use-domain, local sense, candidate head families, NQD-front reasoning, sense-seed read-through, and the lexical Q tuple `{SemanticFidelity, CognitiveErgonomics, MorphologicalActionFit, AliasRisk}`. Do not pick a label only because it is intuitive. Do not accept a replacement label until it passes the `E.10:0.2` replacement-candidate anti-umbrella rule.

3. **A.6.P relation-precision pass when a phrase carries relation, comparison, or action-invitation claim.**
   Restore generic head kind first, then endpoint facets and kinds, then relation kind, slots, qualifiers, scope, time, viewpoint, and hooks for admissibility, evidence, and work. For `support` wording, do not stop at a substitute label: select the live support-like claim or relation under `A.6.P` first, including source-description relation, EntityOfConcern or grounding-holon grounding, base relation through `A.6.6`, evidence, assurance, causal-use, mathematical-lens, characteristic or measurement, admissible-use, work or enablement, or publication-companion use. If ambiguity remains, write a local Candidate-Set Note rather than debating synonyms.

4. **C.2.1 episteme-slot pass when the item is claim-bearing.**
   Name `EntityOfConcern`, grounding, ClaimGraph, viewpoint and view, reference scheme, representation scheme, and bounded context as far as the claim needs. Do not use `PublicationUnit` or a carrier word as a substitute episteme.

5. **E.17.0, E.17, MVPK publication pass when the item is published or reader-facing.**
   Separate the underlying episteme or view, `U.EpistemePublication`, publication form, generic publication face, MVPK face under E.17 constraints, `PublicationUnit`, carrier or rendering, and the exact project-side FPF kind and reference when a project-side claim is live. A face, card, screen, or explanation can guide interpretation or source-finding without becoming evidence, work, gate passage, authority, or release permission. If those claims are live, fill `admissibleUse` and `projectSideFPFRef` instead of treating the generic publication face or MVPK face under E.17 constraints as the source value.

5a. **Precision-restoration exit after source wording and current FPF wording recovery.**
   If source wording and current FPF wording, publication, carrier, face, or `PublicationUnit` recovery exposes architecture or structure wording, characteristic or scale wording, quality-term or evaluative characterization, function-like carrier wording, relation construction, controlled coarsening, naming, evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens, or another exact neighboring claim, fill `precisionRestorationExit` with the exact receiving pattern. Do not keep the neighboring claim inside `C.2.P` after this pattern has recovered the source wording, current FPF wording, and publication relation set.

6. **Remaining admissible reader move.**
   After the kind, relation, publication, and project-side splits are recovered, state the remaining admissible reader move in one short line: what the working reader can now do, why the distinction still matters, or which exact named FPF pattern governs the live claim. If both Tech and Plain registers are live, keep the Tech interpretation recoverable and make the Plain or didactic line map back to the recovered Tech kind, relation, or named exact FPF pattern application under `E.10:6.2`. Do not make this a heavy form for ordinary prose: a Plain line that carries no FPF-governed use may stay ordinary; a Plain line that carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim must be recoverable through the repaired Tech fields. If the repaired wording only proves that an overclaim was removed, but leaves no usable action, recognition reason, or exact FPF pattern application for the live claim, do not classify the repair as recovered by value.

7. **Authority-changing rewrite boundary.**
   If the result would rename an accepted FPF pattern, change an accepted FPF term, or mint a reusable FPF kind, this pattern only classifies the phrase as recovered by value or as an understandable FPF extension candidate. It does not make the authority change by itself. Use the accepted source that already carries the decision by value; do not add a second decision source merely to restate the same content.

Fail closed:
- if the kind and relation set cannot be recovered, keep the term as plain or informative prose;
- if the relation kind cannot be recovered, keep the statement as a cue or split alternatives;
- if the publication construction cannot be recovered, do not use that publication, generic publication face, MVPK face under E.17 constraints, form, carrier, or rendered unit for work, evidence, gate, or authority claims;
- fill `relationClaimSlice` only when a relation claim is live, and fill `admissibleUse` plus `projectSideFPFRef` when an admissibility or project-side reliance claim is live;
- if the recovered wording is type-correct but leaves no remaining admissible reader move, recognition reason, Tech-to-Plain mapping when both registers are live, or exact FPF pattern application, or if a Plain or didactic line supplies practical guidance through unrecovered ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim, mark the rewrite incomplete or demote the phrase to reduced-use cue or blocked use before using it as claim-bearing FPF or project text.
##### C.2.P:4.1.1 - Slash Discipline

In conventional abbreviations, source titles, mathematical notations, standards, URLs, file paths, and ordinary notations, a slash can be part of an accepted designation rather than a hidden FPF kind. In FPF-facing episteme and publication ontology, a slash is still a recovery trigger before it is a synonym marker unless the mark is part of such accepted notation, carrier syntax, or conventional designation.

Before leaving a slash expression in current prose, classify the expression as one of these cases:
- accepted notation or conventional designation: a standard name, source name, discipline abbreviation, established compound name, formula, ratio, fraction, unit, path-like quoted source token, title, product name, file path, URL, or quoted source wording where the slash is part of the accepted designation or carrier syntax; keep `ISO/IEC`, `ISO/IEC/IEEE`, `1/2`, URLs, conventional abbreviations, and similar forms when the sentence uses them as notation;
- a plain-language synonym pair with no ontology, authority, evidence, or admissibility claim;
- a lazy `and/or`-style join that must be split or recovered before FPF-governed use;
- a composite-kind candidate that needs `F.18` and `A.6.P` recovery;
- a relation claim that needs a `RelationKind`, a `QualifiedRelationRecord`, or a multi-term relation phrase with typed endpoints, slots, qualifiers, scope, time, and viewpoint;
- a tuple-like record that needs a named record kind and named slot semantics;
- a failed ontology signal where the sentence lists unlike values because the live FPF kind, relation record, relation phrase, tuple-like record, alternative-case disposition, or not-triggered disposition has not yet been recovered.

If the expression is not one of the safe notation, conventional-designation, carrier-syntax, quoted-source, or plain-language cases, do not keep the slash as final wording. Do not repair it by replacing the slash with one equally vague grouped word.
Write the recovered FPF kind, relation record, relation phrase, tuple-like record, alternative-case disposition, or not-triggered disposition by value.

##### C.2.P:4.1.2 - Unclear Source Meaning and FPF Extension Candidates

Sometimes the problem is not a bad word but one of two different cases:
- the intended claim cannot be determined from the surrounding source, current `FPF` kinds, or current FPF episteme and publication ontology;
- the claim is understandable, but current `FPF` does not yet contain the kind, pattern, relation record, or method guidance needed to carry it.

Do not merge those cases.
An unclear claim is not current architecture truth merely because deleting it feels risky, and it must not be rewritten by guessing a likely author intention.
An understandable uncovered claim may be retained as a candidate `FPF` extension only when the problem situation, tempting overread, rejected current uses, current `FPF` gap, and the first user action that would improve are stated by value.

Classify the case explicitly:
- **recovered by value:** the text now names the exact `U.Episteme`, selected `EntityOfConcern`, `U.View`, publication form, generic publication face, MVPK face under E.17 constraints, `PublicationUnit`, carrier relation, relation record, relation phrase, tuple-like record, FPF pattern, document with named source, evidence, architecture, reviewed publication, review packet, review record, or review state, exact project-side FPF kind and reference when `projectSideFPFRef` is live. The selected value is one live value, not the list: `C.11` `ChoiceResult`; `C.11` decision record; `A.6.A` action invitation; `A.15` `U.WorkPlan`; `A.15.1` dated `U.Work` occurrence; `U.Method`; `U.MethodDescription`; `A.20` constraint or adjudication decision record; `A.21` `GateDecision`; `A.21` `DecisionLogRef`; `A.10` evidence path; typed evidence record; `B.3` assurance or engineering-justification record; typed status record whose FPF status pattern is named; carrier relation; front-end relation; or not-triggered alternative;
- **understandable FPF extension candidate:** the thought is clear enough to state as a candidate new or amended FPF kind, pattern, relation record, method guidance, accepted `DRR` content decision, or campaign-scoped content question, but it does not carry current authority, evidence, or admissibility claim until an accepted architecture decision, accepted `DRR`, or accepted FPF pattern supplies that authority;
- **source wording without FPF-governed use:** the phrase has no current authority, evidence, or admissibility claim;
- **reduced-use cue:** the phrase is kept only as a recognition cue or anti-case, not as a claim-bearing architecture decision;
- **blocked use:** the phrase is not admissible for claim-bearing architecture, pattern, or project text while the needed meaning, kind, or relation is missing.
- **rewrite incomplete:** the repaired wording may be kind-correct, but it does not yet state a remaining admissible reader move, recognition reason, Tech-to-Plain mapping when both registers are live, or exact FPF pattern application, or a Plain or didactic line carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim that cannot be recovered from the Tech interpretation; continue repair or demote to a non-use disposition before the text has FPF-governed use.

These dispositions are recovery results, not a meta-governance authority over all of `FPF`.
When recovery names another exact FPF kind, that exact FPF pattern governs that kind, its admissible use, and its conformance checks.
`C.2.P` may identify that `A.10`, `A.15`, `A.15.4`, `A.20`, `A.21`, `B.3`, `C.11`, `F.9`, `E.17.EFP`, `E.17.ID.CR`, or another exact FPF pattern is live.
It does not govern the recovered kind after that identification.
`C.2.P` only makes the live kind, relation, and use boundary explicit enough that the right governing pattern can be applied.

No other disposition is closed.
In particular, "seems to mean", "probably about", a cleaner paraphrase, or a broad umbrella replacement is not a successful recovery.

#### C.2.P:4.2 - Core Glossary

##### C.2.P:4.2.0 - Cross-Side Fields That Must Stay Split

These fields are current episteme-publication precision vocabulary for `DRR`, architecture, and pattern-drafting work.
They exist to prevent one sentence from mixing FPF-side admissibility, project-side records, actual work or action, method selection, carrier access, and authority records.
They are local recovery aids, not FPF kinds, not record kinds, and not a universal record ontology.
Each field closes only by naming the exact FPF kind, relation record, relation phrase, exact project-side FPF kind and reference, or explicit non-use disposition that is live in the sentence.
The same local-aid rule applies to neighboring field names such as `sourceRelationClass`, `explanationSourceRelationClass`, `comparativeRelationClass`, `representationValidityAdmissibilityValue`, `allowedUse`, `misuseRisk`, and `worldContactPolicy`: they help record a local recovery or reader-use boundary, but they do not become kinds. These local fields do not instantiate evidence, gate, assurance, work, commitment, speech act, decision, release, authority, representation kind, world-contact kind, or policy kind. Read `allowedUse` as a local reader-fit field under `admissibleUse`, not as permission, evidence relation, or authority.

| Term | Current interpretation | Must not mean |
| --- | --- | --- |
| `FPF` as episteme | The whole `FPF` is a claim-bearing episteme with publications, parts, patterns, pattern sections, `DRR`s, and companion publications and documents with named source-basis, evidence-basis, architecture-basis, or review-basis roles. | A file, repository, taxonomy, pattern-language metaphor, or packet-local summary by default. |
| FPF pattern | A named FPF pattern: a reusable episteme species that gives action guidance for a problem situation. It is applied in a live problem situation. | Any recurring arrangement, procedure, method call, route, cluster label, checklist, or document with a named source-basis role. |
| pattern section | Either a part of the pattern episteme or a bounded `PublicationUnit` of that pattern publication, depending on sentence function. State which one matters when the distinction carries a claim. | Independent pattern, file location, generic locus, or record with named authority-reference relation. |
| accepted campaign `DRR` | A campaign decision source that states accepted content decisions for one campaign. | A pattern, current-authority summary, open-ended plan, review log, or replacement for pattern text. |
| `relationClaimSlice` | Empty, or a local note that `A.6.P` relation precision is live for one sentence. It must name the relation problem being handled: relation, comparison, dependency, support, sameness, grounding, mapping, endpoint claim, or cross-context bridge claim. The recovery then names `RelationKind`, `QualifiedRelationRecord`, relation phrase, candidate-set note, or bridge card when live, with typed endpoints, slots, qualifiers, and scope. | Dictionary replacement, one new umbrella kind, a bare `RelationKind` standing in for a relation record, a generic relation slot, support relation by default, or a list left as the final answer. |
| `admissibleUse` | The exact admissible use and non-admissible stronger or adjacent use when the sentence says what use, act, claim, or reliance is admissible. Use A.6.B when the boundary claim needs L-, A-, D-, and E-claim separation. | Generic supported use, permission-by-appearance, or visual cue or readability cue treated as admissibility. |
| `projectSideFPFRef` | The exact project-side FPF kind and reference when a publication, display, cue, or explanation is treated as a project-side source for work, evidence, gate, constraint, adjudication, decision, commitment, method, action invitation, assurance, or engineering justification. The field points to the project-side FPF kind and reference; the exact FPF pattern governs that relation and its checks. | One slot accepting records, actions, methods, carriers, evidence, gates, decisions, assurance, and engineering justification interchangeably. |
| `rejectedOverread` | A local field naming the tempting interpretation, evidence, gate, work, permission, approval, commitment, release, safety-proof, engineering-justification, or pattern-entry interpretation that must not be granted by resemblance alone. It is valid only with the recovered relation record or phrase or current-context unpacking that blocks it. It is not `U.Kind`, not a record kind, not a review-finding kind, and not a moralized defect class. | A general risk slogan, review finding, moralized "bad use", vague misuse label, or reusable FPF kind. |
| `admissibilityTargetKind`, `admissibilityTargetRef` | Source-local helper fields. Prefer `admissibleUse`; if these fields appear in material being repaired, they name the exact kind and reference inside `admissibleUse`, not an `A.6.P` relation slot. | A generic `supported use`, document capability, "stronger claim", reviewer permission, or untyped receiving-pattern exit. |

##### C.2.P:4.2.1 - Episteme, Publication, and Carrier Distinctions

| Term | Current interpretation | Must not mean |
| --- | --- | --- |
| `U.Episteme` | Claim-bearing episteme or episteme species. Use when the value is a claim-bearing episteme that can be described, viewed, grounded, revised, published, or relied on under FPF. | File, paragraph, screen, carrier, status note, process state, or generic "content". |
| `U.EpistemeSlotGraph` | The recoverable slot graph for a claim-bearing episteme: `EntityOfConcernSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot`, `RepresentationSchemeSlot`, and bounded context where live. | A prose checklist, a file map, or an optional decoration. |
| `EntityOfConcern`, `EntityOfConcernRef` | The EntityOfConcern reference under `C.2.1` named by a claim-bearing episteme or episteme-lane `U.View`: entity, relation, FPF pattern, FPF publication, project episteme, project publication, exact project-side FPF kind and reference, work or action when that work or action is itself the entity of concern, or another explicitly typed EntityOfConcern referent. Use this when the text is really about what the episteme is about. In publication-unit work, `EntityOfConcernRef` is used only through a live claim-bearing episteme or episteme-lane `U.View`; it does not float as a free field on the unit. | Generic topic, local table subject, file title, reviewed publication, review packet, or review record, required project-side work, decision, action invitation, authoring work, or anything someone happens to talk about. |
| wording such as `describedEntity`, `DescribedEntityRef`, `primary described entity` | Use `EntityOfConcern` and `EntityOfConcernRef` when the claim-bearing episteme slot is live. Use `publicationUnitPrimaryEntityOfConcern` when one bounded `PublicationUnit` carries or exposes a claim-bearing episteme or episteme-lane `U.View` and the primary entity of concern must be named. | A second C.2.1 slot family, a free publication-unit field, a generic topic, a live alias, or a new ontology beside `EntityOfConcern`. |
| `publicationUnitPrimaryEntityOfConcern` | The primary entity of concern, exact non-claim-bearing kind, topic, or subject that one bounded `PublicationUnit` is mainly about for the current use. When a claim-bearing episteme or episteme-lane `U.View` is live, this must be recoverable from the selected `EntityOfConcernRef`; otherwise name the exact non-claim-bearing kind or keep topic and subject as plain explanatory prose. | `EntityOfConcernRef` created without a claim-bearing episteme or episteme-lane view, publication-unit title by default, authoring process, carrier identity, or reader interest. |
| `GroundingHolon`, grounding relation | The grounding holon or grounding relation that grounds the EntityOfConcern when a claim depends on grounding, embodiment, witness, or reference-plane discipline. | A convenient source citation or an untyped entity mention. |
| `U.View`, `U.EpistemeView` | Effect-free projection or view over an episteme under `E.17.0`, `E.17` and the episteme morphism patterns. An MVPK face under E.17 constraints can be this kind only under MVPK constraints. | A UI view, reader viewpoint, screen, generic publication face, or new claim-bearing episteme by default. |
| `Viewpoint` | The stance or viewpoint specification for a view or multi-view description. | A reader viewpoint, reviewer opinion, pattern-application order, publication label, or carrier label. |
| publication | A publishable episteme, view, record relation, act or occurrence of publishing, or publication form, depending on sentence function. Always split by kind before use. | Generic document, any public-looking file, or proof that a claim is authorized. |
| `U.EpistemePublication` | Claim-bearing publication of an episteme when the publication itself carries episteme-publication identity. | Publication form, generic publication face, MVPK face under E.17 constraints, copy, file, dashboard tile, or carrier. |
| publication form | The typed form in which an episteme, view, or record is published. | The claim-bearing episteme itself, the face rendered for a reader, or the carrier holding bytes. |
| generic publication face | Reader-facing publication projection or face. It is not `U.View` by default; it becomes a view only when the exact governing FPF pattern makes that relation live. | `U.View` by default, carrier, UI face, front-end display, MVPK face under E.17 constraints, or claim-bearing episteme. |
| MVPK face under E.17 constraints | `E.17` face emitted under MVPK constraints from a source episteme or episteme-lane view, publication viewpoint, scope, pins, and face kind. It may be a `U.EpistemeView` when the MVPK profile makes that typing live. | Generic publication face, carrier, UI face, front-end display, or proof of evidence, work, gate, or authority by presentation. |
| carrier, front-end, rendering | The system, medium, file, display, front-end, or rendering that bears or shows an encoding. | Episteme identity, publication form, `U.View`, proof of evidence, or authority-reference relation. |
| `PublicationUnit` | `E.17.AUD`-cluster head for one bounded unit inside a publication that a person inspects as one unit: a pattern body, section, table, note, card, sheet, screen block, or another bounded publication unit whose boundary is named. A card, sheet, or screen block counts only when its boundary is inside a named publication or generic publication face and the sentence needs that bounded unit as the inspected publication unit. It is part of or bounded by the publication face that renders or locates it, whether that face is generic or emitted under E.17 and MVPK constraints. It may carry or expose a claim-bearing episteme, view, record, cue, or local rendered content when that carried item and relation are named, but it is not identical with the carried item. | Authoring process, reviewer process, file, carrier, front-end, UI behavior, dashboard behavior or export behavior, whole publication architecture, `U.Episteme`, `U.View`, publication form, generic publication face, MVPK face under E.17 constraints, or "anything written". |
| exact project-side FPF kind and reference | Evidence record, gate record, work record, status record, commitment record, role-assignment record, decision record, source `U.Episteme`, source `U.EpistemePublication`, status-register entry, or another project record whose governing FPF kind is named. | Semantic content in general, current process state, or a free-form note. |
| source document | A document used as source basis, evidence basis, architecture basis, or review basis. Name whether it is source basis, evidence basis, architecture basis, or review basis directly. | A governing source by folder proximity, the EntityOfConcern carried or exposed by that source document, or the authority-reference relation unless that relation is explicit. |
| reviewed publication, review packet, or review record | The exact reviewed publication, review packet, review record, or bounded publication unit sent or inspected in review. | The EntityOfConcern carried or exposed by that reviewed publication, review packet, or review record, the source-basis role behind it, or a packet-local summary. |
##### C.2.P:4.2.2 - Trigger Boundary

Lexical trigger scanning and direct known exact-pattern selection are governed by `E.10:0.2`, `E.10:0.2a`, `E.10:0.2b`, `E.10:0.2c`, and `E.10:0.2d`.

This pattern is applicable after that scan only when the exact governing pattern cannot yet be selected directly because the sentence still confuses source wording, claim-bearing episteme, publication or carrier construction, project-side reliance, pattern-application wording, or use or non-use disposition.

When this pattern is applicable, do not restart from word taste. Keep the `E.10` trigger result as input and recover source-expression clarification, FPF-governed use, live episteme-publication relation set, use disposition, and remaining admissible reader move.
#### C.2.P:4.3 - Current Preferred Vocabulary
Use `PublicationUnit` when the intended entity is a bounded, human-inspected unit inside a publication.
Do not use it for UI behavior, carrier behavior, front-end behavior, file identity, dashboard behavior, or export behavior; use `A.7`, carrier wording, front-end wording, or the exact FPF governing pattern instead.

Use the current cluster names directly: `PublicationUnit Stability Discipline`, `Local Head Restoration`, and `PublicationUnit Primary EntityOfConcern Discipline`.
When the live entity is a bounded unit inside a publication, use `PublicationUnit`; when the live entity is authoring or editing work, name that work directly.

Use `EntityOfConcern`, `EntityOfConcernRef`, and `publicationUnitPrimaryEntityOfConcern` when local wording means the EntityOfConcern named by a claim-bearing episteme or episteme-lane view, or the primary entity of concern stabilized by one bounded publication unit over that carried item.

For `describedEntity`, `DescribedEntityRef`, `primary described entity`, `EntityOfInterest`, or `EoIClass`, use `EntityOfConcernSlot`, `entityOfConcernRef`, `EntityOfConcernRef`, `EntityOfConcernChangeMode`, `EntityOfConcernClass`, `publicationUnitPrimaryEntityOfConcern`, or the exact local FPF kind. If no claim-bearing episteme or episteme-lane view is live, use an exact non-claim-bearing kind or plain `topic` or `subject` instead of inventing an `EntityOfConcernRef`.

Use ordinary `topic`, `subject`, or `local referent` only in non-normative explanatory prose where no episteme slot, publication construction, or authority relation is being asserted.

Do not mint any other new reusable FPF name from this pattern alone. `PublicationUnit` is governed by the `E.17.AUD` cluster named **PublicationUnit Stability Discipline**; this pattern recovers bounded-publication-unit wording into that head when the entity is live and points to that cluster for governance. FPF-governed uses keep the nearby definition or explicit publication relation set.
##### C.2.P:4.3.1 - F.18 And A.6.P Admission Interpretation For `PublicationUnit`

This is the F.18 and A.6.P name interpretation that this pattern reflects from the selected `E.17.AUD` cluster correction.
It records why `PublicationUnit` is the selected bounded publication-unit head for the `E.17.AUD` cluster, while `C.2.P` remains the epistemic precision-restoration pattern.

```text
F.18 and A.6.P admission interpretation:
  Context: conformant FPF authoring and review where bounded publication units must not be confused with epistemes, views, publication forms, generic publication faces, MVPK faces under E.17 constraints, carriers, authoring work, or review process.
  Kind: primary-entity or local-head field for a bounded unit inside one publication.
  Purpose and use-domain: keep one human-inspected publication unit distinct from episteme, view, publication form, generic publication face, MVPK face under E.17 constraints, carrier, authoring work, and review process.
  Selected Tech label: PublicationUnit.
  Plain interpretation: bounded unit inside a publication that a person inspects as one unit.
  Candidate head families considered:
    - authoring-centered unit labels
    - reader-action-centered unit labels
    - mixed authoring-and-reader-action unit labels
    - PublicationReadingUnit
    - PublicationAuthoringUnit
    - PublicationUnit
    - ContentSpan
    - DocumentUnit
  F.18 result:
    - `PublicationUnit` has better SemanticFidelity than authoring-centered unit labels because the unit belongs to the publication lane, not to the authoring process.
    - `PublicationUnit` has better MorphologicalActionFit than mixed authoring-and-reader-action unit labels because it does not mix author, reader, and unit-boundary roles in one head.
    - `PublicationUnit` has lower AliasRisk than `content span` and `document unit` because `content` and `document` blur episteme, publication form, and carrier.
    - `PublicationUnit` still has nonzero AliasRisk because `publication` itself splits into act or occurrence of publishing, episteme publication, form, generic face, MVPK face under E.17 constraints, unit, and carrier; therefore FPF-governed uses keep the nearby definition or explicit publication relation set.
  Current status: admitted reusable FPF head for conformant episteme-publication-heavy FPF text within the declared bounded-publication-unit repair scope; use a more specific already accepted head where one governs the text under repair.
```

#### C.2.P:4.4 - Epistemic Precision Restoration After E.10

Lexical trigger rewrite rules are governed by `E.10:0.2b`, `E.10:0.2c`, and `E.10:0.2d`.

Use this pattern after those rules only when one of these remains unresolved:
- source-expression clarification versus FPF-governed use;
- source-local meaning versus current FPF wording;
- claim-bearing episteme versus publication, view, face, carrier, or publication unit;
- EntityOfConcern, grounding relation, or source cue versus project-side evidence, work, gate, decision, assurance, method, action, release, or engineering justification;
- declarative FPF pattern application versus project work or control flow;
- use disposition: recovered by value, reduced-use cue, understandable FPF extension candidate, blocked use, rewrite incomplete, or not triggered;
- remaining admissible reader move or Tech-to-Plain mapping after epistemic precision repair.

When none of these remains unresolved, apply the exact governing pattern selected by `E.10` directly.
#### C.2.P:4.5 - Rewrite Execution Modes
Use the smallest sufficient mode that preserves the distinction. The template is an epistemic precision device, not a form to fill for every ordinary wording cleanup.

##### C.2.P:4.5.1 - Local prose cleanup

Use this mode when the phrase under repair is non-normative local prose and does not carry ontology, authority, review scope, release state, admissibility, or a reusable name.

Action: rewrite directly or leave it unchanged. No table row is required.

##### C.2.P:4.5.2 - Compact epistemic precision-restoration row

Use a compact row for ordinary architecture and source-basis or review-basis document cleanup where a sufficient FPF kind, relation record, relation phrase, or tuple-like record can be recovered without minting a new FPF head.

```text
Compact epistemic precision-restoration row:
  file path, if live:
  FPF pattern, if live:
  pattern section, if live:
  sentence reference:
  phrase under repair:
  live sentence function:
  selected exact FPF kind or exact project-side FPF kind:
  `relationClaimSlice` triggered? yes or no
  relation problem, if triggered:
  admissibleUse triggered? yes or no
  projectSideFPFRef triggered? yes or no
  relation claim? yes or no
  if relation claim:
    RelationKind:
    endpoint, slot, qualifier notes:
    admissibilityTargetKind:
    admissibilityTargetRef:
  if local current-context unpacking:
    FPF-side kind, reference, or relation:
    exact project-side FPF kind, if live:
    exact project-side reference, if live:
    notTriggeredReason:
  replacement:
  remaining admissible reader move:
  distinction disposition: preserved, split, intentionally retired, still missing
```

##### C.2.P:4.5.3 - Full epistemic precision-restoration check

Use the full check when the wording may change ontology, introduce or retire a reusable head, change a claim-bearing pattern or document with named source, evidence, architecture, or reviewed publication, review packet, review record, or review state, or resolve a contested source-meaning problem.

```text
Epistemic precision-restoration check:
  file path, if live:
  FPF pattern, if live:
  pattern section, if live:
  sentence reference:
  phrase under repair:
  sentence function:
  distinction carried:
  E.10 head kind and EntityOfConcern and Description-episteme boundary and specification use interpretation:
  F.18 naming status: no stable term, reuse, MintNew sketch, DocumentLegacy
  F.18 candidate head families, if naming is live:
  F.18 lexical Q result, if naming is live:
    SemanticFidelity:
    CognitiveErgonomics:
    MorphologicalActionFit:
    AliasRisk:
  A.6.P trigger? yes or no
  A.6.P selected relation kind, slots, qualifiers, if live:
  claim-bearing episteme live? yes or no
  FPF kind and relation set:
  EntityOfConcern, grounding, ClaimGraph, viewpoint slots triggered:
  E.17 and MVPK publication form, generic face, MVPK face under E.17 constraints, view, carrier split:
  PublicationUnit typing, if any:
  FPF-side or project-side sentence:
  `relationClaimSlice` triggered? yes or no
  relation problem, if triggered:
  admissibleUse triggered? yes or no
  projectSideFPFRef triggered? yes or no
  relation claim? yes or no
  if relation claim:
    RelationKind:
    QualifiedRelationRecord slots:
    admissibilityTargetKind:
    admissibilityTargetRef:
  if local current-context unpacking:
    FPF-side kind, reference, or relation:
    exact project-side FPF kind, if live:
    exact project-side reference, if live:
    notTriggeredReason:
  rejectedOverread, if live:
  project-side record, work, action, method, carrier crossing:
  heterogeneous-list classification: one live kind, relation set, tuple-like record, alternative cases, failed ontology, not triggered
  pattern application, project work, decision distinction:
  chosen rewrite:
  remaining admissible reader move:
  distinction disposition: preserved, split, intentionally retired, still missing
  unrecovered wording retained? no, yes, with scope and reason:
  use disposition: recovered by value, extension candidate, reduced-use cue, blocked use, rewrite incomplete, not triggered
```

##### C.2.P:4.5.4 - Epistemic Precision-Restoration Note

Use an epistemic precision-restoration note only when wording carries ontology, authority, evidence, or admissibility claim. The note records the original phrase, recovered FPF kind or relation, exact reference when live, project-side FPF kind and reference when live, remaining admissible reader move, and disposition: recovered by value, extension candidate, reduced-use cue, blocked use, rewrite incomplete, or not triggered.

#### C.2.P:4.6 - Ordinary Completion and Reopen Boundary

A `C.2.P` application is complete for ordinary pattern-authoring use when the smallest sufficient product is present:

1. `E.10` trigger result is kept as input and the text does not restart from word taste;
2. the wording is either left ordinary, repaired locally, expressed as a compact epistemic precision-restoration row, or escalated to the full check because the live claim requires it;
3. the recovered episteme, publication, view, face, carrier, publication unit, EntityOfConcern, grounding relation, project-side reference, or use disposition is named by value;
4. every relation-like slice that remains live is assigned to `A.6.P` or its retained specialization, rather than being hidden inside this pattern;
5. the remaining admissible reader move survives in ordinary prose or the wording is explicitly demoted to reduced-use cue, blocked use, rewrite incomplete, or not triggered.

Use the lowest sufficient product. A clean sentence is enough when one sentence recovers the live claim. Use a compact row when the reader must inspect one recovered kind, relation, or disposition later. Use the full check only when several fields are live, when source wording's FPF use is contested, when a durable name may be minted, or when a publication, carrier, or project-side overread would otherwise survive.

This pattern can be applied to its own wording at the same lowest sufficient mode. If `C.2.P` text itself blurs a source expression, publication construction, pattern application, relation slice, or project-side reliance claim, repair that local wording here; do not create a recursive pattern-quality apparatus.

Reopen or lower a prior `C.2.P` repair when one of these content discoveries appears:

- the replacement head is another umbrella word such as `support`, `surface`, `route`, `kind`, `object`, `record`, `map`, or `mapping` without exact FPF kind and boundary;
- the repaired wording is type-correct but no longer tells the working reader what action, non-use, or neighboring-pattern application remains;
- a neighboring pattern is now the true governing pattern for the live evidence, assurance, gate, work, decision, publication, architecture, structure, relation, or naming claim;
- an entry cue, ToC row, summary, dashboard, retrieval snippet, or source-basis note preserves the pre-repair broad interpretation after the pattern body was repaired;
- repeated use shows that authors are filling the full check where a local sentence or compact row would suffice.

The ordinary stop condition is local: once the current sentence or bounded publication unit preserves kind, relation, use disposition, and remaining admissible reader move, stop. Do not keep improving wording merely because a more elaborate record could be filled.
