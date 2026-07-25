---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:8"
section_title: "Conformance Checklist (admission checks)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__010_conformance-checklist-admission-checks.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:8 — Conformance Checklist (admission checks)"
line_start: 24500
line_end: 24587
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.27.TA"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "F.6"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actual performer U.System"
  - "admitted U.Work kind"
  - "containing system"
  - "covering U.RoleAssignment"
  - "enacted method"
  - "optional direct bindings and resource use"
  - "performedUnderAssignment"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:8 - Conformance Checklist (admission checks)

**CC-A15.1-1 (Strict distinction).**
`U.Work` is the admitted kind for dated performed Work occurrences. Each Work individual is world-side; it is not a `U.Method` (semantic way), `U.MethodDescription` (description), `U.Role` or `U.RoleAssignment` (assignment), `U.WorkPlan` (plan or schedule), or assertion, record, log, or publication about work.

**CC-A15.1-2 (Required occurrence basis).**
A conforming assertion or description about a Work individual designates one world-side occurrence admitted under `U.Work` and makes each actual performer `U.System`, the exact obtaining `U.RoleAssignment` under which that system performed, any explicit F.6 `performedUnderAssignment(W, RA)` attribution, actual `enactsMethod -> U.Method`, temporal extent, and `executedWithin -> U.System` recoverable. It also makes every actually obtaining direct work-to-referent relation, direct subject relation or A.6.1 binding, and performed resource-use fact used by the receiving claim recoverable; it does not invent any of them when absent. Cite `methodDescriptionRef -> U.MethodDescription` only when the receiving claim depends on that exact description edition. The episteme designates these independently obtaining objects and relations; it does not turn them into occurrence fields or make the assignment act.
**CC-A15.1-3 (Time window).**
A conforming assertion or description about one Work occurrence designates a world-side individual with a closed temporal extent `[t_start, t_end]`, or an explicitly open end while the occurrence is in flight. The episteme states or designates that extent and, where relevant, location or asset; neither an interval field nor the presence of the record creates the occurrence.

**CC-A15.1-4 (Interpretation and policy basis).**
A load-bearing work claim names direct occurrence facts first. It cites `workContinuityPolicyRef`, its effective `U.ReferenceScheme`, and applicable scope or qualification window only when a named identity, episode, retry, resumption, or aggregation use must resolve an ambiguous segmentation. Any exact method-description edition, aggregation-policy episteme, selected model-use structure, acceptance criterion, evaluation work, result episteme, and evidence use remains a neighboring claim rather than a work-identity field.

If two local senses must be related, F.9 receives the exact sense endpoints and the claimed direction and loss. A different reference scheme, role assignment, description edition, or model-use structure alone does not establish a Bridge.
**CC-A15.1-4b (No mandatory state-plane or delta).**
A Work claim needs no `StatePlaneRef`, pre-state, post-state, or delta merely to establish occurrence identity. When actual change is current, A.3.4 identifies the transformation and its state or boundary facts; a separate work-to-change claim connects it to Work.
**CC-A15.1-5 (RoleAssignment interval coverage).**
Every `U.RoleAssignment` cited by an obtaining F.6 `performedUnderAssignment(W, RA)` attribution has as its holder the exact admitted `U.System` stated to perform the work and covers the work interval or exact performed part attributed to that system. If the holder differs or the assignment does not cover the extent, keep the Work occurrence, performer claim, and assignment claim separate: repair or reject the attribution, or establish a retroactive assignment only under the exact A.2.1 rule that admits it.

**CC-A15.1-6 (Actual participant and operation binding).**
Every actual parameter, participant, premise, constituent, operation argument, or operation result used by the work is established through an obtaining direct subject relation or exact A.6.1 application binding. A MethodDescription declaration, default, A.15.3 planned filling, gate selection, compatible ValueKind, or stored token establishes no actual binding.
**CC-A15.1-7 (Capability check).**
Any capability threshold relied on for a Work occurrence is recovered under A.2.2 or the exact direct capability-fit or evaluation owner. A `U.Method` or `U.MethodDescription` may cite or describe that threshold but does not create the capability fact. Check the threshold against each admitted performer system named through the holder of its covering assignment for the performed-work interval or declared checkpoints; state a violation through its separately governed evaluation-result episteme or direct characteristic/evaluation relation, never as an intrinsic work outcome.

**CC-A15.1-8 (Acceptance criteria).**
An acceptance claim names the exact criterion or comparator specification, its edition, applicable scope and window, the evaluation or acceptance work that applied it, and the direct result relation. Success class, quality measurement, comparison result, and acceptance verdict remain distinct; no verdict is an intrinsic field of the Work occurrence or a condition of `U.Work` membership.
**CC-A15.1-9 (Resource honesty).**
Performed resource-use facts (energy, materials, machine-time, money, tool wear) are attributed through exact obtaining relations to particular Work individuals admitted under `U.Work`, not to `U.Method`, `U.MethodDescription`, `U.Role`, or `U.Capability`. Estimates belong in method descriptions or plans. Any aggregate ledger, unit conversion, allocation, or overlap and deduplication result belongs to `B.1.6` and cites the contributing Work occurrences and resource-use facts.

**CC-A15.1-10 (Mereology declared).**
When exact work-part relations obtain among Work individuals, declare each relation: temporal-part, episode-part, operational-part, or another relation with its own predicate. Ambiguous mixtures lower aggregation and identity claims. A `TemporalPartOf_work` claim names parent work identity plus interval or aspect; an `EpisodeOf_work` claim names the parent, candidate boundary events, and named use, adding `workContinuityPolicyRef` only when those facts leave the grouping ambiguous for that use; an `OperationalPartOf_work` claim names the occurrence-side part and any recovered method factor separately. Concurrency adds a separate interval `overlaps` fact and, when current, a separately governed coordination claim; it is not a fourth work-part relation.

**CC-A15.1-11 (Temporal coverage selection).**
For a temporal roll-up, `B.1.4` names the exact Work refs, aggregation concern, time window, coverage and non-overlap conditions, and policy selecting union, convex hull, or another admitted result. A.15.1 supplies the occurrence intervals but does not own the aggregate.

**CC-A15.1-12 (Resource aggregation).**
For a resource roll-up, `B.1.6` names the exact Work refs, typed resource basis, units, evidence, delimitation and time window, overlap or deduplication policy, ledger, and aggregation rule. A.15.1 supplies performed resource-use facts but does not own the aggregate ledger.

**CC-A15.1-13 (Identity and retries).**
A distinct actual work-entry after an established completion or termination identifies a later Work occurrence; a proper work part and its parent and independently grounded concurrent performances are also distinct individuals. Add `retryOf`, `resumptionOf`, or `EpisodeOf_work` only when its own predicate holds. An interruption, performer or assignment replacement, method or mode switch, retune, rework, affected-referent change, or binding change is stated as direct history and neither splits nor preserves the parent by itself. Cite `workContinuityPolicyRef` only when a named use needs a branch criterion for that ambiguity. A changed MethodDescription or policy edition alone revises at most the dependent description or segmentation judgment.
**CC-A15.1-14 (Concurrency and ordering).**
Overlaps and precedences among work occurrences use interval relations (`overlaps`, `precedes`, `contains`, or `within`). Implicit "step order" claims are not admitted as performed-work evidence.

**CC-A15.1-15 (Cross-locality evaluation).**
A work occurrence keeps one identity when several receiving uses evaluate it. Each use names its own effective reference scheme, claim scope, criterion, qualification window, evaluation work, and result episteme. Use F.9 only when an exact Bridge between local senses is actually needed; a shared work name or record carries no acceptance across uses.
**CC-A15.1-16 (Method-description changes do not decide Work identity).**
If a selected MethodDescription edition changes during the occurrence, state the description-selection or override claim separately. The edition change alone neither splits nor preserves Work. When an accompanying actual performer-system, covering-assignment, enacted-method, binding, affected-referent, mode, or extent change creates a boundary question for a named use, apply that use's exact continuity-policy criterion; a later policy edition revises the judgment, not the occurrence.
**CC-A15.1-17 (Distributed performers).**
If multiple admitted `U.System`s jointly perform the same top-level work occurrence, name every system, its exact obtaining covering `U.RoleAssignment`, and every explicit F.6 attribution; verify that each assignment's holder is that system and that its obtaining extent covers the attributed work. If the use instead needs a parent work with child occurrences, give every child its actual performer system, covering assignment, and work-part relation. A lead, accountability, or coordination claim remains separate and cannot substitute one designated assignment for the actual performer set.

**CC-A15.1-18 (Logs are evidence, not work by themselves).**
Logs and telemetry support a claim about work only through an exact evidence-use relation that identifies the Work occurrence, actual performer system and covering assignment, enacted method, temporal extent, and containing system, plus any method-description edition, work-to-referent relation, binding, resource-use fact, policy, or qualification value on which the receiving claim relies.

**CC-A15.1-19 (Affected referent and work scope).**
Each assertion or description about a Work occurrence designates the exact Work individual and states a direct work-to-referent relation only when the receiving use needs one. That relation must obtain independently; naming the referent in the episteme establishes neither actual change, production, delivery, acceptance, nor a universal `affected` relation. When the receiving use needs no such relation, omit it without lowering the Work occurrence.
**CC-A15.1-20 (Actual change stays neighboring).**
When the receiving claim needs actual change, identify an exact `U.Transformation` under A.3.4 and the exact work-to-change facts. Work can occur without a current transformation claim, and a no-op, evaluation, inspection, communication, or record-handling occurrence is not forced into a delta schema.
**CC-A15.1-21 (Record handling remains Work without automatic transformation).**
Copying, formatting, evaluating, or publishing records can be performed by Work individuals admitted under `U.Work` when the actual performer system, covering assignment, actual enacted method, extent, and containing system are grounded. State an affected referent, binding, or resource-use fact only through its independently obtaining relation when the receiving claim uses it. Identify any actual record or dataset transformation separately under A.3.4; a label, output record, or post-state picture does not establish it.
**CC-A15.1-22 (Executed-within declaration).**
Each Work occurrence stands in one exact `executedWithin -> U.System` relation, which an assertion or description about the occurrence may state. When the accountable system is a subsystem in ordinary speech, name the system and its exact part relation to the larger holon. When that system differs from the affected referent, keep both identities and any current direct work-to-subject or work-to-change relation explicit.

**CC-A15.1-23 (No transformation composition from Work mereology).**
Exact Work parts support only their declared work-part facts and provide inputs to separately recovered `B.1.4` or `B.1.6` aggregation claims. They establish neither component transformations, transformation parthood, a composite transformation, nor a parent effect. Recover each actual transformation independently and return the exact missing-governor blocker when a current claim requires unavailable transformation composition.
**CC-A15.1-24 (No new claims on publication views).**
MVPK views about Work project the declared assertion or description of the Work occurrence; they do not add properties or claims. Numeric or comparable content names unit, scale, reference-plane, and `EditionId` pins; work-publication views do not use "signature" for these publication pins.

**CC-A15.1-25 (No Gamma leakage).**
Publication views cite exact `B.1.4` temporal-aggregation or `B.1.6` work-resource-aggregation results and policies when showing aggregates. They do not encode aggregation semantics in prose or imply defaults. Optional Gamma notation lives with its recovered Part B aggregation claim; the view carries only pinned references needed by the publication use.

**CC-A15.1-26 (No input-output re-listing).**
Publication views do not restate method-description input and output lists; they publish presence pins and source references only under the publication-use pattern governing that view.

**CC-A15.1-27 (Comparator ordering and return sets).**
Across-occurrence comparison presented on a publication view about Work uses a declared `ComparatorSet` (map-then-compare), returns sets when order is partial, and lowers hidden scalarization or ordinal-mean claims.

**CC-A15.1-28 (Comparator and transport pins).**
Numeric or comparable acceptance or KPI claims on a publication view about Work pin `ComparatorSet.edition`, comparator-spec edition, and, where conversions occur, `TransportRegistry.edition` with the selected transport policy ids. Bridge ids carry cross-context or cross-plane reuse; penalties affect the reliability relation only.

**CC-A15.1-29 (Telemetry-reference pins, when applicable).**
If a work occurrence feeds G.11 or QD and OEE portfolios, the evidence relation cites the telemetry, archive, and policy references declared by the governing comparison, archive, evidence, or refresh pattern. Illumination remains report-only telemetry unless a governing comparison, archive, or selection pattern promotes that use.

**CC-A15.1-30 (Part naming parsimony).**
Do not create a durable named work part for every interval, telemetry segment, pause, event-log row, engine stroke label, detector component, or encountered wording. Name a work part only when downstream use needs its own resources, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return use. Otherwise lower to a temporal relation, evidence slice, telemetry segment, method-description constituent, missing-source-relation note, or another direct neighboring object.

**CC-A15.1-31 (Method and work granularity are coupled but not isomorphic).**
A work part may enact a recovered submethod, but the correspondence is not automatic. A temporal work part usually enacts the same whole method during a slice. An episode records continuity under one method or mode and may span several operational parts, repeat the same method fragment, or be split by evidence policy without changing method identity. An operational work part corresponds to a method factor only when that factor is recovered as `U.Method` under `A.3.1` and `B.1.5`; otherwise govern the material as a work part, method-description node, evidence segment, mechanism material, or system-component behavior under the direct pattern.

