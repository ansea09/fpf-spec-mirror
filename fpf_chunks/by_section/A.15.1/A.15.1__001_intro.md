---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__001_intro.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:intro — Intro"
line_start: 24180
line_end: 24210
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

## A.15.1 - U.Work

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.Work` as the admitted kind when the current claim concerns one performed Work individual: a world-side dated occurrence performed by one or more admitted holder `U.System`s under exact obtaining `U.RoleAssignment`s. The systems perform the work; the assignments are the separately obtaining role-holding relations under which the attribution is valid. The occurrence has an actual temporal extent, enacts an exact method, and is executed within an exact containing system. State a binding, resource-use fact, or direct work-to-referent relation only when it actually obtains and the receiving use needs it; an assertion, description, log, or record about the occurrence is a separate `U.Episteme` and does not store fields in the occurrence. When the reader asks what the work returned, changed, produced, transferred, or caused someone to accept, use the concrete three-question route in §4.6 instead of adding an output or outcome field to Work.

**Use this when.** Use this pattern when a plan, method description, schedule, log, telemetry stream, dashboard, approval-looking cue, publication face, result statement, or evidence-provenance relation is being treated as if it were performed work. `U.Work` is the admitted kind; one Work individual is the world-side occurrence. A separate assertion or description episteme may designate that occurrence and its obtaining relations, while surrounding records may constrain, evidence, schedule, publish, or judge it; none becomes the occurrence by being published.

**First useful object.** One independently identified world-side dated Work occurrence admitted under `U.Work`. When the receiving use needs an assertion or description, keep that object as a separate `U.Episteme`: let it designate the occurrence and state the admitted holder `U.System` that actually performed it, the exact obtaining `U.RoleAssignment` under which that system performed it, and, when explicit attribution identity is consumed, the F.6 attribution relation linking the Work occurrence to that assignment. State actual `enactsMethod -> U.Method`, temporal extent, and `executedWithin -> U.System`. Add a direct work-to-referent relation, binding, or resource-use relation only when it actually obtains and the receiving claim uses it. If the next sentence reports a result, change, production, delivery, or judgment, select its exact object and owner from §4.6; do not make it a Work field.

**First-use checks.**
1. Name the candidate occurrence and the work-facing claim that depends on it.
2. Recover every admitted `U.System` that actually performed the occurrence and the exact obtaining `U.RoleAssignment` under which each system performed it; then recover the enacted `U.Method`, temporal extent, and accountable or containing `U.System`. Add only the concrete bindings, performed resource-use facts, and direct work-to-referent relations that actually obtain and matter to the receiving use. Route any claimed result, change, production, delivery, evidence use, or judgment through the one matching §4.6 row.
3. Decide whether the encountered record, trace, item, or display designates a Work individual admitted under `U.Work`, only a plan (`A.15.2`), only a method (`A.3.1`), only a method description (`A.3.2`), only evidence for work (`A.10`), only a publication-use relation (`E.17`), only a declarative representation (`C.2.P.DR` or the direct representation pattern), or an `A.15.4` appearance-based reliance repair case.
4. For composite, repeated, interrupted, or overlapping occurrences, declare each work-part relation and the naming threshold. Before using totals, recover the exact `B.1.4` temporal aggregation or `B.1.6` work-resource aggregation and its policy. Do not name a work part when a temporal relation, evidence slice, telemetry segment, or missing-source-relation note is the actual object needed.
5. If the required occurrence references cannot be recovered, lower the claim to a missing-source-relation note, work-evidence note, plan note, publication-use note, declarative-representation note, or `A.15.4` repair request; do not backdate work.

**Ordinary use.** For a simple occurrence, one readable assertion naming the actual performer system, the covering assignment under which it performed, enacted method, temporal extent, and containing system is enough. Add a binding, used resource, or work-to-referent fact only when the assertion relies on that obtaining relation.

**Reliance-bearing use.** Add only the exact neighboring claims on which cost, quality, audit, evidence, conformance, gate, release, measurement, model use, or aggregation currently depends; do not turn them into fields of the work occurrence.

**Stop condition.** Stop once the occurrence is either recoverable as one Work individual admitted under `U.Work` at the needed granularity or lowered to a neighboring relation that no longer claims performed work.

**What goes wrong if missed.** Teams count plans, method descriptions, approval-looking cues, dashboards, telemetry, or evidence records as if work already happened, then attach cost, responsibility, quality, or result claims to the wrong EntityOfConcern.

**What this buys.** One dated occurrence identity whose actual performer systems, covering assignments, enacted method, temporal extent, and containing system remain inspectable, together with any actually obtaining work-to-referent, binding, and resource-use relations used by the claim. A practitioner can then report a result or consequence through the concrete §4.6 branch without turning it into Work identity.

**Not this pattern when.** Not this pattern when the current claim is only a method (`A.3.1`), only a method description (`A.3.2`), only a plan or schedule (`A.15.2`), only declaration-local `SlotFillingsPlanItem` content inside an A.15.3-governed WorkPlan, only work-entry readiness or full-kit preparation before work entry (`A.15.5`), only a visible cue that needs `A.15.4` appearance-based reliance repair before reliance, only evidence or assurance (`A.10` or `B.3`), only publication-use behavior (`E.17`), or only a declarative representation overread as a work-control or method claim (`C.2.P.DR` or the direct representation pattern).

