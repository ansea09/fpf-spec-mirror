---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:12"
section_title: "Existing work-log repair applications"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__014_existing-work-log-repair-applications.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:12 — Existing work-log repair applications"
line_start: 24468
line_end: 24479
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
  - "U.System"
  - "U.SystemRoleAssignment"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actual performer U.System"
  - "admitted U.Work kind"
  - "containing System"
  - "covering U.SystemRoleAssignment"
  - "enacted Method"
  - "optional direct bindings and resource use"
  - "performedUnderAssignment"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:12 - Existing work-log repair applications

1. **Recover occurrence assertions.** For existing logs, identify the independently grounded Work occurrence and recover each actual performer System, the covering assignment occurrence, and its F.6 attribution, together with at least one obtaining `enactsMethod` relation, the extent, and at least one obtaining locally declared containing-system relation. Add optional `methodDescriptionRef` and only those independently obtaining work-to-referent, binding, and resource-use relations on which the receiving claim relies. Do not create Work by creating a record.
2. **Recover the work-judgment basis.** Name the direct occurrence facts first. Add exact `workContinuityPolicyRef`, effective reference scheme, scope, or qualification window only when the identity, episode, retry, resumption, or aggregation judgment has more than one defensible branch. Keep any selected MethodDescription episteme, aggregation policy, criterion, and evidence-use relation outside the Work.
3. **Record a continuity policy only for an actual ambiguity.** Cite exact `workContinuityPolicyRef` and its named use when an interruption, resumption, replacement, switch, or composite boundary could support more than one segmentation. If direct facts already close a simple uninterrupted case, omit the policy.
4. **Separate temporal aspect, temporal Work part, episode, and operational part.** Keep a bare interval or aspect with C.27.TA or its direct domain object. Use `TemporalPartOf_work` only between independently admitted Work individuals when the proper temporal-sub-occurrence predicate passes; use `EpisodeOf_work` only for an independently admitted event-bounded Work sub-occurrence; and use `OperationalPartOf_work` only for an independently admitted performed constituent of the whole. Recover any Method factor separately.
5. **Name only useful work parts.** If no named resource, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return claim depends on the candidate part, keep it as a relation, evidence slice, or telemetry slice.
6. **Use B.1.4 for temporal roll-up.** Cite the exact temporal aggregation and its union, hull, coverage, and non-overlap policy in the KPI rather than recreating it on Work.
7. **Use B.1.6 for resource roll-up.** Recover the typed resource ledger, evidence basis, allocation, and overlap or deduplication policy there; each contributing performed resource-use relation remains independently obtaining with an exact Work occurrence as a participant.
8. **Pull plans out.** Keep calendars and planned fillings in exact `U.WorkPlan` content; establish performed values only through direct relations in which the Work occurrence participates and through exact A.6.1 bindings.
9. **Bind actual values directly.** For an operation argument or result, name the identified A.6.1 application and its exact binding. For any other participant or parameter, name the declared subject predicate, participant order, and actual values; return the matching missing-governor result when that predicate is absent. Retain MethodDescription defaults and WorkPlan choices as non-actual neighbors.

