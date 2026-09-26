---
chunk_kind: "child"
pattern_id: "G.7"
pattern_title: "Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
section_id: "G.7:7"
section_title: "Conformance Checklist (normative) — CC‑G7"
source_path: "FPF-Spec.md"
output_path: "by_section/G.7/G.7__008_conformance-checklist-normative-cc-g7.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "G.7 — Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)"
  - "G.7:7 — Conformance Checklist (normative) — CC‑G7"
line_start: 114471
line_end: 114490
dependencies:
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.21"
  - "C.23"
  - "C.3.3"
  - "E.10"
  - "E.18"
  - "F.17"
  - "F.3"
  - "F.7"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.12"
  - "G.2"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.9"
  - "G.Core"
keywords:
  - "BridgeCalibrationTable (BCT)"
  - "BridgeCard"
  - "BridgeSentinel"
  - "Congruence Level (CL/CL^k/CL^plane)"
  - "GateCrossing"
  - "PathSliceId"
  - "RSCRTriggerKindId"
  - "ReferencePlane"
  - "RegressionSet"
  - "SentinelSet"
  - "UTS"
  - "bridge calibration"
  - "loss notes"
  - "waivers"
  - "Φ(CL)/Ψ(CL^k)/Φ_plane policy pins"
---

### G.7:7 - Conformance Checklist (normative) — **CC‑G7**

| ConformanceId             | Requirement                                                                                                                                                                                                                                                                               | Purpose                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **CC‑G7‑CoreRef**         | `G.7` is conformant only if it satisfies the effective `G.Core` obligations declared by the `GCoreLinkageManifest` in **§4.1** (after nil‑elision and expansion of profile/set/pinset ids), including any explicit deltas listed there. | Make universal invariants one governing definition and enforce citation‑based reuse.       |
| **CC‑G7‑BCT‑1** | An active calibration kit has a BCT with its freshness basis, exact row scope, relation/card references, calibration basis and applicable evidence, regression and sentinel references. Channel summaries and policy/plane pins are present only under their declared calibration or receiving-use conditions. | Make the calibration and its use independently recoverable. |
| **CC‑G7‑BridgeCard‑1** | An F.9 BridgeCard resolves its exact F.17 endpoint senses and relation profile. A kind-channel assertion follows C.3.3 and cites its exact kind endpoints; a plane claim cites its own governor. Keep the channels distinct. | Preserve the subject of each correspondence. |
| **CC‑G7‑UTS‑1** | When G.7 mints or publishes a public identifier, apply CC-GCORE-UTS-1 and expose the resulting UTS rows in the consuming BCT/Ledger or crossing bundle. Include a BridgeCard or GateCrossing row only when that actual object is used; a kind-only calibration creates no F.9 BridgeCard. | Make public names citable without inventing relations. |
| **CC‑G7‑RowScope‑1**      | Every BCT row **MUST** declare its `RowScopeId` (which correspondence or difference is being calibrated), and any loss notes **MUST** be recorded as citable artefacts (refs/ids), not only narrative text.                                                                                                 | Keep reuse honest and locally bounded.                                         |
| **CC‑G7‑CLRegime‑1** | Every reported CL summary satisfies §4.2.1's calibration meaning and aggregation conditions. Actual losses, counterexamples and required search/absence disclosures remain citable. The receiving use has its own rule, tolerance and reliance; a threshold or waiver cites its policy use, justification, authority and additional premises. | Calibration evidence supplies no automatic permission or receiving classification. |
| **CC‑G7‑SCRLinkage‑1** | A calibration cited in SCR/Evidence surfaces MUST identify its exact sense, kind or plane correspondence, row locator and `{BCT.id, RegressionSetId}`. Add BridgeCard/UTS anchors for the actual F.9/public-name use and policy/model pins for the actual reliance, numerical loss or assurance calculation. | Preserve the evidence consumed by the claim without fabricating another channel. |
| **CC‑G7‑SoSLOG‑Pins‑1**   | When `G.7:Ext.SoSLogClauses` is in use, G.7 outputs **MUST** expose the cited SoS‑LOG rule ids and the relevant `PathId/PathSliceId` evidence citations; any change in those pins **MUST** be RSCR‑relevant per `CC‑GCORE‑TRIG‑1…TRIG‑4`.                                               | Keep cross‑Tradition reuse explainable without embedding C.23 semantics.        |
| **CC‑G7‑Acceptance‑1**    | When `G.7:Ext.AcceptanceHooks` is in use, G.7 outputs **MUST** expose the Acceptance clause ids/policy ids used as gates; thresholds/unknown handling remain governed by Acceptance; any change **MUST** be RSCR‑relevant per `CC‑GCORE‑TRIG‑1…TRIG‑4`.                                           | Keep thresholds and unknowns out of bridges while preserving auditability.     |
| **CC‑G7‑RowBottleneck‑1** | A minimum summarizes only a non-empty cell set sharing the declared ordinal scale and calibration question. Keep the constituent evidence and losses; otherwise report separate results or the gap. | Avoid averaging ordinal evidence or treating its minimum as a use decision. |
| **CC‑G7‑PolicyPins‑1**    | G.7 outputs **MUST** publish the *policy id pins* required to audit penalty routing and plane effects (ids only), as required by `CC‑GCORE‑LINK‑1/2` and `CC‑GCORE‑PEN‑1`. G.7 MUST NOT duplicate policy tables or redefine penalty semantics.                                           | Keep penalty routing auditable while preserving single‑governing-pattern policy semantics. |
| **CC‑G7‑GateCrossing‑1** | An independently governed E.18 flow crossing or A.21 gate that consumes calibration MUST retain its required harness, pins, lexical constraints and lane checks. A calibration relation alone is not that flow crossing or gate. | Make actual crossings and gates checkable. |
| **CC‑G7‑Sentinels‑1**     | G.7 **MUST** register `BridgeSentinel` entries for bridges used by live scopes and **MUST** emit typed RSCR triggers (canonical `RSCRTriggerKindId`; see `CC‑GCORE‑TRIG‑1…TRIG‑4`) on calibration‑relevant edits, scoped to the watched `PathSliceId[]` or `PatternScopeId[]`, with the minimum payload pins from §4.1. | Enable targeted refresh rather than pack‑wide reruns.                          |
| **CC‑G7‑QD‑Pins‑1**       | When `G.7:Ext.QDParityPins` is in use, G.7 outputs **MUST** include `{DescriptorMapRef.edition, DistanceDefRef.edition, InsertionPolicyRef}` and treat any change to those pins as RSCR‑relevant per `CC‑GCORE‑TRIG‑1…TRIG‑4`.                                                          | Prevent silent QD telemetry drift.                                             |
| **CC‑G7‑DHC‑Units‑1** | When AlignmentDensity is reported, G.7 outputs **MUST** count the exact obtaining directed F.9 relations in the declared F.17 cell set under C.21, include the declared units, and cite the active DHC method and replay basis. Related DHC accounts use their own exact C.21 definitions. CL labels grant no substitution and do not redefine the counted relation set; G.7 MUST NOT invent arithmetic over ordinal or otherwise inadmissible surfaces. | Keep dashboards and discipline-health readings faithful to their measurement definitions and bounded-use claims. |

