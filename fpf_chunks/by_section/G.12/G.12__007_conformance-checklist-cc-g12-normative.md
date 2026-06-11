---
chunk_kind: "child"
pattern_id: "G.12"
pattern_title: "DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
section_id: "G.12:6"
section_title: "Conformance checklist (CC‑G12, normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.12/G.12__007_conformance-checklist-cc-g12-normative.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "G.12 — DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)"
  - "G.12:6 — Conformance checklist (CC‑G12, normative)"
line_start: 83017
line_end: 83030
dependencies:
  - "A.19"
  - "C.18"
  - "C.19"
  - "C.21"
  - "E.10"
  - "E.5.2"
  - "F.17"
  - "F.18"
  - "G.0"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.Core"
keywords:
  - "DHC"
  - "PathId/PathSliceId"
  - "RSCR/refresh wiring"
  - "UTS twins"
  - "admissible telemetry"
  - "dashboard"
  - "discipline health"
  - "edition pins"
  - "time-series"
  - "view-only slices"
---

### G.12:6 — Conformance checklist (CC‑G12, normative)

| CC ID   | Requirement  | Verification notes  |
| ------- | ------------ | ------------------- |
| **CC‑G12‑CoreRef** | The pattern satisfies the **effective** `G.Core` obligations declared by `GCoreLinkageManifest (G.12)` (profiles/sets/deltas expanded per `G.Core:4.2`).    | Evidence: the manifest is present; required pins/defaults/triggers are accounted for; no local restatement overrides core governing definitions.  |
| **CC‑G12.1** | **DHC slot typing (C.21‑grounded).** Every published dashboard value is indexed by a **C.21‑authored** `DHCSlotId` (typed DHC slot: `CharacteristicId` + scale/unit/polarity + reference plane binding + lane discipline) and is scoped by an explicit `TargetSlice` + `Γ_time`. | Evidence: row/series references `DHCSlotId` and pins `ReferencePlane` and `Γ_time` (or a series `WindowSpec` that yields row Γ_time). |
| **CC‑G12.2** | **Edition discipline (no drift).** Every published time‑series value carries `DHCMethodRef.edition` and any other definition‑pins actually used to obtain it (e.g., `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `UNM_id`, `NormalizationMethodInstanceId[]`, `ComparatorSetRef.edition?`). No free‑text versioning. | Check that `.edition` appears only on `…Ref`; check presence of all definition pins used by the pipeline; extension pins appear only when their extension blocks are present. |
| **CC‑G12.3** | **Spec citation for numeric operations (no shadow specs; no illicit arithmetic).** Any numeric operation in the dashboard pipeline is legal only under explicit **CG‑Spec** and **CN‑Spec** pins (e.g., `SCPRef.edition`, `MinimalEvidenceRef.edition`, `ΓFoldRef.edition?` when used), and any normalization is explicit (`UNM_id` + `NormalizationMethodInstanceId[]` etc). Ordinal/categorical slots remain **compare‑only** (no illicit arithmetic). | Check that operations cite pinned governing definitions; reject “normalize, then compare” without explicit UNM pins; reject arithmetic over ordinal slots unless the governing definition declares an admissible mapping. |
| **CC‑G12.4** | **Set‑returning selection is preserved.** If the dashboard consumes selection / set-result outputs, it MUST preserve set‑return semantics and MUST publish the resolved `DominanceRegime` and `PortfolioMode` by citing each default's governing definition (via `G.Core.DefaultGoverningDefinitionIndex`) rather than inventing local defaults. Any promotion of illumination/telemetry into dominance MUST cite the governing-pattern policy (typically CAL) and be auditable via evidence paths. | Check for set-result outputs; check that any scalar headline is view‑only; check citations to default governing definitions/policies. |
| **CC‑G12.5** | **UTS publication discipline.** `DHCSeries@Context` and its rows (and any published slices) are published as UTS publication units with Tech and Plain twins plus stable identifiers; deprecations and edition bumps follow the canonical UTS discipline. | Check stable ids and twin labels; check that publication does not smuggle `GateDecision` values as authoritative UTS publication content. |
| **CC‑G12.6** | **Bridge/plane routing is explicit when used.** If a series crosses contexts or planes, the rows MUST cite the Bridge/PlaneMap routing (`BridgeId[]`, `CL/CL^k/CL^plane`, `Φ/Ψ/Φ_plane policy‑ids`, `PlaneMapRef.edition?`) and respect penalty routing to `R_eff` only (semantics pinned through `G.Core`). | Check presence of crossing pins when contexts or planes differ; check that any loss is expressed via R‑lane impact only. |
| **CC‑G12.7** | **Telemetry sufficiency for slice‑scoped RSCR.** Emitted dashboard telemetry pins MUST (i) use canonical `RSCRTriggerKindId`, (ii) include `scope` (PathSliceId[] or PatternScopeId) and the touched `…Ref.edition`/policy/window pins, and (iii) block publication when required pins are missing. Each published row is evidence‑citable by `PathSliceId[]` under explicit `Γ_time`. | Check: no free‑text causes; payload includes path/window/editions/policies; missing pins block publish; row has PathSliceId[] and Γ_time. |
| **CC‑G12.8** | **Extension gating.** If any fields and pins governed by the extension appear, the corresponding `G.12:Ext.*` module is present and satisfied. | E.g., QD pins require `G.12:Ext.QDTelemetry`; maturity panel requires `G.12:Ext.MaturityLadderPanel`; SoTA palette hooks require `G.12:Ext.SoTAPalette`; pack inclusion requires `G.12:Ext.PackInclusion`. |

