---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:11"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__013_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:11 — Common Anti-Patterns and How to Avoid Them"
line_start: 24628
line_end: 24642
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

### A.15.1:11 - Common Anti-Patterns and How to Avoid Them

* **"The log is the performed occurrence."** Dumping telemetry without occurrence references (actual performer system, covering assignment, enacted method, time window, and containing system, plus any method-description edition, work-to-referent relation, binding, resource-use fact, or evidence-use relation on which the claim relies) -> **Not Work**. Recover the Work occurrence and relate the log as evidence.
* **Record-handling-as-transformation.** ETL, copying, formatting, evaluation, or publication work is treated as proof that a record or dataset changed -> Keep the grounded Work occurrence, but assert actual change only after A.3.4 identifies the transformation and an exact work-to-change fact obtains.
* **Silent cross-locality acceptance.** "Ops accepted it, so audit accepts it." -> Name each receiving criterion, evaluation work, result episteme, and acceptance relation; add F.9 only when exact local senses must be bridged.
* **Description-change-as-occurrence-change.** A MethodDescription edition swap is treated as automatically splitting or preserving Work -> State the description-selection change separately. Only when an accompanying actual history change creates an identity question for a named use should its exact continuity-policy criterion be applied; the policy revises the judgment, not the occurrence.
* **Budget on the method.** Charging costs to Method or Role -> Attribute performed resource use only through exact relations involving Work individuals; keep estimates in method descriptions or plans.
* **Part ambiguity.** Mixing retries, episodes, and operational parts with no declared relation → Choose and declare the part relation.
* **Slice-as-episode.** A monitoring interval, telemetry window, crank-angle segment, or one-second reception trace is called an episode only because it has timestamps -> Use `TemporalPartOf_work`, an evidence relation, or a telemetry relation unless actual boundary events and the direct episode predicate establish an event-bounded fragment for a named use; add a continuity policy only if those facts leave its grouping ambiguous.
* **Episode-as-new-work by habit.** A pause, retune, or interruption is always recorded as either a new occurrence or the same one -> Preserve the boundary events first. Apply exact `workContinuityPolicyRef` only when a named use must decide the grouping; otherwise return unresolved segmentation rather than forcing either answer.
* **Method-factor-as-work-part by label.** A step, stroke, receiver component, graph node, or method-description section is treated as a work part or submethod by name -> Recover the current object: `U.Method` factor, `U.MethodDescription` constituent, `TemporalPartOf_work`, `OperationalPartOf_work`, evidence segment, mechanism material, system-component behavior, or missing-source-relation note.
* **Granularity inflation.** Every interval or trace row receives a durable work-part name -> Name the work part only when a current resource, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return use hangs on it.
* **Union-hull confusion.** Changing KPI coverage silently between reports -> recover the exact `B.1.4` temporal aggregation and cite its policy per KPI.
* **Double-count in overlaps.** Summing child and parent resource facts as one ledger -> recover the `B.1.6` aggregation claim and apply its exact overlap or deduplication policy.

