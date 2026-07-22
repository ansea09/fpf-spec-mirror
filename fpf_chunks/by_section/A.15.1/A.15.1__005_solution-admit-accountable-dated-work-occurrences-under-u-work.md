---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:4"
section_title: "Solution — admit accountable dated Work occurrences under U.Work"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__005_solution-admit-accountable-dated-work-occurrences-under-u-work.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:4 — Solution — admit accountable dated Work occurrences under U.Work"
line_start: 24294
line_end: 24363
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

### A.15.1:4 - Solution — admit accountable dated Work occurrences under `U.Work`

#### A.15.1:4.1 - Definition and occurrence identity

`U.Work` is the admitted U-kind for dated 4D occurrence holons. One Work individual is one independently identified world-side dated performed occurrence with its own governed temporal extent. Exact `performedBy` relations connect that Work individual to one or more obtaining `U.RoleAssignment` occurrences; each assignment's holder `U.System` is a performer in that attribution. An exact `enactsMethod` relation connects the Work individual to an exact `U.Method`. Exact containing-system, affected-referent, direct subject-relation or A.6.1 binding, and performed resource-use relations are recovered independently when current. An occurrence designator permits reference but does not identify work by label, ticket, trace, record, or storage convention; an assertion or description about the occurrence is a separate `U.Episteme`.

The actual `enactsMethod` relation obtains between the Work occurrence and the exact `U.Method`; it is not a field of either participant. An exact `U.MethodDescription` may be cited when its claims identify, constrain, or justify that method for the receiving use; the description is not enacted and its fields do not become actual work bindings. A selected model-use structure likewise enters only through the exact receiving relation whose interpretation it changes.

When actual change is current, identify one exact `U.Transformation` independently under A.3.4 and recover the exact work-to-change facts under their direct subject governor or the accepted A.15.PROD/A.6.RCD route. A morphism, delta expression, state-plane trace, pre-state, or post-state may represent or support that neighboring change claim; none is a mandatory field of a Work occurrence or a work-identity discriminator by form.

> **Memory aid:** *Work = “how it went this time”* (dated, resourced, accountable).

#### A.15.1:4.2 - Core occurrence references and neighboring links

When a separate assertion or description episteme describes one Work occurrence, recover the following content at the granularity required by the current use. Each item names an occurrence designator, a world-side relation or temporal fact, or a reference to another episteme; the list is not a slot or field schema for the Work individual:

1. **Occurrence and extent** — one occurrence designator plus exact start and end, or an explicitly open end for in-flight work; add location only when the work claim depends on it.
2. **Performer** — each actual `performedBy` relation points to an exact `U.RoleAssignment`; every such assignment has its own holder system, role value, role-taxonomy episteme, effective reference scheme, obtaining condition, and extent under A.2.1.
3. **Enacted method** — actual `enactsMethod -> U.Method`. Cite `methodDescriptionRef -> U.MethodDescription` only when the receiving claim depends on the exact description edition; the description is not enacted.
4. **Containing system** — `executedWithin -> U.System`; if ordinary speech says subsystem, name that `U.System` and its exact part relation to the larger holon.
5. **Affected referent** — the exact subject, asset, product, patient, learner, dataset, document, or other referent with respect to which this occurrence is performed. This work-scope fact does not by itself assert change, production, delivery, or acceptance.
6. **Actual participation and bindings** — each participant, parameter, supplied constituent, premise, reference use, operation argument, or operation result only through an obtaining direct subject relation or exact A.6.1 operation-application binding. A MethodDescription field, plan row, type-compatible value, or log token establishes none of them.
7. **Performed resource use** — exact energy, material, machine-time, money, tool-wear, or other resource-use facts at the boundary needed by costing or sustainability use.
8. **Continuity and identity policy** — `workContinuityPolicyRef` to the exact C.2.1 episteme whose claims state the tolerances, interruption boundaries, and reidentification rule used to resolve descriptions or records to this occurrence. It is not necessarily a `U.MethodDescription` and does not become a work part.
9. **Work mereology and temporal relations** — exact parent, part, predecessor, successor, overlap, retry, or resumption relations only when their predicates obtain.
10. **Actual change and production claims** — exact A.3.4 transformations, direct work-to-change facts, and only the current A.15.PROD production-work, entity-identity-inception, or production-completion claim. None follows from work identity or parthood.
11. **Evaluation and downstream claims** — characteristic value, measurement result, comparison result, evaluation-result episteme, acceptance verdict, delivery, transfer, and downstream effect remain different objects under their direct patterns.
12. **Evidence, publication, and model use** — cite only the exact evidence-use, publication-use, currentness, claim-scope, reference-plane, bridge, or selected model-use relation needed by the receiving claim.

#### A.15.1:4.3 - Clear distinctions (the four‑slot grammar in action)

| You are pointing at…                          | The right FPF concept  | Litmus                                                          |
| --------------------------------------------- | ---------------------- | --------------------------------------------------------------- |
| A claim-bearing episteme expressed through a **recipe, code artifact, or diagram** and substantively about one admitted exact method | **`U.MethodDescription`** | Does the same episteme meet A.3.2's exact membership threshold? Otherwise keep the representation, publication, formal substrate, or other direct owner. |
| The **semantic "way of doing"**               | **`U.Method`**             | Same method identity across notations?                         |
| The **assignment** ("who is being what")     | **`U.Role` value plus `U.RoleAssignment` relation** | Can be reassigned without changing the system?                  |
| The **ability** ("can do within bounds")      | **`U.Capability`**         | Would remain even if not assigned?                             |
| The **dated occurrence** with logs and resource-use evidence | One Work individual admitted under **`U.Work`** | Did it happen during the stated temporal extent, with the recovered performer, enactment, bindings, affected referent, and resource-use facts? |
| The **actual state change associated with this occurrence** | **`U.Transformation` plus exact work-to-change facts** | Is the change independently grounded under A.3.4, and does a separately governed relation connect it to this work? |

#### A.15.1:4.4 - Publication-use boundary for `U.Work`

A publication about one Work occurrence projects an already declared assertion or description episteme; it does not create the world-side occurrence, add performed-occurrence facts, or make a plan, source reconstruction, dashboard, publication face, or carrier count as performed work.

Preparation is classifiable as one Work individual under `U.Work` only after it actually occurs and the exact `performedBy`, `enactsMethod`, temporal, affected-referent, binding, and resource-use relations required by A.15.1 obtain independently. The readiness relation that asks whether intended work is ready enough to enter a work boundary is `WorkEntryReadiness@Context` under `A.15.5`; a readiness label, full-kit checklist, or launch-looking cue is not a performed occurrence.

| Publication-use pressure | Work-local rule |
|---|---|
| PlainView, TechCard, InteropCard, or AssuranceLane presents work material | Project only the work-occurrence references needed by that view: temporal extent, performer assignment, enacted method, concrete bindings, resource-use claims, and affected referent. Project a change, evaluation-result, evidence, production, delivery, or acceptance reference only as a separately governed neighboring claim. |
| numeric, comparable, aggregation, or benchmark content appears | Pin the comparator, aggregation policy, CG-Spec, reference plane, and transport edition needed by the claimed comparison; do not hide scalarization in the publication face. |
| publication cites method-description, work-plan, or cross-context material | Keep the Work occurrence as the dated performed individual admitted under `U.Work`; cite `U.MethodDescription` references, work-plan references, cross-context material, Bridge relation, UTS relation, reference-plane, or edition relation only through the direct governing pattern named for that citation. |
| reconstructed records look like a performed occurrence | Do not synthesize a surrogate Work occurrence; a publication may cite only Work individuals that meet the occurrence basis in this pattern. |

#### A.15.1:4.5 - Crossing visibility for work publications

When a work publication crosses a method-description edition, effective reference scheme, claim scope, selected model-use structure, reference plane, unit, or publication edition, publish the exact crossing or change relation used by the publication. Penalties and reliability changes belong to the relevant comparison, bridge, publication, or evidence relation; they do not change the identity of the Work occurrence.

A planned, gate-selected, or launch-labelled value becomes actual only when an obtaining direct subject relation or exact A.6.1 operation-application binding makes it participate in the occurrence. Do not back-fill a plan or infer an actual binding from shared wording. Pre-state and post-state references remain with an independently governed transformation or comparison claim; they do not bind to the Work occurrence merely because their times bracket it.

#### A.15.1:4.6 - Route neighboring participant, change, and production claims

| Current claim | Direct route from exact Work | Non-inference |
| --- | --- | --- |
| actual participant in a direct subject relation | cite the independently identified obtaining relation occurrence and its exact participant | work scope, plan content, or type compatibility does not establish participation |
| actual operation argument or result | cite the exact A.6.1 application and operation-application binding | a MethodDescription field or A.15.3 planned filling is not an actual binding |
| actual changed referent | cite the independently identified A.3.4 transformation and exact work-to-change fact | temporal overlap, a delta expression, or common referent does not establish the link |
| production-work participation | use the A.15.PROD whole-work or exact proper-work-part branch | work, work parthood, or an intended method effect does not make the occurrence production work |
| entity-identity inception or production completion | cite the exact A.15.PROD local claim with its specification or criterion edition and boundary | neither claim follows from work completion, result wording, delivery, or acceptance |
| evaluation, result episteme, delivery, acceptance, or downstream effect | cite its exact direct governor and relation to the work or subject when current | none is an intrinsic Work field or identity discriminator |

