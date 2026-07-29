---
chunk_kind: "child"
pattern_id: "G.10"
pattern_title: "SoTA Pack Shipping"
section_id: "G.10:8"
section_title: "Conformance checklist (CC‑G10)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.10/G.10__009_conformance-checklist-cc-g10.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "G.10 — SoTA Pack Shipping"
  - "G.10:8 — Conformance checklist (CC‑G10)"
line_start: 100549
line_end: 100566
dependencies:
  - "A.10"
  - "A.15.3"
  - "C.18"
  - "E.18"
  - "E.5.2"
  - "F.17-F.18"
  - "G.11"
  - "G.12"
  - "G.12-G.13"
  - "G.13"
  - "G.2"
  - "G.2-G.9"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "AuditPins"
  - "CrossingBundle"
  - "MOOManifest"
  - "PathId/PathSliceId"
  - "PortfolioRosterId"
  - "RSCR wiring"
  - "SoTA-Pack(Core)"
  - "UTS publication"
  - "edition pins"
  - "no semantic respecification"
  - "notation-independent pack"
  - "pack-boundary governing definition"
  - "parity pins"
  - "selector-ready publication surface"
  - "shipping"
  - "telemetry pins"
---

### G.10:8 - Conformance checklist (CC‑G10)

This pattern inherits order/illumination, evidence, and bridge/penalty legality from the cited governing patterns (not restated here). Shipping‑specific requirements:

| ID  | Statement   | Verification notes (conceptual)  |
| --- | ----------- | -------------------------------- |
| **CC‑G10‑CoreRef** | The pattern satisfies the **effective** `G.Core` obligations declared by `G.10:4.1` (after profile/set/pin‑set expansion under `Nil‑elision`). | Check that the linkage manifest is present and that the expanded obligations are not contradicted. |
| **CC‑G10.1 (Notation‑independent).** | The pack MUST NOT rely on any specific file syntax; cards/tables are conceptual; tool serialisations are informative only. | Look for format‑free conceptual fields; any serialisation is explicitly non‑normative. |
| **CC‑G10.2 (Pack parity pins).** | If QD/OEE fields are present, pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, (optional) `DHCMethodRef.edition` / `DHCMethodSpecRef.edition` when used, and (OEE) `TransferRulesRef.edition`; include `CharacteristicSpaceRef` (+ `CharacteristicSpaceRef.edition` when it affects partitioning reproducibility); for QD archive semantics also pin `EmitterPolicyRef` and `InsertionPolicyRef`. | Verify the corresponding `G.10:Ext.*` block is present and the pins appear in AuditPins and (when relevant) in telemetry pins. |
| **CC‑G10.3 (Telemetry discipline).** | Any illumination increase or archive edit SHALL log `PathSliceId`, the active `policy‑id`, the active editions of the pinned `…Ref` fields (incl. OEE `TransferRulesRef.edition`), and the active `EmitterPolicyRef`/`InsertionPolicyRef` when applicable. | Verify emitted telemetry is PathSlice‑keyed and carries the required pins; ensure causes are recorded using canonical trigger kinds (alias labels optional only). |
| **CC‑G10.4 (UTS publication & twins).** | All shipped heads appear on UTS with Tech/Plain twins **per delegated UTS discipline**; cross‑Context identity (when present) is routed via Bridges with CL and loss notes **per delegated crossing discipline**. | Verify UTS rows exist and that any cross‑Context identity is routed via Bridge artefacts with visible CL/loss notes. |
| **CC‑G10.5 (MOO surfaced in shipping).** | For every declared selector set-result or archive published, the pack SHALL list the applicable generation/parity mechanism ids (e.g., QD `EmitterPolicyRef`/`InsertionPolicyRef`, parity harness ids, method refs where the method definition is generative) and the active policy‑id(s) in SCR‑visible bindings and telemetry pins (ids only; governing-definition delegating). | Verify `MOOManifestId` is present when outcomes are intended for downstream use and does not redefine semantics. |
| **CC‑G10.6 (Pack completeness as a citation surface).** | The pack cites all included upstream artefacts by id/ref and exposes the required pins (`AuditPins`, UTS/Path pins, CrossingBundleIds when required). | Verify all present payload artefacts have ids and the pins needed to cite/replay them. |
| **CC‑G10.7 (CrossingBundle exposure).** | For each GateCrossing relevant to shipped artefacts, the pack exposes the relevant `CrossingBundleIds` (or records that no such crossings exist) **per delegated crossing visibility discipline**, and shipping fails fast on missing/non‑conformant crossing bundles when required. | Verify crossing bundle presence/absence is honest and aligned with the shipped artefacts’ declared crossings. |
| **CC‑G10.8 (Baseline binding is explicit when used).** | If the shipped pack claims a planned baseline, `PlanItemRefs := SlotFillingsPlanItemRef[]` are present (WorkPlanning plan items, cited; no execution logs). | Verify plan items are cited by id and the pack does not treat decision records or execution logs as authoritative plan items. |
| **CC‑G10.9 (Extension‑scoped pin declaration).** | If QD/OEE/interop fields are present, the corresponding `GPatternExtension` block is present and its required pins/editions/policies are recorded in AuditPins and in emitted telemetry pins when those pins affect refreshability. | Verify conditional extension pins are not silently omitted when the mode is used. |
| **CC‑G10.10 (Derived tradition-view shipping).** | If the visible shipped surface or shortlisted source is one derived tradition view such as `TraditionFront` or `TraditionArchive`, the pack **MUST** publish the declared `sourceSetFamily`, keep `basePaletteRef=SoTAPaletteDescriptionId` recoverable, and carry the derivation basis (`derivedViewKind`, declared `Q`, or reachability/coverage rule id) with enough explicitness that the visible surface cannot be mistaken for the default palette semantics. | Verify derived tradition views are shipped as derived views, not as silent redefinitions of the base palette. |

