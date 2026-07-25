---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:4"
section_title: "Solution — admit accountable dated Work occurrences under U.Work"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__005_solution-admit-accountable-dated-work-occurrences-under-u-work.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:4 — Solution — admit accountable dated Work occurrences under U.Work"
line_start: 24278
line_end: 24357
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

### A.15.1:4 - Solution — admit accountable dated Work occurrences under `U.Work`

#### A.15.1:4.1 - Definition and occurrence identity

`U.Work` is the admitted U-kind for dated 4D occurrence holons. One Work individual is one independently identified world-side dated performed occurrence with its own governed temporal extent. The actual performer is an admitted `U.System`. For every performer, recover the exact obtaining `U.RoleAssignment` whose `HolderSystemSlot` resolves to that system, whose role interpretation is current, and whose occurrence covers the work or the exact attributed work part. The system acts; the assignment is the world-side relation under which the attribution holds, and it neither acts nor enacts a method.

The canonical F.6 relation `performedUnderAssignment(W, RA)` attributes one exact Work occurrence to one exact assignment occurrence. For an obtaining attribution, its actual-performer projection is `S = RA.HolderSystemSlot`; the relation obtains only when admitted system `S` actually performed `W` under `RA` and `RA` covers the attributed extent. In practitioner prose name both objects: `S performed W under RA`. The legacy spelling `performedBy(W, RA)` is a deprecated compatibility alias only; do not author new claims with it, and never say that `RA` performed `W`.

An exact `enactsMethod` relation connects the Work individual to an exact `U.Method`, and one exact `executedWithin` relation names its containing `U.System`. Direct work-to-referent, binding, and performed resource-use relations are recovered independently only when they obtain and the current claim needs them. An occurrence designator permits reference but does not identify work by label, ticket, trace, record, or storage convention; an assertion or description about the occurrence is a separate `U.Episteme`.

The actual `enactsMethod` relation obtains between the Work occurrence and the exact `U.Method`; it is not a field of either participant. An exact `U.MethodDescription` may be cited when its claims identify, constrain, or justify that method for the receiving use; the description is not enacted and its fields do not become actual work bindings. A selected model-use structure likewise enters only through the exact receiving relation whose interpretation it changes.

When actual change is current, identify one exact `U.Transformation` independently under A.3.4 and recover the exact work-to-change facts under their direct subject governor or the accepted A.15.PROD/A.6.RCD route. A morphism, delta expression, state-plane trace, pre-state, or post-state may represent or support that neighboring change claim; none is a mandatory field of a Work occurrence or a work-identity discriminator by form.

> **Memory aid:** *Work = “how it went this time”* (dated, resourced, accountable).

#### A.15.1:4.2 - Core occurrence references and neighboring links

When a separate assertion or description episteme describes one Work occurrence, recover the following content at the granularity required by the current use. Each item names an occurrence designator, a world-side relation or temporal fact, or a reference to another episteme; the list is not a slot or field schema for the Work individual:

1. **Occurrence and extent** — one occurrence designator plus exact start and end, or an explicitly open end for in-flight work; add location only when the work claim depends on it.
2. **Performer system and assignment** — name each admitted holder `U.System` that actually performed the occurrence and the exact obtaining `U.RoleAssignment` under which it performed. Verify that the assignment's `HolderSystemSlot` resolves to that same system and recover its role value, role-taxonomy episteme, effective reference scheme, obtaining condition, and extent under A.2.1. When explicit F.6 attribution identity is used, `performedUnderAssignment(W, RA)` cites `RA` as the assignment ground; the actual performer remains its holder system.
3. **Enacted method** — actual `enactsMethod -> U.Method`. Cite `methodDescriptionRef -> U.MethodDescription` only when the receiving claim depends on the exact description edition; the description is not enacted.
4. **Containing system** — `executedWithin -> U.System`; if ordinary speech says subsystem, name that `U.System` and its exact part relation to the larger holon.
5. **Work-to-referent relation, when current** — name the exact direct subject relation and its subject, asset, product, patient, learner, dataset, document, or other referent only when that relation actually obtains and the receiving claim uses it. "Work on X", shared timing, a record mention, or a convenient `affected` field establishes no such relation. An obtaining work-to-referent fact does not by itself assert change, production, delivery, or acceptance.
6. **Actual participation and bindings** — each participant, parameter, supplied constituent, premise, reference use, operation argument, or operation result only through an obtaining direct subject relation or exact A.6.1 operation-application binding. A MethodDescription field, plan row, type-compatible value, or log token establishes none of them.
7. **Performed resource use** — exact energy, material, machine-time, money, tool-wear, or other resource-use facts at the boundary needed by costing or sustainability use.
8. **Continuity policy, only when current** — when a named identity, episode, retry, resumption, or aggregation use must resolve an ambiguous segmentation, cite `workContinuityPolicyRef` to the exact C.2.1 episteme whose claims state the branch criterion and tolerances for that use. Interpret it under its effective `U.ReferenceScheme` and direct policy owner when one exists. It is a `U.MethodDescription` only if the same episteme independently satisfies A.3.2's method-description criterion. A simple uninterrupted occurrence needs no continuity-policy reference; the policy supports a judgment about the occurrence and neither constitutes nor rewrites it.
9. **Work mereology and temporal relations** — exact parent, part, predecessor, successor, overlap, retry, or resumption relations only when their predicates obtain.
10. **Actual change and production claims** — exact A.3.4 transformations, direct work-to-change facts, and only the current A.15.PROD production-work, entity-identity-inception, or production-completion claim. None follows from work identity or parthood.
11. **Evaluation and downstream claims** — use the one matching §4.6 row for evaluation work and result, evidence use, delivery or transfer, and acceptance; omit every row that is not current.
12. **Evidence, publication, and model use** — cite only the exact evidence-use, publication-use, currentness, claim-scope, reference-plane, bridge, or selected model-use relation needed by the receiving claim.

#### A.15.1:4.3 - Clear distinctions (the four‑slot grammar in action)

| You are pointing at…                          | The right FPF concept  | Litmus                                                          |
| --------------------------------------------- | ---------------------- | --------------------------------------------------------------- |
| A claim-bearing episteme expressed through a **recipe, code artifact, or diagram** and substantively about one admitted exact method | **`U.MethodDescription`** | Does the same episteme meet A.3.2's exact membership threshold? Otherwise keep the representation, publication, formal substrate, or other direct owner. |
| The **semantic "way of doing"**               | **`U.Method`**             | Same method identity across notations?                         |
| The **assignment** ("who is being what")     | **`U.Role` value plus `U.RoleAssignment` relation** | Can be reassigned without changing the system?                  |
| The **ability** ("can do within bounds")      | **`U.Capability`**         | Would remain even if not assigned?                             |
| The **dated occurrence** with logs and resource-use evidence | One Work individual admitted under **`U.Work`** | Did it happen during the stated temporal extent, with the recovered performer system, covering assignment, enactment, and containing system? Are any claimed binding, work-to-referent, or resource-use facts independently obtaining? |
| The **actual state change associated with this occurrence** | **`U.Transformation` plus exact work-to-change facts** | Is the change independently grounded under A.3.4, and does a separately governed relation connect it to this work? |

#### A.15.1:4.4 - Publication-use boundary for `U.Work`

A publication about one Work occurrence projects an already declared assertion or description episteme; it does not create the world-side occurrence, add performed-occurrence facts, or make a plan, source reconstruction, dashboard, publication face, or carrier count as performed work.

Preparation is classifiable as one Work individual under `U.Work` only after it actually occurs and the actual performer `U.System`, its covering `U.RoleAssignment` and F.6 attribution when explicit, the exact `enactsMethod`, temporal extent, and `executedWithin` relation obtain independently. Add a work-to-referent, binding, or resource-use fact only through its own obtaining relation when the receiving preparation claim needs it. The readiness relation that asks whether intended work is ready enough to enter a work boundary is `WorkEntryReadiness@Context` under `A.15.5`; a readiness label, full-kit checklist, or launch-looking cue is not a performed occurrence.

| Publication-use pressure | Work-local rule |
|---|---|
| PlainView, TechCard, InteropCard, or AssuranceLane presents work material | Project only the work-occurrence references needed by that view: temporal extent, actual performer system, covering assignment and F.6 attribution when explicit, enacted method, and containing system, plus any independently obtaining binding, resource-use, or work-to-referent relation on which the view relies. Project a neighboring result, change, production, delivery, evidence, or judgment only through its matching §4.6 row; do not add a consequence field to Work. |
| numeric, comparable, aggregation, or benchmark content appears | Pin the comparator, aggregation policy, CG-Spec, reference plane, and transport edition needed by the claimed comparison; do not hide scalarization in the publication face. |
| publication cites method-description, work-plan, or cross-context material | Keep the Work occurrence as the dated performed individual admitted under `U.Work`; cite `U.MethodDescription` references, work-plan references, cross-context material, Bridge relation, UTS relation, reference-plane, or edition relation only through the direct governing pattern named for that citation. |
| reconstructed records look like a performed occurrence | Do not synthesize a surrogate Work occurrence; a publication may cite only Work individuals that meet the occurrence basis in this pattern. |

#### A.15.1:4.5 - Crossing visibility for work publications

When a work publication crosses a method-description edition, effective reference scheme, claim scope, selected model-use structure, reference plane, unit, or publication edition, publish the exact crossing or change relation used by the publication. Penalties and reliability changes belong to the relevant comparison, bridge, publication, or evidence relation; they do not change the identity of the Work occurrence.

A planned, gate-selected, or launch-labelled value becomes actual only when an obtaining direct subject relation or exact A.6.1 operation-application binding makes it participate in the occurrence. Do not back-fill a plan or infer an actual binding from shared wording. Pre-state and post-state references remain with an independently governed transformation or comparison claim; they do not bind to the Work occurrence merely because their times bracket it.

#### A.15.1:4.6 - Route a result or consequence to its direct owner

Start with the ordinary sentence the reader needs, then select exactly one row for each separate claim. An absent row stays absent; the table is not a result record to fill.

| Reader's sentence | Direct owner and exact object | Stop / non-inference |
| --- | --- | --- |
| **This work happened.** | A.15.1: exact `W : U.Work`, performer system, covering assignment, enacted method, extent, and containing system | a log, plan, output, or verdict does not establish `W` |
| **The application returned X** or **X is a result of W.** | exact A.6.1 application and result binding; add an already governed subject-specific `WorkResultRelation` only when its predicate actually obtains. If the wording hides the relation, use A.6.P.WMR to recover it | a result binding is not production, delivery, acceptance, or a universal work-result relation |
| **This referent changed.** | A.3.4: one exact `U.Transformation` plus the exact subject-governed work-to-change fact | temporal overlap, a delta picture, or common referent does not connect the change to `W` |
| **W produced X**, **X first existed**, or **production completed.** | the one current A.15.PROD branch: production-work participation, entity-identity inception, or production completion, each with its own criterion and boundary | one branch establishes neither of the other two nor delivery or acceptance |
| **Evaluation found V.** | separate evaluation `U.Work`; exact evaluation application and result binding or direct evaluation-result relation; when a durable claim is needed, one C.2.1 evaluation-result episteme | the evaluator's work, returned value, and result episteme are three different objects |
| **These observations support the claim.** | A.10 claim-bound evidence-provenance relation, or A.2.4 for the lighter episteme evidence-use relation | evidence supports the named claim for the bounded use; it does not create the work, result, or verdict |
| **X was delivered or transferred.** | the exact subject-owned delivery or transfer relation; use A.2.3 only when a current promise-content use supplies its delivery predicate | production, a package, or a handoff label does not establish transfer; absent a direct governor, return the exact missing-governor blocker |
| **X was accepted.** | exact criterion edition, acceptance or evaluation work, result binding or result episteme, and the exact subject-owned acceptance relation; use A.2.3 only for its promise-content branch | delivery, a passing evaluation value, or evidence alone does not establish acceptance |

**Three-question result check.** (1) **Did the work occur?** Name `W` and its performer, assignment, method, time, and containing system. (2) **What separate result or consequence is claimed?** Name the exact returned value, entity, change, production claim, or transfer and use its row above. (3) **Who judged or accepted what, by which criterion and evidence?** Name the evaluation work, result, evidence relation, and acceptance relation separately. If the reader needs only the first or first two answers, stop there.

