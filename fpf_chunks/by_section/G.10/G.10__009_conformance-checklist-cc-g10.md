---
chunk_kind: "child"
pattern_id: "G.10"
pattern_title: "SoTA Pack Shipping"
section_id: "G.10:8"
section_title: "Conformance checklist (CC‑G10)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.10/G.10__009_conformance-checklist-cc-g10.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "G.10 — SoTA Pack Shipping"
  - "G.10:8 — Conformance checklist (CC‑G10)"
line_start: 141489
line_end: 141506
dependencies:
  - "A.10"
  - "A.15.3"
  - "C.18"
  - "C.21"
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

For order and illumination, evidence, and bridge or penalty legality, apply the cited governing patterns. The following requirements govern shipping.

| ID  | Statement   | Verification notes (conceptual)  |
| --- | ----------- | -------------------------------- |
| **CC‑G10‑CoreRef** | The pattern satisfies the **effective** `G.Core` obligations declared by `G.10:4.1` (after profile/set/pin‑set expansion under `Nil‑elision`). | Check that the linkage manifest is present and that the expanded obligations are not contradicted. |
| **CC‑G10.1 (Notation‑independent).** | The pack MUST NOT rely on any specific file syntax; cards/tables are conceptual; tool serialisations are informative only. | Look for format‑free conceptual fields; any serialisation is explicitly non‑normative. |
| **CC‑G10.2 (Pack parity pins).** | If QD archive fields are present, pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `EmitterPolicyRef` and `InsertionPolicyRef`. Include `CharacteristicSpaceRef` when archive partitioning is declared, with a separate `characteristicSpaceDescriptionRef: U.EpistemeRef` when the exact defining episteme affects reproducibility; resolve the pair under A.19:5.1.1.1. OEE fields pin `TransferRulesRef.edition` under their own extension. When a shipped field consumes a C.21 DHC coordinate, carry every active field of that coordinate's `DHCReplayBasis`. A non-QD generator use does not acquire QD descriptor or archive pins. | Verify the corresponding `G.10:Ext.*` block is present and the pins appear in AuditPins and (when relevant) in telemetry pins. |
| **CC‑G10.3 (Telemetry discipline).** | Any illumination increase or archive edit SHALL log `PathSliceId`, the active `policy‑id`, the active values designated by the pinned `…Ref` fields and the required episteme editions (including OEE `TransferRulesRef.edition`), and the active `EmitterPolicyRef`/`InsertionPolicyRef` when applicable. | Verify emitted telemetry is PathSlice‑keyed and carries the required pins; ensure causes are recorded using canonical trigger kinds (alias labels are optional). |
| **CC‑G10.4 (UTS publication & twins).** | Shipped heads use UTS Tech/Plain twins under the delegated publication rule. A shipped cross-context semantic-use claim cites its obtaining relation, separate bounded-use proposition and matching reliance; calibration summaries keep their evidence role. Kind and plane claims retain their own governors. | Verify the published names and exact relation/use evidence; a visible CL or policy pin alone is insufficient. |
| **CC‑G10.5 (MOO surfaced in shipping).** | For a published selector set-result or archive, the pack SHALL cite the grounds on which its members were selected or included. Identify the actual generation or parity methods, mechanisms, policies and editions where applicable (including QD `EmitterPolicyRef`/`InsertionPolicyRef` or harness ids), using SCR-visible bindings and telemetry pins. Mark missing grounds needed to replay an outcome. | Verify `MOOManifestId` is present for outcomes intended for downstream use. Use its references and stated limits to judge the replay that can be performed. Method semantics remain with their governing definitions. |
| **CC‑G10.6 (Pack completeness as a citation surface).** | The pack provides the sources and relations needed for the commissioned use, with the applicable ids and pins (`AuditPins`, UTS/Path pins, CrossingBundleIds when required). | Follow the receiving operation through what the reader can obtain from the shipment. A list of fully traceable payloads can still omit a premise or rule the recipient needs. For a replay-only commission, successful reconstruction from sufficient cited material meets this condition. When delivery to an audience is promised, establish its access to the issued edition. For an asserted receipt or use, establish what reached the recipient or how it was used. |
| **CC‑G10.7 (CrossingBundle exposure).** | If the shipped artefacts have relevant GateCrossings, expose the required `CrossingBundleIds` for each under the delegated crossing visibility rule. If there are none, record that fact. Stop shipping if a required bundle is missing or non-conformant. | Check the recorded presence or absence of bundles against the shipped artefacts’ declared crossings. |
| **CC‑G10.8 (Baseline binding is explicit when used).** | If the shipped pack claims a planned baseline, `PlanItemRefs := ⟨WorkPlanRef, planLocalContentLocator⟩[]` are present (exact WorkPlan plus plan-local content; no execution logs). | Verify the baseline resolves inside the cited WorkPlan; item and row designators have no independent identity, and decision records or execution logs do not replace the plan. |
| **CC‑G10.9 (Extension‑scoped pin declaration).** | If QD/OEE/interop fields are present, the corresponding `GPatternExtension` block is present and its required pins/editions/policies are recorded in AuditPins and in emitted telemetry pins when those pins affect refreshability. | For each mode used, check that its required extension pins are present. |
| **CC‑G10.10 (Derived tradition-view shipping).** | If the visible shipped surface or shortlisted source is one derived tradition view such as `TraditionFront` or `TraditionArchive`, the pack **MUST** publish the declared `sourceSetFamily`, keep `basePaletteRef=SoTAPaletteDescriptionId` recoverable, and carry the derivation basis (`derivedViewKind`, declared `Q`, or reachability/coverage rule id) so the reader can distinguish the visible derived view from its base palette. | Verify derived tradition views are shipped as derived views, not as silent redefinitions of the base palette. |

