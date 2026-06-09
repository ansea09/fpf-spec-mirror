---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transduction Graph Architecture (E.TGA)"
section_id: "E.18:6"
section_title: "Archetypal Grounding (Tell–Show–Show; concise)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__007_archetypal-grounding-tell-show-show-concise.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "E.18 — Transduction Graph Architecture (E.TGA)"
  - "E.18:6 — Archetypal Grounding (Tell–Show–Show; concise)"
line_start: 66500
line_end: 66515
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.7"
  - "E.10"
  - "E.17"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "CSLC normalize-then-compare"
  - "CV⇒GF (ConstraintValidity → GateFit)"
  - "DesignRunTag"
  - "MVPK faces"
  - "OperationalGate(profile)"
  - "PathSlice/Sentinel refresh"
  - "Set-return selection"
  - "SquareLaw"
  - "UNM declaration locus"
  - "edge=U.Transfer (single-edge kind)"
  - "nodes=morphisms"
  - "transduction graph"
---

### E.18:6 - Archetypal Grounding (Tell–Show–Show; concise)

*Tell (P2W reference path).* A first-principles-to-work path is one path through the graph, not the graph itself: `U.Signature(profile=FormalSubstrate)` declaration, principle frame, mechanism, normalization, selection, planning, work enactment, and refresh become nodes linked by one `U.Transfer` edge kind, with crossings pinned where context, plane, edition, or design/run state changes.

*Show-A (Supply chain).* Nodes: procurement -> inbound QC (UNM) -> selection (supplier set; declared order) <-> planning (lotting/schedule; budget) -> execution (receipts; **WorkEnactment enacts (world-contact)**) -> refresh (quality telemetry; re-emit faces). Crossings: vendor Context via **Bridge/CL**; penalties appear **in R only**; comparators pinned to CG-Spec edition.

*Show-B (Neural-net functional).* Nodes: `U.Signature(profile=FormalSubstrate)` declaration (typed tensor-operation declaration) -> mechanism (combinator algebra) -> UNM (dataset normalization; **TransportRegistry^Phi**) -> selection (architecture/hyperparam set; Pareto set over accuracy@ratio and FLOPs@ratio) <-> planning (compute budget horizon) -> Work (training runs; Delta recorded) -> refresh (parity inserts; slice-scoped). Faces pin **DescriptorMapRef.edition** and **DistanceDefRef.edition** when QD telemetry values are shown; illumination remains **report-only telemetry** by default.

*Show-C (Developed product, then application).* One flow develops a specification, pattern, process description, mechanism description, method set, or tool through drafting, checks, projection, build, or publication. A later flow uses that product in project work or analysis. A further flow may use the result again: a tool is made, then used to make a chair, then the chair supports a person writing a text. The graph can join all these flows through transfers and feedback, while each flow keeps its own governed object, `DesignRunTag`, flow-local relation position for the carried object, work occurrence, evidence, and reopened slice.

*Show-D (FPF pattern development and use).* The development flow creates, evaluates, projects, publishes, and later repairs a pattern. The use flow applies that pattern to its own `EntityOfConcern`. An evaluation or use-found defect can return to the smallest development slice for repair. E.TGA keeps the common graph visible while separating the developed pattern, the use of the pattern, the evidence found during use, and the edition or slice that is reopened.

**Cross-pattern boundary slice (QD archive).** A QD selector emits an archive. `E.18` says: this is one `PathSlice` in one `TransductionGraph`; selection returns a set/archive, not a hidden scalar. `A.20` says: the archive insertion or update step has a live CV class, `CV.Status`, and witness or refusal; no acceptance is inferred. `A.21` says: a comparability gate or `LaunchGate` can publish a `GateDecision` only when that gate relation is live and consumes the relevant CV result. `E.20` says: if a new selector mechanism-governing definition is introduced, the mechanism-governing definition is the locus for the meaning while suites and wiring only cite or bind it. These are four governed loci, not one prescribed work order.

> *Post-2015 SoTA echoes (illustrative):* **TAMP and MPC**, **MAP-Elites / QD (incl. CMA-ME)**, **refinement-typed stacks**, **profunctor optics**. Worked examples and Tell-Show-Show vignettes for P2W, comparator/archive, coupled development/application flows, and refresh specializations stay outside this graph-architecture core unless a current pattern explicitly selects them.

