---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment (Contextual Enactment)"
section_id: "A.15:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__005_solution.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.15 — Role–Method–Work Alignment (Contextual Enactment)"
  - "A.15:4 — Solution"
line_start: 19587
line_end: 19699
dependencies:
  - "A.10"
  - "A.12"
  - "A.15.1"
  - "A.15.1-A.15.4"
  - "A.15.4"
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
  - "E.16"
  - "E.17"
  - "E.17.EFP"
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
---

### A.15:4 - Solution
The solution is a stratified alignment that cleanly separates the `design-time` and `run-time` for contextual **enactment**. The bridge between these worlds is the **`U.RoleAssignment`**.

#### A.15:4.1 - The Core Entities: A Strict Distinction

FPF mandates the use of the following distinct, non-overlapping entities to model method, plan, and work enactment. Using them interchangeably is a conformance violation.

**A) Design-Time Entities (The World of Potential):**

*   **`U.Role`:** A contextual "mask" or "job title" (e.g., `TesterRole`). It specifies a function but is not the function itself.
*   **`U.Method`:** The **abstract way-of-doing** inside a context (paradigm-agnostic; may be imperative, functional, logical, or hybrid).
*   **`U.MethodDescription`:** A **`U.Episteme` describing a `U.Method`** (the SOP/algorithm/proof/recipe on a carrier).
*   **`U.Capability`:** An **attribute** of a `U.System` that represents its **ability** to perform the work described in a `MethodDescription`. This is the "skill" or "know-how."
*   **`U.WorkPlan`:** An **`U.Episteme`** declaring **intended `U.Work` occurrences** (windows, dependencies, intended performers as role kinds, budgets) - see **A.15.2**.

**B) The Bridge Entity:**
*   **`U.RoleAssignment`:** The formal assertion `Holder#Role:Context` that links a specific `U.Holon` to a `U.Role` within a `U.BoundedContext`. This holder-to-role assignment link is what "activates" the requirements associated with a role.

**C) Run-Time Entity (The World of Actuality):**

*   **`U.Work`:** An **occurrence** or **event**. It is the concrete, dated, resource-consuming **execution of a `U.MethodDescription`** by a `Holder` acting under a `U.RoleAssignment`; capability checks are evaluated at run time against the holder. This is the only entity that has a start and end time and consumes resources.

**Kinds of Work and the primary target**

**Well-formedness constraint A15-WF-1 (work target and kind).** A `U.Work` occurrence has `primaryTarget: U.Holon` with cardinality `1..1 (total)` and `kind` with cardinality `1..1 (total)`.

Local `kind` values used here:
* Operational - transforms a `U.System` or its environment.
* Communicative (SpeechAct) - transforms a deontic/organizational frame (e.g., commitments, authority states, approvals).
* Epistemic - transforms a `U.Episteme` (e.g., curating a dataset).
The `primaryTarget` disambiguates enactment: what is being acted upon. Example: an approval is `kind=Communicative`, `primaryTarget = Commitment(change=4711)`. A deployment is `kind=Operational`, `primaryTarget = ServiceInstance(prod-us-eu-1)`.

**Didactic Note for Managers: The "Chef" Analogy**

This model can be easily understood using the analogy of a chef in a restaurant.

*   **`ChefRole`** is the **Role**. It's a job title with certain expectations.
*   A **Cookbook (`U.MethodDescription`)** contains the **recipe** for a Souffle. It's a piece of knowledge.
*   The chef's **skill** in making souffles is their **`U.Capability`**. They have this skill even when they are not cooking.
*   The restaurant's rulebook (`U.BoundedContext`) states that anyone in the `ChefRole` *must* have the `Capability` to follow the recipes in the cookbook.
*   The actual act of **making a souffle** on Tuesday evening - using eggs and butter, taking 25 minutes, and consuming gas - is the **`U.Work`**.

Confusing these is like mistaking the cookbook for the souffle. FPF's framework simply makes these common-sense distinctions formal and mandatory.

#### A.15:4.2 - The Canonical Relations: Connecting the Layers

The entities are connected by a set of precise, normative relations that form an unbreakable causal chain. The following diagram illustrates this flow from the abstract context down to the concrete execution.

```mermaid
graph TD
    subgraph Design-Time Scope (Tᴰ)
        A[U.BoundedContext] -- defines --> B(U.Role)
        M[U.Method] -- isDescribedBy --> D[U.MethodDescription]
        Cap[U.Capability] -- supports --> M
        H(U.System as Holder) --> RB(U.RoleAssignment)
        B -- is the role in --> RB
        A -- is the context for --> RB
        A -- bindsCapability(Role,Capability) --> Cap
    end

    subgraph Run-Time Scope (Tᴿ)
        W[U.Work]
    end

    RB -- performedBy --> W
    W  -- isExecutionOf --> D

    style A fill:#e6f3ff,stroke:#36c,stroke-width:2px
    style B fill:#fff2cc,stroke:#d6b656,stroke-width:2px
    style Cap fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    style M fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    style D fill:#f8cecc,stroke:#b85450,stroke-width:2px
    style H fill:#e1d5e7,stroke:#9673a6,stroke-width:2px
    style RB fill:#dae8fc,stroke:#6c8ebf,stroke-width:3px,stroke-dasharray: 5 5
    style W fill:#ffe6cc,stroke:#d79b00,stroke-width:2px,font-weight:bold
```

*   **`bindsCapability(Role, Capability)`:** A `U.BoundedContext` asserts that a given `Role` requires a specific `Capability`. This is a `design-time` rule.
*   **`isDescribedBy(Method, MethodDescription)`:** A `U.Method` is formally described by one or more `MethodDescription`s. This links the abstract way-of-doing to the recipe on a carrier.
*   **`isExecutionOf(Work, MethodDescription)`:** A specific `U.Work` is a `run-time` realization of a `design-time` `MethodDescription`. Capability checks are evaluated against the holder at run time.
*   **`performedBy(Work, RoleAssignment)`:** A `U.Work` is always performed by a specific `Agent` (a `U.RoleAssignment`). This links the work occurrence to the actor-in-context.

_At run time, capability thresholds declared by the context/spec are **checked** against the holder; `U.Work` outcomes provide **evidence** for capability conformance._

This chain provides complete traceability: a specific instance of `U.Work` can be traced back to the `U.MethodDescription` that governed it, the `U.Method` it describes, and the `Agent` (`Holder` + `Role` + `Context`) that was authorized and responsible for its execution.

#### A.15:4.3 - Bounded specialization scouting and `CheckpointReturn`

When one human-plus-AI pair faces a new task family or candidate solution corridor, the governed work system may temporarily compose four distinct local roles inside the same dyad: a human-side `UtilityOwnerRole`, an `AIScoutRole`, an `AISpecialistProbeRole`, and a human-side `CommitAuthorityRole`. The payoff of the dyad is faster admissible specialization of the next move, not disappearance of the human decision step.


For this bounded dyadic work question, the pair should declare one utility target first, enumerate heterogeneous candidate approaches that may satisfy that target, spend a bounded scout or probe budget before any committed approach is chosen, and return one `CheckpointReturn` that compares the tested approaches rather than silently treating one successful probe as a committed rollout. `A.15` governs this dyadic move and local role split only; it does not restate the checkpoint-record semantics of `C.24` or the budget/guard enforcement of `E.16`.

Every `CheckpointReturn` should carry:
- the declared utility target and current `TaskFamily`
- the candidate approaches actually tested
- the evidence observed on each tested approach, including progress toward the named work-measure threshold and important failure signals
- the budget already burned and the residual budget still available
- the recommended next work move or reliance move: continue probing, commit to planned work, narrow the method or claim, hand off, or stop
- the exact commit trigger that would justify leaving the probe state

The return is candidate support, budget posture, observed result, and commit-trigger support. It is not the selected method, not a `U.WorkPlan`, not performed `U.Work`, not execution evidence, and not rollout authority until the governing FPF pattern and exact project-side FPF kind and reference for that selected-method, work-plan, performed-work, execution-evidence, or rollout-authority claim exist.

Low-human-overlap approaches remain admissible here only while they stay tied to the declared utility target, budget guard rails, and evidence basis by value.

#### A.15:4.4 - Boundary to A.15.4 Work-Relevant Source Restoration

Use `A.15.4` when an encountered episteme, episteme publication, display, credential view, generated explanation, copied statement, provenance mark, dashboard tile, schema wording, API wording, or composed source chain is being used to support approval, permission, gate passage, evidence, engineering justification, role currentness, status currentness, release reliance, or performed `U.Work` by appearance.

`A.15` itself keeps the kernel separation: `U.Role`, holder, context, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, actual `U.Work`, and the `U.RoleAssignment` chain between them. The source-restoration question asks which exact project-side FPF kind and reference must be recovered before the encountered item can support the live work claim, reliance claim, or effect; that question belongs to `A.15.4` or to the exact neighboring source pattern named there.

A principle scheme, functional diagram, scenario, screen, or explanation that makes a P2W chain readable may help the team plan work or find the needed source, but it does not become performed `U.Work`, work authority, evidence, gate passage, engineering justification, or release permission by publication alone.

