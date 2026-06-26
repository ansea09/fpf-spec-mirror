---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:8"
section_title: "Conformance Checklist (admission checks)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__010_conformance-checklist-admission-checks.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:8 — Conformance Checklist (admission checks)"
line_start: 21547
line_end: 21645
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
  - "B.3"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actuals"
  - "event"
  - "execution"
  - "log"
  - "occurrence"
  - "run"
---

### A.15.1:8 - Conformance Checklist (admission checks)

**CC-A15.1-1 (Strict distinction).**
`U.Work` is a dated run-time occurrence. It is not a `U.Method` (semantic way), not a `U.MethodDescription` (description), not a `U.Role` or `U.RoleAssignment` (assignment), and not a `U.WorkPlan` (plan or schedule).

**CC-A15.1-2 (Required links).**
A conforming `U.Work` claim names:
(a) `enactsMethod -> U.Method` (the method enacted),
(b) `methodDescriptionRef -> U.MethodDescription` when the source episteme or editioned method description is current,
(c) `performedBy -> U.RoleAssignment` (the assigned performer in context), and
(d) `executedWithin -> U.System`; if ordinary speech says subsystem, name the `U.System` in subsystem position plus the part relation to the larger holon under A.1, A.14, or B.1.2.

**CC-A15.1-3 (Time window).**
A conforming `U.Work` claim carries a closed interval `[t_start, t_end]`, or an explicitly marked open end for in-flight work, and, where relevant, location or asset.

**CC-A15.1-4 (Context reference and judgement).**
A `U.Work` claim is judged inside a declared `U.BoundedContext` (the judgement context).

- By default, the judgement context is the context of the referenced method-description source.
- If `performedBy` references a `U.RoleAssignment` in a different context, cross-context acceptance needs an explicit bridge relation or policy. Otherwise the work claim is not admitted in that context.

**CC-A15.1-4b (State-plane reference).**
The work claim names the `StatePlaneRef` used for its delta judgement.

**CC-A15.1-5 (RoleAssignment interval coverage).**
The `performedBy` `U.RoleAssignment` timespan covers the work interval. If it does not, lower the claim to a non-admitted role-assignment relation for that context or re-judge it in a context that admits retroactive assignments.

**CC-A15.1-6 (Parameter binding).**
Parameters declared by the `U.MethodDescription` have concrete values bound at work creation or start and recorded with the work occurrence. Defaults in the method description do not by themselves admit the performed-work claim.

**CC-A15.1-7 (Capability check).**
Capability thresholds stated by the `U.Method` or `U.MethodDescription` are checked against the holder in `performedBy` for the performed-work interval or declared checkpoints. Violations are recorded on the work outcome.

**CC-A15.1-8 (Acceptance criteria).**
Success and failure classes and quality grades are determined by the acceptance criteria declared or referenced by the `U.MethodDescription` or comparator specification in the judgement context. The verdict is recorded on the work occurrence.

**CC-A15.1-9 (Resource honesty).**
Performed consumptions and costs (energy, materials, machine-time, money, tool wear) are booked to `U.Work`, not to `U.Method`, `U.MethodDescription`, `U.Role`, or `U.Capability`. Estimates belong in method descriptions or plans; performed values belong in work occurrences.

**CC-A15.1-10 (Mereology declared).**
When a work occurrence has parts, the selected part relation is declared: temporal-part, episode-part, operational-part, or concurrent-part. Ambiguous mixtures lower aggregation and identity claims.

**CC-A15.1-11 (Temporal coverage selection).**
For a roll-up, the judgement context declares which temporal coverage operator applies: union for utilization or convex hull for lead time. Silent mixing lowers the KPI or comparison claim.

**CC-A15.1-12 (Resource aggregation).**
Aggregation of resource ledgers across work parts names an overlap policy, such as attributing shared machine-time to the parent only, before totals are used.

**CC-A15.1-13 (Identity and retries).**
A retry is a new `U.Work` occurrence linked via `retryOf`. Interruptions treated as the same run are represented as episodes (`resumptionOf`) under a context-declared episode policy.

**CC-A15.1-14 (Concurrency and ordering).**
Overlaps and precedences among work occurrences use interval relations (`overlaps`, `precedes`, `contains`, or `within`). Implicit "step order" claims are not admitted as performed-work evidence.

**CC-A15.1-15 (Cross-context evidence).**
If a work occurrence is accepted in multiple contexts, either re-judge it in each context or provide bridge relations that map acceptance criteria, units, and role-assignment relations. Name identity alone does not carry cross-context acceptance.

**CC-A15.1-16 (Method-description source changes during work).**
If the method-description version changes mid-run, split the work into episodes bound to respective method-description source editions, or record an explicit method-description override event in the judgement context. Silent substitution lowers the work claim.

**CC-A15.1-17 (Distributed performers).**
If multiple `U.RoleAssignment` values jointly perform the same top-level work occurrence, either designate a lead `U.RoleAssignment` with concurrent parts, or model the top-level occurrence as a parent work with child work occurrences per `U.RoleAssignment`.

**CC-A15.1-18 (Logs are evidence, not work by themselves).**
Logs and telemetry evidence a work occurrence only after they are bound to method-description source when current, performer, time window, affected referent, and judgement context.

**CC-A15.1-19 (Affected referent).**
Each `U.Work` claim names at least one affected referent, such as asset, product, batch, dataset, or document, through `affected -> {...}`.

**CC-A15.1-20 (State-change witness).**
Each `U.Work` claim carries either explicit pre-state and post-state references on the declared state-plane or a delta predicate evaluable on evidence. A no-op run is flagged as such.

**CC-A15.1-21 (Affected-referent declaration vs. record handling).**
A run whose only effect is copying or reformatting records qualifies as `U.Work` only when the judgement context declares those records to be the product referent, such as data-product manufacture.

**CC-A15.1-22 (Executed-within declaration).**
Each `U.Work` claim names `executedWithin -> U.System`; when the accountable system is a subsystem in ordinary speech, name the system and its part relation to the larger holon. When that system differs from the asset of change, keep `affected` explicit.

**CC-A15.1-23 (Compositionality of delta).**
For composite work, the parent effect is the declared composition of child effects under the same overlap policy as `Gamma_work`.

**CC-A15.1-24 (No new claims on publication views).**
MVPK views for `U.Work` project the declared work-occurrence claim; they do not add properties or claims. Numeric or comparable content names unit, scale, reference-plane, and `EditionId` pins; work-publication views do not use "signature" for these publication pins.

**CC-A15.1-25 (No Gamma leakage).**
Publication views reference Gamma operators and policies by id when showing aggregates. They do not encode aggregation semantics in prose or imply defaults. Gamma lives in Part B; views carry pinned references only.

**CC-A15.1-26 (No input-output re-listing).**
Publication views do not restate method-description input and output lists; they publish presence pins and source references only under the publication-use pattern governing that view.

**CC-A15.1-27 (Comparator ordering and return sets).**
Across-run comparison presented on a `U.Work` publication view uses a declared `ComparatorSet` (map-then-compare), returns sets when order is partial, and lowers hidden scalarization or ordinal-mean claims.

**CC-A15.1-28 (Comparator and transport pins).**
Numeric or comparable acceptance or KPI claims on a `U.Work` publication view pin `ComparatorSet.edition`, comparator-spec edition, and, where conversions occur, `TransportRegistry.edition` with the selected transport policy ids. Bridge ids carry cross-context or cross-plane reuse; penalties affect the reliability relation only.

**CC-A15.1-29 (Telemetry-reference pins, when applicable).**
If a work occurrence feeds G.11 or QD and OEE portfolios, the evidence relation cites the telemetry, archive, and policy references declared by the governing comparison, archive, evidence, or refresh pattern. Illumination remains report-only telemetry unless a governing comparison, archive, or selection pattern promotes that use.

