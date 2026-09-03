---
chunk_kind: "child"
pattern_id: "E.17.ID.CR"
pattern_title: "ComparativeReviewUnit - bounded comparison over comparative review units"
section_id: "E.17.ID.CR:4"
section_title: "Solution - comparative review units with bounded comparison, escalation, and boundary rules"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.ID.CR/E.17.ID.CR__005_solution-comparative-review-units-with-bounded-comparison-escalation-and-boundary-rules.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "E.17.ID.CR — ComparativeReviewUnit - bounded comparison over comparative review units"
  - "E.17.ID.CR:4 — Solution - comparative review units with bounded comparison, escalation, and boundary rules"
line_start: 83904
line_end: 84188
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

### E.17.ID.CR:4 - Solution - comparative review units with bounded comparison, escalation, and boundary rules

#### E.17.ID.CR:4.1 - Ordinary comparative review-unit move

Make one bounded comparison unit over already available source epistemes or source publications. Pin the reviewed sources, state the shared review frame, keep the compared alternatives visible, write the bounded comparative lift, name the downstream claim or effect that remains blocked, and give the boundary trigger that would move the case to another governing pattern.

In plain working terms, this pattern is for a review unit that says something like:
- `this option write-up foregrounds integration pressure more than that one`;
- `these two available source epistemes or source publications are useful together, but they are not yet equivalent`;
- `this dashboard view helps triage one contrastive question, but it is not yet a release decision or a root-cause claim`;
- `this research synthesis foregrounds uncertainty more than that one, but it is not yet a method choice`;
- `this program brief foregrounds continuity risk more than that one, but it is not yet a funding decision`.

If that sounds like the review unit you need, keep the comparison unit bounded by the seven-row card. If the first move is no longer bounded comparison over pinned sources, name the crossed claim and let its governing pattern carry that claim before this unit is used.

#### E.17.ID.CR:4.1.b - Compact placement

`ComparativeReviewUnit` is the governing pattern selected inside the wider `InterpretationDiscipline` naming family for this bounded use. The family name helps readers find the interpretation area; it does not govern the local claim. The local object is one comparative review unit carrying one bounded comparison, or a small set of bounded contrast rows, over already available source epistemes or source publications.

> `ComparativeReviewUnit` governs one comparative review unit over already available, source-pinned epistemes or source-pinned publications. It stays bounded only while the shared review frame and source references remain visible, distinct alternatives stay distinct, the added lift remains comparative, and any crossed bridge, prompt, ontology, work, gate, authority, or downstream-use claim is named and governed by the pattern for that claim.

Use `E.17.ID.CR`, `ID.CR`, or `ComparativeReviewUnit` when this bounded comparison unit is the current object. Use the neighboring pattern when the crossed claim becomes primary.

#### E.17.ID.CR:4.1.c - Why the comparative-review-unit specialization needs its own discipline

Teams already produce small comparative review units, often as comparison notes, comparison sheets, or guided review aids, that add more interpretive lift than a short F.9.1 stance note about an existing bounded-use claim but still stop below action selection, ontology reframing, retargeting, or approval guidance.
Leaving that middle band unnamed creates two opposite failures: one reader dismisses the review unit as harmless prose, while another over-reads it as if it already carried substitution, action-selection pressure, or action authority.

This pattern gives teams a narrow way to prepare, share, and inspect that comparative review unit without smuggling a downstream claim or effect beyond what the source, bridge stance, and bounded use can honestly carry.

#### E.17.ID.CR:4.1.d - Local working vocabulary

This pattern uses a small local vocabulary for review.
- **Comparative review unit** = a lightweight review unit such as a short comparison note, small comparison sheet, guided review aid, or guided comparative UI whose explicit job is one bounded comparison or a small set of bounded contrast rows under one shared review frame.
- **Base governing case** = the primary source relation, pattern-governing case, or project work question that already governs the review use before bounded comparison is added.
- **Reviewed source episteme or source publication** = the already pinned or otherwise reviewable source episteme or source publication being comparatively read; in plain terms, the already available source episteme or source publication under review.
- **Source references** = `sourceAnchorSet` or `sourceRefs` that make the interpreted source episteme or source publication inspectable.
- **Shared review frame** = the review target, described situation, decision situation, release candidate, method family, control scope, problem frame, or source-set reference that remains preserved while the comparison is made.
- **Compared alternative** = one distinct option, method, bulletin, strategy, note, view, source episteme, source publication, or project-side FPF kind and reference named by value kept separate under the shared review frame.
- **Same `EntityOfConcernRef` case** = the special case where the compared sources describe the same entity. This is common, but it is not required when distinct alternatives remain under one shared review frame.
- **Interpretive lift** = the bounded comparative or asymmetry-bearing comparison added on top of already available source epistemes or source publications; in a small comparison sheet, each row has its own declared comparison criterion while the unit keeps one shared blocked downstream claim or effect and boundary trigger.
- **Bridge references** = required `bridgeOccurrenceRef` and `boundedUseClaimRef` when the case depends on bridge-mediated correspondence rather than ordinary source interpretation alone. The use-claim reference resolves a claim whose `EntityOfConcern` is that Bridge occurrence and whose proposed use, direction, correspondence rule, tolerated loss, and polarity match this comparative unit. Optional `bridgeCardRef` cites reusable packaging, and optional `bridgeStanceRef` cites a separate F.9.1 episteme whose `EntityOfConcern` is that exact use claim.
- **Bounded comparative use** = what this review unit can be used for while it remains only a bounded comparative review unit.
- **Overread risk** = how the review unit is most likely to be overread into a bridge, action-selection, ontology, or authority claim that it does not carry.
- **Prompt boundary** = the explicit `U.AbductivePrompt` publication that becomes the governing publication when an abductive-prompt or action-selection claim governs the next action.
- **Ordinary minimum block** = the smallest ordinary record that keeps the review unit honest for working use.
- **Load-bearing extension** = the fuller declaration record used when the case sits close to bridge, explanation, abductive, ontology, or authority boundaries.

These terms are local review fields for completing the comparative review unit. They keep source references, shared review frame, compared alternatives, bounded lift, blocked downstream claim or effect, and boundary trigger readable in the card.
When one of those fields starts carrying a bridge, evidence, gate, speech-act, commitment, work, authority, publication-face, or project-side FPF claim, name that crossed claim and use the governing pattern for it.

#### E.17.ID.CR:4.2 - Scope and exclusions

**In scope**
- bounded comparative asymmetry over already declared reviewed source epistemes or source publications;
- reader-facing interpretive caution that stays source-tethered and preserves the shared review frame;
- comparison of distinct alternatives under one shared review target, described situation, release candidate, method family, control scope, problem frame, or source-set reference;
- comparative review units that answer one explicit contrastive question without creating a rival action-selection search;
- bounded user-fit when that fit only limits use rather than widening authority.

**Out of scope**
- same-entity restatement, conservative rewrite, or representation shift whose main question stays with `A.6.3`, `A.6.3.CR`, or `A.6.3.RT`;
- a separate F.9.1 stance note that only clarifies an already constituted F.9 bounded-use claim;
- explanation-face use discipline, bounded-use boundary, or added-link review on existing faces (`E.17.EFP`);
- abductive-prompt or action-selection cases (`B.5.2.0` or `B.5.2`);
- ontology-facing reframing or changed EntityOfConcern (`OntologicalReframing` or `A.6.4`);
- policy, gate, adjudication, assurance, or work-facing use (`A.15`, `A.20`, or `A.21`).

#### E.17.ID.CR:4.2.a - Working-fit test

Use this discipline only when all of the following hold:
1. the reviewed source episteme or source publication is already pinned or otherwise reviewable;
2. the review unit adds one bounded comparative or interpretive lift, or a small set of bounded contrast rows with row-level comparison criteria;
3. the case is still answering a bounded contrastive question rather than selecting an action;
4. the shared review frame stays preserved, and compared alternatives remain distinct unless an explicit bridge or substitution source supplies equivalence, substitution, or another named relation between them;
5. the main question is not already better described as same-entity viewing, an F.9.1 stance note about an existing bounded-use claim, or explanation-face use discipline.

If any of those fail, handle the current work under the neighboring FPF pattern and project-side FPF kind and reference named by value that actually govern it.

#### E.17.ID.CR:4.2.b - Nearest neighboring work

Name the base source relation or work question before adding bounded comparison. If the current question is already source transformation, bridge, explanation-face use, prompt or action selection, ontology or changed `EntityOfConcern`, decision, work or reliance, gate, assurance, adjudication, or reduced-use source rendering, do not stretch `ComparativeReviewUnit` to carry it. Use the compact boundary map in `E.17.ID.CR:4.5` and the governing pattern for the crossed claim.

#### E.17.ID.CR:4.3 - Working-model first; plain questions first, ordinary minimum second, full declaration third

Most working users do not have to start with a long declaration block.
This pattern therefore follows `E.14`'s working-model-first discipline: the first usable block is a small set of plain questions that helps an engineer-manager keep the review unit bounded to the work it can honestly carry.
The ordinary minimum block comes next for ordinary use: it lets the reader turn the working comparison into the seven-row card before touching the fuller declaration block.
The fuller declaration block remains available as a reviewable declaration extension that carries source, boundary, and downstream-claim fields by value. If a real assurance or B.3 threshold is current, cite the separately constituted B.3 claim or record; do not turn this declaration extension into that assurance record.

#### E.17.ID.CR:4.3.a - Five plain working questions

The near-top quick working-fit check is the canonical first working block for this pattern.
A working user can usually answer these same five questions before touching the fuller blocks:
1. What already available source epistemes or source publications am I comparing?
2. What single contrast or small set of contrast rows am I trying to make visible?
3. Am I still inside the same shared review frame, with compared alternatives kept distinct when they are distinct, or has the review target already shifted?
4. What blocked downstream interpretation does the team avoid taking from this review unit?
5. What would make another governing pattern govern the explanation, bridge work, prompt work, ontology work, or decision-authority claim?

If these five answers are not visible, the case is not ready to stay here as a bounded comparative review unit.

#### E.17.ID.CR:4.3.b - Ordinary minimum block

For ordinary bounded comparative review units, it is usually enough that the unit or its surrounding review context keeps explicit:
- what reviewed source episteme or source publication is being interpreted;
- which source references carry the local claim;
- that the shared review frame remains preserved and that distinct alternatives remain distinct unless another source supplies bridge or substitution relation;
- what declared bounded comparative lift is being added, or which bounded contrast rows are included and what comparison criterion each row uses;
- what downstream claim or effect remains blocked;
- that the default `worldContactPolicy` here is review-only and non-executive;
- and what neighboring FPF pattern becomes mandatory if the case crosses that neighboring boundary.

If those minimum answers cannot stay stable across the same note, sheet, or review aid without sliding between reviewed source episteme or source publication, bounded comparative review unit, bounded lift, and outside work, stop here. Repair local lexical-head kind pressure through `E.17.AUD.LHR` (`Local Head Restoration`); if the whole review unit still has unstable EntityOfConcern or carried-move identification after that repair, apply `E.17.AUD.OOTD` (`PublicationUnit Primary EntityOfConcern Discipline`) before adding more declaration weight.

##### E.17.ID.CR:4.3.b.a - Ordinary working card

An ordinary comparative review unit normally lets a reader recover these seven rows without using the heavier fuller declaration:

| Row | Plain question | Minimum answer |
| --- | --- | --- |
| **Reviewed source** | What already available source epistemes or source publications are being compared? | one pinned source slice, one explicit source pair, or one explicit source set |
| **Source references** | Where can a reviewer inspect that source episteme or source publication? | visible `sourceAnchorSet` or nearby `sourceRefs` |
| **Shared review frame and alternative identities** | What review target, described situation, or source-set reference is preserved, and what alternatives remain distinct under it? | preserved shared review frame; distinct alternatives are not treated as equivalent or substitutable without bridge relation |
| **Bounded lift row(s)** | What single contrast or small row set is this unit making visible? | one declared `comparisonBasis` or a small set of row-level `comparisonBasis` statements under one shared blocked downstream claim or effect and boundary trigger |
| **Blocked downstream claim or effect** | What is this unit not yet claiming? | no equivalence, abductive-prompt creation, ontology change, or decision authority |
| **World-contact limit** | What can the unit not be used to do? | `review-only and non-executive` |
| **Boundary trigger** | What would end this pattern and require another governing pattern? | one explicit bridge, explanation, prompt, ontology, or authority trigger |

This working card can appear inline in the comparative review unit or in its immediate review context.
Use it as the ordinary recovery reference for the near-top working-fit check:
- if rows 1-4 are still unstable because one pressured local lexical head or qualifier is doing too much work, stop and repair that local lexical-head pressure through `E.17.AUD.LHR` (`Local Head Restoration`) before you keep building the comparative review unit here;
- if rows 3-7 cannot stay stable because the same review unit still has unstable reviewed-source, comparative-move identification, or outside-work boundary after one honest local repair, apply `E.17.AUD.OOTD` (`PublicationUnit Primary EntityOfConcern Discipline`);
- if rows 1-7 stay recoverable over one pinned source slice or source pair, one preserved shared review frame, distinct alternatives where present, and one bounded contrast or small row set, `ComparativeReviewUnit` remains the honest primary governing pattern.

The nearest stay-here worked slices for this pattern are `E.17.ID.CR:5.4.5` through `E.17.ID.CR:5.4.6.b`.
The nearest stop-and-reopen worked slice is `E.17.ID.CR:5.4.6.c`.

Use the fuller declaration extension only when one of the boundary, reader-fit, or misuse conditions in `E.17.ID.CR:4.3.c` becomes true.
`ComparativeReviewUnit` remains primary only while those seven rows stay recoverable and the same review unit is still mainly about one bounded comparison, or a small set of bounded contrast rows, over already pinned source epistemes or source publications. If the first question is what the review unit is about, what move it carries, and what wider work remains outside, use `E.17.AUD.OOTD` (`PublicationUnit Primary EntityOfConcern Discipline`) to stabilize that `PublicationUnit` question before adding more declaration weight here.

#### E.17.ID.CR:4.3.c - Fuller Declaration Extension Guidance

A fuller declaration record becomes warranted only when a local condition changes the actual first move: reader-fit is doing real work, overread risk is high, a mixed case depends on `A.6.3.*` or `E.17.EFP`, bridge-mediated relation is live, or the same review unit still has unstable reviewed-source, comparative-move identification, or outside-work boundary after local repair.

The fuller declaration extension can inherit already-declared case ids, source pins, and provenance references instead of restating them inline. When recorded as a claim-bearing review unit, that extension normally captures the ordinary minimum block plus only the neighboring-pattern fields that govern the mixed case.

Do not answer `PublicationUnit` instability by stacking more local fields onto the fuller declaration extension. If `E.17.AUD.LHR` (`Local Head Restoration`) has already repaired the local lexical-head pressure and the same review unit still has unstable reviewed-source, publication-unit, comparative-move identification, or outside-work boundary, stabilize that `PublicationUnit` question with `E.17.AUD.OOTD` (`PublicationUnit Primary EntityOfConcern Discipline`) before deciding how much declaration weight stays here.

#### E.17.ID.CR:4.3.d - Fuller Declaration Block
When the heavier declaration weight really stays here, the unit still makes at least these fields recoverable:
- `sourceRelationClass` using the shared `E.17:5.1b` vocabulary when the comparison depends on source pointer, source availability or retrieval, source use, source faithfulness, claim recoverability, contradiction, omission, claim widening, added linkage, independent verification, bounded use, forbidden downstream use, or reopen trigger;
- `sourceAnchorSet` or `sourceRefs`;
- `comparativeRelationClass = sameEntityComparisonClass | sharedFrameDistinctAlternativeClass | readerFitComparativeClass`;
- `comparisonBasis`;
- `addedClaimPolicy`;
- required `bridgeOccurrenceRef` and `boundedUseClaimRef` when the case depends on bridge-mediated comparative relation; the use-claim reference resolves an exact claim whose `EntityOfConcern` is that Bridge occurrence and whose proposed use, direction, correspondence rule, tolerated loss, and polarity match the current comparative unit;
- optional `bridgeCardRef` when a reusable Card exists;
- optional `bridgeStanceRef` when it resolves the separate F.9.1 episteme whose `EntityOfConcern` is that exact use claim;
- `targetUserModel` when reader-fit is materially shaping the comparison unit;
- `interactionMode` when the review unit is not just one static comparative sentence;
- `contrastiveQuestion` when the case is answering a specific contrast;
- `boundedComparativeUse`;
- `overreadRisk`;
- `promptWorthinessThreshold`;
- `ontologyBoundaryTrigger`;
- `worldContactPolicy`;
- `downstreamAuthorityLimit`;
- `baseCasePattern` when the review unit is a mixed case layered over `A.6.3.*` or `E.17.EFP`.

`sourceRelationClass` is only the source-relation or bounded-claim class for the local claim or use. `comparativeRelationClass` is only the comparative-relation class of this review unit. Neither field is a neighboring object or claim such as a relation kind, Bridge occurrence, bounded-use claim, Card, stance note, semantic identity, evidence relation, gate, assurance, work relation, speech act, commitment, authority reference, or decision record. The `sameEntityComparisonClass` value is a special case for comparisons where the compared sources really describe the same entity; it does not assert semantic identity. When the unit compares distinct alternatives, use `sharedFrameDistinctAlternativeClass` plus distinct alternative refs, and do not treat the alternatives as equivalent or substitutable without an obtaining Bridge and the required bounded-use claim.
`readerFitComparativeClass` by itself does not create an interpretation claim. When bounded correspondence wording implies a cross-context Bridge, first apply F.9. The `boundedUseClaimRef` must resolve a claim whose `EntityOfConcern` is the exact `bridgeOccurrenceRef`, and its proposed use, direction, correspondence rule, tolerated loss, and polarity must match this comparative unit. A positive proposed use requires affirmative polarity; when A.10 or B.3 is triggered, current reliance must support that exact use. A degraded reliance result narrows the use. Negative, abstaining, reopened, evidence-needed, blocked, or mismatched results stop this bridge-mediated use. The pattern that directly constrains the proposed comparison decides authorization, and evidence of the comparative-review Work says whether it occurred. A `bridgeCardRef` remains optional packaging. A `bridgeStanceRef` is also optional and is admissible only when it resolves a separate F.9.1 episteme whose `EntityOfConcern` is that same bounded-use claim. None of these references can substitute for another.
The main comparison question plus the neighboring pattern boundaries still decide the selected FPF pattern or project-side FPF kind and reference named by value.

#### E.17.ID.CR:4.3.e - Interpretant-side block

The interpretant-side fields above do not turn this zone into a full interactive explanation system or a dialog-management system.
Their current role is narrower:
- keep bounded comparison from pretending it is audience-neutral when it is not;
- make the contrastive question, guided review mode, and bounded use visible;
- and stop interpretation prose from quietly becoming prompt-bearing guidance, assurance shorthand, or policy pressure.

#### E.17.ID.CR:4.3.f - Static note versus interactive aid

Use two comparison-relation forms.

1. **Static comparative review note.** A static note, sheet, or short review unit normally needs only the reviewed source episteme or source publication set, source references, `E.17:5.1b` source-relation class when source relation is disputed, comparison criterion, bounded lift, blocked downstream claim or effect, world-contact limit, and boundary trigger. Do not import interactive-explanation vocabulary into this ordinary case.
2. **Interactive comparative aid.** Add `targetUserModel`, `interactionMode`, state or history needed for the comparison claim, `overreadRisk`, and bounded-use boundary only when the aid is actually interactive, stateful, adaptive, or user-model-bearing. These fields keep the interactive comparative aid from being mistaken for audience-neutral static prose; they do not carry a crossed claim.

A comparative review unit can expose or cite the source epistemes, source publications, or project-side FPF references being compared, but layout, fluent contrast, side-by-side placement, or guided-review reuse does not change the kind of the unit or create a stronger source relation. If the required source relation is missing, the repair request or source-gap note is prospective only; it does not backdate a source relation into the earlier comparison.

**Comparative-review-unit identity over revision.** A revised comparison table, regenerated comparison note, or updated guided review aid is not the same bounded comparison merely because the layout, title, or compared-source family stayed familiar. If new source input, revised source references, changed comparison criterion, changed shared review frame, or changed blocked downstream claim or effect changes the comparison identity or downstream use, publish the preserved comparative frame and the changed claims, or treat the result as a new comparative review unit before using it for a stronger crossed claim.

#### E.17.ID.CR:4.3.g - Representation ontology and modeling lens (informative)

The early canonical lens for this pattern is already stated near the top: one comparative review unit over already available, source-pinned epistemes or source-pinned publications, with the shared review frame preserved, one bounded contrast or small row set made visible, and blocked downstream claim or effect kept outside.

This informative note only unpacks that same lens. It does not introduce a second one.

This pattern does not model interpretation in general.
It models the `ComparativeReviewUnit` as the selected governing pattern inside the broader `InterpretationDiscipline` family.
In plain terms, the pattern works over the review unit itself.
That unit can appear as a comparison note, comparison sheet, or guided review aid, but it is not the whole review process, it is not the source system, and it is not a hidden act of interpretation in the abstract.
The bounded comparison is the interpretive lift carried by that review unit.

The minimum typed lens is a compact record of:
- source references and source relation;
- one declared source-relation class;
- one declared comparison criterion and added-claim policy;
- one bounded-use boundary, one overread-risk line, and one `worldContactPolicy` that remains subordinate to `A.20` or `A.21` when gate or adjudication claim appears;
- the relevant prompt, ontology, and authority boundary triggers;
- and which neighboring pattern still governs the base case when this remains a mixed overlay.

That lens is intentionally modest.
It keeps the main read tied to the review unit and the problem-owning review domain, while leaving source, continuity, and boundary discipline under whichever neighboring pattern still governs the base case.
This pattern therefore does not create a rival bridge taxonomy, a rival base-case discipline, or a publication with named authority-reference relation of its own.

#### E.17.ID.CR:4.3.h - Working read-out

A working reader can usually say, in one short paragraph:
- what reviewed source episteme or source publication is being comparatively read;
- what bounded interpretive lift is being added;
- what shared review frame remains preserved, and, in the special same-EntityOfConcern case, why the same `EntityOfConcernRef` remains preserved;
- which crossed claim is still outside this pattern and which neighboring pattern would govern that claim if it became primary;
- and which boundary condition shows that the primary claim is no longer a bounded `ComparativeReviewUnit` claim.

If that read-out becomes fuzzy, the review unit is no longer bounded enough to stay here; narrow it, clarify it, or make the governing neighboring pattern primary for the crossed claim.

#### E.17.ID.CR:4.4 - Branch-discipline summary

This section is the compact governing-rule summary for `ComparativeReviewUnit` inside the Core. Use the fuller solution, boundary table, worked slices, and relations section here only when specific clause wording, full field set, or full reopen conditions matter.

1. **Preserve the shared review frame.**
   Keep the reviewed source episteme or source publication set, source references, declared comparison criterion, and distinct alternative identities visible. If `contrastiveQuestion` is doing real review work, state it.
2. **Keep the lift bounded and comparative.**
   The review unit can add one bounded comparative or asymmetry-bearing lift. It stops when that lift starts carrying a stronger crossed claim.
3. **Name the crossed claim instead of repeating exclusions.**
   When the case stops being bounded comparison, name the claim that crossed the boundary and apply the pattern that governs that claim: source transformation, bridge, explanation face, abductive prompt or action selection, ontology or changed `EntityOfConcern`, decision, work or reliance, gate, assurance, adjudication, or reduced-use source rendering.
4. **Keep neighboring-pattern authority explicit.**
   Bridge-mediated comparison requires an exact `bridgeOccurrenceRef` and a tuple-matched `boundedUseClaimRef` whose `EntityOfConcern` is that Bridge. Positive use requires affirmative polarity and, when A.10 or B.3 is triggered, current reliance for that exact use. Degraded reliance narrows the use; a negative, abstaining, reopened, evidence-needed, blocked, or mismatched result stops it. A Card and F.9.1 stance note remain optional and separate. Authorization and evidence that comparative-review Work occurred remain with their own patterns and records.
5. **Keep reader-fit bounded.**
   `targetUserModel`, `interactionMode`, `contrastiveQuestion`, `boundedComparativeUse`, and `overreadRisk` can be stated when they change actual review use, but they do not create authority that the unit does not carry.

#### E.17.ID.CR:4.5 - Neighboring-work boundary glance

This table is a compact boundary aid for separating the comparative review unit from neighboring project work and source requirements.
For a fuller mixed-case read, read this table together with the neighboring pattern discipline.

| If the case is really doing this... | Governing pattern or bounded disposition |
| --- | --- |
| one local lexical head or qualifier is still doing too much work, but one honest repair would stabilize the same unit | `E.17.AUD.LHR` (`Local Head Restoration`) |
| the same note is mostly rewriting, reframing, or re-rendering the same EntityOfConcern with no bounded comparative lift | `A.6.3`, `A.6.3.CR`, or `A.6.3.RT` |
| the real job is only to add a short reading note about an already constituted F.9 bounded-use claim | `F.9.1`; a Card is optional packaging |
| the comparison wording is now making a relation-precision claim between compared items | `A.6.P` |
| the comparison wording is now making sameness, equivalence, alignment, mapping, substitution, or a cross-context Bridge claim | Part F with `A.6.9` for wording and F.9 for the Bridge and bounded-use claim; use F.9.1 only for an optional stance note about that claim |
| the note is primarily a reduced-use source-pinned rendering with narrower-use, blocked downstream use, and source-bearing reopen discipline | `A.6.3.CSC Controlled Semantic Coarsening` |
| one review unit already keeps the same primary entity of concern, one bounded comparison, and one outside-work boundary stable | `ComparativeReviewUnit` within `InterpretationDiscipline` |
| the same unit still has unstable reviewed-source, comparative-move identification, or outside-work boundary after local repair | `E.17.AUD.OOTD` (`PublicationUnit Primary EntityOfConcern Discipline`) |
| the real job is explanation-face governance on existing faces | `E.17.EFP` |
| the comparison now creates an abductive-prompt claim or action-selection question | `B.5.2.0` or `B.5.2` |
| the target or ontology is changing and now needs continuity witnesses | `OntologicalReframing` or `A.6.4` |
| the unit is now being used as a decision-making claim or decision record | `C.11` |
| the unit is now being used for execution, gate, or adjudication consequence | `A.15`, `A.20`, or `A.21` |

For first-minute use, read the four boundary rows around the comparative-review-unit case itself as a compact mirror of the near-top working-fit check and the ordinary working card:
- pressured local lexical head -> `E.17.AUD.LHR` (`Local Head Restoration`);
- stable same-object comparative review unit -> stay with `ComparativeReviewUnit`;
- same unit still unstable after local repair -> `E.17.AUD.OOTD` (`PublicationUnit Primary EntityOfConcern Discipline`);
- any stronger crossed claim already primary -> the governing pattern for that claim is primary.
If the comparison unit is already carrying neighboring work, use the boundary rows first and then read `E.17.ID.CR:5.4.7` through `E.17.ID.CR:5.4.10` as the nearest worked boundary examples.

#### E.17.ID.CR:4.5.a - Ordinary working order for the card

The shortest ordinary working order is:
1. name the base source relation or work question if the case is mixed;
2. pin the reviewed source episteme or source publication and make the shared review frame plus any distinct alternatives visible;
3. state the bounded comparative lift, or the small set of contrast rows and their row-level comparison criteria, in compact form;
4. declare the blocked downstream claim or effect and the review-only and non-executive world-contact limit;
5. name the boundary trigger that would end interpretation.

Use this order only to recover the seven-row ordinary working card in `E.17.ID.CR:4.3.b.a`; publish the resulting card in compact form whenever boundary pressure still stays low.

If the seven-row working card still cannot be completed plainly through that order, the review unit is not yet ready to stay here.
If the first question is what the note, sheet, or review aid is about, what move it carries, and what wider work remains outside, stabilize that `PublicationUnit` question with `E.17.AUD.OOTD` (`PublicationUnit Primary EntityOfConcern Discipline`) before continuing comparative-review-unit work.

