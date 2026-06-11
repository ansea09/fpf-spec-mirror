---
chunk_kind: "child"
pattern_id: "B.1.1"
pattern_title: "Dependency Graph & Proofs"
section_id: "B.1.1:6"
section_title: "The Proof Kit (ready‑made templates for Γ on D)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.1/B.1.1__007_the-proof-kit-ready-made-templates-for-on-d.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "B.1.1 — Dependency Graph & Proofs"
  - "B.1.1:6 — The Proof Kit (ready‑made templates for Γ on D)"
line_start: 29411
line_end: 29476
dependencies:
  - "A.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.2"
  - "B.1.3"
  - "B.1.4"
  - "B.1.5"
  - "B.1.6"
keywords:
  - "dependency graph"
  - "proofs"
  - "set"
  - "slice"
  - "structural aggregators"
  - "sum"
---

### B.1.1:6 - The Proof Kit (ready‑made templates for Γ on D)

This section provides **small, reusable proof obligations** you attach to a `DependencyGraph D` when invoking any Γ‑flavour. Each obligation is minimal—just enough to guarantee the **Invariant Quintet** for the stated scope and edge set.

#### B.1.1:6.1 - Independence declaration (for COMM/LOC)

> **Obligation IND‑LOC.**
> Provide a **partition of D** into subgraphs `{Dᵢ}` such that:
>
> 1. Their **node sets** are disjoint (no shared holon instances).
> 2. Their **boundaries** are disjoint (no shared ports) or any shared internal stock is **lifted** to the parent boundary in notes.
> 3. No edge in `E` crosses partitions except via explicit `U.Interaction` (not parthood).

**Claim:** Under IND‑LOC, Γ’s fold result is **invariant to local fold order** within and across `{Dᵢ}`.

#### B.1.1:6.2 - Weakest‑link cutset (WLNK)

> **Obligation WLNK‑CUT.**
> Enumerate a **critical set** `C ⊆ V ∪ E` (nodes/edges) such that **failure** (or insufficiency) of any element of `C` makes the aggregation invalid or unsafe in the chosen Γ‑flavour.

**Claim:** For the target property, the result for the whole is bounded by the **minimum** (or tightest cap) across `C`.
Examples:
• Γ\_sys → tensile strength cutset along a load path;
• Γ\_epist → weakest supported premise in a proof spine;
• Γ\_work → availability caps for required inputs across the boundary.

#### B.1.1:6.3 - Monotone coordinates (MONO)

> **Obligation MONO‑AX.**
> Declare the **monotone characteristics** (attributes whose improvement cannot worsen the whole) **for this call**. Specify *how* “improvement” is recognized.

**Claim:** If only monotone characteristics change in the direction of improvement while all else is fixed, the aggregate’s target value cannot degrade.

Examples:
• Γ\_sys → increased component reliability, tighter tolerance;
• Γ\_epist → higher evidence-support class, higher formality;
• Γ\_method → reduced step duration, higher step-assurance class;
• Γ\_time → added non‑overlapping coverage;
• Γ\_work → higher yield η, reduced dissipation.

#### B.1.1:6.4 - Idempotence witness (IDEM)

> **Obligation IDEM‑WIT.**
> Provide the **singleton** case: a subgraph `D₁` with one node and no admissible composition edges.

**Claim:** Γ(D₁) returns that node’s property unchanged.

#### B.1.1:6.5 - Scope & boundary attestations

> **Obligation SCOPE‑1.**
> Affirm `DesignRunTag(D) ∈ {design, run}` and that all nodes share it.
> **Obligation BOUND‑1.**
> List the **U.Boundary** for each top‑level holon in `V` and record any **U.Interaction** edges that are relevant but not part of `E` (to show cross‑boundary influences were not mis‑typed as parthood).

#### B.1.1:6.6 - Flavour‑specific summary table

| Γ‑flavour            | Independence (IND‑LOC)                                             | WLNK‑CUT (what is “critical”)                         | MONO‑AX (what cannot make worse)                    | IDEM‑WIT                      | Notes                                                         |
| -------------------- | ------------------------------------------------------------------ | ----------------------------------------------------- | --------------------------------------------------- | ----------------------------- | ------------------------------------------------------------- |
| **Γ\_sys**          | Disjoint subassemblies with disjoint interfaces (BIC respected)    | Structural cutset on load/flow paths                  | ↑ component reliability/capacity; tighter bounds    | Single module                 | Use **BIC** to keep interfaces explicit.                      |
| **Γ\_epist**         | Independent argument subgraphs; no premise reuse across partitions | Weakest premise/claim on entailment spine             | ↑ formality; ↑ reliability of sources; ↑ congruence | Single section/lemma          | Apply `Φ(CL_min)` penalty only where mappings/links are weak. |
| **Γ\_ctx and Γ\_method** | Parallel branches truly independent (no hidden state)              | Slowest/least reliable step on the critical path      | ↓ duration; ↑ step assurance; ↑ join soundness      | Single step                   | COMM relaxed to partial orders (NC‑1..3).                     |
| **Γ\_time**          | Non‑overlapping time slices; same carrier identity                 | Missing slice creates a gap (temporal WLNK)           | ↑ coverage; ↑ timestamp precision                   | Single slice                  | Phases must cover the window without overlap.                 |
| **Γ\_work**          | Disjoint boundary partitions; shared stocks lifted to parent       | Availability caps for required inputs across boundary | ↑ yield; ↓ dissipation; ↑ availability              | Single resource with no delta | Keep **Boundary Ledger** with basis and time window.          |

Attach the row(s) you use as the **Proof Kit** to the Γ call record.

