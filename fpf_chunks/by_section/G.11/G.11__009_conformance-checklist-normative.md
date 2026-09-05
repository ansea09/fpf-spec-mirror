---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh and Decay Orchestrator"
section_id: "G.11:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__009_conformance-checklist-normative.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "G.11 — Telemetry-Driven Refresh and Decay Orchestrator"
  - "G.11:7 — Conformance Checklist (normative)"
line_start: 106767
line_end: 106783
dependencies:
  - "A.6.RCD"
  - "B.3.4"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.28"
  - "C.32.P2S"
  - "E.18"
  - "F.15"
  - "G.10"
  - "G.12"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
  - "G.Core.TriggerAliasMap.G11"
keywords:
  - "Bridge Sentinels"
  - "PathSlice"
  - "RSCR"
  - "decay"
  - "deprecation"
  - "edition bumps"
  - "edition-aware"
  - "epistemic debt"
  - "re-shipping"
  - "refresh"
  - "telemetry"
---

### G.11:7 - Conformance Checklist (normative)

| ID                                                    | Requirement                                                                                                                                                                                                                                                                                                                                     | Purpose and Notes                                                                                                            |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G11‑CoreRef**                                    | A conforming `G.11` artefact **MUST** satisfy the **effective** core conformance set implied by the `GCoreLinkageManifest` in `G.11:4.1` (profile expansion plus explicit deltas; delegated to `G.Core`).                                                                                                                                       | `G.11` is conformant only if the relevant `G.Core` invariants and trigger discipline are satisfied. |
| **CC‑G11.1 (Slice-scoped planning).**                 | A conforming `RefreshPlan@Context` **SHALL** be scoped to `PathSliceId[]` (preferred) or `PatternScopeId[]` and **SHALL** record canonical `RSCRTriggerKindId` for each planned cause. Pack-wide reruns **MAY** occur only if the declared dependency closure spans all slices; the closure rationale **SHALL** be recorded.                    | Prevents full-rerun mania while keeping a safety escape hatch explicit and auditable.                                      |
| **CC‑G11.2 (Edition discipline; QD and OEE wiring).**     | When QD, OEE, or both are active, a conforming `RefreshPlan@Context` and `RefreshReport@Context` **SHALL** satisfy the required pin, edition, and policy wiring of the applicable extension blocks: `G.11:Ext.QDRefreshWiring`, `G.11:Ext.OEERefreshWiring`, or both. **`.edition` SHALL apply only on `…Ref`.** Missing required pins **SHALL** block publication. | Keeps replayability strict while keeping method-specific pin lists inside the applicable extension blocks.                  |
| **CC‑G11.3 (Telemetry-metric admissibility).**             | If a refresh publishes Illumination, QD, or OEE outcomes, it **SHALL** publish **Q, D, and QD‑score** and any coverage or regret as **telemetry metrics** and **IlluminationSummary** as a **telemetry summary**; these values **SHALL be excluded from dominance** unless a CAL policy explicitly promotes them, and the promoting **policy id SHALL be recorded** in SCR-visible evidence bindings through the cited subject patterns.                                                                                                      | Prevents covert scalarisation and keeps “telemetry vs order” separation explicit.                                          |
| **CC‑G11.4 (Bridge penalties).**                      | Any refresh reacting to Bridge or plane changes **SHALL** satisfy `CC‑GCORE‑PEN‑1` (delegation), and **SHALL** publish `CL`, `CL^k`, `CL^plane`, and the relevant `Φ`, `Ψ`, and `Φ_plane` policy ids with loss notes so penalties are assigned to `R_eff` only (F and G invariant).                                                                                                                                | Keeps penalty assignment auditable during refresh.                                                                            |
| **CC‑G11.5 (Selector invariants).**                   | Any orchestrated re‑selection or selected-set or archive update **SHALL** (i) satisfy `CC‑GCORE‑SET‑1` (delegation), and (ii) cite the selector governing definition (`G.5`) under an unchanged admissible `ComparatorSet` (edition‑pinned where applicable), returning **sets** (`Pareto` or `Archive`) and introducing **no scalarisation** inside `G.11`.                                                                                                                       | Prevents refresh from changing order semantics.                                                                            |
| **CC‑G11.6 (Crossing visibility).**                   | All refresh actions that touch cross-context reuse **SHALL** satisfy `CC‑GCORE‑CROSS‑1` (delegation) and the GateCrossing visibility harness (e.g., `E.18`): `CrossingRef`, BridgeCard, UTS, and `CL` or `Φ_plane` policy ids. Missing or non-conformant crossings **SHALL** block publication.                                                                                                                                 | Prevents “silent crossings” under refresh.                                                                                 |
| **CC‑G11.7 (Decay governance).**                      | When refresh is triggered by freshness or decay events, the refresh outputs **SHALL** choose and record a governance outcome (**Refresh**, **Deprecate**, or **Waive**) with **budget notes** (policy-bound), and **SHALL** publish the decision through `DeprecationNotice@Context` and related pins plus SCR-visible evidence bindings through `G.6` or cited subject patterns.                                                                                                                                                | Turns epistemic debt into explicit, comparable governance artefacts.                                                       |
| **CC‑G11.8 (No default smuggling).**                  | A conforming `G.11` refresh artefact **SHALL NOT** introduce new defaults for `PortfolioMode`, dominance, Γ-fold, or guard behavior. If orchestrated steps rely on defaults, the artefact **SHALL** cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex` and the applicable subject patterns rather than restating defaults inside `G.11`.                                                                                                                                            | Protects default definition-citation discipline under orchestration pressure.                                                     |
| **CC‑G11.9 (Targeted RSCR before republication).**    | Before any refresh result is republished downstream (e.g., parity report updates, pack re-shipping, dashboard slice updates), the execution **SHALL** run or cite a targeted RSCR or regression check for the affected scope and record `RSCRRefs[]` or equivalent refs in `RefreshReport@Context`; exceptions **SHALL** be expressed as `degrade` or `abstain` outcomes (policy-bound) rather than silent skips.                                                                                         | Preserves “refresh ≠ vibes” by making regression gating explicit and slice-scoped.                                         |
| **CC-G11.10 (Causal-use refresh sentinels).**          | When a refreshed publication or output consumes `C.28`, a conforming `RefreshPlan@Context` **SHALL** include causal-use sentinel payload distinctions when counterfactual realizability, counterfactual-data identification and bounding, target-trial reporting, causal fairness, causal representation validation, off-policy and causal-RL evaluation, or simulation validation can change supported use, unsupported use, support verdict, assurance, parity, or downstream selection. | Keeps moving causal SoTA from silently invalidating shipped causal-use results while preserving `G.Core` trigger governance. |
| **CC-G11.11 (Relation-derivation dependency refresh).** | When a reused `A.6.RCD` predicate definition or admitted derived relation kind depends on base definitions, a named substrate edition, an authorized derivation operation, or an applicability scope, the refresh plan **SHALL** pin those dependencies and reopen the affected derivation and dependent uses when one changes. The plan uses existing canonical trigger kinds; it does not mint a relation-specific trigger kind. | Prevents a once-valid derivation from surviving a changed semantic or substrate basis. |

