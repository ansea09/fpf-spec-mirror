---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph & Provenance Ledger"
section_id: "G.6:7.5"
section_title: "Interfaces & Hooks (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__009_interfaces-hooks-normative.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "G.6 — Evidence Graph & Provenance Ledger"
  - "G.6:7.5 — Interfaces & Hooks (normative)"
line_start: 82542
line_end: 82632
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

### G.6:7.5 - Interfaces & Hooks (normative)

Each hook below defines: **Trigger → Obligation → Publishes/Consumes → Invariants**.
Where universal invariants apply (crossings, penalties, trigger typing), this section *cites* `G.Core` rather than redefining semantics.

#### G.6:7.5.1 - H1 — UTS Name Card for EvidenceGraph Nodes

* **Trigger.** A new EvidenceGraph node is minted for an A.10-anchored evidence carrier or evidence role.
* **Obligation.** Mint a UTS Name Card with twin labels (Tech/Plain), citing the declared bounded-context anchor and any required edition pins.
* **Publishes/Consumes.** Publishes: UTS row. Consumes: A.10 anchor metadata.
* **Invariants.** UTS publication and any deprecation/aliasing follow the delegated UTS discipline through `G.Core` and `F.17`.

#### G.6:7.5.2 - H2 — UTS PathCard (PathId/PathSliceId)

* **Trigger.** A new `PathId` (or `PathSliceId`) is minted.
* **Obligation.** Publish a UTS PathCard with twin labels, listing the explicit pins required by §4.1 (context, plane, and time binding, crossing pins if any). If an extension requires additional pins for reproducibility (e.g., `G.6:Ext.QD_OEE_TelemetryPins`), those pins MUST be present when the extension is in use.
* **Publishes/Consumes.** Publishes: UTS row(s). Consumes: EvidenceGraph path metadata + any extension‑required pins.
* **Invariants.** Crossing visibility and penalty routing are delegated to `G.Core` (`CC‑GCORE‑CROSS‑1`, `CC‑GCORE‑PEN‑1`).

#### G.6:7.5.3 - H3 — RSCR Trigger on Evidence‑Impacting Edit (typed; alias‑dockable)

* **Trigger.** Any edit in G.6 that can change a path’s audit‑relevant surface (evidence structure, crossing pins, penalty policy pins, plane binding, freshness binding, edition/policy pins, or telemetry‑bound fields).
* **Obligation.** Emit RSCR triggers **using canonical `RSCRTriggerKindId`** (from `G.Core`) and record affected scope (`PathId/PathSliceId`) plus payload pins required for downstream refresh. If a deprecated `G.6:H3:*` label is recorded, it is recorded as an alias label and docked via `G.Core.TriggerAliasMap.G6`. When `G.6:Ext.BridgeSentinelWiring` is used, include the bridge/sentinel payload pins required by that extension.
* **Publishes/Consumes.** Publishes: RSCR triggers and any associated RSCR test ids. Consumes: relevant pins/refs and CAL artefact references where applicable.
* **Invariants.** Trigger typing and alias docking are delegated to `G.Core` (`CC‑GCORE‑TRIG‑*`). Penalty routing invariants are delegated (`CC‑GCORE‑PEN‑1`).

#### G.6:7.5.4 - H4 — SoS‑LOG Path Citation (selector explainability)

* **Trigger.** A SoS‑LOG rule yields a tri‑state decision for a selection‑relevant pair (e.g., `(TaskSignature, MethodFamily)`), and the decision is justified by evidence.
* **Obligation.** The branch record MUST cite the relevant `PathId/PathSliceId`(s) and the minimal pins required to re‑audit the justification. Any method‑specific attribution fields are handled via Extensions (e.g., `G.6:Ext.SoSLOGPathCitationWiring` for `LensId`/FailureBehavior wiring, `G.6:Ext.BridgeSentinelWiring` for bridge‑monitoring payload pins when cross‑context reuse is invoked, `G.6:Ext.QD_OEE_TelemetryPins` for QD/OEE pins).
* **Publishes/Consumes.** Publishes: an SCR‑visible branch record with cited paths. Consumes: EvidenceGraph path queries.
* **Invariants.** Tri‑state semantics are governed by G.Core (`CC‑GCORE‑GUARD‑1`); G.6 does not add a new decision value.

#### G.6:7.5.5 - H5 — Maturity Rung Transition Justification

* **Trigger.** A maturity rung transition is proposed and justified by evidence.
* **Obligation.** The transition MUST cite one or more `PathId/PathSliceId`(s) and MUST publish an updated maturity entry with those citations. Missing path citations forbid rung advance.
* **Publishes/Consumes.** Publishes: updated UTS entry for maturity artefacts. Consumes: cited paths and A.10 anchors.
* **Invariants.** Any thresholding policy remains governed by CAL/LOG governing definitions; G.6 provides citation, not policy.

#### G.6:7.5.6 - H6 — Bridge/CL Edge Annotation (GateCrossings)

* **Trigger.** An EvidenceGraph edge traverses a declared GateCrossing boundary (context/kind/plane/design↔run/edition).
* **Obligation.** Publish a CrossingBundle‑checkable crossing record with explicit crossing pins (UTS row id, Bridge id/card id if applicable, CL regime pins if applicable, and plane pins if applicable).
* **Publishes/Consumes.** Publishes: crossing row/pins. Consumes: GateCrossing metadata and Bridge artefacts (when present).
* **Invariants.** Crossing visibility is governed by G.Core (`CC‑GCORE‑CROSS‑1`); penalties routing is governed by G.Core (`CC‑GCORE‑PEN‑1`).

#### G.6:7.5.7 - H7 — ReferencePlane penalty policy publication (ids only)

* **Trigger.** A path binds across different reference planes.
* **Obligation.** Publish the relevant policy identifiers (ids only; not tables) required to audit plane effects, alongside the path’s pins.
* **Publishes/Consumes.** Publishes: SCR/UTS fields containing policy ids. Consumes: the governing definition’s policy registries as cited publications or records (do not duplicate tables).
* **Invariants.** Penalty routing is delegated (`CC‑GCORE‑PEN‑1`); no shadow specs (`CC‑GCORE‑CN‑CG‑1`).

#### G.6:7.5.8 - H8 — CrossingBundle exposure (E.18)

* **Trigger.** G.6 artefacts are exported for release or consumed by downstream patterns that require GateCrossing checks.
* **Obligation.** Provide harness‑readable ids/pins so GateCrossing checks can verify: required crossing records exist, lexical constraints hold, and crossing pins are explicit.
* **Publishes/Consumes.** Publishes: checkable ids/pins. Consumes: GateCrossing + lexical rules.
* **Invariants.** Crossing discipline and ID continuity are governed by G.Core (`CC‑GCORE‑CROSS‑1`, `CC‑GCORE‑ID‑*`).

#### G.6:7.5.9 - H9 — SCR surface for assurance provenance

* **Trigger.** A downstream artefact cites a path for audit/selection/maturity.
* **Obligation.** Expose the required provenance fields in SCR views: lane split, context or plane pins, freshness binding, crossing pins (when present), and links to A.10 anchors and CAL refs.
* **Publishes/Consumes.** Publishes: SCR view(s). Consumes: EvidenceGraph paths and cited artefacts governed by cited patterns.
* **Invariants.** Each cited default resolves to its governing definition (`CC‑GCORE‑DEF‑1`).

#### G.6:7.5.10 - H10 — ProofLedger linkage (CAL ↔ G.6)

* **Trigger.** A proof obligation or evidence role is attached to a claim and is represented in G.4 artefacts.
* **Obligation.** Link EvidenceGraph nodes/edges to CAL ProofLedger/EvidenceProfiles entries and to A.10 carriers via the minimal provenance edge vocabulary.
* **Publishes/Consumes.** Publishes: CAL proof refs as pins in the path explanation surface. Consumes: CAL artefacts.
* **Invariants.** G.6 does not redefine CAL proof semantics; it only cites them.

#### G.6:7.5.11 - H11 — Telemetry ingest (selector & probe outcomes)

* **Trigger.** Run‑time outcomes (selection, probes, parity runs, measurement updates) produce observations that bear on previously asserted claims.
* **Obligation.** Ingest the observation as a run‑time evidence line (anchored in A.10), with explicit lane typing and explicit scope/time binding. If method‑specific telemetry pins are required, they are governed by Extensions (e.g., `G.6:Ext.QD_OEE_TelemetryPins`).
* **Publishes/Consumes.** Publishes: new EvidenceGraph nodes/edges + any required UTS rows + typed RSCR triggers when impacts occur. Consumes: run‑time carriers/attestations as conceptual anchors.
* **Invariants.** P2W split is respected (`CC‑GCORE‑P2W‑1`); typed trigger discipline is respected (`CC‑GCORE‑TRIG‑*`).

#### G.6:7.5.12 - Minimal conformance (hooks)

1. UTS publication for minted evidence artefacts and paths (H1–H2), per delegated UTS discipline.
2. Typed RSCR triggers on evidence‑impacting edits (H3) using canonical trigger kind ids.
3. LOG and maturity artefacts cite paths when evidence is used (H4–H5).
4. GateCrossing/crossing records are explicit and checkable when crossings occur (H6–H8).
5. SCR views expose the minimal provenance pins for cited paths (H9–H10).
6. Run‑time telemetry is ingested without collapsing design↔run boundaries (H11).

