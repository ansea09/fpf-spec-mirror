---
chunk_kind: "child"
pattern_id: "C.2.P"
pattern_title: "Epistemic Precision Restoration"
section_id: "C.2.P:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P/C.2.P__008_solution.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "C.2.P — Epistemic Precision Restoration"
  - "C.2.P:4 — Solution"
line_start: 42586
line_end: 42830
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
  - "A.6.P.WMR"
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
2. a stable reusable name has an `F.18` naming result;
3. a relation, comparison, dependency, support, sameness, grounding, mapping, or endpoint claim has `A.6.P` relation precision, with use-boundary and project-side reliance questions split into their own fields;
4. a claim-bearing episteme, episteme species named by value, episteme-lane view, or project-side FPF kind and reference named by value has the needed `C.2.1` typing or named FPF claim or declared-use boundary named by value;
5. publication, view, face, and carrier distinctions satisfy `E.17.0`, `E.17`, and MVPK;
6. the repaired text satisfies `E.2` Pillars, especially `P-2 Didactic Primacy`, by preserving or restoring one remaining reader use: a usable action, a recognition reason that tells the working reader why the distinction matters, or a named FPF pattern application that carries the claim being made; when both Tech and Plain registers are current, the Plain or didactic line maps back to the recovered Tech kind, relation, or FPF pattern application under `E.10:6.2`; ordinary Plain wording and intentional didactic metaphor stay light when they carry no FPF-governed use, but ontological, evidence, causal, assurance, bridge, gate, work, decision, or use-boundary claim in a more expressive Plain line must be recoverable through the repaired Tech fields; FPF-governed Problem frames, Problem sections, recognition texts, examples, and worked slices must still show the broad working situation and first useful move, or the rewrite is incomplete;
7. the final phrase preserves the distinction without adding another claim;
8. unrecoverable meaning, kind, register mapping, or remaining reader use fails closed.

The detailed solution below carries the glossary and rewrite rules as ordinary pattern subsections. It is not an external container: these subsections are the pattern's detailed epistemic precision-restoration guidance.

#### C.2.P:4.0a - Progressive recovery products

An ordinary application ends with the repaired sentence and one plain reason or non-use boundary. It creates no record.

Use a compact row only when another reader must later inspect the recovery:

```text
Compact epistemic precision-restoration row:
  exactSpanOrSentence:
  sentenceFunction:
  recoveredKindOrRelation:
  selectedWordingOrDisposition:
  remainingReaderUse:
```

Add a source identity, publication occurrence, carrier relation, declared-use boundary, project-side reference, naming decision, evidence relation, or assurance reference only when that exact claim is live. Optional fields do not become a common schema.

Use a full check only when several unresolved fields interact, the source-to-FPF use is contested, or a reusable ontological or naming decision is being made. A full check records the original sentence, the competing interpretations, the selected kinds and relations, the exact neighboring-pattern contributions, rejected overreads, selected wording, remaining reader use, and reopen condition. It does not repeat empty trigger flags or every possible downstream field.

When the wording exposes a field defined elsewhere, name the `contributingPattern` and the concrete definition, constraint, or test it supplies. The pattern does not own the sentence or act on it.

**Carrier-specific recovery.** Words such as `carrier`, `file`, `dashboard`, `screen`, `front-end`, and `rendering` are recognition cues. First say what the carrier is being used for. If the next pattern is not already clear, use the compact category-to-contribution route in §4.1.3 for publication, evidence or currentness, generated results, framework packages, Work or reliance, architecture or structure, and base or support questions. Do not close on the word `carrier` alone.

#### C.2.P:4.1 - General Recovery Check

Run this check only after E.10 has left one C.2.P distinction unresolved.

1. **Name the sentence function.** State what the sentence would let a reader claim or do.
2. **Recover one blocking distinction.** Separate source expression, episteme, publication, bounded publication unit, carrier relation, source-to-use relation, or project-side use. Use A.6.P as a separate step only when the remaining problem is relation precision.
3. **Select the next result.** Rewrite directly, write the compact row, perform the full check under its material conditions, or return a non-use result. If another pattern now supplies the needed definition, constraint, or test, name that contribution and stop C.2.P.

Fail closed when the kind, relation, use, or remaining reader action cannot be recovered. A type-correct sentence that no longer shows the working situation or useful action is an incomplete rewrite.

##### C.2.P:4.1.1 - Slash Discipline
In conventional abbreviations, source titles, mathematical notations, standards, URLs, file paths, and ordinary notations, a slash can be part of an accepted designation rather than a hidden FPF kind. In FPF-facing episteme and publication ontology, a slash is still a recovery trigger before it is a synonym marker unless the mark is part of such accepted notation, carrier syntax, or conventional designation.

Before leaving a slash expression in current prose, classify the expression as one of these cases:
- accepted notation or conventional designation: a standard name, source name, discipline abbreviation, established compound name, formula, ratio, fraction, unit, path-like quoted source token, title, product name, file path, URL, or quoted source wording where the slash is part of the accepted designation or carrier syntax; keep `ISO/IEC`, `ISO/IEC/IEEE`, `1/2`, URLs, conventional abbreviations, and similar forms when the sentence uses them as notation;
- a plain-language synonym pair with no ontology, authority, evidence, or use-boundary claim;
- a lazy `and/or`-style join that must be split or recovered before FPF-governed use;
- a composite-kind candidate that needs `F.18` and `A.6.P` recovery;
- a relation claim that needs a `RelationKind`, a `QualifiedRelationRecord`, or a multi-term relation phrase with typed endpoints, slots, qualifiers, scope, time, and viewpoint;
- a tuple-like record that needs a named record kind and named slot semantics;
- a failed ontology signal where the sentence lists unlike values because the FPF kind under repair, relation record, relation phrase, tuple-like record, alternative-case disposition, or not-triggered disposition has not yet been recovered.

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
- **recovered by value:** the text now names the current `U.Episteme`, selected `EntityOfConcern`, `U.View`, publication form, generic publication face, MVPK face under E.17 constraints, `PublicationUnit`, carrier relation, relation record, relation phrase, tuple-like record, FPF pattern, document named for source, evidence, architecture, or review use, reviewed publication, review packet, review record, or review state, project-side FPF kind and reference named by value when `projectSideFPFRef` is current. The selected value is one current value, not the list: `C.11` `ChoiceResult`; `C.11` decision record; `A.6.A` action invitation; `A.15` `U.WorkPlan`; `A.15.1` dated `U.Work` occurrence; `U.Method`; `U.MethodDescription`; `A.20` constraint or adjudication decision record; `A.21` `GateDecision`; `A.21` `DecisionLogRef`; `A.10` evidence path; typed evidence record; `B.3` `AssuranceResult`; an engineering-justification result under its direct pattern; typed status record whose FPF status pattern is named; carrier relation; front-end relation; or not-triggered alternative;
- **understandable FPF extension candidate:** the thought is clear enough to state as a candidate new or amended FPF kind, pattern, relation record, method guidance, accepted `DRR` content decision, or campaign-scoped content question, but it does not carry current authority, evidence, or use-boundary claim until an accepted architecture decision, accepted `DRR`, or accepted FPF pattern supplies that authority;
- **source wording without FPF-governed use:** the phrase has no current authority, evidence, or use-boundary claim;
- **reduced-use cue:** the phrase is kept only as a recognition cue or anti-case, not as a claim-bearing architecture decision;
- **blocked use:** the phrase is blocked for claim-bearing architecture, pattern, or project text while the needed meaning, kind, or relation is missing.
- **rewrite incomplete:** the repaired wording may be kind-correct, but it does not yet state a remaining reader use, recognition reason, Tech-to-Plain mapping when both registers are current, or FPF pattern application, or a Plain or didactic line carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or use-boundary claim that cannot be recovered from the Tech interpretation; continue repair or demote to a non-use disposition before the text has FPF-governed use.

These dispositions are recovery results, not a meta-governance authority over all of `FPF`.
When recovery names another FPF kind, use the pattern that defines or constrains that kind, its declared use boundary, and its conformance checks.
`C.2.P` may identify that `A.10`, `A.15`, `A.15.4`, `A.20`, `A.21`, `B.3`, `C.11`, `F.9`, `E.17.EFP`, `E.17.ID.CR`, or another FPF pattern applies.
After that identification, `C.2.P` no longer defines or constrains the recovered kind.
`C.2.P` only makes the kind under repair, relation, and use boundary explicit enough to apply the appropriate pattern.

No other disposition is closed.
In particular, "seems to mean", "probably about", a cleaner paraphrase, or a broad umbrella replacement is not a successful recovery.

##### C.2.P:4.1.3 - Keep source, return, work, and next-pattern questions separate

When `source data` or `source material` is epistemic, identify the source expression and selected source episteme. Add a publication occurrence only when availability matters. Then name the relation or path that carries the source into the current use.

Treat `source-use` as a cue, not as a relation name. Do not call an endpoint `value` unless the direct pattern actually declares a value slot.

If the wording also makes a claim about a Method, Work, transformation, evaluation, transfer, or receiving use, use its direct pattern. Use `A.6.P.WMR` only while the work-side relation or what is being claimed about it remains hidden. Physical raw material stays with its constituent, resource-use, supply, transfer, or transformation relation.

Use `source-return` only for a reverse or escalation move from a derivative, coarsened, extracted, compressed, rendered, or reused object to a named source. Such a move is current when a stronger use, dispute, freshness change, hidden loss, or missing distinction requires the source again. For ordinary movement from a source into current use, say `source-to-use path` or name the actual relation. Name a rule-bearing ClaimGraph only when later comparison or reuse depends on the identity of that rule.

C.2.P does not decide whether Work may proceed. Use `A.15.4` only after the wording repair shows that a publication, display, or other appearance is being relied on as a reason for intended Work and the exact project-side object or relation is still unresolved. If the direct pattern is already known, use it without an intermediate reliance-repair branch.

Once the remaining question is clear, stop C.2.P and choose the direct branch:

- `A.6.P` for relation precision;
- `F.18` for a reusable name;
- `C.30.P` for a hidden architecture or structure distinction;
- `C.16.P` or `C.16.Q` for a hidden characteristic, scale, or evaluative-quality distinction;
- the applicable episteme or publication pattern for an already identified episteme or publication question.

These are alternatives, not a mandatory sequence. C.2.P may expose a naming or authority question, but it neither renames an accepted FPF pattern nor admits a reusable head; use `F.18` and the applicable accepted decision source for that change.

Carrier-like words are only recognition cues. Once the category is clear, use one row below and stop C.2.P as soon as that contribution closes the question.

| Recovered category | Use the contribution that answers the remaining question |
| --- | --- |
| Publication occurrence, form, face, presentation carrier, rendering, or availability | Use `E.17` to select a source-backed face for a named reader and use; use `E.24.PUB` when publication-occurrence identity, form, carrier, audience, bounded use, or availability matters. If the claim is that access actually occurred, use the pattern for that exact access relation; availability alone does not establish access. |
| Evidence, provenance, or currentness | Use `A.10` for one claim-bound evidence-provenance path and bounded reliance. Use `G.6` only when later citation or replay needs an addressable path through several already established objects and relations. Use `G.11` when staleness or refresh of a source, edition, evidence set, dashboard, or carrier is the live question. |
| Generated or discovered result reached through a carrier | Use `C.35` to decide whether the exact result may seed architecture work. Keep its publication occurrence and carrier under `E.17` or `E.24.PUB`; C.35 admits or rejects the result, not a generic "generated carrier". |
| FPF, DPF, or LPF edition, package carrier, or access carrier | Use `E.4.FPF` for FPF form and publication- or access-carrier assembly and `E.4.DPF` for DPF or LPF authoring and publication- or access-carrier assembly. Use `E.4.PFIP` only for accepted-source integration or predecessor-publication preservation, `E.4.PFR` only for a relation or edition maintenance claim, and `E.4.DPF.DA` only for whole-package adequacy. |
| Work or reliance prompted by a carrier or display | Use `A.15.2` for an identified WorkPlan and `A.15.1` for performed Work. Use `A.15` only while the system-role kind or assignment, Method, WorkPlan, and performed Work remain entangled. Use `A.15.4` only while the appearance hides the direct prerequisite for the intended Work or reliance use; once that prerequisite is known, use its direct evidence, gate, decision, permission, or assurance pattern. |
| Architecture or structure use | Use `C.30.P` while the architecture or structure claim is still hidden, `C.33` to test what selected structure a carrier or observation actually captures and what must return from source, and `C.34` only for a claimed correspondence or preservation between two exact structures. |
| Base or support wording | Use `A.6.6` only when the wording hides an actual basedness relation. Name the dependent, base, and direct predicate first and stop when that ordinary assertion answers the use. If the wording instead concerns evidence, assurance, or work enablement, use the pattern for that claim; leave navigation or ordinary help in ordinary language. |

#### C.2.P:4.2 - Core Glossary

##### C.2.P:4.2.0 - Cross-Side Fields That Must Stay Split

These fields are current episteme-publication precision vocabulary for `DRR`, architecture, and pattern-drafting work.
They exist to prevent one sentence from mixing FPF-side use-boundary, project-side records, actual work or action, method selection, carrier access, and authority records.
They are local recovery aids, not FPF kinds, not record kinds, and not a universal record ontology.
Each field closes only by naming the FPF kind named by value, relation record, relation phrase, project-side FPF kind and reference named by value, or explicit non-use disposition that is current in the sentence.
The same local-aid rule applies to neighboring field names such as `sourceRelationClass`, `explanationSourceRelationClass`, `comparativeRelationClass`, `representationValidityUseBoundaryValue`, `allowedUse`, `misuseRisk`, and `worldContactPolicy`: they help record a local recovery or reader-use boundary, but they do not become kinds. These local fields do not instantiate evidence, gate, assurance, work, commitment, speech act, decision, release, authority, representation kind, world-contact kind, or policy kind. Read `allowedUse` as a local reader-fit field under `declaredUseBoundary`, not as permission, evidence relation, or authority.

| Term | Current interpretation | Must not mean |
| --- | --- | --- |
| `FPF` as episteme | The whole `FPF` is a claim-bearing episteme with publications, parts, patterns, pattern sections, `DRR`s, and companion publications and documents named for source, evidence, architecture, or review use. | A file, repository, taxonomy, pattern-language metaphor, or packet-local summary by default. |
| FPF pattern | A named FPF pattern: a reusable episteme species that gives action guidance for a problem situation. It is applied in a current problem situation. | Any recurring arrangement, procedure, method call, route, cluster label, checklist, or document named only as a citation or source-finding pointer. |
| pattern section | Either a part of the pattern episteme or a bounded `PublicationUnit` of that pattern publication, depending on sentence function. State which one matters when the distinction carries a claim. | Independent pattern, file location, generic locus, or record with named authority-reference relation. |
| accepted campaign `DRR` | A campaign decision source that states accepted content decisions for one campaign. | A pattern, current-authority summary, open-ended plan, review log, or replacement for pattern text. |
| `relationClaimSlice` | Empty, or a local note that `A.6.P` relation precision is current for one sentence. It must name the relation problem being handled: relation, comparison, dependency, support, sameness, grounding, mapping, endpoint claim, or cross-context bridge claim. The recovery then names `RelationKind`, `QualifiedRelationRecord`, relation phrase, candidate-set note, or bridge card when current, with typed endpoints, slots, qualifiers, and scope. | Dictionary replacement, one new umbrella kind, a bare `RelationKind` standing in for a relation record, a generic relation slot, support relation by default, or a list left as the final answer. |
| `declaredUseBoundary` | The declared use boundary and blocked use outside that boundary when the sentence says what declared use boundary applies to a use, act, claim, or reliance. Use A.6.B when the boundary claim needs L-, A-, D-, and E-claim separation. | Generic supported use, permission-by-appearance, or visual cue or readability cue treated as use-boundary. |
| `projectSideFPFRef` | The project-side FPF kind and reference named by value when a publication, display, cue, or explanation is treated as a project-side source for work, evidence, gate, constraint, adjudication, decision, commitment, method, action invitation, assurance, or engineering justification. The field points to that kind and reference; use the relevant FPF pattern for the relation and its checks. | One slot accepting records, actions, methods, carriers, evidence, gates, decisions, assurance, and engineering justification interchangeably. |
| `rejectedOverread` | A local field naming the tempting interpretation, evidence, gate, work, permission, approval, commitment, release, safety-proof, engineering-justification, or pattern-entry interpretation that must not be granted by resemblance alone. It is valid only with the recovered relation or subject-specific source, scheme, scope, practice, or use that blocks it. It is not `U.Kind`, not a record kind, not a review-finding kind, and not a moralized defect class. | A general risk slogan, review finding, moralized "bad use", vague misuse label, or reusable FPF kind. |
| `useBoundaryTargetKind`, `useBoundaryTargetRef` | Source-local helper fields. Prefer `declaredUseBoundary`; if these fields appear in material being repaired, they name the kind and reference inside `declaredUseBoundary`, not an `A.6.P` relation slot. | A generic `supported use`, document capability, "claim outside the declared boundary", review permission, or untyped pattern assignment. |

##### C.2.P:4.2.1 - Episteme, Publication, and Carrier Distinctions

| Term | Current interpretation | Must not mean |
| --- | --- | --- |
| `U.Episteme` | Claim-bearing episteme or episteme species. Use when the value is a claim-bearing episteme that can be described, viewed, grounded, revised, published, or relied on under FPF. | File, paragraph, screen, carrier, status note, process state, or generic "content". |
| C.2.1 episteme constitution and neighboring relations | An exact episteme is identified through claim content, one exact EntityOfConcern, and one effective ReferenceScheme under `EpistemeConstitutionRelation`. Empirical grounding is a separate `EpistemeEmpiricalGroundingRelation`; describing-use viewpoint selection, E.17.0 conformance and same-individual `U.View` membership, C.29 representation, and publication or carrier relations are also separate. SlotKinds occur only inside the exact reusable `RelationSignature` that declares their participant meanings. | One universal episteme-slot tuple, card, field family, or context container. |
| `EntityOfConcern`, `EntityOfConcernRef` | The EntityOfConcern reference under `C.2.1` named by a claim-bearing episteme or episteme-lane `U.View`: entity, relation, FPF pattern, FPF publication, project episteme, project publication, project-side FPF kind and reference named by value, work or action when that work or action is itself the entity of concern, or another explicitly typed EntityOfConcern referent. Use this when the text is really about what the episteme is about. In publication-unit work, `EntityOfConcernRef` is used only through a claim-bearing episteme or episteme-lane `U.View`; it does not float as a free field on the unit. | Generic topic, local table subject, file title, reviewed publication, review packet, or review record, required project-side work, decision, action invitation, authoring work, or anything someone happens to talk about. |
| wording such as `describedEntity`, `DescribedEntityRef`, `primary described entity` | Use the exact EntityOfConcern participant and its applicable reference under C.2.1 when a claim-bearing episteme is current. Use `publicationUnitPrimaryEntityOfConcern` when one bounded `PublicationUnit` carries or exposes a claim-bearing episteme or same-individual `U.View` and the primary entity of concern must be named. | A second C.2.1 slot family, a free publication-unit field, a generic topic, a second current name, or a new ontology beside `EntityOfConcern`. |
| `publicationUnitPrimaryEntityOfConcern` | The primary entity of concern, non-claim-bearing kind named by value, topic, or subject that one bounded `PublicationUnit` is mainly about for the current use. When a claim-bearing episteme or episteme-lane `U.View` is current, this must be recoverable from the selected `EntityOfConcernRef`; otherwise name the non-claim-bearing kind named by value or keep topic and subject as plain explanatory prose. | `EntityOfConcernRef` created without a claim-bearing episteme or episteme-lane view, publication-unit title by default, authoring process, carrier identity, or reader interest. |
| `GroundingHolon`, empirical-grounding relation | The exact grounding holon and obtaining C.2.1 `EpistemeEmpiricalGroundingRelation` that maps named empirical claims of one exact episteme to the required direct observation, intervention, measurement, or test relations. | A constituent of episteme identity, a convenient source citation, an untyped entity mention, or the declaration-local `GroundingHolonSlot` used as the world-side value. |
| `U.View`, `U.EpistemeView` | Same-individual dependent membership of one already identified episteme when an exact E.17.0 `EpistemeViewpointConformanceRelation` to at least one exact viewpoint episteme obtains. A.6.3 source-to-receiving construction, describing-use viewpoint selection, publication, form, and carrier remain separate. An MVPK face can use this typing only under its exact E.17 constraints. | A UI view, reader viewpoint, screen, generic publication face, projection by default, or new claim-bearing episteme by membership alone. |
| `Viewpoint` | One exact `U.Viewpoint` episteme used as the viewpoint participant of an E.17.0 conformance relation or selected for one named describing use. Selection does not prove conformance or `U.View` membership. If source wording says “system in role,” use E.10.ROLE and recover the exact concern, object, local system-role kind, classification judgment, participant relation, or assigned System by value. | A reader opinion, episteme-identity slot, pattern-application order, publication label, carrier label, or assignment manufactured by the viewpoint phrase. |
| publication | A publishable episteme, view, record relation, act or occurrence of publishing, or publication form, depending on sentence function. Always split by kind before use. | Generic document, any public-looking file, or proof that a claim is authorized. |
| `U.EpistemePublication` (rejected spelling) | No durable kind. Recover the claim as the selected `U.Episteme`, an `EpistemePublicationRelation` occurrence or reference when availability matters, publication form, or `U.PresentationCarrier`, according to sentence function. The spelling may remain only in this rejection explanation or a negative test. | A positive object, kind, reference, field, publication identity, or carrier identity. |
| publication form | The typed form in which an episteme, view, or record is published. | The claim-bearing episteme itself, the face rendered for a reader, or the carrier holding bytes. |
| generic publication face | Reader-facing publication projection or face. It is not `U.View` by default; it becomes a view only when `E.17` or the applicable view pattern supplies that typing. | `U.View` by default, carrier, UI face, front-end display, MVPK face under E.17 constraints, or claim-bearing episteme. |
| MVPK face under E.17 constraints | `E.17` face published under MVPK constraints from a source episteme or episteme-lane view, publication viewpoint, scope, pins, and face kind. It may be a `U.EpistemeView` when the MVPK profile makes that typing current. | Generic publication face, carrier, UI face, front-end display, or proof of evidence, work, gate, or authority by presentation. |
| carrier, front-end, rendering | Publication-side or access-side bearer or display relation. Use `U.PresentationCarrier` under E.17 and E.24.PUB when that exact carrier is current; otherwise name the file carrier, transport carrier, rendering, front-end relation, access-carrier relation, or another carrier relation by sentence function. | Episteme identity, publication form, `U.View`, proof of evidence, or authority-reference relation. |
| `PublicationUnit` | `E.17.AUD`-cluster head for one bounded unit inside a publication that a person inspects as one unit: a pattern body, section, table, note, card, sheet, screen block, or another bounded publication unit whose boundary is named. A card, sheet, or screen block counts only when its boundary is inside a named publication or generic publication face and the sentence needs that bounded unit as the inspected publication unit. It is part of or bounded by the publication face that renders or locates it, whether that face is generic or published under E.17 and MVPK constraints. It may carry or expose a claim-bearing episteme, view, record, cue, or local rendered content when that carried value and relation are named, but it is not identical with the carried value. | Authoring process, review work, file, carrier, front-end, UI behavior, dashboard behavior or export behavior, whole publication architecture, `U.Episteme`, `U.View`, publication form, generic publication face, MVPK face under E.17 constraints, or "anything written". |
| project-side FPF kind and reference named by value | Evidence record, gate record, Work record, status record, commitment record, system-role-assignment record, decision record, selected source `U.Episteme`, `EpistemePublicationRelation` occurrence reference when availability matters, status-register entry, or another project record whose FPF kind is named. | Semantic content in general, current process state, or a free-form note. |
| source document | A document named for source-use, evidence use, architecture use, or review use. Name that document use directly. | A governing source by folder proximity, the EntityOfConcern carried or exposed by that source document, or the authority-reference relation unless that relation is explicit. |
| reviewed publication, review packet, or review record | The reviewed publication named by value, review packet, review record, or bounded publication unit sent or inspected in review. | The EntityOfConcern carried or exposed by that reviewed publication, review packet, or review record, the source relation behind it, or a packet-local summary. |

##### C.2.P:4.2.2 - Trigger Boundary

Use `E.10:0.2`, `E.10:0.2a`, `E.10:0.2b`, `E.10:0.2c`, and `E.10:0.2d` for lexical trigger scanning and selection of an already known applicable pattern.

This pattern is applicable after that scan only when one C.2.P-specific source-expression, episteme, publication, carrier, source-to-use, or use-disposition distinction is still needed to select or safely use the direct receiving pattern. When the exact pattern and current field are already recoverable, apply it directly.

When this pattern is applicable, do not restart from word taste. Keep the `E.10` trigger result as input and recover source-expression clarification, FPF-governed use, current episteme-publication relation set, use disposition, and remaining reader use.

#### C.2.P:4.3 - Current Preferred Vocabulary
Use `PublicationUnit` when the intended entity is a bounded, human-inspected unit inside a publication.
Do not use it for UI behavior, carrier behavior, front-end behavior, file identity, dashboard behavior, or export behavior; use `A.7`, specific carrier or front-end wording, or the applicable named FPF pattern instead.

Use the current cluster names directly: `PublicationUnit Stability Discipline`, `Local Head Restoration`, and `PublicationUnit Primary EntityOfConcern Discipline`.
When the current entity is a bounded unit inside a publication, use `PublicationUnit`; when the current entity is authoring or editing work, name that work directly.

Use EntityOfConcern, EntityOfConcernRef, and publicationUnitPrimaryEntityOfConcern when local wording means the EntityOfConcern named by a claim-bearing episteme or episteme-lane view, or the primary entity of concern stabilized by one bounded publication unit over that carried value.

For `describedEntity`, `DescribedEntityRef`, `primary described entity`, `EntityOfInterest`, or `EoIClass`, use the exact EntityOfConcern participant, its applicable `entityOfConcernRef` or `EntityOfConcernRef`, `EntityOfConcernChangeMode`, `EntityOfConcernClass`, `publicationUnitPrimaryEntityOfConcern`, or the local FPF kind named by value. Use `EntityOfConcernSlot` only while inspecting the exact reusable C.2.1 constitution `RelationSignature`; it is not an episteme field. If no claim-bearing episteme or same-individual `U.View` is current, use a non-claim-bearing kind named by value or plain `topic` or `subject` instead of inventing an `EntityOfConcernRef`.

Use ordinary `topic`, `subject`, or `local referent` only in non-normative explanatory prose where no episteme constitution or neighboring direct relation, publication construction, or authority relation is being asserted.

Do not mint any other reusable FPF name from this pattern alone. The `E.17.AUD` cluster **PublicationUnit Stability Discipline** defines and constrains `PublicationUnit`; this pattern only recovers bounded-publication-unit wording into that head and points to the cluster for its tests. FPF-governed uses keep the nearby definition or explicit publication relation set.

##### C.2.P:4.3.1 - `PublicationUnit` use and non-use boundary

`PublicationUnit` means one named, bounded unit inside a publication that a person inspects as one unit: for example, one pattern body, section, table, note, card, sheet, or screen block inside that publication.

Use it when the unit boundary matters to authoring, review, navigation, or a claim about what that bounded unit exposes. Do not use it for the underlying episteme, a view, publication form, whole publication, carrier, file, interface behavior, dashboard behavior, authoring Work, or review process. Name those objects and relations directly.

The bounded unit may carry or expose claim-bearing content, but it is not identical with that content. `PublicationUnit` keeps the inspected publication-side boundary visible without mixing the unit with authoring action or reader action.

#### C.2.P:4.4 - Epistemic Precision Restoration After E.10

Keep the E.10 result as input. Apply C.2.P only while a source-expression, episteme, publication, carrier, or use-disposition distinction is still needed to select or safely use the direct receiving pattern. If the exact pattern and field are already known, apply them directly.

#### C.2.P:4.5 - Rewrite execution modes

##### C.2.P:4.5.1 - Direct repair

Use this mode for the ordinary case. Rewrite the sentence and state one plain reason or non-use boundary. No row or note is required.

Example result: “The note helps the reader find section 4.2.” Reason: this is navigation, not evidence or assurance. Stop.

##### C.2.P:4.5.2 - Compact row

Use the five-field row in 4.0a when the recovered distinction must remain inspectable. Add only the optional fact that changes the current claim.

##### C.2.P:4.5.3 - Full check

Use a full check only when:

- several unresolved fields interact;
- the source-to-FPF use is contested; or
- a reusable ontological or naming decision is being made.

The full check records the exact span and function, competing readings, selected kinds and relations, direct pattern contributions, rejected overreads, final wording, remaining reader use, and reopen condition. It is not required because the text is an FPF pattern or because a source is cited.

##### C.2.P:4.5.4 - Publishing the compact row as a local note

When the five-field compact row must remain beside the repaired text, publish that same row as a local note. This changes only its presentation: it adds no fourth execution mode, no extra required field, and no durable FPF record kind.

#### C.2.P:4.6 - Completion and reopen boundary

The application is complete when the smallest selected product:

1. preserves the E.10 result rather than restarting from word taste;
2. names the recovered kind, relation, or non-use disposition;
3. hands any remaining relation, naming, publication, evidence, work, decision, or assurance claim to its exact pattern;
4. leaves the reader a clear action or stop condition.

Reopen when a replacement head hides another umbrella, a later use adds a material field, the direct receiving pattern changes, or the repair becomes technically exact but hard to use.

Also reopen when an entry cue, summary, dashboard, retrieval snippet, or source note still carries the pre-repair reading. Do not reopen merely because a larger form could be filled.

