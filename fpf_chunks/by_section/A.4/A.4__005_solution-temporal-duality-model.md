---
chunk_kind: "child"
pattern_id: "A.4"
pattern_title: "Temporal Duality & Open‑Ended Evolution Principle"
section_id: "A.4:4"
section_title: "Solution - Temporal Duality Model"
source_path: "FPF-Spec.md"
output_path: "by_section/A.4/A.4__005_solution-temporal-duality-model.md"
commit_sha: "f0b498ddfdf562242984ff7ab7a2557b55af6690"
heading_path:
  - "A.4 — Temporal Duality & Open‑Ended Evolution Principle"
  - "A.4:4 — Solution - Temporal Duality Model"
line_start: 9414
line_end: 9446
dependencies:
  - "B.4"
keywords:
  - "continuous improvement"
  - "design-time"
  - "evolution"
  - "open-ended state change"
  - "run-time"
  - "versioning"
---

### A.4:4 - Solution - Temporal Duality Model

FPF assigns every holon state to one—and only one—of two **temporal
scopes**:

| Scope | Symbol | Definition | Typical contents |
|-------|--------|------------|------------------|
| **Design‑Time** | *Tᴰ* | Interval(s) during which the holon **may be structurally altered** by an *external* `Transformer` executing a `U.TransformationalMethod`. | Specs, CAD, theorem scripts, IaC SCRs. |
| **Run‑Time** | *Tᴿ* | Interval(s) during which the holon **executes its own `OperationalMethod`s** and is assumed structurally stable (self‑maintenance allowed). | Telemetry, transaction logs, field data, physical wear. |

**Temporal invariants**

```text
Tᴰ ∩ Tᴿ = ∅                     (never overlap)
Tᴰ ∪ Tᴿ = worldline(holon)      (cover full existence)
version(n+1) created only in Tᴰₙ (monotonic lineage)
````

#### A.4:4.1 - Open‑Ended Evolution Principle

A holon may repeat the cycle *ad infinitum*:

```
(H₀ in Tᴿ₀) → observe → Δspec in Tᴰ₁ → build → H₁ in Tᴿ₁ → …
```

*Observation itself is a transformation*:
the observing side is a `U.RoleAssignment` whose `holderRef` names the acting `U.System`
and whose `roleRef=TransformerRole@ObservationContext`. That holder executes a
**measurement method** whose *output* is an epistemic holon containing observations.
Thus the traditional “External Observer Pattern” collapses into the universal external
Transformer pattern.

