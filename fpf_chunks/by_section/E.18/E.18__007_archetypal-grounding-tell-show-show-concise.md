---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:6"
section_title: "Archetypal Grounding (Tell–Show–Show; concise)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__007_archetypal-grounding-tell-show-show-concise.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:6 — Archetypal Grounding (Tell–Show–Show; concise)"
line_start: 67264
line_end: 67279
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "P2W support"
  - "composition"
  - "crossings"
  - "flow valuation"
  - "guards"
  - "selected transformations"
  - "transformation flow structure"
---

### E.18:6 - Archetypal Grounding (Tell–Show–Show; concise)

*Tell (P2W reference path).* A first-principles-to-work path is one path through the selected transformation-flow structure, not the whole structure itself: `U.Signature(profile=FormalSubstrate)` declaration, principle frame, mechanism, normalization, selection, planning, work enactment, and refresh are represented as loci linked by one `U.Transfer` relation kind, with crossings pinned where context, plane, edition, or design/run state changes.

*Show-A (Supply chain).* Loci: procurement -> inbound QC (UNM) -> selection (supplier set; declared order) <-> planning (lotting/schedule; budget) -> execution (receipts; **WorkEnactment enacts world-contact**) -> refresh (quality telemetry; affected faces re-emitted). Crossings: vendor Context via **Bridge/CL**; penalties appear **in R only**; comparators pinned to CG-Spec edition.

*Show-B (Neural-net functional).* Loci: `U.Signature(profile=FormalSubstrate)` declaration (typed tensor-operation declaration) -> mechanism (combinator algebra) -> UNM (dataset normalization; **TransportRegistry^Phi**) -> selection (architecture/hyperparam set; Pareto set over accuracy@ratio and FLOPs@ratio) <-> planning (compute budget horizon) -> Work (training runs; Delta recorded) -> refresh (parity inserts; slice-scoped). Faces pin **DescriptorMapRef.edition** and **DistanceDefRef.edition** when QD telemetry values are shown; illumination remains **report-only telemetry** by default.

*Show-C (Developed product, then application).* One flow valuation represents development work that produces a specification, pattern, process description, mechanism description, method set, or tool through drafting, checks, projection, build, or publication. A later flow valuation represents use of that product in project work or analysis. A further flow valuation may represent another use of the result: a tool is made, then used to make a chair, then the chair supports a person writing a text. The selected structure can relate all these valuations through transfers and feedback, while each flow keeps its own governed object, `DesignRunTag`, flow-local relation position for the carried object, work occurrence, evidence, and reopened slice.

*Show-D (FPF pattern development and use).* A development-flow valuation represents pattern development work: creation, evaluation, projection, publication, and later repair of a pattern. A use-flow valuation represents application of that pattern to its own `EntityOfConcern`. An evaluation or use-found defect can select the smallest development slice for repair. E.18 keeps the common selected structure visible while separating the developed pattern, the use of the pattern, the evidence found during use, and the edition or slice that is reopened.

**Cross-pattern boundary slice (QD archive).** A QD selector returns an archive. Under `E.18`, this is one `PathSlice` in one `TransformationFlowStructure`; selection returns a set/archive, not a hidden scalar. Under `A.20`, the archive insertion or update step has a current CV class, `CV.Status`, and witness or refusal; no acceptance is inferred. Under `A.21`, a comparability gate or `LaunchGate` can publish a `GateDecision` only when that gate relation is current and consumes the relevant CV result. Under `E.20`, if a new selector mechanism-governing definition is introduced, the mechanism-governing definition is the locus for the meaning while suites and wiring only cite or bind it. These are four governed loci, not one prescribed work order.

> *Post-2015 SoTA echoes (illustrative):* **TAMP and MPC**, **MAP-Elites / QD (incl. CMA-ME)**, **refinement-typed stacks**, **profunctor optics**. Worked examples and Tell-Show-Show vignettes for P2W, comparator/archive, coupled development/application flows, and refresh specializations stay outside this selected-structure core unless a current pattern explicitly selects them.

