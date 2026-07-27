---
chunk_kind: "child"
pattern_id: "A.15.PROD"
pattern_title: "Production Work, Entity-Identity Inception, and Production Completion Recovery"
section_id: "A.15.PROD:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.PROD/A.15.PROD__002_problem-frame.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.15.PROD — Production Work, Entity-Identity Inception, and Production Completion Recovery"
  - "A.15.PROD:1 — Problem Frame"
line_start: 26212
line_end: 26247
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

### A.15.PROD:1 - Problem Frame

**Use this when.** Practitioners **SHOULD** use this pattern when work is said to have *made*, *produced*, *built*, *assembled*, *grown*, *generated*, *finished*, or *completed* something and the receiving decision needs to know which exact production question is true. They **SHOULD** prefer it when one work occurrence is nested in larger work, several work parts act concurrently, an entity becomes identifiable before all work ends, or completion is being confused with delivery, acceptance, release, publication, or availability.

**Primary EntityOfConcern by selected branch.** Production wording is the umbrella. Each application narrows to one exact local claim whose C.2.1 `EntityOfConcern` is exact `currentWork` for production-work participation, exact `producedEntity` after inception for entity-identity inception, or exact `productionWork` for production completion. When more than one branch is current, each branch retains its own claim episteme and `EntityOfConcern`; one manufactured union concern is inadmissible.

**Primary working reader.** A practitioner or modeler responsible for settling one of these production, identity, or completion questions for a current engineering, manufacturing, construction, lifecycle, audit, or scientific use before relying on delivery, acceptance, release, publication, or availability.

**Primary viewpoint.** The practitioner **SHOULD** recover the smallest receiver-relevant claim: select one branch, identify its exact `EntityOfConcern`, and stop when that branch is decided or its exact blocker is known. This pattern is not a form to fill in.

**First useful move.** The practitioner **SHOULD** first ask which answer the receiving action or decision needs now:

1. Is this dated Work the whole production Work for this use, or a declared proper part of it?
2. Which identity rule applies to the candidate, and at what boundary did changes attributed to this Work first make that rule true so this entity began to exist?
3. Which completion criterion applies to this production Work, and at what boundary did the actual state satisfy it?

The practitioner **MUST NOT** answer one question with evidence for another.

**What goes wrong if missed.** Any work-caused change is called production; an entity is treated as existing before its identity rule first holds; a finishing operation is mistaken for entity creation; a plan, log, post-state picture, or first observation is treated as the change-producing link; and later delivery or acceptance silently rewrites historical completion.

**What this buys.** Teams can attribute production work at the right work boundary, state when one entity first exists, and preserve historical completion without inventing a universal relation kind. Narrow and larger production readings can coexist through exact work-part relations. Identity, completion, rework, delivery, acceptance, release, publication, and availability remain independently inspectable.

**Cross-domain recognition test.** These three non-exhaustive recognition situations show that the same three production questions remain separate across heterogeneous practice:

| Recognition situation | First current question | Blocked overread |
| --- | --- | --- |
| A fastening step is said to have "produced Car 42". | Is the step whole production work or a proper part, did Car 42 already exist, and which completion criterion is current? | The last visible step establishes neither first existence nor completion by narrative order. |
| A culture run or spontaneous biological process is said to have "produced Batch B17". | Did one exact system under an obtaining role assignment enact a method in dated work, and only then which identity or completion branch is current? | Growth or reaction alone may ground actual transformation but establishes no Work occurrence admitted under `U.Work` and no production-through-work claim; a batch label, sample, or first observation closes none of those questions. |
| A build pipeline is said to have "produced ReleaseBinary 12". | Which dated build work and governed effects first established the exact artifact identity, or satisfied the build-completion criterion? | Build success, publication, release, deployment, and availability remain different claims. |

**So-what adoption test.** Would replacing the separate branch answers by one broad production sentence change what the receiver may rely on, schedule, audit, accept, release, or reopen? If yes, the practitioner **SHOULD** apply this recovery. If only one already-governed neighboring claim is current, the practitioner **SHOULD** use its direct pattern instead.

**Not this pattern when.** Practitioners **SHOULD** use `A.15.1` directly when the only question is what work occurred; `A.3.4` when the only question is what actually changed; `A.3.1` when the only question is the reusable way of doing; the direct identity pattern when only entity identity is current; or the direct evaluation, delivery, acceptance, release, publication, availability, evidence, or assurance pattern when only that neighboring claim is current. This pattern coordinates those objects only for a selected production-recovery question.

**No-mint disposition.** Authors and modelers **MUST NOT** introduce `U.ProductionWork` as a U-kind. They **MUST NOT** introduce `WorkProducesEntityRelation`, `EntityIdentityInceptionByWorkRelation`, `ProductionWorkRelation`, or `ProductionCompletionRelation` as universal relation kinds. The default result is one local C.2.1 claim episteme per selected question under A.6.RCD disposition 2. Repeated use of the same predicate with the same participant meanings in one subject practice may justify one reusable predicate-definition episteme in that practice's owning pattern. Consider a derived relation-kind candidate only when a named later action must refer again to the same obtaining relation occurrence rather than merely reuse the predicate; A.6.RCD and later admission govern that continuation.

