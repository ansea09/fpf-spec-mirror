---
chunk_kind: "child"
pattern_id: "G.11"
pattern_title: "Telemetry-Driven Refresh & Decay Orchestrator"
section_id: "G.11:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.11/G.11__008_conformance-checklist-normative.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "G.11 — Telemetry-Driven Refresh & Decay Orchestrator"
  - "G.11:7 — Conformance Checklist (normative)"
line_start: 73145
line_end: 73160
dependencies:
  - "B.3.4"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.28"
  - "E.18"
  - "F.15"
  - "G.10"
  - "G.11"
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

| ID                                                    | Requirement                                                                                                                                                                                                                                                                                                                                     | Purpose / Notes                                                                                                            |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G11‑CoreRef**                                    | A conforming `G.11` artefact **MUST** satisfy the **effective** core conformance set implied by the `GCoreLinkageManifest` in `G.11:4.1` (profile expansion + explicit deltas; delegated to `G.Core`).                                                                                                                                       | Phase‑2 bridge clause: `G.11` is conformant only if the relevant `G.Core` invariants and trigger discipline are satisfied. |
| **CC‑G11.1 (Slice-scoped planning).**                 | A conforming `RefreshPlan@Context` **SHALL** be scoped to `PathSliceId[]` (preferred) or `PatternScopeId[]` and **SHALL** record canonical `RSCRTriggerKindId` for each planned cause. Pack-wide reruns **MAY** occur only if the declared dependency closure spans all slices; the closure rationale **SHALL** be recorded.                    | Prevents full-rerun mania while keeping a safety escape hatch explicit and auditable.                                      |
| **CC‑G11.2 (Edition discipline; QD/OEE wiring).**     | When QD and/or OEE are active, a conforming `RefreshPlan@Context` and `RefreshReport@Context` **SHALL** satisfy the required pin/edition/policy wiring of the applicable extension blocks (`G.11:Ext.QDRefreshWiring` and/or `G.11:Ext.OEERefreshWiring`). **`.edition` SHALL apply only on `…Ref`.** Missing required pins **SHALL** block publication. | Keeps replayability strict while moving method‑specific pin lists into `Extensions` (Phase‑2 modularity).                  |
| **CC‑G11.3 (Telemetry‑metric legality).**             | If a refresh publishes Illumination/QD/OEE outcomes, it **SHALL** publish **Q/D/QD‑score** (and any coverage/regret) as **telemetry metrics** and **IlluminationSummary** as a **telemetry summary**; these values **SHALL be excluded from dominance** unless a CAL policy explicitly promotes them, and the promoting **policy‑id SHALL be recorded** in SCR‑visible evidence bindings (via the cited governing patterns).                                                                                                      | Prevents covert scalarisation and keeps “telemetry vs order” separation explicit.                                          |
| **CC‑G11.4 (Bridge penalties).**                      | Any refresh reacting to Bridge/plane changes **SHALL** satisfy `CC‑GCORE‑PEN‑1` (delegation), and **SHALL** publish `CL/CL^k/CL^plane` and the relevant `Φ/Ψ/Φ_plane` policy‑ids with loss notes so penalties route to `R_eff` only (F/G invariant).                                                                                                                                | Keeps penalty routing auditable during refresh.                                                                            |
| **CC‑G11.5 (Selector invariants).**                   | Any orchestrated re‑selection or selected-set/archive update **SHALL** (i) satisfy `CC‑GCORE‑SET‑1` (delegation), and (ii) cite the selector governing definition (`G.5`) under an unchanged admissible `ComparatorSet` (edition‑pinned where applicable), returning **sets** (Pareto/Archive) and introducing **no scalarisation** inside `G.11`.                                                                                                                       | Prevents refresh from changing order semantics.                                                                            |
| **CC‑G11.6 (Crossing visibility).**                   | All refresh actions that touch cross‑context reuse **SHALL** satisfy `CC‑GCORE‑CROSS‑1` (delegation) and the GateCrossing visibility harness (e.g., `E.18`): `CrossingRef` + BridgeCard + UTS + `CL/Φ_plane` policy‑ids. Missing/non‑conformant crossings **SHALL** block publication.                                                                                                                                 | Prevents “silent crossings” under refresh.                                                                                 |
| **CC‑G11.7 (Decay governance).**                      | When refresh is triggered by freshness/decay events, the refresh outputs **SHALL** choose and record a governance outcome (**Refresh / Deprecate / Waive**) with **budget notes** (policy‑bound), and **SHALL** publish the decision via `DeprecationNotice@Context` (and related pins) and SCR‑visible evidence bindings (via `G.6` / cited governing patterns).                                                                                                                                                | Turns epistemic debt into explicit, comparable governance artefacts.                                                       |
| **CC‑G11.8 (No default smuggling).**                  | A conforming `G.11` refresh artefact **SHALL NOT** introduce new defaults for `PortfolioMode`/dominance/Γ‑fold/guard behavior. If orchestrated steps rely on defaults, the artefact **SHALL** cite each default's governing definition (via `G.Core.DefaultGoverningDefinitionIndex` and the applicable governing patterns) rather than restating defaults inside `G.11`.                                                                                                                                            | Protects default definition-citation discipline under orchestration pressure.                                                     |
| **CC‑G11.9 (Targeted RSCR before republication).**    | Before any refresh result is republished downstream (e.g., parity report updates, pack re‑shipping, dashboard slice updates), the execution **SHALL** run or cite a targeted RSCR/regression check for the affected scope and record `RSCRRefs[]` (or equivalent) in `RefreshReport@Context`; exceptions **SHALL** be expressed as `degrade/abstain` outcomes (policy‑bound) rather than silent skips.                                                                                         | Preserves “refresh ≠ vibes” by making regression gating explicit and slice‑scoped.                                         |
| **CC-G11.10 (Causal-use refresh sentinels).**          | When a refreshed surface consumes `C.28`, a conforming `RefreshPlan@Context` **SHALL** include causal-use sentinel payload distinctions when counterfactual realizability, counterfactual-data identification/bounding, target-trial reporting, causal fairness, causal representation validation, off-policy/causal-RL evaluation, or simulation validation can change supported use, unsupported use, support verdict, assurance, parity, or downstream selection. | Keeps moving causal SoTA from silently invalidating shipped support while preserving `G.Core` trigger governance. |

