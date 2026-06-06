---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph & Provenance Ledger"
section_id: "G.6:7"
section_title: "Conformance Checklist (normative) — CC‑G6"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__008_conformance-checklist-normative-cc-g6.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "G.6 — Evidence Graph & Provenance Ledger"
  - "G.6:7 — Conformance Checklist (normative) — CC‑G6"
line_start: 78401
line_end: 78421
dependencies:
  - "A.10"
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.18"
  - "E.5"
  - "E.5.2"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.7"
  - "G.8"
  - "G.9"
  - "G.Core"
  - "G.Core.TriggerAliasMap.G6"
keywords:
  - "CrossingBundle"
  - "EvidenceGraph"
  - "GateCrossing"
  - "PathId"
  - "PathSliceId"
  - "SCR/RSCR"
  - "TriggerAliasMap"
  - "UTS PathCard"
  - "lane tags (TA/VA/LA)"
  - "provenance"
  - "Γ-fold pinning"
---

### G.6:7 - Conformance Checklist (normative) — **CC‑G6**

| ConformanceId                                     | Requirement                                                                                                                                                                                                                                                                                                                                                                  | Purpose |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **CC‑G6‑CoreRef**                                 | `G.6` is conformant only if it satisfies the **effective** `CC‑GCORE‑*` set expanded from the `GCoreLinkageManifest` in **§4.1** (explicit crossings & pins, penalties→`R_eff` only, P2W split, typed RSCR trigger kinds, defaults with one governing definition, UTS discipline, Δ‑discipline).                                                                                                 | Cite core invariants |
| **CC‑G6‑1 (Anchor & lanes)**                      | Every citable path MUST resolve to A.10 anchors (SCR/RSCR addressable) and MUST declare lane tags (`TA/VA/LA`) on bindings.                                                                                                                                                                                                                                                | Ground auditability |
| **CC‑G6‑2 (No self‑evidence)**                    | Any evidencing `TransformerRole` that certifies the evaluated holon is external; reflexive cases MUST be modelled as a meta‑holon.                                                                                                                                                                                                                                         | Avoid reflexive evidence |
| **CC‑G6‑3 (Context/Plane & crossings)**           | Paths MUST declare `BoundedContext` and `ReferencePlane`, and MUST expose explicit crossing pins when crossings are present. *(Delegation target: `CC‑GCORE‑CROSS‑1`.)*                                                                                                                                                                                                    | Make crossings explicit |
| **CC‑G6‑4 (Penalty routing)**                     | Any crossing/plane penalty wiring visible in G.6 artefacts MUST route penalties to `R_eff` only and MUST preserve `F/G` invariance under penalties. *(Delegation target: `CC‑GCORE‑PEN‑1`.)*                                                                                                                                                                             | Preserve lane purity |
| **CC‑G6‑5 (Γ‑fold discipline + Default Governing Definition Index)** | If a `Γ‑fold` is not explicitly overridden by pinned CAL artefacts, G.6 MUST cite the governing definition of `DefaultId.GammaFoldForR_eff` rather than asserting a local default. If a `Γ‑fold` is explicitly overridden, the path/SCR surface MUST cite the relevant CAL `ProofLedger` ids and publish the override as an auditable pin (not as prose). *(Delegation: `CC‑GCORE‑DEF‑1`; override semantics governed by `G.4`.)* | Keep folding auditable |
| **CC‑G6‑6 (Time/decay/validity binding)**         | Empirical legs MUST expose freshness/time binding (window selector or policy pin) and MUST support an explicit `validUntil`/expiry marker when one is declared (or an equivalent decay/freshness policy pin that implies expiry). Expiry/decay MUST be representable as refresh/RSCR‑relevant change using typed canonical causes. *(Delegation intent: typed causes are governed by G.Core; see `CC‑GCORE‑TRIG‑*`.)*                                  | Enable refresh readiness |
| **CC‑G6‑7 (DesignRunTag split)**                    | Design‑time method descriptions and run‑time work traces MUST NOT be fused into one undifferentiated node; the graph MUST preserve the design↔run boundary via explicit carriers/bridges. *(Delegation intent: P2W split is governed by G.Core; see `CC‑GCORE‑P2W‑1`.)*                                                                                                            | Preserve P2W boundary |
| **CC‑G6‑8 (SCR projection completeness)**         | For any cited `PathId/PathSliceId`, the Assurance SCR view MUST expose at least: lane split, scope/plane pins, freshness/validity binding, explicit crossing pins (and the effective bottleneck `CL`/`CL^k`/`CL^plane` when crossings exist), the effective `Γ‑fold` in force for any `R_eff` folding (default or override, plus CAL `ProofLedger` ids when overridden), and links to contributing A.10 anchors and any CAL evidence/profile refs. | Make decisions auditable |
| **CC‑G6‑9 (Citable PathIds)**                     | Any SoS‑LOG admit/degrade/abstain decision or maturity rung transition that relies on provenance MUST cite `PathId`(s) (or `PathSliceId`(s) when snapshot‑binding is required).                                                                                                                                                                                            | Decision traceability |
| **CC‑G6‑10 (SpanUnion justification note)**       | If a SpanUnion/non‑interaction claim is made across evidence lines, an explicit independence justification MUST be published (as an addressable artefact linked to the path).                                                                                                                                                                                                | Non‑interaction audit |
| **CC‑G6‑11 (UTS hooks)**                          | Evidence carriers and paths minted for citation MUST be UTS‑citable with twin labels and edition pins. *(Delegation target: `CC‑GCORE‑UTS‑1`.)*                                                                                                                                                                                                                           | Stable citations |
| **CC‑G6‑12 (IndependenceCertificate)**            | Independence for SpanUnion claims MUST be carried by an `IndependenceCertificate` (per the relevant certificate pattern) and referenced from SCR/paths.                                                                                                                                                                                                                    | Certificate surface |
| **CC‑G6‑13 (Mandatory provenance pins)**          | Any published/cited path surface MUST expose: `EvidenceGraphId`, `PathId/PathSliceId`, lane split, scope/plane pins, freshness/validity pins when applicable, crossing pins when applicable, and the minimal pin set required by §4.1. When `R_eff` folding is published/relied upon, the effective `Γ‑fold` in force MUST be exposed (default or override, plus CAL `ProofLedger` ids when overridden). When QD/OEE telemetry pins are in use, the extension‑required edition/policy pins MUST also be exposed. | Pin completeness |
| **CC‑G6‑14 (Legality binding; no shadow specs)**  | If numeric operations are cited/used in a path, legality MUST be pinned/cited via `CG‑Spec` rather than asserted locally, and the path/SCR surface MUST fail fast on illegal arithmetic/typing (e.g., CSLC/scale violations); do not “promote” ordinal to cardinal by convention inside G.6. *(Delegation target for “no shadow specs”: `CC‑GCORE‑CN‑CG‑1`.)*                                                                                     | Prevent illicit arithmetic |
| **CC‑G6‑15 (Conditional: QD/OEE telemetry pins)** | *(Conditional)* If `G.6:Ext.QD_OEE_TelemetryPins` is used, the required edition/policy pins from that extension (at minimum `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and the relevant insertion/emitter/transfer policy pins when applicable) MUST be recorded for reproducibility and must participate in RSCR triggering using canonical trigger kind ids.                                                                 | Reproducible archive/OEE |

