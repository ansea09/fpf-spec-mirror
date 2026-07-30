---
chunk_kind: "child"
pattern_id: "G.9"
pattern_title: "Parity and Benchmark Harness"
section_id: "G.9:6"
section_title: "Conformance Checklist (CC‑G9)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.9/G.9__010_conformance-checklist-cc-g9.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "G.9 — Parity and Benchmark Harness"
  - "G.9:6 — Conformance Checklist (CC‑G9)"
line_start: 100486
line_end: 100543
dependencies:
  - "A.19"
  - "A.21"
  - "C.18"
  - "C.19"
  - "C.21"
  - "C.22.1"
  - "C.23"
  - "C.27"
  - "C.28"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.5.2"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "adaptation parity"
  - "benchmark plan"
  - "comparator pins"
  - "freshness windows"
  - "parity harness"
  - "selected-set outcomes"
---

### G.9:6 — Conformance Checklist (CC‑G9)

**CC‑G9‑CoreRef (normative; mandatory).**
G.9 conforms only if it satisfies the **effective** set of `CC‑GCORE‑*` declared in **G.9:4.0 GCoreLinkageManifest** (including trigger typing, Default Governing Definition Index links, and P2W split).

1. **CC‑G9.1 — Equal windows (and budgets) & pinned spec editions (local).**
   A ParityPlan **SHALL** declare a single `FreshnessWindows` shared across baselines. If `Budgeting` is used/pinned, it **SHALL** be shared across baselines as well. `ParityPinSet` **SHALL** include the edition pins required by the referenced governing spec and comparator refs (at minimum `CNSpecRef.edition`, `CGSpecRef.edition`, `ComparatorSpecRef.edition`).
   If the parity run depends on planned slot fillings (WorkPlanning baseline), the plan **SHALL** cite the relevant `SlotFillingsPlanItem` refs via `PlanItemRefs[]` (nil‑elision when not applicable).

2. **CC‑G9.2 — Mode‑specific definition pins are declared via Extensions (local; conditional).**
   When parity depends on mode‑specific definition records beyond the pinned governing spec refs (e.g., DHC/QD/OEE), the ParityPlan/Report **SHALL** include the corresponding `GPatternExtension` blocks and satisfy their `RequiredPins/EditionPins/PolicyPins` (typically carried inside `ParityPinSet`, and echoed via pins deltas in audit):
   * DHC parity → `G.9:Ext.DHCParityPins`
   * QD archive parity → `G.9:Ext.QDArchiveParity`
   * OEE parity → `G.9:Ext.OEEParity`

3. **CC‑G9.3 — CSLC-admissible orders and arithmetic (delegation point + local constraint).**
   Delegated to `CC‑GCORE‑SET‑1` (and the relevant G.5 `PortfolioMode` / selected-set semantics). Additionally: any numeric comparison or aggregation invoked by parity **SHALL** be CSLC-admissible and cite the corresponding CG‑Spec entry; non-admissible operations (e.g., ordinal means / mixed‑scale weighted sums) **SHALL** be refused or abstained with path‑cited trace (citation only; arithmetic admissibility comes from `CG‑Spec`/`MM‑CHR`).

4. **CC‑G9.4 — Normalization discipline (local citation only).**
   If Characteristics differ by unit, scale, or space, the ParityPlan **SHALL** cite the CSLC-admissible comparability mapping by id (`UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`) and compare only after that mapping is applied (“normalize, then compare”).
   If such mapping ids are used, the ParityReport **SHALL** echo the same ids (directly or via explicit pins deltas) so the run is reproducible/auditable without out‑of‑band context.
   The harness **SHALL NOT** define a local mapping.

5. **CC‑G9.5 — Dominance/PortfolioMode interpretation & telemetry separation (local).**
   ParityPlan/ParityReport **SHALL** either (i) explicitly pin the applicable regime/mode via refs/policy‑ids, or (ii) cite the corresponding defaults for `DefaultId.DominanceRegime` and `DefaultId.PortfolioMode` via `G.Core.DefaultGoverningDefinitionIndex`. Any non‑default “promotion” behaviour must be policy‑bound and recorded via policy‑id pins.
   IlluminationSummary/coverage/regret **SHALL** be treated as telemetry (report‑only by default); any promotion into dominance is an explicitly pinned CAL policy and MUST be recorded in audit pins/SCR.

5a. **CC‑G9.5a — Adaptation parity disclosure (local; conditional).**
   When the parity claim concerns bounded specialization, the ParityPlan and ParityReport **SHALL** pin the declared task family or target scope cut, the work-measure threshold target, adaptation budget, prior exposure declaration, and any transfer, retention, downstream exploitation efficiency, downside field, or corridor-entry baseline/evidence note that materially affects comparison.

6. **CC‑G9.6 — Epsilon‑front thinning (local; conditional).**
   If ε‑front thinning is used, `EpsilonDominance (ε≥0)` **SHALL** be explicit in the plan/report and pinned (param/id) such that the same ε is reproducible.

7. **CC‑G9.7 — Crossing visibility (delegation point).**
   Delegated to `CC‑GCORE‑CROSS‑1` and `CC‑GCORE‑PEN‑1`. This item remains as a stable delegation point for Bridge and reference-plane crossing visibility plus R-channel penalty placement discipline.

8. **CC‑G9.8 — Evidence trace completeness (local).**
   A ParityReport **SHALL** include an EvidenceTrace with `EvidenceGraphId` and the relevant `PathId[]` (and `PathSliceId?` when needed), covering both inclusions and refusals/abstains/degrades.

9. **CC‑G9.9 — Telemetry hooks are emitted with pins (local).**
   When parity emits telemetry for refresh, emitted telemetry **SHALL** carry the active edition pins and policy‑ids needed to re‑run parity (including the active subset of `ParityPinSet` relevant to the emitted event).
   In particular, telemetry items SHOULD cite `PathSliceId` when available, and **SHALL** include the policy id governing the telemetry interpretation.
   Mode‑specific definition pins **SHALL** be included as declared by the active `Extensions` blocks (e.g., `G.9:Ext.QDArchiveParity`, `G.9:Ext.OEEParity`, including `EnvironmentValidityRegionId` when OEE parity is in scope).

10. **CC‑G9.10 — RSCR parity tests are published (local).**
   Parity publication **SHALL** include RSCR parity tests (via `F.15` harness refs) that cover negative/refusal paths relevant to this plan (missing pins, edition drift, missing bridge calibration refs, etc.).

11. **CC‑G9.11 — GateCrossing visibility (delegation point).**
    Delegated to `CC‑GCORE‑CROSS‑1` and the applicable GateCrossing/CrossingBundle harness checks (`E.18`, `A.21`, `F.9`, and relevant Part G bridge or crossing wiring). This remains a stable delegation point.

12. **CC‑G9.12 — Tech‑register lexical discipline (local).**
    Tech prose and heads **SHALL** follow E.10: do not introduce drift‑prone primitives (e.g., “metric” as a Tech primitive); reference the source pattern's canonical terms and pinned refs.

13. **CC‑G9.13 — MOO disclosure for parity (local).**
    `Run_Parity` / `Publish_ParityReport` **SHALL** record the ParityHarness identity (UTS ids) and the active pins required to interpret the outcome (editions + policy‑ids), so parity remains auditable without relying on “decision logs”.

14. **CC-G9-CLP-1 - Causal method rung parity.** If a parity report compares causal methods, it SHALL first run `CausalRungParityScreen`; when full parity remains plausible, it SHALL declare target causality-ladder rung, causal-use claim kind, `estimandRef`, interventional-action basis, causal evidence support basis, transportability basis for the source population and target population when needed, estimation-validity basis when needed, bridge and loss relation where rungs differ, `causalUseSupportRecordRef` and `causalUseSupportVerdict` when relevant `C.28` support is consumed, and degraded parity or abstain result where parity cannot be established.

