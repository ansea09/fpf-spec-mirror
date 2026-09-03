---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:8"
section_title: "Conformance Checklist (admission checks)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__010_conformance-checklist-admission-checks.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:8 — Conformance Checklist (admission checks)"
line_start: 25332
line_end: 25422
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
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
  - "E.10.ROLE"
  - "E.17"
  - "F.6"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.WorkPlan"
keywords:
  - "A.13-qualified actual performer U.System"
  - "F.6 only after admission for precise assignment-bound attribution"
  - "conditional agency profile"
  - "containing System"
  - "enacted Method"
  - "exact performance history"
  - "independent U.Work admission"
  - "optional direct bindings and resource use"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:8 - Conformance Checklist (admission checks)

**CC-A15.1-1 (Strict distinction).**
`U.Work` is the admitted kind for dated performed Work occurrences. Each Work individual is world-side; it is not a `U.Method` (reusable way), `U.MethodDescription` (description), local system-role kind, System-classification judgment, `U.SystemRoleAssignment` (assignment), `U.WorkPlan` (plan or schedule), or assertion, record, log, or publication about Work.

**CC-A15.1-2 (Required occurrence basis).**
A conforming world-side Work account starts with one exact dated candidate action and every actual performer `U.System` with its A.13 local kind and criterion, classification, obtaining assignment, scope, working situation, and window, plus evidence adequate for those core claims and any characteristic profile conditionally consumed by the receiving use. It establishes that the action actually followed at least one Method, has a temporal extent, and lies inside at least one locally declared Work-to-System boundary; on that independent basis A.15.1 admits the occurrence under `U.Work` and states its owned relations. F.6 is not an admission condition. When the receiving claim also needs precise assignment-bound performer attribution, apply F.6 afterward to the already admitted Work and the same obtaining A.13 assignment. The account also names every declared Work-to-referent, participation, or resource-use predicate used by the receiving claim, or returns the exact missing governor instead of inventing a relation.
**CC-A15.1-3 (Time window).**
A conforming assertion or description about one Work occurrence designates a world-side individual with a closed temporal extent `[t_start, t_end]`, or an explicitly open end while the occurrence is in flight. The episteme states or designates that extent and, where relevant, location or asset; neither an interval field nor the presence of the record creates the occurrence.

**CC-A15.1-4 (Interpretation and policy basis).**
A load-bearing work claim names direct occurrence facts first. It cites `workContinuityPolicyRef`, its effective `U.ReferenceScheme`, and applicable scope or qualification window only when a named identity, episode, retry, resumption, or aggregation use must resolve an ambiguous segmentation. Any selected method-description episteme, aggregation-policy episteme, selected model-use structure, acceptance criterion, evaluation work, result episteme, and evidence use remains a neighboring claim rather than a work-identity field.

If two local senses must be related, F.9 receives two exact `SchemeSenseCell` endpoints and one `BridgePredicateProfile`; a Bridge is positive only when that profile's predicate obtains. State the proposed comparison, substitution, translation, or publication separately in a C.2.1 bounded-use claim, with its action, direction, correspondence rule, and tolerated loss. State reliance through the applicable A.10 evidence-use relation or B.3 assurance result. A different reference scheme, system-role assignment, selected description episteme, or model-use structure alone establishes none of these facts.
**CC-A15.1-4b (No mandatory state-plane or delta).**
A Work claim needs no `StatePlaneRef`, pre-state, post-state, or delta merely to establish occurrence identity. If the receiving claim says that a referent changed, A.3.4 identifies the transformation and its state or boundary facts. Connect it to Work only through a declared domain predicate with exact W and T participants, or one C.2.1 local compound claim under A.6.RCD disposition 2 with a recoverable constructor, governed base predicates, actual participants, and case facts; otherwise return `missing-governor[work-to-change]`.
**CC-A15.1-5 (SystemRoleAssignment interval coverage).**
Every obtaining F.6 `performedUnderAssignment(W, RA)` attribution cites two assignment identities already recovered through A.2.1 and the performer’s A.13 core: the exact directly declared species and the same obtaining occurrence `RA` of that species. The species supplies the signature, participant meanings, predicate, and applicability. The occurrence supplies the actual participant values, including the holder System, and has an extent covering the Work or exact performed part. The holder equals the exact admitted `U.System` already recovered as actual performer through A.13. If holder equality or coverage fails, keep the Work occurrence, performer claim, assignment occurrence, and attribution separate; repair or reject only the attribution, or establish a retroactive occurrence only under A.2.1's exact rule for its directly declared species. F.6 discovers neither identity nor performer.

**CC-A15.1-6 (Actual participant and operation binding).**
For an operation argument or result, name one identified A.6.1 application and its exact declaration-local binding. For any other actual parameter, participant, premise, constituent, reference use, resource, or work-to-referent claim, name the declared subject predicate, participant order, and actual participant values. If the required route is absent, name the missing relation or binding in the `missing-governor` result and do not assert it. A MethodDescription declaration, default, A.15.3 planned filling, gate selection, compatible ValueKind, or stored token establishes no actual binding.
**CC-A15.1-7 (Capability check).**
Any capability threshold relied on for a Work occurrence is the declared bound in the selected method-side claim and is tested by a named A.2.2 capability-fit predicate against each performer system's capability instance for the work interval or declared checkpoints. Name that predicate, the capability instance, threshold, work need, and result. If the fit predicate is absent, return `missing-governor[capability-fit]` and assert neither fit nor failed fit. A `U.Method` or `U.MethodDescription` may cite or describe the threshold but creates neither capability nor fit. State a failed fit in its evaluation-result episteme or direct characteristic/evaluation relation, never as an intrinsic work outcome.

**CC-A15.1-8 (Acceptance criteria).**
An acceptance claim names the selected criterion episteme or comparator specification, its applicable scope and window, the evaluation or acceptance work that applied it, its returned value or result episteme, and the declared acceptance predicate with all actual participants. If the claim relies on historical continuity with an earlier criterion episteme, name the exact C.2.1 `EpistemeEditionRelation`; a version label alone is not enough. If no acceptance predicate governs the claim, return `missing-governor[acceptance]`. Success class, quality measurement, comparison result, and acceptance verdict remain distinct; no verdict is an intrinsic field of the Work occurrence or a condition of `U.Work` membership.
**CC-A15.1-9 (Resource honesty).**
Performed resource-use facts (energy, materials, machine-time, money, tool wear) are attributed through declared predicates that name the particular Work, resource, amount, unit, and extent participants, not to `U.Method`, `U.MethodDescription`, a system-role kind or assignment, or `U.Capability`. If no predicate governs the needed use, return `missing-governor[resource-use]`; estimates remain in Method descriptions or plans. Any aggregate ledger, unit conversion, allocation, or overlap and deduplication result belongs to `B.1.6` and cites the contributing Work occurrences and resource-use facts.

**CC-A15.1-10 (Mereology declared).**
When exact work-part relations obtain among Work individuals, declare each relation: temporal-part, episode-part, operational-part, or another relation with its own predicate. Ambiguous mixtures lower aggregation and identity claims. Each A.15.1 work-part relation uses two independently admitted Work participants and the predicate and identity rule in §4.1a. A bare interval stays with C.27.TA or its direct domain object. Concurrency adds a separately declared temporal-overlap claim through C.27.TA. If the reader also claims coordination, name its declared predicate and actual participants; overlap alone does not establish it.

**CC-A15.1-11 (Temporal coverage selection).**
For a temporal roll-up, `B.1.4` names the exact Work refs, aggregation concern, time window, coverage and non-overlap conditions, and policy selecting union, convex hull, or another admitted result. A.15.1 supplies the occurrence intervals but does not own the aggregate.

**CC-A15.1-12 (Resource aggregation).**
For a resource roll-up, `B.1.6` names the exact Work refs, typed resource basis, units, evidence, delimitation and time window, overlap or deduplication policy, ledger, and aggregation rule. A.15.1 supplies performed resource-use facts but does not own the aggregate ledger.

**CC-A15.1-13 (Identity and retries).**
A distinct actual work-entry after an established completion or termination identifies a later Work occurrence; a proper work part and its parent and independently grounded concurrent performances are also distinct individuals. Add an `EpisodeOf_work` relation only when its §4.1a predicate holds. Add a retry or resumption relation only under an exact locally declared species whose participant meanings, predicate, identity, cardinality, and applicability pass §4.1a; bare `retryOf` and `resumptionOf` are route cues only. An interruption, performer or assignment replacement, method or mode switch, retune, rework, affected-referent change, or binding change is stated as direct history and neither splits nor preserves the parent by itself. Cite `workContinuityPolicyRef` only when a named use needs a branch criterion for that ambiguity. A changed MethodDescription or another policy episteme alone revises at most the dependent description or segmentation judgment. Call the policy an edition only when an exact C.2.1 `EpistemeEditionRelation` obtains; a non-continuing replacement can support a different judgment without rewriting the occurrence.
**CC-A15.1-14 (Concurrency and ordering).**
Overlaps and precedences among Work occurrences use C.27.TA with an exact temporal bearer, reference, intervals, and declared predicate. A list of familiar interval words supplies no relation declaration, and implicit "step order" is not performed-work evidence.

**CC-A15.1-15 (Cross-locality evaluation).**
A work occurrence keeps one identity when several receiving uses evaluate it. Each use names its own effective reference scheme, claim scope, criterion, qualification window, evaluation work, and result episteme. When two local senses must be related, test the exact F.9 Bridge, then state the proposed comparison or substitution, direction, rule, and tolerated loss in a separate bounded-use claim and check reliance under A.10 or B.3. A shared work name, record, or Bridge carries no acceptance across uses.
**CC-A15.1-16 (Method-description changes do not decide Work identity).**
If the selected MethodDescription episteme changes during the occurrence, state the description-selection or override claim separately. That selection change alone neither splits nor preserves Work. When an accompanying actual performer-system, covering-assignment, enacted-method, binding, affected-referent, mode, or extent change creates a boundary question for a named use, apply that use's exact continuity-policy criterion. A later or competing policy episteme may support another judgment; it is a later edition only when its exact C.2.1 `EpistemeEditionRelation` to the earlier policy obtains. Otherwise it is a non-continuing replacement. Neither changes the occurrence.
**CC-A15.1-17 (Distributed performers).**
If multiple admitted `U.System`s jointly perform the same top-level Work occurrence, name every actual performer and recover its A.13 basis before A.15.1 admission. If precise assignment-bound attribution is current, use F.6 after admission to check the exact assignment for each System. If the use instead needs a parent Work with child occurrences, admit every child independently from its own performer basis, history, Method, extent, and containment, then add any needed F.6 attribution and Work-part relation. A lead, responsibility, or coordination claim remains separate and cannot substitute for the actual performer set.

**CC-A15.1-18 (Logs are evidence, not work by themselves).**
Logs and telemetry support a claim about Work only through an exact evidence-use relation that identifies the candidate action, every actual performer System with its A.13 basis, at least one Method actually followed, temporal extent, and at least one obtaining local Work-to-System containment relation. Those facts may support A.15.1 admission but the log creates none of them. When a precise assignment-bound attribution is also current, support its separate F.6 assertion without making the log or evidence constitute the relation.

**CC-A15.1-19 (Affected referent and work scope).**
Each assertion or description about a Work occurrence designates the exact Work individual and states a direct work-to-referent relation only when the receiving use needs one. That relation must obtain independently; naming the referent in the episteme establishes neither actual change, production, delivery, acceptance, nor a universal `affected` relation. When the receiving use needs no such relation, omit it without lowering the Work occurrence.
**CC-A15.1-20 (Actual change stays neighboring).**
When the receiving claim needs actual change, identify an exact `U.Transformation` under A.3.4. Connect it to Work only through a declared domain predicate with exact W and T participants, or one C.2.1 local compound claim under A.6.RCD disposition 2 with a recoverable constructor, defined base predicates, actual participants, and case facts; otherwise retain both objects and return `missing-governor[work-to-change]`. Work can occur without a current transformation claim, and a no-op, evaluation, inspection, communication, or record-handling occurrence is not forced into a delta schema. The inverse also holds: a transformation becomes Work only when every actual performer System has an A.13 basis and the exact performance history, enacted Method, temporal extent, and at least one obtaining local containing-system relation independently ground A.15.1 admission. Any precise assignment-bound attribution is then checked separately through F.6. Apply the paired first-use probe to natural change and self-directed action; do not invent an assignment for a causal participant, reject a non-human performer by resemblance, or collapse internal performer and affected positions into a primitive self-relation.
**CC-A15.1-21 (Record handling remains Work without automatic transformation).**
Copying, formatting, evaluating, or publishing records can be admitted as `U.Work` when every actual performer System has an A.13 basis and the exact action history, at least one obtaining `enactsMethod` relation, extent, and at least one obtaining local containing-system relation are grounded. A precise assignment-bound attribution is a separate later F.6 result. State an affected referent, binding, or resource-use fact only through its independently obtaining relation when the receiving claim uses it. Identify any actual record or dataset transformation separately under A.3.4; a label, output record, or post-state picture does not establish it.
**CC-A15.1-22 (Containing-System relation declared).**
Each Work occurrence has at least one obtaining locally declared Work-to-System relation whose predicate names the exact system delimitation and qualification window that contain the complete occurrence. Name several when distinct valid boundaries matter; none is inferred from a System part relation, accountability, colocation, or a diagram. Keep every containing System distinct from the affected referent. If the receiving claim relates Work to that referent or to a Transformation, name the separate declared predicate, actual participants, and obtaining facts; containment and shared timing establish neither. Bare `executedWithin` is a historical route cue, not a current positive relation.

**CC-A15.1-23 (No transformation composition from Work mereology).**
Exact Work parts support only their declared work-part facts and provide inputs to separately recovered `B.1.4` or `B.1.6` aggregation claims. They establish neither component transformations, transformation parthood, a composite transformation, nor a parent effect. Recover each actual transformation independently; when a production or effect claim needs unavailable transformation composition, return `missing-governor[transformation-composition]`.
**CC-A15.1-24 (No new claims on publication views).**
MVPK views about Work project the declared assertion or description of the Work occurrence; they do not add properties or claims. Numeric or comparable content names unit, scale, reference-plane, and `EditionId` pins; work-publication views do not use "signature" for these publication pins.

**CC-A15.1-25 (No Gamma leakage).**
Publication views cite exact `B.1.4` temporal-aggregation or `B.1.6` work-resource-aggregation results and policies when showing aggregates. They do not encode aggregation semantics in prose or imply defaults. Optional Gamma notation lives with its recovered Part B aggregation claim; the view carries only pinned references needed by the publication use.

**CC-A15.1-26 (No input-output re-listing).**
Publication views do not restate method-description input and output lists; they publish presence pins and source references only under the publication-use pattern governing that view.

**CC-A15.1-27 (Comparator ordering and return sets).**
Across-occurrence comparison presented on a publication view about Work uses a declared `ComparatorSet` (map-then-compare), returns sets when order is partial, and lowers hidden scalarization or ordinal-mean claims.

**CC-A15.1-28 (Comparator and transport pins).**
Numeric or comparable acceptance or KPI claims on a publication view about Work pin `ComparatorSet.edition`, comparator-spec edition, and, where conversions occur, `TransportRegistry.edition` with the selected transport policy ids. When two local senses must be related, cite the exact obtaining F.9 Bridge only as the correspondence premise, state the proposed bounded reuse in a separate C.2.1 claim, and check reliance under A.10 or B.3. A selected reference-plane change remains with CHR and its direct relation; the Bridge transfers neither reuse nor a plane value. Penalties affect the reliability relation only.

**CC-A15.1-29 (Telemetry-reference pins, when applicable).**
If a work occurrence feeds G.11 or QD and OEE portfolios, the evidence relation cites the telemetry, archive, and policy references declared by the governing comparison, archive, evidence, or refresh pattern. Illumination remains report-only telemetry unless a governing comparison, archive, or selection pattern promotes that use.

**CC-A15.1-30 (Part naming parsimony).**
Do not create a durable named work part for every interval, telemetry segment, pause, event-log row, engine stroke label, detector component, or encountered wording. Name a work part only when downstream use needs its own resources, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return use. Otherwise lower to a temporal relation, evidence slice, telemetry segment, method-description constituent, missing-source-relation note, or another direct neighboring object.

**CC-A15.1-31 (Method and work granularity are coupled but not isomorphic).**
A work part may enact a recovered submethod, but the correspondence is not automatic. A temporal work part usually enacts the same whole method during a slice. An episode records continuity under one method or mode and may span several operational parts, repeat the same method fragment, or be split by evidence policy without changing method identity. An operational work part corresponds to a method factor only when that factor is recovered as `U.Method` under `A.3.1` and `B.1.5`; otherwise keep it as the work part, method-description node, evidence segment, mechanism material, or system-component behavior actually identified.

**CC-A15.1-32 (Work rows do not create architecture).**
Before a timetable, workflow, or architecture row supports a Work whole, part, overlap, or order claim, every Work occurrence is independently admitted from each actual performer System's A.13 basis, grounded action history, enacted Method, actual interval, and required containing-System relation; every whole, part, and temporal relation is then established separately. Apply F.6 afterward only for a precise assignment-bound attribution. Similar labels, shared rows, or planned co-occurrence establish none of these facts.

