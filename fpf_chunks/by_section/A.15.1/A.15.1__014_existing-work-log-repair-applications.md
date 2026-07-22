---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:12"
section_title: "Existing work-log repair applications"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__014_existing-work-log-repair-applications.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:12 — Existing work-log repair applications"
line_start: 24673
line_end: 24684
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
  - "U.Work admitted kind"
  - "actual binding"
  - "affected referent"
  - "enactsMethod"
  - "episode"
  - "no automatic transformation"
  - "occurrence assertion and record separation"
  - "overlap"
  - "performed resource-use fact"
  - "performedBy"
  - "retry"
  - "work continuity"
  - "work part"
  - "world-side dated occurrence"
---

### A.15.1:12 - Existing work-log repair applications

1. **Recover occurrence assertions.** For existing logs, identify the independently grounded Work occurrence and write an assertion or description that cites its designator, actual `enactsMethod`, optional `methodDescriptionRef`, exact `performedBy`, extent, affected referent, bindings, containing system, and resource-use facts. Do not create Work by creating a record.
2. **Recover the work-judgment basis.** Name exact `workContinuityPolicyRef`, its effective reference scheme, and any current MethodDescription edition, scope, qualification window, aggregation policy, criterion, or evidence-use relation without making those epistemes part of the Work.
3. **Record the continuity policy.** Cite exact `workContinuityPolicyRef` and decide when an interruption stays within one occurrence, creates an episode, or forces a new occurrence.
4. **Separate slice, episode, and operational part.** Use interval/aspect for `TemporalPartOf_work`, event-bounded continuity for `EpisodeOf_work`, and recovered occurrence-side part plus any separately recovered method factor for `OperationalPartOf_work`.
5. **Name only useful work parts.** If no current resource, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return use hangs on the candidate part, keep it as a relation, evidence slice, or telemetry slice.
6. **Return temporal roll-up to B.1.4.** Cite the exact temporal aggregation and its union, hull, coverage, and non-overlap policy in the KPI rather than recreating it on Work.
7. **Return resource roll-up to B.1.6.** Recover the typed resource ledger, evidence basis, allocation, and overlap or deduplication policy there; each contributing performed resource-use relation remains independently obtaining with an exact Work occurrence as a participant.
8. **Pull plans out.** Keep calendars and planned fillings in exact `U.WorkPlan` content; establish performed values only through direct relations in which the Work occurrence participates and through exact A.6.1 bindings.
9. **Bind actual values directly.** Recover each participant or parameter through its obtaining subject relation or exact A.6.1 application binding; retain MethodDescription defaults and WorkPlan choices as non-actual neighbors.

