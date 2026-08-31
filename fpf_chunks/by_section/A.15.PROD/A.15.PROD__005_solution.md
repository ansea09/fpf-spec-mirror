---
chunk_kind: "child"
pattern_id: "A.15.PROD"
pattern_title: "Production Work, Entity-Identity Inception, and Production Completion Recovery"
section_id: "A.15.PROD:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.PROD/A.15.PROD__005_solution.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "A.15.PROD — Production Work, Entity-Identity Inception, and Production Completion Recovery"
  - "A.15.PROD:4 — Solution"
line_start: 27690
line_end: 27882
dependencies:
  - "A.1"
  - "A.15.1"
  - "A.15.2"
  - "A.15.6"
  - "A.3.1"
  - "A.3.4"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "C.2.1"
  - "E.18.1"
  - "F.18"
  - "G.11"
keywords:
---

### A.15.PROD:4 - Solution

The practitioner **MUST** choose one of the three production questions, name the Work and the affected referent, candidate basis, or produced entity involved, and gather only the facts that decide that question. The practitioner **MUST** state each answer as a separate local compound relation-bearing claim and **MUST** stop or return an exact blocker when a required predicate, criterion, applicability rule, boundary fact, work granularity, or transformation-composition rule is missing. If another person, tool, or later decision must reuse the answer, publish that one claim as a C.2.1 episteme.

**Core and branch cut.** The common recovery core is receiver-first question selection, exact-object recovery, closure through declared predicates or one local claim selected under A.6.RCD disposition 2, and a deliberate stop. The production-work, entity-identity-inception, and production-completion branches add only their own `EntityOfConcern`, criterion or boundary, and branch-specific base. One branch neither inherits facts from another nor turns the common method into an omnibus production object. Work identity, transformation identity, subject identity, evidence, assurance, delivery, acceptance, release, publication, and availability remain with their subject patterns.

#### A.15.PROD:4.1 - Split the three questions before recovering evidence

| Question | Claim content | Ordinary stopping result | What it does not establish |
| --- | --- | --- | --- |
| Production-work participation | exact `currentWork` is itself `productionWork`, or exact `currentWork` is a declared proper work part of exact `productionWork` | one local positive or negative compound claim, or an exact work-grounding blocker | entity inception, completion, delivery, acceptance, or a universal production-work kind |
| Entity-identity inception | governed actual effects of exact `identityClosingWork` made exact `producedEntity` satisfy the rule in exact applicable `productIdentitySpecification` for the first time at exact `inceptionBoundary` | one local inception claim after the entity exists, plurality of incomparable minimal claims, or an exact blocker | production completion, later persistence, acceptance, or a reusable binary relation kind |
| Production completion | exact `completionSubject` satisfies exact applicable `productionCompletionCriterion` at `completionBoundary`, and a separate declared closure predicate or local claim connects that satisfaction to exact `productionWork` | one state-satisfaction claim plus, when asserted, one historically indexed Work-completion claim; otherwise the exact closure blocker | entity inception, delivery, acceptance, release, publication, or availability |

The three claims may cite overlapping facts. They remain different claims because they answer different receiving questions and can have different boundaries, criteria, and truthful C.2.1 `EntityOfConcern` values.

#### A.15.PROD:4.2 - Recover the smallest exact base

The practitioner **MUST** use only objects needed by the selected branch:

| Working name | Exact object and governor | Required contribution |
| --- | --- | --- |
| `productIdentitySpecification` | one exact C.2.1 predicate-definition episteme whose subject pattern states the identity rule; any continuing-edition relation to another specification episteme is stated separately | states the identity rule before inception without pretending that a future entity exists |
| identity-specification applicability basis | one named applicability predicate with its actual participants and boundary facts, or one filled local compound claim selected under A.6.RCD disposition 2 | applies the exact specification episteme to the candidate basis, subject context, and candidate `inceptionBoundary`; it introduces no universal applicability relation |
| `producedEntity` | one exact `U.Entity`, designated only after inception | is the entity whose identity rule first became true |
| `productionMethod` | one exact `U.Method` under A.3.1 | states the governed way of doing, intended production effect, applicability, and relevant identity or completion criterion meaning |
| `currentWork` | one exact Work individual admitted under `U.Work` by A.15.1 | designates the world-side dated occurrence. Recover every exact actual performer through A.13, then let A.15.1 independently admit the Work from its history, at least one obtaining `enactsMethod` relation, extent, and at least one obtaining locally declared containing-system relation. Only when this production claim also consumes precise assignment-bound attribution name the obtaining occurrence of the exact declared `U.SystemRoleAssignment` species and the separate F.6 relation through the same A.13 assignment. Missing or failed F.6 preserves the Work and lowers only that attribution. Name an additional enactment, binding, resource-use, or affected-referent relation only when the production claim uses that independently obtaining fact; none is a field stored in the occurrence. |
| `productionWork` | one exact Work individual admitted under `U.Work` by A.15.1 | designates either the same occurrence as `currentWork` or the exact larger Work occurrence of which `currentWork` is a declared proper part |
| `actualTransformation` | one or more independently identified `U.Transformation` occurrences under A.3.4 | names what changed without becoming the work or the produced entity |
| work-to-change basis | one named domain predicate with exact Work and transformation participants and obtaining case facts, or one filled local compound claim selected under A.6.RCD disposition 2 | establishes that selected actual changes are effects of exact work; coincidence is insufficient |
| `completionSubject` | the exact state-bearing entity or continuing referent judged by the completion criterion | keeps the criterion's subject explicit instead of applying a product-state test to Work |
| `productionCompletionCriterion` | one exact C.2.1 predicate-definition episteme whose subject pattern states the state-satisfaction rule; any continuing-edition relation to another criterion episteme is stated separately | states what state of `completionSubject` counts as satisfying the production requirement at the candidate boundary |
| production-work closure governor | one declared subject predicate or one filled local A.6.RCD claim that connects exact criterion satisfaction for `completionSubject` to closure of exact `productionWork` at the boundary | states why the Work is complete; criterion satisfaction alone does not supply this link |
| local assertion | one C.2.1 episteme | carries only the state-satisfaction claim or the production-work-completion claim needed by the selected question |

A method description, work plan, objective, commitment, product specification, evaluation result, or publication enters only when a named predicate or filled local claim connects it to the selected Work, entity, or claim and omitting that connection would change the named action or decision. Otherwise keep it separate. None is constitutive of every production occurrence.

#### A.15.PROD:4.3 - Select one production-work branch

**Whole-work branch.** `currentWork = productionWork` is admissible only when that exact dated Work enacts `productionMethod`; the method states its intended production effect; a named applicability claim applies the method to this case's inputs and conditions; the named work-to-change predicates obtain for the exact Work and transformations; and the identity or completion criterion that decides the selected question is named and applicable. A familiar broader production label establishes no parent work.

**Proper-part branch.** Exact `currentWork` is admissible as a proper part of exact `productionWork` only when `OperationalPartOf_work` or another exact A.15.1 work-part relation with fitting occurrence semantics obtains. Interval overlap or concurrency is asserted separately and establishes neither parthood nor coordination. The containing Work must likewise enact the production method; the method must state its intended production effect; a named applicability claim must apply it to the containing case; the named work-to-change predicates must obtain; and the identity or completion criterion that decides the selected question must be named and applicable. A shared label, project membership, common referent, temporal containment, overlap, or adjacency in a plan establishes no work parthood.

The two branches can support different bounded uses. A nut-fastening occurrence can be the whole production work for a narrowly bounded finishing operation and also a proper part of a larger car-production occurrence, provided each local claim names its exact extent, criterion, and work relation. `productionWork` is a relation-defined reading of one Work occurrence admitted under `U.Work`, not an intrinsic kind.

#### A.15.PROD:4.4 - Ground actual effects without inventing transformation composition

The practitioner **MUST** first recover every actual transformation independently through A.3.4: changed referent, exact extent or formal boundary, boundary conditions, actual before/during/after facts, and continuity or reidentification rule. The practitioner **MUST** then name the declared domain predicate for each exact Work-to-transformation pair, state its participant order, and show the case facts that make it obtain. If no one direct predicate suffices, use a local compound claim selected under A.6.RCD disposition 2 only when its constructor, governed base predicates, actual participants, and case facts are recoverable. If neither route is present, keep the Work and transformation separately and return `missing-governor[work-to-change]`. Temporal overlap, a common changed referent, a delta expression, a log record, or a post-state picture does not establish the link.

One transformation identified at the resolution needed by the production claim establishes neither presence nor absence of finer transformation parts. Work parts, method parts, samples, temporal subdivisions, concurrent changes, and flow representations do not establish transformation parts or a composite transformation.

If the selected production claim uses only independently identified transformations, continue without a composition claim. If it asserts positive composite-transformation identity, transformation parthood, or transformation holonhood and no accepted governor supplies that basis, return the exact missing-governor blocker. Composite `identityClosingWork` under A.15.1 does not cure that blocker and does not imply an isomorphic composite transformation.

#### A.15.PROD:4.5 - Recover entity-identity inception

**Definition: A15PROD-D1 (Entity-identity inception).** Entity-identity inception is the boundary at which exact `producedEntity` first satisfies the identity rule stated by exact `productIdentitySpecification` and a named applicability predicate or filled local claim applies that specification to the candidate basis, subject context, and boundary. Plain: **when this exact entity first exists**. `inceptionBoundary` is a case-local boundary designator, not a second technical term, claim kind, or relation kind.

For this branch, the practitioner **MUST** complete all five steps:

1. recover exact `productIdentitySpecification` as one C.2.1 predicate-definition episteme in the subject pattern that states the identity rule. Before inception, the governed question remains about exact work, method, actual effects, that specification episteme, and its candidate basis; no future `producedEntity` participant exists;
2. recover the named applicability predicate or filled local claim that applies that specification episteme to the exact candidate basis, subject context, and candidate `inceptionBoundary`, together with the exact actual effects of exact work and the declared links by which those effects bear on that rule;
3. find the earliest exact `inceptionBoundary` at which the rule in that applicable specification episteme becomes true and designate the resulting exact `producedEntity` only on the after-side of that boundary; the pre-inception candidate basis remains distinct from that entity;
4. identify exact `identityClosingWork`, using the one closing work occurrence when it exists or, for jointly necessary concurrent or nested work parts, their exact composite work under A.15.1 and its declared work-part relations; and
5. publish a positive local inception claim only after exact `producedEntity` exists and the claim names exact `productIdentitySpecification`, its named applicability predicate or filled local claim, exact `identityClosingWork`, exact `inceptionBoundary`, and all declared work-to-change and change-to-identity predicates or compound bases.

A published local inception claim **MUST** be indexed by the exact specification episteme and applicability basis used at `inceptionBoundary`. A later specification episteme does not silently rewrite that earlier claim. If an exact C.2.1 `EpistemeEditionRelation` connects the two specifications, the lineage can trigger refresh of a current dependent use, but the later specification still needs its own applicability basis at the boundary being judged. Without that relation, treat the later object as a non-continuing replacement and evaluate it independently. Changed applicability yields either a separately qualified claim under its new exact basis or an exact blocker; it does not move the earlier indexed boundary.

A delta expression, method description, work plan, log, post-state image, identity-rule episteme, or first observation establishes none of those links by itself. Absence of recoverable work granularity for `identityClosingWork` yields a **work-granularity blocker**. Several incomparable minimal work composites yield several local inception claims; narrative simplicity supplies no rule for selecting only one.

**Regulated-identification boundary.** A persistent identifier is not an inception criterion. A current subject practice that allocates an identifier at build or registration while keeping allocation separate from entity status supplies designation and continuity only. First existence requires a separately applicable subject-identity rule; its absence yields the exact identity-governor blocker. An assigned number does not make the candidate basis the after-side entity.

#### A.15.PROD:4.6 - Recover state satisfaction and historically indexed production completion

Completion wording often hides two claims. First ask whether the exact state-bearing subject satisfied the applicable criterion. Then ask whether the subject practice makes that satisfaction sufficient to close the exact production Work.

The **state-satisfaction claim** names:

- exact `completionSubject` whose state is judged;
- exact `completionBoundary`;
- exact `productionCompletionCriterion` episteme applicable to that subject and boundary;
- the named applicability predicate or filled local claim; and
- the actual boundary-state facts and the criterion predicate they satisfy.

When persisted, this C.2.1 episteme has `completionSubject` as its exact EntityOfConcern. It says nothing yet about whether Work is complete.

The separate **production-work-completion claim** names exact `productionWork`, the exact state-satisfaction claim, the same boundary, and the declared closure predicate or filled local A.6.RCD claim that makes this criterion satisfaction sufficient to close that Work. Its exact EntityOfConcern is `productionWork`. If no closure governor is available, keep the positive state-satisfaction claim and return `missing-governor[production-work-completion]`; do not apply a subject-state predicate to Work by metonymy.

Completion is historical. Later damage, loss, destruction, delivery, rejection, acceptance, release, publication, or unavailability does not erase an earlier true state-satisfaction or Work-completion claim. A later or replacement criterion episteme does not rewrite the earlier claim. Rework or later production Work that closes under an applicable criterion at a later boundary receives another local Work-completion claim.

Entity-identity inception, criterion satisfaction, and production-Work completion remain separate even when they share a boundary. A later evaluation-result episteme may support one of these claims under a direct evidence-use relation, but it creates neither the boundary, the subject state, nor Work closure.

Past Work and the two completion claims remain addressable after later destruction or evidence decay. A later assertion carries its own evidence currentness and reliance status. The produced entity, measurement or evaluation result, delivered entity, acceptance verdict, release, publication, availability, and downstream effect remain objects and claims defined and tested separately.

**Practice-specific criteria stay local.** NASA systems-engineering guidance, Scrum's Definition of Done, and similar authoritative practice sources can supply a criterion for the exact subject and practice use they address. They do not by themselves identify the A.15.1 Work or state that criterion satisfaction closes it. A subject-practice closure predicate or local claim must provide that second step; transition, delivery, review, or release remains separate.

#### A.15.PROD:4.7 - Publish local claims, not an omnibus relation

The default A.6.RCD disposition is **local compound relation-bearing claim**. For an ordinary positive answer, the practitioner **MUST**:

1. name the receiving action or decision, state what it must decide, and select one production question;
2. recover the exact participants, direct predicates, applicability facts, and boundary facts needed by that question;
3. state the smallest readable conjunction of those governed facts and the one answer it supports, or return the exact missing-information, missing-governor, criterion, applicability, work-granularity, or boundary-state blocker; and
4. keep any durable answer in one truthful C.2.1 episteme with exact claim content, one exact `EntityOfConcern`, and an effective `U.ReferenceScheme`, then stop without introducing a relation kind, relation signature, or relation occurrence.

This ordinary positive branch does not require the practitioner to name a substrate document, constructor, hidden-witness policy, polarity algebra, or ordered-boundary operator. It requires the governed facts and a readable answer. Open author-side semantic replay only when A.6.RCD:4.2 requires a substrate pin—nontrivial, interoperability-facing, proof-bearing, high-consequence, or reusable use—or when the current negative claim or first-satisfying-boundary claim actually depends on negation, witness, ordering, or earliest-boundary semantics.

**Branch constructor semantics for the triggered replay.** These are branch-local claim constructors, not a universal production algebra:

| Branch | Least constructor over governed base claims | Hidden-participant, polarity, and time policy |
| --- | --- | --- |
| production-work participation | one typed conjunction over exact A.15.1 work identity, actual method enactment, method applicability and intended production effect, affected referent, direct work-to-change facts, the receiver's current criterion, and either exact work identity or one exact A.15.1 proper-part relation | every participant and conjunct remains named; no projection hides work, transformation, or criterion witnesses; a negative result requires the selected substrate's explicit negation law rather than absence of a base assertion |
| entity-identity inception | one time-indexed conjunction over identity-specification applicability, exact work and governed effects, direct work-to-change and change-to-identity links, and satisfaction of the applicable identity predicate, followed by the substrate's earliest-satisfying-boundary selection over its declared ordered candidate-boundary domain | the candidate basis remains distinct from the after-side entity; work parts and actual transformations remain named or follow the substrate's explicit witness policy; incomparable minimal work composites remain plural, and A.15.PROD supplies no arbitrary minimization rule |
| production completion | one boundary-indexed conjunction first states criterion satisfaction for exact `completionSubject`; a second conjunction states exact `productionWork`, that satisfaction claim, and the declared closure predicate or local closure rule | the claims keep their different entities of concern; no earliest-boundary operator is implied unless separately required, and missing closure semantics preserves satisfaction while blocking only Work completion |

For DPF or FPF authoring and every other pin-triggering use, the responsible author or modeler **MUST** name the exact selected substrate and edition and replay its constructor inputs, output claim, applicability, hidden witnesses, polarity law, and temporal policy. A negative or earliest-boundary claim **MUST** recover the specific negation, witness, ordering, or selection semantics it consumes even when no broader replay is needed. If no current substrate supplies semantics that the claim actually requires, return the exact **missing-substrate blocker**. A.15.PROD supplies no fallback operator.

For an ordinary positive result, the truthful `EntityOfConcern` is exact `currentWork` for production-work participation and exact `producedEntity` for entity-identity inception. Completion uses exact `completionSubject` for the state-satisfaction episteme and exact `productionWork` for a separate Work-completion episteme. A modeler **MUST** split claim content that cannot truthfully concern one exact entity and **MUST NOT** manufacture a union concern from work, method, transformations, criteria, evidence, and receivers.

Repeated use within one subject practice may justify one predicate-definition episteme, with the subject pattern locating the ClaimGraph that defines those participant meanings. Consider a subject-specific derived relation kind only when a named later action must also refer again to the same obtaining relation occurrence. The subject definition must then state obtaining, applicability, base dependencies, recurrence, and occurrence identity. A.6.RCD defines that candidate-construction branch; A.15.PROD defines no such kind admission by itself.

#### A.15.PROD:4.8 - Separate recognition from assurance

**Recognition branch for ordinary work.** The practitioner **SHOULD** ask only three questions:

1. Which is current: **did this Work count as production work, when did this exact entity first exist, or when was production completed?**
2. What happened, to which existing referent or pre-inception candidate basis, and at what boundary? If first existence is current, which entity exists only after that boundary? Name only the Work or work part, method, transformations, identity rule or completion criterion, declared predicates, applicability, and boundary facts needed to decide that question.
3. What one readable answer do those facts support, and what should the receiver do next? If one deciding fact or governor is absent, return its exact blocker instead of opening the other production questions.

A positive local answer can stop at that readable conjunction. It does not require substrate vocabulary. Open only the specific semantic replay needed when the answer is negative, when first existence requires an ordered earliest-boundary judgment, or when A.6.RCD:4.2 triggers a substrate pin. The practitioner **MUST** stop when the local answer is readable and grounded and **MUST NOT** fill the rest of this pattern as a record.

**Assurance branch for authors and high-consequence use.** Replay the exact basis in six visible groups:

- **Work and Method.** Check exact work identity and every relied-on work-part relation, the actual `enactsMethod` relation, method applicability, and the intended production effect.
- **Actual change and entity inception.** Check every work-to-change and change-to-identity predicate and retain the explicit non-inference from work or method composition to transformation composition.
- **State satisfaction and Work closure.** Check every criterion-applicability fact and boundary-state satisfaction fact. Keep the state-satisfaction claim separate from the closure predicate or local claim that closes the Work.
- **Claim epistemes and their current basis.** Check the exact identity-specification and completion-criterion epistemes, the named applicability predicate or filled local claim for each episteme at its claimed boundary, any separately current C.2.1 `EpistemeEditionRelation`, C.2.1 identity, and the evidence-use relations actually relied on.
- **Positive and discriminating cases.** Replay both, so removal of one deciding fact blocks only the claim that consumes it.
- **Pinned author substrate.** When A.6.RCD:4.2 requires a pin, DPF and FPF authors **MUST** record the selected substrate and edition and expose direct base predicates, applicability, hidden participants, polarity law, boundary domain and ordering, witness policy, and every earliest-boundary rule used by the claim.

Assurance may warrant reliance on the claim; it does not constitute work, change, entity inception, or completion.

**Assurance scope by use.** Match the replay to the actual use:

- A modeler whose declaration or model carries one local claim **MUST** check exact claim content, one truthful `EntityOfConcern`, reference scheme, participants, declared predicates, polarity, and boundary indexing.
- A practitioner or conformance reviewer **MUST** verify that the three-question first move reaches either one grounded local answer or one exact blocker and then stops.
- A pattern author or reviewer **MUST** also replay the worked and discriminating cases, neighbor-authority boundaries, checklist, and no-mint disposition.

None of these assurance uses widens the recognition claim or adds a world-side production fact.

#### A.15.PROD:4.9 - Run the recovery sequence and stop deliberately

**Ordinary sequence.** The practitioner **MUST** stop at the first grounded answer or exact blocker:

1. name the receiving action or decision and select one production question; if several are current, handle them one at a time as separate claims;
2. recover only the exact Work, work-part, method, affected-referent, transformation, identity-specification or completion-criterion, applicability, and boundary facts needed by the selected question;
3. select the whole-work or proper-part branch when production-work participation is current;
4. state one readable conjunction and its positive answer, or return the exact blocker naming the missing fact, governor, applicability basis, criterion, work granularity, or boundary state; and
5. if another person, tool, or later decision must reuse the answer, publish it as one local C.2.1 claim episteme; otherwise keep the readable answer local, then stop. Open delivery, acceptance, release, publication, availability, result, evidence, assurance, or relation-kind questions only when the named action or decision asks one of them; none follows from the production answer.

##### Triggered author replay

Continue beyond the ordinary sequence only for an A.6.RCD:4.2 pin-triggering use or when a negative or earliest-boundary answer consumes additional semantics:

6. name the branch-local constructor and, when a pin is required, the exact substrate and edition; expose only the constructor inputs, applicability, hidden-participant or witness policy, polarity law, boundary domain and ordering, and temporal rule that can change this answer;
7. for entity inception, verify the ordered candidate-boundary domain and earliest-satisfying rule; for a negative claim, verify the applicable negation law; for completion, keep the claim indexed by its criterion, applicability basis, and boundary;
8. if one required operator or substrate is unavailable, return the exact missing-substrate blocker rather than lowering the absence to a negative production answer; and
9. stop after the author replay returns the same ordinary answer or blocker.

#### A.15.PROD:4.10 - Pattern NameCard

This NameCard names the recovery pattern, not a relation kind. It uses F.18's expanded identity-bearing form with a direct local-sense claim because no separately recoverable F.17 SenseCell is current for this local naming settlement:

```text
NameCard:
  NameCardId: NC-A15-PROD-PATTERN
  GovernedValueRef: the A.15.PROD pattern that separates and recovers production-work participation, entity-identity inception, and production-completion claims
  SubjectPatternLocator: A.15.PROD
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-A15-PROD-PATTERN.ClaimGraph — complete C.2.1 U.ClaimGraph constituted by all identity-bearing naming-settlement claims designated below
  LocalSenseRef: local expression `Production Work, Entity-Identity Inception, and Production Completion Recovery`; sense claim: the A.15.PROD recovery pattern asks which of the three production questions is current while keeping actual work, first existence, completion, delivery, acceptance, release, publication, and availability distinct under FPFCoreReferenceScheme
  TechLabel: Production Work, Entity-Identity Inception, and Production Completion Recovery
  PlainLabel: separate production work, when this exact entity first exists, and when production was completed
  CandidateSet: Production Work, Entity-Identity Inception, and Production Completion Recovery; Entity Production by Work; Entity-Identity Inception Through Work; Production Boundary Recovery
  CandidateCoverage: recovery-pattern, entity-production, entity-inception, and boundary-recovery head families; no plausible current family remains untested
  RejectedCandidates:
    Entity Production by Work: hides whether the claim concerns work participation, first existence of the entity, or completed production
    Entity-Identity Inception Through Work: omits production work before and after first existence and omits production completion
    Production Boundary Recovery: uses a generic boundary head and does not expose the three governed questions
  SelectionRationale: the selected title names the three distinctions that the pattern must recover and makes the completion kind explicit; it cannot be parsed as one binary or ternary production relation
  LineageEntries: initial durable settlement; the selected Tech and Plain labels are current; this card asserts no alias, rename, split, merge, or retirement
  RefreshCondition: reopen naming if repeated subject use justifies an admitted derived relation kind or one question needs a separate primary EntityOfConcern and recovery algorithm
```

