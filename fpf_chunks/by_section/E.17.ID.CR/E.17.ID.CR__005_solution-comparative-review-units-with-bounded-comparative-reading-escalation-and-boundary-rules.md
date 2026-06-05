---
chunk_kind: "child"
pattern_id: "E.17.ID.CR"
pattern_title: "ComparativeReading — bounded comparative reading over comparative review units"
section_id: "E.17.ID.CR:4"
section_title: "Solution - comparative review units with bounded comparative reading, escalation, and boundary rules"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.ID.CR/E.17.ID.CR__005_solution-comparative-review-units-with-bounded-comparative-reading-escalation-and-boundary-rules.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "E.17.ID.CR — ComparativeReading — bounded comparative reading over comparative review units"
  - "E.17.ID.CR:4 — Solution - comparative review units with bounded comparative reading, escalation, and boundary rules"
line_start: 63992
line_end: 64329
dependencies:
  - "A.15"
  - "A.15.4"
  - "A.16.0"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.9"
  - "A.6.P"
  - "B.5.2"
  - "B.5.2.0"
  - "C.11"
  - "C.2.2a"
  - "E.14"
  - "E.17.AUD.LHR"
  - "E.17.AUD.OOTD"
  - "E.17.EFP"
  - "F.9"
  - "F.9.1"
keywords:
---

### E.17.ID.CR:4 - Solution - comparative review units with bounded comparative reading, escalation, and boundary rules

#### E.17.ID.CR:4.1 - Engineer-manager-first working use, comparison-unit distinction, and compact specialization definition

The solution opening here follows `E.17.ID.CR:4.3`'s working-model-first discipline.
A solution-side reader first meets the engineer-manager working use and the comparison-unit distinction, then the compact `ComparativeReading` definition that names the formal comparative read.
That order keeps the governing pattern explicit without making the compact definition a substitute for the working review moment.

#### E.17.ID.CR:4.1.a - Engineer-manager-first use

In plain working terms, this pattern is for a review unit that says something like:
- `this option write-up foregrounds integration pressure more than that one`;
- `these two available source epistemes or source publications are useful together, but they are not yet equivalent`;
- `this dashboard view helps triage one contrastive question, but it is not yet a release decision or a root-cause claim`;
- `this research synthesis foregrounds uncertainty more than that one, but it is not yet a method choice`;
- `this program brief foregrounds continuity risk more than that one, but it is not yet a funding decision`.

If that sounds like the review unit you need, keep the comparison unit bounded this way.
If instead you are mainly restating source epistemes or source publications, explaining them, opening a new abductive prompt or action-selection question, changing the EntityOfConcern, or making a decision, handle that live work under the FPF pattern or governing FPF pattern and exact project-side FPF kind and reference before the comparison unit carries the claim.

#### E.17.ID.CR:4.1.b - Pattern, case, and comparison-unit distinction

This pattern presents the `ComparativeReading` as the active governing pattern inside the broader `InterpretationDiscipline` family.
The family name marks the wider interpretation zone.
The governing pattern here is narrower and more concrete than interpretation-in-general.
It works over one **comparative review unit** and only the **bounded comparative reading** carried by that unit.
The wider review or decision work remains outside the pattern except where neighboring-work boundary or authority limits are needed.

The kind stack should therefore be read explicitly:
- family name = `InterpretationDiscipline` as the wider naming-level family;
- family-level move class = bounded interpretation work at that wider level;
- governing pattern = `ComparativeReading`;
- comparison unit = the bounded comparative review unit;
- comparative move = bounded comparative reading over already available source epistemes or source publications;
- wider work = the broader review or decision process that still sits outside this pattern.

The family name is only a naming aid for this specialization. It is not a `U.Kind`, `publication-face kind`, publication face, authority reference, or governing-pattern reference; when a record needs a governing pattern, cite `E.17.ID.CR ComparativeReading` or the more exact neighboring pattern.

In ordinary use the bounded comparative review unit may appear as a short comparison note, comparison sheet, guided review aid, or guided comparative UI.
Those are admissible unit forms, not rival comparison units.

This distinction matters because the pattern is not governing reading as such in the abstract and it is not governing the whole review or decision work.
It is governing a small, reviewable unit that carries one bounded comparative lift over already available source epistemes or source publications.
The pattern does not create a new practical publication-unit family of its own; it tells when such a comparative review unit can stay modest and when a downstream claim or effect or decision-bearing record already belongs to another exact neighboring pattern.

##### E.17.ID.CR:4.1.b.a - Compact specialization definition

> `ComparativeReading` is the active governing pattern inside the `InterpretationDiscipline` family.
>
> It governs one comparative review unit over already available, source-pinned epistemes or source-pinned publications and carries one bounded comparative reading, or a small set of bounded contrast rows, over that unit.
>
> It stays admissible only while the case preserves the shared review frame, keeps distinct alternatives distinct unless bridge or substitution relation exists elsewhere, keeps the source references visible, keeps the added comparative lift bounded, and does not turn into same-entity viewing, bridge claims, explanation-face governance, prompt-bearing abductive work, ontology-facing reframing, retargeting, or downstream work or reliance authority.

Read this blockquote as the compact governing-pattern reminder.
It should stay nearby and early, but not stand in front of the engineer-manager-first use block or the comparison-unit distinction that working readers need first.

#### E.17.ID.CR:4.1.c - Why the comparative-reading specialization needs its own discipline

Teams already produce small comparative review units, often as comparison notes, comparison sheets, or guided review aids, that are more committed than a plain bridge-stance overlay over an existing Bridge Card but still below action selection, ontology reframing, retargeting, or approval guidance.
Leaving that middle band unnamed creates two opposite failures: one reader dismisses the review unit as harmless prose, while another over-reads it as if it already carried substitution, action-selection pressure, or action authority.

This pattern gives teams a narrow way to prepare, share, and inspect that comparative review unit without smuggling a downstream claim or effect beyond what the source, bridge stance, and bounded use can honestly carry.

#### E.17.ID.CR:4.1.d - Local working vocabulary

This pattern uses a small local vocabulary for review.
- **Comparative review unit** = a lightweight review unit such as a short comparison note, small comparison sheet, guided review aid, or guided comparative UI whose explicit job is one bounded comparative reading or a small set of bounded contrast rows under one shared review frame.
- **Base governing case** = the primary source relation, pattern-governing case, or project work question that is already live before bounded comparative reading is added.
- **Reviewed source episteme or source publication** = the already pinned or otherwise reviewable source episteme or source publication being comparatively read; in plain terms, the already available source episteme or source publication under review.
- **Source references** = `sourceAnchorSet` or `sourceRefs` that make the interpreted source episteme or source publication inspectable.
- **Shared review frame** = the review target, described situation, decision situation, release candidate, method family, control scope, problem frame, or source-set reference that remains preserved while the comparison is made.
- **Compared alternative** = one distinct option, method, bulletin, strategy, note, view, source episteme, source publication, or exact project-side FPF kind and reference kept separate under the shared review frame.
- **Same `EntityOfConcernRef` case** = the special case where the compared sources describe the same entity. This is common, but it is not required when distinct alternatives remain under one shared review frame.
- **Interpretive lift** = the bounded comparative or asymmetry-bearing reading added on top of already available source epistemes or source publications; in a small comparison sheet, each row has its own declared comparison basis while the unit keeps one shared unsupported downstream claim or effect and boundary trigger.
- **Bridge Card reference** = required `bridgeCardRef` when the case depends on bridge-mediated correspondence rather than ordinary source reading alone; optional `bridgeStanceRef` may qualify that bridge only after the bridge card exists.
- **Allowed use** = what this review unit may be used for while it remains only a bounded comparative review unit.
- **Misuse risk** = how the review unit is most likely to be over-read into a bridge, action-selection, ontology, or authority claim that it does not carry.
- **Prompt boundary** = the explicit `U.AbductivePrompt` publication that becomes the governing publication when abductive-prompt or action-selection claim becomes live.
- **Ordinary minimum block** = the smallest ordinary record that keeps the review unit honest for working use.
- **Load-bearing extension** = the fuller declaration record used when the case sits close to bridge, explanation, abductive, ontology, or authority boundaries.

These terms are local review aids. They inherit the `E.17:5.1e` local-field rule: they do not create `U.Kind`, `publication-face kind`, `RelationKind`, `KindBridge`, `EvidenceKind`, `GateDecision`, `SpeechAct`, `Commitment`, `U.Work`, `authoritySourceRef` target, publication face, or exact project-side FPF kind and reference unless another governing FPF pattern explicitly instantiates that object.
They do not replace source notes, bridge cards, explanation renderings, prompt publications, or gate-bearing source forms.
Their role is to keep a bounded comparative review unit readable without silently upgrading its authority.

#### E.17.ID.CR:4.2 - Scope and exclusions

**In scope**
- bounded comparative asymmetry over already declared reviewed source epistemes or source publications;
- reader-facing interpretive caution that stays source-tethered and preserves the shared review frame;
- comparison of distinct alternatives under one shared review target, described situation, release candidate, method family, control scope, problem frame, or source-set reference;
- comparative review units that answer one explicit contrastive question without opening a rival action-selection search;
- bounded user-fit when that fit only limits use rather than widening authority.

**Out of scope**
- same-entity restatement, conservative rewrite, or representation shift whose main question stays with `A.6.3`, `A.6.3.CR`, or `A.6.3.RT`;
- bridge-stance overlay that only clarifies an already-declared bridge stance over an existing Bridge Card (`F.9.1`);
- explanation-face use discipline, admissibility, or added-link review on existing faces (`E.17.EFP`);
- abductive-prompt or action-selection cases (`B.5.2.0` or `B.5.2`);
- ontology-facing reframing or changed EntityOfConcern (`OntologicalReframing` or `A.6.4`);
- policy, gate, adjudication, assurance, or work-facing use (`A.15`, `A.20`, or `A.21`).

#### E.17.ID.CR:4.2.a - Working-fit test

Use this discipline only when all of the following hold:
1. the reviewed source episteme or source publication is already pinned or otherwise reviewable;
2. the review unit adds one bounded comparative or interpretive lift, or a small set of bounded contrast rows with row-level comparison bases;
3. the case is still answering a bounded contrastive question rather than selecting an action;
4. the shared review frame stays preserved, and compared alternatives remain distinct unless an explicit bridge or substitution source supplies equivalence, substitution, or another named relation between them;
5. the main question is not already better described as same-entity viewing, bridge-stance overlay over an existing Bridge Card, or explanation-face use discipline.

If any of those fail, handle the live work under the neighboring FPF pattern and exact project-side FPF kind and reference that actually govern it.

#### E.17.ID.CR:4.2.b - Nearest neighboring work

Name the base source relation or work question before adding bounded comparative reading.
The nearest neighboring work questions should be separated in this order:
1. **Same-entity rewrite or representation shift.** If the project move is still mainly restatement, representation shift, or another same-entity viewing transform, keep it with `A.6.3`, `A.6.3.CR`, or `A.6.3.RT`.
2. **Bridge-stance clarification.** If the review unit only makes an already-declared bridge stance more legible, it stays subordinate to `F.9.1`.
3. **Explanation-face use.** If the main question is explanation class, face admissibility, or bounded connective prose on an existing face, it stays with `E.17.EFP`.
4. **Abductive prompt or action-selection pressure.** If open-question pressure or action-selection pursuit becomes live, bounded comparative reading ends and `B.5.2.0` or `B.5.2` governs that work.
5. **Changed EntityOfConcern or decision-bearing use.** If continuity witnesses, changed target, decision-bearing consequence, gate, approval, rollout, release, policy, assurance, or adjudication use is needed, the case has already left this discipline for `OntologicalReframing`, `A.6.4`, `A.15`, `A.20`, `A.21`, or another exact governing FPF pattern and exact project-side FPF kind and reference.

#### E.17.ID.CR:4.3 - Working-model first; plain questions first, ordinary minimum second, full declaration third

Most working users should not have to start with a long declaration block.
This pattern therefore follows `E.14`'s working-model-first discipline: the first usable block is a small set of plain questions that helps an engineer-manager keep the review unit bounded to the work it can honestly carry.
The opening of `E.17.ID.CR:4.1` follows that same order by value: engineer-manager working use and comparison-unit distinction come first, and the compact `ComparativeReading` definition stays nearby as a recovery reference rather than a gate before use.
The ordinary minimum block comes next for ordinary use.
The full declaration block remains available as a load-bearing assurance record.

#### E.17.ID.CR:4.3.a - Five plain working questions

The near-top quick working-fit check is the canonical first working block for this pattern.
A working user should be able to answer these same five questions before touching the fuller blocks:
1. What already available source epistemes or source publications am I comparing?
2. What single contrast or small set of contrast rows am I trying to make visible?
3. Am I still inside the same shared review frame, with compared alternatives kept distinct when they are distinct, or has the review target already shifted?
4. What unsupported downstream reading must the team not take from this review unit?
5. What would force this review unit to leave `ComparativeReading` for explanation, bridge work, prompt work, ontology work, or decision authority?

If these five answers are not visible, the case is not ready to stay here as a bounded comparative review unit.

#### E.17.ID.CR:4.3.b - Ordinary minimum block

For ordinary bounded comparative review units, it is usually enough that the unit or its surrounding review context keeps explicit:
- what reviewed source episteme or source publication is being interpreted;
- where the source references live;
- that the shared review frame remains preserved and that distinct alternatives remain distinct unless another source supplies bridge or substitution relation;
- what exact bounded comparative lift is being added, or which bounded contrast rows are included and what comparison basis each row uses;
- what downstream claim or effect remains unsupported;
- that the default `worldContactPolicy` here is review-only and non-executive;
- and what neighboring FPF pattern becomes mandatory if the case crosses that neighboring boundary.

If those minimum answers cannot stay stable across the same note, sheet, or review aid without sliding between reviewed source episteme or source publication, bounded comparative review unit, bounded lift, and outside work, stop here. Repair local lexical-head kind pressure through `E.17.AUD.LHR` (`Local Head Restoration`); if the whole review unit still has unstable EntityOfConcern or carried-move reading after that repair, apply `E.17.AUD.OOTD` (`PublicationUnit Primary EntityOfConcern Discipline`) before adding more declaration weight.

##### E.17.ID.CR:4.3.b.a - Ordinary working card

An admissible ordinary comparative review unit should normally let a reader recover these seven rows without opening the heavier fuller declaration:

| Row | Plain question | Minimum answer |
| --- | --- | --- |
| **Reviewed source** | What already available source epistemes or source publications are being compared? | one pinned source slice, one explicit source pair, or one explicit source set |
| **Source references** | Where can a reviewer inspect that source episteme or source publication? | visible `sourceAnchorSet` or nearby `sourceRefs` |
| **Shared review frame and alternative identities** | What review target, described situation, or source-set reference is preserved, and what alternatives remain distinct under it? | preserved shared review frame; distinct alternatives are not treated as equivalent or substitutable without bridge relation |
| **Bounded lift row(s)** | What single contrast or small row set is this unit making visible? | one declared `comparisonBasis` or a small set of row-level `comparisonBasis` statements under one shared unsupported downstream claim or effect and boundary trigger |
| **Unsupported downstream claim or effect** | What is this unit not yet claiming? | no equivalence, prompt opening, ontology change, or decision authority |
| **World-contact limit** | What may the unit not be used to do? | `review-only and non-executive` |
| **Boundary trigger** | What would end this pattern and require another governing pattern? | one explicit bridge, explanation, prompt, ontology, or authority trigger |

This working card may live inline in the comparative review unit or in its immediate review context.
Read it as the ordinary recovery reference for the near-top working-fit check:
- if rows 1-4 are still unstable because one pressured local lexical head or qualifier is doing too much work, stop and repair that local lexical-head pressure through `E.17.AUD.LHR` (`Local Head Restoration`) before you keep building the comparative review unit here;
- if rows 3-7 cannot stay stable because the same review unit still has unstable reviewed-source, comparative-move, or outside-work reading after one honest local repair, apply `E.17.AUD.OOTD` (`PublicationUnit Primary EntityOfConcern Discipline`);
- if rows 1-7 stay recoverable over one pinned source slice or source pair, one preserved shared review frame, distinct alternatives where present, and one bounded contrast or small row set, `ComparativeReading` remains the honest primary governing pattern.

The nearest stay-here worked slices for this reading are `E.17.ID.CR:5.4.5` through `E.17.ID.CR:5.4.6.b`.
The nearest stop-and-reopen worked slice is `E.17.ID.CR:5.4.6.c`.

Move to the load-bearing extension only when one of the boundary, reader-fit, or misuse conditions in `E.17.ID.CR:4.3.c` becomes true.
`ComparativeReading` remains primary only while those seven rows stay recoverable and the same review unit is still mainly about one bounded comparative reading, or a small set of bounded contrast rows, over already pinned source epistemes or source publications. If the review unit first needs to restabilize what it is about, what move it carries, and what wider work remains outside, use `E.17.AUD.OOTD` (`PublicationUnit Primary EntityOfConcern Discipline`) to stabilize that `PublicationUnit` question before adding more declaration weight here.

#### E.17.ID.CR:4.3.c - Load-bearing extension guidance

A fuller declaration record becomes warranted when:
- reader-fit is doing real work;
- misuse risk is high;
- the review unit sits close to viewing, bridge, explanation, abductive-prompt, ontology-shift, policy, assurance, gate, release, action-selection, or adjudication boundaries;
- mixed composition with `A.6.3.*` or `E.17.EFP` is load-bearing;
- the publication unit still has unstable EntityOfConcern, carried-move, or outside-work reading after local repair;
- or the case would otherwise be too easy to over-read as more committed than a bounded comparative review unit.

The load-bearing extension may inherit already-declared case ids, source pins, and provenance references instead of restating them inline.
When recorded as a load-bearing review unit, that extension normally captures the ordinary minimum block plus any neighboring-pattern fields that remain load-bearing for the mixed case.
Do not answer `PublicationUnit` instability by stacking more local fields onto the load-bearing extension. If `E.17.AUD.LHR` (`Local Head Restoration`) has already repaired the local lexical-head pressure and the same review unit still has unstable reviewed-source, publication-unit, comparative-move, or outside-work reading, stabilize that `PublicationUnit` question with `E.17.AUD.OOTD` (`PublicationUnit Primary EntityOfConcern Discipline`) before deciding how much declaration weight should stay here.

#### E.17.ID.CR:4.3.d - Load-bearing declaration block

When the heavier declaration weight really stays here, the unit should still make at least these fields recoverable:
- `sourceRelationClass` using the shared `E.17:5.1b` vocabulary when the comparison depends on source pointer, source availability or retrieval, source use, source faithfulness, claim recoverability, contradiction, omission, claim widening, added linkage, independent verification, admissible use, forbidden downstream use, or reopen trigger;
- `sourceAnchorSet` or `sourceRefs`;
- `comparativeRelationClass = sameEntityComparisonClass | sharedFrameDistinctAlternativeClass | readerFitComparativeClass`;
- `comparisonBasis`;
- `addedClaimPolicy`;
- `bridgeStanceVisibility`;
- required `bridgeCardRef` plus optional `bridgeStanceRef` when the case depends on bridge-mediated comparative relation;
- `targetUserModel` when reader-fit is materially shaping the reading;
- `interactionMode` when the review unit is not just one static comparative sentence;
- `contrastiveQuestion` when the case is answering a specific contrast;
- `allowedUse`;
- `misuseRisk`;
- `promptWorthinessThreshold`;
- `ontologyBoundaryTrigger`;
- `worldContactPolicy`;
- `downstreamAuthorityLimit`;
- `baseCasePattern` when the review unit is a mixed case layered over `A.6.3.*` or `E.17.EFP`.

`sourceRelationClass` is only source-relation or claim-admissibility class for the local claim or use. `comparativeRelationClass` is only the comparative-relation class of this review unit. Neither field is a `RelationKind`, `KindBridge`, Bridge Card, bridge relation, bridge stance, semantic identity, equivalence, substitution, evidence relation, gate decision, assurance claim, work relation, commitment, speech act, authority-reference relation, or decision record. The `sameEntityComparisonClass` value is a special case for comparisons where the compared sources really describe the same entity; it does not assert semantic identity. When the unit compares distinct alternatives, use `sharedFrameDistinctAlternativeClass` plus distinct alternative refs, and do not treat the alternatives as equivalent or substitutable without bridge relation.
`readerFitComparativeClass` by itself does not open interpretation. Bounded correspondence wording that starts implying bridge relation is bridge-mediated comparative relation: it requires an explicit `bridgeCardRef`, or the case applies `F.9` or `F.9.1` before the comparison unit can carry that bridge-mediated source relation. When cross-context bridge semantics are live, the actual bridge kind and Bridge Card remain governed by `F.9`. If bridge-mediated reading is live, `bridgeCardRef` is required and any `bridgeStanceRef` remains optional and subordinate.
The main comparison question plus the neighboring pattern boundaries still decide the selected FPF pattern or exact project-side FPF kind and reference.

#### E.17.ID.CR:4.3.e - Interpretant-side block

The interpretant-side fields above do not turn this zone into a full interactive explanation system or a dialog-management system.
Their current role is narrower:
- keep bounded comparative reading from pretending it is audience-neutral when it is not;
- make the contrastive question, guided review mode, and allowed use visible;
- and stop interpretation prose from quietly becoming prompt-bearing guidance, assurance shorthand, or policy pressure.

#### E.17.ID.CR:4.3.f - Static note versus interactive aid

Use two comparison-relation forms.

1. **Static comparative review note.** A static note, sheet, or short review unit normally needs only the reviewed source episteme or source publication set, source references, `E.17:5.1b` source-relation class when source relation is disputed, comparison basis, bounded lift, unsupported downstream claim or effect, world-contact limit, and boundary trigger. Do not import interactive-explanation vocabulary into this ordinary case.
2. **Interactive comparative aid.** Add `targetUserModel`, `interactionMode`, state or history needed for the live comparison, `misuseRisk`, and admissible-use boundary only when the aid is actually interactive, stateful, adaptive, or user-model-bearing. These fields still do not authorize prompt selection, action selection, gate use, work or reliance, or approval; they only keep the interactive comparative aid from being mistaken for audience-neutral static prose.

A comparative review unit may expose or cite source epistemes, source publications, or exact project-side FPF kinds and references being compared. It does not become those source epistemes, source publications, exact project-side FPF kinds and references, a bridge card, a gate decision, or a work or reliance source by table layout, fluent contrast, side-by-side placement, or guided-review reuse. If the required source relation is missing, the repair request or source-gap note is prospective only; it does not backdate a source relation into the earlier comparison.

**Comparative-reading identity over revision.** A revised comparison table, regenerated comparison note, or updated guided review aid is not the same comparative reading merely because the layout, title, or compared-source family stayed familiar. If new source input, revised source references, changed comparison basis, changed shared review frame, or changed unsupported downstream claim or effect is live, publish the preserved comparative frame and the changed claims, or treat the result as a new comparative review unit before it is used for recommendation, selection, decision, gate, bridge, work, or reliance claims.

#### E.17.ID.CR:4.3.g - Representation ontology and modeling lens (informative)

The early canonical lens for this pattern is already stated near the top: one comparative review unit over already available, source-pinned epistemes or source-pinned publications, with the shared review frame preserved, one bounded contrast or small row set made visible, and unsupported downstream claim or effect kept outside.

This informative note only unpacks that same lens. It does not introduce a second one.

This pattern does not model interpretation in general.
It models the `ComparativeReading` as the active governing pattern inside the broader `InterpretationDiscipline` family.
In plain terms, the pattern works over the review unit itself.
That unit may appear as a comparison note, comparison sheet, or guided review aid, but it is not the whole review process, it is not the source system, and it is not the hidden act of reading in the abstract.
The bounded comparative reading is the interpretive lift carried by that review unit.

The minimum typed lens is a compact record of:
- source references and source relation;
- one declared source-relation class;
- one declared comparison basis and added-claim policy;
- one allowed-use boundary, one misuse-risk line, and one `worldContactPolicy` that remains subordinate to `A.20` or `A.21` when gate or adjudication claim appears;
- the relevant prompt, ontology, and authority boundary triggers;
- and which neighboring pattern still governs the base case when this remains a mixed overlay.

That lens is intentionally modest.
It keeps the main read tied to the review unit and the problem-owning review domain, while leaving source, continuity, and boundary discipline under whichever neighboring pattern still governs the base case.
This pattern therefore does not create a rival bridge taxonomy, a rival base-case discipline, or a publication with named authority-reference relation of its own.

#### E.17.ID.CR:4.3.h - Working read-out

A working reader should be able to say, in one short paragraph:
- what reviewed source episteme or source publication is being comparatively read;
- what bounded interpretive lift is being added;
- what shared review frame remains preserved, and, in the special same-EntityOfConcern case, why the same `EntityOfConcernRef` remains preserved;
- which neighboring pattern carrying bridge, prompt, ontology, action, gate, adjudication, authority, or downstream claim is still not yet active;
- and what neighboring-pattern boundary would become mandatory if the case were read as carrying a bridge, prompt, ontology, action, gate, adjudication, authority, or downstream claim.

If that read-out becomes fuzzy, the review unit is no longer bounded enough to stay here and should be narrowed, clarified, or moved under the governing neighboring pattern.

#### E.17.ID.CR:4.4 - Branch-discipline summary

This section is the compact governing-rule summary for `ComparativeReading` inside the Core.
It keeps the ComparativeReading governing rule recoverable for ordinary users and engineer-manager-first review.
In mixed cases, the neighboring pattern discipline still remains primary where the base case really belongs to `A.6.3.*`, `F.9.1`, or `E.17.EFP`.

Use the fuller solution, boundary table, worked slices, and relations section here when exact clause wording, full field set, or full reopen conditions matter.
Keep this pattern to these summary rules.

1. **Preserve the shared review frame.**
   Keep the review target, described situation, decision situation, release candidate, method family, control scope, problem frame, or source-set reference visible; keep distinct alternatives distinct unless bridge or substitution relation exists elsewhere; keep source references and one declared comparison basis per contrast row visible; keep `contrastiveQuestion` explicit when it is doing real review work.
2. **Keep the lift bounded and comparative.**
   The review unit may add a bounded comparative or asymmetry-bearing reading, but it may not quietly intensify into theory claim, bridge licence, prompt-opening pressure, explanation governance, ontology shift, or a decision, gate, action, approval, rollout, release, policy, assurance, adjudication, bridge, prompt, or ontology-shift claim.
3. **Name the base source relation or work question.**
   If the main question is really same-entity rewrite, bridge-stance overlay over an existing Bridge Card, explanation-face work, prompt opening, ontology reframing, retargeting, or a decision, gate, action, approval, rollout, release, policy, assurance, adjudication, bridge, prompt, or ontology-shift claim, this pattern should not stay primary.
4. **Keep neighboring patterns for downstream claims explicit.**
   Bridge-mediated comparative relation still requires explicit `bridgeCardRef`; optional `bridgeStanceRef` may qualify only an existing bridge card. Prompt-worthy cases publish `U.AbductivePrompt`; ontology-shift claims apply `OntologicalReframing` or `A.6.4`; action, gate, or adjudication use applies `A.15`, `A.20`, `A.21`, or another exact governing FPF pattern and exact project-side FPF kind and reference. If the primary question is reduced-use source rendering rather than bounded comparison, apply `A.6.3.CSC Controlled Semantic Coarsening`.
5. **Keep reader-fit bounded.**
   `targetUserModel`, `interactionMode`, `contrastiveQuestion`, `allowedUse`, and `misuseRisk` may be stated when they are doing real work, but they do not authorize coaching, prompt selection, action selection, policy guidance, or an authority claim that the unit does not carry.

#### E.17.ID.CR:4.5 - Neighboring-work boundary glance

This table is a compact boundary aid for separating the comparative review unit from neighboring project work and source requirements.
For a fuller mixed-case read, read this table together with the neighboring pattern discipline.

| If the case is really doing this... | It should stay here or move elsewhere... |
| --- | --- |
| one local lexical head or qualifier is still doing too much work, but one honest repair would stabilize the same unit | `E.17.AUD.LHR` (`Local Head Restoration`) |
| the same note is mostly rewriting, reframing, or re-rendering the same EntityOfConcern with no bounded comparative lift | `A.6.3`, `A.6.3.CR`, or `A.6.3.RT` |
| the real job is only to make an already-declared bridge stance explicit over an existing Bridge Card | `F.9.1` |
| the comparison wording is now making a relation-precision claim between compared items | `A.6.P` |
| the comparison wording is now making sameness, equivalence, alignment, mapping, substitution, or cross-context bridge relation | Part F with `A.6.9`, `F.9`, or `F.9.1` |
| the note is primarily a reduced-use source-pinned rendering with narrower-use, non-admissible downstream use, and source-bearing reopen discipline | `A.6.3.CSC Controlled Semantic Coarsening` |
| one review unit already keeps the same primary entity of concern, one bounded comparison, and one outside-work boundary stable | `ComparativeReading` within `InterpretationDiscipline` |
| the same unit still has unstable reviewed-source, comparative-move, or outside-work reading after local repair | `E.17.AUD.OOTD` (`PublicationUnit Primary EntityOfConcern Discipline`) |
| the real job is explanation-face governance on existing faces | `E.17.EFP` |
| the comparison is now opening an abductive prompt or action-selection question | `B.5.2.0` or `B.5.2` |
| the target or ontology is changing and now needs continuity witnesses | `OntologicalReframing` or `A.6.4` |
| the unit is now being used as a decision-making claim or decision record | `C.11` |
| the unit is now being used for execution, gate, or adjudication consequence | `A.15`, `A.20`, or `A.21` |

For first-minute use, read the four boundary rows around the comparative-reading case itself as a compact mirror of the near-top working-fit check and the ordinary working card:
- pressured local lexical head -> `E.17.AUD.LHR` (`Local Head Restoration`);
- stable same-object comparative review unit -> stay with `ComparativeReading`;
- same unit still unstable after local repair -> `E.17.AUD.OOTD` (`PublicationUnit Primary EntityOfConcern Discipline`);
- neighboring pattern for bridge, prompt, ontology, action, gate, adjudication, authority, or downstream claim already primary -> move out of this pattern.
If the comparison unit is already carrying neighboring work, use the boundary rows first and then read `E.17.ID.CR:5.4.7` through `E.17.ID.CR:5.4.10` as the nearest worked boundary examples.

#### E.17.ID.CR:4.5.a - Ordinary working order for the card

The shortest ordinary working order is:
1. name the base source relation or work question if the case is mixed;
2. pin the reviewed source episteme or source publication and make the shared review frame plus any distinct alternatives visible;
3. state the bounded comparative lift, or the small set of contrast rows and their row-level comparison bases, in compact form;
4. declare the unsupported downstream claim or effect and the review-only and non-executive world-contact limit;
5. name the boundary trigger that would end interpretation.

That five-step order is not a second ordinary working card, and it is not a canonical review process. It is only one local working aid for this pattern.
It is the shortest way to recover the seven-row ordinary working card in `E.17.ID.CR:4.3.b.a`.
In ordinary use, publish the resulting seven-row card in compact form rather than a heavier load-bearing declaration block whenever boundary pressure still stays low.
If the seven-row working card still cannot be completed plainly through that order, the review unit is not yet ready to stay here.
If the note, sheet, or review aid first has to answer what it is about, what move it is carrying, and what wider work remains outside, stabilize that `PublicationUnit` question with `E.17.AUD.OOTD` (`PublicationUnit Primary EntityOfConcern Discipline`) before continuing comparative-reading work.

