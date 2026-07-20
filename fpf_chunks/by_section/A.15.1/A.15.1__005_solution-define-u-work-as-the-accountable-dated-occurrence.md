---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:4"
section_title: "Solution — define U.Work as the accountable, dated occurrence"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__005_solution-define-u-work-as-the-accountable-dated-occurrence.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:4 — Solution — define U.Work as the accountable, dated occurrence"
line_start: 23722
line_end: 23777
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
  - "A.2.6"
  - "A.2.8.PER"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
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
  - "EpisodeOf_work"
  - "TemporalPartOf_work"
  - "actuals"
  - "concurrent work part"
  - "operational work part"
  - "performed enactment"
  - "trace"
  - "work occurrence"
---

### A.15.1:4 - Solution — define `U.Work` as the accountable, dated occurrence

#### A.15.1:4.1 - Definition

**`U.Work`** is a **4D occurrence holon**: a **dated performed enactment** of a `U.Method` by a performer designated through a `U.RoleAssignment`, **executed within a concrete `U.System`**, including a system in subsystem position when the larger-holon part relation is current, with concrete bindings and resource use. When a method-description reference is current, `methodDescriptionRef` names the `U.MethodDescription` used to identify, constrain, or justify the enacted method. A `BoundedModelUseStructure` or one of its direct model-use relations enters only when that model-use organization changes the receiving claim.
When the current claim needs a formal state-change witness, represent the selected change through a **morphism** `Δ` on a declared **state-plane** (`StatePlaneRef`), mapping the selected pre-state to the selected post-state under declared bindings for one or more **affected referents**. The work remains the dated occurrence; the morphism is a mathematical-lens expression for the separately governed change claim and does not establish a universal work-result relation.

> **Memory aid:** *Work = “how it went this time”* (dated, resourced, accountable).

#### A.15.1:4.2 - Core reference descriptors (conceptual descriptors; not a data schema)

When you describe a Work instance in a review, answer these prompts:

1. **Window** — start and end timestamps and, where relevant, location or asset.
2. **Method-description reference** — `methodDescriptionRef -> U.MethodDescription` when the description episteme is current; edition pinned when reliance depends on edition.
3. **Performer** — `performedBy -> U.RoleAssignment`; the referenced assignment has an admitted holder system, role value, role-taxonomy episteme, and effective reference scheme. Its temporal extent is described separately from those four relation participants.
4. **Parameters** — concrete values bound for this occurrence (from the **MethodDescription** parameter declarations).
5. **Direct participation and change claims** — recover each affected referent, used or consumed resource, parameter binding, supplied constituent, premise or reference use, operation argument or result binding, and actual change through its own direct relation or A.6.1 binding. Do not collect these as one input-output family.
6. **Resources** — energy, materials, machine time, money (the **only** place we book them).
7. **Evaluation and downstream-effect claims** — success class, characteristic value, measurement result, comparison result, acceptance verdict, and downstream subject effect remain different objects under their direct patterns. None is an intrinsic field of `U.Work`.
8. **Links** — predecessor, successor, overlap, containment, temporal-part, episode-part, operational-part, concurrent-part, or another declared work relation to other `U.Work` occurrences when composite work is current.
9. **Semantic locality and model use when current** — recover the effective reference scheme, claim scope, exact `ModelUseRelation`, or `BoundedModelUseStructure` required by the receiving claim. Do not infer any of them from the method description or role assignment.
10. **Effect (Δ)** — `affected → {referent(s)}` + **pre-state reference** and **post-state reference** (or a declared **Δ-predicate** evaluated on evidence) on the declared state-plane (**StatePlaneRef**).
11. **System** — `executedWithin -> U.System`; if ordinary speech says subsystem, name the `U.System` in subsystem position plus the part relation to the larger holon under A.1, A.14, or B.1.2 (required for admitting the performed-work claim).
12. **Evidence and telemetry references (when current)** — if the occurrence feeds G.11 refresh or QD and OEE archives, cite the telemetry, evidence, archive, and policy references declared by the governing comparison, archive, evidence, or refresh pattern; do not elevate telemetry into dominance without the governing comparison or archive policy.

#### A.15.1:4.3 - Clear distinctions (the four‑slot grammar in action)

| You are pointing at…                          | The right FPF concept  | Litmus                                                          |
| --------------------------------------------- | ---------------------- | --------------------------------------------------------------- |
| The **recipe, code artifact, or diagram**     | **`U.MethodDescription`**         | Is it an episteme or publication describing a way of doing?     |
| The **semantic "way of doing"**               | **`U.Method`**             | Same method identity across notations?                         |
| The **assignment** ("who is being what")     | **`U.Role` value plus `U.RoleAssignment` relation** | Can be reassigned without changing the system?                  |
| The **ability** ("can do within bounds")      | **`U.Capability`**         | Would remain even if not assigned?                             |
| The **dated occurrence** with logs and resource-use evidence | **`U.Work`** | Did it happen during the stated temporal extent, with the recovered performer, enactment, bindings, affected referent, and resource-use facts? |
| The **state change observed for this occurrence** | **`U.Work` delta claim**             | Did the referent change from pre to post on the declared state-plane? |

#### A.15.1:4.4 - Publication-use boundary for `U.Work`

A `U.Work` publication projects an already declared work occurrence; it does not create the occurrence, add performed-occurrence facts, or make a plan, source reconstruction, dashboard, or publication face count as performed work.

Preparation work is `U.Work` only when preparation has actually occurred and has its own performer assignment, enacted method, temporal extent, affected referent, bindings, and resource-use facts. The readiness relation that asks whether intended work is ready enough to enter a work boundary is `WorkEntryReadiness@Context` under `A.15.5`; a readiness label, full-kit checklist, or launch-looking cue is not a performed occurrence.

| Publication-use pressure | Work-local rule |
|---|---|
| PlainView, TechCard, InteropCard, or AssuranceLane presents work material | Project only the work-occurrence references needed by that view: temporal extent, performer assignment, enacted method, concrete bindings, resource-use claims, and affected referent. Project a change, evaluation-result, evidence, production, delivery, or acceptance reference only as a separately governed neighboring claim. |
| numeric, comparable, aggregation, or benchmark content appears | Pin the comparator, aggregation policy, CG-Spec, reference plane, and transport edition needed by the claimed comparison; do not hide scalarization in the publication face. |
| publication cites method-description, work-plan, or cross-context material | Keep the `U.Work` occurrence as the dated performed occurrence; cite `U.MethodDescription` references, work-plan references, cross-context material, Bridge relation, UTS relation, reference-plane, or edition relation only through the direct governing pattern named for that citation. |
| reconstructed records look like a performed occurrence | Do not synthesize surrogate `U.Work`; a publication may cite only work occurrences that meet the occurrence references in this pattern. |

#### A.15.1:4.5 - Crossing visibility for work publications

When a work publication crosses a method-description edition, effective reference scheme, claim scope, selected model-use structure, reference plane, unit, or publication edition, publish the exact crossing or change relation used by the publication. Penalties and reliability changes belong to the relevant comparison, bridge, publication, or evidence relation; they do not change the identity of the `U.Work` occurrence.

Launch values bind only at the occurrence. Planned proposals remain proposals; do not back-fill plan publications with performed-work bindings. Pre-state and post-state references bind to the occurrence: pre at start, post at completion or at declared checkpoints.

