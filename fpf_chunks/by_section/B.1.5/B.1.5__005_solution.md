---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Γ_method — Order‑Sensitive Method Composition & Work Enactment"
section_id: "B.1.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__005_solution.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "B.1.5 — Γ_method — Order‑Sensitive Method Composition & Work Enactment"
  - "B.1.5:4 — Solution"
line_start: 30009
line_end: 30125
dependencies:
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.3.1"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
keywords:
  - "concurrent"
  - "method composition"
  - "plan vs run"
  - "sequential"
  - "workflow"
---

### B.1.5:4 - Solution

#### B.1.5:4.1 - Terms (didactic recap)

* **U.MethodDescription** — a design‑time description of a `U.Method` (A.3.2): typically an imperative **step‑graph** with **SerialStepOf/ParallelFactorOf**, step **capability types**, **pre/post‑conditions**, and required **external interactions**. (Other admissible description forms exist; B.1.5 focuses on the step‑graph case.)
* **U.Method** — the timeless semantic “way of doing” (capability) described by ≥1 MethodDescription and enacted as `U.Work` (A.3.1, A.15.1).
* **U.Work** — the run‑time, dated enactment occurrence: `performedBy → U.RoleAssignment`, `isExecutionOf → U.MethodDescription` (edition‑pinned), plus concrete slot fillings and resource ledger (A.15.1).
* **U.StepSpec / U.StepMethod** — step‑level specialisations: each `StepSpec` describes a `StepMethod`; a composite `MethodDescription` relates them by order. (Run‑time step occurrences are **Work parts**, not “StepMethods”.)
* **Capability type** — the **state/action signature** a step requires and produces (not to be confused with resources; those belong to Γ\_work).
* **Method Interface Standard (MIC)** — the **order‑aware** analogue of BIC: a short, declarative statement of what **external interactions** of the steps are **Promoted / Forwarded / Encapsulated** at the composite method boundary.

> **Separation reminder.**
> Method composition ≠ resource spending. Keep **resource budgets, yields, dissipation** in **Γ\_work**; **Γ\_method** only checks and composes **order and capability**.

#### B.1.5:4.2 - The operator family (two companion flavours)

To respect the DesignRunTag split, **Γ\_method** is presented as two companion operators sharing the same intent but acting at different `DesignRunTag` positions (spec vs run).

1. **Planning (design‑time) — compose specifications**

   ```
   Γ_method^plan : ( D_spec : OrderedDependencyGraph< U.StepSpec >,
                     σ       : OrderSpec,
                     MIC_in  : optional boundary hints )
                   → U.MethodDescription
   ```

   * **Domain.** `D_spec` contains step specifications linked by **SerialStepOf** / **ParallelFactorOf** (**A.15**).
   * **Result.** A single **U.MethodDescription** whose **MIC** is computed from step interfaces using the **Promote / Forward / Encapsulate** quartet (cf. BIC in B.1.2). The resulting MethodDescription **SHALL** declare the `U.Method` it describes (A.3.2); in the step‑graph case this is the semantic serial/parallel composition of the described `StepMethod`s (A.3.1:9).

2. **Enactment (run‑time) — produce Work**

   ```
   Γ_method^run  : ( M_spec : U.MethodDescription,
                     RA     : U.RoleAssignment,
                     Fill   : carrier & parameter slot fillings )
                   → U.Work
   ```

   * **Domain.** A previously composed **MethodDescription**, a performer designated via **RoleAssignment** (the holder bears the required role in context), and concrete **slot fillings** (carriers, parameters) consistent with the MethodDescription’s declared SlotKinds/ValueKinds (A.6.5).
   * **Result.** A **U.Work** record (the dated run) provided that **capability checks** and **pre/post‑conditions** hold and the MIC is honoured.

**Relationship to Γ\_ctx.**
Both flavours **reuse Γ\_ctx** invariants for order (non‑commutative composition with **NC‑1..3** reproducibility). **Γ\_method** specialises the **typing and boundary rules** for methods and introduces **MIC**.

#### B.1.5:4.3 - Core aggregation rules (design‑time composition)

When computing **Γ\_method^plan(D\_spec, σ)**:

1. **Order preservation.**
   Respect the **OrderSpec σ**; independent branches may be folded in any **topological sort** (Γ\_ctx NC‑3). **SerialStepOf** enforces strict precedence; **ParallelFactorOf** allows concurrency with a **join**.

2. **Capability continuity (typed joins).**
   Every join must be **type-sound**: the **post-condition and output signature** of each incoming branch must **meet** the next step's **pre-conditions** (logical entailment or declared **adapter** steps). Missing adapters are **defects**, not assumptions.

3. **MIC synthesis (boundary behaviour).**
   For each external interaction of a step, decide **Promote / Forward / Encapsulate** into the composite **MIC**. This inherits the clarity of BIC (B.1.2) for methods.

   * *Promote*: becomes a direct composite interaction (e.g., top‑level “start/stop”).
   * *Forward*: remains step‑local but exposed under the composite boundary (namespaced).
   * *Encapsulate*: becomes internal; callers cannot rely on it.

4. **Assurance hooks (without computing assurance).**
   Record where **B.3 assurance** will later hang: (i) the **cutset** steps that bound reliability/quality, (ii) the **integration edges** whose **CL** will penalise poor fit (mappings, fragile joins), and (iii) the **envelope** (G) intended for the method’s validity.

5. **No costs here.**
   If a step lists resources/yields, **do not** aggregate them here. Instead, add a pointer to the corresponding **Γ\_work** composition to be executed with the same order/joins at run‑time.

#### B.1.5:4.4 - Core aggregation rules (run‑time enactment)

When executing **Γ\_method^run(M\_spec, RA, Fill)**:

1. **Role–Method–Spec alignment (A.2 / A.3 / A.15).**
   Confirm that `RA.role` is eligible to enact the `U.Method` described by `M_spec` (or a declared equivalent/refinement in the same context), and that the Work’s `performedBy` and `executedWithin` anchors can be satisfied (A.15.1). If this fails, you may still record an attempted run, but it is **not** a conformant “execution of `M_spec`”.

2. **Pre/post enforcement.**
   Before each step, verify **pre‑conditions** against **Fill** and the evolving carrier state; after, check **post‑conditions** hold. Failing these means the run cannot be certified as a conformant `U.Work` execution of `M_spec`.

3. **Typed state flow.**
   The **state/action types** produced by a step must make the next step **well‑typed**; if not, an **adapter method** (itself with a MethodDescription) must be present in the graph.

4. **Order determinism (Γ\_ctx).**
   Respect the `OrderSpec σ` declared in `M_spec`. Parallel branches may execute independently **only if** they share no state that would break **NC‑1..3**; otherwise they must synchronise at the declared join.

5. **MIC honouring.**
   Interactions exposed by **MIC** are the **only** external commitments the composite method makes. Any additional ad‑hoc external interaction is a **model violation** (or requires updating the MIC and re‑planning).

6. **Γ\_work hand‑off.**
   Invoke **Γ\_work** to compute **spent resources, yields, dissipation** along the same order/join structure. The resulting ledgers and work-result records **annotate the Work** but are **not** part of Γ\_method’s aggregation.

> **Invariant intuition.**
>
> * **IDEM:** a single step‑method composed alone yields the same method.
> * **COMM/LOC:** replaced by Γ\_ctx **NC‑1..3** (determinism given `σ`, context hash of `σ`, and partial‑order soundness).
> * **WLNK:** quality/throughput of the composite is bounded by the **critical path** steps (identified for later B.3 assurance).
> * **MONO:** strengthening a step (better pre/post, stronger type, improved adapter) **cannot** make the composite worse.

#### B.1.5:4.5 - Didactic contrasts (to prevent common confusions)

* **Method vs Work.**
  Method = the semantic “way of doing” (what transformations are admissible); **Work** = what happened this time, including **resources spent / yields / dissipation** when enacting it (Γ\_work). Keep them distinct.

* **Method vs Structure.**
  Method composes **ordered steps**; structure composes **parts** (Γ\_sys). Do not use **ComponentOf** where **SerialStepOf/ParallelFactorOf** are intended.

* **Step vs part vs specialization.**
  A “step” in `SerialStepOf/ParallelFactorOf` is a **factor in an order algebra**, not a mereological part and not a type‑specialisation.
  – Use **ComponentOf/PartOf** for structural wholes (A.14).
  – Use **`≤ₘ` refinement / equivalence / substitution** for Method specialisation (A.3.1).
  – Use **Kind‑CAL (`⊑`)** for kind/subkind.

* **Method vs Phase.**
  Method composition is **order**; **PhaseOf** (Γ\_time) is **temporal progression** of the **same carrier**. If a phase boundary also introduces **closure/supervision/context rebase**, that is **MHT** (B.2), not mere phasing.

* **MethodDescription vs Work.**
  Keep **planning** artefacts (MethodDescription) separate from **run‑time occurrences** (Work). `Γ_method^plan` produces MethodDescriptions; `Γ_method^run` produces Work that cites an edition‑pinned MethodDescription and records effective slot fillings and ledgers (A.15.1).

