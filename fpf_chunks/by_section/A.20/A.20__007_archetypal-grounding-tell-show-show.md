---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "U.Flow.ConstraintValidity — Eulerian"
section_id: "A.20:5"
section_title: "Archetypal Grounding (Tell–Show–Show)  ✱"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__007_archetypal-grounding-tell-show-show.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "A.20 — U.Flow.ConstraintValidity — Eulerian"
  - "A.20:5 — Archetypal Grounding (Tell–Show–Show)  ✱"
line_start: 27494
line_end: 27510
dependencies:
  - "A.19.SelectorMechanism"
  - "A.21"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
  - "E.TGA"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
keywords:
  - "ConstraintValidity"
  - "Eulerian"
  - "GateFit"
  - "MVPK"
  - "PathSlice"
  - "Sentinel"
  - "SquareLaw"
  - "TransductionFlow"
  - "flow"
---

### A.20:5 - Archetypal Grounding (Tell–Show–Show)  ✱

**Tell (internal step, not gate passage).**
CV answers whether a transformation step satisfies its own declared constraints: units, laws, admissibility conditions, stability bounds, type/domain/range, and, for `StructuralReinterpretation`, reinterpretation equivalence. If `CV.Status != pass`, GateFit does not get to rescue the step; if `CV.Status=pass`, ranking, acceptance, launch, and profile-fit still belong outside CV.

**Show‑0 (`CV.Status=pass`, no gate opened).**
A normalization step has declared units, domain/range, and invariant refs; the CV check returns `CV.Status=pass` with a `CV.WitnessRef`. No comparison, launch, crossing, freshness, or profile-fit claim is live, so no `GateDecision`, GateFit narrative, or `DecisionLog` is opened. The admissible result is only: this step is internally valid under its declared constraints.

**Show‑1 (compiler build → run).**

A typed module `M` exposes `f : State_d → BuildOutput_d` under a declared `LawSet` (e.g., determinism under fixed toolchain) and `TypeDomainRange`. **CV** checks: (i) `MechanismUnitsCoherence` (toolchain/flags units coherent), (ii) `LawSetInvariants` (reproducible outputs under same `E⃗`), (iii) `Admissibility` (inputs well-typed), and (iv) optional Lipschitz/stability surrogate (bounded perturbation in sandbox). `CtxState` is preserved along raw transfers. Entering `U.Work(run)` uses `LaunchGate` with `FreshnessUpToDate` and `DesignRunTagConsistency` - **GateFit**, not CV.

**Show‑2 (selection archive in QD/AutoML).**
A mechanism emits a **set** (`Front`, `Archive`, or another declared set publication). **CV** checks only: valid descriptor ranges, declared continuity bounds over named metric spaces, and archive invariants (idempotent insert). No ranking or acceptance thresholds are introduced at CV; comparators and acceptance policies bind at gates via `A.21` plus the current comparator and set-publication loci (`A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, or `G.11`) where live. Edition-aware pins on faces carry `DescriptorMapRef.edition` only with `Bridge+UTS`.

**Practice references.** Algebraic effects & handlers separate signatures from handlers (Koka/Effekt, 2015+); reproducible pipelines isolate mechanism constraints from deployment **profiles** (Bazel/Nix); optics/profunctors and open/hypergraph categories motivate composition on open graphs without adding facts on faces; QD/MAP-Elites/CMA-ME/DQD motivate **set-return and declared order relations** (2015-2022).

