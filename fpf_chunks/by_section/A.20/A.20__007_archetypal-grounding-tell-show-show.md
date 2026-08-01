---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Flow Constraint Validity — Eulerian"
section_id: "A.20:5"
section_title: "Archetypal Grounding (Tell–Show–Show)  ✱"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__007_archetypal-grounding-tell-show-show.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "A.20 — Flow Constraint Validity — Eulerian"
  - "A.20:5 — Archetypal Grounding (Tell–Show–Show)  ✱"
line_start: 33641
line_end: 33657
dependencies:
  - "A.19.SelectorMechanism"
  - "A.21"
  - "C.18"
  - "C.19"
  - "E.17"
  - "E.18"
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
  - "TransformationFlowStructure"
  - "flow"
---

### A.20:5 - Archetypal Grounding (Tell–Show–Show)  ✱

**Tell (internal step, not gate passage).**
CV answers whether a transformation step satisfies its own declared constraints: units, laws, admissibility conditions, stability bounds, type, domain, and range, and, for `StructuralReinterpretation`, reinterpretation equivalence. If `CV.Status != pass`, GateFit does not get to rescue the step; if `CV.Status=pass`, ranking, acceptance, launch, and `GateProfile` fit still belong outside CV.

**Show‑0 (`CV.Status=pass`, no gate relation).**
A normalization step has declared units, domain and range, and invariant refs; the CV check returns `CV.Status=pass` with a `CV.WitnessRef`. No comparison, launch, crossing, freshness, or `GateProfile`-fit claim is present, so no `GateDecision`, GateFit narrative, or `DecisionLog` is created. The only A.20 result is: this step is internally valid under its declared constraints.

**Show‑1 (compiler build → run).**

A typed module `M` exposes `f : State_d → BuildOutput_d` under a declared `LawSet` (e.g., determinism under fixed toolchain) and `TypeDomainRange`. **CV** checks: (i) `MechanismUnitsCoherence` (toolchain and flags units coherent), (ii) `LawSetInvariants` (reproducible outputs under same `E⃗`), (iii) `Admissibility` (inputs well-typed), and (iv) optional Lipschitz or stability surrogate (bounded perturbation in sandbox). `CtxState` is preserved along raw transfers. Entering `U.Work(run)` uses `LaunchGate` with `FreshnessUpToDate` and `DesignRunTagConsistency` - **GateFit**, not CV.

**Show‑2 (selection archive in QD and AutoML).**
A mechanism emits a **set** (`Front`, `Archive`, or another declared set publication). **CV** checks only: valid descriptor ranges, declared continuity bounds over named metric spaces, and archive invariants (idempotent insert). No ranking or acceptance thresholds are introduced at CV; comparators and acceptance policies bind at gates via `A.21` plus the current comparator and set-publication loci (`A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, or `G.11`) when those claims are present. Edition-aware pins on faces carry `DescriptorMapRef.edition` only with `Bridge+UTS`.

**Practice references.** Algebraic effects and handlers separate signatures from handlers (Koka and Effekt, 2015+); reproducible pipelines isolate mechanism constraints from release or deployment criteria (Bazel and Nix); optics, profunctors, and open hypergraph categories motivate composition on open graphs without adding facts on faces; QD, MAP-Elites, CMA-ME, and DQD motivate **set-return and declared order relations** (2015-2022).

