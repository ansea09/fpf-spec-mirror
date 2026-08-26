---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:4"
section_title: "Solution — admit dated Work occurrences under U.Work"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__005_solution-admit-dated-work-occurrences-under-u-work.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:4 — Solution — admit dated Work occurrences under U.Work"
line_start: 23774
line_end: 23873
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

### A.15.1:4 - Solution — admit dated Work occurrences under `U.Work`

#### A.15.1:4.1 - Definition and occurrence identity

`U.Work` is the admitted U-kind for dated 4D occurrence holons. One Work individual is one independently identified performed occurrence with its own temporal extent. Every actual performer is an admitted `U.System`. For each performer, F.6 identifies the assignment occurrence under which that System performed the Work; the occurrence's directly declared species, actual holder System, assigned local system-role-kind value, any other actual participant values, and covering interval remain recoverable there. Context and reference scheme may qualify an assertion but are not generic assignment participants. The System acts; the assignment neither acts nor enacts a Method.

Elsewhere in FPF, a **complete A.15.1/F.6 basis** means one dated Work occurrence with at least one obtaining `enactsMethod` relation, its temporal extent, and at least one locally declared Work-to-System relation whose stated boundary contains the complete occurrence, plus every actual performer System and the F.6 attribution through that performer's covering assignment occurrence. Name another `enactsMethod` relation or containing-System relation only when the receiving use relies on it. A.2.1 keeps the assignment occurrence's directly declared species and actual participant values recoverable. A consumer may point to this complete basis and state only the distinctions it uses; it need not repeat the full account.

The canonical F.6 relation `performedUnderAssignment(W, RA)` attributes one exact Work occurrence to one exact assignment occurrence. For an obtaining attribution, its actual-performer projection is `S = RA.HolderSystemSlot`; the relation obtains only when admitted system `S` actually performed `W` under `RA` and `RA` covers the attributed extent. In practitioner prose name both objects: `S performed W under RA`. The legacy spelling `performedBy(W, RA)` is a deprecated compatibility alias only; do not author new claims with it, and never say that `RA` performed `W`.

One or more exact `enactsMethod` relations connect the Work individual to the `U.Method` values actually enacted. At least one locally declared Work-to-System relation locates the complete occurrence under an exact containing-system boundary; several may obtain under different valid boundaries. Direct work-to-referent, binding, and performed resource-use relations are recovered independently only when they obtain and the current claim needs them. An occurrence designator permits reference but does not identify work by label, ticket, trace, record, or storage convention; an assertion or description about the occurrence is a separate `U.Episteme`.

The actual `enactsMethod` relation obtains between the Work occurrence and the exact `U.Method`; it is not a field of either participant. An exact `U.MethodDescription` may be cited when its claims identify, constrain, or justify that method for the receiving use; the description is not enacted and its fields do not become actual work bindings. A selected model-use structure likewise enters only through the exact receiving relation whose interpretation it changes.

Call a selected method description, continuity policy, or criterion an **edition** only when an exact C.2.1 `EpistemeEditionRelation` connects it to the earlier episteme and obtains. Otherwise name the selected episteme, or say that one episteme is a non-continuing replacement for another.

#### A.15.1:4.1a - Direct Work relations used by this pattern

These relations are world-side facts, not fields stored in Work. For each A.15.1-owned relation below, both participants must already be independently admitted under the stated kinds. The exact relation kind plus the ordered participant pair identifies the relation occurrence for ordinary use; if a later claim must distinguish its history or compare two occurrences, use A.6.REL. A changed participant pair identifies another occurrence. State a relation only when its predicate passes.

| Relation and participant order | When it obtains and where it applies | Identity, multiplicity, and boundary |
| --- | --- | --- |
| `enactsMethod(work, method)` with `<U.Work, U.Method>` | The performed occurrence actually follows that exact way of doing over the stated Work extent or an explicitly named performed part. A plan, MethodDescription, label, or intended use does not establish it. | Identity is this relation kind plus the ordered Work–Method pair. Every Work enacts at least one Method. Several may obtain when each Method is actually enacted and its covered extent or performed part is stated. |
| `TemporalPartOf_work(part, whole)` with `<U.Work, U.Work>` | The first Work is a proper temporal sub-occurrence of the second: its exact extent is strictly inside the whole's extent and all of its performed content belongs to that same occurrence history. It applies only when the slice is itself useful as an independently admitted Work individual. | Identity is this relation kind plus the ordered part–whole pair. A part may belong to several larger Work occurrences when the predicate passes for each; no unique parent is assumed. An interval, telemetry segment, or record is not thereby a Work part. |
| `EpisodeOf_work(episode, whole)` with `<U.Work, U.Work>` | The first Work is an independently admitted event-bounded sub-occurrence of the second. Actual start and end events and the performed content must establish both the episode boundary and its inclusion in the whole. A named use selects which already grounded episode matters; it does not create the episode. | Identity is this relation kind plus the ordered episode–whole pair. Several episodes and several larger wholes are allowed when each predicate passes. If boundary facts permit more than one grouping, a cited continuity-policy episteme may support the assertion but is not a participant and does not make the relation obtain. |
| `OperationalPartOf_work(part, whole)` with `<U.Work, U.Work>` | The first Work is an independently admitted performed sub-occurrence whose performed content is a constitutive part of the whole occurrence at the stated operational grain. Mere overlap, a Method factor, schedule row, interval, or result label does not establish it. | Identity is this relation kind plus the ordered part–whole pair. Several parts and several containing Work occurrences are allowed when each predicate passes. State any Method-factor relation separately. |

**Containing Systems.** Current assertions do not use bare `executedWithin`. Declare a direct local predicate such as `workOccursWithinPlantBoundary(work, system)` with participant order `<U.Work, U.System>`. Its predicate must say which exact system delimitation and qualification window make the complete Work occurrence lie within that System for the stated use, and must route that delimitation to A.1, A.14, or the applicable domain pattern. Its ordinary occurrence identity is the exact local relation kind plus the ordered Work–System pair. A complete A.15.1 basis has at least one such obtaining relation. The same Work may stand in several true containing-System relations at different valid boundaries; no universal uniqueness or automatic “immediate” System is assumed. A part relation between Systems, organizational accountability, colocation, or a diagram does not by itself create another Work-containment relation. If the use needs one and none is declared and grounded, return `missing-governor[work-containment]`. Historical `executedWithin` is only a route cue to recover this local relation; do not author a new current claim with it.

**Retries and resumptions.** Bare `retryOf` and `resumptionOf` are likewise route cues, not complete universal relation names. A domain that needs either relation declares a local two-participant species over `<U.Work, U.Work>`. A retry predicate states which earlier Work ended without satisfying which independently named completion condition, which target remains current, and which facts make the later Work another attempt rather than mere repetition. A resumption predicate states the earlier unfinished Work, the interruption boundary, and the direct continuity facts that make the later Work continue it rather than start another attempt. For either species, the exact local relation kind plus its ordered later–earlier pair identifies the ordinary occurrence; the declaration states applicability and whether more than one predecessor is allowed. A repeated label, shared Method, or temporal adjacency establishes neither relation. A continuity-policy episteme may support an ambiguous judgment but is not a participant and cannot replace the local predicate.

Ordinary interval relations are not an A.15.1 synonym list. When a Work use needs overlap, precedence, containment, or another interval relation, use C.27.TA to name the temporal bearer, reference, intervals, direct temporal predicate, and the use that needs it; use B.1.4 only when those already recovered relations are aggregated. These declarations also do not replace F.6 `performedUnderAssignment` or a domain-specific Work-to-referent predicate. A consumer names the relation and actual participants rather than citing “the Work record.”

If the receiving sentence says that a referent changed, identify one exact `U.Transformation` independently under A.3.4. If a declared domain predicate relates exact Work W and transformation T, name that predicate, its participant order, and the facts that make it obtain. If no one direct predicate suffices but a one-case compound claim does, use A.6.RCD disposition 2 only when the substrate-admitted constructor, governed base predicates, actual participants, and case facts are recoverable; the result is C.2.1 claim content, not a relation kind or occurrence. Otherwise retain W and T separately and return `missing-governor[work-to-change]`, or A.6.RCD's missing-substrate result when the proposed constructor itself has no current semantics. Shared time, referent, or wording connects neither object. A morphism, delta expression, state-plane trace, pre-state, or post-state may represent or support the neighboring change claim; none is a Work field or identity discriminator.

> **Memory aid:** *Work = “how it went this time”* (dated, resourced, attributable).

#### A.15.1:4.2 - Core occurrence references and neighboring links
When a separate assertion or description episteme describes one Work occurrence, recover the following content at the granularity required by the current use. Each item names an occurrence designator, a world-side relation or temporal fact, or a reference to another episteme; the list is not a slot or field schema for the Work individual:

1. **Occurrence and extent** — one occurrence designator plus exact start and end, or an explicitly open end for in-flight work; add location only when the work claim depends on it.
2. **Performer System and assignment** — name every admitted `U.System` that actually performed the occurrence and use F.6 to establish the assignment under which each System performed it. Keep that assignment's exact species, holder, local system-role kind, any additional participants, and covering interval recoverable through F.6.
3. **Enacted method** — actual `enactsMethod -> U.Method`. Cite `methodDescriptionRef -> U.MethodDescription` only when the receiving claim depends on that exact description episteme; the description is not enacted.
4. **Containing Systems** — name at least one locally declared Work-to-System predicate, its actual Work and `U.System` participants, and the exact system boundary and qualification window that make it obtain. Name several when different valid boundaries matter to the receiving use. A System's part relation to a larger holon does not by itself establish another Work-containment relation.
5. **Work-to-referent relation used by the claim** — name the declared domain predicate, its participant order, and the actual Work and referent participants only when that predicate obtains and the receiving claim uses it. "Work on X", shared timing, a record mention, or a convenient `affected` field establishes no such relation. If the use needs the relation but no predicate governs it, keep the Work and referent and return `missing-governor[work-to-referent]`. An obtaining work-to-referent fact does not by itself assert change, production, delivery, or acceptance.
6. **Actual participation and bindings** — for an operation argument or result, name one identified A.6.1 application and its exact declaration-local binding. For another participant, parameter, supplied constituent, premise, or reference use, name the declared subject predicate, participant order, and actual values. If the required route is absent, name the missing relation or binding in the `missing-governor` result rather than asserting it. A MethodDescription field, plan row, type-compatible value, or log token establishes none of them.
7. **Performed resource use** — name the declared resource-use predicate and its actual Work, resource, amount, unit, and extent participants at the boundary needed by costing or sustainability use. If no predicate governs the needed use, return `missing-governor[resource-use]`; do not infer use from colocation, timing, or a plan estimate.
8. **Continuity policy for an unresolved segmentation** — when a named identity, episode, retry, resumption, or aggregation use has more than one defensible segmentation, cite `workContinuityPolicyRef` to the exact C.2.1 episteme whose claims state the branch criterion and tolerances for that use, and interpret those claims under its effective `U.ReferenceScheme`. If the criterion or its applicability cannot be recovered, leave that segmentation unresolved. The episteme is a `U.MethodDescription` only if it independently satisfies A.3.2's method-description criterion. A simple uninterrupted occurrence needs no continuity-policy reference; the policy supports a judgment about the occurrence and neither constitutes nor rewrites it.
9. **Work mereology and temporal relations** — exact parent, part, predecessor, successor, overlap, retry, or resumption relations only when their predicates obtain.
10. **Actual change and production claims** — identify each actual transformation independently under A.3.4; connect it to Work only through a declared domain predicate with its exact Work and transformation participants or a filled A.6.RCD disposition-2 claim with recoverable constructor, base predicates, participants, and case facts. Otherwise return `missing-governor[work-to-change]`. Keep the current A.15.PROD production-work, entity-identity-inception, and production-completion claims separate. None follows from work identity or parthood.
11. **Evaluation and downstream claims** — use the one matching §4.6 row for evaluation work and result, evidence use, delivery or transfer, and acceptance; omit every row that is not current.
12. **Evidence, publication, and model use** — cite only the exact evidence-use, publication-use, currentness, claim-scope, reference-plane, bridge, or selected model-use relation needed by the receiving claim.

#### A.15.1:4.3 - Clear distinctions (the four‑slot grammar in action)

| You are pointing at…                          | The right FPF concept  | Litmus                                                          |
| --------------------------------------------- | ---------------------- | --------------------------------------------------------------- |
| A claim-bearing episteme expressed through a **recipe, code artifact, or diagram** and substantively about one admitted exact method | **`U.MethodDescription`** | Does the same episteme meet A.3.2's exact membership threshold? Otherwise keep it as the representation, publication, or formal-substrate object already identified by its own pattern; do not call it a MethodDescription. |
| The **semantic "way of doing"**               | **`U.Method`**             | Same method identity across notations?                         |
| The **assignment** (which admitted System is assigned under which local system-role kind in this case) | **one obtaining occurrence of one directly declared species under `U.SystemRoleAssignment`** | Can this assignment occurrence change without changing the System or its declared species? |
| The **ability** ("can do within bounds")      | **`U.Capability`**         | Would remain even if not assigned?                             |
| The **dated occurrence** with logs and resource-use evidence | One Work individual admitted under **`U.Work`** | Did it happen during the stated temporal extent, with the recovered performer system, covering assignment, at least one obtaining `enactsMethod` relation, and at least one declared containing-system relation under an exact boundary? Are any claimed binding, work-to-referent, or resource-use facts independently obtaining? |
| The **actual state change associated with this occurrence** | **`U.Transformation` plus a named domain predicate, or a C.2.1 local compound claim under A.6.RCD disposition 2** | Is the change independently grounded under A.3.4? Does the direct predicate obtain for exact W and T, or does the local claim expose its constructor, governed bases, participants, and case facts? If neither route is present, retain both objects and return `missing-governor[work-to-change]`. |

#### A.15.1:4.4 - Publication-use boundary for `U.Work`

A publication about one Work occurrence projects an already declared assertion or description episteme; it does not create the world-side occurrence, add performed-occurrence facts, or make a plan, source reconstruction, dashboard, publication face, or carrier count as performed work.

Preparation is classifiable as one Work individual under `U.Work` only after it actually occurs and its performer, enacted Method, temporal extent, at least one obtaining locally declared Work-to-System containment relation, and the covering assignment and F.6 attribution for that performer all obtain. Add a Work-to-referent, binding, or resource-use fact only through its own obtaining relation when the receiving preparation claim needs it. `WorkEntryReadiness@Context` under `A.15.5` asks whether intended Work is ready to enter a Work boundary; a readiness label, full-kit checklist, or launch-looking cue is not a performed occurrence.

| Publication-use pressure | Work-local rule |
|---|---|
| PlainView, TechCard, InteropCard, or AssuranceLane presents work material | Project only the work-occurrence references needed by that view: temporal extent, actual performer System, enacted Method, and at least one obtaining local containing-system relation, plus the assignment and F.6 attribution when the receiving claim uses their identity, and any separately established binding, resource-use, or Work-to-referent relation on which the view relies. Project a neighboring result, change, production, delivery, evidence, or judgment only through its matching §4.6 row; do not add a consequence field to Work. |
| numeric, comparable, aggregation, or benchmark content appears | Pin the comparator, aggregation policy, CG-Spec, reference plane, and transport edition needed by the claimed comparison; do not hide scalarization in the publication face. |
| publication cites method-description, work-plan, or cross-context material | Keep the Work occurrence as the dated performed individual admitted under `U.Work`. Cite the exact selected method-description or work-plan episteme. For a semantic crossing, cite an obtaining F.9 Bridge between two exact `SchemeSenseCell` values and state the proposed action, direction, correspondence rule, and tolerated loss in a separate bounded-use claim. Cite a UTS, reference-plane, or edition relation only when its own predicate obtains. |
| reconstructed records look like a performed occurrence | Do not synthesize a surrogate Work occurrence; a publication may cite only Work individuals that meet the occurrence basis in this pattern. |

#### A.15.1:4.5 - Crossing visibility for work publications

When a work publication relies on another selected method-description episteme, name that episteme and the relation the publication actually uses; do not infer an edition from a version label or later date. For a semantic crossing, name the two F.17 sense cells and test the F.9 Bridge predicate profile, then state the proposed action, direction, rule, and tolerated loss in a separate C.2.1 bounded-use claim. For a reference-scheme, claim-scope, model-use, reference-plane, unit, or publication change, cite the direct relation that the publication actually uses. State reliance through the applicable A.10 evidence-use relation or B.3 assurance result, and state any penalty only under its separate policy; none of these facts changes the Work occurrence's identity.

A planned, gate-selected, or launch-labelled value becomes actual only when a named direct predicate with its actual participants obtains, or when an exact A.6.1 operation-application binding connects one identified application to that value. If neither the predicate nor the binding is present, keep the value planned and return `missing-governor[actual-use]`. Do not back-fill a plan or infer an actual binding from shared wording. Pre-state and post-state references remain with an independently governed transformation or comparison claim; bracketing the Work interval does not bind them to the occurrence.

#### A.15.1:4.6 - Route a result or consequence without folding it into Work

Start with the ordinary sentence the reader needs, then select exactly one row for each separate claim. An absent row stays absent; the table is not a result record to fill.

| Reader's sentence | What to identify | Stop / non-inference |
| --- | --- | --- |
| **This work happened.** | A.15.1: exact `W : U.Work`, performer system, covering assignment, enacted Method, extent, and at least one locally declared containing-system relation with its boundary | a log, plan, output, or verdict does not establish `W` |
| **The application returned X** or **X is a result of W.** | exact A.6.1 application and result binding. If the receiving subject also needs a Work-to-result claim, name its already declared domain predicate, exact W and X participants, and obtaining facts; otherwise retain the binding and return `missing-governor[work-to-result]`. Use A.6.P.WMR when the source wording hides which route is intended | a result binding is not production, delivery, acceptance, or a universal work-result relation |
| **This referent changed.** | A.3.4: one exact `U.Transformation`; then name the declared domain predicate with exact W and T participants, or one C.2.1 local compound claim under A.6.RCD disposition 2 with its substrate-admitted constructor, governed base predicates, actual participants, and case facts. Without either, return `missing-governor[work-to-change]` and keep W and T separately usable | temporal overlap, a delta picture, or common referent does not connect the change to W |
| **W produced X**, **X first existed**, or **production completed.** | the one current A.15.PROD branch: production-work participation, entity-identity inception, or production completion, each with its own criterion and boundary | one branch establishes neither of the other two nor delivery or acceptance |
| **Evaluation found V.** | separate evaluation `U.Work`; exact evaluation application and result binding or direct evaluation-result relation; when a durable claim is needed, one C.2.1 evaluation-result episteme | the evaluator's work, returned value, and result episteme are three different objects |
| **These observations support the claim.** | A.10 claim-bound evidence-provenance relation, or A.2.4 for the lighter episteme evidence-use relation | evidence supports the named claim for the bounded use; it does not create the work, result, or verdict |
| **X was delivered or transferred.** | name the declared delivery or transfer predicate, its exact source, destination, transferred X, and any required occurrence or interval participants. Use A.2.3 only when its current promise-content predicate governs this delivery; otherwise return `missing-governor[delivery-or-transfer]` | production, a package, or a handoff label does not establish transfer |
| **X was accepted.** | name the criterion episteme, acceptance or evaluation Work, returned value or result episteme, and the declared acceptance predicate with its exact verdict and X participants. Use A.2.3 only for its current promise-content branch; if no acceptance predicate is present, return `missing-governor[acceptance]` | delivery, a passing evaluation value, or evidence alone does not establish acceptance |

**Three-question result check.** (1) **Did the work occur?** Name `W`, its performer, assignment, enacted Method, time, and at least one declared relation to a containing System under an exact boundary. (2) **What separate result or consequence is claimed?** Name the exact returned value, entity, change, production claim, or transfer and use its row above. (3) **Who judged or accepted what, by which criterion and evidence?** Name the evaluation work, result, evidence relation, and acceptance relation separately. If the reader needs only the first or first two answers, stop there.

