---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
section_id: "B.1.4:4"
section_title: "Solution — Part 1: What these flavours are, and when to use them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__005_solution-part-1-what-these-flavours-are-and-when-to-use-them.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "B.1.4 — Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
  - "B.1.4:4 — Solution — Part 1: What these flavours are, and when to use them"
line_start: 29373
line_end: 29464
dependencies:
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.1"
keywords:
  - "composition"
  - "order-sensitive"
  - "temporal aggregation"
  - "time-series"
---

### B.1.4:4 - Solution — **Part 1: What these flavours are, and when to use them**

#### B.1.4:4.1 - Two flavours at a glance (edge discipline)

| Flavour                                      | You use it when…                                                      | Edge kinds in `D`                                         | Typical carrier                                                            |
| -------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Γ\_ctx** *(Contextual / order‑sensitive)*  | The **sequence** of steps changes the outcome or meaning.             | `SerialStepOf`, `ParallelFactorOf` (no structural substitution) | `U.Method` (procedures, work processes), also order‑bound argument chains in `U.Episteme` |
| **Γ\_time** *(Temporal / phase aggregation)* | You reconstruct a **timeline** of the **same** holon (phases/slices). | `PhaseOf` of a single carrier (non‑overlapping)                 | Any `U.Holon` with identity across time (systems or epistemes)             |

> **Strict Distinction (A.15) reminder.**
> • Structural inclusion → **Γ\_sys** (ComponentOf / ConstituentOf).
> • Order of actions → **Γ\_ctx** (and its specialisation **Γ\_method**).
> • History of the same carrier identity → **Γ\_time** (PhaseOf).
> • Resource spending → **Γ\_work**.
> • Mappings / representations → value‑level links or `U.Interaction`, not parthood.

#### B.1.4:4.2 - Operator signatures (normative)

**Γ\_ctx — Contextual / Order‑Sensitive Aggregation**

```
Γ\_ctx : (D_ctx : DependencyGraph, σ : OrderSpec, T : U.TransformerRole) → H′ : U.Holon
```

* **D\_ctx:** a DAG whose **edges are only** `SerialStepOf` / `ParallelFactorOf`.
* **σ (OrderSpec):** an explicit **partial order** (or total order) compatible with `D_ctx` that disambiguates how branches compose and where joins occur.
* **T:** the transformer that performs the material act of sequencing/combining steps (A.12).
* **Output H′:** typically a `U.Method` holon, but may be any holon whose identity is defined by stepwise construction.

**Γ\_time — Temporal / Phase Aggregation**

```
Γ\_time : (D_time : DependencyGraph, τ : TimeWindow, T : U.TransformerRole) → H′ : U.Holon
```

* **D\_time:** a DAG whose **edges are only** `PhaseOf`, all phases referring to the **same carrier** identity.
* **τ:** the declared time window to be covered by the aggregation.
* **T:** the transformer that composes the timeline (A.12).
* **Output H′:** the holon reconstructed over τ (system history, theory revision history, dataset growth, etc.).

#### B.1.4:4.3 - Adapted invariants (what replaces COMM/LOC)

Both flavours **keep** IDEM, WLNK, MONO from B.1. They **replace** COMM/LOC by discipline specific to order and time.

**For Γ\_ctx (NC‑invariants):**

* **NC‑1 — Determinism under σ.** Given the same `D_ctx` and `σ`, the fold yields the same result.
* **NC‑2 — Context identifier.** The result **SHALL** record an unambiguous identifier of `σ` (e.g., a canonical text or digest) as part of the aggregation record.
* **NC‑3 — Partial‑Order Soundness.** Any topological sort consistent with `σ` and with declared independence (below) yields the same result; independent branches may fold in parallel.

**For Γ\_time (T‑invariants):**

* **T‑1 — Temporal Idempotence.** A single phase/slice folds to itself.
* **T‑2 — Chronological Discipline.** Phases must be composed in non‑decreasing time consistent with carrier identity; reversing adjacent slices is forbidden.
* **T‑3 — Coverage.** The union of phase intervals equals the declared `τ`, with **no overlaps** and **no unexplained gaps**. Gaps/overlaps require explicit justification (e.g., measurement resolution or MHT).

> **Why we keep WLNK and MONO.**
> Even with order/time, the whole cannot be safer or more reliable than the bottleneck step/phase (WLNK), and improving a step/phase on declared monotone characteristics cannot make the whole worse (MONO).

#### B.1.4:4.4 - Guards that make the folds provable

**For Γ\_ctx**

1. **Edge discipline:** only `SerialStepOf` / `ParallelFactorOf`.
2. **OrderSpec σ:** explicit partial order; joins must have well-typed inputs and outputs (see B.1.5 for join soundness).
3. **Independence declaration:** if you claim parallel folds commute locally, declare **which branches are independent** (no hidden shared state or side‑effects).
4. **Scope:** single `DesignRunTag` (design *or* run) for all nodes; do not mix plans with histories.
5. **Boundary note:** if steps cross holon boundaries, record the relevant `U.Interaction`—do not recast it as parthood.

**For Γ\_time**

1. **Same carrier:** all phases are `PhaseOf` the **same** holon identity; identity change implies a Transformer producing a *new* holon.
2. **Non‑overlap / coverage:** phase intervals are disjoint and cover `τ`; if not, specify how resolution limits or business rules justify the pattern.
3. **Scope:** single `DesignRunTag`; design‑time hypothetical timelines and run‑time actual logs are kept separate.
4. **Boundary note:** if Work across boundaries is reported for phases, route resource statements to **Γ\_work**; Γ\_time itself does not invent costs.

#### B.1.4:4.5 - Selection checklist (didactic quick guide)

* **Does swapping two steps change meaning or safety?** → **Γ\_ctx**.
* **Is this the same entity evolving over time?** → **Γ\_time**.
* **Is it a physical assembly or conceptual inclusion?** → **Γ\_sys**.
* **Is it a “who belongs to this collective” question?** → **MemberOf** + (future) **Γ\_collective**.
* **Do you need durations, critical paths, and joins?** → **Γ\_method** (specialisation of **Γ\_ctx**).
* **Do you need resource spending across a boundary?** → **Γ\_work** (orthogonal; can be used together with Γ\_ctx/Γ\_time).

#### B.1.4:4.6 - Didactic contrasts (one‑liners)

* **Γ\_sys vs Γ\_ctx:** Γ\_sys composes *what the whole is*; Γ\_ctx composes *how it is done*.
* **Γ\_ctx vs Γ\_method:** Γ\_method is Γ\_ctx **plus** step‑specific rules (durations, joins, capability typing).
* **Γ\_time vs Γ\_ctx:** Γ\_time composes *phases of the same carrier*; Γ\_ctx composes *different steps that realise a procedure*.
* **Γ\_time vs Γ\_work:** Γ\_time composes *history*; Γ\_work accounts *costs across a boundary* for each phase.

