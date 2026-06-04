---
chunk_kind: "child"
pattern_id: "A.4"
pattern_title: "Temporal Duality & Open‑Ended Evolution Principle"
section_id: "A.4:4"
section_title: "Solution - Temporal Duality Model"
source_path: "FPF-Spec.md"
output_path: "by_section/A.4/A.4__005_solution-temporal-duality-model.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "A.4 — Temporal Duality & Open‑Ended Evolution Principle"
  - "A.4:4 — Solution - Temporal Duality Model"
line_start: 6557
line_end: 6588
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
An **External Transformer** (`U.System` playing `transformerRole ⊑ TransformerRole`)
executes a **measurement method** whose *output* is an epistemic holon
containing observations.  Thus the traditional “External Observer Pattern” collapses into
the universal external Transformer pattern.

