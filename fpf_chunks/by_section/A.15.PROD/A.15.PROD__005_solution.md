---
chunk_kind: "child"
pattern_id: "A.15.PROD"
pattern_title: "Production Work, Entity-Identity Inception, and Production Completion Recovery"
section_id: "A.15.PROD:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.PROD/A.15.PROD__005_solution.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.15.PROD — Production Work, Entity-Identity Inception, and Production Completion Recovery"
  - "A.15.PROD:4 — Solution"
line_start: 26040
line_end: 26205
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

The practitioner **MUST** recover only the selected production question, its exact work and subject objects, and the smallest governed base that answers it. The practitioner **MUST** publish each answer as a separate local compound relation-bearing claim and **MUST** stop or return an exact blocker wherever a required direct relation, criterion, applicability rule, boundary fact, work granularity, or transformation-composition governor is missing.

**Core and branch cut.** The common recovery core is receiver-first question selection, exact-object recovery, closure through direct governors or one local claim selected under A.6.RCD disposition 2, and a deliberate stop. The production-work, entity-identity-inception, and production-completion branches add only their own `EntityOfConcern`, criterion or boundary, and branch-specific base. One branch neither inherits facts from another nor turns the common method into an omnibus production object. Work identity, transformation identity, subject identity, evidence, assurance, delivery, acceptance, release, publication, and availability remain with their direct governing patterns.

#### A.15.PROD:4.1 - Split the three questions before recovering evidence

| Question | Claim content | Ordinary stopping result | What it does not establish |
| --- | --- | --- | --- |
| Production-work participation | exact `currentWork` is itself `productionWork`, or exact `currentWork` is a declared proper work part of exact `productionWork` | one local positive or negative compound claim, or an exact work-grounding blocker | entity inception, completion, delivery, acceptance, or a universal production-work kind |
| Entity-identity inception | governed actual effects of exact `identityClosingWork` made exact `producedEntity` satisfy the rule in exact applicable `productIdentitySpecificationEdition` for the first time at exact `inceptionBoundary` | one local inception claim after the entity exists, plurality of incomparable minimal claims, or an exact blocker | production completion, later persistence, acceptance, or a reusable binary relation kind |
| Production completion | exact subject-state facts satisfied exact `productionCompletionCriterionEdition`, applicable to exact `productionWork`, at exact `completionBoundary` | one historically indexed local completion claim or an exact blocker | entity inception, delivery, acceptance, release, publication, or availability |

The three claims may cite overlapping facts. They remain different claims because they answer different receiving questions and can have different boundaries, criteria, and truthful C.2.1 `EntityOfConcern` values.

#### A.15.PROD:4.2 - Recover the smallest exact base

The practitioner **MUST** use only objects needed by the selected branch:

| Working name | Exact object and governor | Required contribution |
| --- | --- | --- |
| `productIdentitySpecificationEdition` | one exact edition of a C.2.1 predicate-definition episteme owned by the direct subject pattern | states the identity rule before inception without pretending that a future entity exists |
| identity-specification applicability basis | exact direct subject-governed applicability relation or local compound claim selected under A.6.RCD disposition 2 | establishes that the exact edition applies to the candidate basis, subject context, and candidate `inceptionBoundary`; it introduces no universal applicability relation |
| `producedEntity` | one exact `U.Entity`, designated only after inception | is the entity whose identity rule first became true |
| `productionMethod` | one exact `U.Method` under A.3.1 | states the governed way of doing, intended production effect, applicability, and relevant identity or completion criterion meaning |
| `currentWork` | one exact Work individual admitted under `U.Work` by A.15.1 | designates the world-side dated occurrence; its performer through an obtaining `U.RoleAssignment`, actual `enactsMethod`, extent, bindings, resources, affected referent, and containing system obtain independently rather than being fields stored in the occurrence |
| `productionWork` | one exact Work individual admitted under `U.Work` by A.15.1 | designates either the same occurrence as `currentWork` or the exact larger Work occurrence of which `currentWork` is a declared proper part |
| `actualTransformation` | one or more independently identified `U.Transformation` occurrences under A.3.4 | names what changed without becoming the work or the produced entity |
| work-to-change basis | exact subject-governed direct relations or local compound claims selected under A.6.RCD disposition 2 | establishes that selected actual changes are effects of exact work; coincidence is insufficient |
| `productionCompletionCriterionEdition` | one subject-governed predicate-definition episteme | states the criterion edition applicable to exact production work at the candidate completion boundary |
| local assertion | one C.2.1 episteme | carries only the compound claim needed for one selected question |

A method description, work plan, objective, commitment, product specification, evaluation result, or publication enters only through its own direct relation when the receiving use depends on it. None is constitutive of every production occurrence.

#### A.15.PROD:4.3 - Select one production-work branch

**Whole-work branch.** `currentWork = productionWork` is admissible only when that exact dated work has the actual `enactsMethod` relation to `productionMethod`, the method's governed intended production effect and applicability are current, exact work-to-change facts obtain, and the identity or completion criterion required by the receiving claim is recoverable. A familiar broader production label establishes no parent work.

**Proper-part branch.** Exact `currentWork` is admissible as a proper part of exact `productionWork` only when `OperationalPartOf_work` or another exact A.15.1 work-part relation with fitting occurrence semantics obtains. Interval overlap or concurrency is asserted separately and establishes neither parthood nor coordination. The containing work needs the same grounding as the whole-work branch: dated work identity, enacted production method, intended effect and applicability, affected referent, exact work-to-change facts, and the current identity or completion criterion. A shared label, project membership, common referent, temporal containment, overlap, or adjacency in a plan establishes no work parthood.

The two branches can support different bounded uses. A nut-fastening occurrence can be the whole production work for a narrowly bounded finishing operation and also a proper part of a larger car-production occurrence, provided each local claim names its exact extent, criterion, and work relation. `productionWork` is a relation-defined reading of one Work occurrence admitted under `U.Work`, not an intrinsic kind.

#### A.15.PROD:4.4 - Ground actual effects without inventing transformation composition

The practitioner **MUST** recover every actual transformation independently through A.3.4: changed referent, exact extent or formal boundary, boundary conditions, actual before/during/after facts, and continuity or reidentification rule. The practitioner **MUST** then recover each work-to-change link under its direct subject governor or as a local compound claim selected under A.6.RCD disposition 2. Temporal overlap, a common changed referent, a delta expression, a log record, or a post-state picture does not establish the link.

One transformation identified at the resolution needed by the production claim establishes neither presence nor absence of finer transformation parts. Work parts, method parts, samples, temporal subdivisions, concurrent changes, and flow representations do not establish transformation parts or a composite transformation.

The recovery continues when the selected production claim needs only independently identified transformations. When it needs a positive composite-transformation identity, transformation parthood, or transformation holonhood and no accepted governor supplies that basis, the result is the exact missing-governor blocker. Composite `identityClosingWork` under A.15.1 does not cure that blocker and does not imply an isomorphic composite transformation.

#### A.15.PROD:4.5 - Recover entity-identity inception

**Definition: A15PROD-D1 (Entity-identity inception).** Entity-identity inception is the boundary at which exact `producedEntity` first satisfies the identity rule stated by exact `productIdentitySpecificationEdition` that the direct subject pattern makes applicable to the candidate basis, subject context, and boundary. Plain: **when this exact entity first exists**. `inceptionBoundary` is a case-local boundary designator, not a second technical term, claim kind, or relation kind.

For this branch, the practitioner **MUST** complete all five steps:

1. recover exact `productIdentitySpecificationEdition` as one C.2.1 predicate-definition episteme in the direct subject pattern before applying it. Before inception, the governed question remains about exact work, method, actual effects, that edition, and its candidate basis; no future `producedEntity` participant exists;
2. recover the direct subject-governed applicability basis by which that edition applies to the exact candidate basis, subject context, and candidate `inceptionBoundary`, together with the exact actual effects of exact work and the direct links by which those effects bear on that applicable rule;
3. find the earliest exact `inceptionBoundary` at which the rule in that applicable edition becomes true and designate the resulting exact `producedEntity` only on the after-side of that boundary; the pre-inception candidate basis remains distinct from that entity;
4. identify exact `identityClosingWork`, using the one closing work occurrence when it exists or, for jointly necessary concurrent or nested work parts, their exact composite work under A.15.1 and its declared work-part relations; and
5. publish a positive local inception claim only after exact `producedEntity` exists and the claim names exact `productIdentitySpecificationEdition`, its direct subject-governed applicability basis, exact `identityClosingWork`, exact `inceptionBoundary`, and all governed work-to-change and change-to-identity links.

A published local inception claim **MUST** be indexed by the exact specification edition and applicability basis used at `inceptionBoundary`. A later identity-specification edition does not silently rewrite that earlier claim. Changed applicability yields either a separately qualified claim under its new exact basis or an exact blocker; it does not move the earlier indexed boundary.

A delta expression, method description, work plan, log, post-state image, identity-rule episteme, or first observation establishes none of those links by itself. Absence of recoverable work granularity for `identityClosingWork` yields a **work-granularity blocker**. Several incomparable minimal work composites yield several local inception claims; narrative simplicity supplies no rule for selecting only one.

**Regulated-identification boundary.** A persistent identifier is not an inception criterion. A current subject practice that allocates an identifier at build or registration while keeping allocation separate from entity status supplies designation and continuity only. First existence requires a separately applicable subject-identity rule; its absence yields the exact identity-governor blocker. An assigned number does not make the candidate basis the after-side entity.

#### A.15.PROD:4.6 - Recover historically indexed production completion

A production-completion claim designates:

- exact `productionWork`;
- exact `completionBoundary` inside or at the end of that occurrence;
- exact `productionCompletionCriterionEdition` applicable to that occurrence at that boundary;
- the exact applicability relation; and
- governed subject-state facts that satisfied that edition at the boundary.

Completion is historical. Later damage, loss, destruction, delivery, rejection, acceptance, release, publication, or unavailability does not erase an earlier true completion claim. A later criterion edition does not rewrite the earlier claim. Rework or later production work that satisfies a criterion at a later boundary receives a separate local completion claim.

Entity-identity inception and production completion remain separate claims even when they share a boundary. The applicable identity-specification edition says when this exact entity first exists under its direct subject-governed applicability basis; the completion criterion says when the applicable production requirement was satisfied. A later evaluation-result episteme may support either assertion under a direct evidence-use relation, but it creates neither the boundary nor the subject state.

Past work, entity-identity inception, and production completion remain addressable after later destruction or evidence decay. A later assertion carries its own evidence currentness and reliance status. The produced entity, measurement or evaluation result, delivered entity, acceptance verdict, release, publication, availability, and downstream effect remain separately governed objects and claims.

**Practice-specific completion criteria stay local.** In current NASA systems-engineering practice, product implementation or integration, verification, validation, and product transition are distinct processes; a local completion claim therefore names the exact tailored product-layer criterion and does not substitute transition or delivery for verification or validation. In current Scrum practice, the applicable Definition of Done is a product-specific quality-state criterion and an Increment is born when a Product Backlog item first meets it; Sprint Review and release remain separate. These practice answers can supply an exact criterion or boundary only in their own applicability context. They supply neither the exact A.15.1 work occurrence nor a cross-domain universal completion rule.

#### A.15.PROD:4.7 - Publish local claims, not an omnibus relation

The default A.6.RCD disposition is **local compound relation-bearing claim**. For each selected question, the practitioner **MUST** complete all six actions:

1. name the exact receiving work or decision and the answer that closes it;
2. recover exact participants and direct relations under their own meanings;
3. state the least constructor admitted by the current substrate, its semantics, the governed base claim content it consumes, and any hidden-participant, polarity, applicability, or time policy that changes the result;
4. identify one truthful C.2.1 episteme with exact claim content, one exact `EntityOfConcern`, and an effective `U.ReferenceScheme`;
5. state positive or negative polarity only under the selected substrate's law; keep unresolved reliance or information sufficiency with its evaluation or evidence pattern; and
6. stop without introducing a relation kind, relation signature, or relation occurrence.

**Branch constructor semantics.** These are branch-local claim constructors, not a universal production algebra:

| Branch | Least constructor over governed base claims | Hidden-participant, polarity, and time policy |
| --- | --- | --- |
| production-work participation | one typed conjunction over exact A.15.1 work identity, actual method enactment, method applicability and intended production effect, affected referent, direct work-to-change facts, the receiver's current criterion, and either exact work identity or one exact A.15.1 proper-part relation | every participant and conjunct remains named; no projection hides work, transformation, or criterion witnesses; a negative result requires the selected substrate's explicit negation law rather than absence of a base assertion |
| entity-identity inception | one time-indexed conjunction over identity-specification applicability, exact work and governed effects, direct work-to-change and change-to-identity links, and satisfaction of the applicable identity predicate, followed by the substrate's earliest-satisfying-boundary selection over its declared ordered candidate-boundary domain | the candidate basis remains distinct from the after-side entity; work parts and actual transformations remain named or follow the substrate's explicit witness policy; incomparable minimal work composites remain plural, and A.15.PROD supplies no arbitrary minimization rule |
| production completion | one boundary-indexed conjunction over exact production work, exact criterion edition and applicability, and governed subject-state satisfaction at exact `completionBoundary` | the claim stays indexed by that boundary and edition; no earliest-boundary operator is implied unless the receiving use separately requires and the selected substrate defines it; negative polarity again requires an explicit substrate law |

A readable ordinary-use conjunction does not require a separately materialized substrate document when A.6.RCD:4.2 does not require one. For DPF or FPF authoring of a nontrivial, interoperability-facing, proof-bearing, high-consequence, or reusable claim, the responsible author or modeler **MUST** name the exact selected substrate and edition and **MUST** replay its constructor inputs, output claim, applicability, hidden witnesses, polarity law, and temporal policy. If no current substrate supplies the needed conjunction, boundary indexing, earliest-boundary selection, witness policy, or negation law, the result is the exact **missing-substrate blocker**. A.15.PROD supplies no fallback operator.
For an ordinary positive result, the truthful `EntityOfConcern` is usually exact `currentWork` for production-work participation, exact `producedEntity` for entity-identity inception, and exact `productionWork` for production completion. A modeler **MUST** split claim content that cannot truthfully concern one exact entity and **MUST NOT** manufacture a union concern from work, method, transformations, criteria, evidence, and receivers.

Repeated subject use may justify one predicate-definition episteme in the direct subject pattern. A subject-specific derived relation-kind candidate opens only when a named receiver also consumes stable relation-occurrence identity and the direct subject settlement can state obtaining, applicability, base dependencies, recurrence, and occurrence identity. A.6.RCD governs that continuation; A.15.PROD admits no such kind by itself.

#### A.15.PROD:4.8 - Separate recognition from assurance

**Recognition branch for ordinary work.** The practitioner **SHOULD** ask:

1. Which of the three production questions is current?
2. What exact `currentWork`, `productionWork`, method, affected referent, identity-specification or completion-criterion edition, and direct applicability basis are needed?
3. Which whole-work or proper-part branch obtains?
4. What independently identified actual transformations and direct work-to-change facts are required?
5. Does the exact identity-specification or completion-criterion edition apply at the stated boundary, and do the governed facts satisfy that edition?
6. Does the current substrate supply the branch's conjunction, boundary indexing, witness, polarity, and any earliest-boundary semantics?
7. Can one local compound claim close the receiving use now, or is the result the exact missing-substrate blocker?

The practitioner **MUST** stop when the local answer is readable and grounded and **MUST NOT** fill the rest of this pattern as a record.

**Assurance branch for authors and high-consequence use.** Authors and high-consequence users **MUST** additionally replay the exact work identity and part relations; the actual `enactsMethod` relation; method applicability and intended production effect; every work-to-change and change-to-criterion link; exact identity-specification and completion-criterion editions; the direct subject-governed applicability basis of each edition at its claimed boundary; boundary-state facts; positive and discriminating cases; C.2.1 identity; evidence-use relations; and the explicit transformation-composition non-inference. DPF and FPF authors **MUST** record the selected substrate and edition when A.6.RCD:4.2 requires a pin, and **MUST** expose direct base predicates, applicability, hidden participants, polarity law, boundary domain and ordering, witness policy, and any earliest-boundary rule used by the claim. Assurance may warrant reliance on the claim; it does not constitute work, change, entity inception, or completion.

**Assurance scope by use.** A modeler whose declaration or model carries one local claim **MUST** check exact claim content, one truthful `EntityOfConcern`, reference scheme, participants, direct governors, polarity, and boundary indexing. A practitioner or conformance reviewer **MUST** verify that the three-question first move reaches either one grounded local answer or one exact blocker and then stops. A pattern author or reviewer **MUST** also replay the worked and discriminating cases, neighbor-authority boundaries, checklist, and no-mint disposition. None of these assurance uses widens the recognition claim or adds a world-side production fact.

#### A.15.PROD:4.9 - Run the recovery sequence and stop deliberately

The practitioner **MUST** run the following sequence and **MUST** stop at the first grounded answer or exact blocker:

1. name the receiver and select one or more of the three questions;
2. recover exact work, method, affected referent, identity-specification or completion-criterion edition, its direct subject-governed applicability basis, and independently identified transformations only as needed;
3. select the whole-work or proper-part branch for production-work participation;
4. recover `identityClosingWork`, exact `productIdentitySpecificationEdition`, its applicability to the candidate basis and subject context at exact `inceptionBoundary`, and the earliest satisfying boundary only when first existence is current;
5. recover `completionBoundary`, applicable criterion edition, applicability relation, and boundary state only when completion is current;
6. select the branch-local constructor, state its semantics and governed base claims, and expose any hidden-participant, polarity, applicability, or time policy. For DPF/FPF authoring and other A.6.RCD:4.2 pin-triggering uses, the responsible author or modeler **MUST** name the exact substrate and edition;
7. publish one local C.2.1 claim episteme per answer;
8. return the exact blocker for any missing work granularity, direct governor, identity-specification or completion-criterion edition, direct applicability basis, boundary fact, required transformation-composition basis, constructor semantics, or current substrate; and
9. stop; delivery, acceptance, release, publication, availability, result, evidence, assurance, or relation-kind claims open only when the receiver independently needs them.

#### A.15.PROD:4.10 - Pattern NameCard

This NameCard names the recovery pattern, not a relation kind:

```text
NameCard:
  NameCardId: NC-A15-PROD-PATTERN
  GovernedValueRef: the A.15.PROD pattern that separates and recovers production-work participation, entity-identity inception, and production-completion claims
  GoverningPatternRef: A.15.PROD
  ReferenceScheme: FPFCoreReferenceScheme
  BoundedContextRef: FPF work, transformation, construction, production, and entity-identity use
  LocalSenseRef: recover which production question is current without collapsing actual work, the first existence of one entity, production completion, delivery, acceptance, release, publication, or availability
  TechLabel: Production Work, Entity-Identity Inception, and Production Completion Recovery
  PlainLabel: separate production work, when this exact entity first exists, and when production was completed
  CandidateSet: Production Work, Entity-Identity Inception, and Production Completion Recovery; Entity Production by Work; Entity-Identity Inception Through Work; Production Boundary Recovery
  RejectedCandidates:
    Entity Production by Work: hides whether the claim concerns work participation, first existence of the entity, or completed production
    Entity-Identity Inception Through Work: omits production work before and after first existence and omits production completion
    Production Boundary Recovery: uses a generic boundary head and does not expose the three governed questions
  SelectionRationale: the selected title names the three distinctions recovered by the pattern and makes the completion kind explicit; it cannot be parsed as one binary or ternary production relation
  RefreshCondition: reopen naming if repeated subject use justifies an admitted derived relation kind or one question needs a separate primary EntityOfConcern and recovery algorithm
```

