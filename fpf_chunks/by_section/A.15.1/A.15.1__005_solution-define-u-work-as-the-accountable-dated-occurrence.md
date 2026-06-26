---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:4"
section_title: "Solution — define U.Work as the accountable, dated occurrence"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__005_solution-define-u-work-as-the-accountable-dated-occurrence.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:4 — Solution — define U.Work as the accountable, dated occurrence"
line_start: 21386
line_end: 21441
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

### A.15.1:4 - Solution — define `U.Work` as the accountable, dated occurrence

#### A.15.1:4.1 - Definition

**`U.Work`** is a **4D occurrence holon**: a **dated run-time enactment** of a `U.Method` by a performer designated through a `U.RoleAssignment`, **executed within a concrete `U.System`**, including a system in subsystem position when the larger-holon part relation is current, inside a `U.BoundedContext`, that binds concrete parameters, consumes and produces resources, and leaves an auditable trace. When a method-description source is current, `methodDescriptionRef` names the `U.MethodDescription` used to identify, constrain, or justify the enacted method.
When the current claim needs a formal state-change witness, represent the occurrence through a **morphism** `Δ` on a declared **state-plane** (`StatePlaneRef`), mapping pre-state plus inputs to post-state plus outputs for one or more **affected referents**. The work itself remains the dated occurrence; the morphism is the selected mathematical-lens expression for its delta claim.

> **Memory aid:** *Work = “how it went this time”* (dated, resourced, accountable).

#### A.15.1:4.2 - Core reference descriptors (conceptual descriptors; not a data schema)

When you describe a Work instance in a review, answer these prompts:

1. **Window** — start and end timestamps and, where relevant, location or asset.
2. **Method-description source** — `methodDescriptionRef -> U.MethodDescription` when the description source is current; edition pinned when reliance depends on edition.
3. **Performer** — `performedBy → U.RoleAssignment` (whose holder slot, role value, and bounded-context slot admit the performer).
4. **Parameters** — concrete values bound for this run (from the **MethodDescription** parameter declarations).
5. **Inputs and outputs** — materials, information, or product states used or produced by the Work; service delivery is judged through the Outcome row.
6. **Resources** — energy, materials, machine time, money (the **only** place we book them).
7. **Outcome** — success and failure classes, quality measures, acceptance verdicts (**map-then-compare** per **ComparatorSet** under **CG-Spec**; pin editions).
8. **Links** — predecessor, successor, and overlap relations to other Work, plus step or run nesting if part of a bigger operation.
9. **Context** — the bounded context under which this run is judged, normally inherited from the method-description source and `U.RoleAssignment`; see A.15 for cross-checks.
10. **Effect (Δ)** — `affected → {referent(s)}` + **pre-state reference** and **post-state reference** (or a declared **Δ-predicate** evaluated on evidence) on the declared state-plane (**StatePlaneRef**).
11. **System** — `executedWithin -> U.System`; if ordinary speech says subsystem, name the `U.System` in subsystem position plus the part relation to the larger holon under A.1, A.14, or B.1.2 (required for admitting the performed-work claim).
12. **Evidence and telemetry references (when current)** — if the run feeds G.11 refresh or QD and OEE archives, cite the telemetry, evidence, archive, and policy references declared by the governing comparison, archive, evidence, or refresh pattern; do not elevate telemetry into dominance without the governing comparison or archive policy.

#### A.15.1:4.3 - Clear distinctions (the four‑slot grammar in action)

| You are pointing at…                          | The right FPF concept  | Litmus                                                          |
| --------------------------------------------- | ---------------------- | --------------------------------------------------------------- |
| The **recipe, code artifact, or diagram**     | **MethodDescription**         | Is it an episteme or publication describing a way of doing?     |
| The **semantic "way of doing"**               | **Method**             | Same method identity across notations?                         |
| The **assignment** ("who is being what")     | **`U.Role` value plus `U.RoleAssignment` relation** | Can be reassigned without changing the system?                  |
| The **ability** (“can do within bounds”)      | **Capability**         | Would remain even if not assigned?                             |
| The **dated occurrence** with logs, resources | **Work**               | Did it happen at (t₀, t₁), consume resources, produce outcomes? |
| The **state change observed for this occurrence** | **Work.Δ**             | Did the referent change from pre→post on the declared state-plane? |

#### A.15.1:4.4 - Publication-use boundary for `U.Work`

A `U.Work` publication projects an already declared work occurrence; it does not create the occurrence, add run-time facts, or make a plan, source reconstruction, dashboard, or publication face count as performed work.

Preparation work is `U.Work` only when preparation has actually occurred and has its own performer, method, time window, affected referent, resources, and outcome. The readiness relation that asks whether intended work is ready enough to enter a work boundary is `WorkEntryReadiness@Context` under `A.15.5`; a readiness label, full-kit checklist, or launch-looking cue is not a performed occurrence.

| Publication-use pressure | Work-local rule |
|---|---|
| PlainView, TechCard, InteropCard, or AssuranceLane presents work material | Project only occurrence references: time window, performer, enacted method-description source, parameter-binding occurrence, resource-ledger reference, state-change references, outcome, and acceptance-verdict reference when current. |
| numeric, comparable, aggregation, or benchmark content appears | Pin the comparator, aggregation policy, CG-Spec, reference plane, and transport edition needed by the claimed comparison; do not hide scalarization in the publication face. |
| publication cites design-time material or cross-context material | Keep the `U.Work` occurrence run-time; cite the design-time or cross-context material through Bridge relation, UTS relation, `DesignRunTag`, reference-plane, or edition relation as needed. |
| reconstructed records look like a run | Do not synthesize surrogate `U.Work`; a publication may cite only work occurrences that meet the occurrence references in this pattern. |

#### A.15.1:4.5 - Crossing visibility for work publications

When a work publication crosses design-time state, run-time state, context, reference plane, unit, or edition, publish the crossing relation used by the publication. Penalties and reliability changes belong to the relevant comparison, bridge, publication, or evidence relation; they do not change the identity of the `U.Work` occurrence.

Launch values bind only at the occurrence. Plan-time proposals remain proposals; do not back-fill plan publications with run-time bindings. Pre-state and post-state references bind to the occurrence: pre at start, post at completion or at declared checkpoints.

