---
chunk_kind: "child"
pattern_id: "A.15.PROD"
pattern_title: "Production Work, Entity-Identity Inception, and Production Completion Recovery"
section_id: "A.15.PROD:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.PROD/A.15.PROD__006_archetypal-grounding.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.15.PROD — Production Work, Entity-Identity Inception, and Production Completion Recovery"
  - "A.15.PROD:5 — Archetypal Grounding"
line_start: 28158
line_end: 28310
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.15.2"
  - "A.15.6"
  - "A.3.1"
  - "A.3.4"
  - "A.6.1"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "E.18.1"
  - "E.24.PUB"
  - "F.18"
  - "F.6"
  - "G.11"
keywords:
---

### A.15.PROD:5 - Archetypal Grounding

#### A.15.PROD:5.1 - Car 42 and the required nut

**Identity boundary.** Car 42 already satisfies its identity rule before `NutFasteningWork-42`.

**Assignment declaration.** `Car42FasteningAssignmentSpecies` is a directly declared `U.SystemRoleAssignment` species. Its ordered participant positions are holder and assigned system-role kind; their domains are `U.System` and `Car42FasteningPerformerSystemRoleKindDomain`.

**Assignment occurrence rule.** The species applies to Car-42 fastening Work and says that its holder supplies the fastening contribution as `Car42FasteningPerformerSystemRole` throughout the declared interval. Holder, assigned-kind value, and that uninterrupted interval identify one occurrence.

**Work and Method basis.** The common route in section 4.2 is instantiated here: A.13 recovers `FasteningCell-7 : U.System` through obtaining `Car42FasteningAssignment-42`; A.15.1 independently admits `NutFasteningWork-42` with its enacted fastening Method. Because this case consumes precise assignment-bound attribution, F.6 then relates the admitted Work through the same assignment.

**Actual-change basis.** A.3.4 separately identifies `Car42FastenerAttachmentTransformation`. It concerns the same continuing car and does not bring Car 42 into existence.

**Whole-work branch for the narrow use.** `NutFasteningWork-42` can be the whole `productionWork` when its fastening method is applicable and `FasteningWorkChangedAttachment@Car42(work, transformation)` obtains for that Work and `Car42FastenerAttachmentTransformation`.

**State satisfaction.** At the fastening boundary, `Car42FinishingStateSatisfactionClaim` has exact EntityOfConcern `Car42` and states that the car satisfies `Car42FinishingCriterion-v1`.

**Work closure.** Separately, subject-bounded `Car42FasteningClosureRule-v1` supports `Car42FasteningWorkCompletionClaim`, whose EntityOfConcern is `NutFasteningWork-42`, because the required attachment state is satisfied and no required fastening activity remains for this narrow use.

**Wider-work contrast.** For the broader factory use, the same occurrence can be a proper operational part of `CarProductionWork-42` under an exact A.15.1 part relation. The verb *fasten* and narrative order decide none of these claims.

**Cold-practitioner replay.** Applying section 4.7 to the case facts returns: **this Work completed the required fastening for this use; Car 42 already existed**. Missing `FasteningWorkChangedAttachment@Car42` returns `missing-governor[CAR42-FASTENING-WORK-TO-CHANGE]`. Missing `Car42FasteningClosureRule-v1` preserves `Car42FinishingStateSatisfactionClaim` and returns `missing-governor[CAR42-FASTENING-WORK-COMPLETION]`. The author-side counterfactual uses `Car42FasteningPredicates-v1` for the Work-to-change predicate and `Car42-Claims-v2` for the separate state-satisfaction and Work-completion claims; removing each deciding fact separately reproduces those two results without introducing a universal production or completion relation kind.

#### A.15.PROD:5.2 - Incomplete but identifiable Ship 27

**Identity rule and applicability.** Exact ship-identity specification episteme `SHIP-ID-2` states the hull-closure rule. Local applicability claim `ShipIdentitySpecApplies-2` applies it to exact candidate hull basis `Ship27-HullBasis`, exact yard context `Yard-27`, and the ordered candidate boundaries ending at `inceptionBoundary`.

**Entity inception before later Work ends.** Exact hull-assembly work can close that specification's rule at `inceptionBoundary` while outfitting, software installation, trials, and commissioning continue. The resulting inception claim concerns when Ship 27 first exists and remains indexed by `SHIP-ID-2` and `ShipIdentitySpecApplies-2`.

**Ordinary answer.** Ship 27 first exists at `inceptionBoundary` under that exact specification and applicability basis; later Work continues, and production completion remains a separate question.

**Continuing edition — assignment declaration.** `ShipIdentityRuleRevisionAssignmentSpecies` is a directly declared `U.SystemRoleAssignment` species. Its ordered positions are holder and assigned system-role kind, with holder domain `U.System` and assigned-kind domain `ShipIdentityRuleReviserSystemRoleKindDomain`.

**Continuing edition — assignment predicate.** The predicate applies to ship-identity revision Work in `Yard-27` under `ShipIdentityRuleRevisionMethod`. It obtains when the holder supplies that revision contribution throughout the declared interval. Holder, assigned-kind value, `Yard-27`, and that uninterrupted interval identify one occurrence.

**Continuing edition — Work and Method.** Applying the common route in section 4.2, A.13 recovers `YardIdentityGovernanceSystem` through obtaining `ShipIdentityRuleReviserAssignment-2R`, whose assigned-kind value is `ShipIdentityRuleReviserSystemRole` and whose interval covers the full Work. A.15.1 independently admits `ShipIdentityRuleRevisionWork-2R` with the enacted revision Method. Because this branch consumes precise assignment-bound attribution, F.6 then relates the admitted Work through that same assignment.

**Source expression and predicate.** C.2.P recovers the source expression *hull assembly closes Ship 27 identity* in `SHIP-ID-2`. Predicate-definition episteme `YardRevisionSourceUsePredicates-v1` declares case-local predicate `usesAsRevisionSource(work, sourceEpisteme)` with participant order `<revision Work, source episteme>`.

**Source-use obtaining test.** The predicate applies only to ship-identity revision Work under `ShipIdentityRuleRevisionMethod`. It is true only when that Method application opens the source episteme and uses the selected source claim as a premise.

**Edition basis.** The exact source-use participants are `ShipIdentityRuleRevisionWork-2R` and `SHIP-ID-2`. The revision Work opens `SHIP-ID-2`, selects its hull-closure claim as an explicit premise, and produces `SHIP-ID-2R`, whose separate C.2.1 ClaimContent says that hull assembly plus installed propulsion closes Ship 27 identity. Those facts make `usesAsRevisionSource(ShipIdentityRuleRevisionWork-2R, SHIP-ID-2)` obtain.

The applicable continuity rule for this specification family requires exact use of `SHIP-ID-2`, preservation of the ship EntityOfConcern and listed identity claims, and explicit identification of the corrected claim content without a reference-scheme retargeting. The current source use and preserved and deliberately changed features satisfy that rule, so `ShipIdentitySpecEdition-2-to-2R : EpistemeEditionRelation` obtains for `SHIP-ID-2` and `SHIP-ID-2R`. The performer, Method, Work, provenance, and replacement facts supply evidence for the test; no label makes continuity true. The lineage carries forward neither old applicability nor a new inception boundary.

**Lineage blockers.** Keep the two failures distinct:

- If the source-use predicate is not defined, return `missing-governor[SHIP-IDENTITY-REVISION-SOURCE-USE]`.
- If its definition is current but the actual premise-selection facts cannot be recovered, return `missing-information[SHIP-IDENTITY-REVISION-SOURCE-USE]`.

Either result keeps `SHIP-ID-2R` usable as a separately identified specification episteme but blocks `ShipIdentitySpecEdition-2-to-2R`. A similar title, later date, common publisher, or bare provenance edge does not restore that lineage.

**Non-continuing replacement.** `SHIP-ID-3` is another exact specification episteme, but this fixture establishes no `EpistemeEditionRelation` from `SHIP-ID-2` or `SHIP-ID-2R` to it. A later date, similar ship terminology, and use by the same yard do not make it an edition. A use selecting `SHIP-ID-3` must establish its applicability independently and constitute a separately qualified C.2.1 claim or return the exact blocker; lineage-based refresh cannot substitute it for either earlier specification.

The continuing edition reopens dependent current uses through the named lineage. The non-continuing replacement opens a new applicability question without altering earlier claims.

**Author-side substrate.** Exact substrate edition `YardIdentityHistory-v3` defines time-indexed conjunction over the named work, applicability, actual-effect, work-to-change, change-to-identity, and identity-satisfaction claims. It also defines earliest selection over its declared ordered candidate-boundary domain.

The positive replay returns exact boundary `tI` because the identity predicate stated by `SHIP-ID-2` is false at every earlier candidate boundary and true at `tI`. Exact Work and transformation witnesses remain named.

**Nearest substrate failure.** A snapshot substrate can conjoin facts at `tI` but supplies no ordered boundary domain or earliest-selection law. It cannot establish inception even if a later image satisfies the rule, so the branch returns the exact missing-substrate blocker rather than treating first observation as first existence. The example adds no universal earliest operator or arbitrary minimal-work selection.

**Designation is not identity.** The current IMO integrated scheme uses an IMO ship identification number as a stable designator across later flag, name, ownership, or type changes and states that allocation does not define ship status. Ship identity and continuity therefore still require their applicable subject rules. If the receiving use cannot recover a separate ship-identity rule for this candidate basis and boundary, the inception branch returns the exact identity-governor blocker.

**Larger Work.** A larger exact production-work occurrence contains the identity-closing and later Work through declared A.15.1 part relations.

**State satisfaction.** At `completionBoundary`, one claim may state that Ship 27's actual state satisfies the applicable completion criterion.

**Work closure.** A separate yard closure predicate or local claim must connect that satisfaction to completion of the larger production Work. Without it, preserve the state claim and return `missing-governor[SHIP27-PRODUCTION-WORK-COMPLETION]`.

Delivery, class acceptance, and operational release remain separate. The sentence `the yard produced Ship 27` is admissible only after the writer selects Work participation, first existence, state satisfaction, or Work completion.

#### A.15.PROD:5.3 - Nested and concurrent attribution

**Work structure.** Factory work may contain project work, subassembly work, `identityClosingWork`, and completion-closing work. Every selected work-part relation remains explicit. Jointly necessary concurrent work parts use exact composite work under A.15.1.

**Plural minimal composites.** Two incomparable minimal work composites yield two local inception claims, each indexed by its exact identity-specification episteme and applicability basis. Nested or concurrent attribution creates no additional inception occurrence, and none of those work compositions establishes transformation composition.

**Epistemic basis remains separate.** The identity-specification and completion-criterion epistemes remain cited by the local claims. Each applicability basis remains its named predicate or filled local claim, and any C.2.1 edition relation between such epistemes is separate. None is a work participant.

#### A.15.PROD:5.4 - Pressure adjustment without entity inception

**Work, Method, and change.** A dated pressure-adjustment Work occurrence may enact an exact pressure-adjustment method, while A.3.4 independently identifies a pressure transformation.

**Work-to-change claim.** Open a positive claim only when the subject practice supplies a named predicate with Work and transformation participant positions and the case facts make that predicate obtain. Otherwise keep the two occurrences separate and return `missing-governor[pressure-work-to-change]`.

**Stop.** If the affected vessel or process already exists and no production-completion criterion is current, the result records the exact Work, the exact transformation, and their obtaining Work-to-change predicate. The production-work-participation, entity-inception, and completion branches remain unopened.

#### A.15.PROD:5.5 - PumpSkid assembly before PumpSkid identity

**Actual Work and change.** Mounting, wiring, fluid-connection, and whole-configuration changes may each be independently identified under A.3.4, and exact work parts may be grounded under A.15.1.

**Inception basis.** A PumpSkid inception claim may proceed only when a named applicability predicate or filled local claim applies the exact PumpSkid identity-specification episteme to the candidate configuration and boundary. Named Work-to-change and change-to-identity predicates must also obtain for the actual participants and case facts. A missing applicability or link returns its exact blocker.

**Transformation-composition boundary.** A claim that additionally requires positive composite-transformation identity or transformation parthood stops at `missing-governor[transformation-composition]`. Work or method decomposition supplies no proof of transformation decomposition.

#### A.15.PROD:5.6 - Completion persists after later destruction

**Historical positive case.** The product's state satisfied criterion episteme `PC-3` at boundary `tC`, and the subject-practice closure rule made that satisfaction sufficient to close the named production Work.

`CompletionHistory-v1` keeps the Work identity, applicability of `PC-3`, subject-state facts at `tC`, state-satisfaction claim, and separate Work-completion claim explicit. The two claims keep their different entities of concern. The history uses the declared boundary and does not apply an earliest operator. Record a later accident and destruction in separate claims while retaining the historical claims at `tC`.

**Nearest historical failure.** Keep the later certificate or an unindexed current-state predicate, but remove the semantics that say the subject satisfied `PC-3` at `tC`. The historical check then returns the exact missing-substrate blocker; neither the certificate nor the current-state predicate supplies the missing boundary-indexed satisfaction or Work-completion basis.

If only the closure rule is missing, the state-satisfaction claim remains and only Work completion returns its exact missing governor. Current evidence, availability, replacement Work, acceptance status, and insurance decisions remain separate.

#### A.15.PROD:5.7 - Non-agentive biological synthesis

**Actual transformation.** A spontaneous reaction or biological growth process may be independently grounded as one or more actual transformations under A.3.4. The transformed referent may itself be a `U.System`; the performer question remains separate.

**Performer and Work result.** Apply the common route in section 4.2. A production-through-Work claim opens only after A.13 recovers every exact actual performer and A.15.1 independently admits dated Work with an applicable enacted Method. This fixture stipulates neither basis, so it retains the referent and transformations and returns the performer/Work blocker. Assignment-bound attribution and F.6 are additional only when the receiving use expressly consumes them; their absence is not itself a Work-membership failure.

Entity inception and completion then still need their own exact identity, state-satisfaction, and Work-closure governors. Do not turn observed growth into the missing performer-side basis.

#### A.15.PROD:5.8 - Scrum Increment before review or release

**Product-state and identity basis.** The Scrum Guide and one exact organizational Definition of Done episteme are authoritative practice sources for this bounded software-product use. When `PBI-84` first satisfies that criterion at `tD`, the local product-state and Increment-identity claims may be stated under their exact applicability rules. Work that does not meet that Definition of Done is not part of the Increment.

**Review and release stay separate.** Multiple Increments may exist before Sprint Review, and review is not a release gate.

**Current A.15.PROD use.** The pattern may use the applicable Definition of Done for the state-satisfaction or identity question it actually answers, while keeping Sprint Review, delivery, and release separate.

**Work-completion boundary.** The guide does not identify exact A.15.1 Work, its performer basis, or a local predicate that makes satisfaction close that Work. A Work-completion claim therefore needs an additional subject-practice closure governor. Otherwise keep the product-state claim and return the exact Work-completion blocker.

#### A.15.PROD:5.9 - ReleaseBinary 12: complete build-to-inception replay

BuildOps asks one question: **when did exact `ReleaseBinary_12` first exist?** Verification, transfer, release, deployment, publication, and availability are not part of this answer. The fixture uses one affected referent and one transformation; it does not hide an unnamed effect chain.

**Ordinary answer.** The runner performed the named Work under the applicable build Method. The named Work-to-change predicate connects that Work to the store-population transformation, and the named change-to-identity predicate says that the transformation made the applicable binary-identity rule become true first at 09:11. Therefore **`ReleaseBinary_12` first exists at 09:11 through this build Work; decide completion and later uses separately.** The table below supplies the exact assurance basis for that answer.

| Needed fact | Exact case fact |
| --- | --- |
| Work, performer, and method | Applying the common route in section 4.2, A.15.1:6.7.1 first reuses `BuildRunner_A : U.System`'s A.13 core for this action, including the exact direct assignment species and obtaining occurrence `BuildRunnerAssignment_2026-07-21`; A.15.1 then independently admits `ReleaseBinary12_BuildWork_2026-07-21T0900_0912 : U.Work` from its performance history, enacted Method `ReproducibleBuild@BuildOps-v12`, interval 09:00–09:12, and the obtaining `BuildWorkOccursWithinServiceBoundary` relation to `BuildService_A`. Because this case claim consumes attribution under that assignment, F.6 then establishes the exact relation. The enacted Method states the intended effect of producing an immutable binary. Method-applicability claim `ReproducibleBuildApplies-12` applies that Method to exact build input and configuration `BuildInputSet_12`. |
| Application and candidate basis | After the produced entity exists, A.6.1 application `BuildApplication_12` has result binding `builtBinary -> ReleaseBinary_12`; that binding designates the returned entity but establishes neither its inception nor its boundary. The same identified application is an application of declared operation `storeWrite@BuildOps-v12` and has argument binding `storeTarget -> ArtifactStorePartition_12`; A.15.1:6.7.1 uses this application and binding in the obtaining test for the named Work-to-transformation predicate below. Before inception, `BuildOutputBasis_12` designates the candidate bytes, manifest, digest, and their positions in that partition, not a surrogate future binary. |
| Actual transformation | A.3.4 independently identifies the one transformation consumed here: `ArtifactStorePopulationTransformation_12 : U.Transformation`, the change of `ArtifactStorePartition_12` from no complete candidate tuple at 09:00 to the written bytes, manifest, and digest at 09:11, after which that tuple remains fixed through build completion at 09:12. |
| Work to change | A.15.1:6.7.1's BuildOps relation specification declares `BuildWorkPopulatedStore@BuildOps-v12(work, transformation)` with participant order `<work, transformation>`. Its stated test and the stipulated Work, application, target-binding, and transformation facts make `BuildWorkPopulatedStore@BuildOps-v12(ReleaseBinary12_BuildWork_2026-07-21T0900_0912, ArtifactStorePopulationTransformation_12)` obtain. Shared timing or the result binding alone would not establish this predicate. |
| Identity criterion and applicability | Predicate-definition episteme `ReleaseBinaryIdentitySpec_v12` says that this BuildOps binary exists when one immutable byte sequence, manifest, and digest are fixed together and addressable by that digest in `ArtifactStorePartition_12`. Applicability claim `ReleaseBinaryIdentitySpecApplies-12` applies that episteme to `BuildOutputBasis_12`, the BuildOps-v12 context, and the ordered candidate boundaries from 09:00 through 09:12. This is the criterion episteme for the selected inception question; `BuildCompletionCriterion_v12` belongs to the separate completion question at 09:12. |
| Change to identity | BuildOps predicate-definition episteme `ReleaseBinaryIdentityPredicates-v12` declares case-local predicate `StorePopulationClosedBinaryIdentity@BuildOps-v12(transformation, identitySpecification, candidateBasis, boundary, producedEntity)` with that participant order. Its test requires the governed store change to make the applicable identity rule false at every earlier candidate boundary and true at the named boundary. The stipulated case facts make it obtain for `<ArtifactStorePopulationTransformation_12, ReleaseBinaryIdentitySpec_v12, BuildOutputBasis_12, 09:11, ReleaseBinary_12>`. |
| Local result | C.2.1 episteme `ReleaseBinary12InceptionClaim` has exact `EntityOfConcern = ReleaseBinary_12` and states only that this entity first exists at 09:11 through the governed effects of `ReleaseBinary12_BuildWork_2026-07-21T0900_0912` under `ReleaseBinaryIdentitySpec_v12` and `ReleaseBinaryIdentitySpecApplies-12`. It asserts neither build completion nor verification, transfer, acceptance, release, deployment, publication, or availability. |

**Nearest failing variant.**

Keep every fact above, including the result binding, store transformation, work-to-change predicate, identity specification, applicability, ordered boundaries, and the state that satisfies the identity rule at 09:11. Remove only the declaration and obtaining fact for `StorePopulationClosedBinaryIdentity@BuildOps-v12`.

The exact result is `missing-governor[RELEASE-BINARY-CHANGE-TO-IDENTITY]` for `<ArtifactStorePopulationTransformation_12, ReleaseBinaryIdentitySpec_v12, BuildOutputBasis_12, 09:11, ReleaseBinary_12>`. A timestamp, completed write, or `builtBinary` binding cannot replace that missing change-to-identity predicate.

**Author-side replay of the same result.** Case substrate `ReleaseBinaryInceptionClaims-v1` defines a time-indexed conjunction over the named Work, performer basis, method applicability, the performed `storeWrite` application fact (not the later result binding), affected referent, transformation, work-to-change predicate, identity specification, applicability claim, and change-to-identity predicate.

Its declared ordered boundary domain is 09:00-09:12, and its earliest-satisfying rule returns 09:11. The positive replay therefore yields `ReleaseBinary12InceptionClaim`.

In the failing variant, the same constructor lacks exactly the change-to-identity conjunct and returns `missing-governor[RELEASE-BINARY-CHANGE-TO-IDENTITY]`, exactly as the ordinary replay does. These case-local predicates and this substrate introduce no universal production, work-to-change, or change-to-identity relation kind.

