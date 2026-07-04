---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment (Contextual Enactment)"
section_id: "A.15:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__005_solution.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "A.15 — Role–Method–Work Alignment (Contextual Enactment)"
  - "A.15:4 — Solution"
line_start: 21450
line_end: 21576
dependencies:
  - "A.10"
  - "A.12"
  - "A.15"
  - "A.15.1-A.15.5"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.4"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "B.3"
  - "C.24"
  - "C.26.2"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.16"
  - "E.17"
  - "E.17.EFP"
  - "E.18.1"
keywords:
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.WorkPlan"
  - "actual U.Work"
  - "contextual enactment"
  - "coordinated-work evidence"
  - "role-method-work distinction"
  - "source-restoration boundary"
  - "work admission display"
  - "work-entry readiness"
---

### A.15:4 - Solution

**Method and work governing-pattern cue.**
 When a source-side "process", "algorithm", "solver", "workflow", "procedure", or similar label points to changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern`, use `E.10.ARCH:3.1` to recover the project concern first and then assign separately governed typed values. A.15 carries only the alignment among role, method, method-description, work-plan, and performed-work references. Formal substrate, mathematical-lens use, mechanism declaration or realization, evidence, gate, source, result, publication, and temporal claims are governed by their own patterns.

When methods are related to one another, A.15 keeps only the alignment use of that relation. The method-side object is `MethodRelationStructure@BoundedContext` under `A.3.1`, `A.3.2`, `G.5`, or a direct method-composition pattern when current. A method algebra, workflow graph, process calculus, matrix, category, embedding, or neural representation is a lens or method description over that structure, not a role relation, work plan, dated work occurrence, or assignment relation.
The solution is a stratified alignment that cleanly separates semantic method, method-description source, holder-in-role assignment, holder `U.Capability` instances when relied on, separate capability statements or currentness assessments when those are used, separate capability-fit conditions when current, intended work plan, and dated performed work. The work-facing assignment relation is **`U.RoleAssignment`**.

#### A.15:4.1 - The Core Entities: A Strict Distinction

FPF mandates the use of the following distinct, non-overlapping entities to model method, plan, and work enactment. Using them interchangeably is a conformance violation.

**A) Method, Description, Capability, And Plan Values:**

*   **`U.Role`:** A context-bound role value naming what a holder is being in a bounded context. Expected contribution, responsibility, permission, commitment, obligation, capability-fit, and admission conditions are neighboring relations governed by their direct patterns; the role value is not the holder, method, capability, work plan, or work occurrence.
*   **`U.Method`:** The **abstract way-of-doing** inside a context (paradigm-agnostic; may be imperative, functional, logical, or hybrid).
*   **`U.MethodDescription`:** A **`U.Episteme` describing a `U.Method`**; it may be expressed in an SOP, algorithm, proof, recipe, or other method-description publication.
*   **`U.Capability`:** The `A.2.2` admitted dependent durable U-kind for holder-dependent capability instances. A concrete instance is a `U.System` holder's ability to perform a work family or produce a result class within a declared envelope, measure set, qualification window, and currentness condition. A `CapabilityStatement`, evidence relation, source-use relation, or currentness assessment may support relying on that instance; a capability-fit condition may test it. The capability instance is not the method, method description, support record, fit predicate, work plan, or work occurrence.
*   **`U.WorkPlan`:** An **`U.Episteme`** declaring **intended `U.Work` occurrences** (windows, dependencies, intended performers as role kinds, budgets) - see **A.15.2**.

**B) The Bridge Entity:**
*   **`U.RoleAssignment`:** The typed assignment relation for enactment-facing roles. It links a holder system or acting holon, a `U.Role`, a `U.BoundedContext`, any current window, and justification or source references when they matter.

**C) Performed Occurrence:**

*   **`U.Work`:** An **occurrence** or **event**. It is the concrete, dated, resource-consuming enactment or execution of a `U.Method` by a holder under a `U.RoleAssignment`; capability-fit checks are evaluated against that holder for the occurrence, and `methodDescriptionRef` names the source episteme used to identify or constrain the method when that source is being used for the work claim. This is the only value in this alignment that has a start and end time and consumes resources.

**Kinds of Work and the primary target**

**Well-formedness constraint A15-WF-1 (work target and kind).** A `U.Work` occurrence has `primaryTarget: U.Holon` with cardinality `1..1 (total)` and `kind` with cardinality `1..1 (total)`.

Local `kind` values used here:
* Operational - transforms a `U.System` or its environment.
* Communicative (SpeechAct) - transforms a deontic or organizational frame (e.g., commitments, authority effects, approvals).
* Epistemic - transforms a `U.Episteme` (e.g., curating a dataset).
The `primaryTarget` disambiguates enactment: what is being acted upon. Example: an approval is `kind=Communicative`, `primaryTarget = Commitment(change=4711)`. A deployment is `kind=Operational`, `primaryTarget = ServiceInstance(prod-us-eu-1)`.

**Didactic Note for Managers: The "Chef" Analogy**

This model can be easily understood using the analogy of a chef in a restaurant.

*   **`ChefRole`** is the **Role**. It's a job title with certain expectations.
*   A **Cookbook (`U.MethodDescription`)** contains the **recipe** for a Souffle. It's a piece of knowledge.
*   The chef's **skill** in making souffles is their **`U.Capability`** instance. They have this skill even when they are not cooking, while a certificate or review about the skill is a separate support record.
*   The restaurant's rulebook (`U.BoundedContext`) states that a holder assigned to `ChefRole` needs the capability to follow the recipes in the cookbook before the relevant cooking work is admitted.
*   The actual act of **making a souffle** on Tuesday evening - using eggs and butter, taking 25 minutes, and consuming gas - is the **`U.Work`**.

Confusing these is like mistaking the cookbook for the souffle. FPF's framework simply makes these common-sense distinctions formal and mandatory.

#### A.15:4.2 - The Canonical Relations: Connecting the Layers

The entities are connected by precise, normative relations that form a traceable alignment chain. The following diagram illustrates the relation chain from bounded context and method description to dated work occurrence.

```mermaid
graph TD
    subgraph Method, Role, and Plan Scope
        A[U.BoundedContext] -- defines --> B(U.Role)
        M[U.Method] -- isDescribedBy --> D[U.MethodDescription]
        Cap[U.Capability instance] -- ability-for method family --> M
        Fit[CapabilityFitCondition] -- tests declared measures of --> Cap
        Fit -- may cite --> Q[U.Characteristic value, Q-Bundle slot, or architecture-characteristic row]
        H(U.System as Holder) --> RB(U.RoleAssignment)
        B -- is the role in --> RB
        A -- is the context for --> RB
        A -- declares work-admission condition --> Fit
    end

    subgraph Performed Work Occurrence
        W[U.Work]
    end

    W -- performedBy --> RB
    W  -- enactsMethod --> M

    style A fill:#e6f3ff,stroke:#36c,stroke-width:2px
    style B fill:#fff2cc,stroke:#d6b656,stroke-width:2px
    style Cap fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    style Fit fill:#d5e8d4,stroke:#82b366,stroke-width:2px,stroke-dasharray: 4 4
    style Q fill:#fff2cc,stroke:#d6b656,stroke-width:2px,stroke-dasharray: 4 4
    style M fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    style D fill:#f8cecc,stroke:#b85450,stroke-width:2px
    style H fill:#e1d5e7,stroke:#9673a6,stroke-width:2px
    style RB fill:#dae8fc,stroke:#6c8ebf,stroke-width:3px,stroke-dasharray: 5 5
    style W fill:#ffe6cc,stroke:#d79b00,stroke-width:2px,font-weight:bold
```

*   **Capability-fit condition:** A bounded context, method-description source, work plan, or work-admission rule may state that the holder under a `U.RoleAssignment` must satisfy a capability threshold or envelope for a method or work claim. The fit condition tests the holder's `U.Capability` instance and may cite declared capability measures, `U.Characteristic` values, Q-Bundle slots, or architecture-characteristic criteria rows. The role value does not own the capability, the support record does not become the capability, and the fit condition is not a second capability kind.
*   **`isDescribedBy(Method, MethodDescription)`:** A `U.Method` is formally described by one or more `MethodDescription`s. This links the abstract way-of-doing to the method-description episteme and to the publication used when that source is being used for the method claim.
*   **`enactsMethod(Work, Method)`:** A specific `U.Work` is a dated performed enactment of a `U.Method` under a `U.RoleAssignment`. Capability-fit checks are evaluated against the holder for that occurrence; the `MethodDescription` remains the source episteme or method-description reference used to identify, constrain, or justify the method when that source is being used for the work claim.
*   **`performedBy(Work, RoleAssignment)`:** A `U.Work` is performed by the holder named through a specific `U.RoleAssignment`. This links the work occurrence to the holder-in-role-in-context.

For a performed occurrence, capability thresholds declared by the context, method-description source, work plan, or work-admission rule are **checked** against the holder; `U.Work` outcomes provide **evidence** for capability conformance only through the governing evidence or evaluation relation.

This chain provides complete traceability: a specific instance of `U.Work` can be traced back to the `U.Method` it enacts, the `MethodDescription` or source publication used to identify or constrain that method, and the `U.RoleAssignment` relation whose holder, role, bounded-context, and current-window slots make the holder-in-role admission explicit.

#### A.15:4.3 - Bounded specialization scouting and `CheckpointReturn`

When one human-plus-AI pair faces a new task family or candidate solution family, the governed work system may temporarily compose four distinct local roles inside the same dyad: a human-held `OutcomeCriterionHolderRole`, an `AIScoutRole`, an `AISpecialistProbeRole`, and a human-held `CommitAuthorityRole`. The payoff of the dyad is faster admissible specialization of the next work-family use, not disappearance of the human decision step.

For this bounded dyadic work question, the pair declares one outcome criterion first, enumerates heterogeneous candidate approaches that may satisfy that target, spends a bounded scouting budget or probing budget before any committed approach is chosen, and returns one `CheckpointReturn` that compares the tested approaches rather than silently treating one successful probe as a committed rollout. `A.15` governs this dyadic alignment use and local role split only; it does not restate the checkpoint-record semantics of `C.24` or the budget and guard enforcement of `E.16`.

Every `CheckpointReturn` carries:
- the declared outcome criterion and current `TaskFamily`
- the candidate approaches actually tested
- the evidence observed on each tested approach, including progress toward the named work-measure threshold and important failure signals
- the budget already burned and the residual budget still available
- the recommended next work-family use or reliance use: continue probing, commit to planned work, narrow the method or claim, apply the direct governing pattern for a non-A.15 claim, or stop
- the commit trigger named by value that would justify leaving the bounded probe

The return is candidate-approach evidence, burned and residual budget amounts, observed result, and commit-trigger condition. It is not the selected method, `U.WorkPlan`, performed `U.Work`, execution evidence relation, evidence-provenance relation, or rollout decision. Those claims need the project-side FPF kind and reference named by value before committed rollout.

Low-human-overlap approaches remain admissible here only while they stay tied to the declared outcome criterion, budget limits, and evidence relation or evidence-provenance relation by value.

#### A.15:4.4 - Boundary to A.15.4 Work-Relevant Source Restoration

Use `A.15.4` when an encountered episteme, episteme publication, display, credential view, generated explanation, copied statement, provenance mark, dashboard tile, schema wording, API wording, or composed source chain is being used by appearance for a work claim, reliance claim, role-assignment currentness claim, role-state currentness claim, source-currentness claim, approval, authorization, gate passage, evidence, engineering justification, release reliance, or performed `U.Work`.

`A.15` itself keeps the kernel separation: `U.Role`, holder, context, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, dated performed `U.Work`, and the `U.RoleAssignment` chain between them. The source-restoration question recovers the project-side FPF kind and reference named by value before the encountered source candidate or display can carry the work claim, reliance claim, or effect claim being made; that question belongs to `A.15.4` or to the source-restoration pattern governing that reliance named there.

A principle scheme, functional diagram, scenario, screen, or explanation that makes an `E.18.1` P2W carry-through structure recoverable may help the team plan work or find the needed source.

#### A.15:4.5 - Boundary to A.15.5 Work-Entry Readiness

Use `A.15.5` when the current question is whether intended work is ready enough to enter a work boundary. `A.15` keeps the role-method-work separation; `A.15.5` carries `WorkEntryReadiness@Context`, `FullKitCondition`, commitment disposition, resource-readiness refs, WIP or flow-policy refs, planned-baseline refs, and launch-gate refs when they are current.

Readiness is not performed work, not evidence sufficiency, and not gate passage by itself. A readiness-looking briefing, dashboard, source bundle, or P2W record may cue `A.15.5`, but the readiness relation is admitted only when the target work plan or plan item, missing inputs, preparation work if performed, planned baseline, and stop or degraded-use condition can be named.

