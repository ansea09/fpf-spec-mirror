---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__001_intro.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:intro — Intro"
line_start: 24621
line_end: 24658
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

## A.15.1 - U.Work

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.Work` when the current claim concerns one performed Work individual: a world-side dated occurrence performed by one or more admitted `U.System`s. Each performer acts under a covering system-role assignment, and F.6 states which assignment covers that Work. The assignment identifies its holder but does not act. A short account need name the assignment only when a later claim uses its identity. The occurrence has a time span, enacts a Method, and occurs within a containing System. State a binding, resource-use fact, or Work-to-referent relation only when it obtains and the receiving use needs it; an assertion, description, log, or record about the occurrence is a separate `U.Episteme`. When the reader asks what the Work returned, changed, produced, transferred, or caused someone to accept, use the concrete three-question route in §4.6 instead of adding an output or outcome field to Work.

**Use this when.** Use this pattern when a plan, method description, schedule, log, telemetry stream, dashboard, approval-looking cue, publication face, result statement, or evidence-provenance relation is being treated as if it were performed work. `U.Work` is the admitted kind; one Work individual is the world-side occurrence. A separate assertion or description episteme may designate that occurrence and its obtaining relations, while surrounding records may constrain, evidence, schedule, publish, or judge it; none becomes the occurrence by being published.

**First useful object.** One independently identified world-side dated Work occurrence admitted under `U.Work`. Establish its actual performer Systems, enacted Method, temporal extent, and containing System. For each performer, use F.6 to establish the covering assignment and the Work-attribution relation; keep the assignment's exact species and any additional participants recoverable there. A short assertion or description need expose an assignment identifier only when its claim uses that identity. Add a direct Work-to-referent relation, binding, or resource-use relation only when it obtains and the receiving claim uses it. If the next sentence reports a result, change, production, delivery, or judgment, use the matching §4.6 row; do not make it a Work field.

**First-use checks.**
1. Name the candidate occurrence and the work-facing claim that depends on it.
2. Recover every admitted `U.System` that actually performed the occurrence, then use F.6 to check the covering assignment under which each System performed that Work. Recover the enacted `U.Method`, temporal extent, and containing `U.System`. A short practitioner result may omit an assignment identifier when no receiving claim uses it. If responsibility is claimed, state its direct domain predicate separately or return the exact missing governor. Add only concrete bindings, performed resource-use facts, and direct Work-to-referent relations that actually obtain and matter to the receiving use. Route any claimed result, change, production, delivery, evidence use, or judgment through the one matching §4.6 row.
3. Decide whether the encountered record, trace, item, or display designates a Work individual admitted under `U.Work`, only a plan (`A.15.2`), only a method (`A.3.1`), only a method description (`A.3.2`), only evidence for work (`A.10`), only a publication-use relation (`E.17`), only a declarative representation (`C.2.P.DR` or the direct representation pattern), or an `A.15.4` appearance-based reliance repair case.
4. For composite, repeated, interrupted, or overlapping occurrences, declare each work-part relation and the naming threshold. Before using totals, recover the exact `B.1.4` temporal aggregation or `B.1.6` work-resource aggregation and its policy. Do not name a work part when a temporal relation, evidence slice, telemetry segment, or missing-source-relation note is the actual object needed.
5. If the required occurrence references cannot be recovered, lower the claim to a missing-source-relation note, work-evidence note, plan note, publication-use note, declarative-representation note, or `A.15.4` repair request; do not backdate work.

**Ordinary use.** For a simple occurrence, one readable assertion naming the actual performer System, enacted Method, temporal extent, and containing System is enough when no later claim needs the assignment identity. F.6 must still establish the assignment under which that System performed the Work; expose its identifier only when the receiving claim needs it. Add a binding, used resource, or Work-to-referent fact only when the assertion relies on that obtaining relation.

**Work-versus-transformation probe.** Use the coarsest branch that the current facts support.

- **Change without Work:** `LunarTideRise-2026-07-27` may be identified under A.3.4 as a Transformation of the exact water body over the stated interval. Without an independently admitted performer `U.System`, an enacted `U.Method`, temporal and containing-System relations, and F.6 attribution through a covering occurrence of an exact directly declared `U.SystemRoleAssignment` species, it is not a Work occurrence. A causal explanation of the tide supplies none of those agency facts.
- **Self-directed Work:** in the rehabilitation case, the current model admits `MotorControlRightArmSystem-7 : U.System` and `Person-7 : U.System`; A.14 `ComponentOf(MotorControlRightArmSystem-7, Person-7)` and `ComponentOf(LeftArm-7, Person-7)` obtain, so the mover and the affected limb are distinct parts of one person. `MotorControlRightArmSystem-7` performs `LeftArmStretchWork-7` from `2026-07-27T07:30:00+03:00` to `2026-07-27T07:35:00+03:00` under `SelfCarePerformerAssignment-7`; F.6 `performedUnderAssignment` obtains, the Work enacts `AssistedLeftArmStretchMethod-E1`, and `executedWithin -> Person-7` obtains. Clinic relation specification `ClinicRehabRelations@Clinic-E1` declares `RehabWorkStretchesLimb@Clinic-E1(work, limb, interval)`, and the case facts make it obtain for that Work, `LeftArm-7`, and the five-minute interval. Separately, A.6.1 application `AssistedStretchApplication-7` binds its declared `AffectedLimbArgument` to `LeftArm-7`. The first fact relates the Work to the limb; the second fills an operation argument. Neither is a primitive self-relation, and this case-specific decomposition is not a required anatomy for every self-directed action.

These branches test admitted facts, not human resemblance. A non-human or molecular-scale system can perform Work when its own system admission, covering assignment, enacted method, extent, containing system, and attribution obtain; unfamiliar agency is not a reason to reject it.

**Reliance-bearing use.** Add only the exact neighboring claims on which cost, quality, audit, evidence, conformance, gate, release, measurement, model use, or aggregation currently depends; do not turn them into fields of the work occurrence.

**Stop condition.** Stop once the occurrence is either recoverable as one Work individual admitted under `U.Work` at the needed granularity or lowered to a neighboring relation that no longer claims performed work.

**What goes wrong if missed.** Teams count plans, method descriptions, approval-looking cues, dashboards, telemetry, or evidence records as if work already happened, then attach cost, responsibility, quality, or result claims to the wrong EntityOfConcern.

**What this buys.** One dated occurrence identity whose actual performer systems, covering assignments, enacted method, temporal extent, and containing system remain inspectable, together with any actually obtaining work-to-referent, binding, and resource-use relations used by the claim. A practitioner can then report a result or consequence through the concrete §4.6 branch without turning it into Work identity.

**Not this pattern when.** Not this pattern when the current claim is only a method (`A.3.1`), only a method description (`A.3.2`), only a plan or schedule (`A.15.2`), only declaration-local `SlotFillingsPlanItem` content inside an A.15.3-governed WorkPlan, only work-entry readiness or full-kit preparation before work entry (`A.15.5`), only a visible cue that needs `A.15.4` appearance-based reliance repair before reliance, only evidence or assurance (`A.10` or `B.3`), only publication-use behavior (`E.17`), or only a declarative representation overread as a work-control or method claim (`C.2.P.DR` or the direct representation pattern).

