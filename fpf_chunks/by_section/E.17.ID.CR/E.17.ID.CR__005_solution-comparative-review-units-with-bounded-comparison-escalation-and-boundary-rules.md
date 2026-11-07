---
chunk_kind: "child"
pattern_id: "E.17.ID.CR"
pattern_title: "Compare Sources Within a Shared Review Frame (ComparativeReviewUnit)"
section_id: "E.17.ID.CR:4"
section_title: "Solution - comparative review units with bounded comparison, escalation, and boundary rules"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.ID.CR/E.17.ID.CR__005_solution-comparative-review-units-with-bounded-comparison-escalation-and-boundary-rules.md"
commit_sha: "e307edbd91c04c1d85661bd309b9944fac251937"
heading_path:
  - "E.17.ID.CR — Compare Sources Within a Shared Review Frame (ComparativeReviewUnit)"
  - "E.17.ID.CR:4 — Solution - comparative review units with bounded comparison, escalation, and boundary rules"
line_start: 108595
line_end: 108879
dependencies:
  - "A.15"
  - "A.15.2"
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

Make one bounded comparison from the claims the reviewed sources actually support. Start with the receiving review question, recover the relevant claims and conditions in each source, and derive the contrast on a common basis. A source-linked paragraph or small table can carry the result. Use the construction below when the comparison basis or contrast is not already established.

##### E.17.ID.CR:4.1.1 - Obtain the comparison from the available material

**Recover the question and its criterion.** Identify what the receiving review needs to distinguish and why: for example, the restoration time a release plan can guarantee, the populations covered by two studies, or the conditions under which two Methods can be used. Read the request, applicable requirement and surrounding review context for the object, situation and consequence that make a difference relevant. Turn that difference into an answerable question about each source. If the purpose is only to compare the accounts, the criterion can concern their coverage or emphasis; state that subject. If a necessary priority or requirement is missing, ask the receiving reviewer which consequence or condition the comparison must resolve. Meanwhile retain any useful source contrast whose basis is already clear.

**Recover each source's answer.** Locate the passages bearing on that question, including definitions, qualifications and supporting results. For each alternative, recover what is asserted, about what, under which conditions and with what support. Keep the source return beside the extracted claim when it would otherwise be lost. Read enough surrounding argument to distinguish a stated result, an assumption, a proposed result and an unanswered question. When a source is silent, report the missing coverage; infer absence only when an explicit negative claim or a sufficiently complete account supports it.

**Establish the common basis.** Put the relevant claims together and ask whether the proposed predicate applies to both under compatible interpretations. A shorter reported time is comparable only after its event, unit, scope and status are understood: one observed duration, a mean and an upper bound answer different questions. A common topic does not make them interchangeable. Recover a missing interpretation from the source's definitions or cited basis. Use the subject's comparison Method for the actual claim: C.16 for measurement conditions, for example, or F.9 when a required semantic correspondence connects distinct local senses. If the correspondence or required fact remains unavailable, split the contrast into what each source establishes and state the exact missing basis for the stronger comparison. Different conditions can themselves be the useful contrast.

**Derive and bound the result.** State what follows from the aligned claims and show the reason that connects them. For textual emphasis, identify the content or allocation of discussion that warrants the contrast; this alone says nothing about the described alternatives' actual performance. For a subject claim, preserve its applicable comparison rule and evidence. Distinguish a contrary result from insufficient support. Do not force a common ranking when the sources support different dimensions or incomparable conditions. A precise question such as “obtain B's restoration bound at production load L” is a usable return when that answer is necessary for the requested comparison.

**Publish for the receiving use.** Keep the sources, comparison basis, supported contrast and conditions needed to interpret it recoverable. Use an adjacent pair of passages, a paragraph or a table according to what the reader needs to inspect together. If the wording, arrangement or intended use could reasonably be taken as a stronger claim, state that particular limit and the condition for reopening it. Apply the relevant neighboring Method when that stronger claim is actually requested.

**Worked construction.** A release brief asks whether a rollback plan can establish restoration within eight minutes at production load L. Note A states a ten-minute upper bound at L. Note B reports one six-minute rollback in staging at 0.2L. The reviewer first locates these passages and recovers the different status of the numbers: A gives a bound under the relevant load; B gives one observation under a smaller load. The shared question is the supported production restoration bound, not which displayed number is smaller.

The resulting note can say: “A establishes an upper bound of ten minutes at L; B reports six minutes once at 0.2L. Neither statement establishes the required eight-minute production bound. A may have a tighter supported bound; B needs support for a bound at L. These notes do not establish which rollback is faster in production.” The return identifies the needed inquiry: inspect A's bound derivation for an applicable tighter result, or obtain B's qualified bound at L from its validation or analysis. Further testing is selected only if the available support cannot answer the receiving question and that answer is still needed.

Now suppose B supplies a qualified seven-minute upper bound at L with the same restoration endpoint and applicable conditions. The comparison can establish that B supplies a bound meeting the eight-minute requirement while A's stated bound does not establish that fit. It still cannot infer that every B execution is faster than every A execution. If B instead says nothing about restoration time, the result is a source-coverage gap. The same construction applies to non-numerical sources: align the actual claims and conditions, then state only the contrast that those claims support.

In plain working terms, this pattern is for a review unit that says something like:
- `this option write-up foregrounds integration pressure more than that one`;
- `these two available source epistemes or source publications are useful together, but they are not yet equivalent`;
- `this dashboard view helps triage one contrastive question, but it is not yet a release decision or a root-cause claim`;
- `this research synthesis foregrounds uncertainty more than that one, but it is not yet a method choice`;
- `this program brief foregrounds continuity risk more than that one, but it is not yet a funding decision`.

If that sounds like the review unit you need, keep the ordinary minimum recoverable. If the first move is no longer bounded comparison over pinned sources, name the crossed claim and let its governing pattern carry that claim before this unit is used.

#### E.17.ID.CR:4.1.b - Compact placement

`ComparativeReviewUnit` is the governing pattern selected inside the wider `InterpretationDiscipline` naming family for this bounded use. The family name helps readers find the interpretation area; it does not govern the local claim. The local object is one comparative review unit carrying one bounded comparison, or a small set of bounded contrast rows, over already available source epistemes or source publications.

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
- **Interpretive lift** = the bounded contrast derived from available source claims; in a small comparison sheet, each row has its comparison criterion and material conditions under the shared review question.
- **Bridge references** = required `bridgeOccurrenceRef` and `boundedUseClaimRef` when the case depends on bridge-mediated correspondence rather than ordinary source interpretation alone. The use-claim reference resolves a claim whose `EntityOfConcern` is that Bridge occurrence and whose proposed use, direction, correspondence rule, tolerated loss, and polarity match this comparative unit. Optional `bridgeCardRef` cites reusable packaging, and optional `bridgeStanceRef` cites a separate F.9.1 episteme whose `EntityOfConcern` is that exact use claim.
- **Bounded comparative use** = what this review unit can be used for while it remains only a bounded comparative review unit.
- **Overread risk** = how the review unit is most likely to be overread into a bridge, action-selection, ontology, or authority claim that it does not carry.
- **Prompt boundary** = the point at which an explanatory question with rival explanations still open becomes primary under `B.5.2.0` or `B.5.2`; `U.AbductivePrompt` classifies the published account of that initiating question under `B.5.2.0:4.2.1–4.2.2`.
- **Ordinary minimum block** = the smallest ordinary record that keeps the review unit honest for working use.
- **Load-bearing extension** = the fuller declaration record used when the case sits close to bridge, explanation, abductive, ontology, or authority boundaries.

These terms are local review fields for completing the comparative review unit. They keep source references, shared review frame, compared alternatives, bounded lift, blocked downstream claim or effect, and boundary trigger readable in the review unit.
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
- explanatory questions with rival explanations open (`B.5.2.0` or `B.5.2`), and choice among already available actions, probes, or method options (`C.11`);
- ontology-facing reframing or changed EntityOfConcern (`OntologicalReframing` or `A.6.4`);
- policy, gate, adjudication, assurance, or work-facing use (name the actual claim and use its governing pattern; see `E.17.ID.CR:4.5`).

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
The ordinary minimum block states the content needed for ordinary use; the card is one way to recover and arrange it.
The fuller declaration block remains available as a reviewable declaration extension that carries source, boundary, and downstream-claim fields by value. If a real assurance or B.3 threshold is current, cite the separately constituted B.3 claim or record; do not turn this declaration extension into that assurance record.

#### E.17.ID.CR:4.3.a - Five plain working questions

The near-top working-fit check selects the comparison task. Use these questions to recover its result:
1. Which available sources and alternatives answer the receiving review question?
2. Which claims, conditions and supporting passages in each source bear on it?
3. On what criterion can those claims be compared, and what does the comparison establish?
4. What necessary interpretation or fact remains unavailable, and where can it be obtained?
5. Does the present wording or receiving use imply a stronger claim whose grounds must be supplied?

Use :4.1.1 to obtain a missing comparison basis or contrast. Repair an ambiguous local expression under E.17.AUD.LHR when wording is the obstacle; use E.17.AUD.OOTD when the unit's primary subject or move remains unstable. Missing subject evidence remains a substantive gap.

#### E.17.ID.CR:4.3.b - Ordinary minimum block

For an ordinary bounded comparison, keep recoverable:
- the reviewed sources and passages carrying the relevant claims;
- the shared question, distinct alternatives and comparison criterion;
- the supported contrast and conditions needed to interpret it; and
- any unresolved basis that limits the requested result.

Add a downstream-use limit and its governing pattern when the wording, representation, receiving use or applicable authority rule creates that particular overread. Preserve a required contractual form and the grounds of any actual equivalence, causal, choice, gate or authority claim.

If those minimum answers cannot stay stable across the same note, sheet, or review aid without sliding between reviewed source episteme or source publication, bounded comparative review unit, bounded lift, and outside work, stop here. Repair local lexical-head kind pressure through `E.17.AUD.LHR` (`Local Head Restoration`); if the whole review unit still has unstable primary-subject identification (including the carried EntityOfConcern when applicable) or carried-move identification after that repair, apply `E.17.AUD.OOTD` (`PublicationUnit Primary-Subject Discipline`) before adding more declaration weight.

##### E.17.ID.CR:4.3.b.a - Ordinary working card

An ordinary comparative review unit keeps the applicable content below recoverable. Use these rows when their arrangement helps:

| Row | Plain question | Minimum answer |
| --- | --- | --- |
| **Reviewed source** | What already available source epistemes or source publications are being compared? | one pinned source slice, one explicit source pair, or one explicit source set |
| **Source references** | Where can a reviewer inspect that source episteme or source publication? | visible `sourceAnchorSet` or nearby `sourceRefs` |
| **Shared review frame and alternative identities** | What review target, described situation, or source-set reference is preserved, and what alternatives remain distinct under it? | preserved shared review frame; equivalence or substitution requires its applicable direct relation, with F.9 additionally governing any required cross-context semantic correspondence |
| **Bounded lift row(s)** | What contrast follows from the source claims? | the comparison basis, supported contrast and material conditions obtained through :4.1.1 |
| **Downstream-use limit, when needed** | What stronger reading is plausible here but unsupported? | the particular limit, such as an unestablished equivalence or approval |
| **World-contact limit, when needed** | Does the receiving use require an explicit limit on action or reliance? | the applicable limit and its basis |
| **Boundary trigger, when needed** | What changed claim or condition requires further work? | the condition and the actual governing Method |

The working card may appear inline or in the immediate review context. Retain a card or table when its arrangement supports comparison or independent revision of contrast rows. Keep the form required by a specific receiving contract. When the unit travels separately, carry the interpretation and source return needed for that use.
Use these questions as the ordinary recovery reference for the near-top working-fit check:
- if rows 1-4 are still unstable because one pressured local lexical head or qualifier is doing too much work, stop and repair that local lexical-head pressure through `E.17.AUD.LHR` (`Local Head Restoration`) before you keep building the comparative review unit here;
- if the applicable content in rows 3-7 cannot stay stable because the same review unit still has unstable reviewed-source, comparative-move identification, or outside-work boundary after one honest local repair, apply `E.17.AUD.OOTD` (`PublicationUnit Primary-Subject Discipline`);
- if the applicable rows stay recoverable over one pinned source slice or source pair, one preserved shared review frame, distinct alternatives where present, and one bounded contrast or small row set, `ComparativeReviewUnit` remains the honest primary governing pattern.

The nearest stay-here worked slices for this pattern are `E.17.ID.CR:5.4.5` through `E.17.ID.CR:5.4.6.b`.
The nearest stop-and-reopen worked slice is `E.17.ID.CR:5.4.6.c`.

Use the fuller declaration extension only when one of the boundary, reader-fit, or misuse conditions in `E.17.ID.CR:4.3.c` becomes true.
`ComparativeReviewUnit` remains primary only while the ordinary minimum stays recoverable and the same review unit is still mainly about one bounded comparison, or a small set of bounded contrast rows, over already pinned source epistemes or source publications. If the first question is what the review unit is about, what move it carries, and what wider work remains outside, use `E.17.AUD.OOTD` (`PublicationUnit Primary-Subject Discipline`) to stabilize that `PublicationUnit` question before adding more declaration weight here.

#### E.17.ID.CR:4.3.c - Fuller Declaration Extension Guidance

A fuller declaration record becomes warranted only when a local condition changes the actual first move: reader-fit is doing real work, overread risk is high, a mixed case depends on `A.6.3.*` or `E.17.EFP`, or a bridge-mediated relation is live. Resolve remaining subject or move instability through `E.17.AUD.OOTD` before choosing the declaration weight, as below.

The fuller declaration extension can inherit already-declared case ids, source pins, and provenance references instead of restating them inline. When recorded as a claim-bearing review unit, that extension normally captures the ordinary minimum block plus only the neighboring-pattern fields that govern the mixed case.

Do not answer `PublicationUnit` instability by stacking more local fields onto the fuller declaration extension. If `E.17.AUD.LHR` (`Local Head Restoration`) has already repaired the local lexical-head pressure and the same review unit still has unstable reviewed-source, publication-unit, comparative-move identification, or outside-work boundary, stabilize that `PublicationUnit` question with `E.17.AUD.OOTD` (`PublicationUnit Primary-Subject Discipline`) before deciding how much declaration weight stays here.

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

`sourceRelationClass` is only the source-relation or bounded-claim class for the local claim or use. `comparativeRelationClass` is only the comparative-relation class of this review unit. Neither field is a neighboring object or claim such as a relation kind, Bridge occurrence, bounded-use claim, Card, stance note, semantic identity, evidence relation, gate, assurance, work relation, speech act, commitment, authority reference, or decision record. The `sameEntityComparisonClass` value is a special case for comparisons where the compared sources really describe the same entity; it does not assert semantic identity. When the unit compares distinct alternatives, use `sharedFrameDistinctAlternativeClass` plus distinct alternative refs. Equivalence or substitution requires its applicable direct relation. When that use depends on correspondence between local senses from different semantic contexts, also establish the F.9 Bridge and its required bounded-use claim.
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

1. **Static comparative review note.** A static note needs its sources, comparison criterion, supported contrast and material conditions. Use the `E.17:5.1b` source-relation class when that relation is disputed, and an explicit downstream-use limit or boundary trigger when the current use requires it.
2. **Interactive comparative aid.** Add `targetUserModel`, `interactionMode`, state or history needed for the comparison claim, `overreadRisk`, and bounded-use boundary only when the aid is actually interactive, stateful, adaptive, or user-model-bearing. These fields keep the interactive comparative aid from being mistaken for audience-neutral static prose; they do not carry a crossed claim.

A comparative review unit can expose or cite the source epistemes, source publications, or project-side FPF references being compared, but layout, fluent contrast, side-by-side placement, or guided-review reuse does not change the kind of the unit or create a stronger source relation. If the required source relation is missing, the repair request or source-gap note is prospective only; it does not backdate a source relation into the earlier comparison.

**Comparative-review-unit identity over revision.** A revised comparison table, regenerated comparison note, or updated guided review aid is not the same bounded comparison merely because the layout, title, or compared-source family stayed familiar. If new source input, revised source references, changed comparison criterion, changed shared review frame, or changed blocked downstream claim or effect changes the comparison identity or downstream use, publish the preserved comparative frame and the changed claims, or treat the result as a new comparative review unit before using it for a stronger crossed claim.

#### E.17.ID.CR:4.3.g - Representation ontology and modeling lens (informative)

This pattern does not model interpretation in general.
It models one comparative review unit governed by `ComparativeReviewUnit` within the broader `InterpretationDiscipline` family.
In plain terms, the pattern works over the review unit itself.
That unit can appear as a comparison note, comparison sheet, or guided review aid, but it is not the whole review process or the source system.
The bounded comparison is the interpretive lift carried by that review unit.

The minimum typed lens is a compact record of:
- source references and source relation;
- one declared source-relation class;
- one declared comparison criterion and added-claim policy;
- one bounded-use boundary, one overread-risk line, and one `worldContactPolicy` that remains subordinate to the pattern governing a gate or adjudication claim; `A.21` governs a named gate decision under its applicable profile, while `A.20` applies only to a named internal-constraint check in a transformation-flow case;
- the relevant prompt, ontology, and authority boundary triggers;
- and which neighboring pattern still governs the base case when this remains a mixed overlay.

The lens keeps the main read tied to the review unit and the problem-owning review domain, while leaving source, continuity, and boundary discipline under whichever neighboring pattern still governs the base case.

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
   When the case stops being bounded comparison, name the claim that crossed the boundary and apply the pattern that governs it; use `E.17.ID.CR:4.5` to identify the relevant boundary.
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
| the comparison wording is now making sameness, equivalence, alignment, mapping, substitution, or a cross-context Bridge claim | `A.6.9` recovers the concrete predicate and its subject pattern. Use F.9 for an actual cross-context semantic correspondence and its bounded-use claim; F.9.1 supplies only an optional stance note about that claim. |
| the note is primarily a reduced-use source-pinned rendering with narrower-use, blocked downstream use, and source-bearing reopen discipline | `A.6.3.CSC Controlled Semantic Coarsening` |
| one review unit already keeps the same primary entity of concern, one bounded comparison, and one outside-work boundary stable | `ComparativeReviewUnit` within `InterpretationDiscipline` |
| the same unit still has unstable reviewed-source, comparative-move identification, or outside-work boundary after local repair | `E.17.AUD.OOTD` (`PublicationUnit Primary-Subject Discipline`) |
| the real job is explanation-face governance on existing faces | `E.17.EFP` |
| the comparison raises an explanatory question with rival explanations still open | `B.5.2.0` or `B.5.2` |
| the target or ontology is changing and now needs continuity witnesses | `OntologicalReframing` or `A.6.4` |
| the unit is now used to choose among already available actions, probes, or method options, or to publish the resulting decision record | `C.11` |
| the unit is now being used for execution, gate, or adjudication consequence | `A.15` for System-Role–Method–Work alignment, `A.15.1` for dated `U.Work`, and `A.21` for a named gate decision under its applicable profile; `A.20` only for a named internal-constraint check in a transformation-flow case; adjudication stays with its defining policy or pattern |

For first-minute use, read the four boundary rows around the comparative-review-unit case itself as a compact mirror of the near-top working-fit check and the ordinary working card:
- pressured local lexical head -> `E.17.AUD.LHR` (`Local Head Restoration`);
- stable same-object comparative review unit -> stay with `ComparativeReviewUnit`;
- same unit still unstable after local repair -> `E.17.AUD.OOTD` (`PublicationUnit Primary-Subject Discipline`);
- any stronger crossed claim already primary -> the governing pattern for that claim is primary.
If the comparison unit is already carrying neighboring work, use the boundary rows first and then read `E.17.ID.CR:5.4.7` through `E.17.ID.CR:5.4.10` as the nearest worked boundary examples.

#### E.17.ID.CR:4.5.a - Ordinary working order

The ordinary working order is to recover the receiving question, inspect the relevant source claims, establish their comparison basis and derive the bounded contrast as explained in :4.1.1. Publish that result with its source return and material conditions. Add a particular downstream limit or neighboring Method only when the current claim or receiving use requires it.

If the result cannot yet be obtained, return the missing source, interpretation, criterion or fact and the attainable inquiry that could settle it. Use E.17.AUD.LHR or E.17.AUD.OOTD when the obstacle is respectively local wording or unstable primary-subject or move identification; those repairs do not supply missing subject evidence.

